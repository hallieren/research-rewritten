# Harness checklist

**How to use.** Go through it before spending real money or time for the first time; do not force a tick you cannot pass. Build on the three patterns (resume key, append-only ledger with a hard cap, raw answers on disk), then run the six-line acceptance with evidence per line. Hand the core code to a session that did not write it with briefs/harness-audit.md before the pilot. Green tests prove only the world you defined; seam bugs live outside it, and the pilot is the only test for a seam.

```text
Project: ____________   Harness commit: ____________   Date: ____________

A Tracer bullet (mock, whole chain)
☐ A mock mode runs the whole chain offline: load → call → extract → score → write → summary
☐ Mock output has the same format as a real run; the aggregation script eats it without errors
☐ The mock regression reran after the last change to pipeline logic

B A crash is a lossless event (resume)
☐ Every result line carries a unique key, the minimal tuple that rebuilds the call (task family, item id, arm or config, seed)
☐ Crash drill run: killed midway, restarted, results neither duplicated nor missing (line count reconciled with the ledger)
☐ Tasks flattened into small independent pieces, not one long serial chain
☐ A planted poison-pill task landed on the failed list only; the run stayed alive

C The ledger (append-only, hard cap)
☐ Every external call appends one line at once: timestamp, target, usage, cost; never held in memory until the end
☐ The hard cap exists and has been seen to fire (cap set near zero, one run attempted); a fuse that never blew is not a fuse
☐ Ledger and result file are separate; results can be cleaned and rerun, the ledger is never edited

D Criteria and records
☐ The criteria file's commit is earlier than the first result line
☐ Every change after the run starts goes to an append-only change log; the locked criteria are untouched; the harness obeys reality, the plan does not move
☐ The raw answer text is on disk; the score is a derived column, replayable after any scorer fix

E The pilot
☐ Pilot at 3 to 5% of budget (illustrative) before the full run
☐ Pilot numbers read by a human arm by arm; raw text spot-checked behind every 0 and every perfect score
☐ Asked verbatim: "Does the strongest arm's performance make sense?" (bugs zero out the strongest arm first)

Acceptance (six lines, evidence each): mock walks the chain: ____  crash drill: ____  fuse blown: ____
criteria commit before first result: ____  poison pill on failed list only: ____  pilot read arm by arm: ____
Risk accepted without a tick (written, not implied): ____________
Signature: ____________ (must be a human)
```

Machine check: `python scripts/ledger.py check <ledger>` (intact chain, cap fires) and `python scripts/prereg_check.py timing <criteria file> --results <results file>` (criteria locked before the first result).

### Self-check
- [ ] Tests all green, so the pilot was skipped? Green proves the code matches the world you defined. Run the pilot.
- [ ] Group B resting on "resume is supported in theory"? A resume without a crash drill runs its drill during the first real crash. Kill it on purpose now.
- [ ] Ticked after the full run finished? The accident it prevents has happened. Go to templates/result-interrogation-record.md.
- [ ] "It is running" taken for "it is producing"? Logs and bills moving prove nothing. Trace one number to criteria, ledger, and raw text.
- [ ] Only scores on disk? Every scorer bug then costs the full amount again. Store the raw answers.

Filled in → goes to: templates/surprise-result-red-flags.md
