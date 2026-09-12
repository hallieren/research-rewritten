# Red-team dispatch brief

**How to use.** The brief's only purpose is to hand the red team all the materials without telling it what you expect. Compress the final deliverable into 5 to 10 (illustrative) neutrally worded factual claims; a conclusion and its qualifying conditions get one line each; number claims to recomputable precision. Materials as paths to originals, never your summary. One attack surface per work order, each in a fresh session with the model switched from the writing channel: briefs/redteam-scorer.md, briefs/redteam-data.md, briefs/redteam-independence.md, briefs/redteam-cost.md. Run the leak check, then dispatch.

```text
# Red-team dispatch brief
Deliverable: ____________ (name only; no body text, see the claims list)
Date: ____________   Red-team session and model (different from the writing channel): ____________

## Materials (paths and originals only)
Raw results file: ____________
Criteria / preregistration file (with timestamp): ____________
Scoring / analysis script: ____________
Cost ledger (if there are cost claims): ____________
Data / problem text file: ____________

## Claims list (one attackable factual claim per line, neutral wording)
A1 ____________
A2 ____________
A3 ____________
A4 ____________
(number claims as "Δ = <value>, CI [<lo>, <hi>]"; no adjectives, no stakes, no summary)

## Work order
Attack surface of this order (one of four): the scorer / data composition / independence assumptions / cost basis
Brief file for this surface: briefs/redteam-________.md
Output required: charge | consequence | executable check, ordered by lethality; "nothing found on this surface" allowed, padding not
```

Machine check: `python scripts/leak_check.py brief <this file>` must print `BRIEF: clean` before dispatch; a LEAK line names the phrase to delete.

### Self-check
- [ ] The brief says what you expect, fear, or claim as a contribution? Delete every such phrase; a red team that reads your expectation aims off target to match it.
- [ ] Adjectives on the claims? Rewrite each as a neutral statement with the number.
- [ ] Four surfaces merged into one order? Split them; merged, the model fills the page with the softest surface.
- [ ] Dispatched from the session or model that wrote the conclusion? Switch. Context is a position.
- [ ] Your summary handed over instead of the originals? A red team cannot attack what the summary left out. Give the paths.

Filled in → goes to: templates/disposition-record.md
