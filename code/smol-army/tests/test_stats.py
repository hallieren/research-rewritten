from smol_army.stats import paired_bootstrap, verdict


def test_bootstrap_zero_diff():
    a = [1, 0] * 50
    boot = paired_bootstrap(a, a, n=2000, seed=1)
    assert boot["mean"] == 0 and boot["ci_lo"] == 0 == boot["ci_hi"]


def test_bootstrap_detects_gap():
    a = [1] * 80 + [0] * 20
    b = [1] * 60 + [0] * 40
    boot = paired_bootstrap(a, b, n=2000, seed=1)
    assert boot["mean"] == 0.2
    assert boot["ci_lo"] > 0.05


def test_verdict_bands():
    assert verdict({"mean": 0, "ci_lo": -0.01, "ci_hi": 0.01}) == "tie"
    assert verdict({"mean": -0.1, "ci_lo": -0.15, "ci_hi": -0.05}) == "army_behind"
    assert verdict({"mean": 0.1, "ci_lo": 0.05, "ci_hi": 0.15}) == "army_ahead"
    assert verdict({"mean": 0.01, "ci_lo": -0.05, "ci_hi": 0.05}) == "inconclusive"
