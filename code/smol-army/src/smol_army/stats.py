"""Paired bootstrap and the pre-registered equivalence readout."""
import random


def paired_bootstrap(a, b, n=10_000, seed=0):
    """95% CI for mean(a - b) over paired per-item scores."""
    rng = random.Random(seed)
    diffs = [x - y for x, y in zip(a, b, strict=True)]
    m = len(diffs)
    means = sorted(sum(rng.choices(diffs, k=m)) / m for _ in range(n))
    return {"mean": sum(diffs) / m,
            "ci_lo": means[int(0.025 * n)], "ci_hi": means[int(0.975 * n)]}


def verdict(boot, eps=0.02):
    """Pre-registered readout: tie only if the whole CI sits inside ±eps."""
    if -eps <= boot["ci_lo"] and boot["ci_hi"] <= eps:
        return "tie"
    if boot["ci_hi"] < -eps:
        return "army_behind"
    if boot["ci_lo"] > eps:
        return "army_ahead"
    return "inconclusive"
