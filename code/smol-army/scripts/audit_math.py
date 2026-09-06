"""Post-hoc audit of the math family result (NOT pre-registered; see CHANGES.md).

Trigger: the pre-registered analysis showed army_vote +18.3pp over frontier on
math — the only arm/family where the army beat the frontier outright. Rule
before interpreting a surprising win: audit the scorer and the data.

Findings this script reproduces:
1. All 49 frontier math misses are items math-100..149 (one GSM-Symbolic
   probability template) and every miss equals exactly 4x the gold answer with
   a % sign: gold reads "how much more likely (as a percentage)" as an
   absolute percentage-point difference; frontier answers the relative
   increase ((p1-p2)/p2). The base probability is 1/4 in every variant, so
   relative = 4x absolute. This is an ambiguous item, not a math error.
2. Excluding the ambiguous template: frontier 1.000, army_vote 0.977
   (-2.3pp, paired bootstrap 95% CI [-4.0, -0.7]), self_consistency 0.983.
   The pre-registered +18pp reverses sign.
3. The 150-item math set contains only ~3 template families (fog bank /
   remora / dice, 50 sequential variants each — fetch_data.py took the first
   150 rows). Effective sample size is far below 150; the pre-registered CI
   overstates certainty for this family.

Usage: uv run python scripts/audit_math.py
"""
import collections
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = {f"math-{i}" for i in range(100, 150)}  # ambiguous dice template


def main():
    rows = [json.loads(l) for l in (ROOT / "results" / "runs.jsonl").open()]
    math = [r for r in rows if r["family"] == "math"]
    items = {it["id"]: it for it in map(json.loads, (ROOT / "data" / "math.jsonl").open())}

    def acc(rs):
        return sum(r["score"] for r in rs) / len(rs) if rs else float("nan")

    print(f"{'arm':20s} {'all':>7s} {'clean':>7s} {'ambig':>7s}")
    for arm in ["frontier", "army_vote", "self_consistency"]:
        rs = [r for r in math if r["arm"] == arm]
        print(f"{arm:20s} {acc(rs):7.3f} "
              f"{acc([r for r in rs if r['item_id'] not in TEMPLATE]):7.3f} "
              f"{acc([r for r in rs if r['item_id'] in TEMPLATE]):7.3f}")

    wrong = [r for r in math if r["arm"] == "frontier" and r["score"] == 0]
    patt = sum(1 for r in wrong
               if (m := re.fullmatch(r"([\d.]+)%?", r["answer"].strip()))
               and abs(float(m.group(1)) - 4 * float(items[r["item_id"]]["answer"])) < 1e-6)
    print(f"\nfrontier misses: {len(wrong)}; exactly 4x-relative pattern: {patt}")

    random.seed(0)
    fr = {r["item_id"]: r["score"] for r in math
          if r["arm"] == "frontier" and r["item_id"] not in TEMPLATE}
    av = collections.defaultdict(list)
    for r in math:
        if r["arm"] == "army_vote" and r["item_id"] not in TEMPLATE:
            av[r["item_id"]].append(r["score"])
    diffs = [sum(av[i]) / len(av[i]) - fr[i] for i in sorted(fr)]
    boots = sorted(sum(random.choices(diffs, k=len(diffs))) / len(diffs)
                   for _ in range(10000))
    print(f"clean-only army_vote - frontier: {sum(diffs)/len(diffs):+.3f} "
          f"[{boots[249]:+.3f}, {boots[9749]:+.3f}]")

    def sig(p):
        s = re.sub(r"\b[A-Z][a-z]+\b", "NAME", p.split("Think step")[0])
        return re.sub(r"\d+", "N", s).strip()

    fams = collections.Counter(sig(it["prompt"]) for it in items.values())
    print(f"\n{len(items)} items span {len(fams)} literal templates "
          f"(top counts: {[c for _, c in fams.most_common(5)]})")


if __name__ == "__main__":
    main()
