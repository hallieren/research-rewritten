# Number tracing with the basis check
Kind: VERIFICATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

Trace every number to its original source through an independent channel, and check that the basis matches, not just the digits: comparison baseline, time window, units. A number that is right on a swapped basis is falsified, not confirmed. A number traced to a dead end is undecidable, and a dead end is a hard defect that moves the whole output up a layer. The channel is never told which number carries the conclusion.

## Prompt(s)

```text
You are the verifier. Below is a set of numerical claims. Trace each one to its source. I
will not name the document these numbers came from, and I will not say which number matters.
For each number output:
1 The most original source you can reach (paper table, data file, official statistics), with the specific location;
2 Basis check: the number's comparison baseline, time window, and units in the source, do they match how the claim uses it?
3 Verdict, one of three: confirmed / falsified (including the number is right but the basis was swapped) / undecidable (traced to a dead end).

Numerical claim list:
1 [the number and its claimed meaning]
2 [...]
```

## Leak self-check
- [ ] The brief names which number carries the conclusion, or what you hope it shows? Strip it; the claim and its stated meaning only.
- [ ] A summary table pasted instead of the numbers with their claimed meanings? The channel traces claims, not your recap. Give the claims.
- [ ] A number confirmed on the digits while the basis was swapped? That is falsified. The basis check is the point.
- [ ] A dead end logged as undecidable and then let through? Undecidable is not pass; a sourceless number is a hard defect.
- [ ] Ran in the session that produced the numbers? Void. A separate session or model.

## Before you dispatch
`python scripts/leak_check.py brief briefs/trace-numbers.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/trace-numbers.md, leak_check: clean
