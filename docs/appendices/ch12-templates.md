# Chapter 12 templates · Layered Verification Workflow Card + Independent-Channel Check Prompt Set + Verification Budget Sheet

> This appendix is the complete fillable version of the three tools in Chapter 12.
> The order of use is fixed. First assign the output a layer with Template 3. Then execute the checklist for that layer in Template 1. Every check task dispatched to AI uses a prompt from Template 2. The three independent channel disciplines (channel independence / the brief leaks no expected answer / three-value output) apply to all three layers.

---

## Template 1 · Layered Verification Workflow Card

**How to use.** The layer is decided by "cost of being wrong × probability of being wrong," not by how good the output looks, and prose plays no part in it. The quantities for each layer (how many to sample, how long to budget) are starting defaults. Calibrate them to your field, write them into your own card, and do not change them on the spot after that.

### Layer quick-reference table

| Layer | Trigger | Scope of check | Time budget | Required item |
|---|---|---|---|---|
| L0 spot check | The output does not leave your desk (brainstorming, exploratory drafts, intermediate material) | Sample | 15–30 minutes | A random sampling rule |
| L1 full verification | The output enters the decision chain, someone will spend money, commit people, or draw conclusions based on it | Every citation + every number + the reasoning chain | Half a day–one day (mostly AI time) | The "claim → source" table filed |
| L2 adversarial recompute | A single conclusion being wrong would trigger a hard-to-reverse action (selection, funding, publication) | The named load-bearing conclusions | One to several days / per conclusion | Independent re-derivation + red team (red team method in the Chapter 10 templates) |

### L0 checklist

- [ ] Random citation sample, 5 or 10% (whichever is larger). Two questions each. Does it exist? Does it really say what the output claims it says?
- [ ] Sampling is decided by you or by a random number. Never let the generating side choose, and the verification channel does not choose either.
- [ ] Sample 3 key numbers and trace each to its source, either to the origin or to a dead end (a dead end is a hard defect).
- [ ] One reverse question (the simplified use of Template 2d): "Which claim in this material has the weakest evidence, and why?"
- [ ] Escalation rule. Any hard defect found (fabricated citation / sourceless number) → the whole output moves up to L1.

### L1 checklist

- [ ] Extract the claim list (Template 2a) and group by type, citation / number / reasoning.
- [ ] Forward-check every citation (Template 2b) with three questions. Does it exist? Does it say so? Was it later overturned or retracted?
- [ ] Trace every number (Template 2c) back to its original source and check that the basis matches (comparison baseline, time window, units).
- [ ] Walk the reasoning chain link by link. Label each link's type (citation / calculation / "the author thinks"). List the "author thinks" links separately and hand them to a human ruling.
- [ ] When collating, a human goes through only two columns, every "undecidable" + every "falsified." Undecidable ≠ pass. Nothing turns green quietly.
- [ ] File it. The "claim → source" table is stored with the output, with the check date and channel noted.

### L2 checklist (for each named load-bearing conclusion)

- [ ] Independent re-derivation (Template 2e). Another channel gets only the raw materials and the question, not the conclusion, and derives from scratch.
- [ ] Compare. Converges → record as machine evidence. Does not converge → rule on each point of disagreement by hand, and each one either fixes the output or goes into the limitations.
- [ ] Recompute key numbers by another method, a different calculation path or a different data source.
- [ ] Red-team this conclusion (required; full method and prompts in Chapter 10 and its templates).
- [ ] File every ruling.

### Self-check (run once before and once after executing any layer)

- [ ] Was the layer assigned by "destination + the most likely kind of error," or by "how reliable it looks"? The latter is grading by prose.
- [ ] Was the sampling rule locked in first? Picking "the few that look suspicious" on the spot is not a spot check, it is a hunch.
- [ ] Did any check run through the channel that generated the output? If so it is void. Re-dispatch.
- [ ] Is the "undecidable" column empty? Either this output is unusually clean, or your verification channel is fudging. Check two items yourself.
- [ ] Did output that failed verification take the exception channel of "the author explained and it was let through"? What fails the mechanism does not merge, no exceptions.
- [ ] Was the check record filed? A check with no archive, three months later, equals a check never done.

---

## Template 2 · Independent-Channel Check Prompt Set

**How to use.** The five prompts share three disciplines. ① The verification channel is separate from the generation channel (a different session / a different model / a person), sharing none of the context from generation; ② the brief gives only the claim, not its origin or the expectation; ③ output is always three-valued, confirmed / falsified / undecidable. Each prompt is a skeleton you can rewrite directly. Fill in your content at the [square brackets].

