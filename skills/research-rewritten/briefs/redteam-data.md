# Red-team order: data composition
Kind: VERIFICATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

One of four attack orders, run only after the deliverable is compressed into a neutral claims list. This order attacks the samples, the problems, and the corpus. One surface, one fresh session, the model switched from the writing channel. The output is charges, each with a charge, its consequence, and a same-day executable check; a charge with no check is not accepted. "Nothing found on this surface" counts only when a second model returns the same. The whole-conclusion ruling and the tier are the human's, in templates/disposition-record.md.

## Prompt(s)

```text
Role: you are hired to attack the claims list below, on this attack surface:
Attack surface: the samples, the problems, the corpus itself (source, draw, structure, coverage, contamination).
Check first:
1 the structure brought in by the draw (first N rows, a single batch, a single source, a convenience sample);
2 how many molds the samples really have: after stripping proper nouns and numbers, how many literal templates remain and what share each holds;
3 whether the test material could sit inside the training corpus of the system under test (public question banks, famous datasets, material from before the corpus cutoff date);
4 whether the data coverage holds up the wording of the claim, whether "holds on the X slice" got written as "holds".
Input: the claims list and the materials named in the dispatch brief (paths and originals, not a summary).
Output: a list of charges ordered by lethality; every charge carries three things:
1 Charge: which point of this surface could make one of the claims fail (name the claim number);
2 Consequence: if the charge holds, which claim dies, and the direction and rough size of the effect it manufactures;
3 Check: one check executable the same day (a script sketch, a sampling plan, a replay experiment, a recompute on another basis) whose result can confirm or rule out the charge.
Rules: attack only, no balanced coverage; do not rule on whether the conclusion as a whole holds; do not list a charge you cannot pair with an executable check; if you find nothing, write "nothing found on this surface" and do not pad.
```

## Leak self-check
- [ ] The brief names which arm you built, which direction you want, or what you hope to announce? Delete it; claims by neutral wording, materials by path.
- [ ] A claim carries an adjective (significantly, robustly, surprisingly)? Rewrite it as a neutral statement of fact.
- [ ] You merged this surface with the other three into one order? Split them; a merged order gets filled with the softest surface.
- [ ] Dispatched from the session or model that wrote the conclusion? Switch. Context is a position.
- [ ] The charges come back praising you ("the design is rigorous, only minor issues")? Expectations leaked; return to the dispatch brief and strip it.

## Before you dispatch
`python scripts/leak_check.py brief briefs/redteam-data.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/redteam-data.md, leak_check: clean
