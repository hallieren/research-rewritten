import json

from smol_army import report


def test_aggregate_and_compare(tmp_path):
    runs = [
        {"family": "math", "item_id": "m0", "arm": "frontier", "seed": 0, "score": 1, "usd": 0.01},
        {"family": "math", "item_id": "m1", "arm": "frontier", "seed": 0, "score": 0, "usd": 0.01},
        {"family": "math", "item_id": "m0", "arm": "army_vote", "seed": 0, "score": 1, "usd": 0.002},
        {"family": "math", "item_id": "m0", "arm": "army_vote", "seed": 1, "score": 0, "usd": 0.002},
        {"family": "math", "item_id": "m1", "arm": "army_vote", "seed": 0, "score": 1, "usd": 0.002},
        {"family": "math", "item_id": "m1", "arm": "army_vote", "seed": 1, "score": 1, "usd": 0.002},
    ]
    agg = report.aggregate(runs)
    assert agg[("math", "frontier")]["accuracy"] == 0.5
    assert agg[("math", "army_vote")]["accuracy"] == 0.75
    per = report.per_item(runs, "math", "army_vote")
    assert per == {"m0": 0.5, "m1": 1.0}