### 2a Claim extraction prompt

(The purpose of this step is to break the output into a list of independently checkable claims. It can be dispatched to any channel, but before the list goes to the verification channel you must strip the concluding tone yourself, see the Self-check.)

```text
Below is a document. Extract every "checkable claim" in it as a list,
one per line, labeled by type:

- Citation: claims a source exists and says something
- Number: gives a specific number and its meaning
- Reasoning: a conclusion derived from the claims above

Requirements:
1 Rewrite each claim in neutral wording, stripping the original's rhetoric, emphasis, and concluding tone;
2 Note where the claim sits in the original (section / paragraph);
3 Do not judge whether a claim is true. Extract only.

Document:
[paste the full output]
```

### 2b Citation check brief (the core template that leaks no expected answer)

```text
You are the verifier. Below is a set of claims. Check each one independently.
I will not tell you which document they came from, and I will not tell you which ones I hope hold.

For each claim output:
1 Verdict (pick one of three): confirmed / falsified / undecidable
2 Basis: the source you actually found (it must open, or point to a specific
  location in a specific paper)
3 For citation claims, answer three questions: does the source exist? Does it really say
  what the claim says it says (check the original text, and watch for dropped qualifiers)? Was it
  later overturned, corrected, or retracted (check forward citations)?
4 If "falsified" or "undecidable": where exactly the gap between the claim and the evidence lies

Forbidden: guessing the "expected answer" from the wording or ordering of the claims;
Forbidden: leaning phrasing on any "undecidable" item;
Forbidden: middle-state phrasings such as "basically correct" or "broadly credible."

Claim list:
1 [claim one]
2 [claim two]
```

### 2c Number-tracing brief

```text
You are the verifier. Below is a set of numerical claims. Trace each one to its source.
I will not tell you which document these numbers came from, and I will not tell you which
number matters to the conclusion.

For each number output:
1 The most original source you can reach (paper table / data file / official statistics),
  with the specific location
2 Basis check: the number's comparison baseline, time window, and units in the source,
  do they match how the claim uses it?
3 Verdict (pick one of three): confirmed / falsified (including "the number is right but the basis was swapped") /
  undecidable (traced to a dead end)

Numerical claim list:
1 [the number and its claimed meaning]
2 [...]
```

### 2d Reverse-question prompt (the lightweight version for L0)

```text
Below is a piece of research material. Your task is not to summarize it but to find its soft spots:

1 Which three claims in this material have the weakest evidence? Why?
2 Which number would you most like to see the source for?
3 If you could check only one claim, which one?

No need to verify, only to point. No pleasantries, and no praising before criticizing.

Material:
[paste the output]
```

### 2e Independent re-derivation brief (for L2; the most leak-prone of the set, self-check word by word)

```text
Below is a batch of raw materials and one research question. Based on these materials
and only these materials, derive your own conclusion independently.

Research question: [the question itself, with no leaning wording]

Requirements:
1 Give your conclusion, and the complete reasoning chain from the materials to it;
2 For each link, note which part of which material it depends on;
3 Where the materials cannot support a judgment, say "insufficient material" explicitly,
  and do not fill in with common knowledge;
4 At the end, list separately: which two or three premises your conclusion depends on most, and
  how the conclusion changes if they are wrong.

Raw materials:
[raw materials only. No part of the original output, including its subheadings,
figure captions, and paragraph structure]
```

### Self-check (run before every dispatch, focused on leak checks)

- [ ] Does the brief contain words like "confirm," "verify our findings," "support"? Already leaked. Rewrite.
- [ ] Did you paste the full original output or a fragment to the verification channel (2b/2c/2e scenarios)? Context is a position. Re-dispatch.
- [ ] Does the ordering or wording of the claim list hint at which items are "important"? Shuffle the order and rewrite neutrally.
- [ ] Did the check and the generation use the same session? Void. Convenience is not a reason.
- [ ] Did the channel take it upon itself to turn three-value output into "agree / disagree" or a score? Send it back for a three-value redo.
- [ ] Did the re-derivation materials for 2e pick up structural residue of the original output (subheadings, figure captions, wording from the conclusion)? Reorganize the materials and dispatch again.
- [ ] Did the check report give conclusions without basis? A "confirmed" with no basis you can open is treated as "undecidable."

---

## Template 3 · Verification Budget Sheet (fillable)

**How to use.** One page that assigns a layer, row by row, to the project's outputs for the next month. Fill it in and paste it into the project README or the team wiki. Half its job is setting discipline for yourself, and half is making "has this thing passed the layer it should have passed" a question anyone on the team can ask. Review it once a month. When an output's destination changes, its layer changes with it.

