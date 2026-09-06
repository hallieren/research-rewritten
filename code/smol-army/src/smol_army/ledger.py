"""Append-only JSONL cost ledger with a hard budget cap. Thread-safe."""
import json
import threading
import time
from pathlib import Path


class BudgetExceeded(RuntimeError):
    pass


class Ledger:
    def __init__(self, path, prices, cap_usd):
        self.path = Path(path)
        self.prices = prices
        self.cap = cap_usd
        self.spent = sum(e["usd"] for e in self.entries())
        self._lock = threading.Lock()

    def entries(self):
        if not self.path.exists():
            return []
        return [json.loads(l) for l in self.path.read_text().splitlines() if l]

    def cost(self, model, usage):
        p = self.prices[model]
        return usage["prompt_tokens"] / 1e6 * p["in"] + usage["completion_tokens"] / 1e6 * p["out"]

    def record(self, model, usage, **meta):
        usd = self.cost(model, usage)
        entry = {"ts": time.time(), "model": model, "usd": round(usd, 8),
                 "in": usage["prompt_tokens"], "out": usage["completion_tokens"], **meta}
        with self._lock:
            with self.path.open("a") as f:
                f.write(json.dumps(entry) + "\n")
            self.spent += usd
            if self.spent > self.cap:
                raise BudgetExceeded(f"spent ${self.spent:.2f} > cap ${self.cap}")
        return usd
