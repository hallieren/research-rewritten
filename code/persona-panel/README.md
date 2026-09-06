# persona-panel

Companion repo for the book *Research, Rewritten*: do LLM persona panels answer
like the real human subgroups they imitate? Ground truth is World Values Survey
Wave 7 (USA). Pre-registration (`docs/prereg.md`) was locked before any run.

## Data

WVS-7 raw respondent rows cannot be redistributed, so the repo does not ship
them. It ships `data/wvs7_usa_aggregates.json` instead: per-subgroup,
per-question answer counts derived from the USA slice, which is all the
pre-registered metrics need. `report` reads it when the raw CSV is absent, so
the readout reproduces without any download.

To regenerate from the source, register and download the official v6.0
cross-national CSV yourself (regular or "inverted" layout, both handled) (see `docs/data-license.md`), then:

```bash
uv run python scripts/prepare_wvs.py <path-to-official-csv>
```

This writes `data/wvs7_usa.csv` (gitignored; for the inverted layout the script
maps the P-suffixed, direction-flipped columns back to codebook coding) and rewrites the
aggregates file. With the CSV present, `report` uses the raw rows.

## Run

```bash
uv sync --extra dev
uv run pytest                             # offline unit tests
uv run python -m persona_panel.run --mock # offline end-to-end
OPENAI_API_KEY=... uv run python -m persona_panel.run
uv run python -m persona_panel.report     # pre-registered readout (--mock reads results_mock/)
```

Hard $10 budget cap; every call in `results/ledger.jsonl`; resumable.

`results/` ships the author's full run (10,800 answers), so a fresh `run` against
it finds nothing left to do. To re-run from scratch, move `results/answers.jsonl`
and `results/ledger.jsonl` aside first. `--mock` writes to `results_mock/` and
never touches `results/`.
