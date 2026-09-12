# Research, Rewritten

[![ci](https://github.com/hallieren/research-rewritten/actions/workflows/ci.yml/badge.svg)](https://github.com/hallieren/research-rewritten/actions/workflows/ci.yml) [![docs](https://github.com/hallieren/research-rewritten/actions/workflows/docs.yml/badge.svg)](https://github.com/hallieren/research-rewritten/actions/workflows/docs.yml) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22543684.svg)](https://doi.org/10.5281/zenodo.22543684)

> **Deep research gives you plausible. This book gives you reliable.**

Written for software and AI engineers who have to do research at work. You are asked to sign off on a technical judgment (can a small model replace the large one, should the retrieval layer be swapped, can this AI report be trusted), and the evidence is an experiment anyone can rerun. The signature is yours. Academic researchers, analysts, and people doing due diligence use the same process, with the shape of the case converted as Chapter 3, section 3.6 shows. If "sounds right" is good enough, you need a good search tool, not this book. It wires general-purpose AI and agents into every step of truth-seeking work, from reading the literature to red-teaming, and at every step it says plainly where you can hand it to AI, where you must gate it yourself, and where nobody knows yet. Sixteen chapters plus Start Here, prompts and templates for every chapter, and two rerunnable experiments. Start Here runs a real experiment in two hours; the reading paths and the spine case are in [docs/index.md](docs/index.md).

## How to read

- **Online**: <https://hallieren.github.io/research-rewritten/> (full-text search, dark mode, previous and next chapter).
- **On GitHub**: the chapter links below go straight to the files.
- **Offline**: [EPUB](https://hallieren.github.io/research-rewritten/research-rewritten.epub), or build it locally with `./scripts/build_epub.sh` (needs pandoc).
- **Locally**: `uvx --from mkdocs-material mkdocs serve`, then open <http://127.0.0.1:8000>.

## Hand it to your agent

After every chapter's exercise block there is an instruction you can paste straight into Claude Code, Codex, or any coding agent. It walks you through the chapter's appendix prompt set, leaves the criteria, the scoring, and the signature to you, and opens the verification channel in a separate session, as the book's discipline requires. The one-time setup instruction is on the [home page](docs/index.md). An agent can also read the whole book from [llms.txt](https://hallieren.github.io/research-rewritten/llms.txt) (index) and [llms-full.txt](https://hallieren.github.io/research-rewritten/llms-full.txt) (full text).

## The skill

The book's templates, dispatch briefs and checks are packaged as a Claude Code skill in [skills/research-rewritten](skills/research-rewritten/). It triggers when you are about to sign off on an AI-assisted result: a memo, an announcement, a report someone else generated, a tool's claim. It carries 24 fillable templates, 16 independent-channel briefs, and five stdlib Python checks (preregistration timing, append-only ledger, effective sample size, number interlock, leak check). The book stays the source of truth; the skill is the desk copy. Install it in Claude Code with `/plugin marketplace add hallieren/research-rewritten` then `/plugin install research-rewritten@research-rewritten`, or symlink it with `ln -s "$PWD/skills/research-rewritten" ~/.claude/skills/research-rewritten`. The comparison against a no-skill baseline is in `skills/research-rewritten/evals/`.

## Chapters

| # | Chapter | Templates | Code |
|---|---|---|---|
| Preface | [This Book Was Put on Trial](docs/chapters/ch-preface.md) | / | [smol-army](code/smol-army/) · [persona-panel](code/persona-panel/) |
| Start Here | [A Two-Hour Win](docs/chapters/ch00-start-here.md) | / | [smol-army](code/smol-army/) |
| **Part I · Reframing** | | | |
| 1 | [After Coding, Research](docs/chapters/ch01.md) | [Templates](docs/appendices/ch01-templates.md) | |
| 2 | [A Map Stolen from Paradigm Shifts](docs/chapters/ch02.md) | [Templates](docs/appendices/ch02-templates.md) | |
| 3 | [The Truth-Seeking Workflow and the Autonomy Ladder](docs/chapters/ch03.md) | [Templates](docs/appendices/ch03-templates.md) | |
| **Part II · The Main Line, One Step per Chapter** | | | |
| 4 | [Master a Field](docs/chapters/ch04.md) | [Templates](docs/appendices/ch04-templates.md) | |
| 5 | [Questions and Hypotheses](docs/chapters/ch05.md) | [Templates](docs/appendices/ch05-templates.md) | [persona-panel](code/persona-panel/) |
| 6 | [Turn an Idea into a Falsifiable Test Plan](docs/chapters/ch06.md) | [Templates](docs/appendices/ch06-templates.md) | [persona-panel](code/persona-panel/) |
| 7 | [Execution](docs/chapters/ch07.md) | [Templates](docs/appendices/ch07-templates.md) | |
| 8 | [Read the Results, Catch the Errors](docs/chapters/ch08.md) | [Templates](docs/appendices/ch08-templates.md) | [smol-army](code/smol-army/) · [persona-panel](code/persona-panel/) |
| 9 | [Delivery](docs/chapters/ch09.md) | [Templates](docs/appendices/ch09-templates.md) | [smol-army](code/smol-army/) |
| 10 | [Red Team](docs/chapters/ch10.md) | [Templates](docs/appendices/ch10-templates.md) | [persona-panel](code/persona-panel/) |
| **Part III · Trust, the Book's Cutting Edge** | | | |
| 11 | [Failure Modes Unique to Research](docs/chapters/ch11.md) | [Templates](docs/appendices/ch11-templates.md) | [persona-panel](code/persona-panel/) |
| 12 | [The Verification Workflow](docs/chapters/ch12.md) | [Templates](docs/appendices/ch12-templates.md) | [persona-panel](code/persona-panel/) |
| 13 | [An Honest Map](docs/chapters/ch13.md) | [Templates](docs/appendices/ch13-templates.md) | |
| **Part IV · New Roles** | | | |
| 14 | [The Researcher's New Craft](docs/chapters/ch14.md) | [Templates](docs/appendices/ch14-templates.md) | |
| 15 | [Make It a Habit and a Capability](docs/chapters/ch15.md) | [Templates](docs/appendices/ch15-templates.md) | |
| 16 | [Coda · How This Book Stays Current](docs/chapters/ch16.md) | [Templates](docs/appendices/ch16-templates.md) | |

**Templates**: [Template index](docs/appendices/template-index.md) · **Experiments**: [Experiment ledger index](docs/experiments.md) · **Companion code**: [code/smol-army](code/smol-army/) · [code/persona-panel](code/persona-panel/) (install [uv](https://docs.astral.sh/uv/), then `uv sync --extra dev && uv run pytest` inside either project)

## Verified by its own method

A book that teaches verification publishes the full record of its own verification. The spine experiment's criteria were written down before it ran ([prereg.md](code/smol-army/docs/prereg.md)), its conclusions took a red team before release ([redteam-2026-07-25.md](code/smol-army/docs/redteam-2026-07-25.md)), every cent of API spend is in the [cost ledger](code/smol-army/results/ledger.jsonl), and every number in the book points back to its [raw results](code/smol-army/results/). The [Experiment ledger index](docs/experiments.md) is the entry point.

Prose CC BY-NC-SA 4.0 · code MIT ([LICENSE.md](LICENSE.md)) · [Contributing](CONTRIBUTING.md) · [How to cite](CITATION.cff)
