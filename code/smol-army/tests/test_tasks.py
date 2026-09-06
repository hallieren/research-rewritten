from smol_army.tasks import (extract_answer, extract_code, score_math,
                             score_choice, score_code)


def test_extract_answer():
    assert extract_answer("blah\nANSWER: 42") == "42"
    assert extract_answer("no answer here") is None


def test_extract_code():
    assert extract_code("```python\ndef f(): pass\n```") == "def f(): pass\n"
    assert extract_code("def f(): pass") == "def f(): pass"


def test_score_math_normalizes():
    assert score_math("1,000", "1000") == 1
    assert score_math("$7.0", "7") == 1
    assert score_math("20%", "20") == 1
    assert score_math("7", "8") == 0
    assert score_math("abc", "8") == 0
    assert score_math(None, "8") == 0


def test_score_choice():
    assert score_choice("B", "b") == 1
    assert score_choice("B. because", "B") == 1
    assert score_choice(None, "b") == 0


def test_score_code_pass_and_fail():
    assert score_code("def f():\n    return 4", "assert f() == 4") == 1
    assert score_code("def f():\n    return 5", "assert f() == 4") == 0
