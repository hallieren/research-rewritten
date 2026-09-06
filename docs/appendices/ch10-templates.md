# Chapter 10 templates · Red-Team Dispatch Brief Template + Four-Attack-Surface Red-Team Prompt Set + Disposition Table

> This appendix is the complete fillable version of the three tools in Chapter 10.
> The order of use is fixed. Once the deliverable is final, use Template 1 to compress it into a claims list and write the dispatch brief. Open an **independent session** for each of the four attack surfaces and run the matching prompt from Template 2. Once the list of charges comes back, rule on it line by line, then use Template 3 to assign a tier, dispose, and file. "The red team is mandatory" in the L2 verification of Chapter 12 means exactly these three steps.

---

## Template 1 · Red-Team Dispatch Brief (fillable)

**How to use.** The only purpose of the brief is to get the red team all the materials without letting it know what you expect. An independent session, zero history, and switching models is better still. Letting the model that paired with you to write the conclusion serve as its red team violates the generation/verification orthogonality principle. Run the leak check at the end of this section once, then dispatch.

```text
# Red-team dispatch brief
Deliverable: ____________ (paper / memo / report name; no body text, see the claims list)
Date: ____________  Red-team session and model (different from the writing channel): ____________

## Materials (paths and originals only, not your summary or narrative)
- Raw results file: ____________
- Criteria / preregistration file (with timestamp): ____________
- Scoring / analysis script: ____________
- Cost ledger (if there are cost claims): ____________
- Data / problem text file: ____________

## Claims list (each line = one attackable factual claim in the deliverable, neutrally worded)
A1 ____________________________________________
A2 ____________________________________________
A3 ____________________________________________
A4 ____________________________________________
(5-10 lines is about right; a conclusion and its qualifying conditions get one line each;
 write number claims to recomputable precision, such as "Δ = −2.3pp, CI [−4.0, −0.7]")

## Work order
Attack surface of this order: ____________ (the scorer / data composition / independence assumptions / cost basis, one of four)
Run the prompt for the matching attack surface in Template 2.
```

**Self-check (leak check, must pass before dispatch)**:

- [ ] Does the brief say "I hope / I am worried / confirm this for me / our contribution"? Delete all of it. A red team that reads your expectations aims off target to match them.
- [ ] Do the claims carry adjectives ("significantly," "robustly," "surprisingly")? Rewrite them as neutral statements.
- [ ] Did you merge the four attack surfaces into one order? Split them. Dispatched merged, the model fills the page with the softest surface.
- [ ] Did you dispatch from the session or the model that wrote the conclusion? Switch. Context is a position.
- [ ] Did you hand over your summary instead of the original files? Give the originals. A red team cannot attack what your summary left out, and that is exactly where the hits land.

---

## Template 2 · Four-Attack-Surface Red-Team Prompt Set

**How to use.** The four surfaces share one generic skeleton, and only the [attack surface definition] block gets swapped. One surface, one order, an independent session. The output must be the set of three, charge + consequence + executable check. A charge without a check is a comment, and it is not accepted.

**The generic skeleton**:

```text
Role: you are hired to attack the claims list below, on the attack surface:
[attack surface definition, paste in one of the four blocks below]
Input: the claims list and the materials (see the dispatch brief).
Output: a list of charges, ordered by lethality, and every charge must carry three things:
1 Charge: which point of this attack surface could make one of the claims fail (name the claim number);
2 Consequence: if the charge holds, which claim dies, and what direction and rough magnitude of effect gets manufactured;
3 Check: one check executable the same day (a script sketch / a sampling plan / a replay experiment /
  a recompute on another basis), whose result can confirm or rule out this charge.
Rules: attack only, no balanced coverage; do not evaluate "whether the conclusion as a whole is credible";
do not list a charge you cannot give an executable check for; if you find nothing, state "nothing found on this surface,"
do not pad.
```

**Surface 1, the scorer / the criteria**:

```text
Attack surface definition: how right and wrong, success and failure, get judged (gold answers, scoring
scripts, human annotation rules, an LLM judge, the operational definition of "valid / successful").
Check first:
① whether the definition of "right" has a second defensible reading (ambiguous gold, ambiguous problem text);
② the links in the parsing → matching → scoring chain that silently swallow points or hand them out
  (format suffixes, units, null, timeouts, partial matches);
③ tidy patterns in the wrong answers: always k times, always off by a constant, always in one format, clustered
  in a continuous id stretch (tidiness is the fingerprint of a sick scorer or sick gold);
④ whether the conclusion flips under an equally reasonable alternative scorer / annotator.
```

**Surface 2, data composition**:

```text
Attack surface definition: the samples, the problems, the corpus itself (source, draw, structure, coverage, contamination).
Check first:
① the structure brought in by the draw (first N rows / a single batch / a single source / a convenience sample);
② how many "molds" the samples really have: after stripping proper nouns and numbers, how many literal
  templates are left, and what share each holds;
③ whether the test material could sit inside the training corpus of the system under test (public question banks,
  famous datasets, material from before the corpus cutoff date);
④ whether the data coverage holds up the wording range of the claim, whether "holds on the X slice"
  got written as "holds."
```

**Surface 3, independence assumptions**:

