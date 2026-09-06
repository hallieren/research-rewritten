# Chapter 4 templates · Controversy Map Prompt + Paper Card + Frontier-Layer Subscription Rules + Coverage Checklist

> How to use. The four tools match the three-layer intake workflow of Chapter 4. The map layer uses Template 1, the skeleton layer Template 2, the frontier layer Template 3, and Template 4 runs before you close out. Budget one afternoon for the whole first round.

---

## Template 1 · Controversy Map Prompt (map layer)

**How to use.** Fill in the field and your specific question, and use the output as a first-draft map. The hard step cannot be skipped. Every paper AI lists, confirm one by one at Semantic Scholar / Google Scholar that it exists (about twenty minutes). This is the only cordon between you and "a castle in the air built out of fabricated citations."

```text
I need to master a field, starting with a map. Field: [your field].
My specific question is: [the question you need to answer].

Give me:
1. The 3-6 main positions/camps in this field, and each one's core claim;
2. 2-3 representative works per camp (title, authors, year, venue);
3. The real points of disagreement between camps, not differences in wording, substantive conflicts of the form "if A is right, B is wrong";
4. The 1-2 disagreements most relevant to my question.

Requirement: list only papers you can give a real source for; mark anything you are unsure exists as "unsure".
```

The controversy map table (fillable version; rows are claims, and every paper you read afterward gets filled in):

```text
| Claim | Papers that support it | Papers that oppose it | Substance of the disagreement |
|---|---|---|---|
| ____________ | ____________ | ____________ | ____________ |
| ____________ | ____________ | ____________ | ____________ |
```

## Template 2 · Paper Card (skeleton layer)

**How to use.** Generate one card for every load-bearing paper (each camp's representative works, the repeatedly cited sources, the empirical studies tied directly to your question, usually five to fifteen of them). The last field is always left blank, and you fill it by hand after reading the key passages of the original. A card where you filled in "how much I believe it" is your own judgment. An AI summary is only a compression of somebody else's.

```text
Read this paper and distill it in the format below, no embellishment:
- Core claim (one sentence, in the paper's own wording)
- Evidence (what experiment/data/task, at what scale)
- Where the claim applies (limits the authors admit, in the limitations section and hidden in footnotes)
- Which prior work this paper refutes or depends on
- [Blank] How much I believe it:
```

## Template 3 · Frontier-Layer Subscription Rules

**How to use.** Set it up once after the map is built, then run it a fixed half hour every week. The admission criterion is locked in. Without a rule that permits letting things flow past, chasing the frontier is nothing but anxiety.

```text
1 Citation alerts: at Google Scholar / Semantic Scholar, set citation alerts for
  [3-5 load-bearing papers]. Whoever cites them may be shaking or reinforcing your map.
2 Weekly scan prompt (fixed output format):
  "This is my controversy map: [paste]. This is this week's new literature: [paste search results].
   Output in three columns: new evidence relevant to the map / signals the map needs changing / noise I can ignore."
3 Admission criterion (locked in): a new paper is worth entering the skeleton layer if and only if it could
  change who wins a row of the controversy map. Let the rest flow past.
```

## Template 4 · Coverage Checklist (before you close out)

**How to use.** The blind spots of a single search path are systematic. Before you close out, go through the four-way cross-check one item at a time. AI never volunteers "I missed a community". The only antidote is this step, not a cleverer prompt.

- [ ] **Keyword multipath**: have AI generate 5-8 sets of search terms from different terminology systems (the same thing goes by different names in different communities), and run a round on each;
- [ ] **Citation graph**: start from the load-bearing papers and walk one layer forward (who cited it) and one layer backward (who it cited);
- [ ] **Reverse test**: ask AI "if one paper could overturn my current map, what would it most likely look like and which community would it sit in", then go search whether it exists;
- [ ] **Human anchor**: take the controversy map to someone who really knows the field and ask "what did I miss".

---

### Self-check (tick each item before you hand over the map)

- [ ] **Fabricated citation**: has every paper AI listed been confirmed to exist in an academic search engine? The title is plausible, the authors are common names, the journal is real. A paper that does not exist is AI's most typical invention.
- [ ] **Misremembered title**: for a citation you wrote from memory, did you go back to a first-hand source and check the title word by word? A title off by one word is, in search and under someone else's check, a paper that does not exist. The inventor is not necessarily AI, it can also be your memory.
- [ ] **Secondhand drift**: has every claim entering a decision been checked against that passage in the original? Each hand it passes through drops a little of the qualifier, and the qualifier is exactly the part judgment needs most.
- [ ] **The coverage illusion**: did all four paths of Template 4 really run? A fluent, complete answer is not complete coverage, especially when you want a "gap", where AI only wraps it to look more real.
- [ ] Does the controversy map hold at least one line of "if A is right, B is wrong"? A map with no disagreement usually means you have not found the battlefield yet.
