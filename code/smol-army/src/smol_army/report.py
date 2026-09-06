"""Aggregate results/runs.jsonl into results/report.md + results/results.csv."""
import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

from .stats import paired_bootstrap, verdict

ROOT = Path(__file__).resolve().parents[2]
ARMY_ARMS = ["army_vote", "self_consistency", "army_debate", "army_division"]


def aggregate(runs):
    groups = defaultdict(list)
    for r in runs:
        groups[(r["family"], r["arm"])].append(r)
    return {k: {"n": len(rs),
                "accuracy": sum(r["score"] for r in rs) / len(rs),
                "usd_per_query": sum(r["usd"] for r in rs) / len(rs)}
            for k, rs in groups.items()}


def per_item(runs, family, arm):
    scores = defaultdict(list)
    for r in runs:
        if r["family"] == family and r["arm"] == arm:
            scores[r["item_id"]].append(r["score"])
    return {k: sum(v) / len(v) for k, v in scores.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mock", action="store_true", help="read/write results_mock/ instead")
    args = ap.parse_args()
    results = ROOT / ("results_mock" if args.mock else "results")
    runs = [json.loads(l) for l in (results / "runs.jsonl").read_text().splitlines()]
    agg = aggregate(runs)
    families = sorted({f for f, _ in agg})

    with (results / "results.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["family", "arm", "n", "accuracy", "usd_per_query"])
        for (family, arm), v in sorted(agg.items()):
            w.writerow([family, arm, v["n"], f"{v['accuracy']:.4f}", f"{v['usd_per_query']:.6f}"])

    lines = ["# Results\n", "| family | arm | n | accuracy | USD/query |", "|---|---|---|---|---|"]
    for (family, arm), v in sorted(agg.items()):
        lines.append(f"| {family} | {arm} | {v['n']} | {v['accuracy']:.3f} "
                     f"| {v['usd_per_query']:.5f} |")

    lines += ["", "## Army vs frontier (paired bootstrap, ε = 2pp)", "",
              "| family | arm | Δacc (arm − frontier) | 95% CI | verdict |", "|---|---|---|---|---|"]
    for family in families:
        base = per_item(runs, family, "frontier")
        for arm in ARMY_ARMS:
            cmp_ = per_item(runs, family, arm)
            common = sorted(base.keys() & cmp_.keys())
            if not common:
                continue
            boot = paired_bootstrap([cmp_[i] for i in common], [base[i] for i in common])
            lines.append(f"| {family} | {arm} | {boot['mean']:+.3f} "
                         f"| [{boot['ci_lo']:+.3f}, {boot['ci_hi']:+.3f}] | {verdict(boot)} |")

    (results / "report.md").write_text("\n".join(lines) + "\n")
    print(f"wrote {results.name}/report.md and {results.name}/results.csv")


if __name__ == "__main__":
    main()
