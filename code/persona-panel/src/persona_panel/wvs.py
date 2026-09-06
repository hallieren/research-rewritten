"""Load WVS Wave 7 responses from the user-downloaded CSV (never committed).

WVS codes negative values (-1, -2, -4, -5) as missing/refused; they are dropped.
Expected columns: B_COUNTRY_ALPHA, Q260 (sex), Q262 (age), plus question columns.

The raw file cannot be redistributed, so the repo ships per-subgroup answer
counts instead (data/wvs7_usa_aggregates.json, written by scripts/prepare_wvs.py).
`aggregate` builds them, `expand` turns them back into answer lists so the
metrics see exactly the same input either way.
"""
import csv
import json
from collections import Counter
from pathlib import Path


def load_responses(csv_path, question_ids):
    rows = []
    with open(csv_path, newline="", encoding="utf-8", errors="replace") as f:
        for r in csv.DictReader(f):
            rows.append({"country": r.get("B_COUNTRY_ALPHA"),
                         "sex": r.get("Q260"), "age": r.get("Q262")}
                        | {q: r.get(q) for q in question_ids})
    return rows


def subgroup_rows(rows, sg):
    out = []
    for r in rows:
        try:
            age = int(float(r["age"]))
        except (TypeError, ValueError):
            continue
        if (r["country"] == sg["country"] and r["sex"] == sg["sex_code"]
                and sg["age_lo"] <= age <= sg["age_hi"]):
            out.append(r)
    return out


def answers_for(rows, qid):
    return [a for a in (r[qid] for r in rows)
            if a and not a.lstrip().startswith("-")]


def aggregate(rows, subgroups, question_ids):
    """subgroup name -> qid -> {option code: count}. Derived counts only, no rows."""
    return {sg["name"]: {q: dict(Counter(answers_for(subgroup_rows(rows, sg), q)))
                         for q in question_ids}
            for sg in subgroups}


def load_aggregates(path):
    return json.loads(Path(path).read_text())


def expand(counts):
    return [code for code, n in sorted(counts.items()) for _ in range(n)]
