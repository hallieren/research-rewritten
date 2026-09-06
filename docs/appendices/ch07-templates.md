# Chapter 7 templates · Minimal Harness Checklist + Ledger and Resume Patterns + "Have AI Audit the Harness" Prompt

> This appendix is the complete fillable version of the three tools in Chapter 7.
> The order of use is fixed. Build the skeleton on the patterns of Template 2 when you start, go through Template 1 item by item before you spend real money, and once the checklist is done, run a round of Template 3 before the pilot.

---

## Template 1 · Minimal Harness Checklist

**How to use.** Go through it item by item before you spend real money or real time for the first time. Every item matches a class of real accident from Chapter 7, and the bill for that accident was three hours and five bugs. The goal of this sheet is to make you pay only for the checking, never for the accident. Do not force a tick on an item you cannot pass. Fix it before you start, or write down the risk you are accepting.

**A Tracer bullet (mock, whole chain)**

- [ ] Is there a mock mode (fake model or fake data source) that runs the whole chain **offline**, load → call → extract → score → write to disk → summary report?
- [ ] Is the format of the mock output identical to a real run (the aggregation script eats mock data without errors)?
- [ ] After every change to the pipeline logic, has the mock regression been rerun? (it is your only free whole-chain test)

**B A crash is a lossless event (resume)**

