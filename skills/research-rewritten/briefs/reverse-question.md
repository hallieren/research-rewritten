# The L0 reverse question
Kind: VERIFICATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

The cheapest scout, for an output that stays on your desk. It does not rule; it points at the soft spots so you know where the one number or the one claim to check by hand is. Run it in a separate session; the material goes over with no hint of which claim you are attached to. What it names, you then trace to origin or to a dead end. A dead end moves the whole output up a layer.

## Prompt(s)

```text
Below is a piece of research material. Your task is not to summarize it but to find its soft spots:
1 Which three claims here have the weakest evidence? Why?
2 Which one number would you most want to see the source for?
3 If you could check only one claim, which one?
No need to verify, only to point. No pleasantries, and no praising before criticizing.

Material:
[paste the output]
```

## Leak self-check
- [ ] The material carries your framing, your hope, or the claim you are attached to? Strip it; the material only.
- [ ] Asked it to confirm the material instead of finding soft spots? This prompt points, it does not vouch. Ask for the weak spots.
- [ ] Ran it in the session that wrote the material? Void. A separate session.
- [ ] It opened by praising the work before criticizing? Sycophancy. Rerun with the no-pleasantries line intact.
- [ ] Named a soft spot and then left it unchecked? Pointing is not checking; trace it to origin or a dead end.

## Before you dispatch
`python scripts/leak_check.py brief briefs/reverse-question.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/reverse-question.md, leak_check: clean
