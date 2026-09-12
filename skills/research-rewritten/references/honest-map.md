**Load this reference when:** you must label what a field's claims are worth, two headlines contradict each other, or anyone asks to mark something verified.
Source: chapter 13 (docs/chapters/ch13.md, docs/appendices/ch13-templates.md; the two disciplines from docs/chapters/ch02.md)

## Contents

1. Rules
2. Procedure: build the map from the last deliverable
3. Procedure: assign a status
4. Procedure: review
5. Procedure: read an "AI did research on its own" claim
6. Decision and vocabulary
7. Self-check
8. Templates and briefs

## Rules

Change the unit before answering. A headline's unit is the event; a judgment's unit is the claim. "Which headline is true" cannot be answered; "which row does this move" can. One row per claim, five columns, and each column has a rule.

| Column | Rule |
|---|---|
| Claim | One sentence that can die. Rewrite "X has a lot of promise" as "X beats [baseline] on [setting]". Carry the qualifiers; they are part of the claim. A sentence that will not go into falsifiable form is a slogan and gets no row |
| Current status | verified / still exploring (evidence accumulating or nobody knows) / falsified. When unsure, still exploring, then mark the grade. "Basically verified" is banned |
| Key evidence | Identifiable items only: papers, controlled measurements, practice many users can reproduce. "Industry consensus" and "everyone says so" are not accepted |
| What evidence would change its status | Written as a search instruction, both the upgrade condition and the downgrade condition: "on seeing X, change to Y". The most valuable column: it forces you to write down how the status dies at the moment you write it |
| Last review date | Changes on every review, even when the status did not move |

Status definitions:

- Verified requires all three at once: production-grade evidence (not a demo, not a case write-up); independent sources ≥ 2, or you reproduce it with your own hands; a written falsification shape (the fourth column is not empty). Missing any one: still exploring.
- Still exploring is the default when neither end is reachable. Two grades: evidence accumulating (the direction shows, the volume does not) and nobody knows (not even a direction). Daring to write "nobody knows" is what separates a map from a headline.
- Falsified requires either one: a criterion written down in advance was triggered, or a reproducible counterexample punched through the claim as stated. Punching through the unconditional form is not punching through the weakened form. Give the surviving weak form a row of its own. Falsified rows stay, with date and evidence; tombstones are part of a map's credit.

Two disciplines screen the evidence before anything else (rule):

1. Demo is not production. Demo videos, case write-ups, and vendor material qualify only to trigger an investigation, never to decide a status. Status recognizes production-grade evidence only.
2. Self-perception is not evidence; calibration comes from measurement. "Everyone who used it says it's great" does not enter the evidence column. Controlled measurements do.

Evidence levels:

| Level | Form of evidence | What it can support |
|---|---|---|
| E1 | Controlled measurement against preregistered criteria; independent replication by several parties | Can set verified or falsified |
| E2 | A single peer-reviewed study or systematic evaluation | Can set a direction; alone not enough for verified |
| E3 | Production practice reproducible by many users | Can support verified for workflow-type claims |
| E4 | Demos, case write-ups, vendor material | Only triggers an investigation |
| E5 | Hearsay, intuition, self-report | Does not enter the evidence column |

The highest-level evidence in a row decides its status (rule). A row whose evidence column holds only E4 or E5 drops to still exploring at once.

The most dangerous row is the one you want to be true. For any row where "this row holding is good for me", the required evidence level goes up one notch (rule).

Status changes pass through a human (rule). You run the fifth column's searches and propose date changes. You never change a status and never issue "verified". A map maintained automatically has every row fluent, complete, and confident, and never volunteers which block it missed.

Copy structure, not status. A status is a reading of the evidence at one point in time through one pair of eyes. From anyone else's map, this one included, take the five columns and re-derive or spot-check the status yourself.

One illustrative row pair (illustrative):

| Claim | Status | Key evidence | What would change it |
|---|---|---|---|
| Method X beats the baseline (unconditional form) | Falsified | Several independent measurements show the gain is non-monotonic in scale and disappears under default settings; a strongly tuned baseline nearly catches up | None. The unconditional form is dead; the live argument is the next row |
| Under cost alignment, method X has a net gain on task families of type T | Still exploring (evidence accumulating) | Two systematic evaluations, each carrying counterexamples; the conclusion is task-dependent; both camps' evidence stays real | A comparison on a stated cost basis with a same-budget baseline as a third arm, across task families |

## Procedure: build the map from the last deliverable

Do not start from "what are the big claims in my field"; that yields a pile of slogans. Start from money already bet.

