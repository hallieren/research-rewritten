#!/usr/bin/env python3
"""The brief leaks no expectation, the report is three-valued, the sample is nobody's choice.

Rules enforced: a brief handed to an independent channel carries no wanted outcome,
no strength adjective, no ownership (only fenced text blocks leave the desk, so only
they are scanned) and no residue of the draft it checks; a report gives each claim one
verdict from confirmed, falsified, undecidable, a basis for every confirmed, and every
ruling line signed (UNSIGNED counts) beside a channel line and a criteria timestamp
line; a spot-check sample is drawn by seed, not picked by either side.
"""
import argparse, contextlib, io, math, os, random, re, sys, tempfile

LEXICON = [  # (class, pattern, fix); each pattern names a way a brief tells the channel what to find
    ("expectation", r"\b(we|i) (expect|hope|believe|think|assume|predict|know)\b", "state the claim and the check, not the wanted outcome"),
    ("expectation", r"\bshould (show|confirm|find|reveal|hold|work|pass|be (correct|right|fine|ok))\b", "state the claim and the check, not the wanted outcome"),
    ("expectation", r"\b(confirm|verify|prove) that\b|\bhopefully\b|\bas expected\b|\bexpected to\b", "ask for a verdict from confirmed, falsified, undecidable"),
    ("adjective", r"\b(impressive|promising|robust|remarkable|excellent|strong|solid|clear(ly)?|obvious(ly)?|surprising(ly)?|striking|compelling|convincing|weak|flawed|sloppy|careful(ly)?)\b", "delete the adjective, give the number or the check"),
    ("ownership", r"\b(our|my) (result|finding|hypothesis|model|method|approach|claim|conclusion|work|paper|analysis|numbers)s?\b|\bwe (found|showed|demonstrated|achieved|obtained|measured)\b", "name the artifact, not the owner"),
]
MUSH = [  # phrases banned in a ruling position because they read as a verdict without being one
    "basically correct", "broadly credible", "looks fine", "should be ok", "generally holds",
    "may under some circumstances", "i am aware of it", "largely correct", "mostly right", "essentially right"]
VERDICTS = ("confirmed", "falsified", "undecidable")
NOT_THREE = re.compile(r"\b(pass|fail|agree|disagree)\b|score:|\b\d+/10\b", re.I)  # look like verdicts, are not in the vocabulary
BASIS = re.compile(r"\b(basis|source|http|file|table|p\.)", re.I)  # a confirmed claim must point at something
CLAIM_START = re.compile(r"^\s*(\d+[.):]|[A-Z]{1,3}\d+[.:)]|[-*+] )")  # numbered, letter-number id, or bullet


def text_blocks(path):
    """Yield (line_no, line) for lines inside fenced text blocks."""
    inside = False
    with open(path) as f:
        for n, line in enumerate(f, start=1):
            if line.strip().startswith("```"):
                inside = not inside and line.strip().lower() == "```text"
                continue
            if inside:
                yield n, line.rstrip("\n")


