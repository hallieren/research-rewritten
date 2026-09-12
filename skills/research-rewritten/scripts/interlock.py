#!/usr/bin/env python3
"""Every number in a deliverable traces to the results file.

Rule enforced: no number typed by hand. Each numeric token in one or two
documents is looked up in the results file (percent and fraction count as the
same fact), two documents must carry the same facts, and a superlative with no
number in its sentence is listed. The script does not judge importance.
"""
import argparse, contextlib, csv, io, json, math, os, re, sys, tempfile

NUM = re.compile(r"(?<![\w.])[-+]?\d[\d,]*(?:\.\d+)?%?")  # a numeric token not glued to an identifier
SKIP_BEFORE = re.compile(r"(section|\u00a7|chapter|figure|fig\.|table|step|item|footnote)\s*$", re.I)  # labels, not facts
YEAR = (1900, 2099)  # four-digit tokens in this range read as calendar years unless --keep-years
SUPERLATIVE = re.compile(r"\b(best|fastest|largest|smallest|strongest|most|least|unprecedented|state.of.the.art|"
                         r"dramatic(ally)?|significant(ly)?|massive(ly)?|huge|record|superior|breakthrough|"
                         r"outperforms?|vastly|overwhelming(ly)?)\b", re.I)  # strength words that need a number beside them
FINAL = "This script does not judge importance. A human reads every MISMATCH and NOT FOUND line."


def to_float(s):
    try:
        return float(s.replace(",", "").rstrip("%"))
    except ValueError:
        return None


def candidates(tok):
    raw = to_float(tok)
    c = {raw}
    if tok.endswith("%"):
        c.add(raw / 100)
    elif 0 < abs(raw) < 1:
        c.add(raw * 100)
    return c


def doc_numbers(path, keep_years):
    """Yield (line_no, token, context) for every numeric token in a document."""
    with open(path) as f:
        for n, line in enumerate(f, start=1):
            line = line.replace("\u2212", "-")
            for m in NUM.finditer(line):
                tok = m.group()
                if SKIP_BEFORE.search(line[:m.start()]):
                    continue
                if not keep_years and re.fullmatch(r"\d{4}", tok) and YEAR[0] <= int(tok) <= YEAR[1]:
                    continue
                yield n, tok, line[max(0, m.start() - 20):m.end() + 20].strip()


def leaves(x):
    if isinstance(x, bool):
        return
    if isinstance(x, (int, float)):
        yield float(x)
    elif isinstance(x, str) and to_float(x) is not None:
        yield to_float(x)
    elif isinstance(x, dict):
        for v in x.values():
            yield from leaves(v)
    elif isinstance(x, list):
        for v in x:
            yield from leaves(v)


def load_results(path):
    vals = set()
    with open(path, newline="") as f:
        if path.endswith(".jsonl"):
            for line in f:
                if line.strip():
                    vals.update(leaves(json.loads(line)))
        elif path.endswith(".md"):
            for line in f:
                if line.lstrip().startswith("|"):
                    for cell in line.split("|"):
                        for m in NUM.finditer(cell.replace("\u2212", "-")):
                            vals.update(candidates(m.group()))
        else:
            for row in csv.reader(f):
                vals.update(v for v in map(to_float, row) if v is not None)
    return sorted(vals)


def classify(tok, results, tol, rel, near):
    best, best_d = None, math.inf
    for c in candidates(tok):
        for v in results:
            d = abs(v - c)
            if d <= tol or d <= rel * abs(v):
                return "MATCH", v, 0.0
            if d / max(abs(c), tol) < best_d:
                best, best_d = v, d / max(abs(c), tol)
    if best is not None and best_d <= near:
        return "MISMATCH", best, best_d
    return "NOT FOUND", None, None


def superlatives(path):
    text = open(path).read()
    for sent in re.split(r"(?<=[.!?])\s+|\n{2,}", text):
        sent = " ".join(sent.split())
        if sent and SUPERLATIVE.search(sent) and not re.search(r"\d", sent):
            yield sent[:120]


