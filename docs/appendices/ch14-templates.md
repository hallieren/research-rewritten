# Chapter 14 templates · Process Self-Check Sheet + Dispatch Brief Template

> Prerequisite. You have read the Chapter 14 prose. Template 1 goes with 14.3/14.8 (the craft migration list and the "my process list" exercise), Template 2 goes with 14.5 (dispatch craft).

---

## Template 1 · Process Self-Check Sheet (fillable)

**How to use.** List the process steps you actually did last week (list them against your calendar, not from impression), label each one with the two sorting questions, work out the time distribution, and circle the first step you will dispatch this week. Refill it once a quarter.

| # | Process step (verb first, down to the object) | Cheap ground truth? (yes / no) | How fast do errors show up (on the spot / at delivery / only downstream) | Transcription / judgment | Depreciating / appreciating | Share of last week | Action (dispatch / keep / drill) |
|---|---|---|---|---|---|---|---|
| Example 1 | Format 42 citations | Yes | On the spot | Transcription | Depreciating | 10% | Dispatch |
| Example 2 | Decide which baseline to compare against | No | Only downstream | Judgment | Appreciating | 5% | Keep + drill |
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| 6 | | | | | | | |
| 7 | | | | | | | |
| 8 | | | | | | | |
| 9 | | | | | | | |
| 10 | | | | | | | |
| 11 | | | | | | | |
| 12 | | | | | | | |
| 13 | | | | | | | |
| 14 | | | | | | | |
| 15 | | | | | | | |

**Three summary lines once it is filled in:**

- Total share of time on the depreciating side: ______% (most people land at six to eight tenths on the first pass)
- This week's first dispatch (the most time-consuming step on the depreciating side, go write Template 2): ____________
- Weakest item on the appreciating side (pick one of taste in questions / criteria design / dispatch craft / verification discipline / honest calibration): ____________

**Self-check**:

- [ ] Every step is specific down to "verb + object"; anything written at the grain of "did research" or "read the literature" gets split again;
- [ ] Time shares filled in against a calendar or a time log, not from impression, self-perception is not trustworthy (row 3 of the transfer map);
- [ ] The "judgment" label has to pass a test. If you cannot say what counts as wrong for this step, do not label it judgment yet, it may be transcription you have not thought through;
- [ ] Any step labeled "mixed" must be split in two and refilled; "mixed" is the usual escape from sorting;
- [ ] Depreciating does not mean stop doing it. A depreciating step goes from "you do it by hand" to "you dispatch and accept," what disappears is the hand, not the responsibility;
- [ ] This sheet is a snapshot, not a verdict. The dividing line moves with the tools, and an expired list is as dangerous as an expired map.

---

## Template 2 · Dispatch Brief (task / context / boundaries / acceptance criteria, four columns, fillable)

**How to use.** Once it is written, run it through the "stranger executor test." Can an executor who has never met you and cannot ask you questions start work from this brief alone, and know what counts as delivered? If it does not pass, fix the brief before you dispatch.

```text
[TASK]
What to produce (verb first, one sentence):
Medium and format (file type / table structure / word or line count):
Deadline and priority:

[CONTEXT]
Background in one sentence (why this task exists, who the output is for):
Required reading list (files / links, and which one wins in a conflict):
Key terms and basis (in this task "X" is defined as ...):
Existing conclusions, or ones already overturned (if any, state the status):
☐ Confirmed before dispatch, the context pack is the current version
  (stale facts are the top source of rework, an agent does not refresh facts on its own)

[BOUNDARIES]
Not allowed. Inventing facts, citations, numbers. Anything uncertain gets marked "to verify"
Do not touch (what is outside the executor's remit this time, such as the wording of claim strength):
When information is missing. Come back with a list of "facts I need," no filling in from imagination
Explicitly out of scope:

[ACCEPTANCE CRITERIA]
Executable checks that the deliverable passes (a third party can run them):
1.
2.
3.
Rework conditions (any one of the following sends it back):
```

### Bad brief and good brief, side by side

(The examples are built for teaching, not facts from this book's case.)

**Bad brief.**

```text
Look into whether multi-agent beats a single model, focus on the latest progress,
and write me a solid summary, not too long.
```

Item by item, what is wrong. "Look into" defines no deliverable. "Latest" has no time basis. "Solid" and "not too long" cannot be accepted against. Zero context, the executor does not know why the survey exists or what conclusions you already hold. Zero boundaries, citations can be invented and no list will catch them. Whatever comes back, good or bad, you have no acceptance standard, and the rework rate is left to chance.

**Good brief.**

```text
[TASK] Produce an evidence summary on "multi-agent vs single model," a markdown table,
one paper per row: claim / evidence / limits of application / relevance to our question.
10-15 rows, by 22:00 tonight.

[CONTEXT] Purpose. Give the decision meeting on "do we pilot multi-agent in the retrieval module" a base table of evidence.
Required reading. The attached Controversy Map v3 (this one wins, do not use the version in your memory).
Basis. "Stronger" means accuracy after cost alignment, not comparisons with unaligned cost.

[BOUNDARIES] Include only papers you can give a real source for. Mark anything you are unsure exists "to verify."
Draw no conclusion on "should we pilot," that is the meeting's business. If basis information is missing, come back with a list.

[ACCEPTANCE CRITERIA]
1. Every paper is findable in an academic search engine (attach the search link);
2. Every row's "claim" uses the paper's own qualifier wording, with no qualifiers removed;
3. No row has an empty "limits of application."
Rework conditions. A claim with no source, or any citation that cannot be found.
```

**Brief self-check**:

- [ ] The stranger executor test passes. Someone who cannot ask you questions can start from it and knows what counts as delivered;
- [ ] The context pack has been updated to the current version (the rework lesson from this book's own case, a writing agent read an old version of the facts doc and three passages came back for redoing);
- [ ] The acceptance criteria can be run by a third party, with no criteria of the "write it better" or "go a bit deeper" kind;
- [ ] For a verification task, the brief leaks no expected answer and gives only the claim to be checked (the channel discipline in Chapter 12);
- [ ] The boundaries column carries "come back with a list when facts are missing," giving the executor a way out other than imagination, the cheapest gate there is against hallucination.
