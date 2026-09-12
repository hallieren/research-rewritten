#!/usr/bin/env python3
"""n is the number of independent units, not the number of rows.

Rule enforced: a confidence interval assumes independence, so the naive
per-row interval and the clustered interval are printed side by side. When
they disagree, the clustered one is the one to report. Zero variance withholds
the verdict. Verdicts come from a closed list: tie, ahead, behind, inconclusive.
"""
import argparse, contextlib, csv, io, json, math, os, random, sys, tempfile

WIDTH_RATIO = 1.5  # clustered interval 1.5x wider than naive means the rows were not independent
MIN_CLUSTERS = 5  # below 5 clusters the cluster bootstrap only returns the range of cluster means


def load(path):
    if path.endswith(".jsonl"):
        with open(path) as f:
            return [json.loads(line) for line in f if line.strip()]
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def percentile_ci(means):
    means = sorted(means)
    return means[int(0.025 * len(means))], means[int(0.975 * len(means))]


def verdict(lo, hi, eps):
    if -eps <= lo and hi <= eps:
        return "tie"
    if lo > eps:
        return "ahead"
    if hi < -eps:
        return "behind"
    return "inconclusive"


def naive_bootstrap(diffs, n, rng):
    return percentile_ci(sum(rng.choices(diffs, k=len(diffs))) / len(diffs) for _ in range(n))


def cluster_bootstrap(groups, n, rng):
    keys = list(groups)
    means = []
    for _ in range(n):
        pool = [d for k in rng.choices(keys, k=len(keys)) for d in groups[k]]
        means.append(sum(pool) / len(pool))
    return percentile_ci(means)


def cmd_count(a):
    rows = load(a.file)
    if not a.cluster:
        print(f"N: n={len(rows)} rows, independent units UNKNOWN (no cluster column given; rows may share a template, source, session, or author)")
        return 0
    sizes = {}
    for r in rows:
        key = r[a.item] if a.item else id(r)
        sizes.setdefault(r[a.cluster], set()).add(key)
    print(f"N: n={len(rows)} rows, {len(sizes)} independent units (cluster={a.cluster})")
    print("N: sizes " + ", ".join(f"{k}={len(v)}" for k, v in sorted(sizes.items())))
    return 0


def cmd_compare(a):
    rows = load(a.file)
    scores, cluster_of = {}, {}
    for r in rows:
        if r[a.arm] in (a.a, a.b):
            scores.setdefault((r[a.item], r[a.arm]), []).append(float(r[a.score]))
            if a.cluster:
                cluster_of.setdefault(r[a.item], r[a.cluster])
    items = sorted({i for i, arm in scores if (i, a.a) in scores and (i, a.b) in scores})
    if not items:
        print("usage error: no item appears in both arms", file=sys.stderr)
        return 2
    mean = lambda xs: sum(xs) / len(xs)
    diffs = {i: mean(scores[(i, a.a)]) - mean(scores[(i, a.b)]) for i in items}
    k = len(set(cluster_of.values())) if a.cluster else 0
    print(f"N: n={len(items)} rows (items paired across arms {a.a},{a.b}), "
          + (f"{k} independent units (cluster={a.cluster})" if a.cluster else "independent units UNKNOWN (no cluster column given)"))
    if len(set(diffs.values())) == 1:
        print("DEGENERATE: zero variance in diffs, verdict withheld")
        return 1
    rng = random.Random(a.seed)
    d = list(diffs.values())
    lo, hi = naive_bootstrap(d, a.resamples, rng)
    v_naive = verdict(lo, hi, a.eps)
    print(f"NAIVE: diff {mean(d):+.4f} CI[{lo:+.4f},{hi:+.4f}] verdict={v_naive} (eps={a.eps}, assumes {len(d)} independent rows)")
    if not a.cluster:
        return 0
    groups = {}
    for i in items:
        groups.setdefault(cluster_of[i], []).append(diffs[i])
    clo, chi = cluster_bootstrap(groups, a.resamples, rng)
    v_cl = verdict(clo, chi, a.eps)
    print(f"CLUSTERED({k}): diff {mean(d):+.4f} CI[{clo:+.4f},{chi:+.4f}] verdict={v_cl} (eps={a.eps}, {k} clusters)")
    ratio = (chi - clo) / (hi - lo) if hi > lo else math.inf
    print(f"WIDTH: clustered/naive = {ratio:.2f}x")
    if k < MIN_CLUSTERS:
        print(f"CLUSTERS: k<{MIN_CLUSTERS}, clustered interval is the range of cluster means, this data cannot decide")
    if ratio > WIDTH_RATIO or v_naive != v_cl:
        print("INDEPENDENCE: rows are not independent units; report the clustered interval")
        return 1
    return 0


