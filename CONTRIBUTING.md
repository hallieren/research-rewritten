# How to contribute

Boundaries first, then the welcome.

## What is not accepted

**Rewrite-style PRs to the chapters.** This book keeps a single author's voice and will eventually go through a publishing process, so the wording, structure, and positions of the text are maintained by the author. If you disagree with the text, open an issue to discuss it. Do not edit the manuscript directly.

## What is accepted

1. **Errata.** Typos, factual errors, dead links, code that does not run. Small ones go straight to a PR, large ones start with an issue.
2. **Reproduction reports.** Ran the Start Here demo or the full smol-army experiment, or failed to? Your numbers differ from the book's? This is exactly the input the book wants most. Submit with the [reproduction report template](https://github.com/hallieren/research-rewritten/issues/new?template=repro-report.yml).
3. **Chapter feedback.** A chapter's method does not work in your field or setting, or you have a better one. Submit with the [chapter feedback template](https://github.com/hallieren/research-rewritten/issues/new?template=chapter-feedback.yml).
4. **Case submissions.** Run the book's workflow on a real problem of your own and write it up as a case. After public release a case library directory will open for submissions (the model is happy-llm's Extra Chapter, the author guards the text, the community grows the case library).

## License grant

By submitting you agree that text contributions are released under CC BY-NC-SA 4.0 and code contributions under MIT (see [LICENSE.md](LICENSE.md)), and that you grant the author the right to relicense your text contributions, including for the commercial published edition of this book. Code under MIT needs no extra grant.

## Language

English preferred, Chinese also accepted.

## Code contributions

The two projects under `code/` accept bug fixes and added tests. To run the tests, go into the project directory and run `uv sync --extra dev && uv run pytest`. Changes must keep the existing tests green.
