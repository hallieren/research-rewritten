**Load this reference when:** you are asked to check, accept, or trust any AI-heavy output, the verification budget is short, or a judge or scorer model is in play.
Source: chapter 12 (docs/chapters/ch12.md, docs/appendices/ch12-templates.md)

## Contents

1. Rules
2. Procedure: assign the layer
3. Procedure: L0 spot check
4. Procedure: L1 full verification
5. Procedure: L2 adversarial recompute
6. Procedure: the downgrade ladder
7. Procedure: the verification budget sheet
8. Decision and vocabulary
9. Self-check
10. Templates and briefs

## Rules

Grade by mechanism, never by prose. Break "trustworthy" into three questions that each ask "can you" and none that asks about conscience.

| Property | The question | Fail condition |
|---|---|---|
| Traceable | Can you point to the source of any claim within three minutes (illustrative): which paper, which dataset, which experiment? | A claim whose source you cannot point to is treated as having none |
| Reproducible | Can a different person or a different model take the same raw materials, walk the path again, and reach the same conclusion? Is the path on record? | No path on record |
| Checkable | Was the criterion for right or wrong locked before the output existed? Does the criteria timestamp precede the result? | `criteria timestamp: after results` or `none` |

The independent channel principle (rule). The channel that produces a conclusion cannot be its own judge. Verification runs through an independent channel that shares no context and knows no expectations. Three disciplines follow. All three apply at every layer, and to human reviewers as well:

1. Channel independence. Verify in another session, on another model, or with a person. Whatever it is, it is not the context that generated the output. Context is a position.
2. The brief leaks no expected answer. The task sheet holds only the claim to be checked, not where it came from and not whether you want it to hold or fall. Wording test: "please confirm X" has stuffed the answer into the question; "please rule on the evidence status of X" has not.
3. Three-value output. confirmed / falsified / undecidable and nothing else (rule). "Basically correct" and "broadly credible" are leaked expectations coming back around. Undecidable does not equal pass (rule).

Four forces make a same-session check worthless, and they push the same way at once:

| Force | What it does to the check |
|---|---|
| The model talks along with the asker | Asked with a lean, it answers along the lean |
| The model prefers its own earlier output | Measured self-preference when a model judges between its own text and someone else's |
| The same context yields no new water | The session already holds the retrieval results that propped up the claim in the first place |
| The asker's own motive | You hoped to be confirmed. Motivated collusion has no tool fix, only a channel that does not share the motive |

Lineage question (rule). Two channels in appearance can be one lineage underneath: evaluation code cross-reviewed by agents of the same family, a judge distilled from the model being judged. Ask one sentence: how much lineage does the judge share with the generator, the same model, the same family, distilled from whom? What you cannot state, treat as the same channel.

The judge is an instrument (rule). Any model used for scoring is calibrated before it produces numbers. Let it rule blind on a batch of human-labeled samples. Read its disagreement rate layered by cost of error. On the class where an error costs the most, it may only report up, never release.

Three lessons from code review, six lines:

1. Unfamiliar output is trusted through mechanism, not goodwill. Traceable is "origin on record", reproducible is "check out and rerun", checkable is "tests first".
2. The right question is not "can this output be trusted" but "how dense is my net of mechanisms". Verification infrastructure sets the radius of trust.
3. Mechanical checks go to the machine (citation existence, number and figure consistency, uniform units and basis). People look only where the machine cannot: does this chain of evidence bear weight, was that convenient slice declared beforehand.
4. Where it breaks: a red CI is red, but an "undecidable" has no color and gets waved through as green. Discipline 3 and the escalation rule plug that hole.
5. What fails the mechanism does not merge, and there is no exception channel. "The author thinks it is fine" is not a pass.
6. Where it breaks: code has a permission system that welds generation apart from verification; research has only institutions. See `references/habits-and-dispatch.md`.

