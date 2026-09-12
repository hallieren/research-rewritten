**Load this reference when:** you are building or running a pipeline, harness, backtest, eval script, or batch experiment, and before any run that spends money or time.
Source: chapter 7 (docs/chapters/ch07.md, docs/appendices/ch07-templates.md).

## Contents

- Rules
- Procedure: build and accept the harness
- The five pillars
- The five seam classes
- Decision and vocabulary
- Self-check
- Templates and briefs

## Rules

1. Credibility comes from the structure of the harness, and the structure leaves errors nowhere to hide. "Looks right" is aesthetic; your code almost always looks right. "Cannot hide" is structural: a crash loses nothing, every dollar has a line, the criteria cannot be edited, scoring can be replayed.
2. Green tests prove the code matches the world you defined. Seam bugs (API contracts, environments, data quirks) live outside that world. The pilot is the only probe that reaches the world's side.
3. Bugs zero out the strongest arm first. The strongest arm has the most special contract, burns the most tokens, answers in the tidiest format, and depends on the heaviest grader. An uncaught harness bug most likely wrongs the strongest contestant, which produces the "weak beats strong" result the user wants most. A bug that chews an arm to zero screams; a bug that chews off 3 points (illustrative) says nothing and still flips a verdict.
4. Pilot before the full run (rule), at 3 to 5% of the total budget (illustrative). Read the numbers arm by arm and configuration by configuration, and ask the dedicated question: does the strongest arm's performance make sense?
5. Results record the current understanding and may be cleaned and rerun. The ledger records history, and history does not accept edits. The two files are separate.
6. The harness implements the plan; it never revises it. Every difference between plan and reality (an API refusing a preregistered parameter, a token ceiling raised) goes to the change log with date, what, why. The plan file does not move. "Just this once" has no stopping condition; the change log does.
7. "When do you stop tuning" is agreed in advance. Any further failure of a component after the agreed point is reported as a property of that component, not patched.
8. Raw answers on disk; the score is a derived column. A scorer fix is a replay at zero cost. An experiment that stored no original text has no evidence to overturn anything later.
9. The harness audit runs in a session that did not help write the harness. The writing session defends its own assumptions. Audit output is a list of leads with a minimal check each, not a verdict.
10. Any command error: stop and show the output. A pipeline that logs, scrolls, and bills is working in appearance only; the test is whether every number points to the criteria, the ledger, and the original answer text.

## Procedure: build and accept the harness

Budget half a day (illustrative). Input: the timestamped plan. Output: the six-line acceptance, each ticked with evidence, and a pilot read arm by arm.

1. Build the skeleton on the pillar patterns from `templates/harness-checklist.md`: flat independent tasks, resume key, append-only ledger with a hard cap, mock mode, raw answers to disk. Lines that touch the scoring function, the ledger's cost formula, and the resume key get read by the human word by word; boilerplate (retries, argument parsing, disk writes) gets a glance.
2. Fire the mock tracer bullet. A fake model or data source walks load, call, extract, score, write, aggregate offline. The aggregation eats mock output without error. Rerun mock after every logic change; it is the free regression.
3. Crash drill. Kill a run midway, restart, count lines, reconcile the ledger. Results neither duplicated nor missing, or add the resume key before spending.
4. Blow the fuse. Set the hard cap near zero, run, watch it abort, restore the cap. A fuse that has never blown is not a fuse. Use `python scripts/ledger.py init <ledger> --cap <x> --unit <unit>` and confirm `LEDGER: CAP EXCEEDED` appears.
5. Check timestamps. `python scripts/prereg_check.py timing <plan> --results <first results file>` must print `PREREG: locked before results`. Anything else routes back to the test plan.
6. Plant a poison pill. Drop in a task that must fail; confirm it lands on the failed list only and the run stays alive.
7. Dispatch the harness audit through a separate session with `briefs/harness-audit.md`: the core code, the API docs, and real data samples, never the human's expectations. Run each returned minimal check. Fixes that touch a plan-versus-reality difference go to the change log.
8. Pilot at 3 to 5% of budget (illustrative). The human reads the numbers arm by arm, spot-checks the original answer text behind every 0 and every perfect score, and answers "does the strongest arm's performance make sense". Any probe-based selection rule locked in the plan executes now, with readings and choice logged.
9. Tick the six-line acceptance with evidence, then run mock regression once more, then the full run. The human signs the acceptance.

## The five pillars

| Pillar | What it does | Discipline |
|---|---|---|
| 1 Resume key | Every result line carries the minimal tuple that rebuilds it (task family, item, arm, seed). A run starts by striking finished keys from the pool. | Tasks flattened into small independent pieces; a single failure goes to the failed list and never takes down the run; a crash becomes a lossless event |
| 2 Append-only ledger with a hard cap | Every external call appends one line (timestamp, target, usage, cost). Cumulative spend past the cap throws and stops the run. | Never edited; written at once per entry, never batched in memory; cost is the sum of a column, not a recollection |
| 3 Mock mode | A fake model or data source walks the whole chain offline. | Tracer bullet first, regression after every change; mock cannot clear seam bugs |
| 4 Criteria in the repo ahead of results | The plan's commit precedes the first result line. | The harness implements the plan, never revises it; differences go to the change log |
| 5 Raw answers to disk | The extracted original answer text is stored; the score is derived. | Scorer fixes replay for free; the same text is reviewed again at interrogation and red team |

