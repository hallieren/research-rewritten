"""Run the pre-registered evaluation. Resumable; every call passes the cost ledger."""
import argparse
import json
import threading
import tomllib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

write_lock = threading.Lock()

from . import tasks, topologies
from .ledger import BudgetExceeded, Ledger
from .llm import LLM, MockLLM

ROOT = Path(__file__).resolve().parents[2]


def load_toml(name):
    return tomllib.loads((ROOT / "config" / name).read_text())


def done_keys(results_path):
    if not results_path.exists():
        return set()
    return {(e["family"], e["item_id"], e["arm"], e["seed"])
            for e in map(json.loads, results_path.read_text().splitlines())}


def run_item(llms, ledger, item, arm_cfg, family, seed):
    spent = []

    def ask(prompt):
        llm = llms[len(spent) % len(llms)]  # round-robin across the team
        text, usage = llm.chat([{"role": "user", "content": prompt}],
                               seed=seed * 1000 + len(spent))
        spent.append(ledger.record(llm.model, usage, family=family,
                                   item=item["id"], arm=arm_cfg["name"], seed=seed))
        return text

    extract = tasks.extract_code if family == "code" else tasks.extract_answer
    kind = arm_cfg["kind"]
    if kind == "single":
        answer = extract(ask(item["prompt"]))
    elif kind == "vote":
        answer = topologies.run_vote(ask, extract, item["prompt"], arm_cfg["k"])
    elif kind == "debate":
        answer = topologies.run_debate(ask, extract, item["prompt"])
    else:
        answer = topologies.run_division(ask, extract, item["prompt"])
    return answer, tasks.score(family, answer, item), round(sum(spent), 8)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mock", action="store_true", help="offline: MockLLM, no network")
    ap.add_argument("--limit", type=int, help="cap items per family (pilot runs)")
    args = ap.parse_args()

    cfg = load_toml("run.toml")
    prices = load_toml("prices.toml")
    # Mock runs never touch the real results (which ship with the author's run).
    results_dir = ROOT / ("results_mock" if args.mock else "results")
    results_dir.mkdir(exist_ok=True)
    results_path = results_dir / "runs.jsonl"
    ledger = Ledger(results_dir / "ledger.jsonl", prices, cfg["budget_cap_usd"])
    done = done_keys(results_path)

    jobs = []
    for fam_cfg in cfg["families"]:
        family = fam_cfg["name"]
        try:
            items = tasks.load_family(family, min(fam_cfg["limit"], args.limit or 10**9))
        except FileNotFoundError:
            print(f"skip {family}: no data file")
            continue
        for arm_cfg in cfg["arms"]:
            arm_items = items[:arm_cfg["limit"]] if "limit" in arm_cfg else items
            llms = [MockLLM()] if args.mock else [
                LLM(cfg["models"][m]["id"], cfg["models"][m]["base_url"],
                    cfg["models"][m]["key_env"], temperature=arm_cfg["temperature"],
                    max_tokens=cfg["models"][m].get("max_tokens", 1024),
                    reasoning=cfg["models"][m].get("reasoning", False))
                for m in arm_cfg["models"]]
            jobs += [(llms, arm_cfg, family, seed, item)
                     for seed in range(arm_cfg["seeds"]) for item in arm_items
                     if (family, item["id"], arm_cfg["name"], seed) not in done]

    failed = []

    def work(job):
        llms, arm_cfg, family, seed, item = job
        try:
            answer, score, usd = run_item(llms, ledger, item, arm_cfg, family, seed)
        except BudgetExceeded:
            raise
        except Exception as e:
            # One bad item must not kill the run; resume regenerates it.
            with write_lock:
                failed.append((family, arm_cfg["name"], item["id"], repr(e)))
            return
        with write_lock, results_path.open("a") as f:
            f.write(json.dumps({"family": family, "item_id": item["id"],
                                "arm": arm_cfg["name"], "seed": seed,
                                "answer": answer, "score": score,
                                "usd": usd}) + "\n")
            if (n := sum(1 for _ in open(results_path))) % 100 == 0:
                print(f"{n} results, ledger ${ledger.spent:.2f}")

    with ThreadPoolExecutor(max_workers=1 if args.mock else 32) as ex:
        list(ex.map(work, jobs))
    for f_ in failed:
        print("FAILED", *f_)
    print(f"done: {len(jobs) - len(failed)}/{len(jobs)} jobs, "
          f"{len(failed)} failed (rerun to retry), ledger ${ledger.spent:.2f}")


if __name__ == "__main__":
    main()
