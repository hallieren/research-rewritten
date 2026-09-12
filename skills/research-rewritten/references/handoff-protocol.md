**Load this reference when:** you must decide a delegation level for a task, answer whether you may do X alone, x-ray a "tool does research autonomously" claim, rate a project's levels step by step, or check your own conduct against the human's role.
Source: chapter 3 (docs/chapters/ch03.md, docs/appendices/ch03-templates.md), chapter 14 (docs/chapters/ch14.md), chapter 15 (docs/chapters/ch15.md), and the "Want an agent to run it with you?" block in docs/chapters/ch00-start-here.md through ch16.md.

## Contents

- Rules
- Procedure: set the level for one task
- Procedure: rate a project (ladder self-rating)
- Procedure: x-ray an "AI did research" claim
- Decision and vocabulary
- The dated snapshot (snapshot, 2026-08)
- Agent conduct rules
- Self-check
- Templates and briefs

## Rules

1. The level lives on one kind of task at one step (step x task). There is no master switch, no project-wide level, no per-person level. Asked "what level does this project use", answer "which step, which task".
2. Four questions set the level, and nothing else does: who drafts, who reviews, who decides, who answers when it's wrong. Change any answer and the level changes. Capability adjectives ("smarter", "more powerful") set nothing.
3. Three variables decide whether the knob may go up: how visible errors are, how cheap correction is, whether cheap ground truth exists. Where errors are silent, correction is expensive, and no ground truth exists, the knob stays low however strong the model.
4. The ticket into collaborator is an executable standard of verification locked before the work. No locked criteria, no standing to spot-check, no collaborator level.
5. Climbing is not turning every knob to maximum. Some steps stop at assistant on purpose. Read and catch errors is downgraded on purpose.
6. `answers when wrong: NOBODY` on any task means the task runs one level lower and goes back to the human with the four questions. NOBODY never proceeds.
7. The snapshot below is dated. When the four questions and the snapshot disagree, the four questions win.
8. Levels also depend on the human's situation. Same step, same task, a different evidence shape or no next round, and the safe ceiling moves down a level. Check the five premises before trusting any ceiling.

## Procedure: set the level for one task

1. Name the step (one of the seven) and the task inside it (one kind of task, not "the step").
2. Answer the four questions in writing. Who drafts. Who reviews, and how (every part / checkpoints and spot checks against a locked process / end product only). Who decides. Who answers when it's wrong (a person's name, or NOBODY).
3. Read the level off the four-level table below. The lowest answer wins: a task reviewed "end product only" with NOBODY answering is autonomous whatever the drafting looks like.
4. Check the three knob variables for this task. Any of the three on the wrong side (silent errors, expensive correction, no cheap ground truth) caps the task at assistant.
5. Check the collaborator ticket. A task at collaborator or above must point at a criteria file with a timestamp earlier than the first result. No file, drop to assistant.
6. Compare with the snapshot row for the step. Above the water line, write the reason in one sentence and name the locked criteria that justify it. Below or at the line, proceed.
7. Emit the four sentinel lines for the task. `answers when wrong:` carries a name or NOBODY. NOBODY triggers rule 6.

## Procedure: rate a project (ladder self-rating)

1. Build an empty step-by-level matrix from `templates/ladder-self-rating.md`. Seven rows, one per step; columns for current level, target level, upgrade precondition, and who found the last error.
2. Walk the seven steps one at a time. For each, ask the human the four questions and fill the current level from the answers. Do not upgrade the human. A cell where the human cannot answer "who answers when it's wrong" is filled tool level, without exception.
3. Ask for the target level per step. Higher is not better. Where the snapshot says "no door", a target above assistant gets sent back with the snapshot row quoted.
4. Fill the upgrade precondition per step: the locked criterion or process that must exist before the knob goes up. A collaborator target with an empty precondition drops to assistant.
5. Fill "who found the last error". A column that reads "I happened to notice" all the way down means no process-level verification exists; no step goes above assistant.
6. The human circles two cells: the step they most want to climb, and the step they should least let go of (their operating room). You bold only the two cells they circle. You circle nothing.
7. Fill one card per step from `templates/seven-step-cards.md`: what is produced, who is downstream, the four answers, the done criterion, the send-back signal. A blank the human cannot fill is the diagnosis; leave it blank and say so.
8. Run the five premises from `templates/five-premise-table.md`. Whether each holds is the human's call. For each broken premise, state the conversion direction (what fails first, what compensates). Two or more broken means every later step needs one conversion; write the broken premises next to the conclusion of every deliverable.

