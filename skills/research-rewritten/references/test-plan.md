**Load this reference when:** you are designing any test, eval, benchmark, or A/B, the user says "just run it" or "quick benchmark", or criteria are being written or edited.
Source: chapter 6 (docs/chapters/ch06.md, docs/appendices/ch06-templates.md).

## Contents

- Rules
- Procedure: write the plan
- The seven items
- The confounder checklist, groups A to F
- Decision and vocabulary
- Self-check
- Templates and briefs

## Rules

1. The enemy is not fraud. It is degrees of freedom colluding with motive: dozens of decisions defensible either way (slice, metric, tuning budget, outliers, stopping point, which runs count), deferred until the data is seen, then pulled by the result you want. Lock the degrees of freedom before the data and motive finds no fork.
2. Criteria before numbers (rule). The plan, the basis, and above all what counts as losing go into a file with a timestamp earlier than the first result. Criteria written after the run grow into the shape of the result and endorse it; they are worth nothing.
3. A criterion that has never gone red does not count when it is green. Run the falsification rehearsal: invent numbers and watch the criteria rule against the human who wrote them.
4. The control arm grows on the right enemy. A control against "doing nothing" or a straw man proves the design beats inaction. The steelman arm pins the strongest opponent's sentence.
5. One primary basis down to the formula; the sensitivity basis listed separately; the commitment written in: opposite conclusions get reported, no picking. Reporting only the flattering basis is picking data afterward in the clothes of sensitivity analysis.
6. Banned words in a criterion: "as appropriate", "a reasonable range", "at discretion", "judged as a whole once the results are in". Each is a backdoor. Turn it into a number.
7. After sign-off the plan is never edited. Changes are appended to the change log with date, what changed, why, and "after results seen: yes/no". Yes downgrades every related conclusion to exploratory; confirmatory status needs a rerun.
8. Exploration outside the plan is allowed and often the next hypothesis, as long as it enters labeled "exploratory" and never wears confirmatory clothes.
9. What an AI red team returns is a draft list, not a ruling. The human adopts or rejects each line; rejected lines carry one reason each. An empty red-team report is not evidence the plan is solid: the checklist still runs.
10. Unfair baseline, basis drift, and criteria backdoor are not reliably self-flagged by you. Say so, and run the checklist line by line anyway.
11. When ground truth is not ready-made, half of the design work is designing the ground truth, and the gap between the proxy and the real target is written as a formal limitation.

## Procedure: write the plan

Budget one evening (illustrative). Input: the signed question-sharpening card. Output: a timestamped plan file.

1. Build the seven-item form from `templates/test-plan.md`. Copy the hypothesis as is from the card; do not restate it.
2. Ask the human for the strongest opponent's sentence: "if the result comes out as you want, how would the person who least wants this conclusion call it an artifact?" You check one thing: does the arm design have an arm built to pin that sentence. No arm, no proceeding.
3. Ask for the baseline's tuning budget in the same unit as the main arm. Unequal budgets need a written reason.
4. Rank the bases. Primary basis is the unit the final reader thinks in, computed down to the formula. Sensitivity basis separate. Write the commitment verbatim.
5. The human writes criteria down to "what number triggers it": win, lose, undecided; test; significance level; repeats per configuration; seed; stopping rule. You then invent a concrete set of numbers and run the falsification rehearsal. Confirm the criteria really trigger "lost". If nothing triggers it, send the criteria back.
6. Run the confounder checklist below. The human ticks each line; you record the lines they cannot clear into the mitigation or the limitations. An all-green checklist is itself suspect.
7. Dispatch the plan red team through a separate session with `briefs/plan-red-team.md`. Paste only the plan, never the human's expectations. Each returned line comes back as "the problem, who it favors, how to fix it". The human rules line by line; adopted lines change the plan, rejected lines get a reason on file. Repeat until a new round returns only lines already deliberately rejected.
8. Run `python scripts/prereg_check.py sections <plan>` and fix every `FAIL`. Then the human stamps the timestamp (git commit, a dated email, a version-history document, or a preregistration platform). Remind them to commit.
9. Colleague test: someone reading only the plan can say what result makes the plan's owner admit they lost. If they cannot guess, the criteria are not locked; back to step 5.
10. Any parameter deferred (a specific model version, a list price) is locked just before the run and the locking goes into the change log. Nothing locks quietly.

## The seven items

The plan carries these seven in this order. Missing one leaves a class of accident waiting.

```text
# Test plan (signed before the run; after sign-off, only appended change-log entries, no edits)

1 Question: what this test has to answer. One sentence.
2 Hypothesis H: falsifiable statement with its scope. (The question-sharpening output, copied as is.)
3 Arm design:
   - Main arm (your design):
   - Baseline arm (control): lock in the tuning budget the baseline gets, equal to the main arm.
   - Steelman arm: write down the sentence the strongest opponent would use
     to call your result an artifact, then name the arm built to block it.
4 Basis: one primary basis (how it is computed, down to the formula); sensitivity basis listed separately.
   Locked-in commitment: if the two bases reach opposite conclusions, report it honestly, no picking.
5 Criteria and falsification condition: what counts as a win, as a loss, as undecided,
   written down to "what number triggers it." Statistical test, repeat count,
   random seed, stopping rule, all set beforehand.
6 Contamination and confounder checklist: run every line; for lines you cannot clear,
   write a mitigation, or write it honestly into the limitations.
7 Filing: stamp a timestamp (git commit / an email to yourself or the team /
   a preregistration platform).
```

