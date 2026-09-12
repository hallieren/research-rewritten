#!/usr/bin/env python3
"""Append-only ledger with a hard cap that fires.

Rule enforced: history does not accept edits. Every line is hash-chained to the
previous one, the cap is checked after the entry is written (the crossing entry
stays recorded, the fuse blows on the call that crossed), and a sidecar head
file catches a deleted tail. Works for money, calls, checks, or minutes.
"""
import argparse, contextlib, hashlib, io, json, os, sys, tempfile, time
from datetime import datetime

UNITS = ("usd", "calls", "checks", "minutes")  # closed list so sums never mix a currency with a count


def canon(d):
    return json.dumps(d, sort_keys=True, separators=(",", ":"))


def digest(d):
    return hashlib.sha256(canon({k: v for k, v in d.items() if k != "hash"}).encode()).hexdigest()


def entries(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def parse_ts(s):
    if s is None:
        return time.time()
    try:
        return float(s)
    except ValueError:
        return datetime.fromisoformat(s).timestamp()


def append(path, entry):
    with open(path, "a") as f:
        f.write(canon(entry) + "\n")
    with open(path + ".head", "w") as f:
        f.write(canon({"n": entry["i"] + 1, "last": entry["hash"]}))


def cmd_init(a):
    if os.path.exists(a.ledger):
        print(f"usage error: {a.ledger} exists; a ledger is never re-initialized", file=sys.stderr)
        return 2
    g = {"i": 0, "ts": parse_ts(a.ts), "amount": 0.0, "unit": a.unit,
         "meta": {"cap": a.cap, "genesis": True}, "prev": ""}
    g["hash"] = digest(g)
    append(a.ledger, g)
    print(f"LEDGER: init cap {a.cap} {a.unit}, n=1")
    return 0


def cmd_record(a):
    rows = entries(a.ledger)
    genesis, last = rows[0], rows[-1]
    meta = dict(kv.split("=", 1) for kv in a.meta)
    e = {"i": last["i"] + 1, "ts": parse_ts(a.ts), "amount": a.amount, "unit": genesis["unit"],
         "meta": meta, "prev": last["hash"]}
    e["hash"] = digest(e)
    append(a.ledger, e)
    total = sum(r["amount"] for r in rows) + a.amount
    cap = genesis["meta"]["cap"]
    pct = 100 * total / cap if cap else 0.0
    tail = f"total {total:g} / cap {cap:g} ({pct:.1f}%), n={e['i'] + 1}"
    if total > cap:
        print(f"LEDGER: CAP EXCEEDED, +{a.amount:g} {e['unit']}, {tail}")
        return 2
    print(f"LEDGER: +{a.amount:g} {e['unit']}, {tail}")
    return 0


def cmd_sum(a):
    rows = entries(a.ledger)
    unit = rows[0]["unit"]
    if a.by:
        groups = {}
        for r in rows[1:]:
            k = r["meta"].get(a.by, "(none)")
            groups.setdefault(k, [0.0, 0])
            groups[k][0] += r["amount"]
            groups[k][1] += 1
        for k, (t, n) in sorted(groups.items()):
            print(f"LEDGER SUM: {a.by}={k} {t:g} {unit} (n={n})")
    total = sum(r["amount"] for r in rows)
    print(f"LEDGER SUM: total {total:g} {unit} over {len(rows) - 1} entries")
    return 0


def check_chain(path):
    """Return (message, code); message starts after 'LEDGER: '."""
    if not os.path.exists(path + ".head"):
        return "NO SIDECAR", 1
    rows = entries(path)
    prev, prev_ts = "", float("-inf")
    for k, r in enumerate(rows, start=1):
        if r["i"] != k - 1 or r["prev"] != prev or r["hash"] != digest(r):
            return f"BROKEN at line {k}", 1
        if r["ts"] < prev_ts:
            return f"TS NOT MONOTONIC at line {k}", 1
        prev, prev_ts = r["hash"], r["ts"]
    with open(path + ".head") as f:
        head = json.load(f)
    if head["n"] > len(rows):
        return f"TRUNCATED (sidecar n={head['n']}, file has {len(rows)})", 1
    if head["n"] != len(rows) or head["last"] != prev:
        return f"BROKEN (sidecar does not match line {len(rows)})", 1
    total = sum(r["amount"] for r in rows)
    cap = rows[0]["meta"]["cap"]
    return f"intact (n={len(rows)}, total {total:g} / cap {cap:g} {rows[0]['unit']})", 0


def cmd_check(a):
    msg, code = check_chain(a.ledger)
    print(f"LEDGER: {msg}")
    return code


def build_parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--selftest", action="store_true", help="run the built-in checks and exit")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("init", help="create a ledger with a genesis line holding cap and unit")
    s.add_argument("ledger")
    s.add_argument("--cap", type=float, required=True)
    s.add_argument("--unit", choices=UNITS, required=True)
    s.add_argument("--ts", help="epoch seconds or ISO 8601; default now")
    s.set_defaults(fn=cmd_init)
    s = sub.add_parser("record", help="append one entry, then check the cap")
    s.add_argument("ledger")
    s.add_argument("--amount", type=float, required=True)
    s.add_argument("--meta", nargs="*", default=[], metavar="k=v")
    s.add_argument("--ts", help="epoch seconds or ISO 8601; default now")
    s.set_defaults(fn=cmd_record)
    s = sub.add_parser("sum", help="total, optionally grouped by a meta key")
    s.add_argument("ledger")
    s.add_argument("--by", metavar="META_KEY")
    s.set_defaults(fn=cmd_sum)
    s = sub.add_parser("check", help="verify the hash chain, timestamps, and sidecar")
    s.add_argument("ledger")
    s.set_defaults(fn=cmd_check)
    return p


def run(argv):
    a = build_parser().parse_args(argv)
    return a.fn(a)


def selftest():
    def cap(argv):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = run(argv)
        return code, buf.getvalue()

    n = 0

    def case(name, ok):
        nonlocal n
        if not ok:
            print(f"SELFTEST: {name} FAILED")
            sys.exit(1)
        n += 1
        print(f"SELFTEST: {name} ok")

    with tempfile.TemporaryDirectory() as d:
        L = os.path.join(d, "l.jsonl")
        case("init", cap(["init", L, "--cap", "10", "--unit", "usd", "--ts", "100"])[0] == 0)
        case("record under cap", cap(["record", L, "--amount", "6", "--ts", "101", "--meta", "arm=a"])[0] == 0)
        code, out = cap(["record", L, "--amount", "5", "--ts", "102", "--meta", "arm=b"])
        case("cap exceeded exit 2", code == 2 and "LEDGER: CAP EXCEEDED" in out)
        case("crossing entry stays recorded", len(entries(L)) == 3)
        code, out = cap(["sum", L, "--by", "arm"])
        case("sum --by", "arm=a 6 usd" in out and "arm=b 5 usd" in out and "total 11 usd" in out)
        case("check intact", cap(["check", L])[0] == 0)
        cap(["record", L, "--amount", "1", "--ts", "50"])
        code, out = cap(["check", L])
        case("non-monotonic ts", code == 1 and "TS NOT MONOTONIC at line 4" in out)
        lines = open(L).read().splitlines()
        open(L, "w").write("\n".join(lines[:3]) + "\n")
        code, out = cap(["check", L])
        case("deleted tail TRUNCATED", code == 1 and "TRUNCATED" in out)
        open(L, "w").write("\n".join(lines[:1] + [lines[1].replace('"amount":6.0', '"amount":1.0')] + lines[2:]) + "\n")
        code, out = cap(["check", L])
        case("in-place edit BROKEN", code == 1 and "BROKEN at line 2" in out)
        os.remove(L + ".head")
        case("no sidecar", "NO SIDECAR" in cap(["check", L])[1])
    print(f"SELFTEST: all {n} passed")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv[1:]:
        sys.exit(selftest())
    sys.exit(run(sys.argv[1:]))
