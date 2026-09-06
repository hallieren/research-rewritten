# Chapter 9 templates · Two Real Deliverables + Claims List / Technical-Report Skeleton / One-Page Memo Templates + Delivery Prompt Set

> This appendix comes in two parts. Part one holds the book case's **two real deliverables**, the technical-report skeleton (shaped like a workshop paper) and the CTO one-page memo from the small-model army experiment. Every number points at a results file and a commit in the smol-army repo (`code/smol-army`) and can be recomputed one by one. The honest account. These two documents were delivered to this book's case library. **Nothing was submitted, no conference accepted them, and no CTO ever signed off on them.** The book does not invent those events. Part two is the fillable template version.
> The order of use is fixed. Write Template 1 first (the claims list) → use Template 2/3 to produce the two vehicles → run the prompt set's interlock check → the signature test sentence by sentence.

---

# Part One · Real Deliverables

## Deliverable one, the technical-report skeleton (shaped like a workshop paper, real numbers)

```text
Title: When does a small-model army pay off? A preregistered five-arm comparison with real cost
accounting and an equal-budget self-consistency control
(Working title: When Does a Small-Model Army Pay Off? A Pre-registered,
Cost-Accounted Comparison with a Self-Consistency Control)

=== Abstract ===
Can a team of small open-source models tie a single frontier model on a cost-matched basis? The literature splits into two camps,
but the decision-grade comparison combining "dollar-basis accounting + an equal-budget self-consistency control + several task families" is missing.
We preregistered (criteria before any result commit) a five-arm comparison. GPT-5.6-terra single shot vs
the vote/debate/division armies of three open-source small models (total parameters ≤21B) vs self-consistency on the strongest member,
across three task families (GSM-Symbolic 150, MMLU-Pro 150, HumanEval+ 100), total cost $5.58.
The result is highly task-dependent. On code the army and frontier cannot be told apart (93.7% vs 96.0%, CI crossing zero)
at 1/5 the unit price; on knowledge QA the army trails by 14.9pp [−21.3, −8.7]; on math the preregistered reading gives the army
+18.2pp [+12.7, +24.2], but a pre-announced audit found all 49 frontier wrong answers came from a single ambiguous template
(each wrong answer exactly 4 times the gold answer), and after removal the direction reverses to −2.3pp [−4.0, −0.7]. Both sets of
numbers are reported side by side. On clean data the army and self-consistency cannot be told apart (0.977 vs 0.983). This experiment
gives no evidence for any contribution of "teaming" over "multi-sampling." Preregistration, the append-only ledger, and the audit script are all public.

=== 1 Problem and related work (skeleton) ===
· The enthusiasts. Sampling and voting gains (Li et al., TMLR 2024); open-source layered aggregation beats GPT-4o (length-controlled
  basis; Wang et al., ICLR 2025); multi-model debate (Du et al., ICML 2024).
· The skeptics. Performance is non-monotonic in the number of calls (Chen et al., NeurIPS 2024); under default settings debate loses to
  self-consistency (Smit et al., ICML 2024); a single agent with a strong prompt nearly matches discussion
  (Wang et al., ACL 2024).
· Where this paper stands (the narrowed contribution). It does not claim to fill a "cost-alignment gap" (comparisons of that kind already exist on the
  skeptics' side). The contribution is drawing the task-dependence boundary + decision-grade real accounting. Dollars per query as the main basis, an equal-budget
  self-consistency control arm, three task families, preregistered criteria, and a fully public ledger.

=== 2 Method ===
2.1 Hypothesis and criteria (preregistration precedes results entering the repo; after that every change goes only into CHANGES.md)
· H: On a cost-matched basis, the accuracy gap between the open-source small-model army and a
  single frontier model on the chosen task families is ≤ ε = 2pp.
· Reading: paired bootstrap, 10,000 resamples (seed 0). A 95% CI falling entirely inside [−2, +2] is a tie;
  entirely above is army_ahead; entirely below is army_behind; anything else is inconclusive.
· Falsification conditions: (a) the army trails by >5pp on all three families, or (b) it catches up only at >2× frontier's unit price.

2.2 Task families
| Family | Source | Slice | Scoring |
|---|---|---|---|
| math | GSM-Symbolic (contamination-resistant perturbed variants) | first 150 problems | exact numeric match |
| mmlu_pro | MMLU-Pro test | 150 problems stratified by category (seed 0) | exact option match |
| code | HumanEval+ | first 100 problems | test execution passes |
Excluded by design: every open-generation task scored by an LLM judge (judge preference would contaminate the measurement).

2.3 Arms and models (list price in $/1M tokens, input/output)
| Arm | Configuration |
|---|---|
| frontier | GPT-5.6-terra single shot ($2.50/$15; a reasoning model, provider default decoding, see the change log) |
| army_vote | k=5 majority vote, rotating qwen3.5-9b ($0.10/$0.15) / ministral-14b-2512 ($0.20/$0.20) / gpt-oss-20b ($0.030/$0.13), 3 seeds |
| self_consistency | the steelman arm: one model, k=5 majority vote; the member picked by the preregistered rule as the strongest on a 20-problem probe = gpt-oss-20b (probe 0.867), 3 seeds |
| army_debate | 3 agents × 2 rounds, majority vote on the final answer, a 100-problem sub-slice per family, 1 seed |
| army_division | plan→solve→check role chain, a 100-problem sub-slice per family, 1 seed |
Army size tier: total parameters per model ≤21B (9B dense / 14B dense / 21B-MoE-3.6B active).

2.4 Cost and execution
Dollars per query (API list price), an append-only ledger recording every call, budget hard cap
$35. 3,580 result lines in full, actual total cost $5.58, 0 failures.

=== 3 Results ===
3.1 Main table (accuracy and $/query)
| Family | frontier | army_vote | self_consistency | army_debate | army_division |
|---|---|---|---|---|---|
| code | 0.960 ($0.00269) | 0.937 ($0.00053) | 0.947 ($0.00041) | 0.940 ($0.00083) | 0.940 ($0.00108) |
| math | 0.673 ($0.00195) | 0.856 ($0.00199) | 0.733 ($0.00041) | 1.000† ($0.00152) | 1.000† ($0.00103) |
| mmlu_pro | 0.793 ($0.00498) | 0.644 ($0.00223) | 0.616 ($0.00083) | 0.740 ($0.00228) | 0.630 ($0.00125) |
† The 100-problem sub-slice for debate/division happens to exclude the ambiguous-template stretch (math-100..149, see 3.3),
  the stretch that holds all of frontier's wrong answers; both arms and frontier score full marks on this sub-slice, Δ=0;
  the sub-slice is also hit by the zero-variance degenerate-interval artifact, see charge ⑨ in Chapter 10.

3.2 Preregistered reading (army arm − frontier, 95% CI)
| Family | army_vote | self_consistency |
|---|---|---|
| code | −2.3pp [−6.0, +1.7] inconclusive | −1.3pp [−3.7, +1.0] inconclusive |
| math | +18.2pp [+12.7, +24.2] army_ahead | +6.0pp [+3.1, +9.1] army_ahead |
| mmlu_pro | −14.9pp [−21.3, −8.7] army_behind | −17.8pp [−24.9, −10.9] army_behind |
(debate/division: code −2.0 / −2.0, both inconclusive; math both Δ=0 tie, see †;
mmlu −8.0 inconclusive / −19.0 army_behind.)

3.3 Post-hoc audit (post-hoc, pre-announced; scripts/audit_math.py, the post-hoc audit entry in CHANGES.md)
· All 49 frontier math wrong answers fall in math-100..149 (the 50 variants of a single GSM-Symbolic probability template).
  Each wrong answer is exactly 4 times gold and carries a %. The mechanism: the problem text "how much more
  likely (as a percentage)" has two readings, gold takes the absolute percentage-point difference, frontier always answers the
  relative multiple; the template's base probability is always 1/4, so the relative reading always equals 4×gold. Ruling: an ambiguous problem,
  not a math error. On the ambiguous template, army_vote 0.61 / self_consistency 0.23 / frontier 0.02.
  The army's "overtake" is three lineages' distribution of readings happening to land on gold's reading, not a reasoning advantage.
· Remove that template: frontier 1.000, army_vote 0.977, self_consistency 0.983;
  army_vote − frontier = −2.3pp [−4.0, −0.7], direction reversed.
· Data composition: the 150 math problems are really only ~3 template families (50 sequential variants each, sampled without shuffling),
  the effective sample size is far below 150, and the preregistered CI is overconfident for this family.
· Reporting discipline: the preregistered numbers are reported as is (3.2), and this section breaks them out side by side, labeled post-hoc, replacing nothing.

3.4 Criteria reconciliation
Falsification condition (a) not triggered (code's CI crosses zero); (b) not triggered (army unit price: on code 1/5 of
frontier's, on mmlu less than half, on math about equal, and no family bought a tie with more money). H is not falsified and does not
hold across the board. The landing point is task dependence. code has a shot, knowledge QA has no shot, the math evidence is void pending a retest.

=== 4 Limitations (written for real) ===
1. Template concentration in the math slice: ~3 template families were treated as 150 independent samples, the bootstrap independence assumption fails,
   and the preregistered CI is overconfident for this family; a retest needs a template-shuffled problem set with enough families.
2. The math direction reversal comes from a post-hoc breakdown: −2.3pp is a post-hoc number and may be made official only after a preregistered retest
   next round; this round draws no conclusion on math.
3. Code's preregistered reading is inconclusive, not tie: 100 problems cannot squeeze out a ±2pp equivalence band;
   "cannot be told apart" is a decision-grade statement, not a statistical equivalence ruling.
4. A single cost basis, API list price only. The self-hosted amortization basis promised in the preregistration (computed analytically from GPU rental prices)
   was not executed and is recorded as outstanding; the two accounts may give different conclusions.
5. Frontier is one model at one point in time, and it is the balanced tier of the GPT-5.6 family
   (terra), not the flagship tier (Sol); the conclusion is limited to that tier.
6. On clean data the army ≈ self-consistency (0.977 vs 0.983; on code SC is cheaper): this
   experiment can give no evidence at all for the contribution of the "teaming" mechanism itself.
7. The contamination-resistant design covers only the math family (perturbed variants);
   HumanEval+ and MMLU-Pro may sit inside the training corpora of the models evaluated.

=== 5 Reproducibility ===
Repository smol-army (this book's case library): preregistration precedes results entering the repo
(docs/prereg.md); changes are append-only (docs/CHANGES.md); a per-call ledger
(results/ledger.jsonl, append-only); per-problem results (results/runs.jsonl, 3,580 lines); the
summary (results/report.md); the audit script (scripts/audit_math.py, the post-hoc audit entry in CHANGES.md). Every number here points to those files and can be recomputed.
```

