#!/usr/bin/env python3
"""Criteria are locked before the numbers, and every later edit is a tagged log entry.
Rules: the criteria file names every required section with no backdoor wording; it entered
the record before the first result (git history or a ts field, not mtime alone); the change
log has dated entries saying what, why, and whether results had been seen."""
import argparse, contextlib, csv, io, json, os, re, subprocess, sys, tempfile
from datetime import datetime, timezone

KEYS = {  # required key -> pattern that counts as naming it; the words are the ones the templates use
    "hypothesis": r"\bhypothes[ie]s\b",
    "arms": r"\barms?\b|\bconditions?\b|\bvariants?\b|\btreatments?\b",
    "control": r"\bcontrol\b|\bbaseline\b|\bsteelman\b|cheapest alternative",
    "primary_basis": r"\bprimary\b",
    "sensitivity_basis": r"\bsensitivity\b|\bsecondary\b|\brobustness\b",
    "criteria_numeric": r"(criteri\w*|threshold|readout|verdict|success|\btie\b|\bwin\b)[\s\S]{0,200}?\d|\d[\s\S]{0,200}?(criteri\w*|threshold|readout|verdict|success|\btie\b|\bwin\b)",
    "falsification": r"\bfalsif",
    "stopping_rule": r"stopping rule|stop(ping)? (when|after|at|criterion|condition)|\bstopping\b",
    "confounders": r"\bconfound|\bexclud|\bcontaminat|\bleak|threats? to validity",
    "filing": r"\bfil(e|ed|ing)\b|\brecord(ed)?\b|\bledger\b|\bcommit\b|\bCHANGES\b|change log|decision record",
}
INFERRED_STOP = r"\bn\s*=\s*\d+|first \d+|\d+ (items|samples|trials|runs|queries|participants)|sample size|hard cap|budget cap"  # a fixed n or a cap stops a run without saying so
BACKDOOR = r"reasonable range|as appropriate|at (our |the |my )?discretion|judged as a whole"  # wording that lets the reader move the bar later
CHANGE_LOG = ("CHANGES.md", "changes.md", "change-log.md", "CHANGELOG.md")  # sibling names accepted for the change log
TS_FIELDS = ("ts", "timestamp", "time", "date")  # first of these in a results row is the result time
ENTRY = re.compile(r"^(- |### )")  # a change-log entry starts as a top-level bullet or a level-3 heading
iso = lambda t: datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def cmd_sections(a):
    text = open(a.criteria).read()
    missing, warnings = [], 0
    for key, pat in KEYS.items():
        if re.search(pat, text, re.I):
            continue
        if key == "stopping_rule" and re.search(INFERRED_STOP, text, re.I):
            print("WARN: stopping rule inferred from a fixed sample size / hard cap"); warnings += 1; continue
        missing.append(key)
    backdoors = [n for n, l in enumerate(text.splitlines(), 1) if re.search(BACKDOOR, l, re.I) and not re.search(r"\d", l)]
    for n in backdoors: print(f"PREREG SECTIONS: FAIL backdoor line {n}")
    d = os.path.dirname(a.criteria) or "."
    if not a.changes and not any(os.path.exists(os.path.join(d, c)) for c in CHANGE_LOG):
        print("WARN: no change log beside the criteria file (CHANGES.md); create it before the first run"); warnings += 1
    if missing:
        print(f"PREREG SECTIONS: FAIL missing={','.join(missing)}")
    if missing or backdoors: return 1
    print(f"PREREG SECTIONS: PASS ({len(KEYS)}/{len(KEYS)} keys, warnings={warnings})")
    return 0


def git_commit(path, first):
    """(hash, epoch) of the first commit that added path, or the last that touched it; None if untracked."""
    d, name = os.path.dirname(os.path.abspath(path)), os.path.basename(path)
    # No --follow: its rename heuristic ties a same-content criteria copy to an older commit, hiding a same-commit filing.
    args = ["--diff-filter=A"] if first else ["-1"]
    r = subprocess.run(["git", "-C", d, "log", *args, "--format=%H %ct", "--", name], capture_output=True, text=True)
    toks = r.stdout.split() if r.returncode == 0 else []
    return (toks[-2], int(toks[-1])) if toks else None


