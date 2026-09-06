"""The two-hour naive demo (book: Start Here). NOT part of the registered analysis.

Deliberately naive on purpose: 20 code items, one small model vs the frontier,
single call each, no seeds/repeats/CI/cost ledger discipline — the comparison a
reader would throw together in an afternoon. The book then lists every reason
this number cannot be trusted; the registered five-arm run is the repaired
version. Results go to results/demo_naive.jsonl (kept out of runs.jsonl).

Usage: set -a && source ../../.env && set +a && uv run python scripts/demo_naive.py
"""
import json
import tomllib
from pathlib import Path

from smol_army import tasks
from smol_army.llm import LLM

ROOT = Path(__file__).resolve().parents[1]

N = 20


def main():
    cfg = tomllib.loads((ROOT / "config" / "run.toml").read_text())
    items = tasks.load_family("code", N)
    out = ROOT / "results" / "demo_naive.jsonl"
    rows = []
    for name in ["gptoss", "frontier"]:
        m = cfg["models"][name]
        llm = LLM(m["id"], m["base_url"], m["key_env"],
                  max_tokens=m.get("max_tokens", 4096),
                  reasoning=m.get("reasoning", False))
        for it in items:
            text, usage = llm.chat([{"role": "user", "content": it["prompt"]}], seed=0)
            score = tasks.score("code", tasks.extract_code(text), it)
            rows.append({"model": name, "item_id": it["id"], "score": score,
                         "usage": usage})
            print(f"{name} {it['id']} score={score}")
    out.write_text("".join(json.dumps(r) + "\n" for r in rows))
    for name in ["gptoss", "frontier"]:
        sub = [r for r in rows if r["model"] == name]
        print(f"{name}: {sum(r['score'] for r in sub)}/{len(sub)}")


if __name__ == "__main__":
    main()
