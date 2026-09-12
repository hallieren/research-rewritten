**Load this reference when:** a deliverable is final and about to go out, the user asks to attack a conclusion, the acceptance layer is L2, or a manuscript is being reviewed.
Source: chapter 10 (docs/chapters/ch10.md, docs/appendices/ch10-templates.md)

## Contents
- Rules
- Procedure
- Decision and vocabulary
- Self-check
- Templates and briefs

## Rules

Conservation of criticism. A conclusion with weight meets its first serious attack sooner or later. Nobody decides whether. The human decides two things: before release or after, and whether the attacker is hired by them or by their own curiosity and hostility. The red team is the hired option: kill the conclusion at home before someone else does it in a reply with the boss copied in.

Interrogation versus red team:

| | Interrogation | Red team |
|---|---|---|
| Trigger | Excitement; the object is a result someone wants to announce | None; every claim in the deliverable takes a beating, dazzling or dull |
| Timing | During interpretation; it hits numbers | After the deliverable is final and before it goes out; it hits the sentence other people will read, wording included |
| Your role | Juror: lay out facts, pass no judgment | Hired prosecutor: construct charges as hard as you can; hand in a list of charges each with an executable check; not one millimeter of ruling power moves |

The real risk of the prosecutor is hitting too softly. "Take a look and see if anything is wrong" returns three harmless items. Sycophancy turns a death-penalty review into an awards ceremony. Attacks come from enumerating a fixed list of surfaces, not from inspiration: "is there a problem" is a prayer, "here is what each surface turned up" is a process. The production cost of charges collapsed; the cost of ruling on them did not. Triage stays human.

The four attack surfaces (rule). Any empirical conclusion stands on four parts: who judged right from wrong, what it was tested on, how many independent samples there really are, and whether it was worth the price.

| Surface | The prosecutor's questions | Check first |
|---|---|---|
| The scorer and the criteria | Who defined "right"? Is there a second defensible definition? Has every link of the scoring chain been replayed? | A second reading of gold or of the item text; links in parse, match, score that silently swallow or hand out points (suffixes, units, null, timeouts, partial matches); tidy patterns in the wrong answers; whether the conclusion flips under an equally reasonable scorer or annotator |
| Data composition | Where did the items come from and how were they drawn? How many molds? Are they in the training corpus? | Structure brought in by the draw (first N rows, one batch, one source, convenience sample); literal templates left after stripping names and numbers; whether the material predates the corpus cutoff or is a public bank; whether "holds on the X slice" was written as "holds" |
| Independence assumptions | Is n rows or independent units? What does the interval assume? Are the two arms' errors correlated? | Same template, same person, same batch, repeated measurement, and how much each shrinks n; how far the interval moves recomputed by cluster; shared item set, scorer, or time window; whether n was fixed in advance or run until it looked good |
| Cost basis | Who chose the basis and when? Does the conclusion flip on another set of books? Was the control arm's price fair? | Basis chosen before or after results, and whether it favors the design under test; alternative pricing, hidden costs (retries, failures, labor), amortization; equal tier, discount, and point in time on both sides; whether estimated numbers have measured backing or a caveat beside them |

Scorer applies to research with no benchmark too: a human annotation rulebook, an LLM judge's preferences, and the operational definition of "valid" are all scorers. Every claim carrying "cheaper", "better value", or "cost-matched" owes the cost surface a round. The move that seals one surface can open another: a contamination-resistant variant set blocks memorized items and turns the item set into copies of a few templates.

Five dispatch disciplines (rule):
1. An independent session, zero history. The narrative, the excitement, and the wording habits of the last weeks all leak expectations. Switching models is better still. The model that paired on the conclusion may not red-team it.
2. The brief gives only the claims list and the raw materials as paths. Compress the deliverable into 5 to 10 (illustrative) neutral claims, a conclusion and each qualifying condition on separate lines, number claims at recomputable precision. Not one word of which claim should survive. "I am worried", "confirm this for me", and "our contribution" are barred.
3. One surface, one order. Four orders in four fresh sessions. Dispatched merged, the model fills the page with the softest surface and gives the one that hurts two perfunctory lines.
4. A charge carries an executable check. A charge without a check is a comment and is not accepted. The rule forces "the data may have a problem" into "cluster the item texts by template and count how many kinds there are".
5. File the output and rule line by line. Every charge gets its check run or is rejected in writing with one line of reason. The rejection record is ammunition at the defense.

