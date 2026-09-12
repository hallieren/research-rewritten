# One-page memo

**How to use.** Audience: decision makers; their question is "what should I do". Three hard constraints (rule): one page; conclusion on top; risks right behind the conclusion, not at the foot, nobody reads the foot. Generate only from the signed templates/claims-list.md with briefs/audience-rewrite.md, strength locked. Every number shares its source with templates/technical-report-skeleton.md. Never invent a recipient or a submission.

```text
STATUS: DRAFT, not for the decision chain
To: ________   From: ________   Date: ________
Subject: ____________ (the decision question, not the project name)

Conclusion (one sentence, verbatim from the strongest signed claim in the list):
____________________________________________

Risks (three lines, each one caveat that could change the decision; read before the table)
1 Extrapolation boundary (what was measured, what was not): ____________
2 Mechanism caveat (what the control arm or the audit said that hurts): ____________
3 Basis caveat (known gaps in the cost or data basis): ____________

Numbers (at most five rows; every cell quoted from the results file)
| Scenario | Reading | Cost | Judgment (has a shot / no shot / evidence void) |
|---|---|---|---|
| ____ | <value> [<lo>, <hi>] | ____ | ________ |

Recommended next step (one, executable, with configuration and budget; a pilot names its criteria and threshold before it runs):
____________________________________________

Basis (one line): repo ________, preregistration ________, total cost ________
verification level note: <tier>; checked: <list>; not checked: <list>; reason: <the real constraint>
Signature test run sentence by sentence: ____________ (must be a human)
```

Machine check: `python scripts/interlock.py <this memo> <the report> --results <results file>` before it is sent; every MISMATCH and NOT FOUND line is read by a human.

### Self-check
- [ ] "May" or "to some extent" in the one-sentence conclusion? Rewrite to a strength you dare sign, or admit the evidence is not enough and do not deliver.
- [ ] A risk line that is boilerplate ("limited sample size")? A risk line that cannot change the decision is decoration. Make it specific.
- [ ] Judgment column all "has a shot"? Check the list for the unfavourable conclusions. "No shot" and "evidence void" save the most money.
- [ ] Numbers not checked against the report? Run the interlock before sending.

Filled in → goes to: templates/red-team-dispatch-brief.md