1. Take the user's most recent deliverable (report, paper, slide deck, review). Copy out the claims it cited or took as true by default, until there are 10 (illustrative).
2. Force each into one sentence that can be judged true or false. Ones that will not go, keep as is and label "slogan". Discovering a cited slogan is a gain on its own.
3. Build the empty five-column table from `templates/honest-map.md`. The human fills the gut status.
4. The human fills the fourth column. Any row where it cannot be written drops to still exploring (nobody knows) without exception (rule). A claim whose death you cannot write down, you do not know what keeps it alive.
5. Fill the evidence column, each item identifiable. If nothing harder than "everyone says so" can be written, send it back and return to step 4. Then mark today's date and set the cadence.

Ten rows all verified is a placebo, not a map (rule). Go back to step 1 and add the claim the human least dares to touch.

## Procedure: assign a status

1. Screen every evidence item with the two disciplines. Drop demo and self-report items from the evidence column.
2. Grade what remains E1 to E5. The highest level present decides.
3. Apply the three definitions. Verified needs all three conditions; falsified needs one of two; everything else is still exploring with a grade.
4. Run the self-consistency audit: "how did I treat this type of evidence elsewhere on this map?" The same type of evidence enjoying different treatment in two rows means one row has a preference mixed in. Find which row you wanted true; that is where it landed.
5. Raise the bar one notch on every wanted-true row.
6. Write the proposed status as a draft. The human enters it.

## Procedure: review

Review equals running the fifth column, row by row. It does not require rereading the literature. The fourth column is a ready-made search instruction; check whether that kind of evidence has shown up.

Three legal moves after checking, and no fourth: change the status (the evidence arrived); change the evidence (a harder source replaced it); change the date (checked, nothing moved). Even when only the date changes, it must change (rule). A map whose review dates do not move is a dead map, and a dead map is more dangerous than no map, because it still wears the skin of a map. Log one line per review: date, which rows moved, why. You run the searches; the human moves the status.

| Current status | Cadence | Example trigger |
|---|---|---|
| Verified | Every 6 months (illustrative), or at once on a field-level event | A new model generation ships; the workflow you depend on changes heavily |
| Still exploring (evidence accumulating) | Every 3 months (illustrative) | A new study of the type the fourth column describes appears |
| Still exploring (nobody knows) | Event-driven, plus one scan every 6 months (illustrative) | The evidence the fourth column describes shows up for the first time |
| Falsified | Not reviewed; tombstone kept | none |
| Pending backfill | Tied to when the experiment or event completes | A preregistered experiment reports results |

## Procedure: read an "AI did research on its own" claim

A milestone report is E4 until it passes three questions. Ask them in order, then the fourth from the delegation ladder.

1. What level is the venue? A workshop, a leaderboard, an internal deployment, and a main conference are different exam halls. Changing exam halls is not passing.
2. Was the review informed? Reviewers told that AI papers were mixed in, organizers who approved in advance, or undisclosed submission each change what one acceptance proves.
3. How far did humans intervene? Rebuttals written by humans, wet-lab work done by humans, effect sizes revised down on human reanalysis all reduce the claim.
4. Who answers when it's wrong? In academic publishing the answer is nobody. In an in-company setting an institutional answer may exist, at the price that the output never enters the public body of knowledge.

One paper accepted says it passed one spot check. It does not say the process deserves the name "autonomous researcher". The row stays still exploring until three things come together: stable acceptance at mainstream venues under informed review, independent replication, and a named person who answers when it's wrong.

## Decision and vocabulary

| Slot | Allowed values |
|---|---|
| Claim tier | verified / still exploring (evidence accumulating or nobody knows) / falsified / outstanding |
| Evidence level | E1 / E2 / E3 / E4 / E5 |
| Review move | change status / change evidence / change date |
| Claim form | falsifiable sentence / slogan |

Every proposed status is a draft: `ruling: <tier> | signed by: UNSIGNED`. You never write "verified" into a status cell.

## Self-check

- [ ] Did a demo, a case write-up, or a self-report land in the evidence column? Remove it; it triggers an investigation, nothing more.
- [ ] Is any fourth column empty? Drop that row to still exploring (nobody knows).
- [ ] Is every row verified? Placebo. Add the claim the human least dares to touch.
- [ ] Did the same type of evidence get different treatment in two rows? Find the wanted-true row and raise its bar.
- [ ] Did you change a status yourself, or copy one from someone else's map? Revert it to a draft and hand it to the human.
- [ ] Did a falsified unconditional claim take its weak form down with it? Give the weak form its own row.
- [ ] Did a review end with no date change? Change the date. A dead map wears the skin of a map.

## Templates and briefs

- `templates/honest-map.md`: the five-column table, the status rules card with E1 to E5, and the cadence table.
