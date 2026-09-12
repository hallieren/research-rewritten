**Load this reference when:** any result has arrived, the user wants to announce it, or an interval or a significance claim is being read.
Source: chapter 8 (docs/chapters/ch08.md, docs/appendices/ch08-templates.md)

## Contents
- Rules
- Procedure
- Decision and vocabulary
- Self-check
- Templates and briefs

## Rules

Interrogate before anyone announces. The brake rule (rule): any result that makes the user want to announce it at once goes through the interrogation before it is announced. Wanting to announce is the trigger. Nobody has to feel that something is wrong first.

Sit as a juror, never as a judge. Pull originals, cluster, recompute, tabulate. The ruling "does this count as evidence" is the human's. This step downgrades on purpose: interpretation is sycophancy's home ground, a question asked with excitement gets answered with excitement, a wrong ruling raises no error, and a retracted announcement is priced in reputation.

Three questions, in this order:

| Question | You do unasked | The human rules |
|---|---|---|
| 1. Can the scorer be trusted? | Pull the original text of the answers scored wrong and scored right (all of them, or a random sample; never a hand-picked few). List the relation between each wrong answer and its gold answer. Walk one sample through every link of the scoring chain: parse, match, score. Spot-check whether the gold answers' definition of "correct" has a second reading. | Messy wrongness or tidy wrongness |
| 2. What does the data look like? | Open the raw item text, not a summary. Cluster items by template after stripping proper nouns and numbers. Count the molds (templates, sources, batches). Name the sampling method (first N rows, random, stratified) and the structure it brings in. | How many independent units there are; whether the interval's independence assumption holds |
| 3. Where is the win concentrated? | Spread the per-item difference between arms by id and by slice. Mark the stretches where it concentrates. Report the control arm's behavior on the same stretch. Recompute with the handful removed and report whether the direction changed. | Whether the concentration matters; whether the handful gets its own interrogation |

Messy versus tidy wrongness. Messy wrongness (scattered, varied, no relation to gold) looks like a capability boundary. Tidy wrongness (always k times gold, always a constant offset, always one suffix, all inside one continuous id stretch) is the fingerprint of a sick scorer or a sick gold answer: the arm was answering a different question with extreme consistency. You lay out the pattern. The human names it messy or tidy after reading the originals.

Illustrative case of tidy wrongness, no numbers. The strongest arm failed a block of easy items. Every one of its wrong answers was the same constant multiple of the gold answer, with a percent sign attached, no exception. The item text had two defensible readings, an absolute difference and a relative increase. Gold took one reading; the arm took the other on every variant, and because the base quantity was identical in every variant the two readings differed by a constant factor. The math was right and the question was ambiguous. The other arm's "win" was a win at guessing the reading, not at reasoning. The harness was innocent; the bug lived in the definition of "right". A bug that zeroes an arm surfaces in an error message sooner or later. A bug that hands an arm points is caught only by the interrogation.

Dispatch the juror with mechanical wording only. Never "is this +N credible": that hands the judge's seat to sycophancy. Say: "List the original text of every wrong answer for [arm X], the matching gold answer, and the numerical or literal relation between the two, ordered by item id." The brief carries no expectation and no "help me confirm". The brief's Forbidden line: any ruling that the overall conclusion is reliable or unreliable. Run it in a separate session and print the trailer: `verification channel: separate session, <model or person>, brief: briefs/interrogation-dispatch.md, leak_check: clean`.

Effective n. Rows are not independent units. Whatever shares a source (one template, one batch of cells, one crawl, one surveyed institution, one respondent measured repeatedly) counts as one unit. When the unit count is below the reported n, write both into the body text, not a footnote, in this format (rule): `n=<rows>, <k> independent units`. Keep the original interval as is and add one sentence: "this interval was computed under the assumption that items are independent, and at this number of independent units that assumption does not hold." Do not quietly swap the interval. Recomputing it is next round's job; this round turns the assumption from implicit into explicit. `scripts/effective_n.py count --cluster <col>` prints the unit count; `compare --cluster <col>` prints the naive and clustered intervals side by side and withholds a verdict when the clusters are too few to decide.

Side by side, three hard rules (rule):
1. Preregistered numbers are reported as is, however much anyone dislikes them after the interrogation.
2. Post-hoc breakdowns are reported beside them, each labeled "post-hoc" with the reason for the breakdown stated. A breakdown without a reason is indistinguishable from picking data.
3. No post-hoc number replaces a preregistered one, under any circumstances. A post-hoc number that wants promotion gets preregistered and retested next round.
Replacing is worse than not interrogating, because it wears the clothes of rigor. The interrogation is itself post-hoc analysis, so every breakdown also gets an entry in the append-only change log.

Symmetry (rule): favourable and unfavourable results run the same checklist. The trigger is surprise and stakes; direction is not in it. A falsified result is interrogated too: is the scorer computable and rerunnable, how many molds, where does the loss concentrate. The more spread out the loss, the sturdier the falsification. A result checked less because it matched expectations goes into limitations as exactly that asymmetry.

Do not force a single reading. When a finding has two readings the design cannot separate (memorized items versus sensitivity to wording; a treatment effect versus a shared scoring path), report both and check whether the conclusion stands under each. Forcing one reading is the defect.

Two things a locked criteria file cannot lock out: an error buried in the gold answers, and correlation built into the data at selection time. The criteria lock motive, not ignorance. The only detector for both is questions 1 and 2, seeing the originals.

The ten surprise red flags. Scan them the moment a result arrives, two minutes (illustrative). One hit opens the interrogation record at the matching first move. Three or more hits (rule): treat the announcement sentence as condemned until the record clears it. Zero hits on a mediocre result: an L0 spot check is enough; do not run the record as a ritual. Zero hits on a major result: the stakes are a variant of flag 9; open the record. An innocent explanation for a flag goes into the record after the interrogation, never as a waiver before it.

