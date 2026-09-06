"""Fetch task slices via the HF datasets-server API into data/*.jsonl."""
import json
import random
from pathlib import Path

import httpx

DATA = Path(__file__).resolve().parents[1] / "data"
API = "https://datasets-server.huggingface.co/rows"

MATH_SUFFIX = ("\n\nThink step by step, then give the final answer on its own "
               "last line as: ANSWER: <number>")
CHOICE_SUFFIX = ("\n\nThink step by step, then give the final answer on its own "
                 "last line as: ANSWER: <letter>")
CODE_SUFFIX = "\n\nReturn the complete implementation as a single ```python code block."


def rows(dataset, config, split, n):
    out, offset = [], 0
    while len(out) < n:
        r = httpx.get(API, params={"dataset": dataset, "config": config, "split": split,
                                   "offset": offset, "length": min(100, n - len(out))},
                      timeout=60)
        r.raise_for_status()
        batch = r.json()["rows"]
        if not batch:
            break
        out += [b["row"] for b in batch]
        offset += len(batch)
    return out[:n]


def fetch_math(n=150):
    items = []
    for i, r in enumerate(rows("apple/GSM-Symbolic", "main", "test", n)):
        gold = r["answer"].split("####")[-1].strip()
        items.append({"id": f"math-{i}", "family": "math",
                      "prompt": r["question"] + MATH_SUFFIX, "answer": gold})
    return items


def fetch_mmlu_pro(n=150):
    pool = rows("TIGER-Lab/MMLU-Pro", "default", "test", 2000)
    by_cat = {}
    for r in pool:
        by_cat.setdefault(r["category"], []).append(r)
    rng = random.Random(0)
    for rs in by_cat.values():
        rng.shuffle(rs)
    picked = []
    while len(picked) < n and any(by_cat.values()):
        for cat in sorted(by_cat):
            if by_cat[cat] and len(picked) < n:
                picked.append(by_cat[cat].pop())
    letters = "ABCDEFGHIJ"
    items = []
    for r in picked:
        opts = "\n".join(f"{letters[j]}. {o}" for j, o in enumerate(r["options"]))
        items.append({"id": f"mmlu-{r['question_id']}", "family": "mmlu_pro",
                      "prompt": f"{r['question']}\n\n{opts}" + CHOICE_SUFFIX,
                      "answer": r["answer"]})
    return items


def fetch_code(n=100):
    items = []
    for r in rows("evalplus/humanevalplus", "default", "test", n):
        items.append({"id": r["task_id"], "family": "code",
                      "prompt": ("Complete this Python function.\n\n```python\n"
                                 + r["prompt"] + "\n```" + CODE_SUFFIX),
                      "answer": "",
                      "tests": r["test"] + f"\n\ncheck({r['entry_point']})"})
    return items


def main():
    DATA.mkdir(exist_ok=True)
    for name, fetch in [("math", fetch_math), ("mmlu_pro", fetch_mmlu_pro),
                        ("code", fetch_code)]:
        items = fetch()
        with (DATA / f"{name}.jsonl").open("w") as f:
            for it in items:
                f.write(json.dumps(it) + "\n")
        print(f"{name}: {len(items)} items")


if __name__ == "__main__":
    main()
