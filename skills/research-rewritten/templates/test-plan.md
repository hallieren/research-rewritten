# Test plan

**How to use.** Fill it in and stamp a timestamp before anything runs; after sign-off, only appended change-log entries, no edits (rule). A blank you cannot fill is where you have not thought it through; start the run with blanks and they fill themselves in along your preference once results exist. Copy the hypothesis from templates/question-sharpening-card.md as is. Run every line of templates/confounder-checklist.md at item 6 and one round of briefs/plan-red-team.md before signing. Colleague test: someone reading only this plan can say what result makes you admit you lost.

> The order of use is fixed. templates/test-plan.md → templates/confounder-checklist.md → templates/harness-checklist.md → templates/surprise-result-red-flags.md → templates/result-interrogation-record.md → templates/side-by-side-report.md.

```text
STATUS: DRAFT, not for the decision chain
# Test plan
Project: ____________   Drafted by: ____________   Draft date: ____________
Sign-off date: ____________   Timestamp method (git commit / email / preregistration platform): ____________

## 1 Question
The question this test has to answer (one sentence): ____________

## 2 Hypothesis H (copied as is from the question-sharpening card)
Falsifiable statement: ____________
Scope (tasks / populations / conditions it covers): ____________
Falsification condition (what observation kills H): ____________

## 3 Arm design
Main arm: ____________
Baseline arm (control): ____________
  Tuning / optimization budget the baseline gets: ______ (rule: equal to the main arm; if not, write the reason)
Steelman arm:
  The strongest opponent's sentence ("your result is really just ____"): ____________
  The arm built to block that sentence: ____________
Other arms (one line each, naming the alternative explanation it rules out): ____________

## 4 Basis
Primary basis (how it is computed, down to the formula): ____________
Reason it is primary (usually the unit the final reader thinks in): ____________
Sensitivity basis (listed separately, never mixed with the primary): ____________
Commitment (rule, effective on sign-off): if the two bases reach opposite conclusions, both are reported, no picking.

## 5 Criteria and falsification condition
Win (the number that triggers it): ________   Lose: ________   Undecided (wording when neither is met): ________
Statistical test: ______   Level or interval: ______   Sample size or repeats per configuration: ______   Seed: ______
Stopping rule (set first; guards against "run until significant"): ____________
Falsification rehearsal record (invented numbers, and the criteria ruled against me): ____________
Banned in any criterion (rule): "as appropriate", "a reasonable range", "at discretion".

## 6 Contamination and confounder check
Every line of templates/confounder-checklist.md run. Lines that do not clear:
  Line: ______   Disposition (mitigation / written into limitations): ____________

## 7 Filing and change log
Timestamp: ____________
Change log (append only): Date: ______  What changed: ______  Reason: ______  After results seen: yes / no (yes → related conclusions are exploratory)
Plan red-team round (briefs/plan-red-team.md), each line adopted or rejected with a reason: ____________

criteria timestamp: before results | after results | none
answers when wrong: NOBODY | <person's name>
Signature: ____________ (must be a human)
```

Machine check: `python scripts/prereg_check.py sections <this file>` (required keys present, no backdoor wording) and `python scripts/prereg_check.py timing <this file> --results <first results file>` (locked before the first result).

### Self-check
- [ ] Falsification condition empty, or "judged as a whole once results are in"? That is decoration. Go back to the card and grind it.
- [ ] No steelman arm? The control proves only "better than nothing". Give the opponent's sentence an arm.
- [ ] Stopping rule blank? "Run until significant" is the best hidden degree of freedom. Set n or a hard cap now.
- [ ] Falsification rehearsal skipped? Criteria that never went red do not count when green. Invent numbers and watch it fail.
- [ ] No timestamp? A plan that cannot prove it was locked first is exploratory. Commit it before the first result.

Filled in → goes to: templates/confounder-checklist.md
