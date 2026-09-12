# Plan red-team brief
Kind: VERIFICATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

Use it the moment the plan looks final and is not yet signed; the earlier the beating, the cheaper. What gets red-teamed here is a plan that has not run; red-teaming conclusions is briefs/redteam-scorer.md and its siblings. The output is a draft list, not a ruling: each line the human adopts becomes a change to the plan, each line rejected gets one line of reason on file. An empty output is not evidence the plan is solid; templates/confounder-checklist.md still runs.

## Prompt(s)

```text
This is a test plan:

[paste the full plan: arm design, basis, criteria; nothing about who wrote it or which result is wanted]

Your job is to overturn it, not to improve it. Assume you are the reviewer
who least wants this conclusion to hold.

1 List every degree of freedom in the plan that can still be moved after the results are in;
2 For each one, say which conclusion it would favor if adjusted after the fact;
3 Give one cheapest alternative explanation that, with the arm design unchanged, would produce the same result;
4 Point out which criterion's wording leaves a backdoor (words like "as appropriate", "a reasonable range", "at discretion");
5 Check the baseline arm: is it the steelman of that comparison method? Where does it look like a straw man?
6 If you were to add one arm built to make trouble for this conclusion, which arm would you add and why?

Rules: raise only problems specific enough to act on, no general methodology advice.
Output each one in three parts: the problem → who it favors → how to fix it.
Tag each problem: confirmed (quote the plan line that leaves it open) / undecidable (the plan text does not settle it).
If an item turns up nothing, write "nothing found on this item"; do not pad.
```

## Leak self-check
- [ ] The paste includes the motivation, the sponsor, or the result the author expects? Strip it; the plan text only.
- [ ] The prompt says which arm is the author's own? Arms are named by letter or role. Rename.
- [ ] Only the lines that were easy to hear got adopted? The ones that irritate deserve the closest look. Write a reason before rejecting any line.
- [ ] One round only? Feed the fixed plan another round until a new round returns only old lines you deliberately rejected.
- [ ] A criteria change after the red team not logged? Legitimate at this moment, and still a change-log entry with "after results seen: no".

## Before you dispatch
`python scripts/leak_check.py brief briefs/plan-red-team.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/plan-red-team.md, leak_check: clean