The charge triple (rule). Every charge returns `charge | consequence | executable check`: which point of this surface could make which numbered claim fail; if it holds, which claim dies and what direction and rough magnitude of effect was manufactured; one check runnable the same day (script sketch, sampling plan, replay, recompute on another basis) whose result confirms or rules the charge out. Output ordered by lethality. The Rules block goes into every order verbatim:
```
Rules: attack only, no balanced coverage; do not evaluate whether the conclusion as a whole is credible;
do not list a charge you cannot give an executable check for; if you find nothing, state "nothing found
on this surface", do not pad.
```
A list of dozens of charges is a dilution tactic: ask for them merged and reordered, and a report whose top three do not hurt is dispatched again in full.

Two illustrative charge shapes, no numbers:
- Scorer surface. Charge: the numeric parser scores correct values wrapped in markup residue as zero, and only one arm's model family emits that residue, so the post-hoc reversal on the clean subset is a one-sided scoring artifact. Consequence: the claim "direction reversed on the clean subset" dies; under a lenient extractor every arm saturates and the family is uninformative in both directions. Check: rescore the clean subset with a lenient numeric extractor and rerun the paired bootstrap.
- Independence surface, mechanism. Charge: the vote tallies exact strings and resolves ties to the first sample; extracted code strings almost never collide, so the "vote" arm on the code family is identically the first member's single sample. Consequence: the teaming claim dies; what survives is a single small model's single shot, and most of the calls bought nothing. Check: replay the tally over the stored samples and count how often the returned answer equals the first sample.

Three dispositions (rule). A held charge gets exactly one. There is no fourth. "I am aware of it" is not a disposition, and a hit with no written disposition is worse than no red team, because now the human knows.

| Disposition | Trigger | Action | Unqualified form |
|---|---|---|---|
| Overturn | The charge hits load-bearing structure and no rewording saves it | The announcement sentence comes off the deliverable. The preregistered numbers are still reported as is, post-hoc beside them. What is overturned is the sentence, never a number that happened | Quietly deleting the number and never mentioning that the conclusion existed |
| Narrow | The charge holds, but what it cuts away is the range or the strength, not the conclusion | Rewrite the boundary (task family, sample, confidence, exact model and tier). The new statement is strictly weaker than the old one and still checkable | Narrowing into vaguer words ("may under some circumstances"): escape, not narrowing |
| Caveat | The charge holds or cannot be ruled out, and it is unfixable, untestable, and not fatal | The conclusion stays; the caveat travels at the same address as the conclusion, every place it appears; one check is left for the next round | Buried in an appendix or footnote; hung where an overturn belongs |

Qualification order (rule): fixable, fix it; testable, test it; fatal, overturn or narrow; only when all three fail does the caveat get its turn. A caveat states the boundary of the evidence, so it goes on even when the conclusion feels solid, and even on a FAIL. Far more caveats than overturns plus narrowings means the caveat is being used as a trash can.

The empty-report rule (rule). "No major problems found" means suspect the dispatch first: an expectation leaked, or the material was a summary and the originals never went in. Switch models, dispatch the surface again; it counts as empty only when both rounds come back empty. Then celebrate quietly.

The red team attacks the audit itself. An audit hunts down the first bug and issues a clean bill for the rest. The red team then lands exactly where the bill said clean: the audit's own rescoring (a parser fixed for one suffix let two other residues through), the sampling of a family the audit never opened, the basis of the ledger. A fixed bug class has siblings.

The finest defense you rehearse rests on a fact you never verified. A rehearsed rebuttal claimed the comparison arm's hidden cost was real money and so the charge could not move the conclusion; the prosecutor read the usage field and the hidden cost measured zero. Every defense written in advance gets its own executable check before it is used.

Publish the case file. "I checked it myself" carries about zero information, because everyone who never checked says the same. Transferable trust has one shape: criteria, ledger, scripts, and the disposition record on the table, and "recheck it" brought down to one command. A report carrying bullet holes and dispositions is more credible than one that looks untouched. What cannot all be published still ships with the disposition record attached.

The revision changes what the human intended to say and never a number. After revision, one more quick round: a patch introduces new handles. A hit can send the work back to any earlier step (a scorer hit to the plan and the harness, a data-composition hit to the choice of task family); budget for fix-and-rerun.

