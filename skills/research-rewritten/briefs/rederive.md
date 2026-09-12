# Independent re-derivation from raw materials
Kind: VERIFICATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

The L2 check, and the most leak-prone brief in the set: a second channel gets only the raw materials and the question, never the conclusion, and derives from scratch. Converges with the original, and it becomes machine evidence; diverges, and each point of disagreement is ruled by hand, fixing the output or entering the limitations. No residue of the original may ride along: not its wording, not its structure, not its subheadings or figure captions. Reorganize the materials; never clip the first half of the output. With no raw materials, this check is not possible; use the four red-team orders as the acceptance checklist instead.

## Prompt(s)

```text
Below is a batch of raw materials and one research question. Working from these materials
and only these, derive your own conclusion independently.
Research question: [the question itself, with no leaning wording]
Requirements:
1 Give your conclusion and the full reasoning chain from the materials to it;
2 For each link, note which part of which material it rests on;
3 Where the materials cannot support a judgment, write "insufficient material" and do not fill the gap with common knowledge;
4 At the end, list separately the two or three premises the conclusion leans on most, and how the conclusion changes if each is wrong.

Raw materials:
[raw materials only; no part of the original output, including its subheadings, figure captions, or paragraph structure]
```

## Leak self-check
- [ ] The materials picked up structural residue of the original (subheadings, figure captions, wording from the conclusion)? Reorganize and dispatch again.
- [ ] You clipped the first half of the output as the materials? That carries the conclusion's framing. Rebuild the materials from sources.
- [ ] The research question is worded to lean one way? Strip the lean; the bare question.
- [ ] Ran the re-derivation in the generating session? Void. A different session or model.
- [ ] Converged, so it was recorded as evidence without checking the chain? Read the reasoning chain; convergence on a wrong path is not evidence.

## Before you dispatch
`python scripts/leak_check.py brief briefs/rederive.md --original <the output being examined>`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/rederive.md, leak_check: clean
