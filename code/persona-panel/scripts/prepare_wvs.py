"""Build data/wvs7_usa.csv (official-codebook coding) from the WVS-7 release CSV.

WVS publishes v6.0 in two layouts. The regular cross-national CSV carries the
official-codebook codes our config/questions.toml uses (Q46 1 = Very happy)
and is copied as-is. The "inverted" release renames direction-flipped
categorical items with a P suffix (Q46 -> Q46P, higher = more of the trait);
those are mapped back via code = (scale_max + 1) - value. The script detects
which layout it was given per column. Ten-point scales keep their original
names and direction in both; WVS negative missing codes are preserved untouched.

Direction verified empirically on the USA slice before this script was written
(anchors: Q46 mode "rather happy" ~62%, Q49 mean ~7.2, Q1 "very important"
~89%, Q57 trusted ~40% — all match published US figures only under the
mapping used here).

Also writes data/wvs7_usa_aggregates.json, the per-subgroup answer counts the
repo ships in place of the raw rows (see docs/data-license.md, section 4).

Usage: uv run python scripts/prepare_wvs.py <path-to-official-release.csv>
"""
import csv
import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from persona_panel import wvs  # noqa: E402
QIDS = ["Q1", "Q2", "Q5", "Q6", "Q46", "Q49", "Q57", "Q106", "Q120", "Q131",
        "Q158", "Q164", "Q184", "Q185", "Q240"]
INVERTED_MAX = {"Q1": 4, "Q2": 4, "Q5": 4, "Q6": 4, "Q46": 4, "Q57": 2, "Q131": 4}


def main():
    raw = Path(sys.argv[1])
    out = ROOT / "data" / "wvs7_usa.csv"
    out.parent.mkdir(exist_ok=True)
    n = 0
    with open(raw, newline="", encoding="utf-8", errors="replace") as f, \
         out.open("w", newline="") as g:
        w = csv.writer(g)
        w.writerow(["B_COUNTRY_ALPHA", "Q260", "Q262"] + QIDS)
        for r in csv.DictReader(f):
            if r["B_COUNTRY_ALPHA"] != "USA":
                continue
            row = [r["B_COUNTRY_ALPHA"], r["Q260"], r["Q262"]]
            for q in QIDS:
                if q in INVERTED_MAX and q + "P" in r:
                    v = r[q + "P"]
                    flipped = v and not v.startswith("-")
                    row.append(str(INVERTED_MAX[q] + 1 - int(v)) if flipped else v)
                else:
                    row.append(r[q])
            w.writerow(row)
            n += 1
    print(f"wrote {out} ({n} USA rows)")

    cfg = tomllib.loads((ROOT / "config" / "run.toml").read_text())
    agg = wvs.aggregate(wvs.load_responses(out, QIDS), cfg["subgroups"], QIDS)
    agg_out = ROOT / cfg["wvs_aggregates"]
    agg_out.write_text(json.dumps(agg, indent=1, sort_keys=True) + "\n")
    print(f"wrote {agg_out} (per-subgroup counts, safe to commit)")


if __name__ == "__main__":
    main()