Peer review, both sides. Before submitting, dispatch the manuscript under the five disciplines, one round per surface; the charges are a pre-review report; write the response now, and what cannot be written is a narrowing signal. When reviewing, the four surfaces are the checklist, one paragraph per surface. Red line (rule): never send someone's unpublished manuscript under review to an outside AI service. NIH has barred reviewers from using generative AI in grant review since 2023; major publishers bar reviewers from uploading manuscripts. The checklist runs without AI. Confidentiality outranks convenience.

Ceiling. The four surfaces catch diseases of method. They do not catch "this measurement has been notorious in the field for years". Route the conclusion and the disposition record to a human anchor who knows the field.

## Procedure

Budget half a day (illustrative), plus the rerun.

1. Compress the deliverable into 5 to 10 (illustrative) neutral claims in `templates/red-team-dispatch-brief.md`: conclusion and qualifiers on separate lines, numbers at recomputable precision, materials as paths (results, criteria file with timestamp, scoring script, ledger, item text).
2. Run `python scripts/leak_check.py brief briefs/redteam-scorer.md` and the same for the other three orders. Delete every expectation, worry, and adjective it flags. The human deletes again what you missed.
3. Open four fresh sessions, one per surface, shakiest surface first; paste only the brief. Print the trailer per session: `verification channel: separate session, <model or person>, brief: briefs/redteam-<surface>.md, leak_check: clean`.
4. Triage: run the executable check on every returned charge and record the result. You never rule holds or rejected.
5. The human rules each charge and assigns a disposition to each held charge. Record it in `templates/disposition-record.md`, one line of reason per rejected charge.
6. Apply each disposition at every place the conclusion appears, not only the abstract. Rerun a quick round on the revised deliverable.
7. File the disposition record in the same repo as the deliverable and ship them together.

Shape of a disposition record: a protocol header (four sessions, one surface each, briefed with a neutral claims list and file paths only, every charge carrying an executable check, checks run against committed files, key findings replicated by the human before disposition, dispositions from the three-value scheme); the line "the preregistered numbers stand as registered; everything below is post-hoc and labeled"; one entry per sustained charge with id, surface, one-sentence charge, disposition in capitals, the check and its result, what is retracted and how it is restated; a "minor sustained" list; an "attacked and held" list with one reason each; and a closing "what survives, restated with the narrowing applied".

## Decision and vocabulary

| Where | Values |
|---|---|
| Charge verdict | holds / rejected |
| Disposition of a held charge | overturn / narrow / caveat |
| Surface report | charges ordered by lethality, or "nothing found on this surface" |

Per charge: `ruling: holds / rejected; disposition: overturn / narrow / caveat | signed by: UNSIGNED`. Banned anywhere in the record: "I am aware of it", "overall credible", "the design is rigorous, only minor issues". The last one means an expectation leaked; go back to the brief.

## Self-check

- [ ] Did the brief carry "I hope", "confirm", "our contribution", or an adjective on a claim? Leaks. Neutral claims only, then the script again.
- [ ] Did one order cover all four surfaces? Split it; merged orders pad the softest surface.
- [ ] Did the red team run in the session or the model that wrote the conclusion? Context is a position. Fresh session, different model.
- [ ] Did a charge arrive without an executable check? Send it back; no debate.
- [ ] Did you write holds, rejected, or a disposition? Those are rulings. Run the check, record the result, leave the slot.
- [ ] Did every held charge come back caveat? Rerun the qualification order line by line.
- [ ] Did the disposition change the abstract and leave the body paragraph as it was? The disposition lands as many times as the conclusion appears.
- [ ] Did an empty report get celebrated after one round? Switch models, dispatch again.

## Templates and briefs

- `templates/red-team-dispatch-brief.md`: materials as paths, neutral claims list, one work order per surface; machine check `scripts/leak_check.py brief`.
- `templates/disposition-record.md`: tier table without specimens; the record filed with the deliverable.
- `briefs/redteam-scorer.md`, `briefs/redteam-data.md`, `briefs/redteam-independence.md`, `briefs/redteam-cost.md`: the generic skeleton with one surface block each; one file per fresh session.
- `scripts/leak_check.py`: `brief` flags expectation, adjective, and ownership leaks; `report` lints three-value verdicts and sentinel lines on the returned record.
