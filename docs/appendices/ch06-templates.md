# Chapter 6 templates · Test Plan Template + Confounder Checklist + Plan Red-Team Prompt

> This appendix is the complete fillable version of the three tools in Chapter 6.
> The order of use is fixed. Fill Template 1 first, run every line of Template 2 when you reach item 6, and run one round of Template 3 before you sign.

---

## Template 1 · Test Plan (preregistration-style fillable version)

**How to use.** Fill it in and stamp a timestamp before you run anything; after sign-off, only appended change-log entries, no edits. Not filling every blank is fine. The blanks you cannot fill are exactly where you have not thought it through. Start the run with blanks still in it and they will fill themselves in along your preference once the results are out, which is the "degrees of freedom colluding with motive" of Chapter 6.

```text
# Test plan
Project: ____________   Drafted by: ____________   Draft date: ____________
Sign-off date: ____________   Timestamp method (git commit / email / preregistration platform): ____________

## 1 Question
The question this test has to answer (one sentence):
____________________________________________

## 2 Hypothesis H (the Chapter 5 output, copied as is)
Falsifiable statement: ____________________________________________
Scope (within what tasks/populations/conditions it holds): ____________________
Falsification condition (what observation kills H): ____________________

## 3 Arm design
Main arm (my design): ____________________________________________
Baseline arm (control): ____________________________________________
  - Tuning/optimization budget the baseline gets: ______ (must equal the main arm; if not, write the reason)
Steelman arm:
  - The strongest opponent's sentence ("your result is really just ____"): ____________
  - The arm built to block that sentence: ____________________________________
Other arms (one line each, stating which alternative explanation it rules out):
  - ____________________________________________

## 4 Basis
Primary basis (how it is computed, down to the formula): ____________________________
Reason for making it primary (usually = the unit the final reader thinks in): __________
Sensitivity basis (listed separately, never mixed with the primary): ______________________
Commitment (copy as is, effective on sign-off): if the two bases reach opposite conclusions, report it honestly, no picking.

## 5 Criteria and falsification condition
What counts as a win (what number triggers it): __________________________
What counts as a loss: ____________________________________________
What counts as undecided (how to word it when neither is met): ________________________
Statistical test: ____________   Significance level: ____________
Sample size / repeats per configuration: ____________   Random seed: ____________
Stopping rule (when to stop running, set first, guards against "run until significant"): __________
Falsification rehearsal record (invent a set of numbers, confirm the criteria really rule against me): ____________

## 6 Contamination and confounder check
Run every line of Template 2. Lines that do not clear:
  - Line: ______   Disposition (mitigation / written into limitations): ______________

## 7 Filing and change log
Timestamp: ____________
Change log (append only):
  - Date: ______   What changed: ______   Reason: ______
    Did this change happen after the results were seen: ______ (yes → related conclusions downgraded to exploratory)
```

**Self-check** (run through before signing):

- [ ] Is the falsification condition in item 2 empty, or written as "judged as a whole once the results are in"? That is not criteria, that is decoration. Go back to Chapter 5 and grind it again.
- [ ] Cannot find the steelman arm in item 3? Your control only proves "better than doing nothing." Ask once more. "If the result comes out as I want, what would the strongest opponent say?" Give that sentence an arm.
- [ ] Cannot fill the tuning budget field on the baseline arm? The review meeting in section 6.1 is waiting for you.
- [ ] Is the "stopping rule" in item 5 blank? "Run until significant" is one of the best hidden degrees of freedom.
- [ ] Skipped the falsification rehearsal? Watch it go red first. Criteria that have never been able to fail do not count when they are green.
- [ ] Does the criteria wording carry "a reasonable range," "as appropriate," "at discretion"? Every one of them is a backdoor. Turn it into a number.
- [ ] No timestamp? A plan with no timestamp cannot prove three weeks later that it was "locked in first."

---

## Template 2 · Confounder Checklist

**How to use.** Run it line by line while filling item 6 of Template 1. The goal is not to tick every line, the goal is **honest disposition**. Tick what clears; for what does not clear, write a mitigation, or write it honestly into the limitations. An all-green checklist is itself suspect. You can let AI run your plan against this list line by line first (breadth is its strong suit), but the final tick on every line is yours.

**A Baseline fairness**

