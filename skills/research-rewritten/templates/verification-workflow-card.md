# Verification workflow card

**How to use.** Assign the layer by destination and the most likely error class, never by how reliable the output looks; state it as `acceptance layer: L<n>`. Run the layer's checklist through independent channels only; a check in the generating session is void (rule). Neither the generating side nor the checking side picks the sample; `scripts/leak_check.py sample` does. The human reads two columns only, undecidable and falsified; undecidable is not pass and nothing turns green quietly (rule). Short on time, go to templates/downgrade-note.md: cut layers whole, keep the order.

| Layer | Trigger | Scope | Time (illustrative) | Required item |
|---|---|---|---|---|
| L0 spot check | The output stays on your desk | A sample | 15 to 30 minutes | A random sampling rule, locked first |
| L1 full verification | The output enters the decision chain: money, people, or conclusions rest on it | Every citation, every number, the reasoning chain | Half a day to a day, mostly AI time | The claim-to-source table filed with date and channel |
| L2 adversarial recompute | One conclusion being wrong triggers a hard-to-reverse action | The named load-bearing conclusions | One to several days per conclusion | Independent re-derivation plus red team |

```text
STATUS: DRAFT, not for the decision chain
Output: ____________   Date: ____________   Destination: own desk / team / decision chain / public
Most likely error class: fabricated citation / criteria backdoor / leakage / sycophancy drift / average face
acceptance layer: L__

L0 (independent channel)
☐ Citation sample by `python scripts/leak_check.py sample --n 5 --pct 10 --seed <s> <citation list>` (5 or 10%, whichever is larger, illustrative); each: exists? says so? → briefs/verify-citations.md
☐ Three key numbers traced to origin or dead end (a dead end is a hard defect) → briefs/trace-numbers.md
☐ One reverse question → briefs/reverse-question.md
☐ Escalation (rule): any hard defect → the whole output goes to L1; say so

L1 (every item)
☐ Claim list extracted and grouped: citation / number / reasoning → briefs/verify-citations.md
☐ Every citation: exists, says so, later retracted or overturned
☐ Every number: original source, basis match (baseline, window, units) → briefs/trace-numbers.md
☐ Every reasoning link typed citation / calculation / "author thinks"; "author thinks" links listed for the human
☐ Claim-to-source table filed (below)

L2 (per named load-bearing conclusion)
☐ Independent re-derivation from raw materials only, no residue of the original → briefs/rederive.md; converges: machine evidence; diverges: each point ruled by hand
☐ Key numbers recomputed by another method or data source
☐ Red team, mandatory → templates/red-team-dispatch-brief.md
☐ No raw materials: write "L2: not possible (no raw materials); the four attack surfaces used as the acceptance checklist instead"

Claim-to-source table (filed with the output)
| # | Claim (neutral wording) | Type (citation / number / reasoning) | Source found (opens, or exact location) | Verdict (confirmed / falsified / undecidable) | Channel | Date |
|---|---|---|---|---|---|---|
| 1 | ____________ | ______ | ____________ | ________ | ______ | ______ |

acceptance layer: L<n> (destination: <...>; likely error class: <...>)
checked: <list>   not checked: <list>
verdicts: confirmed <a> / falsified <b> / undecidable <c>   hard defects: <n>   escalated: yes/no
criteria timestamp: before results | after results | none
verification channel: separate session, <model or person>, brief: briefs/<file>, leak_check: clean
verification level note: <tier>; reason: <the real constraint>
ruling (fit for <destination>): <draft value> | signed by: UNSIGNED
answers when wrong: NOBODY | <person's name>
Signature: ____________ (must be a human)
```

### Self-check
- [ ] Layer assigned by how reliable it looks? That is grading by prose. Reassign by destination and error class.
- [ ] Sample picked by hand on the spot? A hunch is not a spot check. Lock the rule and let the script pick.
- [ ] Any check run in the generating channel? Void. Re-dispatch with the brief as the only payload.
- [ ] Undecidable column empty? Either unusually clean or the channel is fudging. Check two items yourself.
- [ ] A failed item let through because the author explained? What fails the mechanism does not merge. Keep it falsified.

Filled in → goes to: templates/downgrade-note.md