"No time to verify" and "no time to finish this" are the same sentence (rule). Priority disguised as constraint ("this one is not important, a spot check will do", while it goes into the decision chain) is solved by delaying delivery, not by the downgrade ladder.

The verifier errs too. "Confirmed" means the evidence found at this moment supports it, not a permanent verdict. Spot checks plus filing are enough. No infinite regress.

Criteria depreciate. A criterion is a snapshot. Rising capability exhausts its discriminating power, and corpus contamination voids "the questions have not been seen". A project that runs once locks the criteria until the run ends. A project that runs for months gives the criteria a review date and folds it into the map cadence in `references/honest-map.md`.

## Procedure: assign the layer

Assign the layer first, then do the work. Two questions; their product is the layer.

1. Where is this output going? own desk / team discussion / the decision chain / the public knowledge base. The farther it goes, the larger the blast radius of an error.
2. Which kind of error is it most likely to hide? Citation-heavy output hides fabricated citations, statistical conclusions hide spurious significance, synthetic answers hide the average face. Take the class from the census in `references/failure-modes.md`.

State it: `acceptance layer: L<n> (destination: <...>; likely error class: <...>)`. The layer follows destination and cost. It never follows how reliable the output looks, and never "it was good quality last time".

| | L0 spot check | L1 full verification | L2 adversarial recompute |
|---|---|---|---|
| Trigger | The output does not leave your desk: brainstorming, exploratory drafts, intermediate material | Someone will spend money, commit people, or draw conclusions on it, and it is about to leave your desk | A single conclusion being wrong triggers a hard-to-reverse action: architecture selection, funding, public release |
| Budget | 15 to 30 minutes (illustrative) | Half a day to a day, mostly machine time (illustrative) | One to several days per named conclusion (illustrative) |
| Actions | Sample citations, sample numbers, one reverse question | Forward-check every citation, trace every number, walk the reasoning chain link by link, file the claim-to-source table | Independent re-derivation, recompute by another method, red team |
| Escalation and close-out | One hard defect found: the whole output moves up to L1 | Undecidable may not quietly turn green | Every unresolved disagreement gets a human ruling |

Every quantity above is a starting default. Calibrate it to your field once, write it into your card, and do not change it on the spot.

## Procedure: L0 spot check

Three items, all dispatched through an independent channel.

1. Random citation sample: 5 citations or 10%, whichever is larger (illustrative). Two questions each: does it exist, does it really say what the output claims? Draw the sample with `python scripts/leak_check.py sample`. Neither the generating side nor the checking channel picks the sample (rule).
2. Three key numbers (illustrative): trace each to its source or to a dead end. A dead end is a hard defect.
3. One reverse question through the independent channel: "which claim in this material has the weakest evidence, and why".

Escalation rule (rule): one hard defect, a fabricated citation or a sourceless number, moves the whole output to L1. One defective unit in the sample means this production line does not deserve sampling. Say so in the report: `escalated: yes`.

Dispatch note: the brief carries the claims only, stripped of rhetoric and concluding tone. Which items get sampled is decided by you or by a random number, never by the channel doing the check.

## Procedure: L1 full verification

Four items. What L1 adds over L0 is "full" and "filed".

1. Extract the claim list and group by type: citation / number / reasoning. Strip the concluding tone before the list leaves your desk.
2. Forward-check every citation with three questions: does it exist, does it say so, was it later overturned or retracted. The third question is the easiest to skip and the last one that should be.
3. Trace every number to its original source and check the basis item by item: comparison baseline, time window, units. "The number is right but the basis was swapped" is falsified.
4. Walk the reasoning chain link by link. Type each link: citation / calculation / "author thinks". List the "author thinks" links separately and hand them to a human ruling.
5. File the claim-to-source table with the output, with check date and channel. This table is the physical form of the traceable property.

Dispatch note: split into mechanical subtasks and batch them, citation checks through one channel, number tracing through another, and neither brief carries the other's conclusions. When collating, the human reads only two columns: every undecidable and every falsified. Nothing turns green quietly. Neither L0 nor L1 requires that you can rerun the output; both run with the report alone in hand.

