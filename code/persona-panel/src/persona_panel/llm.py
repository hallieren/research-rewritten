"""Minimal OpenAI-compatible chat client + offline mock."""
import json
import os
import time

import httpx


class LLM:
    def __init__(self, model, base_url, api_key_env, temperature=0.7, max_tokens=1024,
                 reasoning=False):
        self.model = model
        self.base_url = base_url
        self.api_key = os.environ[api_key_env]
        self.temperature = temperature
        self.max_tokens = max_tokens
        # Reasoning-model API contract: max_completion_tokens, provider-fixed temperature.
        self.reasoning = reasoning

    def chat(self, messages, seed=None):
        payload = {"model": self.model, "messages": messages,
                   **({"seed": seed} if seed is not None else {})}
        if self.reasoning:
            payload["max_completion_tokens"] = self.max_tokens
        else:
            payload["temperature"] = self.temperature
            payload["max_tokens"] = self.max_tokens
        for attempt in range(4):
            try:
                r = httpx.post(
                    f"{self.base_url}/chat/completions", timeout=300,
                    headers={"Authorization": f"Bearer {self.api_key}"},
                    json=payload)
                if r.status_code not in (429, 500, 502, 503):
                    r.raise_for_status()
                    d = r.json()
                    # Reasoning models may burn the whole budget thinking -> content None.
                    return d["choices"][0]["message"]["content"] or "", d["usage"]
            except (httpx.TransportError, json.JSONDecodeError, KeyError):
                # Provider hiccups: dropped connections, 200s with garbage bodies,
                # error payloads without "choices". Retry like a 5xx.
                if attempt == 3:
                    raise
            time.sleep(2 ** attempt)
        raise RuntimeError(f"{self.model}: retries exhausted")


class MockLLM:
    """Offline stand-in: fixed answer, fixed token counts."""
    model = "mock"

    def chat(self, messages, seed=None):
        return "2", {"prompt_tokens": 150, "completion_tokens": 5}