## Deliverable two, the CTO one-page memo (real numbers)

```text
To: CTO
From: [author]
Date: 2026-07-26
Subject: replacing the frontier API with open-source small models (a decision recommendation from one $5.58 controlled evaluation)

Conclusion (one sentence)
On code generation, the accuracy gap between a voting combination of open-source small models
(total parameters ≤21B) and GPT-5.6-terra cannot be told apart within measurement precision (93.7%
against 96.0%, confidence interval crossing zero), while the unit cost is one fifth of the latter's ($0.00053 against $0.00269 per query).

Risks (three lines, read them before the table)
1  The table below is a public benchmark, not our workload. The code conclusion has not been validated on real traffic.
2  The evaluation shows the gain from "multi-model teaming" cannot be distinguished from "multi-sampling one model" (on code the latter
   scores 94.7% at $0.00041, and is cheaper still). The recommended deployment shape is therefore multi-sampling on one model, not
   multi-model orchestration; discount any proposal sold on "army" or "teaming" accordingly.
3  Cost is counted at API list price; the amortization account for self-hosted GPUs was not measured. Self-hosting needs its own evaluation.

Numbers (all recomputable in the repo)
| Task type | Small models vs frontier | Cost ratio | Judgment |
|---|---|---|---|
| Code generation (HumanEval+ 100) | 93.7% vs 96.0%, CI crossing zero | 1/5 | Has a shot, take it to pilot |
| Knowledge QA (MMLU-Pro 150) | trails by 14.9pp [−21.3, −8.7] | ~45% | No shot, stay on frontier |
| Math word problems (GSM-Symbolic 150) | preregistered +18pp; −2.3pp after the audit found a problem-set defect, direction reversed | ≈1:1 | Evidence void, do not cite |

Recommended next step
Run a two-week shadow-traffic pilot on code workloads, taking the cheapest configuration in the
evaluation that ties with frontier: gpt-oss-20b, 5-sample majority vote ($0.00041 per query).
Knowledge QA stays as is. For math, wait for the next round after the problem set is reissued, and do not use this round as a basis.

Basis
The smol-army repository: preregistration (docs/prereg.md, before results entered the repo), an append-only ledger, the audit script (scripts/audit_math.py).
Every number on this page can be recomputed; the whole evaluation cost $5.58, and the $35 budget hard cap was never touched.
```

