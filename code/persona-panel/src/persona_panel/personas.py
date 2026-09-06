"""Deterministic persona cards for a demographic subgroup."""
import random

OCCUPATIONS = [
    "public school teacher", "registered nurse", "software developer",
    "retail sales associate", "truck driver", "restaurant server",
    "accountant", "construction worker", "office administrator",
    "warehouse worker", "hair stylist", "electrician",
    "customer service representative", "small business owner", "retired",
]


def make_card(subgroup, i):
    rng = random.Random(f"{subgroup['name']}-{i}")
    age = rng.randint(subgroup["age_lo"], min(subgroup["age_hi"], 85))
    occupation = rng.choice(OCCUPATIONS)
    return (f"- Age: {age}\n- Gender: {subgroup['sex']}\n"
            f"- Country: {subgroup['country']}\n- Occupation: {occupation}")
