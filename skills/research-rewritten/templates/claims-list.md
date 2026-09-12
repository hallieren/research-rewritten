# Claims list

**How to use.** Step 1 of delivery, before any prose. Write every claim in the strongest form you dare sign: so weak that signing costs nothing is cowardice, so strong that it crosses the line is drift. Every sentence in both vehicles is generated from this table; no downstream document edits it backward, and polishing never strengthens it (rule). "Not done" is a row too: a basis promised and not executed, an arm that got cut. The model builds the table and proposes pointers; it never writes the claim text, picks the strength, or fills the signature.

> The order of use is fixed. templates/claims-list.md → templates/technical-report-skeleton.md / templates/one-page-memo.md → templates/red-team-dispatch-brief.md → templates/disposition-record.md.

```text
STATUS: DRAFT, not for the decision chain
# Claims list: ____________ (project)   Date: ________
Master source of evidence (repo / results file / commit): ____________

| # | Claim (one sentence, the strongest form dared) | Evidence pointer (file / table / commit) | Tier (verified / still exploring / falsified / outstanding) | Signature (dare / do not dare) |
|---|---|---|---|---|
| 1 | ______________________ | ____________ | ________ | ____ |
| 2 | ______________________ | ____________ | ________ | ____ |
| 3 | ______________________ | ____________ | ________ | ____ |
| Outstanding | Promised but not executed: ________ | Where promised: ____ | outstanding | I dare sign "not done" |

Preregistered numbers and post-hoc breakdowns in separate rows, the post-hoc row labeled post-hoc: ☐ checked
ruling: dare / do not dare (per row, in the table) | signed by: UNSIGNED
answers when wrong: NOBODY | <person's name>
criteria timestamp: before results | after results | none
Signature: ____________ (must be a human)
```

### Self-check
- [ ] A claim with no pointer? It does not enter the list. Get the evidence or downgrade to still exploring.
- [ ] A preregistered number and a post-hoc breakdown in one row? Split them; the post-hoc row carries its label.
- [ ] Outstanding row empty? Check every basis and arm signed in the plan. Only a fully delivered plan earns an empty row.
- [ ] Every claim in its weakest form? Evidence bought with real money is being wasted. Push each up a tier until one more notch would stop you signing.
- [ ] The tier or signature column filled by the model? Blank them. Those two columns are human handwriting.

Filled in → goes to: templates/technical-report-skeleton.md (peers, "how do you know") or templates/one-page-memo.md (decision makers, "what should I do")
