import pytest
from smol_army.ledger import Ledger, BudgetExceeded

PRICES = {"m": {"in": 1.0, "out": 2.0}}


def test_cost_math(tmp_path):
    led = Ledger(tmp_path / "l.jsonl", PRICES, cap_usd=10)
    usd = led.record("m", {"prompt_tokens": 1_000_000, "completion_tokens": 500_000}, arm="x")
    assert usd == pytest.approx(2.0)


def test_cap_enforced(tmp_path):
    led = Ledger(tmp_path / "l.jsonl", PRICES, cap_usd=1.5)
    with pytest.raises(BudgetExceeded):
        led.record("m", {"prompt_tokens": 1_000_000, "completion_tokens": 500_000})


def test_resume_sums_existing(tmp_path):
    p = tmp_path / "l.jsonl"
    Ledger(p, PRICES, cap_usd=10).record("m", {"prompt_tokens": 1_000_000, "completion_tokens": 0})
    assert Ledger(p, PRICES, cap_usd=10).spent == pytest.approx(1.0)