def parse_ts(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return datetime.fromisoformat(str(v).replace("Z", "+00:00")).timestamp()


def results_ts(path, field):
    with open(path, newline="") as f:
        row = json.loads(f.readline()) if path.endswith(".jsonl") else next(csv.DictReader(f), {})
    field = field or next((k for k in TS_FIELDS if k in row), None)
    return (parse_ts(row[field]), f"field {field}") if field and row.get(field) not in (None, "") else (None, None)


def cmd_timing(a):
    crit = git_commit(a.criteria, True)
    res_t, res_src = results_ts(a.results, a.results_ts_field)
    res = None if res_t else git_commit(a.results, True)
    reason = ("criteria and results entered the repo in the same commit" if crit and res and crit[0] == res[0]
              else "not a git repo and no ts field" if not crit and not res_t else None)
    if reason: print(f"PREREG: NO TIMESTAMP ({reason})"); return 1
    crit_t, crit_src = (crit[1], f"commit {crit[0][:7]}") if crit else (os.path.getmtime(a.criteria), "mtime")
    if res: res_t, res_src = res[1], f"commit {res[0][:7]}"
    elif res_t is None: res_t, res_src = os.path.getmtime(a.results), "mtime"
    detail = f"(criteria {iso(crit_t)} via {crit_src}, first result {iso(res_t)} via {res_src})"
    last = git_commit(a.criteria, False)
    if last and last[1] > res_t:
        print("WARN: criteria file was modified after the first result (edits belong in the change log)")
    if crit_t <= res_t: print(f"PREREG: locked before results {detail}"); return 0
    print(f"PREREG: LOCKED AFTER RESULTS (exploratory) {detail}"); return 1


def cmd_changes(a):
    entries, cur = [], None
    for line in open(a.changes).read().splitlines():
        if ENTRY.match(line): cur = [line]; entries.append(cur)
        elif cur is not None and line.strip() and not line.startswith("#"): cur.append(line)
    complete = after = untagged = 0
    for i, e in enumerate(entries, 1):
        t = " ".join(e)
        fields = re.split(r"\s+(?:\u2014|\u2013|--?)\s+", t)
        have = {"date": bool(re.search(r"\d{4}-\d{2}-\d{2}", t)),
                "what": bool(re.search(r"→|->|\bchanged\b|\bfrom .* to\b|\bold\b.*\bnew\b", t, re.I)),
                "why": bool(re.search(r"\b(reason|why|because)\b", t, re.I)) or len(fields) >= 4}
        tag = re.search(r"after results seen:\s*(yes|no)", t, re.I)
        untagged += not tag
        after += bool(tag and tag.group(1).lower() == "yes")
        missing = [k for k, v in have.items() if not v] + ([] if tag else ["tag 'after results seen: yes|no'"])
        complete += not missing
        if missing: print(f"CHANGES: entry {i} ({t[:40]!r}) missing {', '.join(missing)}")
    print(f"CHANGES: {len(entries)} entries, {complete} complete, {after} after results seen (exploratory), {untagged} missing tag")
    return 0 if entries and complete == len(entries) else 1


def cmd_all(a):
    codes = [cmd_sections(a), cmd_timing(a)]
    a.changes = a.changes or os.path.join(os.path.dirname(a.criteria) or ".", CHANGE_LOG[0])
    codes.append(cmd_changes(a) if os.path.exists(a.changes) else 1)
    return max(codes)


def run(argv):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--selftest", action="store_true", help="run the built-in checks and exit")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sections", help="required keys, backdoor wording, change-log sibling")
    s.add_argument("criteria"); s.add_argument("--changes"); s.set_defaults(fn=cmd_sections)
    s = sub.add_parser("changes", help="every change-log entry dated, explained, and tagged")
    s.add_argument("changes"); s.set_defaults(fn=cmd_changes)
    for name, text, fn in (("timing", "criteria commit time versus first result time", cmd_timing),
                           ("all", "sections, timing, and changes in one run", cmd_all)):
        s = sub.add_parser(name, help=text); s.add_argument("criteria"); s.add_argument("--results", required=True)
        s.add_argument("--results-ts-field"); s.add_argument("--changes"); s.set_defaults(fn=fn)
    a = p.parse_args(argv); return a.fn(a)


GOOD = """# Criteria
Hypothesis: arm new beats arm old on accuracy by at least 2 points.
Arms: old (baseline, the cheapest alternative) and new. Control: old at default settings.
Primary basis: accuracy. Sensitivity basis: latency p95.
Criteria: the win threshold is 2 points. Falsification: a difference under 0 falsifies it.
Stopping rule: stop after 150 items. Confounders: template clusters. Filing: results/, CHANGES.md.
"""


