# Interrogation dispatch brief
Kind: VERIFICATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

The independent channel for the mechanical work of a result interrogation: pull originals, find patterns, cluster templates, spread the effect by slice. The brief carries no expectation and no "help me check whether this is real". The channel is a juror, not a judge; it never answers "is this credible". Messy versus tidy wrongness, effective n, and whether concentration matters are the human's rulings, entered in templates/result-interrogation-record.md. The `N:` line from `python scripts/effective_n.py count` is pasted into the record, not into this brief; the channel counts molds on its own.

## Prompt(s)

```text
These are the raw per-problem results of an experiment (data file path attached: [path]).
Do factual organization only. Make no evaluation of whether the result is credible.

1 List every sample scored wrong for [arm X]: sample id, the model's raw answer, the gold answer,
  and the numerical or literal relation between the two, ordered by id;
2 Summarize patterns in the wrong samples: numerical relation (such as always k times), format features,
  id distribution (whether concentrated in a continuous stretch);
3 Cluster the problem text of all samples by template: after removing proper nouns and numbers, how many
  literal templates remain, and how many problems in each;
4 Output a per-problem table of [arm A] − [arm B] differences, and mark the stretches of samples where the difference concentrates;
5 For [arm B] on the same stretches: does it show an anomaly in the same direction?

For each item report: confirmed (the pattern is in the file, with the ids) / falsified (looked for, not present) / undecidable (the file does not carry the field).
Forbidden: any ruling that the overall conclusion is reliable or unreliable; that is not your job.
Forbidden: "messy" or "tidy" as a verdict; report the pattern and the ids only.
```

## Leak self-check
- [ ] The brief says which arm you built, which direction you expect, or what you want to announce? Delete it; arms by letter, file path only.
- [ ] "Help me check whether this is real" anywhere? That hands the judge's seat to sycophancy. Factual organization only.
- [ ] A summary attached instead of the raw file? The channel cannot cluster a summary. Attach the per-problem file.
- [ ] The `N:` line or the announcement sentence pasted in? Both stay in the record. The channel counts molds without seeing your count.
- [ ] Dispatched from the session that ran the experiment? Void. Fresh session, this file as the only payload.

## Before you dispatch
`python scripts/leak_check.py brief briefs/interrogation-dispatch.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/interrogation-dispatch.md, leak_check: clean
