# Pre-registration: Small-Model Army vs Frontier Model

Locked before any evaluation run. Changes after this commit go to `CHANGES.md` only.

## Hypothesis H

Under cost-aligned conditions, an ensemble ("army") of open-weight models (each ≤9B params)
matches a single frontier model's accuracy on the selected task families within
**ε = 2 percentage points**.

## Task families and slices

| Family | Source | Slice | Scoring |
|---|---|---|---|
| math | GSM-Symbolic (apple/GSM-Symbolic, `main` config) | first 150 | numeric exact match |
| mmlu_pro | TIGER-Lab/MMLU-Pro test | 150, stratified by category (seed 0) | letter exact match |
| code | evalplus/humanevalplus | first 100 | test execution pass |

Excluded by design: any open-ended-generation task scored by an LLM judge (judge preference
would contaminate the measurement). GSM-Symbolic chosen over GSM8K for contamination
resistance (perturbed variants).

## Arms

1. **frontier** — single call, temperature 0. Model ID locked immediately before the first
   real run and recorded in `CHANGES.md` (pre-registered as "current frontier tier").
2. **army_vote** — majority vote over k=5 samples, round-robin across Qwen3-8B,
   Llama-3.1-8B-Instruct, Gemma-2-9b-it. 3 seeds.
3. **self_consistency** — the critical control: majority vote over k=5 samples of a *single*
   small model (Qwen3-8B). Separates "teaming works" from "sampling works". k adjusted
   after a 20-item pilot so its USD/query matches army_vote within ±10% (recorded in
   CHANGES.md). 3 seeds.
4. **army_debate** — 3 agents (one per small model), 2 rounds, majority of final answers.
   1 seed, 100-item subslice per family (budget).
5. **army_division** — plan → solve → check role chain across the 3 small models. 1 seed,
   100-item subslice per family.

## Cost accounting

- **Primary:** USD per query at API list prices (per-call ledger, append-only JSONL).
  Second ledger view: local-deployment amortization, computed analytically from public
  GPU-rental $/hr and measured token throughput — not measured on local hardware.
- **Sensitivity:** active params × generated tokens (compute proxy).
- If the two ledgers disagree on the verdict, both are reported.

## Statistics

Paired bootstrap (10,000 resamples, seed 0) on per-item mean scores (averaged over seeds),
army arm vs frontier, per family. Readout:
- **tie** if the whole 95% CI ⊂ [−2pp, +2pp]
- **army_behind** if CI entirely below −2pp; **army_ahead** if entirely above +2pp
- otherwise **inconclusive**

## Falsification conditions

H is falsified if (a) every army topology is behind by >5pp on all three families, or
(b) a tie is only achievable at >2× the frontier arm's USD/query.

## Budget

Hard cap **$35** enforced by the ledger (run aborts on breach). Reserve lives outside this repo.

## Decision record

ε=2pp, USD-primary accounting, ≤9B size class, deferred frontier lock: decided by the
book's managing editor under delegated authority, 2026-07-18; author review may amend.