def selftest():
    def cap(argv):
        with contextlib.redirect_stdout(io.StringIO()) as buf:
            code = run(argv)
        return code, buf.getvalue()

    n = 0

    def case(name, ok):
        nonlocal n
        if not ok: print(f"SELFTEST: {name} FAILED"); sys.exit(1)
        n += 1; print(f"SELFTEST: {name} ok")

    def git(d, *args, t=None):  # epochs near 1.7e9 because git rejects small numbers as dates
        env = dict(os.environ, GIT_AUTHOR_DATE=f"{t} +0000", GIT_COMMITTER_DATE=f"{t} +0000") if t else None
        subprocess.run(["git", "-C", d, "-c", "user.name=t", "-c", "user.email=t@t", "-c", "core.hooksPath=/dev/null",
                        *args], check=True, capture_output=True, env=env)

    with tempfile.TemporaryDirectory() as d:
        C, L, R = (os.path.join(d, x) for x in ("criteria.md", "CHANGES.md", "runs.jsonl"))
        open(C, "w").write(GOOD); open(L, "w").write("")
        code, out = cap(["sections", C])
        case("good stub PASS", code == 0 and "PREREG SECTIONS: PASS (10/10 keys, warnings=0)" in out)
        open(C, "w").write(GOOD.replace("Falsification: a difference under 0 falsifies it.", "").replace("Stopping rule: stop after 150 items.", "n = 150."))
        code, out = cap(["sections", C])
        case("minus falsification FAIL, stop inferred", code == 1 and "FAIL missing=falsification" in out and "WARN: stopping rule inferred" in out)
        open(C, "w").write(GOOD + "Other metrics are judged as a whole.\n")
        code, out = cap(["sections", C])
        case("backdoor line FAIL", code == 1 and "PREREG SECTIONS: FAIL backdoor line 7" in out)
        open(C, "w").write(GOOD); open(R, "w").write('{"item": 1, "score": 1}\n')
        case("no git no ts", cap(["timing", C, "--results", R])[1].startswith("PREREG: NO TIMESTAMP (not a git repo"))
        git(d, "init", "-q"); git(d, "add", "criteria.md"); git(d, "commit", "-q", "-m", "c", t=1700001000)
        git(d, "add", "runs.jsonl"); git(d, "commit", "-q", "-m", "r", t=1700002000)
        code, out = cap(["timing", C, "--results", R])
        case("locked before results", code == 0 and out.startswith("PREREG: locked before results (criteria 2023-11-14T22:30Z via commit"))
        open(R, "w").write('{"ts": 1600000000, "score": 1}\n')
        code, out = cap(["timing", C, "--results", R])
        case("locked after results via ts field", code == 1 and "LOCKED AFTER RESULTS (exploratory)" in out and "via field ts" in out)
        open(C, "a").write("Edited later.\n"); git(d, "commit", "-qam", "edit", t=1700003000); open(R, "w").write('{"ts": 1700002500}\n')
        case("warn modified after first result", "WARN: criteria file was modified after the first result" in cap(["timing", C, "--results", R])[1])
        C2, R2 = (os.path.join(d, x) for x in ("c2.md", "r2.jsonl")); open(C2, "w").write(GOOD); open(R2, "w").write('{"score": 1}\n')
        git(d, "add", "-A"); git(d, "commit", "-qm", "both", t=1700004000)
        case("same commit", "NO TIMESTAMP (criteria and results entered the repo in the same commit)" in cap(["timing", C2, "--results", R2])[1])
        open(L, "w").write("# Log\n- 2026-01-02 - eps - 0.02 -> 0.03 - reason: pilot variance - after results seen: no\n"
                           "- 2026-01-03 - scorer - strips % now\n  continuation line\n")
        code, out = cap(["changes", L])
        case("changes 1 complete 1 untagged", code == 1 and "CHANGES: 2 entries, 1 complete, 0 after results seen (exploratory), 1 missing tag" in out
             and "entry 2" in out and "missing what, why, tag" in out)
    print(f"SELFTEST: all {n} passed")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv[1:]:
        sys.exit(selftest())
    sys.exit(run(sys.argv[1:]))