```text
# Verification budget sheet
Project: ____________   Owner: ____________   Date filled: ____________
Next review date: ____________

| Output | Destination* | Cost of being wrong | Probability of being wrong** | Layer | Verification channel*** | Escalation trigger | Last checked |
|---|---|---|---|---|---|---|---|
| ______ | ____ | high/medium/low | high/medium/low | L_ | ______ | ______ | ______ |
| ______ | ____ | high/medium/low | high/medium/low | L_ | ______ | ______ | ______ |
| ______ | ____ | high/medium/low | high/medium/low | L_ | ______ | ______ | ______ |

*   Four destinations: self only / team discussion / the decision chain / the public knowledge base
**  For the probability of being wrong, use the Chapter 11 failure-mode census: which kind of error this type of output most often grows
*** Name the verification channel specifically (which model / which prompt path / which colleague),
    and it must be separate from the generating side

Table-wide escalation rules (locked in, no bargaining on the spot):
- A spot check finds a hard defect (fabricated citation / sourceless number) → the whole output moves up one layer
- The output's destination escalates (e.g. an internal draft gets cited in a decision document) → reassign the layer by the new destination
- A conclusion gets cited by a bigger decision → that conclusion is named L2 on its own
```

**Self-check** (after filling it in):

- [ ] Is the whole sheet L0? Either the project has no output that dares enter the decision chain, or you are exempting yourself from inspection.
- [ ] Is the whole sheet L2? You have handed back all the speed dividend AI gave you. Layering is pricing between holding the line and taking the speed. All L2 is a pricing failure, not rigor.
- [ ] Does the verification channel column just say "AI"? Be specific. Which model, which path, and whether it is the same one as the generating side. A channel not named specifically will, when the time comes, take the easy road and be the same one.
- [ ] Is the escalation trigger written as "depends"? That is not a rule. It is a backdoor left for your future self.
- [ ] Is any row's layer set because "it was good quality last time"? The layer follows destination and cost, not impressions.
- [ ] Is the next review date blank? A budget sheet with no review cadence is an out-of-date decoration three months later.

---

## Card 4 · Downgrade note template (matches Chapter 12, section 12.6)

**How to use.** For when the budget runs short. **Pre-write** this line in your project template first. Downgrades always happen on the busiest day, and on that day you will not have the mind to improvise the wording. You will skip it. The filled-in line travels with the conclusion and gets cited along with the numbers.

```text
[VERIFICATION LEVEL NOTE]
This conclusion is delivered at the ____ tier (ten minutes / half an hour / two hours / no next round).

Checked:
- Criteria timestamp: ______ (before the results / after the results / no criteria)
- Citation spot check: ___ / ___ passed
- Number tracing: ______ (all / sampled ___ / not done)
- Independent channel reverse question: ______ (done, weakest claim is ___ / not done)

Not checked: ____________ (list the steps that were cut, as they are; "the rest omitted" is not allowed)

Reason: ____________ (the real constraint: exactly what the time / budget / permission ceiling is)
```

**The three floors of the "no next round" tier** (when the interrogation killed the conclusion and there are no resources to rerun, follow each one):

1. **Report the numbers under the original criteria as is**, with the interrogation's output standing beside them, labeled "post-hoc." Killed in the interrogation does not mean deleted. Deleting is the fraud.
2. **Write "no next round" into the limitations, and be specific**. Not "limited by resources," but "the X this conclusion depends on has only ___ independent units, a confirmatory retest would need about ___ additional samples, and this project did not run it."
3. **Lower the claim strength to the tier the evidence can carry, not to zero.** Erring upward is writing an unconditional statement knowing the evidence falls short. Erring downward is being frightened into saying nothing. Both directions are dereliction.

**Self-check**:

- [ ] Does the "not checked" column say "the rest omitted"? That equals writing nothing. A downgrade without a record and a pretense of the full set look identical to a downstream reader.
- [ ] Did you cut by trimming a little from every layer? Wrong. Cut layers, not the order. Cut the later ones whole and keep the earliest in the order (the criteria timestamp). A gap in every line of defense = no defense on any line.
- [ ] Does the "reason" column say "this one is not important"? That is not a budget problem, it is a prioritization problem. Importance is set by destination, and what enters the decision chain is important. Prioritization problems are solved by delaying delivery, not by downgrading.
- [ ] At the ten-minute tier, did you only read it through? The only action at the ten-minute tier is checking the criteria timestamp. Reading through is the least profitable use of ten minutes, because what you read is precisely the other side's strongest face.
