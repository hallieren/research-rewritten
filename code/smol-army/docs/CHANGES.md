# Change record

Post-registration changes only. Format: date — field — old → new — reason.

- 2026-07-25 — frontier model — "current frontier tier, deferred" → **GPT-5.4 (OpenAI, full model)** — author supplied an OpenAI key and floated GPT-5.4-mini for cost; managing editor locked the full model instead: the frontier arm is single-call over ~400 items (≈$3-5 total), and substituting a mid-tier distill would hollow out the hypothesis ("tied the frontier"). Exact API slug to be verified against `/v1/models` before the first run.
- 2026-07-25 — small-model provider — DeepInfra → **OpenRouter** — author has an OpenRouter key. Model trio unchanged (qwen3-8b, llama-3.1-8b-instruct, gemma-2-9b-it, all ≤9B). Before the first run the OpenRouter catalog will be checked for strictly newer same-lineage ≤9B successors; any swap gets its own entry here.
- 2026-07-25 — price table — placeholder frontier prices → provisional GPT-5.4/OpenRouter prices — final verification against provider pricing immediately before the first run will be recorded here.
- 2026-07-25 — noted for later, NOT an arm change — author asked about cheap frontier-class open models (DeepSeek V4, GLM-5.2, Kimi) as substitutes. Decision: they enter, if at all, as a post-hoc **exploratory** baseline after the pre-registered readout; they are neither ≤9B (army) nor the closed frontier tier the hypothesis names.
- 2026-07-25 — frontier model — GPT-5.4 → **GPT-5.6-terra (OpenAI)** — author's explicit preference (author authority supersedes the editor's earlier lock). Still a frontier-tier closed model; hypothesis framing unchanged. Slug verified against `/v1/models` before first run.
- 2026-07-25 — army roster + size class — qwen3-8b / llama-3.1-8b / gemma-2-9b (≤9B, 2024-25 era) → **qwen3.5-9b / ministral-14b-2512 / gpt-oss-20b**; size class amended from "≤9B" to "**smallest practical band: ≤21B total params**" (9B dense / 14B dense / 21B-MoE-3.6B-active) — author rejected the stale trio and supplied a current OpenRouter menu across ~100B/~30B/smallest bands; editor picked the smallest band to keep the "small model" framing honest and the outcome genuinely uncertain. Three lineages preserved (Qwen / Mistral / OpenAI-oss). The ~100B band is parked as a possible post-hoc exploratory "mid-size army". Book text (ch05 5.4 / ch06 6.6) still says "≤9B" — flagged for author review.
- 2026-07-25 — self_consistency arm model — qwen3-8b (fixed) → **the army member with the highest accuracy on the 20-item cost-parity pilot** (rule fixed now, choice recorded here at pilot time; config default qwen3.5-9b until then) — strongest-single-model sampling is the harder, fairer control against the "teaming = just sampling" critique. Decided by managing editor.
- 2026-07-25 — small-model prices — provisional values → author-supplied OpenRouter prices (see prices.toml); frontier price still provisional until run-day verification.
- 2026-07-25 — run-day verification — all slugs confirmed live (`gpt-5.6-terra` on OpenAI `/v1/models`; all three army slugs on OpenRouter). Prices verified: OpenRouter API returns qwen3.5-9b $0.10/$0.15, ministral-14b $0.20/$0.20, gpt-oss-20b $0.030/$0.13 (last one corrected from $0.029/$0.14); GPT-5.6-terra $2.50/$15 per 1M (community pricing aggregators, consistent across sources). Tier note, recorded for honesty: terra is the *balanced* tier of the current GPT-5.6 frontier family — the flagship is Sol ($5/M in). The frontier arm is therefore "current frontier family, balanced tier", author-selected; the book must name the exact model.
- 2026-07-25 — tooling, not design — `run.py` gains a `--limit N` flag (caps items per family) for the pre-registered 20-item pilot.
- 2026-07-25 — tooling, not design — runner parallelized (ThreadPoolExecutor,
  16 workers; thread-safe ledger; 429/5xx retry with backoff in the client).
  Sequential full run would have taken ~15h wall-clock.
- 2026-07-25 — frontier decoding — prereg said "single call, temperature 0";
  GPT-5.6-terra is a reasoning model whose API rejects custom temperature
  (provider-fixed default 1) and requires max_completion_tokens. Frontier arm
  therefore decodes at the provider default with a fixed seed; hidden reasoning
  tokens are billed as completion tokens and counted by the ledger as-is.
  Budget 4096 completion tokens (reasoning included) to avoid truncation-zero
  scores. Discovered on first pilot attempt (400 errors), not anticipated.
- 2026-07-25 — decoding budget, small models — max_tokens 1024 → 4096 —
  qwen3.5-9b (and gpt-oss-20b) are reasoning models on OpenRouter; at 1024 they
  hit the length cap mid-think, returning truncated or null content (pilot crash).
  Null content now coalesces to "" (scored 0 only if genuinely no answer).
- 2026-07-25 — pilot bug log (harness, not design) — two scoring bugs caught by
  the pilot, both of which zeroed the *strongest* arms first: (1) numeric answers
  with a % suffix failed float parsing (GSM-Symbolic slice is percent-heavy) —
  scorer now strips %; (2) the code-family test harness (evalplus) imports numpy,
  which was missing from the venv, so every code run of every arm scored 0 —
  numpy added as a dependency. All stored answers rescored via scripts/rescore.py;
  38 null-answer rows (truncation-era) dropped and re-run.
- 2026-07-25 — SC model selection executed — per the pre-registered rule
  (pilot-best army member), 20-item probe accuracies: gpt-oss-20b 0.867,
  ministral-14b 0.850, qwen3.5-9b 0.533 → **self_consistency = gpt-oss-20b**.
  Pilot-era SC rows (run with qwen before selection) purged from runs.jsonl to
  avoid model mislabeling; ledger untouched (append-only).
