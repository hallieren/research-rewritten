import pytest

from persona_panel.metrics import dist, js_divergence, top_choice_match, variance_ratio


def test_dist_normalizes_and_orders():
    assert dist(["1", "1", "2"], ["1", "2", "3"]) == [2 / 3, 1 / 3, 0.0]


def test_dist_empty_is_zeros():
    assert dist([], ["1", "2"]) == [0.0, 0.0]


def test_js_zero_for_identical():
    assert js_divergence([0.5, 0.5], [0.5, 0.5]) == 0


def test_js_one_for_disjoint():
    assert js_divergence([1.0, 0.0], [0.0, 1.0]) == pytest.approx(1.0)


def test_top_choice_match():
    assert top_choice_match([0.7, 0.3], [0.6, 0.4]) is True
    assert top_choice_match([0.7, 0.3], [0.4, 0.6]) is False


def test_variance_ratio_collapse():
    persona = ["3"] * 10
    human = ["1", "5", "3", "2", "4"] * 2
    assert variance_ratio(persona, human) == 0.0
