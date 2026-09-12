**Load this reference when:** you are delegating to an agent or subagent, writing a task brief, setting up a process or checklist, or the user is a beginner in the field.
Source: chapters 14, 15, 16 (docs/chapters/ch14.md, docs/chapters/ch15.md, docs/chapters/ch16.md, docs/appendices/ch14-templates.md, docs/appendices/ch15-templates.md, docs/appendices/ch16-templates.md)

## Contents

1. Rules
2. Procedure: sort process steps
3. Procedure: write a dispatch brief
4. Procedure: install a habit unit and retire its lines
5. Procedure: the monthly signal filter
6. Decision and vocabulary
7. Self-check
8. Templates and briefs

## Rules

Separate the person from the process steps. What gets eaten is transcription work; judgment work appreciates because production got cheap and every output now needs someone to answer "can it be trusted". Depreciating does not mean gone: a transcription step moves from "you do it by hand" to "you dispatch and accept", the hand disappears, the responsibility stays in your name. Two sorting questions decide which is which:

| Question | Transcription | Judgment |
|---|---|---|
| Is there cheap ground truth? | Yes: right and wrong checkable on the spot, the method sits in ten million precedents | No: "what counts as right" is itself part of the job |
| How fast do errors show up? | On the spot or at delivery | Only downstream, silent until then |

Five crafts, one line each:

| Craft | One line |
|---|---|
| Taste in questions | Judging which of a hundred candidate questions deserves three months of a life |
| Criteria design | Signing "what counts as losing" before the run |
| Dispatch craft | Turning tacit context into a brief a stranger can execute |
| Verification discipline | Layer assignment, independent channel, three-value output, across all seven steps |
| Honest calibration | Pricing your own output: status, what changes it, review date |

All five are meta-work. They produce constraints on content and not one line of the content. The sentence: you go from a person who produces content to a person who produces constraints.

"Who answers when it's wrong" must be a person's name (rule). If no name can be written, drop one delegation level and ask again; `answers when wrong: NOBODY` means hand back. The context pack is updated before dispatch (rule). The executor does not refresh facts on its own; the world in the brief is its entire world. A stale status doc is the top source of rework, and the rework is booked to the dispatcher, not the executor.

The smallest unit of a habit is a trigger plus a checklist; resolve is not one of them. The trigger is an objective event ("every time I open a new conversation for this step", "every time before output leaves my desk"); "I will be more rigorous" is a wish. The checklist is three questions at most (rule). A checklist on the wall is decoration; only a checklist on the path is a gate. The path is the first line of the conversation template, the first column of the dispatch brief, the head of the document template. A sticky note beside the monitor is the wall. Give judgment to people and execution to institutions, and do not get it backwards: review bandwidth equals the number of verification steps times the probability they get executed, and an institution governs that probability. A criterion executed only on good-energy days is worth half its nominal hardness.

Beginner's brake (rule while it stands). If the user has not banked judgment in this field, keep at least one transcription step by hand, literature summaries or citation checks, for a full month (illustrative) before outsourcing. At the literature step you may find which paper to read and quiz after reading ("I understand it as X, how far does the original support that"); you may not write the summary. At the criteria step, drafted plans are walked item by item against the confounder checklist, never adopted whole. Withdrawal condition: a controlled measurement shows that people who used AI throughout from the start have judgment indistinguishable from the traditional path three years later (illustrative). Until then, slower is better.

What expires versus what does not. Conclusions, statuses, model names, and benchmark scores expire within months. The seven-step structure, verification discipline (generation separated from verification, criteria locked first, independent channel, production-grade over demo-grade), the five-column map method, and the pattern check on new headlines do not expire with a model version. Bet on mechanisms, not outcomes.

## Procedure: sort process steps

1. List the 10 to 15 process steps (illustrative) the user actually did last week, verb first, down to the object: "formatted the citations for a report". Send anything at the grain of "did research" back for splitting.
2. Ask the two sorting questions per step. The human answers and sets the label. "Mixed" is split in two and relabeled; it is the usual escape from sorting. Estimate time shares against the calendar, never against impression.
3. Circle the most time-consuming depreciating step: it gets the first four-column brief this week. Circle the weakest of the five crafts: it is the user's private focus.

## Procedure: write a dispatch brief

Four columns, in this order. Nothing outside the brief exists for the executor.

```
[TASK] What to produce. Verb first, one sentence. Medium, format, length, deadline.
[CONTEXT] Every fact and file the executor needs, on the rule "the recipient knows only what the brief says":
          required reading and which file wins in a conflict; key terms and basis; conclusions already overturned. ☐ Context pack confirmed current.
[BOUNDARIES] No inventing facts, citations, or numbers; anything uncertain marked "to verify".
          What not to touch (claim strength wording, for one). Missing information: come back with a list.
[ACCEPTANCE CRITERIA] Checks a third party can run. Rework conditions: any one sends it back.
```

The stranger-executor test (rule): an executor who has never met you and cannot ask you questions can start work from this brief alone, and knows what counts as delivered. Fail it, fix the brief before dispatch. For a verification task the brief gives only the claim and leaks no expected answer: use a file from `briefs/` and run `python scripts/leak_check.py brief` first. Fill `answers when wrong:` with a name before dispatch.

