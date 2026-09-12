# Dispatch brief

**How to use.** Four columns: task, context, boundaries, acceptance criteria. Once written, run the stranger-executor test: an executor who has never met you and cannot ask questions can start from this brief alone and knows what counts as delivered. Fail, fix the brief before dispatch. Check that the context pack is the current version; stale facts are the top source of rework and an agent does not refresh facts on its own. `answers when wrong:` carries a person's name or the task goes back one level. For a verification task, use a file in briefs/ instead: it leaks no expected answer.

```text
[TASK]
What to produce (verb first, one sentence): ____________
Medium and format (file type / table structure / word or line count): ____________
Deadline and priority: ____________

[CONTEXT]
Background in one sentence (why this task exists, who the output is for): ____________
Required reading (files / links, and which wins in a conflict): ____________
Key terms and basis (in this task "X" is defined as ...): ____________
Existing conclusions, or ones already overturned (with status): ____________
☐ Checked before dispatch: the context pack is the current version

[BOUNDARIES]
Not allowed: inventing facts, citations, numbers; anything uncertain is marked "to verify"
Do not touch (outside the executor's remit, e.g. the wording of claim strength): ____________
When information is missing: come back with a list of "facts I need"; no filling in from imagination
Explicitly out of scope: ____________

[ACCEPTANCE CRITERIA]
Executable checks a third party can run: 1 ________  2 ________  3 ________
Rework conditions (any one sends it back): ____________
answers when wrong: NOBODY | <person's name>
```

Good example (teaching, generic):

```text
[TASK] Produce an evidence summary on "[approach A] vs [approach B]": a markdown table, one paper per row,
claim / evidence / limits of application / relevance to the question. 10 to 15 rows, by 22:00 tonight.
[CONTEXT] Purpose: a base table of evidence for the decision meeting on "do we pilot [approach A] in [module]".
Required reading: the attached controversy map v3 (this one wins, not the version in your memory).
Basis: "stronger" means accuracy after cost alignment, never a comparison with unaligned cost.
[BOUNDARIES] Include only papers you can give a real source for; mark anything unsure "to verify".
Draw no conclusion on "should we pilot"; that is the meeting's business. Missing basis information: come back with a list.
[ACCEPTANCE CRITERIA] 1 Every paper findable in an academic search engine (search link attached);
2 every row's claim uses the paper's own qualifier wording, none removed; 3 no row has an empty "limits of application".
Rework: a claim with no source, or any citation that cannot be found.
```

### Self-check
- [ ] "Look into", "latest", "solid", "not too long" in the task line? None can be accepted against. Name the deliverable, the time basis, and the length.
- [ ] Context pack not checked as current? Passages come back for redoing. Refresh it before dispatch.
- [ ] An acceptance criterion of the "write it better" kind? A third party cannot run it. Replace with an executable check.
- [ ] Boundaries missing the "come back with a list" line? That is the cheapest gate against hallucination. Add it.
- [ ] `answers when wrong: NOBODY`? Drop one delegation level and hand it back to the human with the four questions.

Filled in → goes to: templates/three-process-questions.md