def run(argv):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--selftest", action="store_true", help="run the built-in checks and exit")
    p.add_argument("doc1")
    p.add_argument("doc2", nargs="?")
    p.add_argument("--results", required=True, help="csv, jsonl, or md table")
    p.add_argument("--tol", type=float, default=0.0005, help="absolute tolerance, half a unit in the third decimal")
    p.add_argument("--rel", type=float, default=0.01, help="relative tolerance, covers rounding to 3 figures")
    p.add_argument("--near", type=float, default=0.10, help="relative distance that still counts as a mismatch, not a miss")
    p.add_argument("--window", type=int, default=40, help="context characters shown around a flagged token")
    p.add_argument("--keep-years", action="store_true")
    a = p.parse_args(argv)
    results = load_results(a.results)
    counts = {"MATCH": 0, "MISMATCH": 0, "NOT FOUND": 0}
    seen = {}
    for doc in [d for d in (a.doc1, a.doc2) if d]:
        name = os.path.basename(doc)
        seen[doc] = []
        for n, tok, ctx in doc_numbers(doc, a.keep_years):
            seen[doc].append((n, tok))
            kind, v, d = classify(tok, results, a.tol, a.rel, a.near)
            counts[kind] += 1
            if kind == "MATCH":
                print(f"MATCH {name} line {n}: {tok} = {v:g}")
            elif kind == "MISMATCH":
                print(f"MISMATCH {name} line {n}: {tok} nearest results {v:g} (delta {100 * d:.1f}%) \"{ctx[:a.window]}\"")
            else:
                print(f"NOT FOUND {name} line {n}: {tok} \"{ctx[:a.window]}\"")
    only = 0
    if a.doc2:
        sets = {doc: [candidates(t) for _, t in toks] for doc, toks in seen.items()}
        for doc, other in ((a.doc1, a.doc2), (a.doc2, a.doc1)):
            for (n, tok), cs in zip(seen[doc], sets[doc]):
                if not any(any(abs(x - y) <= a.tol for x in cs for y in o) for o in sets[other]):
                    print(f"DOC-ONLY {os.path.basename(doc)}: {tok} (line {n})")
                    only += 1
    sup = 0
    for doc in [d for d in (a.doc1, a.doc2) if d]:
        for sent in superlatives(doc):
            print(f"SUPERLATIVE (no number in sentence): \"{sent}\"")
            sup += 1
    total = sum(counts.values())
    print(f"INTERLOCK: {total} numbers, {counts['MATCH']} matched, {counts['MISMATCH']} mismatched, "
          f"{counts['NOT FOUND']} not found, {only} doc-only, {sup} unquantified superlatives")
    print(FINAL)
    return 1 if counts["MISMATCH"] or counts["NOT FOUND"] else 0


def selftest():
    def cap(argv):
        with contextlib.redirect_stdout(io.StringIO()) as buf:
            code = run(argv)
        return code, buf.getvalue()

    n = 0

    def case(name, ok):
        nonlocal n
        if not ok:
            print(f"SELFTEST: {name} FAILED"); sys.exit(1)
        n += 1; print(f"SELFTEST: {name} ok")

    with tempfile.TemporaryDirectory() as d:
        R, D1, D2 = (os.path.join(d, x) for x in ("r.csv", "d1.md", "d2.md"))
        open(R, "w").write("arm,n,accuracy\nold,100,0.9400\nnew,100,0.7500\n")
        open(D1, "w").write("# Memo\n\nIn 2026 the new arm scored 75% on 100 items, the old arm 94% (see Table 3).\n"
                            "The old arm reached 0.95 accuracy. Latency was 3.14159 seconds.\n"
                            "This is the best system we have ever built.\n")
        open(D2, "w").write("Slide: new arm 0.75, old arm 94%, 0.95, 100 items.\n")
        code, out = cap([D1, "--results", R])
        case("3 matched 1 mismatched 1 not found", "INTERLOCK: 5 numbers, 3 matched, 1 mismatched, 1 not found" in out)
        case("mismatch names nearest", "MISMATCH d1.md line 4: 0.95 nearest results 0.94" in out)
        case("superlative listed", "SUPERLATIVE (no number in sentence): \"This is the best system" in out
             and "1 unquantified superlatives" in out)
        case("year and table number skipped", "2026" not in out and "line 3: 3 " not in out)
        case("exit 1 on mismatch or not found", code == 1)
        case("final line fixed", out.rstrip().endswith(FINAL))
        code, out = cap([D1, D2, "--results", R])
        case("doc-only across two docs", "DOC-ONLY d1.md: 3.14159" in out and "DOC-ONLY d2.md" not in out and "1 doc-only" in out)
        open(D2, "w").write("Slide: new arm 0.75, old arm 0.940.\n")
        code, out = cap([D2, "--results", R])
        case("clean doc exits 0", code == 0 and "2 numbers, 2 matched" in out)
    print(f"SELFTEST: all {n} passed")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv[1:]:
        sys.exit(selftest())
    sys.exit(run(sys.argv[1:]))
