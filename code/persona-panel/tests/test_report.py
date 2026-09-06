from persona_panel.report import contamination_flags, evaluate_subgroup

OPTIONS = ["1", "2"]


def test_evaluate_subgroup_pass():
    # persona and human distributions nearly identical on both questions
    persona = {"Q1": ["1"] * 7 + ["2"] * 3, "Q2": ["2"] * 6 + ["1"] * 4}
    human = {"Q1": ["1"] * 70 + ["2"] * 30, "Q2": ["2"] * 60 + ["1"] * 40}
    r = evaluate_subgroup(persona, human, {"Q1": OPTIONS, "Q2": OPTIONS})
    assert r["passes_a"] is True
    assert r["collapse_fraction"] < 1 / 3


def test_evaluate_subgroup_collapse():
    persona = {"Q1": ["1"] * 10, "Q2": ["2"] * 10}  # zero variance everywhere
    human = {"Q1": ["1", "2"] * 5, "Q2": ["1", "2"] * 5}
    r = evaluate_subgroup(persona, human, {"Q1": OPTIONS, "Q2": OPTIONS})
    assert r["collapse_fraction"] == 1.0


def test_contamination_flags():
    by_variant = {"Q1": {"original": ["1"] * 10, "p1": ["1"] * 9 + ["2"], "p2": ["1"] * 10},
                  "Q2": {"original": ["1"] * 10, "p1": ["2"] * 10, "p2": ["2"] * 10}}
    flags = contamination_flags(by_variant, {"Q1": OPTIONS, "Q2": OPTIONS})
    assert flags["Q1"] is False
    assert flags["Q2"] is True
