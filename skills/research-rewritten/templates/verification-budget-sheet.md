# Verification budget sheet

**How to use.** One page that assigns a layer, row by row, to the project's outputs for the next month. The layer follows destination, cost of being wrong, and probability of being wrong, never how good the output looks. Probability of being wrong comes from templates/failure-mode-census.md. Name the verification channel specifically and separately from the generating side; an unnamed channel takes the easy road and becomes the same one. Review monthly; when a destination changes, the layer changes with it.

```text
# Verification budget sheet
Project: ____________   Owner: ____________   Date filled: ____________   Next review: ____________

| Output | Destination (own desk / team / decision chain / public) | Cost of being wrong | Probability of being wrong (error class from the census) | Layer | Verification channel (which model or person, which brief; not the generator) | Escalation trigger | Last checked |
|---|---|---|---|---|---|---|---|
| ______ | ____ | high / medium / low | high / medium / low: ______ | L_ | ______ | ______ | ______ |
| ______ | ____ | high / medium / low | high / medium / low: ______ | L_ | ______ | ______ | ______ |
| ______ | ____ | high / medium / low | high / medium / low: ______ | L_ | ______ | ______ | ______ |

Table-wide escalation rules (locked, no bargaining on the spot; rule):
- A spot check finds a hard defect (fabricated citation / sourceless number) → the whole output moves up one layer
- The destination escalates (an internal draft gets cited in a decision document) → reassign by the new destination
- A conclusion gets cited by a bigger decision → that conclusion is named L2 on its own
Layer quick reference: templates/verification-workflow-card.md
Signature: ____________ (must be a human)
```

### Self-check
- [ ] Whole sheet L0? Either nothing dares enter the decision chain or you are exempting yourself. Ask where each output goes.
- [ ] Whole sheet L2? The speed dividend has been handed back. Layering is pricing; all L2 is a pricing failure. Reassign by destination.
- [ ] Channel column says "AI"? Which model, which brief, and is it the generator. Name it.
- [ ] Escalation trigger says "depends"? That is a backdoor for your future self. Write the rule.
- [ ] A layer set because last time was good quality? The layer follows destination and cost, not impressions. Reassign.

Filled in → goes to: templates/verification-workflow-card.md
