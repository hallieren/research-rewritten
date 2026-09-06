from persona_panel.metrics import dist, variance
from persona_panel.wvs import aggregate, answers_for, expand, load_responses, subgroup_rows

CSV = """B_COUNTRY_ALPHA,Q260,Q262,Q46
USA,1,25,1
USA,2,45,2
USA,1,70,-1
DEU,1,30,1
"""


def make_rows(tmp_path):
    p = tmp_path / "wvs.csv"
    p.write_text(CSV)
    return load_responses(p, ["Q46"])


def test_load(tmp_path):
    assert len(make_rows(tmp_path)) == 4


def test_subgroup_filter(tmp_path):
    sg = {"country": "USA", "sex_code": "1", "age_lo": 18, "age_hi": 29}
    sub = subgroup_rows(make_rows(tmp_path), sg)
    assert len(sub) == 1
    assert answers_for(sub, "Q46") == ["1"]


def test_negative_codes_dropped(tmp_path):
    sg = {"country": "USA", "sex_code": "1", "age_lo": 60, "age_hi": 80}
    sub = subgroup_rows(make_rows(tmp_path), sg)
    assert answers_for(sub, "Q46") == []  # -1 is a WVS missing code


def test_aggregate_roundtrip_matches_raw(tmp_path):
    sg = {"name": "usa-all", "country": "USA", "sex_code": "1", "age_lo": 18, "age_hi": 80}
    rows = make_rows(tmp_path)
    agg = aggregate(rows, [sg], ["Q46"])
    assert agg == {"usa-all": {"Q46": {"1": 1}}}  # -1 dropped, DEU and sex 2 excluded
    raw = answers_for(subgroup_rows(rows, sg), "Q46")
    via_agg = expand(agg["usa-all"]["Q46"])
    assert dist(via_agg, ["1", "2"]) == dist(raw, ["1", "2"])
    assert variance(via_agg) == variance(raw)
