"""Recompute scores in results/runs.jsonl from stored answers (scorer fixes).

A None answer is a legitimate zero (model produced no parseable answer) and is
kept. --drop-null deletes those rows instead so a resumed run regenerates them —
use ONLY to purge rows produced under a broken decoding config, never to retry
honest failures.
"""
import json
import sys
from pathlib import Path

from smol_army import tasks

ROOT = Path(__file__).resolve().parents[1]


def main():
    drop_null = "--drop-null" in sys.argv
    path = ROOT / "results" / "runs.jsonl"
    items = {}
    for fam in ("math", "mmlu_pro", "code"):
        for it in tasks.load_family(fam, 10**9):
            items[(fam, it["id"])] = it
    kept, dropped, changed = [], 0, 0
    for line in path.read_text().splitlines():
        r = json.loads(line)
        if r["answer"] is None:
            if drop_null:
                dropped += 1
                continue
            kept.append(r)
            continue
        new = tasks.score(r["family"], r["answer"], items[(r["family"], r["item_id"])])
        changed += new != r["score"]
        r["score"] = new
        kept.append(r)
    path.write_text("".join(json.dumps(r) + "\n" for r in kept))
    print(f"kept {len(kept)}, rescored-changed {changed}, dropped-null {dropped}")


if __name__ == "__main__":
    main()