The stopping rule says how many runs count as done and under what condition the run may stop early. "Run until significant" is the best-hidden degree of freedom.

## The confounder checklist, groups A to F

Run every line while filling item 6. The goal is honest disposition per line: clears / mitigation / written into limitations. You may run the plan against the list first for breadth; the final tick on every line is the human's.

| Group | Line |
|---|---|
| A Baseline fairness | Did the baseline get a tuning/prompt-optimization budget equal to the main arm? |
| A Baseline fairness | Is the baseline's version/configuration the strong form of that method rather than a straw man (default parameters, an outdated version, an obviously suboptimal setting)? |
| A Baseline fairness | If the baseline is a number from someone else's paper, are the runtime environment and the data slice comparable to your main arm? Or should it be rerun? |
| B Budget and basis alignment | Are the resources both sides consume (money / compute / number of calls / person-hours) measured on the same basis? |
| B Budget and basis alignment | Is the definition of "same budget" locked in? (Otherwise budget alignment is itself a degree of freedom to fiddle with afterward) |
| B Budget and basis alignment | Are the primary basis and the sensitivity basis listed separately, with a commitment to report both? |
| C Alternative explanations | Have you listed at least three cheap explanations that "explain the same result without your hypothesis"? |
| C Alternative explanations | Does every cheap explanation point at an arm or a step in the plan built to rule it out? |
| C Alternative explanations | Does the cheapest explanation of all have an arm of its own? (A two-arm design of new system versus strong baseline cannot tell "the structure works" from "spending more works" until a same-budget arm of the plain method is added) |
| D Data contamination | Could the evaluation data have been "seen" by the model during training? (Public benchmarks, public survey data, question banks circulating online, treated as seen by default) |
| D Data contamination | Could it have been "seen" by your own development process? (Looking at the same validation set over and over while tuning = human overfitting) |
| D Data contamination | Is the contamination check a step written into the plan, or one line saying "should be fine"? |
| E Criteria backdoors | Is the metric unique and set beforehand? (Counting several metrics equals picking the metric afterward) |
| E Criteria backdoors | Is the data slice set beforehand? ("Significant on some subset" counts only when that subset was declared in advance) |
| E Criteria backdoors | Is the exclusion rule for outliers set beforehand? |
| E Criteria backdoors | Is the stopping rule set beforehand? |
| F The measurement itself | Could the way scoring and judging works favor one arm? (A task scored by an LLM judge is this line: judge preference contaminates the measurement into a second research question) |
| F The measurement itself | If there is a human judging stage, does the judge know which arm a sample came from? (Blind it wherever you can) |

## Decision and vocabulary

| Situation | Verdict | Consequence |
|---|---|---|
| Criteria file timestamp earlier than the first result | `criteria timestamp: before results` | Conclusions may be confirmatory |
| Criteria edited, or a change-log entry with "after results seen: yes" | `criteria timestamp: after results` | "exploratory" in the same sentence as every related conclusion; rerun to regain confirmatory status |
| No criteria file, or no datable timestamp | `criteria timestamp: none` | Step 3 has not happened; "just run it" routes here first |
| A criterion contains a banned word | backdoor | Rewrite as a number before sign-off |
| The falsification rehearsal cannot trigger "lost" | decoration, not criteria | Send back for rewrite |
| Opposite conclusions on primary and sensitivity basis | report both | Never pick; the commitment was signed |
| An analysis outside the plan | exploratory | Label it; it is a lead, not a conclusion |

Per-family results against the threshold take three values: tie / undecided / lost. The gray band (between the tie line and the loss line) is undecided, reported as is.

Plan red team versus conclusion red team: the plan red team attacks a plan that has not run (degrees of freedom still movable, backdoors, straw-man baseline, the missing arm). Red-teaming conclusions is a later step with its own reference.

## Self-check

- [ ] Is the falsification condition empty or written as "judged as a whole once the results are in"? Send it back; grind the hypothesis again.
- [ ] Is there no steelman arm, or does the control only beat "doing nothing"? Ask for the opponent's sentence and give it an arm.
- [ ] Is the baseline's tuning budget field blank? Fill it or write the reason it is unequal.
- [ ] Is the stopping rule blank? "Run until significant" is waiting; set it.
- [ ] Did you skip the rehearsal because the criteria "obviously" can fail? Invent the numbers and watch it go red.
- [ ] Did you adopt only the red-team lines that were easy to hear, or accept an empty report as a certificate? Rule on every line; run the checklist regardless.
- [ ] Did you edit the plan after sign-off instead of appending to the change log? Revert; append with the after-results flag.
- [ ] Did you paste the human's hopes into the red-team session? Void; re-dispatch with the plan only and a clean leak check.

## Templates and briefs

- `templates/test-plan.md`: the seven-item form with the change log and the machine-check line for `scripts/prereg_check.py`.
- `templates/confounder-checklist.md`: groups A to F as tick boxes with a disposition per line.
- `briefs/plan-red-team.md`: the "overturn it, do not improve it" prompt for a separate session (VERIFICATION).
- `scripts/prereg_check.py`: `sections` for completeness and backdoor words, `timing` for the criteria-before-results check, `changes` for the change-log tags.
