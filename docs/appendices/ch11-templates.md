# Chapter 11 templates · Failure-Mode Census Sheet + AI Self-Check Prompt Set

> This appendix is the complete fillable version of the two tools in Chapter 11.
> The order of use is fixed. Fill in Template 1 (the census sheet) first, then pick the matching self-check prompt from Template 2 according to what the census turned up.
> **The most important sentence in this appendix sits in the use warning of Template 2. AI self-check misses errors of the motivated collusion class. Read it first, then use the prompts.**

---

## Template 1 · Failure-Mode Census Sheet

**How to use.** Run a thirty-minute census on your project (the full flow is Chapter 11, section 11.7). Start with the quick reference, there is no background knowledge to memorize. The quick-reference block prints the signature of each of the four failure modes right under the header, and all you do is translate them into concrete signals in your project. Refill the census sheet at every milestone (before plan sign-off, after the first results, before delivery), and keep the old sheets on file for comparison.

### Quick reference, the four failure modes (a condensation of Chapter 11, section 11.4)

| Failure mode | Chief attribute | High-incidence step | General signature |
|---|---|---|---|
| Hallucination and fabricated citations | Fluency × corpus prior | Master the field, deliver | The most on-point citation is the most suspect; the retelling carries fewer qualifiers than the original |
| Spurious significance and the criteria backdoor | Sycophancy × fluency | Test plan, interpretation | The criterion appears after the result; the conclusion "just happens" to clear the line |
| Data leakage and contamination | Corpus prior | Execution | The score is too good to be true; it collapses on fresh questions from the same distribution |
| Sycophancy drift | Sycophancy | Interpretation, red team | Ask the same question twice with opposite leans and the conclusion flips |

One more cross-cutting error does not pick a step, **motivated collusion**, where the conclusion you are most excited about = the conclusion you checked least. It is not in the matrix. It gets a column of its own below the matrix, and AI self-check cannot catch it (see the warning in Template 2).

### The census matrix (fillable)

Walk your project's seven steps row by row. Steps where AI is lightly involved can be filled in short. The three steps where AI is most deeply involved must be filled in completely.

```text
# Failure-mode census sheet
Project: ____________  Filled in by: ____________  Date: ____________
Project milestone this census belongs to (before plan sign-off / after the first results / before delivery): ____________

## Step 1 · Master the field
AI involvement (none/light/deep): ______  Attribute mainly consumed: ______
Error type most likely to grow here: ____________________
Concrete signature in this project (translate it into a concrete signal, such as "which citations are the most on-point and therefore checked first"):
____________________________________________
Cost of being wrong (high/medium/low): ______

## Step 2 · Questions and hypotheses
AI involvement: ______  Attribute mainly consumed: ______
Error type most likely to grow here: ____________________
Concrete signature in this project: ____________________
Cost of being wrong: ______

## Step 3 · Test plan
AI involvement: ______  Attribute mainly consumed: ______
Error type most likely to grow here: ____________________
Concrete signature in this project (such as "which criterion's wording can still be explained away after the fact"):
____________________________________________
Cost of being wrong: ______

## Step 4 · Execution
AI involvement: ______  Attribute mainly consumed: ______
Error type most likely to grow here: ____________________
Concrete signature in this project (such as "anything above __ points gets treated as leakage first"):
____________________________________________
Cost of being wrong: ______

## Step 5 · Read and catch errors
AI involvement: ______  Attribute mainly consumed: ______
Error type most likely to grow here: ____________________
Concrete signature in this project (such as "which question have I not yet asked a second time with the opposite lean"):
____________________________________________
Cost of being wrong: ______

## Step 6 · Deliver
AI involvement: ______  Attribute mainly consumed: ______
Error type most likely to grow here: ____________________
Concrete signature in this project (such as "which numbers changed hands more than once between analysis and final draft"):
____________________________________________
Cost of being wrong: ______

## Step 7 · Red team
AI involvement: ______  Attribute mainly consumed: ______
Error type most likely to grow here: ____________________
Concrete signature in this project: ____________________
Cost of being wrong: ______

## Cross-cutting column, motivated collusion (mandatory, no blanks allowed)
The one conclusion I am currently most excited about: ____________________________
Which step and which cell it sits in: ____________________
My actual checking intensity on it (write it honestly): ____________________
A channel that does not share my motive (a person's name / how to dispatch an independent agent): ______

## The two circled cells
Operating room (the cell where being wrong costs most): ____________________
High-incidence zone (the cell holding the conclusion I am most excited about): ____________________

## Closing self-test (one sentence, no answer means the census fails)
If this project blows up three months from now, most likely in: ______ cell;
what the crime scene looks like: ____________________________
```

