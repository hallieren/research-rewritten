# Confounder checklist

**How to use.** Run it line by line while filling item 6 of templates/test-plan.md. The goal is honest disposition, not a full row of ticks: tick what clears; for what does not, write a mitigation or write it into the limitations. An all-green checklist is itself suspect. The model may run the plan against the list first (breadth is its strong suit); the final mark on every line is yours.

```text
Plan: ____________   Run by: ____________   Date: ____________
Mark each line: clears / mitigation: ______ / limitation: ______

A Baseline fairness
☐ A1 The baseline got a tuning or prompt-optimization budget equal to the main arm
☐ A2 The baseline is the strong form of its method, not a straw man (defaults, outdated version, an obviously suboptimal setting)
☐ A3 A baseline number taken from someone else's paper has a comparable environment and data slice, or gets rerun

B Budget and basis alignment
☐ B1 Resources consumed by both sides (money / compute / calls / person-hours) are measured on the same basis
☐ B2 The definition of "same budget" is locked (otherwise alignment is a degree of freedom to fiddle with afterward)
☐ B3 Primary and sensitivity basis listed separately, with the commitment to report both

C Alternative explanations
☐ C1 At least three cheap explanations that explain the same result without the hypothesis are listed
☐ C2 Every cheap explanation points at an arm or a step built to rule it out
☐ C3 The cheapest explanation of all has an arm of its own (a two-arm design cannot tell "the mechanism works" from "spending works" until an equal-budget arm without the mechanism is added)

D Data contamination
☐ D1 Evaluation data the system could have seen in training is treated as seen by default (public benchmarks, public surveys, question banks online)
☐ D2 Data the development process saw is named (the same validation set looked at repeatedly while tuning is human overfitting)
☐ D3 The contamination check is a step written into the plan, not the line "should be fine"

E Criteria backdoors
☐ E1 The metric is unique and set beforehand (several metrics equals picking the metric afterward)
☐ E2 The data slice is set beforehand ("significant on some subset" counts only when that subset was declared in advance)
☐ E3 The outlier exclusion rule is set beforehand
☐ E4 The stopping rule is set beforehand

F The measurement itself
☐ F1 Scoring and judging cannot favor one arm (rule: an LLM judge whose preference becomes a second research question is excluded)
☐ F2 A human judging stage is blind to which arm a sample came from, wherever blinding is possible

Lines that did not clear, copied to item 6 of the plan: ____________
Signature: ____________ (must be a human)
```

### Self-check
- [ ] Every line ticked green? An all-green list is the suspect one. Reread A1, C3, and E1 with the opponent's sentence in hand.
- [ ] A line marked "mitigation" with no mitigation named? Name the arm or step, or move the line to limitations.
- [ ] C3 cleared with only two arms? It cannot be. Add the equal-budget arm or write the limitation.
- [ ] The model's ticks accepted as final? Breadth is its strength, the mark is yours. Re-mark every line by hand.

Filled in → goes to: templates/harness-checklist.md
