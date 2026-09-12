# Diverge candidates brief
Kind: GENERATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

Five prompts, run in order; everything they produce lands on templates/question-sharpening-card.md. Counts and the one-hour budget are illustrative. The three-test scores, the falsifiable sentence, and the pick are the human's; the model supplies candidates and counterpoints only.

## Prompt(s)

Step 1, diverge candidates. Item 4 is the "already asked" detector; do not delete it.

```text
My direction: [one sentence describing the vague direction].
Background, the controversy map: [paste or summarize: main camps / load-bearing papers / the real disagreement].
My constraints: [time budget] / [available data and hardware] / [the edge of my skills].

Generate 20 candidate research questions. Requirements:
1. Cover different grain sizes, from "worth a paper" to "worth an afternoon";
2. Cover different positions; at least 5 are questions the opposition or a skeptic would ask first;
3. Attach to each question one line, "what evidence could refute it"; if you cannot write that line, do not list it;
4. At the end, mark separately which questions have most likely already been asked in the literature, and what the clue is; mark "unsure" where you cannot give a clue.
Do not recommend a candidate. The pick is not yours.
```

Step 2, the three tests, model as juror. The scores (0/1/2) are the human's; the model attacks.

```text
Candidate question: [paste one candidate].

Attack it from three angles, the strongest single objection for each:
1. Testability: is there any evidence that could kill it? If not, point out where it is a position rather than a question;
2. Worth answering: assume the answer is "yes", then "no"; what changes in action? If nothing changes, say it is decoration;
3. Affordable: under these constraints ([paste constraints]), what is the most expensive step on the road to evidence?

Attack only, do not patch. Patching is not your job.
```

Step 3, rewrite it falsifiable. The human writes first; three versions only when stuck.

```text
Rewrite the candidate question below into a falsifiable hypothesis, strictly following the pattern:
"Under [conditions/basis], the [measurable metric] of [subject], compared with [control], is [direction and threshold].
If [specific observed outcome] is observed, the hypothesis is falsified."

Candidate question: [paste].

Requirements:
1. Give 3 versions, thresholds from strict to loose;
2. For each version, state which slot was hardest to fill and what you assumed to fill it; those assumptions get rechecked by hand;
3. Do not use words no observation can refute, such as "effectiveness", "possibility", "potential".
```

Step 4, action rehearsal. Item 3 matters most; middle outcomes expose holes.

```text
Hypothesis: [paste the falsifiable sentence].
Reader or decision maker: [yourself / a manager / an investment committee / a reviewer].

Rehearse:
1. If the answer is "yes", what does that decision maker do? How is it different from now?
2. If the answer is "no", what do they do? How is it different from now?
3. List 2 to 3 middle outcomes, neither yes nor no (partly holds, holds at extra cost, holds only on a subset),
   and for each check: does the falsification condition give a verdict? Where it is silent is a hole in the hypothesis.
If the actions in 1 and 2 are the same, say so plainly: this question changes no action.
```

Step 5, reality-check the resources. Whether the route is walkable is the human's ruling; accept only shrink suggestions that keep the question the same question.

```text
Hypothesis: [paste the falsifiable sentence].
Resources: [time] / [budget and compute] / [available data] / [the skill range of the human plus AI].

Give:
1. The shortest route from the hypothesis to the "specific observed outcome", step by step;
2. The biggest cost item at each step (time / money / difficulty of getting the data);
3. If the whole route exceeds the resources, 3 ways to shrink it (task scope / metric / control),
   and for each, whether the question is still the same question after shrinking.
```

## Leak self-check
- [ ] The direction line already names the answer you want? The twenty candidates will orbit it. State the direction, not the wished-for finding.
- [ ] Item 4 deleted because the marks were annoying? "Not seen" means unsure, not novel. Put it back.
- [ ] Step 2 asked to patch or to rank? Attack only; the ranking is the three-test score you give.
- [ ] The step 3 prompt fed your favourite version as a seed? Three fresh versions; recheck each assumption by hand.
- [ ] The survivor written into the card by the model? The card's sign-off reads "AI only supplied candidates and counterpoints". Fill it yourself.

## Before you dispatch
`python scripts/leak_check.py brief briefs/diverge-candidates.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/diverge-candidates.md, leak_check: clean
