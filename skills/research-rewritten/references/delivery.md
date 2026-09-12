**Load this reference when:** writing or polishing any memo, report, paper, slide, or summary that carries a claim.
Source: chapter 9 (docs/chapters/ch09.md, docs/appendices/ch09-templates.md)

## Contents
- Rules
- Procedure
- Decision and vocabulary
- Self-check
- Templates and briefs

## Rules

Write the claims list before any prose. No sentence of a deliverable exists until the list is signed. The list is the single source of truth; both vehicles are generated from it, and no downstream document edits it backward.

Four fields per claim, plus one row (rule):

| Field | Content | What fails it |
|---|---|---|
| Claim | One sentence, the strongest form the human dares sign | A preregistered number and a post-hoc breakdown crammed into one row: split them, the post-hoc row carries its label |
| Evidence pointer | File, table, commit | A claim with no pointer does not enter the list; get the evidence or downgrade to still exploring |
| Tier | verified / still exploring / falsified / outstanding | A tier chosen by you |
| Signature | dare / do not dare | A name you typed |
| Outstanding row | Everything the plan promised and this round did not do (a basis never run, an arm that was cut) | An empty row on a plan that was not fully delivered; only a fully delivered plan earns an empty row |

The strongest form the human dares sign. So weak that signing costs nothing is cowardice and wastes evidence bought with real money. So strong that it crosses the line is drift. Push each claim up until one more notch would stop the signature. On the same evidence "tie" has at least four writings, and which one is chosen is the signature itself:
- "Proved a tie"
- "Looks like a tie"
- "Undecided, but no gap shows in direction"
- "A tie under these three premises"
You propose the ladder. You never pick the rung.

Two vehicles, and where the honesty layering lands in each (rule):

| Vehicle | Audience and their question | Fixed structure | Where the tier column lands |
|---|---|---|---|
| Technical report skeleton | Peers, reviewers, the technical committee: "how do you know" | Question; method (criteria with falsification conditions, arms, basis, statistics); results (main table, preregistered reading, post-hoc breakdown in its own labeled subsection, criteria reconciliation); limitations; reproducibility | Limitations, written for real: every item carries numbers, no "certain limitations may exist" |
| One-page memo | Decision makers: "what should I do" | One-sentence conclusion on top, verbatim from the strongest signed claim; three risk lines right behind it, not at the foot; a table of at most five rows (rule) with a judgment column; one executable next step with configuration and budget; one basis line | The three risk lines, each specific enough to change the decision |

The same fact changes shape across the vehicles. A data-composition defect is a paragraph of statistical discussion with numbers in the report and one line in the memo: "evidence void, do not cite". Tune the depth of the layering to the audience. Never tune its honesty.

Strength drifts upward under polishing. The shortest path to fluency is confident wording; qualifiers shed a layer with every rewrite; "under condition X it looks like" becomes "the results show". The model fabricates no number and still parks the summary sentence in the most flattering corner of the legitimate wording space. Illustrative drift, no numbers: a draft abstract built from the preregistered table alone closed with a sentence in which "surpass" came from a row the interrogation had already killed, "match" was stamped on an interval the criteria read as undecided, and a handsome class name was invented on the spot for one measurement artifact. Every word had a source; not one word was signable. So: lock the facts, then let go of the wording, and after every polish rerun the strength reconciliation and the interlock (rule). Polishing is not a free operation. Mark every wording stronger than the list; more than three per round is normal, not an incident.

The rewrite prompt locks strength. Hard constraints in `briefs/audience-rewrite.md`: no claim changes strength ("undecided" never becomes "matched", "looks like" never becomes "shows", post-hoc labels never drop); no two claims merge into one stronger sentence; the evidence pointer stays after every number; nothing outside the list appears. The prompt carries the tier and signature columns; without them the model invents strength, always upward.

No number by hand (rule). Every number in both vehicles is quoted from the results file, then interlocked against the other vehicle. Any disagreement among report, memo, and results file means at least one is lying. Run `scripts/interlock.py <report> <memo> --results <file>` first; it exits non-zero on any MISMATCH or NOT FOUND and lists every superlative with no number behind it. It does not judge importance: the human reads every MISMATCH and NOT FOUND line. Then `briefs/interlock-check.md` in a separate session handles what each number claims to mean in context. A "source not found" is never fixed by typing the number: compute it from the results file or delete the sentence.

The signature test (rule). Sentence by sentence through both vehicles: "pulled out on its own with my name on it, do I stand behind it?" A sentence the human does not dare sign has two roads, lower the strength or delete it. The title gets the strictest test; it is the sentence quoted alone most often. This step is never outsourced; you run the list, the human answers per sentence.

Charts. Before any chart, answer "what judgment should the reader make?". You draw the chart and the caption. The human owns the error bars and the axes. A "large lead" drawn with the y axis starting near the top is the graphical cousin of wording drift: the numbers are right, the strength lies.

