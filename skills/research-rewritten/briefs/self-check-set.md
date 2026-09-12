# AI self-check set for the four failure modes
Kind: GENERATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

**Use warning, read before you dispatch (the bold is not decoration).** AI self-check misses the motivated-collusion class of error, where the conclusion you are most excited about is the conclusion you checked least. The reason is structural: the motive is in you, and the model is trained to talk along with you. Hand it your own conclusion and it checks the form (does the citation exist, do the numbers add up, does the reasoning chain break); your wish it does not check, it amplifies. So this set is a first-pass screen for formal errors, under two rules. 1 A screen that returns "no problems found" never equals no problems; it equals passing the formal screen. 2 The motivated-collusion class has only a process fix: a channel that does not share your motive, a person or an agent that does not know the answer you want, dispatched through briefs/rederive.md or the four red-team orders. Send these prompts to a session that took no part in producing the output; run in the producing session, the trailer reads SAME-CHANNEL (void).

The four prompts are the formal first-pass screen for fabricated citations, the criteria backdoor, leakage, and sycophancy drift. Each returns a work order or a comparison, never a verdict; a returned work order that no one executes equals no check. Run the one or two that match your output for a desk draft; an output entering the decision chain runs all four.

## Prompt(s)

```text
Below is the full text of a research output, or its citation list:

[paste]

Run a formal first-pass screen of every citation and every key factual claim. Do not
reach for your impression of these papers to vouch for what is real. Your output is a
check work order, not a verdict.
1 Extract every citation and output each one: title, authors, year, venue;
2 Tag each with an on-point rating, which claim it carries and how much, most on-point first (a fabricated citation is built to order, so the most on-point is the most suspect);
3 Extract every retelling sentence ("one study shows..."), setting the retold wording beside the qualifiers that need the original to confirm (task scope, sample, basis);
4 Extract every sourceless number and every superlative ("first", "largest", "universal");
5 Output the check work order by priority, one line each: what to check, where to check it (search tool, which section of the original), and what to do if it is not found.
```

```text
Below is an analysis output and, if one exists, the test plan written beforehand:

[paste the full analysis]
[paste the plan; with no plan write "none", and "none" is itself the largest finding]

Answer item by item, and output only findings you can point to a location for:
1 For every conclusion, where is the decision standard written? Mark whether it appears before the results (in the plan) or after them (in the narrative);
2 List every degree of freedom that can still be moved after the results are in (metric choice, data slicing, outlier removal, stopping time), marking for each whether the text set a rule in advance;
3 Find every number that just clears the line (just past a threshold, just at target);
4 How many hypotheses and how many metrics did this analysis look at? If more than one, is there a multiple-comparisons problem, and does the text correct for it?
5 Output which conclusions qualify as confirmatory and which only as exploratory.
```

```text
Below is the design and code of an evaluation or analysis, or a description of it:

[paste: data sources, how it was split, feature engineering, eval set choice, scores]

Work the leakage paths one by one; for each output "risk point, location in the text or code, the check action you suggest":
1 Is the eval data public (a public benchmark, a public question bank, a dataset circulating online)? Public means treat it by default as seen in training. List contamination-resistant variants or fresh questions available as substitutes;
2 Could test-set information leak into the training side anywhere in the code (normalization or statistics computed before the split, feature engineering over the full data, a validation set reused for tuning)?
3 Where does the score sit relative to comparable work? A score too good to be true gets treated as leakage first. List the concrete way to retest on fresh questions from the same distribution;
4 Is there time leakage (using information available only after the decision point)?
5 Output the check actions, sorted by cheap and lethal.
```

```text
Version A (positive lean), sent in one clean conversation:
Do these results [paste] support the conclusion "____________"?

Version B (negative lean), sent in a second clean conversation that cannot see the first:
Is it possible these results [paste] do not support "____________", and are only
[noise / confounding / a selection effect]? Argue it.
```

The flip test is not the model checking itself; it is a controlled experiment you run on the model. Prepare the two versions of one question, send each in a clean conversation that cannot see the other, then read by these rules:
- The two agree in substance (only wording and tone differ): the reading can go on being used for now.
- The two are substantively opposite: what you measured is how you asked, not the data. Downgrade that reading as a whole and redo it through an independent channel (briefs/rederive.md).
- Either version opens with "you are right" and carries no reservation anywhere: treat it as sycophancy and retest with another model or another wording.

## Leak self-check
- [ ] Sent to the same session that generated the output? Orthogonality broken. Void it and rerun in a session that took no part in producing it.
- [ ] All four came back green so the output feels safe? Reread the use warning. Passing the formal screen is not no problems, and the motivated-collusion class is out of this set's range entirely.
- [ ] The one conclusion you are most excited about, assigned to a channel that does not share your motive? This is the single move the screen cannot make and the one most easily skipped.
- [ ] The citation work order still sitting in the inbox? A work order no one runs equals no check.
- [ ] Downgraded a conclusion to exploratory here but wrote it in the deliverable as confirmatory? Word it as exploratory where it ships.

## Before you dispatch
`python scripts/leak_check.py brief briefs/self-check-set.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/self-check-set.md, leak_check: clean
