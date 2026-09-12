# Three process questions card

**How to use.** Install it on the path, not on the wall: the first line of the conversation template, the first column of the dispatch brief, the head of the document template. One card per process step; steps never share a card. Nouns and numbers count, adjectives do not. The trigger is an objective event, precise down to the action. Retirement cadence (rule): monthly retrospective; every line either shows a recent catch record or an explicit reason to stay, and a line with neither is deleted. The health metric is the catch record, not the length of the checklist.

```text
# Three process questions card   Process step: __________   Trigger (objective event): __________

Question one, criteria
  Where does this output go?  ☐ own desk   ☐ team discussion   ☐ decision chain / public
  → Verification layer: L____
  What counts as passing (a check a third party can execute): __________
  What counts as losing (locked before starting; no answer, no start): __________
  criteria timestamp: before results | after results | none

Question two, delegation
  Level AI sits on for this step:  ☐ tool   ☐ assistant   ☐ collaborator   ☐ autonomous (local)
  Who drafts: ____   Who reviews: ____   Who decides: ____
  answers when wrong: NOBODY | <person's name>   (no name → drop one level and ask again)

Question three, verification
  Error class this step most likely breaks in (from templates/failure-mode-census.md): __________
  Signature (the specific signal in this project, not copied): __________
  Layer it passes before it leaves: L____   Independent channel that executes it (model or person, brief file): __________

Retirement log (monthly): date ______   lines with a catch record: ______   lines kept with a reason: ______   lines deleted: ______
Signature: ____________ (must be a human)
```

### Self-check
- [ ] Card stuck on the wall instead of the path? It will not fire. Paste it at the head of the template it governs.
- [ ] An adjective in an answer ("careful review")? Replace with a noun and a number.
- [ ] `answers when wrong:` has no name? Drop one level and ask the four questions again.
- [ ] A line with no catch record and no reason to stay? Delete it this month.
- [ ] Two steps sharing a card? Split them; the trigger and the layer differ.

Filled in → goes to: templates/ladder-self-rating.md
