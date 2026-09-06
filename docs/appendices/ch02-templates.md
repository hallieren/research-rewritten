# Chapter 2 templates · The Transfer Map

> This appendix goes with section 2.5 in the chapter (the transfer map) and section 2.6 (the three failure condition questions).

---

## Template 1 · Blank Transfer Map

**How to use.** Build a "precedent → now" transfer map for your own field. The precedent need not have anything to do with AI. Any historical change of the "a tool rewriting a craft" kind will do (how to pick one is Template 2, step 1). Aim for 5–12 rows. Fewer than 5 means the mechanism extraction did not go deep enough, more than 12 means you did not merge. Once it is built, run the self-check at the end.

**Header information (fill these four cells first)**

```text
My field / craft: ________________________
Chosen precedent: ________________________ (why this one: ________________)
Date built: ____________  Planned review cycle: every ____ months
Citation format for this table: row N of the transfer map
```

**The main map table**

| # | Pattern (one sentence, write the mechanism not the ending) | How it happened in the precedent (give the event, give the numbers, mark anything from memory [check]) | The counterpart in my field (observable today, or mechanically due to appear) | Status (verified / still exploring / falsified) | Basis / to check |
|---|---|---|---|---|---|
| 1 | ________ | ________ | ________ | ________ | ________ |
| 2 | ________ | ________ | ________ | ________ | ________ |
| 3 | ________ | ________ | ________ | ________ | ________ |
| 4 | ________ | ________ | ________ | ________ | ________ |
| 5 | ________ | ________ | ________ | ________ | ________ |
| … | ________ | ________ | ________ | ________ | ________ |

**What the status column means** (the same as the rest of the book):
- Verified = enough evidence is already observable in your field, not just "it happened in the precedent";
- Still exploring = it makes sense mechanically, the evidence on your side is undecided, and when in doubt put this;
- Falsified = your field already has counterevidence. When not one row in the whole table says "falsified," be wary. It may not be that every pattern is right, it may be that you never looked for a counterexample.

---

## Template 2 · Guiding Questions for a Transfer Analysis of Your Own Field

**How to use.** Fill in the five steps and pour the output straight into Template 1. A full analysis takes about 2–4 hours. Step 4 (the failure condition audit) is the easiest to skip and the one you can least afford to skip. Skip it and what you did is a one-point analogy, not a transfer.

### Step 1 · Pick the precedent

```text
Tool changes my field (or an adjacent field) went through in the past 50 years, list every one I can think of:
1. ________________
2. ________________
3. ________________

Chosen precedent: ________________

Qualifying tests (all three have to be answered "yes," otherwise pick another):
□ Did it substantially change the cost structure of some stage? (which stage: ________)
□ Was it accompanied by panic or hype at the time? (what people said then: ________)
□ Can the outcome be reconciled by now? (at least one professional generation back, the books: ________)
```

### Step 2 · Mechanism extraction (ask these of the precedent one by one)

```text
1. What had its production cost collapse? By roughly how many orders of magnitude?
   ________________________________________
2. Once the old bottleneck disappeared, where did the new bottleneck move to?
   ________________________________________
3. Which class of previously nonexistent error was born in bulk? Are they invisible, do they come in bulk?
   ________________________________________
4. How was trust in output from strangers rebuilt? (graded delegation / review mechanism / origin tracing / other)
   ________________________________________
5. Whose work had its "mechanical part" eaten? What is left that was not eaten?
   ________________________________________
6. Which panics of the time missed? In what unexpected way did they miss?
   ________________________________________
```

### Step 3 · Write the counterparts

```text
Translate each mechanism from step 2 into my situation today:
Counterpart of mechanism 1: ________________ (observable today? □ yes □ no)
Counterpart of mechanism 2: ________________ (observable today? □ yes □ no)
Counterpart of mechanism 3: ________________ (observable today? □ yes □ no)
Counterpart of mechanism 4: ________________ (observable today? □ yes □ no)
Counterpart of mechanism 5: ________________ (observable today? □ yes □ no)
Counterpart of mechanism 6: ________________ (observable today? □ yes □ no)
Anything ticked "yes" is a candidate for "verified" (you still have to write the basis); anything ticked "no" gets "still exploring."
```

### Step 4 · Failure condition audit (score each on "how far it holds," 0–10)

```text
1. Cheap ground truth. Does my field have a "compiler" (a right or wrong signal in seconds to minutes, nearly free)?
   How long one verification takes and what it costs: ________  Score: __/10
2. Feedback loop. The iteration cycle in the precedent vs my iteration cycle, how many orders of magnitude apart?
   ________________  Score: __/10
3. Error recallability. If it is wrong, can it be rolled back? Or does it enter public knowledge / the decision chain, get cited, get inherited?
   ________________  Score: __/10
4. Corpus coverage. How many "relatives" does what I am doing have in the training data? The closer to the frontier, the fewer.
   ________________  Score: __/10
5. Survivorship bias. Is the precedent I picked one that ended well? Was there a similar tool that drove an industry into a ditch
   with nobody to write its biography? Counter-precedent found: ________  Score: __/10

For any item under 5 points, every map row tied to that premise gets downgraded to "still exploring,"
and the reason for the discount goes in the "Basis / to check" column.
```

### Step 5 · Land a falsifiable judgment

```text
Based on row __ of the transfer map, I predict: ______________________________
If within ____ (deadline) I observe ______________________, this judgment is void and the map gets redrawn.
(Every row has to yield at least one sentence like this. A row that cannot does not deserve to be called a judgment, only an impression.)
```

---

## Quick card, the three questions before you rule with the map

The condensed version of section 2.6, copy it out and stick it next to the map:

1. How far do the premises this pattern depends on (cheap ground truth, fast feedback, recallable errors) hold in my setting?
2. Am I transferring the **mechanism**, or transferring the **ending**?
3. How would this judgment be falsified?

---

## Self-check (run it before you hand the sheet in)

- [ ] Every row's "pattern" is written as a mechanism (cost, bottleneck, error type, trust, roles), not as an ending ("everyone turned out fine" is not a pattern).
- [ ] The status column is filled in, one of the three, and no "still exploring" was optimistically written up as "verified." When in doubt, downgrade.
- [ ] Every event, number, and date written from memory is marked [check].
- [ ] You looked seriously for a counterexample or a counter-precedent at least once. An all-green table is a danger signal, not a good score.
- [ ] Every row can state "what observation would overturn it" (step 5). Rows that cannot are either deleted or downgraded.
- [ ] All five failure conditions are scored, and the map rows tied to the low-scoring ones are downgraded with the reason noted.
- [ ] The header carries the date built and the review cycle. Maps expire, and a map with no review date is the same as no map.
