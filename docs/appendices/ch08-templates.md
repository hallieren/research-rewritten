# Chapter 8 templates · Result Interrogation Checklist + Preregistered/Post-hoc Side-by-Side Report Template + Surprise-Result Red Flags

> This appendix is the complete fillable version of the three tools in Chapter 8.
> The order of use is fixed. The moment a result arrives, scan Template 3 first (the red flags, two minutes). If any flag is hit, or you notice you want to announce, run Template 1 (the interrogation checklist). Whatever the interrogation finds, deliver the numbers with Template 2 (the side-by-side report), no exceptions.

---

## Template 1 · Result Interrogation Checklist (fillable)

**How to use.** The trigger is "wanting to announce," not "feeling something is wrong." You do not need to doubt it to interrogate, you only need to notice that you are excited. Fill it in before any number leaves your desk. The interrogation itself is post-hoc analysis. Everything it produces goes into the "post-hoc" column of Template 2, and the preregistered numbers may not be revised.

```text
# Result interrogation record
Project: ____________   Interrogator: ____________   Date: ____________
Source of the result (repo / file / commit): ____________

## 0 Announcement sentence (write it first, as the autopsy subject)
The sentence I originally wanted to say out loud (not a word changed):
____________________________________________
Compared with my prior expectation/odds, this result is: as expected / better / worse (circle one)
My stake in it (does it benefit me if it holds): ____________________
-> If either "better than expected" or "benefits me" holds: every item on this checklist is mandatory, no sampling.

## 1 Question one: can the scorer be trusted
- Did you pull out the original text of the samples scored wrong (all, or a random sample, no picking): ______
- Do the wrong answers have a pattern (numerical relation / fixed format / concentrated in one class): __________
- Messy wrongness (like a capability boundary) or tidy wrongness (like a sick scorer/gold answer): ______
- Did you spot-check the gold answers themselves, is their definition of "correct" ambiguous: ______
- Did you walk one sample through every link of the scoring chain (parse -> match -> score): ______

## 2 Question two: what does the data look like
- Have you seen the raw problem text/samples with your own eyes (not a statistical summary, the originals): ______
- How many "molds" do the samples come from (templates / sources / batches): ____________
- Estimated effective sample size (number of independent units, not rows): ____________
- Does the CI / significance test assume independent samples? Does that assumption hold: ______
- Could the sampling method (first N rows / random / stratified) introduce structure: ______

## 3 Question three: where is the win concentrated
- Did you spread the effect out by problem/slice (per-problem difference, ordered by id): ______
- Is the effect spread evenly or concentrated in a small handful: ____________
- If concentrated: did that handful get its own interrogation (back to questions 1 and 2): ______
- The control arm's performance on the same handful (an anomaly in the same direction = a data problem signal): ______
- With that handful removed, how much effect is left, and did the direction change: ____________

## 4 Ruling (signed by a human, AI may not sign on their behalf)
Fate of the announcement sentence: alive as is / alive after narrowing (new wording: ______) / dead
Post-hoc breakdowns entered in the report side by side per Template 2: ______
Interrogation record archived (location): ____________
```

**Interrogation dispatch prompt** (the independent channel for handing the mechanical work to AI; no expectations of yours in the brief, and no "help me confirm"):

```text
These are the raw per-problem results of an experiment (data/file path attached).
Do factual organization only, and make no evaluation of "whether the result is credible":

1 List every sample scored wrong for [arm X]: sample id, the model's raw answer, the gold answer,
  and the numerical/literal relation between the two, ordered by id;
2 Summarize patterns in the wrong samples: numerical relation (such as always k times), format features,
  id distribution (whether concentrated in a continuous stretch);
3 Cluster the problem text of all samples by template: after removing proper nouns and numbers, how many
  literal templates remain, and how many problems in each;
4 Output a per-problem table of [arm A − arm B] differences, and mark the stretches of samples where the difference concentrates.

Forbidden: any ruling that "the overall conclusion is reliable/unreliable"; that is not your job.
```

**Self-check**:

- [ ] Did you interrogate only the undesirable results? The interrogation trigger is surprise and stakes, in either direction. Favorable results must go through the same checklist.
- [ ] Did you ask AI "is this result credible"? That hands the judge's seat to sycophancy. Dispatch again, factual organization only, and make the ruling yourself.
- [ ] Are the wrong examples "I spot-checked a few and found nothing"? Sampling is either random or complete. "Picking a few to look at" avoids exactly the ones that hurt most.
- [ ] Is the effective sample size field just the row count? Samples from the same template/source/batch are not independent units. The 150 problems of Chapter 8 held only ~3 template families.
- [ ] Did the interrogation change the conclusion, and then you reported only the post-interrogation numbers? Go read the first rule of Template 2.

---

## Template 2 · Preregistered/Post-hoc Side-by-Side Report Template (fillable)

**How to use.** For any test with a preregistration (or criteria locked in beforehand, Chapter 6 style), deliver the numbers with this table. There are only three rules, all hard. ① The preregistered numbers are **reported as is**, however much you dislike them after the interrogation; ② post-hoc breakdowns are **reported side by side**, each labeled "post-hoc" with the reason for the breakdown stated; ③ **under no circumstances may a post-hoc number replace a preregistered one**. A post-hoc number that wants promotion gets preregistered and retested in the next round.

