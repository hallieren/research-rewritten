# Ladder self-rating sheet

**How to use.** Score one real project in hand, not yourself and not your tools. Fill two cells per step: the current level (how the step is done right now) and the target level. Higher is not better for the target; some steps stop at assistant on purpose. Rule on the level with the four questions in the quick reference; when an answer changes, the level changes. Refill each time the project goes around the loop.

> The order of use is fixed. templates/ladder-self-rating.md → templates/seven-step-cards.md → templates/five-premise-table.md.

| Level | Who drafts | Who reviews | Who decides | Who answers when it's wrong |
|---|---|---|---|---|
| tool | You | You, a glance in passing | You | You; errors visible on the spot |
| assistant | AI | You, every part in full | You | You; human review is the only line of defense |
| collaborator | AI, with self-checks and alternatives | You, checkpoints plus spot checks against a locked process | You | You plus the process; errors hit the criteria first |
| autonomous (local) | AI, including intermediate decisions | Mostly AI self-review; you accept the end product | Goals and acceptance criteria stay with you; the process goes to AI | NOBODY; enter serious settings with care |

```text
Project: ____________   Date filled: ____________   Fill-in round: ____

| Step | Current level (tool / assistant / collaborator / autonomous) | Target level | Upgrade precondition (the locked criterion or process this step needs before it may go up one level) | Who or what found the last error at this step |
|---|---|---|---|---|
| 1 Master the field | | | | |
| 2 Questions and hypotheses | | | | |
| 3 Test plan | | | | |
| 4 Execution | | | | |
| 5 Read and catch errors | | | | |
| 6 Deliver | | | | |
| 7 Red team | | | | |

The step I most want to climb: ____________
The step I least dare let go of (my operating room): ____________
Cells where "who answers when it's wrong" has no name: ____________ (rule: those cells run at tool level until a name exists)
Signature: ____________ (must be a human)
```

### Self-check
- [ ] All seven steps at the same level? Levels live on step x task. Refill per step.
- [ ] A step marked collaborator with no locked criterion in the precondition column? Drop it to assistant; without criteria there is no standing to spot-check.
- [ ] Read and catch errors marked collaborator or higher? Drop it; no step's errors disguise themselves better.
- [ ] The last-error column reads "I happened to notice" everywhere? There is no process-level verification yet. Nothing goes above assistant.
- [ ] The whole target column says autonomous? Turning every knob to maximum is an operating room that fails sterilization. Name the steps that stop at assistant on purpose.

Filled in → goes to: templates/seven-step-cards.md
