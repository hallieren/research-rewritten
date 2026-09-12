**Load this reference when:** the user is entering an unfamiliar field, holds a direction with no finished state, wants a question sharpened, or needs a hypothesis written in a form that can be falsified.
Source: chapter 4 (docs/chapters/ch04.md, docs/appendices/ch04-templates.md) and chapter 5 (docs/chapters/ch05.md, docs/appendices/ch05-templates.md).

## Contents

- Rules
- Procedure: three-layer intake (field)
- Procedure: coverage check
- Procedure: five steps to sharpen a question
- Decision and vocabulary
- Self-check
- Templates and briefs

## Rules

1. "Master a field" means "can ask it something": put an insider's question to the field and know how to check the answer. Reading volume is not the criterion.
2. Map before detail. Camps, representative works, and the substance of their disagreement come before any single paper is read closely.
3. Every paper you list carries `exists: confirmed` with the search tool named, or `exists: unverified`. A citation enters notes only after two checks: the paper exists in an academic search engine, and it contains the sentence you paraphrased. You never run the existence check on the human's behalf.
4. Any claim entering a decision goes back to the original passage. Secondhand retelling drifts: each hand drops a qualifier ("improves on arithmetic tasks" becomes "improves"; "when cost is unconstrained" disappears).
5. Paper cards carry `How much I believe it:` blank. The human fills it after reading the key passages. You never fill it.
6. The done test for a map, asked verbatim: "Can you predict what evidence would change this map?" No answer means the human toured the field and has not moved in.
7. A direction has no finished state; a question has one (answered or falsified, then over). Size does not separate them. Only the finished state does.
8. Three tests, none skipped: testable (what evidence would kill it), worth answering (the answer changes action), affordable (the road to evidence is walkable). Testable is a veto. The human scores; you attack.
9. Mirror risk: your candidates come from the corpus, so "already asked" is covered densely and "nobody has asked" thinly. Your list is a floor, not a ceiling. "Not seen" means unsure, not novel.
10. Which question is worth answering has no cheap ground truth, raises no error when wrong, and costs months to redo. You propose candidates; you never recommend one. Nobody answers for "I recommend candidate 3".
11. No scoring by an LLM judge when the judge is a second unknown. One question with two unknowns is zero answerable questions. Scoring is programmatic, cheap, and uncontested, or the task changes.
12. Total defeat is legitimate. A run where no candidate clears all three gates saved weeks; say so and route back to the map or loosen a resource constraint.

## Procedure: three-layer intake (field)