## Procedure: L2 adversarial recompute

Spend it only on the named load-bearing conclusions, one or two per output (illustrative). Three items per conclusion.

1. Independent re-derivation. Another channel gets only the raw materials and the question, never the conclusion, and derives from scratch. Converges: record as machine evidence. Does not converge: rule on each point of disagreement by hand; each one either fixes the output or goes into the limitations.
2. Recompute key numbers by another method: a different calculation path or a different data source.
3. Red team this conclusion. In L2 the red team is mandatory (rule). Method in `references/red-team.md`.
4. File every ruling.

Dispatch note: the re-derivation brief is the easiest in the whole process to leak. No residue of the original conclusion, its wording, its structure, or its subheadings may appear in it. Reorganize the raw materials; never clip the first half of the output. Run `python scripts/leak_check.py brief briefs/rederive.md --original <the output>` before dispatch. With no raw materials, write `L2: not possible (no raw materials); the four attack surfaces used as the acceptance checklist instead`.

## Procedure: the downgrade ladder

Cut layers whole, never the order (rule). Doing half of every layer (three citations instead of five, one number instead of three, a re-derivation stopped halfway) leaves a gap in every line of defense, and a gap stops as much as an open door. Keep the earliest line in the order and cut the later ones whole, because a criterion patched in afterward contaminates every downstream conclusion, while two fewer citations sampled loses only two citations' worth of information.

| Tier | The only actions | What it produces |
|---|---|---|
| 10-minute | Check the criteria timestamp. Nothing else. "After" or "none" means the conclusion is an untested hypothesis and is treated as one | "Is this something that can be tested at all", not "trust / do not trust" |
| 30-minute | The 10-minute tier, plus L0 items 1 and 3: the citation sample for existence and paraphrase fidelity, and one reverse question through an independent channel. Number tracing is cut whole; a half-done trace is worse than none, because you will remember "I checked the numbers" and forget you checked one | A scout report |
| 2-hour | The full afternoon: assign layers in the first ten minutes (illustrative), send the L0 scout, then list the L1 table and the L2 to-dos. This is not a downgrade | An evidence status, not an impression score |
| no-next-round | The three floors below, all of them | An honestly priced output |

The three floors of the no-next-round tier (rule), for when the interrogation killed the conclusion and there are no resources to rerun:

1. Report the numbers under the original criteria as is. The interrogation's output stands beside them, labeled post-hoc. Killed in the interrogation does not mean deleted. Deleting is the fraud.
2. Write "no next round" into the limitations, specifically. Not "limited by resources". Write: "the X this conclusion depends on has only <k> independent units, a confirmatory retest would need about <n> additional samples, and this project did not run it." A reader can price the conclusion from that. A vague disclaimer gives them nothing.
3. Lower the claim strength to the tier the evidence can carry, not to zero. Erring upward is an unconditional statement written knowing the evidence falls short. Erring downward is being frightened into saying nothing. Both are dereliction.

A downgrade leaves a record (rule). The note travels with the conclusion and gets cited along with the numbers. Pre-write it in the project template; downgrades happen on the busiest day, and on that day you will skip the wording.

```
[VERIFICATION LEVEL NOTE]
This conclusion is delivered at the ______ tier (10-minute / 30-minute / 2-hour / no-next-round).
Checked:
- criteria timestamp: before results | after results | none
- citation spot check: ___ / ___ passed
- number tracing: all | sampled ___ | not done
- independent channel reverse question: done, weakest claim is ___ | not done
Not checked: <the cut steps listed as they are; "the rest omitted" is not allowed>
Reason: <the real constraint: the exact time, budget, or permission ceiling>
```

A downgrade without a record and a pretense of the full set look identical to a downstream reader. A labeled "L0 spot check passed" the reader knows how to use; an unlabeled conclusion the careful reader discounts at the worst case and the careless reader takes at full marks.

## Procedure: the verification budget sheet

