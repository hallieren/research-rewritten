# research-rewritten, a skill

A Claude Code skill distilled from the book "Research, Rewritten" (the repo this folder lives in). It is for anyone who must sign off on a technical conclusion reached with AI help: a benchmark or A/B result, a tech-selection memo, a report someone else generated with AI, a vendor's claim. It wires the book's seven-step truth-seeking loop into agent behaviour, and above all it keeps the book's line on what the agent may do alone, what it drafts for a human to rule on and sign, and what it must label as unknown. It is not for code with no claim to defend, prose editing, or a summary nobody will act on.

## What you get

Hand it a result to sign off on and it does not answer "looks good". It runs the step, drafts the ruling, and leaves the signature to you. Every ruling it produces carries four grep-able lines:

```
ruling: alive after narrowing | signed by: UNSIGNED
answers when wrong: NOBODY | <a person's name>
verification channel: separate session, model Y, brief: briefs/verify-citations.md, leak_check: clean
criteria timestamp: before results
```

The agent writes `signed by: UNSIGNED` and never fills the name, not even on request; a document still carrying UNSIGNED is stamped `STATUS: DRAFT, not for the decision chain`. It draws the map and hands you the pen.

## Layout

- `SKILL.md`: the hand-off protocol, the four sentinel lines every ruling carries, closed vocabularies, route table, step contracts, acceptance mode, excuse table.
- `references/`: eleven files, one level deep, each opening with "Load this reference when". They carry the per-step craft.
- `templates/`: 24 fillable forms in five ordered families; each ends with "Filled in, goes to".
- `briefs/`: 16 prompts that leave the desk verbatim into an independent channel (another session, another model, a person). Nothing else lives here.
- `scripts/`: five stdlib Python checks, each with `--help` and `--selftest`.
- `evals/`: the test prompts, fixtures, and trigger queries used to compare the skill against a no-skill baseline.

## Install

In Claude Code, install from the plugin marketplace:

```
/plugin marketplace add hallieren/research-rewritten
/plugin install research-rewritten@research-rewritten
```

Or symlink it directly:

```
ln -s "$PWD/skills/research-rewritten" ~/.claude/skills/research-rewritten
```
Other harnesses: copy the folder into their skills directory.

## The book is the source of truth

Templates and briefs here are domain-neutral distillations of `docs/appendices/` (index: `docs/appendices/template-index.md`). When the two disagree, the book wins. The scripts lift stdlib code from `code/smol-army` and `code/persona-panel`.

## Scripts

- `prereg_check.py`: prints `PREREG SECTIONS:`, `PREREG:`, `CHANGES:`. Were the criteria complete, and locked before the first result? Note: git can only order files that entered the repo in different commits; a preregistration committed together with its results reads `NO TIMESTAMP`.
- `ledger.py`: prints `LEDGER:`. Append-only, hash-chained, with a hard cap that fires.
- `effective_n.py`: prints `N:`, `NAIVE:`, `CLUSTERED:`. Rows are not independent units.
- `interlock.py`: prints `INTERLOCK:`. Every number in two documents traced to the results file.
- `leak_check.py`: prints `BRIEF:` and `REPORT:`. No expectation leaks into a brief; verdicts are three-valued; rulings carry their sentinel lines.

## Testing

`evals/evals.json` holds five prompts with grep-able assertions; `evals/trigger-evals.json` holds ten should-trigger and ten should-not queries. Against a no-skill baseline on the five scenarios, the with-skill runs passed every grep-able assertion and the baseline almost none. The prompts, fixtures, and assertions are in `evals/`.

## License

Prose in this folder (SKILL.md, references, templates, briefs) is CC BY-NC-SA 4.0; `scripts/` and `evals/` are MIT, following `LICENSE.md` at the repo root.
