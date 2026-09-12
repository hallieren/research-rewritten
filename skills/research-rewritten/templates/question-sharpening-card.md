# Question-sharpening card

**How to use.** One card per complete run of the five prompts in briefs/diverge-candidates.md. The three-test scores (0/1/2) are yours; the model only attacks. Testable at 0 is a veto (rule). Write the falsifiable sentence yourself; ask for three versions only when stuck. Budget one hour (illustrative); well over means sharpening is putting off starting. Sign when filled, then pin it to the first page of templates/test-plan.md.

```text
STATUS: DRAFT, not for the decision chain
====================== Question-sharpening card ======================
Date: ____________  Project: ____________

[Direction] (raw material, vague allowed): ____________

[Candidate pool] (step 1)  Total: ____  Marked "already asked": ____  Marked "unsure": ____
  Top three entering scoring:  A. ________  B. ________  C. ________

[Three-test scores] (0/1/2; testable 0 = veto)
                Testable  Worth answering  Affordable  Total
  Candidate A:    ___          ___            ___       ___
  Candidate B:    ___          ___            ___       ___
  Candidate C:    ___          ___            ___       ___
  Survivor: ____   Survivor among the "already asked" marks: ☐ no  ☐ yes (back to step 1)

[Falsifiable sentence] (step 3, both lines required)
Under __________ (conditions/basis), the __________ (measurable metric) of __________ (subject),
compared with __________ (control), is __________ (direction and threshold).
If __________________________________ is observed, the hypothesis is falsified.
Control is the cheapest alternative explanation for the same result, steelmanned, not a straw man: ____________
Threshold values and their reasons (final lock at the test plan): ____________
Gray band (rule: three values only):  tie: ______  undecided: ______  lost: ______

[Action rehearsal] (step 4)
  If the answer is yes, action: ______________   If the answer is no, action: ______________
  Different?  ☐ yes (pass)  ☐ no (back to step 2)
  Middle outcomes and the verdict the falsification condition gives each (at least one): ____________

[Resource check] (step 5)
  Most expensive step: ______________
  Walkable?  ☐ walkable  ☐ walkable after shrinking (what was shrunk; still the same question: ________)  ☐ not walkable
  If not walkable: ☐ switch candidate  ☐ back to the map for a different battlefield  ☐ shelve it honestly

[Exclusion] (rule) no scoring by an LLM judge where judge preference becomes a second unknown: ☐ checked

[Sign-off] I ruled on this question. AI only supplied candidates and counterpoints.
ruling: candidate ____ survives / no candidate survives | signed by: UNSIGNED
answers when wrong: NOBODY | <person's name>
Signature: ____________ (must be a human)
======================================================================
```

### Self-check
- [ ] The question has no finished state? Then it is a direction. State under what conditions it counts as answered or falsified.
- [ ] "Effectiveness", "possibility", "potential" in the falsifiable sentence? No observation can kill those. Replace with a metric and a threshold.
- [ ] The survivor is the model's recommendation? Nobody answers for that. Score the three tests yourself and rule.
- [ ] A middle outcome the falsification condition is silent on? That silence is a hole. Rewrite the condition until every middle outcome gets a verdict.
- [ ] Threshold numbers with no reason recorded? Write the reason now; the test plan locks them next.

Filled in → goes to: templates/test-plan.md
