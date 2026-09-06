# Chapter 15 templates · 30-Day Adoption Plan + Three Process Questions Card + Team Metrics Starter Sheet

> This appendix is the complete fillable version of the three tools in Chapter 15.
> The order of use is fixed. Start with Template 2 (the three questions card) to install your first habit unit (the two-week trial run of 15.8). Once the trial run has a catch record, open up Template 1 (the full 30-day plan). Leave Template 3 alone until your personal process runs smoothly. Team metrics are built on top of a personal working example, and reversing the order gets you the enterprise tool from section 15.1 that nobody logs into.

---

## Template 1 · 30-Day Adoption Plan

**How to use.** Install one part a week, and hold a retrospective at the weekend. Fill in the "success criterion" field before you start. For your own adoption plan too, the criteria get locked in first. The weekly retrospective answers two numbers only, coverage (of the times it should have fired, how many it actually ran) and the catch record (what got caught).

```text
# 30-day adoption plan   Start date: ____

## Week one   one process step
- Process step chosen: __________ (suggested: the one where AI is deepest in, with a moderate cost of error)
- Trigger (an objective event, precise down to the action): __________
- Content of the three questions card (copied from Template 2, filled in as yours): __________
- Success criterion: coverage ≥ ____% (suggested 80%; output quality is not assessed)
- Weekend retrospective: covered ___/___ times; catch record: __________

## Week two   chain two (generation + verification welded shut)
- Downstream verification action: after every generation, run one L0 spot check (Chapter 12)
- Spot-check parameters: ___ citations / ___ numbers sampled (starting default 5 citations or 10%)
- Success criterion: share of generations followed by verification ≥ ____%
- Weekend retrospective: covered ___/___ times; catch record: __________

## Week three   run the whole workflow once
- Small real problem chosen (two or three days of work): __________
- Take the small loop of the seven steps, answer the three questions at every door, rough is allowed
- Record: which door made the three questions most awkward? __________ (= where the checklist needs rewording)

## Week four   retrospective and retirement
- Total times the three questions were answered: ____
- Catch list (one line each: what got caught, at which process step): __________
- Lines that never caught anything: __________ → delete or rewrite
- Decisions: which triggers stay / which process steps get added next month: __________

## Acceptance test at day 30 (behavioral signal, tick one honestly)
- [ ] Skipping the three questions feels awkward (the default has been swapped, the institution has taken over)
- [ ] It does not feel awkward (back to week one, pick a more painful process step or a harder trigger)
```

---

## Template 2 · Three Process Questions Card

**How to use.** Install it on the path, do not stick it on the wall (the first line of the conversation template, the first column of the dispatch brief, the head of the document template). Write your project's specific answer after each of the three questions. Nouns and numbers count, adjectives do not. One card per process step. Different steps get filled in separately and never share a card.

```text
# Three process questions card   Process step: __________   Trigger: __________

Question one, criteria (Chapters 6 and 12)
  Where does this output go? [ ] stays on my desk   [ ] into team discussion   [ ] into the decision chain / public
  → Verification layer: L____
  What counts as passing: __________ (a check a third party can execute)
  What counts as losing: __________ (locked in before you start; no answer, no start)

Question two, delegation (Chapter 3)
  Level AI sits on for this step: [ ] tool   [ ] assistant   [ ] collaborator   [ ] autonomous (local, see Chapter 7)
  Who drafts: ____   Who reviews: ____   Who decides: ____   Who answers when it's wrong: ____
  (The "who answers when it's wrong" field has to be a person's name. If you cannot write a name, drop a level and ask again.)
  (The four answers combined are your title in the human-side role table of Chapter 14, the artisan, the lead writer, the editor-in-chief, or the principal.)

Question three, verification (Chapters 11 and 12)
  Which class is this process step most likely to break in (open your failure-mode census sheet): __________
  Signature (the specific signal in your project, not copied from the book): __________
  Which layer it passes before it leaves: L____   Which independent channel executes it: __________
```

**Retirement cadence (carried with the card).** Hold a retrospective once a month. Every line either produces a recent catch record or gives an explicit reason to stay. A line with neither gets deleted. The health metric is the catch record, not the length of the checklist.

---

## Template 3 · Team Metrics Starter Sheet

**How to use.** Use the three metrics in pairs, draw trend lines, and keep them for this group's learning only. They do not enter individual performance reviews, and absolute values do not get compared across teams (the basis differs, the comparison is meaningless). Audit the metrics themselves once a quarter, and for the one whose number improved, first ask "did things get better, or did the reporting change."

| Metric | Basis | Collection method | Paired metric (anti-gaming) | This month | Last month |
|---|---|---|---|---|---|
| Rework rate | Share of output with AI deeply involved that gets sent back for redoing after delivery downstream | The "sent back" label plus its reason on the task board, counted once at month end | Throughput (stops people cutting rework by delivering less) | | |
| Verification pass rate | Share passing on the first try in spot checks and full verification; citation existence, paraphrase fidelity, and number traceability recorded separately | The verification ledger (Chapter 12) is the data source, nothing separate to collect | Verification coverage (stops people checking only the safe output) | | |
| Claim survival rate | Share of conclusions entering the decision chain that still stand at a scheduled review point (three months, say) | The conclusion register plus the review cadence of Chapter 13 | The risk level of the conclusion (stops conclusions getting more and more timid) | | |

**Rules that ship with it (copy these along when you copy it into the team wiki)**:
1. The numbers serve this group's learning and do not enter individual performance reviews (once they do, rework moves into private messages and the board is at peace forever);
2. Metrics have to be read in pairs, since a single metric always has a painless cheat posture;
3. Audit the metrics themselves once a quarter;
4. Whoever updates signs, the same discipline for the metrics sheet as for the case status doc.
