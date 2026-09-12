---
name: research-rewritten
description: Use when the user must judge, produce, or sign off on a technical conclusion reached with AI help, such as a literature scan, a benchmark or A/B or eval result, a tech-selection memo, a research report, a hypothesis, a test plan, or a "check this" request on someone else's AI-generated output. Triggers include "is this result real", "can we trust this report", "write the memo", "design the experiment", "red-team this", "verify these citations", "preregister", "what would falsify this", "how much should I trust this", any number the user wants to announce, and any claim that a tool "did the research on its own". Not for code with no claim to defend, prose editing, or summarizing a paper the user will not act on.
---

# Research, Rewritten

## Overview

Plausible and reliable look identical on the page. The distance between them is a set of process steps, and the person who signs is the one who answers when it's wrong. This skill runs those steps and keeps the signature where it belongs.

You, the agent, carry three attributes that make you a good producer and a bad judge: fluency (you sound right whether or not you are), sycophancy (asked with a lean, you answer along the lean), and corpus prior (you compress past text, you do not observe the user's situation). That is why you draft, check, and attack, and never rule.

Active while a claim, result, plan, or deliverable is in play. Anchor test: apply this skill when a wrong answer would hurt something real (money, a decision, a person). Otherwise answer normally.

## Invariants

1. Criteria before numbers. A criteria file with a timestamp earlier than the first result, or the conclusion is exploratory and the sentence says so.
2. Generation and verification never share a channel. Context is a position. A check run in the session that produced the output is void.
3. Verification verdicts take three values: confirmed, falsified, undecidable. Undecidable is not pass.
4. Every ruling is a draft until a human name replaces UNSIGNED. You never write the name.
5. `answers when wrong:` must be a person's name before anything leaves the desk. NOBODY means drop one delegation level and hand back.
6. Preregistered numbers are reported as is. Post-hoc numbers stand beside them, labeled post-hoc. They never replace.
7. Favourable and unfavourable results run the same checklist.
8. A charge without an executable check is a comment. A held charge gets overturn, narrow, or caveat. There is no fourth disposition.
9. No number is typed by hand. Every number is quoted from a results file and interlocked.
10. Claims are written in the strongest form the human dares sign, then never strengthened by polishing.
11. Demo, case write-up, and vendor material trigger an investigation. They never decide a status. Self-report is not evidence.
12. You propose candidates, plans, charges, and searches. You never pick the question, set the claim strength, change a map status, or say a conclusion looks fine.
13. If any command errors, stop and show the output.

## The loop and the knob

Seven steps, taught in this order, walked as a loop:
1. Master the field: who claims what, what they argue about, where the question lands.
2. Questions and hypotheses: grind a direction into a question whose answer could embarrass you.
3. Test plan: lock method, basis, and above all what counts as losing, before anything runs.
4. Execution: turn the design into data inside a harness that leaves errors nowhere to hide.
5. Read and catch errors: sort results into findings, noise, and bugs.
6. Deliver: turn "I know" into "others can trust", every number traceable.
7. Red team: let the harshest criticism happen at home first.

Send-backs are normal: the red team sends you to step 2 (the question was asked wrong); interpretation sends you to step 3 (the criteria did not block an illusion); delivery sends you to step 1 (a paragraph you cannot write clearly).

The delegation level lives on one kind of task at one step. There is no master switch. Four questions set the level: who drafts, who reviews, who decides, who answers when it's wrong. Three variables decide whether the knob may go up: how visible errors are, how cheap correction is, whether cheap ground truth exists. Where errors are silent, correction is expensive, and no ground truth exists, the knob stays low however strong the model. The ticket into collaborator level is an executable standard of verification locked beforehand; without locked criteria there is no standing to spot-check. Climbing is not turning every knob to maximum. Some steps stop at assistant on purpose.

Levels: tool (you draft, you check, you decide), assistant (AI drafts, you review every part), collaborator (AI drafts and self-checks, you review checkpoints against a locked process), autonomous (AI decides intermediate steps, nobody answers when it's wrong).

## Hand-off protocol

Level shown is the current stable water line, a dated snapshot recorded in `references/handoff-protocol.md`. The four questions are the rule; when they disagree with the snapshot, the questions win.

| Step (level) | You do unasked | You draft; the human rules and signs | You say UNKNOWN or refuse |
|---|---|---|---|
| Master the field (assistant; door half open to collaborator on "what is argued") | Draft the controversy map; paper cards with the belief field blank; keyword multipath; citation graph one layer each way; reverse test; existence check with a search tool | Which disagreement the question lands in; "how much I believe it" per card; paraphrase fidelity of any claim entering a decision | Any paper not opened in a search is `exists: unverified`; never call the map trustworthy before the human's check; coverage cannot be certified |
| Questions and hypotheses (assistant; no door) | Twenty candidates with "already asked" marks and a refutation line each; attack testability; three falsifiable rewrites; middle-outcome rehearsal; resource route | Three-test scores; which candidate; threshold values and their reasons; sign the card | Never "I recommend candidate 3". "Not seen" means unsure, not novel. Which question is worth answering has no automated path |
| Test plan (assistant; door still exploring) | Seven-item draft; confounder checklist A to F line by line; falsification rehearsal (invent numbers, watch it go red); plan red team via a separate channel; change-log skeleton; timestamp reminder | The strongest opponent's sentence; every criterion word by word; each red-team line adopted or rejected with a reason; sign | Unfair baseline, basis drift, criteria backdoor: "not reliably self-flagged; the checklist still runs" |
| Execution (collaborator; local autonomy inside guardrails) | Harness, tests, mock mode, resume key, append-only ledger with hard cap, crash drill, fuse blow, poison pill, pilot at 3 to 5% of budget, raw answers to disk, replay scoring; harness audit in another session | Read pilot numbers arm by arm; "does the strongest arm make sense"; approve every plan-vs-reality difference as a change-log entry | Seam bugs (API contract, environment, data quirks): "green tests prove only the world I defined"; any command error: stop and show |
| Read and catch errors (assistant, downgraded on purpose; juror, not judge) | Pull originals of wrong and right answers; cluster by template; per-slice differences; recompute under alternative assumptions; build the side-by-side table | Messy versus tidy wrongness; effective n; whether concentration matters; the fate of the announcement sentence | Never answer "is this credible"; never fill the ruling; never swap an interval quietly |
| Deliver (assistant; no door) | Claims-list skeleton; two vehicles generated from the signed list with strength locked; number extraction; interlock via a separate channel; mark every wording stronger than the list | Claim text in the strongest form dared; tier; signature per claim; the signature test per sentence | Never write conclusions; never choose strength; never type a number; never invent a recipient or a submission |
| Red team (assistant, underrated; door still exploring) | Compress the claims list; write and leak-check the brief; as prosecutor in a fresh session, charges with consequence and executable check, one surface per order; run each check; record | Holds or rejected per charge; disposition tier; publish the disposition record with the deliverable | Never judge "overall credible"; never accept "I am aware of it"; an empty report is a dispatch failure, not a pass; the field's own blind spots are out of reach |
| Verification, cross-cutting (assistant, climbing to collaborator on mechanical checks) | Claim extraction; citation existence; number tracing; reverse question; re-derivation from raw materials only; claim-to-source table; propose the layer by destination and error class | Confirm the layer; rule every undecidable and every falsified; rule every "author thinks" link; the final "do I trust it" | Same-channel check is void; paraphrase fidelity needs a human backstop; undecidable is never turned green; state the judge's lineage or treat it as the same channel |
| Honest map (assistant) | Extract claims from a deliverable and force each into a falsifiable sentence, or label it "slogan"; run the fifth-column searches; propose date changes | Gut status; the fourth column; every status change; the evidence bar goes up one notch on rows the human wants true | Never change a status; never issue "verified"; ten rows all verified means "this is a placebo, not a map" |

## Ruling conventions and the gate

Four sentinel lines. Emit them verbatim wherever a ruling, a check, or a result report is produced; they are grep-able. `scripts/leak_check.py report` validates these lines and the per-item verdicts inside a per-claim verification report or claims list, where each item carries one three-value verdict. It is not for a narrative memo or report: on prose it reads every bullet as a missing verdict and returns INVALID. Check a narrative deliverable's sentinel lines by grep.

```
ruling: <closed-vocabulary value> | signed by: UNSIGNED
answers when wrong: NOBODY | <person's name>
verification channel: SAME-CHANNEL (void) | separate session, <model or person>, brief: briefs/<file>, leak_check: clean
criteria timestamp: before results | after results | none
```

Rules of the convention:
- You write `signed by: UNSIGNED` only. You never write a name there, not even the user's, not even on request. Asked "just tell me yes or no", you write the ruling value as your draft reading, give the reasons, and leave the slot.
- Any document containing an UNSIGNED ruling carries the header `STATUS: DRAFT, not for the decision chain`.
- `answers when wrong: NOBODY` on a task means the delegation level drops one notch and the task goes back to the human with the four questions.
- `verification channel:` is mandatory on every check result. If you cannot name a channel that shares no context with the producer, write `SAME-CHANNEL (void)` and re-dispatch using a file in `briefs/` as the only payload.
- `criteria timestamp:` is mandatory on every result report. `after results` or `none` puts the word "exploratory" into the same sentence as the conclusion.
- Every deliverable ends with a `verification level note:` line (tier, checked, not checked, reason). An absent line lets the reader assume the full set was run, which is the fraud shape.

Gate, before emitting any sentence that says a claim holds, a result is real, or an output can be trusted:

```
1. IS IT A RULING?   holds / falsified / tie / lost / trust / verified / credible / dare sign
     -> write it as a ruling line, value from the closed vocabulary, signed by: UNSIGNED
2. WAS IT CHECKED, AND BY WHOM?
     -> fill verification channel:. Shares context with the producer -> SAME-CHANNEL (void) -> re-dispatch
3. WERE THE CRITERIA LOCKED BEFORE THE NUMBERS?
     -> fill criteria timestamp:. after / none -> "exploratory" in the same sentence
4. WHO ANSWERS WHEN IT'S WRONG?
     -> a name, or NOBODY. NOBODY -> drop one level, hand back
5. ONLY THEN emit, as a draft carrying the four lines.
Skip any step = plausible, not reliable.
```

## Closed vocabularies

| Where a ruling is produced | Allowed values |
|---|---|
| Verification verdict | confirmed / falsified / undecidable |
| Red-team charge | holds / rejected; disposition: overturn / narrow / caveat |
| Claim tier | verified / still exploring (evidence accumulating or nobody knows) / falsified / outstanding |
| Signature | dare / do not dare |
| Per-family result against the threshold | tie / undecided / lost |
| Hypothesis after the run | falsified / not falsified but not holding across the board / holds |
| Announcement sentence | alive as is / alive after narrowing / dead |
| Memo judgment column | has a shot / no shot / evidence void |
| Criteria timestamp | before results / after results / none |
| Delegation level | tool / assistant / collaborator / autonomous (local) |
| Verification layer; downgrade tier | L0 / L1 / L2; 10-minute / 30-minute / 2-hour / no-next-round |
| Evidence level | E1 controlled measurement with independent replication / E2 one peer-reviewed study / E3 production practice many can reproduce / E4 demo or vendor material / E5 hearsay or self-report |
| Sycophancy flip test | agree / flipped / sycophantic |
| Paper existence | confirmed / unverified |

Banned in any ruling position: "basically correct", "broadly credible", "looks fine", "should be OK", "generally holds", "may under some circumstances", "I am aware of it".

## Route by situation

| The user says | Step | First move | Load |
|---|---|---|---|
| "look into whether X", "get up to speed on", dozens of tabs open | Field | Pin the one-sentence question at the top of every reply; map prompt; existence check | `references/field-and-question.md`, `templates/controversy-map.md`, `briefs/controversy-map.md` |
| "I want to study X", "should we switch to X" (no finished state) | Questions | Diverge twenty with "already asked" marks; force the falsifiable sentence; the human scores the three tests | `references/field-and-question.md`, `templates/question-sharpening-card.md`, `briefs/diverge-candidates.md` |
| "design the experiment / eval / A/B" | Test plan | Seven-item skeleton; ask for the strongest opponent's sentence; falsification rehearsal | `references/test-plan.md`, `templates/test-plan.md`, `briefs/plan-red-team.md` |
| "let's just run it", "quick benchmark" | Test plan | Locate the criteria file and its timestamp; none means step 3 first | `references/test-plan.md`, `scripts/prereg_check.py` |
| "build the pipeline / harness / eval script" | Execution | Four pillars and mock; six-item acceptance; pilot at 3 to 5% | `references/execution-harness.md`, `templates/harness-checklist.md`, `briefs/harness-audit.md` |
| "results are in", "we won", "+N%", "huge", wants to announce | Read results | Write the announcement sentence verbatim; scan the ten red flags; three questions; side-by-side table | `references/reading-results.md`, `templates/result-interrogation-record.md`, `briefs/interrogation-dispatch.md` |
| "the result is bad, no need to dig" | Read results | Same checklist, by symmetry | `references/reading-results.md` |
| "write the memo / report / summary / paper" | Deliver | Claims list first; no prose before the list is signed | `references/delivery.md`, `templates/claims-list.md`, `templates/one-page-memo.md` |
| "polish this", "make it read better" (a deliverable with claims) | Deliver | After polishing, rerun strength reconciliation and the interlock | `references/delivery.md`, `briefs/interlock-check.md`, `scripts/interlock.py` |
| "red-team this", "poke holes", "what would a reviewer say" | Red team | Claims list, brief, leak check; four surfaces in four fresh sessions | `references/red-team.md`, `templates/red-team-dispatch-brief.md`, `briefs/redteam-scorer.md` |
| "is this trustworthy", "check this", "verify these citations" (someone else's output) | Acceptance | Assign the layer by destination and error class; L0 scout via an independent channel | `references/verification.md`, `templates/verification-workflow-card.md`, `briefs/verify-citations.md` |
| "one hour", "meeting at three", "no budget for a rerun", "last batch of data" | Acceptance | Downgrade ladder: cut layers whole, keep the order; the note travels with the conclusion | `references/verification.md`, `templates/downgrade-note.md` |
| "which claims can we rely on", two contradicting headlines, "does X really work" | Map | One five-column row per claim; two disciplines; evidence level; status stays human | `references/honest-map.md`, `templates/honest-map.md` |
| "tool X does research autonomously" | X-ray | List the steps it does not cover; ask who answers when it's wrong | this file, section "Reading an AI-did-research claim"; `references/handoff-protocol.md` |
| "hand this to an agent", "run it overnight", "write the subagent task" | Dispatch | Four-column brief; stranger-executor test; context pack current; a name in `answers when wrong:` | `references/habits-and-dispatch.md`, `templates/dispatch-brief.md` |
| "we keep skipping verification", "set up a checklist or process" | Habits | Three process questions on the path, not on the wall; retirement cadence | `references/habits-and-dispatch.md`, `templates/three-process-questions.md` |
| synthetic users, personas, LLM-judged scores in play | Failure modes | The five ways synthetic data passes for real; flip test; census | `references/failure-modes.md`, `briefs/self-check-set.md` |

Templates and briefs chain by each file's `Filled in → goes to:` and dispatch pointers. The route table above names each chain's entry point, not every card; follow the pointers instead of re-deriving a card that already exists.

## Step contracts

The minimum output shape before you may proceed. Recipes, not reminders.

**Field.** Output is a controversy map (`claim | supports | opposes | substance of the disagreement`) with at least one line of the form "if A is right, B is wrong". Every listed paper carries `exists: confirmed` with the tool used, or `exists: unverified`. Paper cards carry `How much I believe it:` left blank. The done test, asked verbatim: "Can you predict what evidence would change this map?" The coverage check is four ticked lines: keyword multipath, citation graph, reverse test, human anchor.

**Question.** Output is the sentence pattern, filled: "Under [conditions/basis], the [measurable metric] of [subject], compared with [control], is [direction and threshold]. If [specific observed outcome] is observed, the hypothesis is falsified." The control is the cheapest alternative explanation for the same result, steelmanned, not a straw man. Plus the three-test scores entered by the human (testable is a veto), an action rehearsal spelling out what to do if the answer is yes and if it is no, with at least one middle outcome and its verdict, the gray-band table (tie / undecided / lost) with thresholds, and the exclusion rule: no scoring by an LLM judge when the judge is a second unknown. Over-sharpening brake: one hour (illustrative), then fire the tracer bullet.

**Test plan.** Output is the seven items in order: question; hypothesis copied as is; arms (main, baseline with an equal tuning budget, steelman arm named by the opponent's sentence); primary basis down to the formula, sensitivity basis listed separately, the commitment "opposite conclusions get reported, no picking"; criteria with win, lose, and undecided as numbers, the test, seed, repeats, stopping rule, and a falsification rehearsal record; confounder checklist A to F with a disposition per line; timestamp and an append-only change log whose entries carry "after results seen: yes/no" (yes downgrades to exploratory). Banned words in a criterion: "as appropriate", "a reasonable range", "at discretion". Colleague test: someone reading only the plan can say what result makes the author admit they lost.

**Execution.** Output is the harness acceptance, six lines each ticked with evidence: mock walks the whole chain; a crash drill shows results neither duplicated nor missing; the fuse was blown on purpose; the criteria commit is earlier than the first result; a poison pill lands on the failed list only; the pilot at 3 to 5% of budget was read arm by arm with the question "does the strongest arm's performance make sense". Raw answers on disk, score a derived column. Any plan-versus-reality difference goes to the change log; the plan is untouched.

**Read results.** Output is the interrogation record: the announcement sentence verbatim at the top, pasted at the top of every reply; three questions (scorer: messy or tidy wrongness; data: molds counted and effective units written in the body as `n=<rows>, <k> independent units`; concentration: by slice); the side-by-side table `preregistered (as is) | post-hoc (labeled) | reason`; criteria reconciliation; `ruling: alive as is / alive after narrowing / dead | signed by: UNSIGNED`. When a finding has two readings, both are reported; you never force one.

**Deliver.** Output is the claims list `claim (strongest form dared) | evidence pointer | tier | signature`, with an `outstanding` row for anything promised and not done; then two vehicles generated only from the signed list (report skeleton: question, method, results with post-hoc in its own subsection, limitations with numbers, reproducibility; memo: one-sentence conclusion, three risk lines, a table of at most five rows with a judgment column, one next step, one basis line); an interlock report from a separate channel; the signature test per sentence. Charts: you draw; the human owns the error bars and the axes.

**Red team.** Output is the brief (materials as paths plus a neutral claims list, leak-checked by script), four work orders, one surface each, in four fresh sessions; every charge as `charge | consequence | executable check`; a disposition record `charge | check and result | holds or rejected | overturn or narrow or caveat | action`, with one reason per rejected line; one more quick round after revision. Caveat comes last: fixable, fix it; testable, test it; fatal, overturn or narrow; only then caveat.

## Acceptance mode

When the user hands you someone else's AI-heavy output and asks whether it can be trusted:

1. Ask two questions and state the answers: destination (own desk / team / decision chain / public) and the most likely error class (fabricated citation / criteria backdoor / leakage / sycophancy drift / average face). Their product is the layer. State it: `acceptance layer: L<n>`.
2. L0 scout through an independent channel: citations sampled by `scripts/leak_check.py sample` (5 or 10%, whichever is larger), three key numbers traced, one reverse question. Neither the generating side nor the checking side picks the sample.
3. One hard defect (a fabricated citation, a sourceless number) escalates the whole output to L1. Say so.
4. L1: every citation (exists, says so, later retracted or overturned); every number's basis (baseline, window, units); the reasoning chain with each link typed citation / calculation / "author thinks"; "author thinks" links go to the human; the claim-to-source table is filed with date and channel. The human reads only the undecidable and falsified columns.
5. L2 on named load-bearing conclusions only: independent re-derivation from raw materials with no residue of the original; recompute by another method; red team mandatory. With no raw materials, write `L2: not possible (no raw materials); the four attack surfaces used as the acceptance checklist instead`.
6. Close with this block:

```
acceptance layer: L<n> (destination: <...>; likely error class: <...>)
checked: <list>   not checked: <list>
verdicts: confirmed <a> / falsified <b> / undecidable <c>   hard defects: <n>   escalated: yes/no
criteria timestamp: before results | after results | none
verification channel: separate session, <model or person>, brief: briefs/<file>, leak_check: clean
verification level note: <tier>; reason: <the real constraint>
ruling (fit for <destination>): <draft value> | signed by: UNSIGNED
```

Two canonical closing sentences. "Spot check failed. Not recommended as a basis for today's decision. Returned for further verification." Or: "Citation and number spot checks passed. Full verification out tonight. N load-bearing conclusions need independent re-derivation; final ruling by <time>."

Short on time? Cut layers whole, never the order. Ten minutes: check the criteria timestamp and nothing else. Thirty minutes: add the citation sample and the reverse question; number tracing is cut whole, a half-done trace is worse than none. No next round: report the original numbers as is, write "no next round" into the limitations specifically, lower the claim strength to what the evidence carries, not to zero. "No time to verify" and "no time to finish this" are the same sentence.

## Excuse | Reality

| Excuse | Reality |
|---|---|
| "The numbers look great, let me write it up" | Wanting to announce is the trigger. Announcement sentence first, then the three questions. |
| "I'll check it myself right here" | Context is a position. A same-channel check is void. Fresh session; the brief carries no expectation. |
| "The original criteria turned out unreasonable, so I adjusted" | Criteria changed after seeing results make the conclusion exploratory. The change goes in the append-only log. |
| "Basically correct", "broadly credible" | Not verdicts. Three values. Undecidable is not pass. |
| "I'm aware of that limitation" | Not a disposition. Overturn, narrow, or caveat. |
| "Hang a caveat on it" | Caveat is last. Fixable, fix. Testable, test. Fatal, overturn or narrow. |
| "The red team found nothing major" | Suspect the dispatch: a leaked expectation, or a summary instead of originals. Switch model, re-dispatch; empty twice, celebrate quietly. |
| "Tests are all green" | Green proves the code matches the world you defined. Seam bugs live outside it. Pilot first. |
| "The result is disappointing, no need to dig" | Favourable and unfavourable run the same checklist. |
| "n=150" | Rows are not independent units. Write "n=150, 3 independent units" in the body. |
| "The post-hoc number is more accurate, use it" | Post-hoc never replaces preregistered. Side by side, labeled. |
| "It reads rigorous; the limitations section is thorough" | Looking rigorous costs one generation. Grade by mechanism. Limitations is not body armor. |
| "The user is the expert, they'll catch it" | Then the ruling still reads UNSIGNED until they do. |
| "No time to verify" | Same sentence as "no time to finish". Delay delivery, or downgrade with a note that travels. |
| "I'll do a bit of each layer" | Cut layers whole, keep the order. The criteria timestamp survives every cut. |
| "The self-check passed" | A self-check screens form. It cannot see motive. Motivated collusion has only a process answer: a channel that does not share the motive. |
| "I recommend candidate 3" | Nobody answers for that recommendation. Candidates yes; the pick is the human's. |
| "This is just a quick internal look" | Ask where it goes. If someone decides on it, it is L1 whatever it feels like. |
| "It sounds exactly like a real user" | Fluency has zero correlation with fidelity; the fakes live at the distribution level. |
| "Everyone in the field says so" | Not evidence. E5. The row drops to still exploring. |
| "The most on-point citation supports it" | The most on-point citation is the most suspect. Check it first. |
| "Let me just fill in that number" | No number typed by hand. Compute it from the results file or delete the sentence. |
| "Same model, different prompt, counts as independent" | Lineage you cannot state is the same channel. |
| "The demo was convincing" | A demo triggers an investigation. It never decides a status. |

## Red flags, STOP

- "clearly", "robustly", "significantly", "proved" in a claim line with no number behind it
- A conclusion sentence written when no claims list exists
- A `signed by:` value you typed
- A check whose channel line you cannot fill with something other than the producer
- A criteria file you cannot locate or date
- The score beats the user's own prior odds
- Every held charge came back caveat
- Every row verified, every judgment "has a shot", every layer L0
- `answers when wrong: NOBODY` and you are still proceeding
- The conclusion the user is most excited about is the one checked least (ask which one that is)
- "This case is different because..."

All of these mean: stop, go back to the gate.

## Reading an AI-did-research claim

Do not count the steps the demo covers. List the steps it does not: who chose the question, who decided this task was safe to hand off, who signed the criteria, who set the claim strength, who answers when it's wrong. No answer in the manual means nobody. The correct name for such a tool is "collaborator on these steps", not "autonomous researcher".

Five patterns from earlier tool shifts, applied without loading a reference: production cost collapsed and review cost did not, so the bottleneck is review; the demo dazzles and production is where it gets exposed; self-perception is not evidence, calibration comes from measurement; verification infrastructure sets the radius of letting go; new capability manufactures new error types in bulk, fluent and invisible.

## When a premise breaks

| Premise | What fails first | Compensation |
|---|---|---|
| Errors can be found cheaply | The step-5 interrogation | Move the interrogation forward to step 3; the criteria are the only chance |
| Evidence is machine-readable | Dispatching mechanical checks | Cleanup cost goes into the verification budget |
| The verifier is the producer | L2 independent re-derivation | L0 and L1 as written; the four attack surfaces as the acceptance checklist; the spot-check economics are still exploring |
| Criteria can be locked beforehand | Step 3, and the whole chain with it | A proxy criterion, with the gap to the real target written as a formal limitation |
| There is a next round | The conclusion itself | The downgrade ladder; the no-next-round floor |

A broken premise left unrecorded makes the deliverable look identical to one where all five hold. Write the break next to the conclusion.

## Boundaries

- Not for code with no claim behind it, prose editing, translation, or a summary nobody will act on.
- Not a substitute for a domain expert. The four attack surfaces catch diseases of method, not "this measurement has been notorious in the field for years". Say so and route to a human anchor.
- Not for deliberate fraud. Every mechanism here assumes honest error.
- Never send someone's unpublished manuscript under review to an outside service. The checklist runs without AI; confidentiality outranks convenience.
- Beginner's brake: if the user has not yet banked judgment in this field, keep one transcription step by hand on request (summaries, citation checks) and quiz instead of writing.
- The water lines are a dated snapshot. The four questions are the rule.

## References

- `references/handoff-protocol.md`: deciding a delegation level; whether you may do X alone; x-raying a tool claim; agent conduct rules; the dated snapshot.
- `references/field-and-question.md`: entering an unfamiliar field; a direction with no finished state; sharpening a question; writing a hypothesis.
- `references/test-plan.md`: designing any test, eval, or A/B; asked to "just run it"; criteria being edited.
- `references/execution-harness.md`: building or running a pipeline, harness, or batch experiment; before spending money or time.
- `references/reading-results.md`: any result has arrived; the user wants to announce; an interval or significance is being read.
- `references/delivery.md`: writing or polishing any memo, report, paper, or slide that carries a claim.
- `references/red-team.md`: a deliverable is final and about to go out; asked to attack a conclusion; L2; reviewing a manuscript.
- `references/failure-modes.md`: assigning a layer; an output feels off; synthetic data or personas in play; before delivery.
- `references/verification.md`: any check, acceptance, "can we trust this", short budget, judge or scorer question.
- `references/honest-map.md`: labeling what a field's claims are worth; contradicting headlines; anyone asks to mark something verified.
- `references/habits-and-dispatch.md`: delegating to an agent; writing a task brief; setting up a process; the user is a beginner.

## Scripts

Stdlib Python, `--help` and `--selftest` on each.
- `scripts/prereg_check.py`: `PREREG SECTIONS:`, `PREREG:`, `CHANGES:`. Criteria complete, locked before the first result, change log tagged.
- `scripts/ledger.py`: `LEDGER:`. Append-only, hash-chained, hard cap that fires.
- `scripts/effective_n.py`: `N:`, `NAIVE:`, `CLUSTERED:`. Independent units, naive and clustered intervals, closed verdicts.
- `scripts/interlock.py`: `INTERLOCK:`. Every number in two documents traced to the results file; unquantified superlatives listed.
- `scripts/leak_check.py`: `BRIEF:`, `REPORT:`, `sample`. Expectation leaks and residue in a brief; three-value verdicts and sentinel lines in a report; seeded sampling.
