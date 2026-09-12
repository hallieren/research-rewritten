# Result interrogation record

**How to use.** The trigger is wanting to announce, not feeling something is wrong. Write the announcement sentence first, verbatim, and paste it at the top of every reply. Fill the record before any number leaves the desk. The mechanical work (pulling wrong samples, clustering templates, per-slice differences) goes to a separate channel through briefs/interrogation-dispatch.md; the model never answers "is this credible". Everything the interrogation produces is post-hoc and goes to the post-hoc column of templates/side-by-side-report.md; the preregistered numbers are never revised (rule).

```text
STATUS: DRAFT, not for the decision chain
# Result interrogation record
Project: ____________   Interrogator: ____________   Date: ____________
Source of the result (repo / file / commit): ____________

## 0 Announcement sentence (the autopsy subject, not a word changed)
____________________________________________
Against my prior odds this result is: as expected / better / worse      My stake (does it benefit me if it holds): ____________
Rule: "better" or "benefits me" makes every item below mandatory, no sampling.

## 1 Scorer: can it be trusted
Raw text of the wrongly scored samples pulled (all, or a random sample, no picking): ______
Pattern in the wrong answers (numerical relation / fixed format / one class): ____________
Messy wrongness (capability boundary) or tidy wrongness (sick scorer or gold): ______ (my ruling, after reading the originals)
Gold answers spot-checked; is "correct" ambiguous: ______      One sample walked through parse → match → score: ______

## 2 Data: what it looks like
Raw problem text seen with my own eyes (originals, not a summary): ______
Molds the samples come from (templates / sources / batches): ____________
Effective sample size, written into the body as "n=<rows>, <k> independent units": ____________
CI or test assumes independent samples; does that hold: ______      Sampling method (first N / random / stratified) introduces structure: ______

## 3 Concentration: where the win sits
Effect spread by problem or slice, ordered by id: ______      Even or concentrated in a handful: ____________
If concentrated: that handful interrogated on its own (back to 1 and 2): ______
Control arm on the same handful (same-direction anomaly = shared-path signal): ______
With the handful removed, effect left and direction: ____________

## 4 Ruling (a human signs; the model may not sign on their behalf)
Two readings of any finding are both reported; neither is forced.
ruling: alive as is / alive after narrowing (new wording: ______) / dead | signed by: UNSIGNED
answers when wrong: NOBODY | <person's name>
verification channel: SAME-CHANNEL (void) | separate session, <model or person>, brief: briefs/<file>, leak_check: clean
criteria timestamp: before results | after results | none
Post-hoc breakdowns entered side by side in templates/side-by-side-report.md: ______   Record archived at: ____________
Signature: ____________ (must be a human)
```

Machine check: `python scripts/effective_n.py count <results file> --cluster <template or batch column>` gives the `N:` line to paste into section 2; `python scripts/effective_n.py compare <results file> --score <col> --item <col> --arm <col> --a <A> --b <B> --cluster <col>` gives the `NAIVE:` and `CLUSTERED:` lines, and the `INDEPENDENCE:` line when the interval must be reported clustered.

### Self-check
- [ ] Only the undesirable results interrogated? Surprise and stakes trigger in both directions. Run the favourable one through the same record.
- [ ] Asked the model "is this result credible"? That seats sycophancy as judge. Re-dispatch for factual organization only and rule yourself.
- [ ] "Spot-checked a few and found nothing"? Sampling is random or complete. Pull all or a random sample.
- [ ] Effective sample size equals the row count? Rows from one template or batch are not independent units. Count molds and write "n=<rows>, <k> independent units".
- [ ] Interrogation changed the conclusion and only the new numbers reported? Preregistered numbers stay as is, post-hoc beside them. Open the side-by-side report.

Filled in → goes to: templates/side-by-side-report.md