def words(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def cmd_brief(a):
    leaks = 0
    lines = list(text_blocks(a.brief))
    for n, line in lines:
        for cls, pat, fix in LEXICON:
            for m in re.finditer(pat, line, re.I):
                print(f"LEAK line {n}: \"{m.group()}\" ({cls}) -> {fix}")
                leaks += 1
    residue = 0
    if a.original:
        orig = open(a.original).read()
        brief_text = "\n".join(l for _, l in lines)
        sh = lambda t: {tuple(w[i:i + a.shingle]) for w in [words(t)] for i in range(len(w) - a.shingle + 1)}
        heads = lambda t: {l.strip("# ").strip().lower() for l in t.splitlines() if l.startswith("#")}
        k, j = len(sh(brief_text) & sh(orig)), len(heads(brief_text) & heads(orig))
        print(f"RESIDUE: {k} shared {a.shingle}-word shingles, {j} shared headings")
        residue = k + j
    if leaks or residue:
        print(f"BRIEF: LEAKS {leaks}, RESIDUE {residue} (do not dispatch)")
        return 1
    print("BRIEF: clean")
    return 0


def cmd_report(a):
    lines = open(a.report).read().splitlines()
    blocks, problems = [], []
    for n, line in enumerate(lines, start=1):
        if CLAIM_START.match(line):
            blocks.append([line.split()[0].rstrip(".:)") if line.split()[0] not in "-*+" else f"bullet@{n}", n, []])
        if blocks:
            blocks[-1][2].append(line)
        low = line.lower()
        for m in MUSH:
            if m in low:
                print(f"MUSH line {n}: \"{m}\" (rewrite as confirmed, falsified, or undecidable with a basis)")
                problems.append(f"mush line {n}")
    counts = dict.fromkeys(VERDICTS, 0)
    for cid, n, body in blocks:
        text = "\n".join(body)
        found = [v for v in VERDICTS if re.search(rf"\b{v}\b", text, re.I)]
        if len(found) > 1:
            print(f"CLAIM {cid}: {len(found)} VERDICTS (pick one)")
            problems.append(f"claim {cid} double verdict")
        elif not found:
            other = NOT_THREE.search(text)
            print(f"CLAIM {cid}: NOT THREE-VALUE (\"{other.group()}\")" if other else f"CLAIM {cid}: NO VERDICT")
            problems.append(f"claim {cid} no verdict")
        elif found[0] == "confirmed" and not BASIS.search(text):
            print(f"CLAIM {cid}: confirmed without basis (treat as undecidable)")
            counts["undecidable"] += 1
        else:
            counts[found[0]] += 1
    rulings = [n for n, l in enumerate(lines, start=1) if l.startswith("ruling:")]
    problems += [f"ruling line {n} unsigned" for n in rulings if "signed by:" not in lines[n - 1]]
    if rulings:
        chan = [l for l in lines if l.startswith("verification channel:")]
        if not chan:
            problems.append("verification channel line missing")
        elif any("SAME-CHANNEL" in l for l in chan):
            problems.append("verification channel is SAME-CHANNEL (void)")
        if not any(l.startswith("criteria timestamp:") for l in lines):
            problems.append("criteria timestamp line missing")
    print(f"undecidable: {counts['undecidable']} (≠ pass)")
    print(f"confirmed: {counts['confirmed']}, falsified: {counts['falsified']}")
    if problems:
        print(f"REPORT: INVALID ({'; '.join(problems)})")
        return 1
    print(f"REPORT: ok ({len(blocks)} claims)")
    return 0


def cmd_sample(a):
    items = [l.rstrip("\n") for l in open(a.file) if l.strip()]
    pct = a.pct / 100 if a.pct > 1 else a.pct  # accept 10 or 0.10 for ten percent
    k = min(len(items), max(a.n, math.ceil(pct * len(items))))
    picks = random.Random(a.seed).sample(items, k)
    print(f"SAMPLE: seed={a.seed} picked={k} of {len(items)}")
    print(*picks, sep="\n")
    return 0


def run(argv):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--selftest", action="store_true", help="run the built-in checks and exit")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("brief", help="scan the fenced text blocks of a brief for leaks and residue")
    s.add_argument("brief")
    s.add_argument("--original", help="the draft the channel must not see; residue is measured against it")
    s.add_argument("--shingle", type=int, default=8, help="8 consecutive words rarely repeat by chance")
    s.set_defaults(fn=cmd_brief)
    s = sub.add_parser("report", help="lint a verification report for three-value verdicts and sentinels")
    s.add_argument("report")
    s.set_defaults(fn=cmd_report)
    s = sub.add_parser("sample", help="seeded pick of max(n, pct of the list) lines")
    s.add_argument("file")
    s.add_argument("--n", type=int, required=True)
    s.add_argument("--pct", type=float, required=True)
    s.add_argument("--seed", type=int, required=True)
    s.set_defaults(fn=cmd_sample)
    a = p.parse_args(argv); return a.fn(a)


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
        B, O, R, L = (os.path.join(d, x) for x in ("b.md", "o.md", "r.md", "l.txt"))
        open(B, "w").write("# Brief\nWe expect a win (outside the block, ignored).\n```text\nCheck each claim. "
                           "We expect the numbers to hold.\nThe result is impressive.\nOur result beats the baseline.\n```\n")
        open(O, "w").write("## Method\nthe quick brown fox jumps over the lazy dog again\n")
        code, out = cap(["brief", B])
        case("three leak classes", code == 1 and all(f"({c})" in out for c in ("expectation", "adjective", "ownership"))
             and "line 2" not in out and "BRIEF: LEAKS 3, RESIDUE 0" in out)
        open(B, "w").write("```text\n## Method\nthe quick brown fox jumps over the lazy dog again\nlist the claims\n```\n")
        code, out = cap(["brief", B, "--original", O])
        case("residue shingles and heading", "RESIDUE: 4 shared 8-word shingles, 1 shared headings" in out and code == 1)
        open(B, "w").write("```text\nList each claim with confirmed, falsified, or undecidable.\n```\n")
        case("clean brief", cap(["brief", B, "--original", O])[1].endswith("BRIEF: clean\n"))
        open(R, "w").write("STATUS: DRAFT\nA1. confirmed, basis: table 2 of the file\nA2. confirmed and also falsified\n"
                           "A3. the claim is basically correct\nA4. undecidable, no source reachable\nA5. confirmed\n"
                           "ruling: verified\nverification channel: SAME-CHANNEL (void)\n")
        code, out = cap(["report", R])
        case("double verdict", "CLAIM A2: 2 VERDICTS (pick one)" in out)
        case("mush phrase", "MUSH line 4: \"basically correct\"" in out and "CLAIM A3: NO VERDICT" in out)
        case("confirmed without basis", "CLAIM A5: confirmed without basis" in out and "undecidable: 2 (≠ pass)" in out)
        case("sentinel lint", code == 1 and "ruling line 7 unsigned" in out and "SAME-CHANNEL" in out and "criteria timestamp line missing" in out)
        open(R, "w").write("A1. confirmed, basis: table 2\nA2. score: 7/10\n")
        case("not three-value", "CLAIM A2: NOT THREE-VALUE (\"score:\")" in cap(["report", R])[1])
        open(R, "w").write("- confirmed, source: p. 4\n- falsified, the file says 12\nruling: holds | signed by: UNSIGNED\n"
                           "verification channel: separate session, model X\ncriteria timestamp: before results\n")
        code, out = cap(["report", R])
        case("valid report", code == 0 and "REPORT: ok (2 claims)" in out and "confirmed: 1, falsified: 1" in out)
        open(L, "w").write("".join(f"cite{i}\n" for i in range(40)))
        code, out = cap(["sample", L, "--n", "5", "--pct", "0.1", "--seed", "7"])
        case("sample determinism", out == cap(["sample", L, "--n", "5", "--pct", "0.1", "--seed", "7"])[1]
             and out.startswith("SAMPLE: seed=7 picked=5 of 40\n") and len(set(out.splitlines()[1:])) == 5)
    print(f"SELFTEST: all {n} passed")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv[1:]:
        sys.exit(selftest())
    sys.exit(run(sys.argv[1:]))