**How the two pieces interlock**. Every number line in the memo (93.7/96.0, $0.00053/$0.00269, −14.9pp, +18→−2.3, $5.58, $0.00041) shares a source with sections 3.1/3.2/3.3 of the skeleton, both pointing at results/report.md and the audit script. Different detail, same body of fact.

---

# Part Two · Fillable Templates

## Template 1 · Claims List (single source of truth)

**How to use.** Step 1 of delivery, before any document. Write every claim in **the strongest form you dare sign**. So weak that signing costs nothing is cowardice, so strong that it crosses the line is drift. Every sentence in both vehicles is generated from this table. The wording can change, and no downstream document may edit this table backward. "Not done" is a line too (a basis promised but not executed, an arm that got cut).

```text
# Claims list: ____________ (project)  Date: ________  Signed: ________
Master source of evidence (repo / results file / commit): ____________

| # | Claim (one sentence, the strongest form you dare sign) | Evidence pointer (file/table/commit) | Tier (verified / still exploring / falsified) | Signature (dare / do not dare) |
|---|---|---|---|---|
| 1 | ______________________ | ____________ | ________ | ____ |
| 2 | ______________________ | ____________ | ________ | ____ |
| 3 | ______________________ | ____________ | ________ | ____ |
| Outstanding | Promised but not executed: ________ | Where promised: ____ | Outstanding | I dare sign "not done" |
```

