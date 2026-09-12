# Honest map

**How to use.** Start from the claims you cited or took as true in your most recent deliverable, ten rows at most (illustrative). Fill the claim and your gut status first, then the fourth column; a row whose fourth column cannot be filled drops to still exploring (nobody knows). Two disciplines before everything (rule): a demo is not production evidence, it only triggers an investigation; self-report is not measurement, it does not enter the evidence column. A row's status is decided by its highest evidence level; E4 or E5 alone drops the row to still exploring. The model runs the fifth column's searches and proposes date changes; every status change passes through a human; ten rows all verified is a placebo, not a map.

```text
STATUS: DRAFT, not for the decision chain
# Honest map   Owner: ____________   Date: ________

| # | Claim (one sentence that can die, qualifiers kept) | Status (verified / still exploring: evidence accumulating or nobody knows / falsified) | Key evidence (identifiable sources, E-level each) | What evidence would change it (a search instruction, "on seeing X, change to Y", up and down) | Last reviewed (YYYY-MM) |
|---|---|---|---|---|---|
| 1 | ____________ | ________ | ____________ | ____________ | ______ |
| 2 | ____________ | ________ | ____________ | ____________ | ______ |

Status rules (rule)
verified, all three at once: production-grade evidence (not a demo or case write-up); independent sources ≥ 2, or reproduced by your own hands; the fourth column is not empty. Missing any one → still exploring.
still exploring: the default when neither end is reachable; grade it evidence accumulating (direction shows, volume does not) or nobody knows (not even a direction).
falsified, either one: a criterion written in advance was triggered; a reproducible counterexample punched through the claim as stated. Punching through the unconditional form does not punch through the weak form; the surviving weak form gets its own row. Falsified rows stay, with date and evidence; tombstones are part of the map's credit.

| Level | Form of evidence | What it can support |
|---|---|---|
| E1 | Controlled measurement against preregistered criteria; independent replication | verified or falsified |
| E2 | One peer-reviewed study or systematic evaluation | A direction; alone not enough for verified |
| E3 | Production practice many users can reproduce | verified for workflow-type claims |
| E4 | Demos, case write-ups, vendor material | Triggers an investigation only |
| E5 | Hearsay, intuition, self-report | Does not enter the evidence column |

Review cadence (illustrative): verified every 6 months or at once on a field-level event; evidence accumulating every 3 months; nobody knows event-driven plus one scan every 6 months; falsified never, tombstone kept; pending backfill when the preregistered experiment reports.
Review moves (rule): change the status (evidence arrived) / change the evidence (a harder source replaced it) / change the date (checked, nothing moved). Even when only the date changes, it changes. One log line per review: date, rows moved, why.
Rows where holding is good for me (evidence bar up one notch): ____________

ruling: status per row, as written in the table | signed by: UNSIGNED
answers when wrong: NOBODY | <person's name>
Signature: ____________ (must be a human)
```

### Self-check
- [ ] A row that cannot be written as a sentence that can die? Delete or rewrite it; "X has a lot of promise" becomes "X beats [baseline] on [setting]".
- [ ] A fourth column empty? The row drops to nobody knows. Write the search instruction.
- [ ] Every row verified? That is a placebo. Re-derive two statuses by hand.
- [ ] A status copied from someone else's map? Copy structure only. Re-derive or spot-check the status yourself.
- [ ] Review dates unchanged since the last review? A map whose dates do not move is dead. Change the date even when nothing moved.

Filled in → goes to: templates/ladder-self-rating.md
