# Interlock check brief
Kind: VERIFICATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

Run `python scripts/interlock.py <report> <memo> --results <results file>` first. The script traces every number in both documents to the results file and lists unquantified superlatives; it does not judge importance. Hand the channel the script's MISMATCH and NOT FOUND lines plus both documents; the channel's job is what each number claims to mean in context (basis, window, units, which arm), the part a string match cannot see. The human rules on every disagreement. No number is typed by hand to close a gap: recompute from the results file, or delete the sentence.

## Prompt(s)

```text
Here are two documents, one results file, and a script report: [technical-report skeleton] [memo] [results file or table] [interlock report lines].
Do factual checking only. Do not evaluate the conclusions.

1 Extract every number appearing in the two documents (body text, tables, titles) into a list:
  the number, where it appears, and what it claims to mean in context (basis, comparison baseline, time window, units, which arm);
2 For each number, look for its counterpart in the results file and mark it:
  confirmed (matches, same meaning) / falsified (does not match, or the number matches but the meaning in context does not; list both values) /
  undecidable (not found in the results file);
3 For each MISMATCH and NOT FOUND line in the script report, state what the document's number claims to mean and which results-file field, if any, carries that meaning;
4 Cross-compare the numbers for the same fact between the two documents and list every disagreement;
5 List every comparative or superlative in the documents with no number behind it ("faster", "strongest", "substantially").

Forbidden: judging whether a disagreement matters; that is not your job.
Forbidden: proposing a corrected number; report the gap only.
```

## Leak self-check
- [ ] The check ran in the session that wrote the draft? The same session protects its own draft. Separate session.
- [ ] The prompt says which document is the master or which number is load-bearing? Delete it; the channel reads both as strangers.
- [ ] The script report attached without both documents? The channel needs the context around each number. Attach both.
- [ ] A number filled in by hand where the report said not found? Recompute from the results file or delete the sentence.
- [ ] Polished after the check? The check is void. Rerun the script and re-dispatch.

## Before you dispatch
`python scripts/leak_check.py brief briefs/interlock-check.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/interlock-check.md, leak_check: clean
