from smol_army.tasks import extract_answer
from smol_army.topologies import majority, run_vote, run_debate, run_division


def make_ask(outputs):
    it = iter(outputs)
    return lambda prompt: next(it)


def test_majority_basic():
    assert majority(["a", "b", "a"]) == "a"


def test_majority_ignores_none():
    assert majority([None, "b", None, "b", "a"]) == "b"


def test_majority_tie_first_wins():
    assert majority(["a", "b", "b", "a"]) == "a"


def test_majority_all_none():
    assert majority([None, None]) is None


def test_run_vote():
    ask = make_ask(["ANSWER: 4", "ANSWER: 5", "ANSWER: 4"])
    assert run_vote(ask, extract_answer, "2+2?", k=3) == "4"


def test_run_debate_call_count_and_answer():
    calls = []

    def ask(prompt):
        calls.append(prompt)
        return "ANSWER: 7"

    assert run_debate(ask, extract_answer, "q") == "7"
    assert len(calls) == 6  # 3 agents x 2 rounds


def test_run_division_chain():
    ask = make_ask(["1. step one", "so ANSWER: 9", "checked. ANSWER: 9"])
    assert run_division(ask, extract_answer, "q") == "9"
