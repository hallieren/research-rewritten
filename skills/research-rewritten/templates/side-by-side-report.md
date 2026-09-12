# Side-by-side report

**How to use.** Deliver the numbers of any test with locked criteria in this table, no exceptions. Three rules, all hard: the preregistered numbers are reported as is however much you dislike them; post-hoc breakdowns stand beside them, each labeled post-hoc with the reason for the breakdown; a post-hoc number never replaces a preregistered one. A post-hoc number that wants promotion gets preregistered and retested next round. A falsification condition not triggered does not mean the hypothesis holds.

```text
STATUS: DRAFT, not for the decision chain
# Result report: ____________ (project / experiment)
Preregistration file and timestamp: ____________   Results file and commit: ____________
Audit or breakdown script (with commit): ____________

| Basis | Preregistered result (as is) | Post-hoc breakdown (labeled post-hoc) | Reason for breakdown |
|---|---|---|---|
| <arm A vs arm B, task family X> | <value> [<lo>, <hi>], tie / undecided / lost | post-hoc: after removing <the defective subset>, <value> [<lo>, <hi>], direction same / reversed | <every wrong answer of one arm traced to one ambiguous template with two defensible readings> |
| ____ | ____________ | ____________ | ________ |

## Criteria reconciliation (walk the locked win / lose / undecided conditions one by one)
Falsification condition 1: ____________ → triggered / not triggered
Falsification condition 2: ____________ → triggered / not triggered
Per family against the threshold (rule: three values only):  ____: tie / undecided / lost   ____: tie / undecided / lost

## Known statistical weaknesses
Effective sample size: n=<rows>, <k> independent units (basis: ____________)
CI independence assumption: holds / broken (clustered interval: [<lo>, <hi>])
Sensitivity basis result (reported even when it disagrees with the primary): ____________

## Change log pointer
Every post-hoc analysis in this report is registered at: ____________ (date + entry, "after results seen: yes")

ruling: falsified / not falsified but not holding across the board (qualifier: ______) / holds | signed by: UNSIGNED
answers when wrong: NOBODY | <person's name>
verification channel: SAME-CHANNEL (void) | separate session, <model or person>, brief: briefs/<file>, leak_check: clean
criteria timestamp: before results | after results | none
Signature: ____________ (must be a human)
```

### Self-check
- [ ] Numbers only in the post-hoc column with "see above" in the preregistered column? Both columns, same table, same row. Fill the preregistered cell.
- [ ] A post-hoc cell with no reason? Without a reason it is indistinguishable from picking data. Write the mechanism.
- [ ] "Not falsified" written as "holds"? Not triggered is not holding. Pick the middle value and write its qualifier.
- [ ] The sensitivity basis or the unfavourable account left out? The commitment was both, no picking. Add the row.
- [ ] A breakdown missing from the change log? Post-hoc is allowed; unrecorded post-hoc is not. Register it.

Filled in → goes to: templates/claims-list.md
