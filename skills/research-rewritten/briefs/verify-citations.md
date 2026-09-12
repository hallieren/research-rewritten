# Citation extraction and check
Kind: VERIFICATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

Two prompts. The first breaks the output into a list of independently checkable claims, labeled citation, number, or reasoning. Before that list goes to the check channel, strip the concluding tone yourself; the check channel must not read which claim you want to hold. The second runs each citation through an independent channel with three questions: does it exist, does it say so, was it overturned. Every claim comes back confirmed, falsified, or undecidable, with a basis you can open; a confirmed with no openable basis is treated as undecidable.

## Prompt(s)

```text
Below is a document. Extract every checkable claim as a list, one per line, labeled by type:
- Citation: claims a source exists and says something
- Number: gives a specific number and its meaning
- Reasoning: a conclusion derived from the claims above
Requirements:
1 Rewrite each claim in neutral wording, stripping the rhetoric, emphasis, and concluding tone;
2 Note where the claim sits in the original (section, paragraph);
3 Do not judge whether a claim is true. Extract only.

Document:
[paste the full output]
```

```text
You are the verifier. Below is a set of claims. Check each one independently. I will not
name the document they came from, and I will not say which ones matter to the conclusion.
For each claim output:
1 Verdict, one of three: confirmed / falsified / undecidable;
2 Basis: the source you actually found (it must open, or point to a specific location in a specific paper);
3 For a citation claim, three questions: does the source exist? does it say what the claim says it says (read the original, watch for dropped qualifiers)? was it later overturned, corrected, or retracted (check forward citations)?
4 For falsified or undecidable: where exactly the gap between claim and evidence lies.
Forbidden: guessing a wanted answer from the wording or ordering of the claims;
Forbidden: leaning phrasing on any undecidable item;
Forbidden: middle-state wordings such as "basically correct" or "broadly credible".

Claim list:
1 [claim one]
2 [claim two]
```

## Leak self-check
- [ ] Handed the check channel the full output or a fragment instead of the neutral claim list? Context is a position. Extract first, then dispatch only the list.
- [ ] The claim list's ordering or wording hints at which items matter? Shuffle the order and reword neutrally.
- [ ] The brief says confirm, verify our findings, or support? Already leaked. Ask for a verdict from the three values.
- [ ] Extraction and check ran in the session that wrote the output? Void. A different session or model.
- [ ] A confirmed came back with no basis you can open? Treat it as undecidable, not as pass.

## Before you dispatch
`python scripts/leak_check.py brief briefs/verify-citations.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/verify-citations.md, leak_check: clean