**Self-check**:

- [ ] Is there a claim with no pointer? A claim without a pointer does not enter the list. Go back and get the evidence, or downgrade it to "still exploring."
- [ ] Are a preregistered number and a post-hoc breakdown crammed into one row? Split them into two, and the post-hoc entry carries its own post-hoc label (the discipline of Template 2 in Chapter 8 takes effect upstream here).
- [ ] Is the "outstanding" row empty? Check every basis and every arm you signed off in the plan file. Only a fully delivered plan is allowed an empty row.
- [ ] Is every claim written in its weakest form? You are wasting evidence bought with real money. Push each one up a tier, until one more notch would stop you from signing.

## Template 2 · Technical-Report Skeleton (shaped like a workshop paper, fillable)

**How to use.** Audience = peers and the technical committee, and their question is "how do you know." Generate it from Template 1. Give method and statistics in full, and write limitations for real (each item carrying numbers, no camouflage wording). Skeleton first. Get the five parts standing on their own, then expand into prose.

```text
Title: put the main conclusion in the title (with its qualifier, such as "task-dependent"): ____________

Abstract (six sentences):
① One sentence on the problem and the dispute: ____________
② One sentence on method and preregistration (criteria before results): ____________
③ One sentence on the main result (preregistered numbers as is): ____________
④ One sentence on any overturn or breakdown (if any, labeled post-hoc): ____________
⑤ One sentence on the mechanism control (what the control arm said): ____________
⑥ One sentence on openness (repo/preregistration/ledger public): ____________

1 Problem and related work: 2-3 papers from each camp + where this paper's contribution stands (narrowed to what you dare sign)
2 Method: hypothesis and criteria (with falsification conditions) / tasks and data / arm design / cost basis / statistics
3 Results: main table → preregistered reading → post-hoc breakdown (its own subsection, labeled post-hoc) → criteria reconciliation
4 Limitations (written for real, each item carrying numbers):
   - Data composition problems: ____________
   - Stating the identity of the post-hoc analyses: ____________
   - Weaknesses in reading and statistics: ____________
   - Bases promised and not delivered (outstanding): ____________
   - External validity boundaries (model/point in time/contamination): ____________
5 Reproducibility: repo / preregistration commit / ledger / audit script
```

**Self-check**:

- [ ] Does the title dare say more than the abstract? The title is the sentence quoted alone most often, so run the strictest signature test on it.
- [ ] Is a weakness admitted in limitations still used as a selling point in the abstract or the conclusion? Downgrade consistently across the whole document. Limitations is not a disclaimer.
- [ ] Did post-hoc numbers mix into the preregistered subsection? Separate sections, label them, report side by side, replace nothing.
- [ ] Did the "outstanding" entry disappear? Template 1's outstanding row must have a matching entry in limitations.

## Template 3 · One-Page Memo (fillable)

**How to use.** Audience = decision makers, and their question is "what should I do." Three hard constraints. One page, conclusion on top, risks right behind the conclusion (not at the foot of the page, nobody reads the foot). Every number shares its source with Template 2.

```text
To: ________  From: ________  Date: ________
Subject: ____________ (state the decision question, not the project name)

Conclusion (one sentence, verbatim from the strongest signed claim in Template 1):
____________________________________________

Risks (three lines, each one caveat that could change the decision):
1 Extrapolation boundary: ____________ (what was measured, what was not)
2 Mechanism caveat: ____________ (what the control arm or the audit said that hurts)
3 Basis caveat: ____________ (known gaps in the cost or data basis)

Numbers (a table of ≤5 rows, every cell recomputable):
| Scenario | Reading | Cost | Judgment |
|---|---|---|---|
| ____ | ____ | ____ | Has a shot, take it to pilot / No shot / Evidence void |

Recommended next step (one, executable, with configuration and budget):
____________________________________________

Basis (one line): repo ________, preregistration ________, total cost ________
```