| # | Red flag | What it usually means | First move |
|---|---|---|---|
| 1 | The effect beats the odds the user set beforehand | Either riches, or a sick scorer or data, and the second is far cheaper | Every item of the interrogation record, no sampling |
| 2 | The control arm shows an anomaly in the same direction (it also "won" where it should not) | The effect comes from shared data or a shared scoring chain, not from the treatment | Check the links both arms share: item set, parser, gold |
| 3 | The strongest arm fails easy items | Suspect the gold answer first, the world second | Pull the original text of the wrong answers; look for a numerical or format pattern |
| 4 | Wrong answers are highly regular (always k times, always off by a constant, always with one suffix) | Question ambiguity or a scorer parsing defect, not a capability boundary | Read the item text word by word; look for two defensible readings |
| 5 | Wrong answers concentrate in a continuous id stretch or a single source batch | Same-template variants; sampling not shuffled | Cluster the item text by template; re-estimate the effective n |
| 6 | The interval is abnormally narrow for the sample size and task noise | Samples are correlated; the independence assumption is bankrupt; the interval is falsely confident | Count independent units; recompute clustered by template or batch |
| 7 | Every metric improves at once, without exception | A shared-source error blooms everywhere; real improvement rarely does | Find a pair of metrics that ought to trade off; see whether it wins both |
| 8 | Remove a small handful of samples and the effect vanishes or flips sign | The conclusion hangs on that handful | That handful gets its own interrogation (questions 1 and 2) |
| 9 | The result confirms exactly a prediction already said in public | The desirability flag: the drive to check is at its lowest; prime ground for motivated collusion | Symmetry: run the full set, as for flag 1 |
| 10 | The user is already wording the announcement | The trigger itself | Stop; write the announcement sentence down verbatim; open the record |

## Procedure

Budget two hours (illustrative). Output is the interrogation record in `templates/result-interrogation-record.md`.

1. Write the announcement sentence verbatim at the top of the record and paste it at the top of every reply. Under it record: as expected / better / worse against the user's prior odds, and the user's stake. "Better" or "benefits me" makes every item mandatory, no sampling.
2. Scan the ten red flags. Note hits and the matching first moves.
3. Question 1: dispatch `briefs/interrogation-dispatch.md` in a separate session with the raw per-item results as paths. Lay the returned patterns before the human. Do not name them messy or tidy.
4. Question 2: count the molds from the item text. Run `scripts/effective_n.py count`. Write `n=<rows>, <k> independent units` into the body with the one-sentence assumption note. Leave the interval untouched.
5. Question 3: spread the difference by id and by slice. Recompute with the concentrated handful removed. Report the direction, not a verdict.
6. Build the side-by-side table in `templates/side-by-side-report.md`: `preregistered (as is) | post-hoc (labeled) | reason`. Walk every preregistered falsification condition: triggered / not triggered. Register each breakdown in the change log.
7. Emit the ruling line with the fate of the announcement sentence as your draft reading, reasons attached, slot empty.

## Decision and vocabulary

| Where | Values | Reading rule |
|---|---|---|
| Announcement sentence | alive as is / alive after narrowing (new wording) / dead | All three are qualified outputs; the second is the most common. The only unqualified output is a sentence sent out without the interrogation. |
| Hypothesis after the run | falsified / not falsified but not holding across the board (qualifier) / holds | A falsification condition not triggered is not "holds". |
| Per family against the threshold | tie / undecided / lost | An interval crossing zero on a sample too small to squeeze the equivalence band is undecided, never tie. |
| Two readings of one table | preregistered reading (per family, against the threshold) beside the decision-grade reading (direction and price) | Different questions, not a contradiction. Report both; neither replaces the other. |

Sentinel lines on every interrogation record:
```
ruling: alive as is / alive after narrowing / dead | signed by: UNSIGNED
answers when wrong: NOBODY | <person's name>
verification channel: separate session, <model or person>, brief: briefs/interrogation-dispatch.md, leak_check: clean
criteria timestamp: before results | after results | none
```
`after results` or `none` puts "exploratory" into the same sentence as any conclusion. The interrogation runs anyway.

## Self-check

- [ ] Did you ask the model "is this result credible"? You handed the judge's seat to sycophancy. Re-dispatch with factual organization only; the human rules.
- [ ] Did the wrong examples come from "I spot-checked a few"? Sampling is random or complete. Picking a few avoids exactly the ones that hurt.
- [ ] Is the effective-n field the row count? Rows sharing a template, source, or batch are one unit. Count the molds and write both numbers in the body.
- [ ] Did the interrogation change the conclusion and the report then carry only the post-interrogation numbers? Preregistered as is, post-hoc beside it, labeled, with a reason.
- [ ] Did only the unfavourable results get interrogated? Same checklist in both directions; the asymmetry, if any, goes into limitations.
- [ ] Did you fill the ruling slot, or pick one of two readings the design cannot separate? Draft value with reasons, slot empty, both readings reported.

## Templates and briefs

- `templates/surprise-result-red-flags.md`: the ten flags with first moves; scan first.
- `templates/result-interrogation-record.md`: announcement sentence, three questions, ruling signed by a human; machine check `scripts/effective_n.py`.
- `templates/side-by-side-report.md`: preregistered as is, post-hoc labeled, criteria reconciliation, known statistical weaknesses.
- `briefs/interrogation-dispatch.md`: the juror payload for question 1, factual organization only, leak-checked before dispatch.
- `scripts/effective_n.py`: `count` for independent units; `compare --cluster` for naive versus clustered intervals with a closed verdict.