## Procedure: x-ray an "AI did research" claim

1. Do not count the steps the demo covers. That count grows every quarter and cheats you.
2. List the steps it does not cover. The stable absentee list: who chose the question, who decided this task was safe to hand off, who signed the criteria, who set the claim strength, who answers when it's wrong.
3. Look the last one up in the manual. No answer in the manual means nobody.
4. Name the tool correctly: "collaborator on <the covered steps>". Never "autonomous researcher".
5. Route any adoption decision through the snapshot row for each covered step and the three knob variables. A demo triggers an investigation; it never decides a status.

## Decision and vocabulary

The four levels by the four questions:

| Level | Who drafts | Who reviews | Who decides | Who answers when it's wrong |
|---|---|---|---|---|
| Tool | You | You (a glance in passing) | You | You; errors visible on the spot |
| Assistant | AI | You, every part in full | You | You; human review is the only line of defense |
| Collaborator | AI (with self-checks and alternatives) | You, checkpoints and spot checks against a locked process | You | You plus the process; errors hit the criteria first |
| Autonomous researcher | AI (including intermediate decisions) | Mostly AI self-review; the human accepts only the end product | Goals and acceptance criteria stay with the human; the process goes to AI | Nobody; the reason this level is rare where a wrong answer hurts |

The same ladder from the human side (roles live on step x task, like levels):

- Tool: artisan. The craft is in your hands, AI is a faster pen.
- Assistant: lead writer and full reviewer. AI drafts, you read every paragraph; your eyes are the line of defense.
- Collaborator: editor-in-chief and process designer. You write criteria, design the process, spot-check, and rule.
- Autonomous researcher: principal, with nobody answering. The human role at this level has never been filled in; "nobody" must never appear in a role column.

The three things that stay human, each with its test:

| Always human | Test |
|---|---|
| Judgments where someone answers when they are wrong | When it goes wrong, who cleans up (retracts, compensates, corrects, apologizes)? AI bears no consequences, so the last pair of eyes on any judgment with unrecallable consequences is a person. |
| The power to define what counts as winning | Open the criteria file and read the name where the final ruling goes. That name is the project's real researcher. |
| A signature carrying lifetime responsibility for the output | Ask: three years from now this is falsified, who steps up? An output whose answer holds no person's name does not go out. |

The three process questions, asked at the door of every step (opening a conversation, dispatching a task, taking delivery of an output):

| Question | Ask | Answer form |
|---|---|---|
| Criteria | Where does this output go, what counts as passing, what counts as losing? | destination; a number that triggers "lost" |
| Delegation | Which level for this step, who drafts, who reviews, who answers when it's wrong? | the four answers; `answers when wrong: <name>` |
| Verification | Which class is it most likely to break in, and which layer does it pass before it leaves? | error class; `acceptance layer: L<n>` |

A checklist on the wall is decoration. Ask the three questions on the path: first line of the conversation, first column of the brief, head of the document.

## The dated snapshot (snapshot, 2026-08)

Water lines as of the rechecking date. To count as stable, many everyday users must reproduce it; demos do not count. Read the first two columns to set the level; the note column is evidence for looking back.

