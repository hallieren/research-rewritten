# Pre-registration: Can LLM Persona Panels Stand In for Survey Respondents?

Locked before any run. Changes after this commit go to `CHANGES.md` only.

## Question

Do answer distributions from LLM personas, prompted with real demographic profiles,
match the answer distributions of the corresponding real human subgroups on
World Values Survey (Wave 7) questions — without systematic stereotyping drift?

## Ground truth

- **Single source:** WVS Wave 7, USA respondents (user-downloaded CSV; never committed).
- **Design change (2026-07-24):** the original ch12 design had a second arm — n≈20-30
  fresh structured human interviews as a contamination-immune calibration source. The
  author cannot recruit; that arm is cancelled. Consequence: the paraphrase contamination
  check below is mandatory, and all conclusions carry the caveat that ground truth may
  itself sit inside model training corpora.

## Design

- **Subgroups (6):** USA × sex {male, female} × age band {18-29, 30-49, 50+}.
- **Personas:** 40 per subgroup, deterministic cards (seeded age/occupation jitter).
- **Questions:** 15 WVS-7 items across value domains (family Q1, friends Q2, work Q5,
  religion Q6, competition Q120, neighborhood security Q131, happiness Q46, life
  satisfaction Q49, trust Q57, income equality Q106, science & tech Q158, importance of
  God Q164, abortion Q184, divorce Q185, left-right scale Q240).
- **Variants:** each question asked as original + 2 hand-written paraphrases.
- **Interview mode:** independent single-turn calls (one question per call). This measures
  distribution match, not conversational consistency — stated limitation.
- **Interview model:** locked immediately before the first real run; recorded in CHANGES.md.

## Criteria (pass/fail per pre-registration)

- **(a) Distribution match:** per subgroup, median Jensen-Shannon divergence (base 2)
  between persona and human answer distributions ≤ 0.10 bits AND top-choice agreement on
  ≥ 70% of questions.
- **(b) Variance-collapse red line:** persona variance / human variance < 0.5 on more than
  1/3 of questions in any subgroup → stereotyping collapse, (a) cannot rescue the verdict.
- **(c) Subgroup cross-check:** (a) must hold in ≥ 5 of 6 sex×age cells, and no cell may
  exceed median JS 0.20.
- **Contamination check:** per question, JS between persona answers on original vs pooled
  paraphrases > 0.05 → flag as contamination-suspect; excluded from (a) and reported.

## Falsification shape

If (a) fails on most subgroups or (b) triggers, "persona panels can stand in for human
respondents in pre-research" is falsified for this setting; the downgraded claim
"useful only for questionnaire-wording dry runs" remains separately assessable.

## Budget

Hard cap **$10** enforced by the ledger.

## Decision record

Thresholds in (a)-(c) and the contamination threshold set by the book's managing editor
under delegated authority, 2026-07-24; author review may amend.
