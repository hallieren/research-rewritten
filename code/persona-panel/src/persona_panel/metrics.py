"""Distribution comparison metrics (pre-registered in docs/prereg.md)."""
import math
from collections import Counter


def dist(answers, option_codes):
    counts = Counter(answers)
    n = sum(counts[o] for o in option_codes)
    return [counts[o] / n if n else 0.0 for o in option_codes]


def _kl(p, q):
    return sum(pi * math.log2(pi / qi) for pi, qi in zip(p, q) if pi > 0)


def js_divergence(p, q):
    """Jensen-Shannon divergence, base 2 (0..1)."""
    m = [(pi + qi) / 2 for pi, qi in zip(p, q)]
    return _kl(p, m) / 2 + _kl(q, m) / 2


def top_choice_match(p, q):
    return p.index(max(p)) == q.index(max(q))


def variance(answers):
    xs = [float(a) for a in answers]
    mu = sum(xs) / len(xs)
    return sum((x - mu) ** 2 for x in xs) / len(xs)


def variance_ratio(persona_answers, human_answers):
    hv = variance(human_answers)
    return variance(persona_answers) / hv if hv else float("inf")
