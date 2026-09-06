import re

from persona_panel.personas import make_card

SG = {"name": "usa-m-18-29", "country": "USA", "sex": "male", "age_lo": 18, "age_hi": 29}


def test_deterministic():
    assert make_card(SG, 3) == make_card(SG, 3)
    assert make_card(SG, 3) != make_card(SG, 4)


def test_age_in_band():
    age = int(re.search(r"Age: (\d+)", make_card(SG, 0)).group(1))
    assert 18 <= age <= 29
