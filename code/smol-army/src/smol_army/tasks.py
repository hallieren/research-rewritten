"""Task items ({id, family, prompt, answer[, tests]}), answer extraction, scoring."""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"

ANSWER_RE = re.compile(r"ANSWER:\s*(.+?)\s*$", re.MULTILINE)
CODE_RE = re.compile(r"```(?:python)?\n(.*?)```", re.DOTALL)


def load_family(family, limit):
    lines = (DATA / f"{family}.jsonl").read_text().splitlines()
    return [json.loads(l) for l in lines[:limit]]


def extract_answer(text):
    m = ANSWER_RE.search(text)
    return m.group(1).strip() if m else None


def extract_code(text):
    m = CODE_RE.search(text)
    return m.group(1) if m else text


def score_math(pred, gold):
    if pred is None:
        return 0
    norm = lambda s: s.replace(",", "").replace("$", "").replace("%", "").strip()
    try:
        return int(float(norm(pred)) == float(norm(gold)))
    except ValueError:
        return 0


def score_choice(pred, gold):
    return int(pred is not None and pred.strip().upper()[:1] == gold.strip().upper())


def score_code(pred_code, tests):
    """Run candidate + tests in a subprocess; pass iff exit code 0."""
    if pred_code is None:
        return 0
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(pred_code + "\n\n" + tests)
    try:
        r = subprocess.run([sys.executable, f.name], capture_output=True, timeout=30)
        return int(r.returncode == 0)
    except subprocess.TimeoutExpired:
        return 0


def score(family, pred, item):
    if family == "code":
        return score_code(pred, item["tests"])
    if family == "mmlu_pro":
        return score_choice(pred, item["answer"])
    return score_math(pred, item["answer"])