- 2026-07-25 — decoding budget, qwen only — 4096 → 8192 — qwen3.5-9b returned
  no parseable answer on 28/60 probe items at 4096 (thinking timeout). Raised
  once; if it still times out at 8192 that is reported as a property of the
  member, not patched further. Probe/SC-selection numbers above were measured
  at 4096 and are not reopened.
- 2026-07-25 — post-hoc audit, NOT a change to the pre-registered analysis —
  the headline math result (army_vote +18.3pp over frontier) was audited before
  interpretation (scripts/audit_math.py). Findings: (1) all 49 frontier math
  misses sit in items math-100..149, one GSM-Symbolic probability template
  whose gold reads "how much more likely (as a percentage)" as an absolute
  percentage-point difference; frontier consistently answers the relative
  increase, which is exactly 4x gold in every variant (base probability 1/4).
  Ambiguous item, not a math error. (2) Excluding that template: frontier
  1.000, army_vote 0.977 (-2.3pp, 95% CI [-4.0, -0.7]) — the sign reverses.
  (3) The 150-item math slice contains only ~3 template families (50
  sequential variants each; fetch_data.py took the first 150 rows), so the
  effective sample size is far below 150 and the pre-registered CI overstates
  certainty for this family. The pre-registered numbers stand as registered;
  the clean-subset split is reported alongside them, labeled post-hoc.
- 2026-07-25 — book demo, NOT part of the registered analysis —
  scripts/demo_naive.py: the deliberately naive comparison the book's Start
  Here chapter walks the reader through (20 HumanEval+ items, gpt-oss-20b vs
  frontier, single call, no repeats/CI/ledger). Result: 19/20 vs 20/20.
  Written to results/demo_naive.jsonl, kept out of runs.jsonl.
- 2026-07-25 — erratum to the parallelization entry above — it says "16
  workers"; the committed run.py has always used 32 for real runs. 32 is what
  the full run executed with; the entry text was stale, the code was not.
- 2026-07-25 — book material, NOT part of the registered analysis —
  results/abstract_draft_raw.txt: a real "lazy first draft" abstract generated
  by the frontier model from results/report.md alone (pre-registered numbers,
  no audit context). Kept verbatim as the strength-drift specimen quoted in
  the book's delivery chapter ("达到或超越 frontier" — the unaudited +18
  presented as a win). One call, seed 0.
- 2026-07-25 — red-team finding, disposition: fixed + caveat — the evaluated
  item files (data/*.jsonl) were gitignored with no hash or dataset-revision
  anchor, so the evidence chain bottomed out in unverifiable local files.
  Fix: data/SHA256SUMS committed (hashes of the exact evaluated files).
  Remaining caveat: fetch_data.py does not pin HF dataset revisions, so
  re-fetching may not reproduce the slices bit-for-bit; the hashes define
  the evaluated corpus, the fetch script documents provenance only.
- 2026-07-25 — red-team round (four attack surfaces, independent sessions) —
  full case file with charges, replications, and dispositions in
  docs/redteam-2026-07-25.md. Headline dispositions: (1) the post-hoc clean-math
  "-2.3pp reversal" (entry above) is RETRACTED — scorer residue (`**`, `}`)
  one-sidedly zeroed correct small-model answers; relaxed extraction gives
  frontier 1.000 / army 0.9967 / SC 1.0000, and with 2 template families the
  subset is uninformative; (2) prereg's SC ±10% cost-parity clause was never
  executed (k stayed 5; SC ran at 0.21-0.77x army cost) — "same-budget" labels
  retracted, VIOLATION recorded; (3) code-family vote is mechanically degenerate
  (exact-string tally, tie -> first sample = qwen single sample; 4/5 calls
  bought nothing); (4) the mmlu slice is business/law/psychology only (3/14
  categories, STEM zero) — "stratified by category" was a misregistration;
  (5) ledger is list-price simulation, not billed cost (army ~19% under on demo
  evidence); 12.6% of real spend sits outside all reported USD/query figures;
  (6) frontier ran at observed zero reasoning tokens (undisclosed default) with
  asymmetric truncation remedies. Pre-registered numbers stand as registered;
  all restated conclusions are in the case file's closing section.
- 2026-07-26 — docs, not design — README erratum: env vars corrected to what
  config/run.toml actually reads (DEEPINFRA_API_KEY → OPENROUTER_API_KEY +
  OPENAI_API_KEY); demo_naive.py entry line, env setup notes, and Data section
  (SHA256SUMS mismatch guidance) added.
- 2026-09-05 — erratum to the red-team data-anchor entry above — it says
  "data/SHA256SUMS committed"; the file never entered any commit (`.gitignore`'s
  `data/` swallowed it) and the evaluated `data/*.jsonl` were not preserved.
  Fix: slices re-fetched with the unchanged fetch_data.py; all 3,580 stored
  answers in runs.jsonl rescored against the re-fetched gold/tests with zero
  changes, the MMLU-Pro question-id set matches exactly, and audit_math.py
  reproduces 49/49 and the clean-subset interval. data/SHA256SUMS now holds
  the hashes of that re-fetch, un-ignored and committed. The hashes anchor a
  corpus verified equivalent to the evaluated one on everything the scorer
  reads, not the original bytes.
- 2026-09-05 — tooling, not design — `--mock` runs write to `results_mock/`
  instead of `results/`; `report` gains `--mock` to read it. Reason: the repo
  ships the author's full runs.jsonl, so a reader's mock run resumed to zero
  jobs and, with any new item id, would have appended mock rows to the real
  evidence files. demo_naive.py drops a redundant sys.path hack.
