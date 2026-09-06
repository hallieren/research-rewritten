# smol-army

Cost-aligned eval harness for the book *Research, Rewritten*: can a team of small
open models (9B / 14B / 20B) tie a frontier model? Pre-registration
(`docs/prereg.md`) was locked before any run; post-lock changes live in
`docs/CHANGES.md`.

## Run

```bash
uv sync --extra dev
uv run pytest                          # unit tests, offline
uv run python scripts/fetch_data.py    # build data/ slices
uv run python -m smol_army.run --mock  # offline end-to-end
OPENROUTER_API_KEY=... OPENAI_API_KEY=... uv run python -m smol_army.run
OPENROUTER_API_KEY=... OPENAI_API_KEY=... uv run python scripts/demo_naive.py  # ~a few cents; the book's Start Here chapter entry point
uv run python -m smol_army.report      # results/report.md + results.csv (--mock reads results_mock/)
```

The three army models call OpenRouter (`OPENROUTER_API_KEY`); the frontier arm
calls OpenAI (`OPENAI_API_KEY`). Set them with `export OPENROUTER_API_KEY=...`
and `export OPENAI_API_KEY=...`, or keep them in a `.env` file and load it with
`set -a && source .env && set +a`.

Every API call lands in `results/ledger.jsonl`; the run aborts past the $35 cap.
Runs are resumable, completed (family, item, arm, seed) keys are skipped.

`results/` ships the author's full run (3,580 rows, $5.58 of the cap), so a fresh
`run` against it finds nothing left to do. To reproduce from scratch, move
`results/runs.jsonl` and `results/ledger.jsonl` aside first. `--mock` writes to
`results_mock/` and never touches `results/`.

## Data

`data/SHA256SUMS` pins the task files. The files evaluated in 2026-07 were not
preserved and the hash file was never committed (`.gitignore` swallowed it). The
hashes are from a 2026-09 re-fetch, verified against the original run by
rescoring all 3,580 stored answers in `results/runs.jsonl` with zero changes and
by matching every MMLU-Pro question id (see `docs/CHANGES.md`, 2026-09-05).
After `fetch_data.py`, run `shasum -a 256 -c data/SHA256SUMS`. A mismatch means
the upstream row order changed, open an issue comparing your hashes.