```text
# Result report: ____________ (project / experiment name)
Preregistration file and timestamp: ____________   Results file and commit: ____________
Audit script (if any, with commit): ____________

| Basis | Preregistered result (as is) | Post-hoc breakdown (labeled post-hoc) | Reason for breakdown |
|---|---|---|---|
| ____ | ____________ | ____________ | ________ |
| ____ | ____________ | ____________ | ________ |

## Criteria reconciliation (walk the preregistered win/lose/undecided conditions one by one)
- Falsification condition 1: ____________ -> triggered / not triggered
- Falsification condition 2: ____________ -> triggered / not triggered
- Status of hypothesis H (pick one + one qualifying clause):
  falsified / not falsified but not holding across the board (qualifier: ____________) / holds

## Known statistical weaknesses (list them honestly)
- Effective sample size issue: ____________
- Status of the CI's independence assumption: ____________

## Change log pointer
All post-hoc analyses this report involves are registered at: ____________ (date + entry)
```

**Filled example** (the spine case's math family, excerpted from Chapter 8):

| Basis | Preregistered result (as is) | Post-hoc breakdown (labeled post-hoc) | Reason for breakdown |
|---|---|---|---|
| math army vote vs frontier | +18.2pp [+12.7, +24.2], army_ahead | After removing the ambiguous template −2.3pp [−4.0, −0.7], direction reversed | All 49 frontier wrong answers = 4×gold with %, a single ambiguous template (two readings, absolute percentage points vs relative multiple) |

**Self-check**:

- [ ] Does the table have numbers only in the post-hoc column, with "see above" in the preregistered column? Not allowed. Both columns in the same table in the same position, so the reader compares across in one glance.
- [ ] Does the post-hoc column lack a reason for the breakdown? A breakdown without a reason is indistinguishable from picking data.
- [ ] Was "not falsified" written as "holds"? A falsification condition not triggered ≠ the hypothesis holds. Chapter 8's H is the standard example, not falsified, not holding across the board, landing narrowed to "which tasks have a shot."
- [ ] Did the sensitivity basis / the undesirable set of accounts stay out of the table? The commitment signed in Chapter 6. If the two bases reach opposite conclusions, report it honestly, no picking.
- [ ] Did the audit/breakdown stay out of the change log? Post-hoc analysis is allowed. Post-hoc analysis without a record is not.

---

## Template 3 · Surprise-Result Red Flags

**How to use.** Scan it the moment a result arrives, two minutes. Each flag on its own has an innocent explanation. A flag does not mean "the result is wrong." It means "check here first." Hit any one, go into Template 1, and the matching "first move" is where the interrogation starts. Hit three or more, treat the announcement sentence as a condemned prisoner first.

| # | Red flag | What it usually means | First move |
|---|---|---|---|
| 1 | The effect beats the odds you set beforehand yourself | Either you are about to get rich, or the scorer/data is sick, and the latter is far cheaper | Into Template 1, every item, no sampling |
| 2 | The control arm shows an anomaly in the same direction (the control also "won" where it should not) | The effect does not come from your treatment, it comes from shared data or a shared scoring chain | Check the links both arms share: problem set, parser, gold |
| 3 | The strong player dies on an easy task (a frontier-grade model gets grade-school problems wrong) | "'select' Isn't Broken": suspect the gold answer first, the world second | Pull the original text of the wrong answers, look for a numerical/format pattern |
| 4 | The wrong answers are highly regular (always k times, always off by a constant, always with a certain suffix) | Not a capability boundary, it is question ambiguity or a scorer parsing defect | Read the problem text word by word, look for two defensible readings |
| 5 | Wrong answers concentrate in a continuous id stretch / a single source batch | A data structure problem: same-template variants, sampling not shuffled | Cluster the problem text by template, re-estimate the effective sample size |
| 6 | The CI is abnormally narrow (relative to sample size and task noise) | Samples are correlated, the independence assumption is bankrupt, the CI is falsely confident | Count independent units; run a clustered robustness check by template/batch |
| 7 | Every metric improves at once, without exception | Real improvement rarely blooms everywhere; a shared-source error does | Find a pair of metrics that ought to trade off, and see whether it also "wins both" |
| 8 | Remove a small handful of samples and the effect vanishes or flips sign | The conclusion hangs on that handful | That handful gets its own interrogation (Template 1, questions 1 and 2) |
| 9 | The result confirms exactly the prediction you have already said in public | The desirability flag: the drive to check is at its lowest right now, prime ground for motivated collusion | Symmetry discipline, run the full set as for red flag 1 |
| 10 | You are already thinking about how to word the announcement | The trigger itself | Stop, write down the announcement sentence first, then into Template 1 |

**Self-check**:

- [ ] While scanning, did you find an "innocent explanation" for a flag and skip it? The innocent explanation goes into the record after the interrogation. It may not serve as an inspection waiver before it.
- [ ] Zero hits on the whole table and a mediocre result? Low risk, an L0 spot check (Chapter 12) is enough. Do not run the interrogation checklist as a ritual.
- [ ] Zero hits on the whole table but a major result? The stakes themselves are a variant of flag 9. Into Template 1.
- [ ] Nobody has hit red flag 9 in a long time? Most likely it is not that you have no desirable results. It is that you have not looked at yourself.