The resume key in two lines:

```python
done = {(r["family"], r["item_id"], r["arm"], r["seed"]) for r in results}
jobs = [j for j in all_jobs if key(j) not in done]
```

A key missing a dimension (the seed, say) makes resume skip combinations that never ran, silently. Verify with the crash drill, not by reading.

Non-coder translation (same pillars, different material; interviews, questionnaires, archives, report checks):

| Pillar | Non-code form |
|---|---|
| Resume key | Number each finished minimal unit (one interview, one document); resume from the number, redo nothing, miss nothing |
| Ledger with a cap | Money and hours on a sheet that only grows; a ceiling set before starting; stop at the line |
| Mock mode | Walk the whole process on one set of fake material before touching real material; walk it again after every process change |
| Criteria ahead of results | A timestamped email or a version-history document; later changes append, never overwrite |
| Raw records to disk | Keep recordings, source excerpts, screenshots; derive coding and scoring from them; recompute instead of collecting again |

## The five seam classes

Bugs that green tests cannot reach. Each has a symptom and a preferred victim.

| Seam | Symptom | Who zeroes out first |
|---|---|---|
| Plan and API contract | A preregistered parameter refused (a reasoning model rejecting a custom temperature, a renamed token-limit field); a 400 error | The strongest arm; not one problem runs |
| Token budget and reasoning model | Thinking truncated, content returned null, the harness crashes on a null string | The strongest reasoning member |
| Provider and client | Status 200 with a non-JSON body; parsing blows up | Whoever it hits; the only random landing point |
| Scorer and data | Correct answers in a format variant (a % suffix, units, thousands commas, capitalization, multiple lines) parsed as failures and scored 0 | The arm with the tidiest answers |
| Grader and runtime environment | A missing dependency; the grader records 0 for every item in every arm without an error | Every arm on the affected task set |

The audit prompt walks four of these as seams to probe (code and API, scorer and data, grader and environment, harness and criteria) and asks which three pilot numbers deserve a hand check.

## Decision and vocabulary

The six-item acceptance. Each line ticked with evidence, or the run does not start:

| Item | Evidence |
|---|---|
| Mock walks the whole chain | Mock output aggregated without error |
| Crash drill: results neither duplicated nor missing | Line count and ledger reconciliation after kill and restart |
| The fuse was blown on purpose | `LEDGER: CAP EXCEEDED` observed, cap restored |
| The criteria commit is earlier than the first result | `PREREG: locked before results` |
| A poison pill lands on the failed list only | The failed list holds it; the run finished |
| Pilot at 3 to 5% of budget read arm by arm | The strongest-arm question answered by the human; zeros and perfect scores spot-checked against original text |

| Situation | Verdict |
|---|---|
| "Tests are all green, skip the pilot" | Green proves the defined world; pilot anyway |
| The strongest arm scores 0 or near it | Harness bug until proven otherwise; stop, pull original answers |
| A plan assumption rejected by reality | Harness obeys reality; change log gets the entry; plan untouched |
| A mislabeled batch of result lines | Delete and rerun the result lines; ledger lines never move |
| A component keeps timing out after the agreed ceiling | Report as a property of the component; no more patching |
| Audit returns "no serious problems" | Not a certificate; run the checklist regardless |
| Any command errors | Stop; show the output |

## Self-check

- [ ] Did you accept the harness on green tests without a pilot? Seam bugs are outside the tests; pilot at 3 to 5% (illustrative) first.
- [ ] Did you read pilot totals instead of arm by arm? Read per arm, spot-check zeros and perfect scores, ask whether the strongest arm makes sense.
- [ ] Did you fix the plan file to match reality? Revert; append the difference to the change log.
- [ ] Did you edit or delete a ledger line while cleaning results? Restore it; only result lines are cleaned.
- [ ] Did the audit run in the session that wrote the harness, or without API docs and real samples? Void; re-dispatch with `briefs/harness-audit.md` and the world's side included.
- [ ] Is the ledger accumulating in memory for a single write at the end? A crash loses the account and the cap with it; write per entry.
- [ ] Did you keep tuning a component past the agreed stopping point? Stop; report the failure as a property.

## Templates and briefs

- `templates/harness-checklist.md`: groups A to E (tracer bullet, resume, ledger, criteria and records, pilot) plus the three design patterns.
- `briefs/harness-audit.md`: the four-seam audit prompt for a session that did not write the harness (VERIFICATION).
- `scripts/ledger.py`: `init`, `record`, `sum`, `check`; append-only, hash-chained, the cap fires with exit 2.
- `scripts/prereg_check.py timing`: the criteria-before-results check between the plan file and the first results file.
