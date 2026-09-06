"""Evaluate pre-registered criteria and write results/report.md."""
import argparse
import json
import statistics
import sys
import tomllib
from collections import defaultdict
from pathlib import Path

from . import wvs
from .metrics import dist, js_divergence, top_choice_match, variance_ratio

ROOT = Path(__file__).resolve().parents[2]

JS_MEDIAN_MAX = 0.10       # criterion (a)
TOP_CHOICE_MIN = 0.70      # criterion (a)
COLLAPSE_RATIO = 0.5       # criterion (b)
COLLAPSE_FRACTION = 1 / 3  # criterion (b)
CELL_JS_MAX = 0.20         # criterion (c)
CONTAM_JS = 0.05           # contamination flag


def evaluate_subgroup(persona_answers, human_answers, options_by_q):
    js, matches, collapsed = {}, {}, 0
    qids = sorted(options_by_q)
    for qid in qids:
        opts = options_by_q[qid]
        p = dist(persona_answers[qid], opts)
        h = dist(human_answers[qid], opts)
        js[qid] = js_divergence(p, h)
        matches[qid] = top_choice_match(p, h)
        if variance_ratio(persona_answers[qid], human_answers[qid]) < COLLAPSE_RATIO:
            collapsed += 1
    median_js = statistics.median(js.values())
    match_rate = sum(matches.values()) / len(matches)
    return {"js": js, "median_js": median_js, "top_choice_rate": match_rate,
            "collapse_fraction": collapsed / len(qids),
            "passes_a": median_js <= JS_MEDIAN_MAX and match_rate >= TOP_CHOICE_MIN}


def contamination_flags(answers_by_variant, options_by_q):
    flags = {}
    for qid, variants in answers_by_variant.items():
        opts = options_by_q[qid]
        pooled = variants["p1"] + variants["p2"]
        flags[qid] = js_divergence(dist(variants["original"], opts),
                                   dist(pooled, opts)) > CONTAM_JS
    return flags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mock", action="store_true", help="read/write results_mock/ instead")
    args = ap.parse_args()
    results = ROOT / ("results_mock" if args.mock else "results")
    cfg = tomllib.loads((ROOT / "config" / "run.toml").read_text())
    questions = tomllib.loads((ROOT / "config" / "questions.toml").read_text())["questions"]
    options_by_q = {q["id"]: [c for c, _ in q["options"]] for q in questions}
    qids = list(options_by_q)

    answers = [json.loads(l)
               for l in (results / "answers.jsonl").read_text().splitlines()]
    csv_path, agg_path = ROOT / cfg["wvs_csv"], ROOT / cfg["wvs_aggregates"]
    if csv_path.exists():
        rows = wvs.load_responses(csv_path, qids)

        def human_answers(sg, qid):
            return wvs.answers_for(wvs.subgroup_rows(rows, sg), qid)
        print(f"ground truth: {cfg['wvs_csv']} (raw rows)")
    elif agg_path.exists():
        agg = wvs.load_aggregates(agg_path)

        def human_answers(sg, qid):
            return wvs.expand(agg[sg["name"]][qid])
        print(f"ground truth: {cfg['wvs_aggregates']} (per-subgroup counts)")
    else:
        sys.exit(f"Neither {cfg['wvs_csv']} nor {cfg['wvs_aggregates']} found. "
                 "WVS raw data is not committed (license forbids redistribution). "
                 "Register and download the v6.0 cross-national CSV per "
                 "docs/data-license.md, then run scripts/prepare_wvs.py to "
                 "generate both files.")

    # persona answers: subgroup -> qid -> [answers]; variants: subgroup-agnostic pool
    by_sg = defaultdict(lambda: defaultdict(list))
    by_variant = defaultdict(lambda: defaultdict(list))
    for a in answers:
        if a["answer"] is None:
            continue
        by_variant[a["qid"]][a["variant"]].append(a["answer"])
        if a["variant"] == "original":
            by_sg[a["subgroup"]][a["qid"]].append(a["answer"])

    flags = contamination_flags(by_variant, options_by_q)
    clean_qids = [q for q in qids if not flags[q]]

    lines = ["# Persona panel vs WVS-7 — pre-registered readout\n",
             f"Contamination-suspect questions (excluded from a/c): "
             f"{[q for q in qids if flags[q]] or 'none'}\n",
             "| subgroup | median JS | top-choice | collapse frac | passes (a) |",
             "|---|---|---|---|---|"]
    cell_results = []
    for sg in cfg["subgroups"]:
        human = {q: human_answers(sg, q) for q in clean_qids}
        persona = {q: by_sg[sg["name"]][q] for q in clean_qids}
        r = evaluate_subgroup(persona, human, {q: options_by_q[q] for q in clean_qids})
        cell_results.append(r)
        lines.append(f"| {sg['name']} | {r['median_js']:.3f} | {r['top_choice_rate']:.0%} "
                     f"| {r['collapse_fraction']:.0%} | {r['passes_a']} |")

    b_triggered = any(r["collapse_fraction"] > COLLAPSE_FRACTION for r in cell_results)
    c_pass = (sum(r["passes_a"] for r in cell_results) >= 5
              and all(r["median_js"] <= CELL_JS_MAX for r in cell_results))
    lines += ["",
              f"- Criterion (b) variance-collapse red line triggered: **{b_triggered}**",
              f"- Criterion (c) subgroup cross-check passes: **{c_pass}**",
              f"- Overall: **{'PASS' if c_pass and not b_triggered else 'FAIL'}** "
              "(see docs/prereg.md for the falsification shape)"]

    (results / "report.md").write_text("\n".join(lines) + "\n")
    print(f"wrote {results.name}/report.md")


if __name__ == "__main__":
    main()
