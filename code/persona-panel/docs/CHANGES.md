# Change record

Post-registration changes only. Format: date — field — old → new — reason.

- 2026-07-24 — question domain label — prereg lists "competition Q120" → Q120
  kept, but in the official WVS-7 questionnaire Q120 is "risk of being held
  accountable for giving/receiving a bribe" (competition is Q109) — prereg
  mislabeled the ID; the pre-registered ID governs, official Q120 wording used
  in config/questions.toml.
- 2026-07-25 — interview model — "locked immediately before first run" →
  **GPT-5.4-mini (OpenAI)** — persona fidelity above the 8B class at low per-call
  cost (~10,800 calls ≈ $1-2). Sensitivity option: a qwen3-8b (OpenRouter) rerun
  stays configured under `models.small`, exploratory only.
- 2026-07-25 — price table — placeholder → provisional GPT-5.4-mini/OpenRouter
  prices — final verification against provider pricing before first run,
  recorded here.
- 2026-07-25 — sensitivity model — qwen3-8b → qwen3.5-9b (OpenRouter) — kept in
  lockstep with the smol-army roster refresh (author-supplied current menu).
  Interview model unchanged: GPT-5.4-mini.
- 2026-07-25 — ground-truth file — author downloaded the official v6.0
  "inverted" cross-national CSV (P-suffixed columns are direction-flipped).
  scripts/prepare_wvs.py maps the 7 affected items (Q1/Q2/Q5/Q6/Q46/Q131
  4-point, Q57 2-point) back to codebook coding; 10-point items are unchanged.
  Direction verified against published US anchors before transform (Q46 mode
  "rather happy" 62%, Q49 mean 7.2, Q57 trusted 40%). USA slice: 2,596 rows.
- 2026-07-25 — interview model API contract — gpt-5.4-mini uses the same
  reasoning-model contract as terra (max_completion_tokens, provider-fixed
  temperature); config gains reasoning=true, max_tokens=2048.
- 2026-07-26 — docs + harness, not design — README erratum (DEEPINFRA_API_KEY →
  OPENAI_API_KEY, the key config/run.toml actually reads) and prepare_wvs.py
  step added to the Data section; docs/data-license.md synced from v5.0 to the
  v6.0 inverted release; report exits with download/prepare guidance instead of
  a FileNotFoundError traceback when data/wvs7_usa.csv is absent.
- 2026-09-05 — tooling, not design — `--mock` runs write to `results_mock/`
  instead of `results/`; `report` gains `--mock` to read it. The repo ships the
  author's full answers.jsonl, so a reader's mock run resumed to zero jobs and
  could have appended mock rows to the real evidence files.
- 2026-09-05 — data shipping, not design — ground truth was only reachable by
  downloading WVS-7 yourself → repo now ships `data/wvs7_usa_aggregates.json`
  (per-subgroup answer counts, derived statistics; raw rows still not
  committed, see data-license.md §4). `prepare_wvs.py` writes it alongside
  the CSV; `report` falls back to it when the CSV is absent and prints which
  source it used. Metrics receive identical inputs either way (tested).
  Aggregates generated 2026-09-05 from a fresh download of the regular v6.0
  CSV (no P columns; prepare_wvs.py now detects the layout per column). USA
  slice 2,596 rows, anchors re-checked: Q1 very important 89.3%, Q46 rather
  happy 61.9%, Q57 trusted 39.7%, Q49 mean 7.22.