```text
Attack surface definition: the independence behind the sample size and the statistical inference (the quality of n).
Check first:
① the gap between independent units and rows: same template / same person / same batch / repeated measurement,
  how much each shrinks n;
② whether the data structure breaks the independence assumption of the CI, the significance test, the bootstrap;
  how much the interval moves after recomputing by cluster (template family / batch / respondent);
③ whether the errors of the comparison arms are correlated: shared problem set, shared scorer, shared time window
  (an anomaly moving the same way in a control arm signals a sick shared path);
④ stopping rules and multiple comparisons: was n fixed in advance, or "run until it looks good."
```

**Surface 4, cost basis**:

```text
Attack surface definition: the accounting behind every claim of the "cheaper / faster / better value /
cost-matched" kind.
Check first:
① who chose the basis, when it was chosen (before the results or after), and whether it happens to favor
  the author's own design;
② whether the conclusion flips under a reasonable alternative basis, another pricing scheme, one carrying hidden
  costs (retries, failures, labor, development time), one carrying amortization;
③ whether the two sides of the comparison got equally fair prices and configurations: tier, discount, wholesale
  price, point in time (list prices move, did the claim mark its point in time);
④ whether estimated numbers (amortization, extrapolation, conversion) have measured backing; and where they do not,
  whether a caveat hangs beside the claim.
```

**Self-check (run through it when the list of charges comes back)**:

- [ ] The charges are not ordered by lethality, or there are dozens at once? Ask for them merged and reordered. A long list is a dilution tactic, and a report whose top three do not hurt gets dispatched again in full.
- [ ] A charge with no executable check? Send it back. No debate, send it back.
- [ ] "Nothing found on this surface" shows up? Dispatch this surface once more with another model, and it counts only when both rounds come back empty.
- [ ] Did you dispatch only the surfaces you feel safe about? Run all four, the one you feel shakiest about first.
- [ ] Does the list of charges seem to be praising you ("the overall design is rigorous, only minor issues")? Expectations leaked. Go back to Template 1 and check the brief.

---

## Template 3 · Disposition Table and Disposition Record

**How to use.** Every charge ruled "holds" must get a tier and a disposition, one of three, written into the disposition record. There is no fourth. "I am aware of it" is not a disposition. The qualification check runs in a fixed order. First ask whether it can be fixed (fix it), then whether it can be tested (test it), then whether it is fatal (overturn or narrow). Only when all three fail does the caveat get its turn.

**The tier table**:

| Tier | Trigger condition | Disposition action | The unqualified form | The specimen in this book |
|---|---|---|---|---|
| Overturn | The charge hits load-bearing structure and no rewording saves it | The announcement sentence comes off the deliverable; the preregistered numbers still get reported as is, with the post-hoc breakdown side by side (the Chapter 8 discipline). What is overturned is the sentence, not the number | Quietly deleting the number and never mentioning that this conclusion existed | math +18.2pp: the ambiguous-gold charge held, and after removal the −2.3pp reversed direction, so "the army pulls ahead on math" came off (that −2.3 was itself later overturned by the red team, a scoring-residue artifact, see 10.7; but the disposition of overturning the +18 announcement sentence still stands) |
| Narrow | The charge holds, but what it cuts away is the range or the strength of the evidence, not the conclusion itself | Rewrite the boundary of the claim (task family / sample / confidence / exact model), and the new statement is **strictly weaker** than the old one and still checkable | Narrowing into vaguer words ("may under some circumstances"), which is escape, not narrowing | math CI: ~3 template families → "this problem set cannot detect a conclusion, reissue it and test again"; "ties frontier" → "ties GPT-5.6-terra (the balanced tier)" |
| Caveat | The charge holds or cannot be ruled out, and it is unfixable, untestable, not fatal | The conclusion stays, and the caveat travels at the **same address** as it; also leave one check for the next round of experiments | The caveat buried deep in an appendix or a footnote; a caveat hung where an overturn belongs | The subplot's single-source ground truth: "WVS may be inside the training corpus" travels with every subplot conclusion, the FAIL included |

**Disposition record (fillable, filed with the deliverable)**:

```text
# Red-team disposition record
Deliverable: ____________  Date: ____________
Red-team channel (model / session, must differ from the writing channel): ____________

| # | Attack surface | Charge (one sentence) | Check and result | Verdict | Tier | Disposition action (which sentence changed / what caveat hangs) |
|---|---|---|---|---|---|---|
| 1 | ____ | ____________ | ________ | holds/rejected | overturn/narrow/caveat | ____________ |
| 2 | ____ | ____________ | ________ | ________ | ________ | ____________ |

Rejected charges (one line of reason each, kept as ammunition at the defense):
- ____________________________________________

Does the revised deliverable get one more quick round: ______ (a patch can introduce a new handle)
Where this record is filed (same repo as the deliverable): ____________
```

**Self-check**:

- [ ] A charge ruled "holds" with no tier? There is no fourth disposition.
- [ ] Far more caveats than overturns plus narrowings? Check whether you are using the caveat as a trash can, and rerun the three qualification questions line by line.
- [ ] Is the new statement after narrowing vaguer than the old one instead of weaker? "Weaker" means still checkable, with a clearer boundary. Vaguer runs the other way.
- [ ] Did the disposition change only the abstract and leave the matching paragraph in the body untouched? However many times the same conclusion appears in the deliverable, the disposition lands that many times.
- [ ] Not planning to publish the disposition record with the deliverable? It is part of the trust mechanism. A report carrying bullet holes and dispositions is more credible than one that looks untouched.