1. Pin the human's one-sentence question. Paste it at the top of every reply so it survives the search.
2. Map layer. Fire the controversy-map prompt (`briefs/controversy-map.md`): 3 to 6 camps (illustrative) with a core claim each, 2 to 3 representative works per camp (illustrative), the substantive disagreements in the form "if A is right, B is wrong", and the 1 to 2 disagreements the question lands in. List only papers you can give a real source for; mark the rest "unsure".
3. Build the controversy map table `claim | supports | opposes | substance of the disagreement` from `templates/controversy-map.md`. Every paper read later is filed into a row.
4. Existence check, about 20 minutes (illustrative), no skipping. The human confirms each listed paper in an academic search engine. Until they finish, every row reads `exists: unverified` and you may not call the map trustworthy.
5. Skeleton layer. For each load-bearing paper (each camp's representative works, the repeatedly cited sources, the empirical studies tied to the question; 5 to 15 papers, illustrative), generate a card from `templates/paper-card.md`: core claim in the paper's own wording, evidence (experiment, data, scale), where the claim applies (limits admitted, including footnotes), which prior work it refutes or depends on, and the blank belief field. Then take the human's questions to the paper: is the baseline fair, how much gain survives cost alignment, what did the limitations dodge.
6. Frontier layer. Set citation alerts on the 3 to 5 load-bearing papers (illustrative). Weekly scan (a fixed half hour, illustrative) in three columns: new evidence relevant to the map / signals the map needs changing / noise. Admission criterion (rule): a new paper enters the skeleton layer if and only if it could change who wins a row of the controversy map. Everything else flows past.
7. Test question before closing: which disagreement does the human's question land in? If none, either the question already has an accepted answer (look it up) or the real battlefield is not found yet (change search terms, go back to step 2).

## Procedure: coverage check

Run all four before the map is handed over. A single search path has systematic blind spots, and you never volunteer "I missed a community".

1. Keyword multipath. Generate 5 to 8 sets of search terms (illustrative) from different terminology systems; the same thing goes by different names in different communities. Run a round on each.
2. Citation graph. From the load-bearing papers, walk one layer forward (who cited them) and one layer backward (who they cited).
3. Reverse test. Ask: if one paper could overturn the current map, what would it look like and which community would it sit in? Then search for it.
4. Human anchor. The human shows the map to someone who knows the field and asks "what did I miss". A structural omission takes an expert ten minutes to spot (illustrative).

The most expensive miss is the human's own: a "gap in the literature" they want to exist, which you only wrap to look more real. A gap that survives the scan must also survive the forward-citation walk and the reverse test before it is written into a question.

## Procedure: five steps to sharpen a question

Budget one hour (illustrative). Input: a direction plus the controversy map. Output: one hypothesis with a falsification condition, or an honest "it will not sharpen".

1. Diverge. Run the diverge prompt (`briefs/diverge-candidates.md`): 20 candidates (illustrative) covering grain sizes from "worth a paper" to "worth an afternoon", at least 5 (illustrative) that the opposition would ask first, one refutation line each (no line, no listing), and an "already asked" mark with the clue. Mark each candidate `already asked` / `not seen` / `unsure` with a source for the mark. The novelty space sits near the unmarked lines.
2. Score. The human scores each candidate 0, 1, or 2 on the three tests and writes a reason. You attack only (testability, action, cost) and never patch. A 0 on testable is out on the spot; if the human forgets the veto, remind them. Top three by total go on.
3. Rewrite falsifiable. The human writes the pattern; you supply three versions (thresholds strict to loose) only when they are stuck, stating which slot was hardest to fill and what you assumed:

   ```text
   Under [conditions/basis], the [measurable metric] of [subject], compared with [control], is [direction and threshold].
   If [specific observed outcome] is observed, the hypothesis is falsified.
   ```

   You judge one thing: does the sentence say what counts as losing. Wish sentences ("explore the possibility of X", "validate the effectiveness of Y") fail; cure them by pouring in nouns: which metric, compared with whom, how big a gap.
4. Action rehearsal. Assume yes, then no; the human writes what the decision maker does differently in each case. Same action both ways means the question is decoration; back to step 2. Then list 2 to 3 middle outcomes (illustrative): partly holds, holds at extra cost, holds only on a subset. Check each against the falsification condition. Where the condition is silent is a hole; the rehearsal rehearses the falsification condition, not only the answer. A missing cost boundary (a tie bought at unlimited money) is the standard hole.
5. Resource check. List the shortest route to the observed outcome, the biggest cost per step, and three shrink options (scope, metric, control), each marked "still the same question: yes/no". Walkable is the human's ruling. Accept only shrinks that keep the question the same.
6. The survivor goes onto `templates/question-sharpening-card.md`, and the human signs the date. Threshold values carry their reasons and get final sign-off at the test plan.

## Decision and vocabulary

Direction versus question:

| Symptom | Verdict | Move |
|---|---|---|
| Can always "read a bit more"; no condition under which it is over | Direction | Run the five steps |
| Answered or falsified ends it; a specific observation kills it | Question | Proceed to the test plan |

Status of a listed paper and of a claim taken from it:

| Line | Meaning | Who sets it |
|---|---|---|
| `exists: confirmed (<search tool>)` | The paper was opened in an academic search engine | The human |
| `exists: unverified` | Listed from memory or from your output; not yet opened | You, by default, on every listed paper |
| `says so: confirmed` | The original passage carries the paraphrased claim with its qualifiers | The human, after reading the passage |
| `paraphrase drift` | The original carries a qualifier the summary dropped | Either; the claim reverts to the original wording |

The gray-band table (rule: read family by family, no aggregation across families; a total averaged over families represents nobody's decision):

| Result on one task family | Verdict |
|---|---|
| Trails by ≤ ε (the tie line, <value>) | tie |
| Trails by more than ε and up to the loss line (<value>) | undecided; report as is, no picking a side |
| Trails by more than the loss line | this family lost |
| Every family lost, or catching up only above the cost boundary (<value> times the control's cost) | hypothesis falsified |

Losing one family does not kill the hypothesis when "which families have a shot" is part of the question. The tie line, the loss line, and the cost boundary are judgments, not theorems; each carries a written reason and is signed by the human.

Flags in this step:

| You see | Name | Response |
|---|---|---|
| More than half the candidates restate the literature brawl | Mirror risk | Read the "already asked" column as a free novelty check; the novelty space is elsewhere |
| A metric scored by an LLM judge | Second unknown | Exclusion rule: switch to programmatic scoring or change the task |
| The hour is long over and the question is "one polish short" | Over-sharpening | Stop; fire the tracer bullet with the good-enough question and let evidence sharpen it |
| No candidate clears all three gates | Total defeat | Legitimate result; back to the map for another battlefield, or loosen a constraint |
| "I recommend candidate 3" | Knob past the safety line | Delete the recommendation; list candidates with marks and reasons |

## Self-check

- [ ] Did you list a paper without a source, or leave `exists:` unset? Mark it `unverified` and hand the check to the human.
- [ ] Did you call the map trustworthy, complete, or done before the human finished the existence check and the four coverage lines? Retract; the done test is "what evidence would change this map".
- [ ] Did you fill `How much I believe it:` or find the "if A is right, B is wrong" line for the human unasked? Blank it; hint only when they cannot.
- [ ] Is the human's question missing from the top of your reply? Paste it.
- [ ] Did you score a candidate, pick a survivor, or write the falsifiable sentence unasked? Undo; you attack, supply versions when stuck, and judge only "does it say what counts as losing".
- [ ] Does the falsification condition have no verdict for a middle outcome? Report the hole; the human rewrites.
- [ ] Is the survivor marked "already asked"? Say so before the card is signed.

## Templates and briefs

- `templates/controversy-map.md`: the claim / supports / opposes / substance table, the admission rule, and the four coverage lines.
- `templates/paper-card.md`: the fixed card format with the belief field left for the human.
- `templates/question-sharpening-card.md`: direction, candidate pool, three-test scores, the falsifiable sentence, action rehearsal, resource check, signature.
- `briefs/controversy-map.md`: the map prompt, the paper-card prompt, and the weekly scan prompt (GENERATION).
- `briefs/diverge-candidates.md`: the five-step prompts including the "already asked" detector and the juror "attack only, do not patch" (GENERATION).
