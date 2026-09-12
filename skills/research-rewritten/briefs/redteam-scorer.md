# Red-team order: the scorer and the criteria
Kind: VERIFICATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

One of four attack orders, run only after the deliverable is final and compressed into a neutral claims list. This order attacks how right and wrong get judged. One surface, one fresh session, the model switched from the writing channel. The output is a list of charges, each with a charge, its consequence, and a same-day executable check; a charge with no check is a comment and is not accepted. "Nothing found on this surface" counts only when a second model returns the same. This channel never rules on whether the conclusion as a whole holds; that ruling and the tier go in templates/disposition-record.md.

## Prompt(s)

```text
Role: you are hired to attack the claims list below, on this attack surface:
Attack surface: how right and wrong, success and failure, get judged (gold answers, scoring scripts, human annotation rules, an LLM judge, the operational definition of valid or successful).
Check first:
1 whether the definition of right has a second defensible reading (ambiguous gold, ambiguous problem text);
2 the links in the parse, match, score chain that silently swallow points or hand them out (format suffixes, units, null, timeouts, partial matches);
3 tidy patterns in the wrong answers: always k times, always off by a constant, always one format, clustered in a continuous id stretch (tidiness is the fingerprint of a sick scorer or sick gold);
4 whether the conclusion flips under an equally reasonable alternative scorer or annotator.
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
`python scripts/leak_check.py brief briefs/redteam-scorer.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/redteam-scorer.md, leak_check: clean
