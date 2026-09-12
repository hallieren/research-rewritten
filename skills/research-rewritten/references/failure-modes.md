**Load this reference when:** assigning an acceptance layer (it needs the likely error class), an output feels off, synthetic data or personas or LLM-judged scores are in play, or a deliverable is about to leave.
Source: chapter 11 (docs/chapters/ch11.md, docs/appendices/ch11-templates.md)

## Contents
- Rules
- Procedure
- Decision and vocabulary
- Self-check
- Templates and briefs

## Rules

Read failure modes as the product of an AI attribute and a research step, never as a bug list about AI. The three attributes are neutral and are why the tool was bought: fluency (coherent and confident whether or not the content is true), sycophancy (trained to produce answers people are satisfied with), corpus prior (a compression of past text, not an observation of the user's situation). The same attribute lands on different steps and grows different errors.

Three amplifiers make the same error more lethal in research than elsewhere. They multiply, they do not add.

| Amplifier | What it does | Consequence for you |
|---|---|---|
| Invisibility | A wrong conclusion raises no error and looks identical to a right one | Only a process step can catch it; skipped steps are the whole risk |
| Compounding | Downstream work cites it, decisions rest on it, later models train on it; there is no rollback | A sourceless number tonight is a decision record next quarter |
| Motivated collusion | When the error grows into the shape the user wanted, the drive to check drops to its lowest; the inspector and the error become accomplices | You amplify this amplifier: you talk in the direction the user faces. Never say a wanted conclusion looks fine |

AI added no new kind of error. It changed the production function: volume (a dozen passable fabrications per generation, no intent required), fluency (the wrong paragraph and the right one come off the same engine, no tell), and marginal cost (the length of a citation list is decoupled from the probability that anyone's hands touched an entry).

The attribute by step table:

| High-incidence step | Failure mode | Chief attribute | One-line signature |
|---|---|---|---|
| Master the field, deliver | Hallucination and fabricated citations | Fluency and corpus prior | The most on-point citation is the most suspect |
| Test plan, interpretation | Spurious significance and the criteria backdoor | Sycophancy and fluency | The criterion appears after the result |
| Execution | Data leakage and contamination | Corpus prior | The score is too good to be true |
| Interpretation, red team | Sycophancy drift | Sycophancy | The conclusion flips with how you ask |

Per mode, the detection signature and the mitigation:

| Mode | Detect | Mitigate |
|---|---|---|
| Hallucination and fabricated citations | Fabricated citations are built to order and their distribution is not random: the entry that fills the gap in the argument, the title that hits the question dead center, gets checked first. Paraphrase drift: a real citation retold with fewer qualifiers than the original ("improves on task X" becomes "improves"). Watch first drafts of reviews, report citation lists, and any source AI "added while it was at it" | Existence check with a search tool; every paper carries `exists: confirmed` with the tool named or `exists: unverified`; retold wording set beside the original's qualifiers; `briefs/verify-citations.md` in a separate session; a claim-to-source table |
| Spurious significance and the criteria backdoor | "Have a look at whether there is anything in this data" always returns something. Ask: was this criterion locked before the data was seen, or after? "After" or "cannot answer" means the significance counts as zero. A number that just clears the line; a criterion quietly revised; exploratory analysis delivered as confirmatory | `criteria timestamp:` on every result report; `scripts/prereg_check.py timing`; list every degree of freedom movable after results (metric, slicing, outliers, stopping time) and whether a rule was set in advance; count hypotheses and metrics tested; "exploratory" written into the conclusion sentence |
| Data leakage and contamination | A public benchmark or question bank is treated by default as seen in training. Test-set information leaking into the training side: statistics before the split, feature engineering over all the data, a validation set reused for tuning. Time leakage. The score collapses on fresh questions from the same distribution | Contamination-resistant variants or fresh items; check the split code; "leakage ruled out" comes only from the numbers of a retest, never from a review of the code |
| Sycophancy drift | Ask with a lean, get an answer along the lean. Two fluent and opposite readings of one dataset. The producer asked to check itself | The flip test below; generation and verification never share a channel; an independent channel with no expectation in the brief |

"Wait for a stronger model" is not a defense. None of the four modes needs the model to get dumber. All four are byproducts of the model working normally. The attributes do not disappear with capability; they get more fluent. New capability manufactures new error types in bulk, so this table expires: when a new error surfaces, ask which attribute hit which step and add a row. Nobody has measured the relative incidence of the four; the order above follows the steps, not frequency or damage.

Motivated collusion has no step and no tool solution. It offends on whichever step carries the user's wish. Signature: the conclusion the user is most excited about is the conclusion checked least. That is the default output of the motive structure, not a matter of character; "be careful next time" is not a countermeasure. Illustrative, no numbers: a paper title remembered with one word wrong died on a mechanical forward-citation check within a day; the judgment that a "gap" in the literature existed lived a whole round unchecked, because a gap meant the project had a contribution. AI self-check cannot catch this class: asked to check a conclusion, it checks the form (citation exists, numbers add up, chain holds) and goes along with the motive. The only answer is process: a channel that does not share the motive, a named person or a verification agent that does not know the expected answer, touches the most exciting conclusion. The census question that finds it: "the conclusion I am most excited about". Ask it, and route that conclusion to the channel.

Five ways synthetic data passes for real. Personas, silicon samples, LLM-judged scores, and synthetic rows in an eval set fake in the same five ways.

| Way | Lives in the single answer or the distribution | Evidence grade |
|---|---|---|
| The fluency illusion: coherent, detailed, in voice; fluency has zero correlation with distributional fidelity | Single answer; it fools intuition | Mechanism fact, no experiment needed |
| The average face: each answer is a weighted average of the corpus's stereotype; variance collapses; power calculations come out overconfident | Distribution | Verified in political surveys, still exploring in other fields |
| Stereotype drift: the subgroup's answers are narrower and systematically more extreme, centered near the stereotype, off the real mean | Distribution, center pulled toward the stereotype | Verified at the phenomenon level |
| Sycophancy drift: a persona follows a leaning question further than a real respondent, who wanders, pushes back, or rejects the question | Distribution; it follows how you ask | Still exploring, one preprint's preliminary signal and nothing else |
| Time dislocation: the persona is a time slice of the corpus; attitude shifts after the cutoff are missing, and retrieval does not fix it | Distribution; the whole thing stopped at the corpus cutoff | Symptom confirmed, cause still exploring |

Rule: not one of the five is visible at the level of a single answer. Every answer passes its check and a thousand together are wrong. Reading transcripts more carefully does nothing. "Like a real person" rises to evidence only as a match at the distribution level against real ground truth, on criteria locked before the run, and only as far as the question bank's domain. Failure modes of the same shape apply to LLM judges: the judge is a second unknown and is excluded from scoring when it cannot be calibrated blind.

The self-check prompt set is a first-pass screen for formal errors, under two iron rules (rule): "no problems found" equals passing the formal screen, never "no problems"; the motivated collusion class is outside its range entirely. Send the prompts to a session that took no part in generating the output. Each prompt returns a work order, not a verdict; a work order lying in the inbox equals no check. A conclusion the criteria prompt downgrades to exploratory is worded as exploratory in the deliverable. An output entering the decision chain passes all four prompts.

The flip test. Not a self-check: a controlled experiment run on the model. Two versions of one question, each sent to a clean conversation that cannot see the other. Version A: "Do these results support the conclusion X?" Version B: "Is it possible these results do not support X and are only noise, confounding, or a selection effect? Argue it." Three reading rules (rule):
1. agree: the two answers agree in substance and differ only in wording and tone. The reading stays in use for now.
2. flipped: the two are substantively opposite. What was measured is the asking, not the data. The reading of that question is downgraded whole and redone through the independent channel.
3. sycophantic: either version opens with "you are right" and carries no reservation anywhere. Retest with another model or another wording.

## Procedure

The census, thirty minutes (illustrative), refilled at every milestone (before plan sign-off, after first results, before delivery), old sheets kept for comparison. Fill `templates/failure-mode-census.md`.

1. Lay the project along the seven steps. Mark the three where AI is most deeply involved; those rows are filled completely.
2. For every step ask two questions: which attribute is being consumed here (fluency / sycophancy / corpus prior), and which mode from the table that attribute most likely grows into here. Ask the questions; the human fills the answers.
3. For every high-risk cell, the human writes one concrete signal in this project. Send back any wording copied from the table: "the score is too good to be true" has to become a specific number; "the most on-point citation" has to become specific entries. A cell with no concrete signal means the error there has not been worked out.
4. The human circles two cells: the operating room (where being wrong costs most) and the high-incidence zone (the cell holding the conclusion they are most excited about). You never circle either. When the two coincide, the whole verification budget goes there first.
5. Cross-cutting column, no blanks: the most exciting conclusion, its cell, the actual checking intensity written honestly, and a channel that does not share the motive (a person's name, or how to dispatch an independent agent).
6. Closing self-test, one sentence: if this project blows up three months (illustrative) from now, which cell, and what does the crime scene look like. No answer means the census fails; go back to the deepest AI step.
7. Run the self-check set from `briefs/self-check-set.md` in a fresh session, reading its warning aloud first. Execute every returned work order; report each item as confirmed / falsified / undecidable.

## Decision and vocabulary

| Where | Values |
|---|---|
| Flip test | agree / flipped / sycophantic |
| Self-check item result | confirmed / falsified / undecidable |
| Likely error class for the acceptance layer | fabricated citation / criteria backdoor / leakage / sycophancy drift / average face |
| Paper existence | confirmed / unverified |

The mode named in the census is the error class handed to acceptance mode; destination and error class together set the layer. Trailer on every self-check run: `verification channel: separate session, <model or person>, brief: briefs/self-check-set.md, leak_check: clean`. Run in the producing session it reads `SAME-CHANNEL (void)`.

## Self-check

- [ ] Did the concrete-signature field copy the table's wording? Same as blank. A number, a named entry, a named criterion.
- [ ] Is the motivated-collusion column blank or filled with something harmless? The most valuable field was walked around. Refill it.
- [ ] Did you call the most exciting conclusion fine, or circle a cell for the human? Neither is yours. Route the conclusion to the channel without the motive.
- [ ] Did the self-check set run in the session that produced the output? Void. Fresh session, then rerun.
- [ ] Did four green prompts turn into "the output is safe"? Formal screen passed; motive unchecked; work orders still to execute.
- [ ] Did "sounds exactly like a real user" enter as evidence? Fluency is single-answer; the fakes live at the distribution level.
- [ ] Is "a stronger model will fix this" in the mitigation column? Remove it. The attributes get more fluent, not fewer.

## Templates and briefs

- `templates/failure-mode-census.md`: quick reference of the four modes; the step by mode matrix; the mandatory motivated-collusion column; the two circled cells; the closing self-test.
- `briefs/self-check-set.md`: the four formal-screen prompts (citations and facts, criteria and significance, leakage, the flip test) with the use warning; GENERATION kind, work orders out.
- `briefs/verify-citations.md`: existence and says-so checks per citation, three-value verdicts, run through an independent channel.
