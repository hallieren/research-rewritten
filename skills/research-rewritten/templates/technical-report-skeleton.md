# Technical report skeleton

**How to use.** Audience: peers and the technical committee; their question is "how do you know". Generate it only from the signed templates/claims-list.md with briefs/audience-rewrite.md, strength locked. Method and statistics in full; limitations written for real, each item carrying numbers, no camouflage wording. Skeleton first: get the five parts standing, then expand into prose. After any polishing, rerun the strength reconciliation and the interlock.

```text
STATUS: DRAFT, not for the decision chain
Title (the main conclusion with its qualifier, e.g. "task-dependent"; the sentence most often quoted alone): ____________

Abstract (six sentences)
1 The problem and the dispute: ____________
2 Method and preregistration (criteria before results): ____________
3 Main result (preregistered numbers as is): ____________
4 Any overturn or breakdown (labeled post-hoc): ____________
5 What the control arm said about the mechanism: ____________
6 Openness (repo / preregistration / ledger public): ____________

1 Problem and related work: 2 to 3 papers per camp (illustrative); where this work stands, narrowed to what the list dares sign
2 Method: hypothesis and criteria with falsification conditions / tasks and data / arm design / cost basis / statistics
3 Results: main table → preregistered reading → post-hoc breakdown (own subsection, labeled post-hoc) → criteria reconciliation
4 Limitations (each item with numbers)
  Data composition: ____________
  Identity of every post-hoc analysis: ____________
  Weaknesses in reading and statistics (effective n, independence): ____________
  Bases promised and not delivered (the outstanding row): ____________
  External validity (model / point in time / contamination): ____________
  Broken premises (from templates/five-premise-table.md), if any: ____________
5 Reproducibility: repo / preregistration commit / ledger / audit script

Every number quoted from the results file, pointer kept after it (rule: no number typed by hand)
Wordings stronger than the claims list, marked for the human: ____________
verification level note: <tier>; checked: <list>; not checked: <list>; reason: <the real constraint>
Signature test run sentence by sentence: ____________ (must be a human)
```

Machine check: `python scripts/interlock.py <this report> <the memo> --results <results file>`; a human reads every MISMATCH and NOT FOUND line; the channel in briefs/interlock-check.md reads what each number claims to mean in context.

### Self-check
- [ ] Title dares more than the abstract? Run the strictest signature test on the title; it travels alone.
- [ ] A weakness admitted in limitations still a selling point in the abstract? Downgrade consistently across the whole document.
- [ ] Post-hoc numbers inside the preregistered subsection? Separate sections, labeled, side by side, nothing replaced.
- [ ] The outstanding row missing from limitations? Every outstanding row has a matching limitation. Add it.
- [ ] "Clearly", "robustly", "significantly" with no number behind it? Delete the adverb or attach the number.

Filled in → goes to: templates/red-team-dispatch-brief.md