def cmd_synth(a):
    rng = random.Random(a.seed)
    per = a.rows // a.clusters
    out = []
    for i in range(per * a.clusters):
        c = i // per + 1
        base = 0.3 + 0.4 * rng.random()
        out.append({"item": f"i{i}", "arm": "B", "cluster": f"c{c}", "score": round(base, 4)})
        bump = a.shift if c == a.clusters else 0.0
        out.append({"item": f"i{i}", "arm": "A", "cluster": f"c{c}", "score": round(base + bump + rng.gauss(0, 0.05), 4)})
    if a.out.endswith(".jsonl"):
        with open(a.out, "w") as f:
            f.writelines(json.dumps(r) + "\n" for r in out)
    else:
        with open(a.out, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    print(f"N: wrote {len(out)} rows, {per * a.clusters} items, {a.clusters} clusters, arms A,B to {a.out}")
    return 0


def build_parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--selftest", action="store_true", help="run the built-in checks and exit")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("count", help="rows versus independent units")
    s.add_argument("file")
    s.add_argument("--cluster")
    s.add_argument("--item")
    s.set_defaults(fn=cmd_count)
    s = sub.add_parser("compare", help="paired bootstrap of arm a minus arm b, naive and clustered")
    s.add_argument("file")
    for col in ("score", "item", "arm", "a", "b"):
        s.add_argument(f"--{col}", required=True)
    s.add_argument("--cluster")
    s.add_argument("--eps", type=float, default=0.02, help="equivalence margin, 2 points is the usual tie band")
    s.add_argument("--resamples", type=int, default=5000)
    s.add_argument("--seed", type=int, default=0)
    s.set_defaults(fn=cmd_compare)
    s = sub.add_parser("synth", help="write a clustered synthetic file for a dry run")
    s.add_argument("out")
    s.add_argument("--rows", type=int, default=150, help="items per arm")
    s.add_argument("--clusters", type=int, default=3)
    s.add_argument("--shift", type=float, default=0.6, help="lift on arm A in the last cluster only")
    s.add_argument("--seed", type=int, default=0)
    s.set_defaults(fn=cmd_synth)
    return p


def run(argv):
    a = build_parser().parse_args(argv); return a.fn(a)


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

    cmp = ["--score", "score", "--item", "item", "--arm", "arm", "--a", "A", "--b", "B", "--cluster", "cluster"]
    with tempfile.TemporaryDirectory() as d:
        J, C = os.path.join(d, "s.jsonl"), os.path.join(d, "s.csv")
        cap(["synth", J, "--rows", "150", "--clusters", "3"])
        code, out = cap(["compare", J, *cmp, "--resamples", "1000"])
        case("naive ahead, clustered inconclusive", "verdict=ahead" in out and "verdict=inconclusive" in out)
        w = [float(l.split("= ")[1].rstrip("x")) for l in out.splitlines() if l.startswith("WIDTH:")]
        case("clustered wider", w and w[0] > 1.0 and "INDEPENDENCE:" in out and code == 1)
        case("k<5 line", "CLUSTERS: k<5" in out)
        code, out2 = cap(["count", J, "--cluster", "cluster", "--item", "item"])
        case("count units", "3 independent units" in out2 and "c1=50" in out2)
        cap(["synth", C, "--rows", "150", "--clusters", "3"])
        case("CSV round-trip identical", cap(["compare", C, *cmp, "--resamples", "1000"])[1] == out)
        with open(J, "w") as f:
            f.writelines(json.dumps({"item": i, "arm": arm, "cluster": 1, "score": 1}) + "\n" for i in range(10) for arm in "AB")
        code, out = cap(["compare", J, *cmp])
        case("all-equal DEGENERATE", code == 1 and "DEGENERATE:" in out)
    print(f"SELFTEST: all {n} passed")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv[1:]:
        sys.exit(selftest())
    sys.exit(run(sys.argv[1:]))
