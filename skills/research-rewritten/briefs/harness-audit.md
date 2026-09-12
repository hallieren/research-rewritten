# Harness audit brief
Kind: VERIFICATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

Hand the harness's core code to a session that did not help write it. The session that wrote it is blind to its own assumptions; changing the session changes the viewpoint. Feed the world's side too (API docs, real data samples); code alone audits only the world you defined. The output is a list of leads, each with a minimal verification experiment; the human rules after running them one by one. Use it before the pilot, so the expensive bugs die before the money is spent. An empty audit is not a safety certificate; templates/harness-checklist.md still runs.

## Prompt(s)

```text
This is the core code of an experiment harness:

[paste: model or service calls, answer extraction, scoring, writing to disk, the ledger module]

This is the test plan it has to implement (the criteria part):

[paste: the arm design, the basis, and the criteria of the plan]

Your job is to find the ways this harness quietly produces wrong numbers,
not to improve its code style. Work through four seams one by one:

1 The code/API seam. For each model or service, check the code's assumptions against its real API contract:
  parameter names and values that get refused (a reasoning model refusing a custom temperature), truncation behavior,
  null or empty returns, non-JSON responses, rate limits and retries.
2 The scorer/data seam. Pull 10 real samples from the task data and walk the scoring logic by hand.
  Do format variants (units, % suffixes, thousands commas, capitalization, multiple lines) score a correct answer wrong?
  Is the tidiest way of writing a correct answer exactly the parser's most fragile path?
3 The grader/environment seam. The libraries, subprocesses, and timeouts the grading depends on: do they install fully
  and run in a clean environment? When a dependency is missing, does it error, or quietly record 0?
4 The harness/criteria seam. Compare the basis the code implements against the basis the plan locked in, item by item:
  sample size, slices, seeds, repeat counts, cost formula. Where do they quietly disagree?

For each finding, output three parts:
the seam's location → the worst consequence (which arm or configuration's numbers get contaminated first, and in which direction)
→ one minimal experiment that verifies it on the spot (one command or one sample).
Tag each finding: confirmed (reproduced on the paste) / undecidable (needs the live environment).

Rules: attack only; do not judge whether the harness as a whole is sound; a finding without a minimal experiment is not accepted;
if a seam turns up nothing, write "nothing found on this seam", do not pad.
Finally: if only one 20-problem pilot is allowed, which three numbers are most worth checking by hand, and why those?
```

## Leak self-check
- [ ] The paste names which arm the author built or expects to win? Strip it; arms by letter or role.
- [ ] Code only, no API docs and no real data samples? The expensive bugs live on the seam between code and world. Attach both.
- [ ] Audit session is the writing session? It will defend its own assumptions. Change the session, and the model if you can.
- [ ] A finding fixed in code without a change-log entry? A fix that touches a plan-versus-reality difference goes into the log; the locked criteria do not move.
- [ ] A finding accepted without running its minimal experiment? An audit produces false positives. Run each one.

## Before you dispatch
`python scripts/leak_check.py brief briefs/harness-audit.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/harness-audit.md, leak_check: clean
