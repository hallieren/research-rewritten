# Disposition record

**How to use.** Every charge that comes back gets a verdict, holds or rejected, from a human; every held charge gets one of three dispositions; there is no fourth (rule). "I am aware of it" is not a disposition. Qualification runs in a fixed order: fixable, fix it; testable, test it; fatal, overturn or narrow; only when all three fail does caveat get its turn. The model runs each executable check and records the result; the verdict, the tier, and the action are yours. File the record with the deliverable; a report carrying bullet holes and dispositions is more credible than one that looks untouched.

| Tier | Trigger | Disposition action | The unqualified form |
|---|---|---|---|
| overturn | The charge hits load-bearing structure and no rewording saves it | The announcement sentence comes off the deliverable; the preregistered numbers are still reported as is, post-hoc beside them. The sentence is overturned, not the number | Quietly deleting the number and never mentioning the conclusion existed |
| narrow | The charge holds but cuts range or strength of evidence, not the conclusion | Rewrite the boundary (task family / sample / confidence / exact model); the new statement is strictly weaker and still checkable | Narrowing into vaguer words ("may under some circumstances"): escape, not narrowing |
| caveat | The charge holds or cannot be ruled out; unfixable, untestable, not fatal | The conclusion stays; the caveat travels at the same address; one check is left for the next round | Buried in an appendix or footnote; a caveat hung where an overturn belongs |

```text
STATUS: DRAFT, not for the decision chain
# Red-team disposition record
Deliverable: ____________   Date: ____________
Red-team channel (model / session, differs from the writing channel): ____________

| # | Attack surface | Charge (one sentence) | Check run and result | Verdict (holds / rejected) | Tier (overturn / narrow / caveat) | Action (which sentence changed, at every address it appears / what caveat hangs) |
|---|---|---|---|---|---|---|
| 1 | ____ | ____________ | ________ | ________ | ________ | ____________ |
| 2 | ____ | ____________ | ________ | ________ | ________ | ____________ |

Rejected charges (one line of reason each, kept as ammunition at the defense): ____________
Surfaces that came back empty, re-dispatched with another model (empty counts only twice): ____________
One more quick round after revision (a patch can introduce a new handle): yes / no
Filed at (same repo as the deliverable): ____________

ruling: holds / rejected per charge; disposition: overturn / narrow / caveat | signed by: UNSIGNED
answers when wrong: NOBODY | <person's name>
verification channel: SAME-CHANNEL (void) | separate session, <model or person>, brief: briefs/<file>, leak_check: clean
criteria timestamp: before results | after results | none
Signature: ____________ (must be a human)
```

### Self-check
- [ ] A charge ruled holds with no tier? There is no fourth disposition. Assign one.
- [ ] Far more caveats than overturns plus narrowings? The caveat is being used as a trash can. Rerun the three qualification questions line by line.
- [ ] The narrowed statement vaguer instead of weaker? Weaker means still checkable with a clearer boundary. Rewrite it.
- [ ] Only the abstract changed? The conclusion appears at several addresses; the disposition lands at every one. Search the body.
- [ ] Record not going out with the deliverable? It is part of the trust mechanism. Attach it.

Filled in → goes to: templates/honest-map.md