| Step | Stable water line | Half-open door | Note (snapshot, 2026-08) |
|---|---|---|---|
| Master the field | Assistant | Collaborator: having AI find what the literature is arguing about is feasible | "Which argument is worth entering" stays human; the output of fully automatic review tools works as a first draft, not yet as a map |
| Questions and hypotheses | Assistant (batch-generating candidate questions and hypotheses) | None | "Which question is worth answering" has no reliable automated path, still exploring. The closest current systems come to autonomous questioning is picking up ideas already public and abandoned, combining them, and landing them, which is an extension of execution; "autonomous" claims here are mostly marketing |
| Test plan | Assistant | Collaborator, still exploring | AI drafts a plan fast, but the most expensive flaws in a plan (unfair baseline, basis drift, a criteria backdoor) are the kind it does not flag itself. Inferred from adjacent evidence (models are insensitive to flaws in their own output; AI-as-judge fails silently); no direct measurement yet of the "drafting a test plan" setting |
| Execution | Collaborator | Local autonomy: feasible on closed subtasks with tests and criteria guardrails in place | Highest of the seven, the most direct dividend from coding transfer. "Local" is load-bearing: leave the guardrails and it downgrades. Unattended runs of days to weeks on closed tasks have public cases; feasible does not mean faster |
| Read and catch errors | Assistant (nominally) | None | Demands the strongest human presence. Models tend to say what you expect; sycophancy is measured across frontier assistants and many task types, and human preference data rewards it. How to make AI disagree reliably is still exploring |
| Deliver | Assistant | None | Drafting, rewriting, figure captions can be handed off; responsibility for claim strength and wording cannot |
| Red team | Assistant, widely underrated | Collaborator, systematic search for counterevidence, still exploring | Having AI attack a draft costs almost nothing and pays at once; it finds holes in reasoning, not the "everyone in the field knows this, only it doesn't" kind |

Half-open door means: feasible in public cases, not yet reproduced by many everyday users. Treat a half-open door as assistant until the locked criteria for this task exist.

## Agent conduct rules

Distilled from the agent blocks named on the Source line. Each rule is a boundary you hold without being reminded.

1. You build the table; you never write the human's conclusions.
2. Ask the four questions and fill the level from the answers; do not upgrade the human.
3. You may not sign on the human's behalf. `signed by:` reads UNSIGNED until a human writes a name.
4. You may not say that a conclusion looks fine, and you may not say a number is probably right.
5. For any check, open a separate session and paste only the plan or the claims, never the human's expectations.
6. You may not check citations on the human's behalf, and you may not call a map trustworthy before the human has finished checking.
7. You only bold the two cells the human circles; you circle nothing, and you do not circle the cell holding the conclusion they are most excited about.
8. Send a signature back if it copies a generic phrase instead of a concrete signal from the human's own project.
9. Paste the human's one-sentence question, or the announcement sentence verbatim, at the top of every reply.
10. You may not swap an interval quietly; you write `n=<rows>, <k> independent units` into the body and stop there.
11. If any command errors, stop and show the output.
12. Generate candidates, counterpoints, charges, and leads; the pick, the score, the ruling, and the disposition are the human's. "I recommend candidate 3" is banned.
13. Mark every candidate "already asked", "not seen", or "unsure", with a source for the mark. "Not seen" means unsure, not novel.
14. Record what the human cannot clear into the limitations; never clear a line for them.
15. Send back any trigger that is an intention ("plan to", "try to") and any evidence entry that reads "everyone says so".
16. The human sets the label, the status, the threshold, and the date; you check the count, the class, and the format, and flag disagreement with the reference table.

## Self-check

- [ ] Did you set one level for a whole project or a whole step? Levels live on step x task. Split the task and re-answer the four questions.
- [ ] Is a task at collaborator with no criteria file you can locate and date? Drop it to assistant.
- [ ] Is "read and catch errors" at collaborator or above? Downgrade it on purpose; this step's errors disguise themselves best.
- [ ] Does any `answers when wrong:` line read NOBODY while you are still proceeding? Stop, drop one level, hand back.
- [ ] Did you count the steps a demo covers? Count the steps it does not, and look up who answers when it's wrong.
- [ ] Did you write a name into `signed by:`, circle a cell, or pick a candidate? Undo it; those are the human's.
- [ ] Does the snapshot contradict the four questions for this task? The questions win; write the reason.

## Templates and briefs

- `templates/ladder-self-rating.md`: the step-by-level matrix with the four-question level table; fill two cells per step.
- `templates/seven-step-cards.md`: one card per step (produce, downstream, four answers, done criterion, send-back signal).
- `templates/five-premise-table.md`: the five premises, what fails first, and the compensation; fill before any ceiling is trusted.
- `templates/dispatch-brief.md`: the four-column brief with the `answers when wrong:` line; see `references/habits-and-dispatch.md`.
- `templates/three-process-questions.md`: the door card; install on the path, not the wall.