- [ ] Did the baseline get a tuning/prompt-optimization budget equal to the main arm?
- [ ] Is the baseline's version/configuration the strong form of that method rather than a straw man (default parameters, an outdated version, an obviously suboptimal setting)?
- [ ] If the baseline is a number from someone else's paper, are the runtime environment and the data slice comparable to your main arm? Or should it be rerun?

**B Budget and basis alignment**

- [ ] Are the resources both sides consume (money / compute / number of calls / person-hours) measured on the same basis?
- [ ] Is the definition of "same budget" locked in? (Otherwise budget alignment is itself a degree of freedom to fiddle with afterward)
- [ ] Are the primary basis and the sensitivity basis listed separately, with a commitment to report both?

**C Alternative explanations**

- [ ] Have you listed at least three cheap explanations that "explain the same result without your hypothesis"?
- [ ] Does every cheap explanation point at an arm or a step in the plan built to rule it out?
- [ ] Does the cheapest explanation of all have an arm of its own? (The lesson of the spine case, the two-arm design of army vs frontier cannot tell "teaming works" from "spending works," until the same-budget self-consistency arm is added)

**D Data contamination**

- [ ] Could the evaluation data have been "seen" by the model during training? (Public benchmarks, public survey data, question banks circulating online, treated as seen by default)
- [ ] Could it have been "seen" by your own development process? (Looking at the same validation set over and over while tuning = human overfitting)
- [ ] Is the contamination check a step written into the plan, or one line saying "should be fine"?

**E Criteria backdoors**

- [ ] Is the metric unique and set beforehand? (Counting several metrics equals picking the metric afterward)
- [ ] Is the data slice set beforehand? ("Significant on some subset" counts only when that subset was declared in advance)
- [ ] Is the exclusion rule for outliers set beforehand?
- [ ] Is the stopping rule set beforehand?

**F The measurement itself**

- [ ] Could the way scoring and judging works favor one arm? (The spine case ruling out LLM-judged tasks in Chapter 5 is exactly this line, judge preference would contaminate the measurement into a second research question)
- [ ] If there is a human judging stage, does the judge know which arm a sample came from? (Blind it wherever you can)

---

## Template 3 · Plan Red-Team Prompt

**How to use.** Use it the moment you believe the plan is final but have not signed it, since the earlier you take the beating the cheaper it is. The output is a draft list, not a ruling. Go line by line, what you adopt turns into a change to the plan, what you reject gets one line of reason on file (that rejection record becomes your ammunition at the defense later). Mind the division of labor. Red-teaming **conclusions** is Chapter 10's business. What gets red-teamed here is a **plan** that has not run yet.

```text
This is my test plan:

[paste the full plan, including arm design, basis, criteria]

Your job is to overturn it, not to improve it. Assume you are the reviewer
who least wants this conclusion to hold.

1 List every degree of freedom in the plan that "can still be moved after the results are in";
2 For each one, say which conclusion it would favor if adjusted after the fact;
3 Give one cheapest alternative explanation that, with the arm design unchanged,
  would produce the same result;
4 Point out which criterion's wording leaves a backdoor (words like "as appropriate," "a reasonable range");
5 Check the baseline arm. Is it the strong form of that comparison method? Where does it look like a straw man?
6 If you were to add one arm built to make trouble for my conclusion, which arm would you add and why?

Raise only problems specific enough to act on, no general methodology advice.
Output each one in three parts, "the problem → who it favors → how to fix it."
```

**Self-check** (run through when you use the red-team output):

- [ ] Did you adopt only the lines that were easy to hear? The ones that deserve the closest look are exactly the ones that irritate you.
- [ ] AI reported no serious problem? Do not take that as evidence the plan is solid. In the words of the Chapter 3 snapshot, the most expensive flaws in a plan (unfair baseline, basis drift, a criteria backdoor) are exactly the kind it does not flag itself. When the red-team output is empty, the confounder checklist (Template 2) still gets run.
- [ ] Planning to reject a "new arm" it proposed? Write the reason for rejecting before you reject. What you cannot write out, you should probably adopt.
- [ ] Changed the criteria after the red team? Legitimate, and changing them at this moment is exactly the point. But the change still goes into the change log. Want to change them after sign-off and a different rule applies (see item 7 of Template 1).
- [ ] Only ran one round? Fix it and feed it another round, until a new round returns only old lines you have deliberately rejected.