**Self-check**:

- [ ] Does the one-sentence conclusion contain "may" or "to some extent"? Either rewrite it down to a strength you dare sign, or admit the evidence is not enough and do not deliver.
- [ ] Are the risk lines generic boilerplate ("limited sample size")? Every line must be specific enough to change a decision. A risk line that cannot change a decision is decoration.
- [ ] Is the judgment column all "has a shot"? Go back to Template 1 and check. Did the unfavorable conclusions get delivered too? "No shot" and "evidence void" are the two most money-saving words in a memo.
- [ ] Have the numbers been checked against the technical-report skeleton? Run the prompt set's interlock check before you send it.

## Prompt set, audience rewriting + the number interlock check

**Audience rewriting prompt** (drafting and rewriting handed to AI, strength locked):

```text
Below is my claims list (each row carries the claim, the evidence pointer, the honesty tier, and the signature status):
[paste Template 1]

Rewrite it as [technical-report skeleton / one-page memo] for an audience of [technical committee / peer review / CTO / ____],
whose core question is ["how do you know" / "what should I do"].

Hard constraints:
1 Do not change the strength of any claim. "Undecided" may not become "matched," "looks like" may not become "shows,"
  and post-hoc labels may not be dropped;
2 Do not merge two claims into one stronger sentence;
3 Keep the evidence pointer after every number (turn them into citations or footnotes in the final draft);
4 Not one claim outside the list may appear.
```

**Number interlock check prompt** (independent channel, mechanical work):

```text
Here are two documents and one results file: [technical-report skeleton] [memo] [results file/table].
Do factual checking only, and do not evaluate the conclusions:
1 Extract every number appearing in the two documents (body text, tables, titles included) into a list of
  the number, where it appears, and what it claims to mean in context;
2 For each number, look for its counterpart in the results file and mark it: matches / does not match (list both values) /
  not found in the results file;
3 Cross-compare the numbers for the same fact between the two documents and list every disagreement;
4 List every comparative or superlative in the documents with no number behind it ("faster," "strongest," "substantially").
Forbidden: judging whether a disagreement matters. That is not your job.
```

**Self-check (prompt set)**:

- [ ] Did the rewriting prompt omit the tier and the signature status? With no strength information, AI invents strength of its own, and always upward.
- [ ] Did the interlock check run in the same session that wrote the draft? Switch to an independent channel. The same session protects its own draft.
- [ ] Did you fill in a number by hand where the check report said "source not found"? No number may be typed by hand. Go back to the results file and compute it, or delete the sentence.
- [ ] Did you skip rerunning the check after a round of polishing? After any operation that touches the text, the check is void. Rerun it.

---

## Post-red-team revision record (after Chapter 10 opened court)

The two finished pieces in Part One are the versions as of Chapter 9, and keeping them unchanged is deliberate. The Chapter 10 red team put them on trial (four attack surfaces × independent sessions), and all ten charges held. The revisions:

1. All "equal-budget self-consistency" statements withdrawn. The preregistered ±10% cost-alignment clause was never executed (k stayed at 5), SC actually paid only 0.21-0.77 times the army, and the honest restatement is "SC spent less money and still tied or did better";
2. The mmlu_pro conclusion narrowed to knowledge recall in three subjects, business/law/psychology (the sample was drawn in blocks, with zero STEM coverage);
3. The "army vote" mechanism on code degenerated into a single sample from a single model (exact string tallying, ties resolved to the first sample). 93.7% is really qwen's single-shot score, and the conclusion is restated accordingly;
4. The −2.3pp on clean math withdrawn (scoring residue killed the small models in one direction only, and under lenient parsing all three arms saturate). The math family retired in both directions;
5. All cost numbers relabeled "list-price basis" (not what the bill charged, the army actually paid about 19% more), with a procurement sensitivity caveat added;
6. The memo's "recommended next step" of "gpt-oss-20b, 5-sample majority vote" is revised in step with item 3 above. Exact string tallying degenerates to a single sample on code (4 of the 5 calls wasted), so the recommendation is restated as "start with single shot (cheaper), or fix the tallying mechanism and re-evaluate k=5."

The full disposition is in the smol-army repo at docs/redteam-2026-07-25.md. By Chapter 9's discipline, a revision is not an erasure. Both versions stand, and the difference is the lesson.