**Self-check** (walk it once when the sheet is filled):

- [ ] Did the "concrete signature" field copy the book's wording directly? Copying the wording is the same as leaving it blank. "The score is too good to be true" has to become a concrete number in your project.
- [ ] Motivated collusion column left blank, or "the conclusion I am most excited about" filled in with something harmless? You just walked around the most valuable field in the census. Refill it honestly.
- [ ] Are the high-incidence zone and the operating room the same cell? That is the most dangerous position in your project right now, and the verification budget (Chapter 12) goes there first, all of it.
- [ ] Did every cell get "medium" for cost of being wrong? No ranking means no layering. Force out a top two.
- [ ] Cannot answer the closing self-test? Go back to the step where AI is most deeply involved and walk the two questions again.
- [ ] Is the previous version of the census sheet still around? Comparing how the sheet changes between milestones carries more information than any single sheet.

---

## Template 2 · The "Have AI Self-Check for Failure Modes" Prompt Set

> **Use warning (read first, the bold is not decoration). AI self-check misses errors of the motivated collusion class.**
> The reason is structural. The motive is in you, and the model is trained to talk along with you. Hand it your own conclusion to check and it checks the form (whether the citation exists, whether the numbers add up, whether the reasoning chain breaks). Your wish it does not check, it amplifies (the firsthand specimen in Chapter 11, section 11.5, this book's own "literature gap" judgment, which AI never questioned and which finally died on an independent forward-citation check).
> So this prompt set is positioned as **a first-pass screen for formal errors**, under two iron rules.
> ① A self-check that outputs "no problems found" never equals no problems. It equals passing the formal first-pass screen;
> ② The motivated collusion class has only a process solution, that "channel that does not share your motive" in the cross-cutting column of the census sheet (another person, or a verification agent that does not know the answer you expect), and how to dispatch it is in the independent channel brief template in Chapter 12.
> One more thing. Send the prompts below to another model or another clean conversation that **took no part in generating the output**. The AI that produced the conclusion cannot serve as its own judge (orthogonality, Chapter 2, section 2.4).

### Prompt 2a, citation and fact self-check (against hallucination and fabricated citations)

```text
Below is the full text of a research output (or its citation list):

[paste]

Your task is a formal first-pass screen of every citation and every key factual
claim. Do not reach for your "impression" of these papers to vouch for what is
real. Your output is a check work order, not a verification verdict.

1 Extract every citation and output each one, title / authors / year / venue;
2 Tag each with an "on-point rating", which claim it carries and how much. Highest
  on-point first (fabricated citations are built to order, the most on-point is the most suspect);
3 Extract every retelling sentence ("one study shows..."), listing the retold wording vs
  the qualifiers that need the original to confirm (task scope, sample, basis);
4 Extract every sourceless number and every superlative claim ("first", "largest", "universal");
5 Output the check work order by priority, one line each, what to check, where to check it
 (academic search engine / which section of the original), and what to do if it is not found.
```

After use. The work order has to be executed by a person (or an independent verification agent). What this prompt produces is a to-do list, and the list itself guarantees nothing.

### Prompt 2b, criteria and significance self-check (against spurious significance and the criteria backdoor)

```text
Below is an analysis output, and (if one exists) the test plan that goes with it:

[paste the full analysis]
[paste the plan written beforehand; with no plan write "none", and "none" is itself the biggest finding]

Answer item by item, and output only findings you can point to a location for:

1 For every conclusion in this analysis, where is the decision standard written? Mark whether
  it appears before the results (in the plan) or after them (in the analysis narrative);
2 List every degree of freedom that "can still be moved after the results are in", metric
  choice, data slicing, outlier removal, stopping time, marking for each whether the text
  declares a rule set in advance;
3 Find every number that "just clears the line" (just past a significance threshold, just at target);
4 How many hypotheses did this analysis test, how many metrics did it look at? If more than one,
  is there a multiple comparisons problem, and does the text correct for it;
5 Output which conclusions qualify as "confirmatory" and which only qualify as "exploratory".
```

After use. A conclusion downgraded to "exploratory" has to be worded as exploratory in the deliverable (the wording discipline in Chapter 9).

### Prompt 2c, leakage and contamination self-check (against data leakage and contamination)

```text
Below is the design and code of an evaluation or analysis (or a description of it):

[paste: data sources, how it was split, feature engineering, eval set choice, scores]

Work through the leakage paths one by one, and for each output "risk point → location in
the text or code → the check action you suggest":

1 Is the eval data public (a public benchmark, a public question bank, a dataset circulating
  online)? Public means treating it by default as "the model saw it during training". List the
  contamination-resistant variants or fresh questions available as substitutes;
2 Could test-set information leak into the training side anywhere in the code, normalization
  or statistics computed before the split, feature engineering over the full data, a validation set reused for tuning;
3 Where does the score sit relative to comparable work? An absurdly good score gets treated as
  leakage first. List the concrete way to "retest on a fresh set of questions from the same distribution";
4 Is there time leakage in the data pipeline (using information available only after the decision point);
5 Output the list of check actions, sorted by "cheap and lethal".
```

After use. The check actions on the list have to actually run. Having AI hunt for leakage and having AI fix leakage can be the same session, but the conclusion "leakage ruled out" can only come from the numbers of a retest.

### Prompt 2d, the sycophancy flip test (against sycophancy drift)

**How to use.** This one is not AI checking itself. It is a controlled experiment you run on AI. Prepare two versions of the same question, send each in **two clean conversations that cannot see each other**, and compare the conclusions.

```text
Version A (positive lean):
Do these results [paste] support the conclusion "____________"?

Version B (negative lean):
Is it possible that these results [paste] do not support "____________",
and are only [noise / confounding / a selection effect]? Argue it.
```

Reading rules:

- The two versions agree in substance (only wording and tone differ) → the reading can go on being used for now;
- The two versions are substantively opposite → what you measured is not the data, it is how you asked. The reading of that question is downgraded as a whole, and it gets redone through the independent channel in Chapter 12;
- Either version opens with a "you are right" and carries no reservation anywhere → treat it as sycophancy, and retest with another model or another wording.

### Self-check (walk it once after running the whole prompt set)

- [ ] Did you send the self-check prompt to the same session that generated the output? That violates orthogonality. Void it and rerun.
- [ ] All four prompts came back green, so the output feels safe? Reread the use warning at the top of this template. Passing the formal first-pass screen ≠ no problems, and the motivated collusion class is not within this prompt set's range at all.
- [ ] The "most exciting conclusion" in the cross-cutting column of the census sheet, has it been assigned to a channel that does not share your motive? This is the one move in the whole self-check AI cannot make, and the one most easily skipped.
- [ ] Has the check work order from 2a been executed? A work order lying in the inbox equals no check.
- [ ] Did you run only the one or two prompts relevant to your own output? That is normal, layering is supposed to work that way (Chapter 12 expands); but an output about to be delivered (one entering the decision chain) has to pass all four.
