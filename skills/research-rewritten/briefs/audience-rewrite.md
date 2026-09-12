# Audience rewrite brief
Kind: GENERATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

Drafting and rewriting are handed off; claim strength is not. The prompt carries the signed templates/claims-list.md with tier and signature per row, so the channel has no strength to invent. Two vehicles come out of the same list: templates/technical-report-skeleton.md for "how do you know", templates/one-page-memo.md for "what should I do". After the draft, the human reconciles strength sentence by sentence and marks every wording stronger than the list; then briefs/interlock-check.md runs in a separate session.

## Prompt(s)

```text
Below is a claims list. Each row carries the claim, the evidence pointer, the tier, and the signature status:
[paste the claims list, every column]

Rewrite it as a [technical-report skeleton / one-page memo] for an audience of [technical committee / peer review / decision maker / ____],
whose core question is ["how do you know" / "what should I do"].

Hard constraints:
1 Do not change the strength of any claim: "undecided" may not become "matched", "looks like" may not become "shows",
  and post-hoc labels may not be dropped;
2 Do not merge two claims into one stronger sentence;
3 Keep the evidence pointer after every number (they become citations or footnotes in the final draft);
4 Not one claim outside the list may appear; the outstanding row appears as a limitation;
5 Type no number from memory; every number is copied from the pointer's file.

At the end, list every sentence where you were unsure whether the wording matches the tier; the human rules on each.
```

## Leak self-check
- [ ] Tier and signature columns left out of the paste? With no strength information the model invents strength, always upward. Paste every column.
- [ ] A claim added in the prompt that is not on the list? Back to the list; sign it there first or drop it.
- [ ] The prompt asks for "compelling" or "persuasive"? Delete the adjective; the audience question is the only steer.
- [ ] The draft polished afterward and the interlock not rerun? Any operation that touches the text voids the last check. Rerun briefs/interlock-check.md.

## Before you dispatch
`python scripts/leak_check.py brief briefs/audience-rewrite.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/audience-rewrite.md, leak_check: clean