Fill one page for the project's outputs of the next month (illustrative), one row per output, and post it where "has this thing passed the layer it should have passed" becomes a question anyone can ask.

1. List the outputs: reviews, analysis reports, charts, code, memos.
2. Two questions per row assign the layer: where is it going, which kind of error is it most likely to hide.
3. Lock the escalation rules (rule): a spot check finds a hard defect, the whole output moves up one layer; the destination escalates (an internal draft gets cited in a decision document), reassign by the new destination; a conclusion gets cited by a bigger decision, that conclusion is named L2 on its own.
4. Name the channel for L1 and above: which model, which prompt path, which colleague. A channel written as "AI" will take the easy road and be the generating side.
5. Set the next review date. Review monthly (illustrative). When a destination changes, the layer changes with it.
6. Pre-write one downgrade note per layer.

Track verdicts in a verification ledger: `python scripts/ledger.py record <ledger> --amount 1 --meta claim=<id> verdict=<value> channel=<name>` with `--unit checks`, so the pass rate is read from the ledger and never estimated.

## Decision and vocabulary

| Slot | Allowed values |
|---|---|
| Verification verdict | confirmed / falsified / undecidable; a "confirmed" with no basis you can open is undecidable; agree / disagree and scores are sent back |
| Layer | L0 / L1 / L2 |
| Downgrade tier | 10-minute / 30-minute / 2-hour / no-next-round |
| Link type in a reasoning chain | citation / calculation / "author thinks" |
| Hard defect | fabricated citation / sourceless number |

Sentinel lines on every check result, verbatim:

```
verification channel: SAME-CHANNEL (void) | separate session, <model or person>, brief: briefs/<file>, leak_check: clean
criteria timestamp: before results | after results | none
ruling (fit for <destination>): <draft value> | signed by: UNSIGNED
```

Two canonical closing sentences. Spot check failed: "Spot check failed. Not recommended as a basis for today's decision. Returned for further verification." Spot check clean: "Citation and number spot checks passed. Full verification out tonight. <N> load-bearing conclusions need independent re-derivation; final ruling by <time>."

## Self-check

- [ ] Did you assign the layer by how reliable the output looks? That is grading by prose. Reassign by destination and error class.
- [ ] Did you pick "the few that look suspicious" on the spot? That is a hunch, not a spot check. Lock the sampling rule first and draw with the script.
- [ ] Did any check run through the channel that generated the output? Void. Re-dispatch with a `briefs/` file as the only payload.
- [ ] Can you state the judge's lineage? If not, it is the same channel.
- [ ] Is the undecidable column empty? Either the output is unusually clean or the channel is fudging. Check two items yourself.
- [ ] Did a failed output pass through "the author explained it and it was let through"? No exception channel. It goes back for rework.
- [ ] Did you trim a little from every layer? Cut layers whole. The criteria timestamp survives every cut.
- [ ] Does the reason column say "this one is not important" while the output enters the decision chain? Prioritization problem. Delay delivery.
- [ ] Is the check record filed? A check with no archive equals a check never done.

## Templates and briefs

- `templates/verification-workflow-card.md`: the layer table, the L0 / L1 / L2 checklists, the acceptance output block, the claim-to-source table.
- `templates/verification-budget-sheet.md`: the one-page sheet with locked escalation rules.
- `templates/downgrade-note.md`: the note above plus the three floors.
- `briefs/verify-citations.md`: claim extraction and the citation check, three questions per citation.
- `briefs/trace-numbers.md`: number tracing with the basis check.
- `briefs/reverse-question.md`: the L0 reverse question.
- `briefs/rederive.md`: the L2 re-derivation brief, raw materials only; run `leak_check.py brief --original` first.
- `scripts/leak_check.py`: `brief` for expectation leaks and residue, `report` for three-value verdicts and sentinel lines, `sample` for the seeded citation draw.
- `scripts/ledger.py`: as the verification ledger, `--unit checks`, one line per verdict.