- [ ] Does every result written to disk carry a unique key (the minimal tuple that fully rebuilds this call, such as task × configuration × seed)?
- [ ] Have you run the crash drill, kill the process midway, restart, and results come back **neither duplicated nor missing** (verified by counting lines and reconciling the ledger)?
- [ ] Are the tasks flattened into small independent pieces rather than one long serial chain? (a long chain's mid-state cannot be expressed as a key, the root of the crashes in Chapter 7, 7.1)
- [ ] Does a single task's failure go onto the failed list only, leaving the run alive, with resume retrying it naturally? (verified with your own eyes by planting a "poison pill" task)

**C The ledger (append-only + hard cap)**

- [ ] Does every external call (API / compute / human annotation) write one line to an append-only ledger, recording timestamp, target, usage and cost?
- [ ] Does the budget hard cap exist, and have you **seen it fire with your own eyes** (set the ceiling near zero and try one run, a fuse that has never blown is not a fuse)?
- [ ] Are the ledger and the result file separate, results can be cleaned and rerun, the ledger never edited?

**D Criteria and records**

- [ ] Is the commit timestamp of the criteria file (the Chapter 6 plan or preregistration) **earlier than** the first line of results?
- [ ] Does every change after the run starts go into an append-only change log (date, what changed, reason), with the locked criteria themselves untouched?
- [ ] Is the original answer text (the faithful extract) written to disk (not only the score), so that after a scorer bug fix all scoring can be replayed offline?

**E The pilot (the only test for a seam)**

- [ ] Is a pilot planned at 3-5% of the total budget, and before the full run?
- [ ] Have the pilot numbers been read by a human arm by arm and configuration by configuration, with the original answer text spot-checked behind every 0 and every perfect score?
- [ ] Have you asked the dedicated question, "**Does the strongest arm or configuration's performance make sense?**" (the theme sentence of Chapter 7, bugs zero out the strongest arm first. When the harness has bugs, the most likely bias in the readings is systematically wronging the strongest contestant)

**Self-check** (compare while you run the sheet):

- [ ] All tests green, so you skipped the pilot? Green only proves the code matches the world you defined. All five bugs lived on seams outside that definition (API contracts, dependency environments, data quirks).
- [ ] Was the checklist ticked after the full run finished? The accident it prevents has already happened, and what you need now is the interrogation checklist of Chapter 8.
- [ ] Is group B resting on "resume is supported in theory"? A resume that has never had a crash drill runs its drill during the first real crash.
- [ ] Taking "it is running" for "it is producing"? Logs, progress bars and the bill are all moving, and that does not make the numbers trustworthy. There is only one test, can every number point to the criteria, the ledger and the original answer text.

---

## Template 2 · Ledger and Resume Patterns

**How to use.** Three language-independent design patterns, each implementable in a few dozen lines. Copy the structure, not the code. Your key, your cost unit and your storage format are decided by your experiment. The three patterns together are the structural base for what Chapter 7 called "leaving errors nowhere to hide."

**Pattern 1, the resume key (idempotent writes)**

```text
key = (task family, item ID, arm/config, seed)   # the minimal tuple that uniquely rebuilds this call
result file = append-only JSONL, every line carries the full key + original answer text + score

At the start of a run:
  done = { keys of the lines already written }
  task pool = [ all combinations ] - done        # flat, unordered, mutually independent
During the run:
  each piece finished → append to disk at once (with a write lock under concurrency)
  a piece fails → record it on the failed list and print, do not throw; resume retries it naturally
Effect:
  a crash mid-run = a lossless event, restart and continue, no rerun, no second payment
  a flat task pool unlocks concurrency for free (Chapter 7, serial full run ~15 hours → 32 lanes in one pass)
```

**Pattern 2, append-only ledger + budget hard cap**

```text
Immediately after every external call:
  ledger.append({ timestamp, model/resource, usage (tokens etc.), dollars, task metadata })
  if cumulative spend > hard cap: throw, abort the whole run

Discipline (more important than the code):
  the ledger is append-only, never edited. Results record the current understanding and can be corrected;
  the ledger records history, and history does not accept edits
  the result file is separate from the ledger, cleaning mislabeled result lines moves no ledger line
Dividend:
  "how much did the experiment cost" = the sum of a column, not an impression
  the basis promise of a cost-matched comparison (Chapter 6) is redeemed in this ledger
```

**Pattern 3, write the original answer text (the faithful extract) to disk, scoring stays replayable**

```text
what goes to disk is the original answer text (the faithful extract of the model's reply); the score is only a derived column
a scorer bug fixed → the replay script recomputes every score, at zero cash cost
  (the Chapter 7 case, fixing the % suffix bug and the numpy bug = change the scorer + replay, no second payment to the API)
generation and scoring are orthogonal. The same original answer text gets reviewed again and again by
  the interrogation of Chapter 8 and the red team of Chapter 10. An experiment that stored no original text has no evidence to overturn anything later
```

**Self-check**:

- [ ] Did the key design miss a dimension (the seed, say)? Resume will "skip" combinations that never ran, and the gap is silent. Verify with the crash drill, not with your eyes.
- [ ] Is the ledger accumulating in memory and written to disk once at the end? A crash loses the account, and the hard cap goes with it. Write every entry at once.
- [ ] Stored only the scores and not the original answer text? Every scorer bug then costs the full amount again, and the audit of Chapter 8 has nowhere to start.

---

## Template 3 · "Have AI Audit the Harness" Prompt

**How to use.** Hand the harness's core code to an AI session that **did not help write it** for audit. The session that wrote the harness is blind to its own assumptions, and changing the session changes the viewpoint. This is the executable version of Chapter 2's principle that generation and verification are orthogonal. The output is a list of leads, not a verdict. Every finding comes with a minimal verification experiment, and you rule only after running them one by one. Use it before the pilot, so the most expensive bugs die before the money is spent.

```text
This is the core code of my experiment harness:

[paste: model/service calls, answer extraction, scoring, writing to disk, the ledger module]

This is the test plan it has to implement (the criteria part):

[paste: the arm design, the basis and the criteria of the Chapter 6 plan]

Your job is to find the ways this harness "quietly produces wrong numbers,"
not to improve its code style. Work through four seams one by one:

1 The code ↔ API seam. For each model or service, check the code's
  assumptions against its real API contract. Will parameter names and values be refused (a reasoning
  model refusing a custom temperature), truncation behavior, null or empty returns, non-JSON responses, rate limits and retries.
2 The scorer ↔ data seam. Pull 10 real samples from the task data and walk the
  scoring logic by hand. Do format variants (units, % suffixes, thousands commas, capitalization, multiple lines)
  score a correct answer wrong? Is the "tidiest" way of writing a correct answer exactly
  the parser's most fragile path?
3 The grader ↔ environment seam. The libraries, subprocesses and timeouts the grading depends on, do they
  install fully and run in a clean environment? When a dependency is missing, does it error, or quietly record 0?
4 The harness ↔ criteria seam. Compare the basis the code implements against the basis the plan locked in, item by item.
  Sample size, slices, seeds, repeat counts, cost formula, where do they quietly disagree?

For each finding, output three parts:
the seam's location → the worst consequence (which arm or configuration's numbers get contaminated first, and in which direction)
→ one minimal experiment that verifies it on the spot (one command or one sample).

Finally answer this. If only one 20-problem pilot is allowed,
which three numbers are most worth checking by hand? Why those?
```

**Self-check** (run through it when you use the audit output):

- [ ] AI says "no serious problems found"? Do not take it as a safety certificate. All five bugs of Chapter 7 came out of a harness AI helped write deeply, with 19 tests all green, and every one was the kind it does not flag. When the audit comes back empty, the checklist of Template 1 gets run all the same.
- [ ] Audited the code only, without giving it the API docs and real data samples? The most expensive bugs are not in the code, they are on the seam between the code and the world (where bugs one, three and five are registered). Feed it nothing from the world's side and it audits the world you defined.
- [ ] Is the audit session the same as the writing session? It will defend its own assumptions. Change the session, and preferably the model.
- [ ] Were the problems the audit found fixed in code only, never entered in the change log? A fix that touches a difference between the plan and reality (an API refusing a preregistered decoding parameter, say) is disposed of the way Chapter 7's pillar four does it. The harness obeys reality, the difference is appended to the change log, and the locked criteria do not move.
- [ ] Did the findings list skip the minimal verification experiment on each item? An AI audit also produces false positives. Leads have to be verified, and the code it writes has to be piloted, one and the same discipline.
