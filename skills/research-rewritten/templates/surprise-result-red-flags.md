# Surprise-result red flags

**How to use.** Scan the moment a result arrives, two minutes (illustrative). A flag does not mean the result is wrong; it means check here first. Hit any one, open templates/result-interrogation-record.md and start at the matching first move. Hit three or more, treat the announcement sentence as a condemned prisoner. Favourable and unfavourable results get the same scan (rule).

| # | Red flag | What it usually means | First move |
|---|---|---|---|
| 1 | The effect beats the odds you set yourself beforehand | You are about to get rich, or the scorer or data is sick; the latter is far cheaper | Interrogation record, every item, no sampling |
| 2 | The control arm shows an anomaly in the same direction | The effect comes from shared data or a shared scoring chain, not the treatment | Check the links both arms share: problem set, parser, gold |
| 3 | The strong player dies on an easy task | Suspect the gold answer first, the world second | Pull the raw text of the wrong answers, look for a numerical or format pattern |
| 4 | Wrong answers are highly regular (always k times, always off by a constant, always one suffix) | Not a capability boundary; ambiguity or a parsing defect | Read the problem text word by word for two defensible readings |
| 5 | Wrong answers concentrate in a continuous id stretch or one source batch | Same-template variants, sampling not shuffled | Cluster problem text by template; re-estimate effective n |
| 6 | The CI is abnormally narrow for the sample size and task noise | Samples correlated; the independence assumption is bankrupt | Count independent units; recompute clustered by template or batch |
| 7 | Every metric improves at once | Real improvement rarely blooms everywhere; a shared-source error does | Find a pair of metrics that ought to trade off and see whether both "win" |
| 8 | Remove a small handful of samples and the effect vanishes or flips | The conclusion hangs on that handful | Interrogate that handful on its own (questions 1 and 2) |
| 9 | The result matches exactly the prediction you already said in public | The desirability flag: the drive to check is at its lowest | Symmetry discipline: run the full set as for flag 1 |
| 10 | You are already wording the announcement | The trigger itself | Stop; write the announcement sentence verbatim, then open the record |

```text
Result: ____________   Date: ____________   Scanned by: ____________
Flags hit (numbers): ____________   Count: ____
Announcement sentence, verbatim, unchanged: ____________
Next: ☐ zero hits, mediocre result: L0 spot check only   ☐ zero hits, major result: the stakes are flag 9, open the record   ☐ any hit: open the record at its first move
```

### Self-check
- [ ] Found an innocent explanation and skipped the flag? The innocent explanation goes in the record after the interrogation, not before it. Open the record.
- [ ] Zero hits on a major result and moving on? Stakes are a variant of flag 9. Open the record.
- [ ] Nobody has hit flag 9 in a long time? You have not looked at yourself. Name the prediction you said in public.
- [ ] Scanned only the disappointing results? Same scan both directions. Scan the one you like.

Filled in → goes to: templates/result-interrogation-record.md
