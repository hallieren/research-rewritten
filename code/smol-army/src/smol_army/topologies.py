"""Team topologies. Each takes ask(prompt) -> text and returns a final answer."""
from collections import Counter


def majority(answers):
    """Most common non-None answer; ties break to earliest occurrence."""
    counts = Counter(a for a in answers if a is not None)
    if not counts:
        return None
    top = max(counts.values())
    for a in answers:
        if a is not None and counts[a] == top:
            return a


def run_vote(ask, extract, prompt, k):
    return majority([extract(ask(prompt)) for _ in range(k)])


def run_debate(ask, extract, prompt, agents=3, rounds=2):
    views = [ask(prompt) for _ in range(agents)]
    for _ in range(rounds - 1):
        views = [ask(f"{prompt}\n\nOther agents answered:\n"
                     + "\n---\n".join(v for j, v in enumerate(views) if j != i)
                     + "\n\nReconsider and give your final answer.")
                 for i in range(agents)]
    return majority([extract(v) for v in views])


def run_division(ask, extract, prompt):
    plan = ask(f"Break this problem into steps. Do not solve it.\n\n{prompt}")
    solution = ask(f"{prompt}\n\nA colleague suggests this plan:\n{plan}\n\nSolve it.")
    check = ask(f"{prompt}\n\nProposed solution:\n{solution}\n\n"
                "Verify it. Give the corrected final answer if wrong; restate it if right.")
    return extract(check)
