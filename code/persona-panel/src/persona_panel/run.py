"""Interview every persona on every question x variant. Resumable, cost-capped."""
import argparse
import json
import threading
import tomllib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import interview, personas
from .ledger import BudgetExceeded, Ledger
from .llm import LLM, MockLLM

write_lock = threading.Lock()

ROOT = Path(__file__).resolve().parents[2]
VARIANTS = ["original", "p1", "p2"]


def load_toml(name):
    return tomllib.loads((ROOT / "config" / name).read_text())


def done_keys(path):
    if not path.exists():
        return set()
    return {(e["subgroup"], e["persona"], e["qid"], e["variant"])
            for e in map(json.loads, path.read_text().splitlines())}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mock", action="store_true")
    args = ap.parse_args()

    cfg = load_toml("run.toml")
    questions = load_toml("questions.toml")["questions"]
    # Mock runs never touch the real results (which ship with the author's run).
    results_dir = ROOT / ("results_mock" if args.mock else "results")
    results_dir.mkdir(exist_ok=True)
    results_path = results_dir / "answers.jsonl"
    ledger = Ledger(results_dir / "ledger.jsonl", load_toml("prices.toml"),
                    cfg["budget_cap_usd"])
    done = done_keys(results_path)

    m = cfg["models"][cfg["active_model"]]
    llm = MockLLM() if args.mock else LLM(
        m["id"], m["base_url"], m["key_env"],
        max_tokens=m.get("max_tokens", 1024), reasoning=m.get("reasoning", False))

    jobs = []
    for sg in cfg["subgroups"]:
        for i in range(cfg["personas_per_subgroup"]):
            card = personas.make_card(sg, i)
            jobs += [(sg, i, card, q, variant) for q in questions for variant in VARIANTS
                     if (sg["name"], i, q["id"], variant) not in done]

    failed = []

    def work(job):
        sg, i, card, q, variant = job
        qtext = q["text"] if variant == "original" else q[variant]
        prompt = interview.render(card, qtext, q["options"])
        try:
            text, usage = llm.chat([{"role": "user", "content": prompt}], seed=i)
        except BudgetExceeded:
            raise
        except Exception as e:
            # One bad call must not kill the run; resume regenerates it.
            with write_lock:
                failed.append((sg["name"], i, q["id"], variant, repr(e)))
            return
        usd = ledger.record(llm.model, usage, subgroup=sg["name"],
                            persona=i, qid=q["id"], variant=variant)
        answer = interview.extract_option(text, {c for c, _ in q["options"]})
        with write_lock, results_path.open("a") as f:
            f.write(json.dumps({"subgroup": sg["name"], "persona": i,
                                "qid": q["id"], "variant": variant,
                                "answer": answer, "usd": usd}) + "\n")
            if (n := sum(1 for _ in open(results_path))) % 500 == 0:
                print(f"{n} answers, ledger ${ledger.spent:.2f}")

    with ThreadPoolExecutor(max_workers=1 if args.mock else 8) as ex:
        list(ex.map(work, jobs))
    for f_ in failed:
        print("FAILED", *f_)
    print(f"done: {len(jobs) - len(failed)}/{len(jobs)} jobs, "
          f"{len(failed)} failed (rerun to retry), ledger ${ledger.spent:.2f}")


if __name__ == "__main__":
    main()