Limitations is not body armor. Honesty layering is a downgrade consistent across the whole document. A weakness admitted in limitations (an overconfident interval, template concentration) may not be cited as a victory in the abstract or the conclusion. Insuring an overclaim in the main text with a limitations section is worse than writing no limitations at all. A defect you declare is rigor; a defect someone else finds is an incident. What was promised and not done goes into limitations as outstanding, and not one number is invented for it.

Negative results go on top. The most common delivery failure for a negative result is burial, a FAIL spread across ten pages of "worth further study". One sentence, first line.

No invented recipient. Credibility comes from being recomputable, not from "already adopted". If it was not submitted, say it was not submitted. A pilot is called a pilot. Never write a CTO's sign-off, a reviewer, or an acceptance that did not happen.

Submission corner, five lines. Venue choice is an audience judgment: a mixed ending with a post-hoc overturn and decision-grade accounting fits a workshop, and inflating it into main-conference packaging completes the strength drift by hand; the engineering cousin is choosing internal team review before a report to management. Draft the point-by-point rebuttal, and leave how far each point concedes, and which comment is worth resisting, to the human. Review comments are a free red-team round. The "preliminary results" paragraph of a grant, proposal, or budget request is the disaster zone for drift, where pilot data grows into "an established method" under polishing. Numbers point to the repo, strength matches the evidence, and only what the human dares sign gets submitted.

Acceptance in one sentence: the audience arrives with its own question and hits the answer on the first screen, and any number challenged is traced to its source within fifteen seconds (illustrative). One draft sent to everyone fails it: readers do not reorder detail, readers stop reading.

## Procedure

Budget half a day (illustrative).

1. Build the claims-list skeleton from `templates/claims-list.md`: one row per claim with pointer, tier column blank for the human, signature column blank, outstanding row filled from every basis and arm signed off in the plan. Split preregistered and post-hoc rows. You write no claim text; you draft candidates and the human writes the strongest form dared.
2. Stop until the list is signed. Any UNSIGNED row keeps the header `STATUS: DRAFT, not for the decision chain` on every downstream file.
3. Generate both vehicles from the signed list only, with `briefs/audience-rewrite.md`, strength locked. Report from `templates/technical-report-skeleton.md`; memo from `templates/one-page-memo.md`.
4. Reconcile strength: compare every sentence against the list and mark each wording stronger than its row. Hand the marked list back.
5. Run `scripts/interlock.py`; then dispatch `briefs/interlock-check.md` in a separate session with only the two documents and the results file. List every disagreement among the three for the human to rule on.
6. Run the signature test sentence by sentence with the human. Lower or delete whatever is not signed.
7. After any later polish, rerun steps 4 and 5. Close the deliverable with the `verification level note:` line.

## Decision and vocabulary

| Where | Values |
|---|---|
| Claim tier | verified / still exploring (evidence accumulating or nobody knows) / falsified / outstanding |
| Signature per claim | dare / do not dare |
| Memo judgment column | has a shot / no shot / evidence void |
| Interlock per number | MATCH / MISMATCH / NOT FOUND / DOC-ONLY; plus SUPERLATIVE (no number in sentence) |

Per claim, the signature is the ruling: `ruling: dare / do not dare | signed by: UNSIGNED`. "No shot" and "evidence void" are the two most money-saving words in a memo; a judgment column reading "has a shot" in every row means the unfavourable conclusions were not delivered.

Trailer on the interlock result: `verification channel: separate session, <model or person>, brief: briefs/interlock-check.md, leak_check: clean`. An interlock run in the session that wrote the draft is `SAME-CHANNEL (void)`: the same session protects its own draft.

## Self-check

- [ ] Is there prose and no signed claims list? Delete the prose. The list comes first; the vehicles are generated from it.
- [ ] Did you write a claim's strength, or the name in the signature column? Candidates only; strength and name are the human's.
- [ ] Is the outstanding row empty on a plan that promised more than this round delivered? Fill it from the plan file; "not done" is a line.
- [ ] Does the abstract or the conclusion still sell a number that limitations admits is overconfident? Downgrade across the whole document.
- [ ] Did a number enter by hand after the interlock said NOT FOUND? Compute it from the results file or delete the sentence.
- [ ] Was the text polished after the last interlock and reconciliation? Both are void; rerun them.
- [ ] Does the memo name a recipient, a submission, or an adoption that did not happen? Remove it; a pilot is a pilot.

## Templates and briefs

- `templates/claims-list.md`: four fields plus the outstanding row; the single source of truth.
- `templates/technical-report-skeleton.md`: question, method, results with post-hoc in its own subsection, limitations with numbers, reproducibility.
- `templates/one-page-memo.md`: conclusion on top, three risk lines, table of at most five rows with a judgment column, one next step, one basis line.
- `briefs/audience-rewrite.md`: generation payload with strength locked; carries tier and signature columns.
- `briefs/interlock-check.md`: verification payload for number extraction and cross-document comparison, run after the script.
- `scripts/interlock.py`: every number in two documents traced to the results file; unquantified superlatives listed; exit non-zero on MISMATCH or NOT FOUND.