Bad brief (illustrative): "Look into whether method X beats the baseline, focus on the latest progress, and write me a solid summary, not too long." "Look into" defines no deliverable; "latest" has no time basis; "solid" and "not too long" cannot be accepted against; zero context, zero boundaries, and no list will catch an invented citation. Good brief (illustrative):

```
[TASK] Produce an evidence table on "method X vs the baseline", one paper per row:
       claim / evidence / limits of application / relevance to our question. 10 to 15 rows, by 22:00.
[CONTEXT] Purpose: a base table for the meeting deciding whether to pilot X. Required reading: the attached
       controversy map v3 (wins over memory). Basis: "stronger" means accuracy after cost alignment.
[BOUNDARIES] Only papers with a real source; mark unsure ones "to verify". Draw no conclusion on "should we
       pilot". Missing basis information: come back with a list.
[ACCEPTANCE CRITERIA] 1 every paper findable in an academic search engine, link attached; 2 every claim keeps
       the paper's own qualifiers; 3 no empty limits cell. Rework: a claim with no source, or a citation not found.
```

## Procedure: install a habit unit and retire its lines

1. Pick one process step: the one where AI is deepest in and the cost of error is moderate.
2. Write the trigger as an objective event, precise down to the action. Send back intention triggers ("plan to", "try to").
3. Fill the three process questions card for that step. Nouns and numbers count; adjectives do not.

```
Question one, criteria. Where does this output go (own desk / team / decision chain or public)? Layer L__.
  What counts as passing (a third-party check). What counts as losing (locked before start; no answer, no start).
Question two, delegation. Level for this step (tool / assistant / collaborator / autonomous local).
  Who drafts / who reviews / who decides / who answers when it's wrong (a person's name, or drop a level).
Question three, verification. Most likely error class (from the census) and its signature in this project.
  Which layer it passes before it leaves, and which independent channel runs it.
```

4. Install the card on the path: first line of the conversation template, first column of the brief template, head of the document template. Edit the files; do not post a note.
5. Put the retrospective on the calendar at day 14 (illustrative). Count two numbers: how many times the three questions were answered, and what got caught. Nothing caught means either the checklist is worded too loosely (reword) or the step was low risk (pick a more painful step); lay out both, the human picks. The acceptance signal is behavioral: skipping the three questions feels awkward.
6. Retire lines monthly (illustrative). Every line either shows a recent catch record or gives an explicit reason to stay. Delete or rewrite every line that has never caught anything (rule). A line at one hundred percent pass for three months (illustrative) with no catch is either internalized (delete it) or never executed (reword it or change the trigger). The health metric of a checklist is its catch record; its length does not count. A dead checklist is more dangerous than none, because ticking manufactures the illusion of safety in bulk.

## Procedure: the monthly signal filter

A piece of news is worth an hour if and only if it could change the status of some row on some map of the user's. Hold it against that row's fourth column and ask whether this is the evidence it describes. The hour (illustrative): 20 minutes sorting sources into hit or flow past, 30 minutes running the fourth column on the hits, 10 minutes changing a status or a date and writing one change-log line. Checked and nothing moved, the date still changes.

| Signals that trigger a re-derivation | Ignore list |
|---|---|
| A production-grade measurement appeared (merge rate, rework rate, verification pass rate, claim survival rate) | Demo videos and vendor launch events: trigger an investigation, never a status, never anxiety |
| An independent reproduction or refutation appeared | Self-reported speedups with no control |
| A criterion locked earlier was tripped, or the fourth column's evidence surfaced | Model version-number news; a controlled measurement on the user's own tasks is the signal |
| Repeated rework in the user's own workflow, the same step crashing several times running | The Nth round of the "AI replaces scientists" debate |
| A policy or basis change from journals, reviewers, or regulators | Secondhand retellings with no link to the original; anonymous leaks and rumors |

## Decision and vocabulary

| Slot | Allowed values |
|---|---|
| Process step label | transcription / judgment (mixed is split, never kept); depreciating / appreciating |
| Delegation level | tool / assistant / collaborator / autonomous (local) |
| Trigger; checklist line at retrospective | an objective event, intentions rejected; catch record / explicit reason to stay / deleted |

Sentinel on every brief and every card: `answers when wrong: NOBODY | <person's name>`. NOBODY drops one level and hands back.

## Self-check

- [ ] Did you label a step "judgment" without being able to say what counts as wrong for it? Transcription not yet thought through. Re-sort.
- [ ] Did you estimate time shares from impression? Self-perception is not evidence. Read the calendar.
- [ ] Does the brief fail the stranger-executor test, carry a criterion like "write it better", or ship with an unconfirmed context pack? Fix the brief; replace the criterion with a third-party check; expect rework and book it to yourself.
- [ ] Is the trigger an intention, or is the card on the wall? Rewrite the trigger as an event; move the card onto the path.
- [ ] Has a checklist line gone three months with no catch? Delete or rewrite it.
- [ ] Is the user a beginner, and did you write the summary for them? Quiz instead. Keep one transcription step by hand.

## Templates and briefs

- `templates/dispatch-brief.md`: the four-column brief with the stranger-executor test and a generic good example.
- `templates/three-process-questions.md`: the card, one per process step, with the retirement cadence attached.
