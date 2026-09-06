# Chapter 5 templates · Five-Step Question-Sharpening Prompt Set + Question-Sharpening Card

> How to use. Run the five prompts in order, and everything they produce lands on the question-sharpening card at the end. Budget one hour for the whole run. If you run well over, go back and read the "Over-sharpening" item in Chapter 5, section 5.8.

---

## Part one, the five-step question-sharpening prompt set

### Step 1, diverge candidates

**How to use.** Fill in your direction, the controversy map from Chapter 4, and your real constraints. Item 4 is the mirror-risk detector, do not delete it.

```text
My direction: [one sentence describing your vague direction].
Background: here is my controversy map: [paste or summarize: main camps / load-bearing papers / the real disagreement].
My constraints: [time budget] / [available data and hardware] / [the edge of my skills].

Generate 20 candidate research questions. Requirements:
1. Cover different grain sizes, from "worth a paper" to "worth an afternoon";
2. Cover different positions, at least 5 of them questions the opposition or a skeptic would ask first;
3. Attach to each question one line, "what evidence could refute it," and if you cannot write that line, do not list it;
4. At the end, mark separately which questions have most likely already been asked in the literature, and what the clue is.
```

### Step 2, score the three tests (AI as juror)

**How to use.** The scores are yours to give (0/1/2), and this prompt only makes AI take the other side and supply attack angles you missed. "Testable" is a veto.

```text
Candidate question: [paste one candidate question].

Attack it from three angles, with the strongest single objection for each:
1. Testability: is there any evidence that could kill it? If not, point out where it is a position rather than a question;
2. Worth answering: assume the answer is "yes," then "no," and what changes in action? If nothing changes, say it is decoration;
3. Affordable: under my constraints ([paste constraints]), what is the most expensive step on the road to evidence?

Attack only, do not patch. Patching is my job.
```

### Step 3, rewrite it falsifiable

**How to use.** Write it yourself first, and ask AI for three versions to revise only when you are stuck. Anything that cannot fill every slot in the pattern goes back to step 2.

```text
Rewrite the candidate question below into a falsifiable hypothesis, strictly following the pattern:

"Under [conditions/basis], the [measurable metric] of [subject], compared with [control], is [direction and threshold].
If [specific observed outcome] is observed, the hypothesis is falsified."

Candidate question: [paste].

Requirements:
1. Give 3 versions, thresholds from strict to loose;
2. For each version, state which slot was hardest to fill and what you assumed to fill it, since those assumptions are exactly what I will recheck by hand;
3. Do not use words that no observation can refute, such as "effectiveness," "possibility," "potential."
```

### Step 4, action rehearsal

**How to use.** Item 3 matters most, since middle outcomes are the likeliest to expose a hole in the hypothesis (this is how the cost clause of the Chapter 5 spine case got added).

```text
Hypothesis: [paste the falsifiable sentence from step 3].
Reader/decision maker: [yourself / your boss / the investment committee / a reviewer].

Rehearse:
1. If the answer is "yes," what does that decision maker do? How is it different from now?
2. If the answer is "no," what do they do? How is it different from now?
3. List 2-3 middle outcomes that are "neither yes nor no" (partly holds, holds at extra cost, holds only on a subset),
   and check each one, does my falsification condition have a verdict for it? Where it is silent is a hole in the hypothesis.
If the actions in 1 and 2 are the same, say so plainly, this question changes no action.
```

### Step 5, reality-check the resources

**How to use.** Let AI list the route and the costs. Whether it is walkable is your ruling. Accept only the shrink suggestions that do not change the nature of the question.

```text
Hypothesis: [paste the falsifiable sentence].
My resources: [time] / [budget and compute] / [available data] / [the skill range of me + AI].

Give me:
1. The shortest route from the hypothesis to the "specific observed outcome," listed step by step;
2. The biggest cost item at each step (time/money/difficulty of getting the data);
3. If the whole route exceeds my resources, give 3 ways to shrink it (shrink the task scope / shrink the metric / shrink the control),
   and mark each one, after shrinking that way, is the question still the same question.
```

---

## Part two, the question-sharpening card (fillable)

**How to use.** One card per complete run of the five steps. Sign it when it is filled, and pin it to the first page of the Chapter 6 test plan. An empty box is a step of the process not finished.

```text
════════════ Question-sharpening card ════════════
Date: ____________  Project: ____________

[Direction] (raw material, vague is allowed)
____________________________________

[Candidate pool] (output of step 1)
- Total candidates: ____  Of them marked "already asked": ____
- Top three entering scoring:
  A. ________________________________
  B. ________________________________
  C. ________________________________

[Three-test scores] (0/1/2; a 0 on testable = veto)
              Testable  Worth answering  Affordable  Total
  Candidate A:   ___          ___           ___       ___
  Candidate B:   ___          ___           ___       ___
  Candidate C:   ___          ___           ___       ___
  Survivor: ____

[Falsifiable sentence] (output of step 3, both lines required)
Under __________________ (conditions/basis),
the __________________ (measurable metric) of __________________ (subject),
compared with __________________ (control), is __________________ (direction and threshold).
If __________________________________ is observed, the hypothesis is falsified.

[Action rehearsal] (output of step 4)
- Action if the answer is "yes": ______________________
- Action if the answer is "no": ______________________
- Are they different?  ☐ Yes (pass)  ☐ No (back to step 2)
- Middle outcomes and their verdicts (at least one):
  ____________________________________

[Resource check] (output of step 5)
- The most expensive step: ______________________
- Walkable?  ☐ Walkable  ☐ Walkable only after shrinking (what was shrunk: ________)  ☐ Not walkable
- If not walkable: ☐ Switch candidate  ☐ Back to Chapter 4 for a different battlefield  ☐ Shelve it honestly

[Sign-off] I ruled on this question. AI only supplied candidates and counterpoints.
Signature: ____________
══════════════════════════════════════════════════
```

### Self-check (tick each before submitting)

- [ ] My "question" has a finished state, and I can say under what conditions it counts as answered or falsified (otherwise it is a direction).
- [ ] The falsifiable sentence has no unkillable words like "effectiveness/possibility/potential" (wish-list hypotheses).
- [ ] The surviving candidate is my ruling, not AI's recommendation (this step has no cheap ground truth, and nobody answers for AI's recommendation).
- [ ] I read the "already asked" marks and confirmed the survivor is not among them (the mirror risk, AI candidates lean toward old questions in the corpus).
- [ ] If scoring relies on an LLM judge, I have confirmed that judge preference will not contaminate the measurement into a second research question (if that cannot be done, change the task).
- [ ] The action rehearsal covered middle outcomes, and the falsification condition has a verdict for every one of them.
- [ ] The whole run took about an hour. If it ran far over, I confirm I am not using sharpening to put off starting.
- [ ] Threshold numbers (ε and the like) have their reasons recorded, left for the final sign-off at the test design preregistration (Chapter 6).
