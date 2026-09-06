# Chapter 13 templates · The Honest Map Toolkit

> How to use. A three-piece kit, used together. First list the rows with Template A, then assign each row a status with rules card B, and last schedule the reviews by cadence table C. Goes with Chapter 13 of the main text.

---

## A. Honest map template (five columns, fillable)

**How to use (one line).** Start from the claims you cited or took as true by default in your most recent deliverable, 10 rows at most. Fill in "claim" and your gut status first, then the fourth column. Rows where the fourth column cannot be filled drop to "still exploring (nobody knows)" automatically.

```text
| # | Claim | Current status | Key evidence | What evidence would change its status | Last reviewed |
|---|-------|----------------|--------------|---------------------------------------|---------------|
| 1 | [one sentence that can be judged true or false] | [verified / still exploring (evidence accumulating or nobody knows) / falsified] | [identifiable source 1; source 2] | [specific, "on seeing X, change to Y"] | [YYYY-MM] |
| 2 | | | | | |
| 3 | | | | | |
| … | | | | | |
```

**Rules for each column.**

- **Claim.** Write a sentence that can die. Rewrite "X has a lot of promise" as "X beats [baseline] on [setting]." Carry the qualifiers. The qualifiers are part of the claim.
- **Current status.** When unsure, "still exploring" without exception, then mark the grade (evidence accumulating / nobody knows). Fence-sitting wording like "basically verified" is banned.
- **Key evidence.** Identifiable sources only (papers, controlled measurements, reproducible practice). "Industry consensus" and "everyone says so" are not accepted.
- **What evidence would change its status.** Write it in the form of a search instruction, so at review time you check straight from it. Write both the upgrade condition and the downgrade condition.
- **Last review date.** Changes on every review, even when the status did not move.

**Self-check (run through before wrapping up).**

- [ ] Every claim in every row can be hit by evidence (ones that cannot be written in falsifiable form, delete or rewrite)
- [ ] No row has an empty fourth column
- [ ] The map is not all "verified" (all green = placebo, not a map)
- [ ] Rows where "this row holding is good for me," the required evidence level has gone up one notch
- [ ] All review dates filled in, and scheduled into the cadence table
- [ ] No status cell is copied (from other people's maps copy only the structure, re-derive or spot-check the status yourself)

---

## B. Status rules card

**How to use (one line).** First screen the evidence with the two disciplines, then grade the evidence with the evidence-level table, and last assign the status by the three operational definitions.

**Two ruling disciplines (before everything else).**

1. **A demo is not production evidence** (row 2 of the transfer map). Demo videos, case write-ups, and vendor material only qualify to trigger an investigation, never to decide a status.
2. **Self-report is not measurement** (row 3 of the transfer map). "Everyone who used it says it's great" does not go into the evidence column. Controlled measurements do.

**Three operational definitions.**

- **Verified**, all three at once:
  ① production-grade evidence (not a demo, not a case write-up);
  ② independent sources ≥ 2, or you can reproduce it with your own hands;
  ③ you can write its falsification shape (the fourth column is not empty).
  Missing any one, back to "still exploring."
- **Still exploring**, the default when neither end is reachable. Then mark the grade:
  **Evidence accumulating** (the direction shows, the volume does not) / **Nobody knows** (not even a direction).
  When unsure, put it here. Faking certainty is the one unforgivable error on this map.
- **Falsified**, either one:
  ① a criterion written down in advance was triggered;
  ② a reproducible counterexample punched through the claim as stated.
  Note, punching through the unconditional form is not punching through the weakened form. After falsification, give the surviving weak form a row of its own.
  Falsified rows **stay, never deleted**, with the falsification date and evidence noted (tombstones are part of a map's credit).

**Evidence-level quick table.**

| Level | Form of evidence | What it can support |
|---|---|---|
| E1 | Controlled measurement against preregistered criteria; independent replication by several parties | Can set "verified" or "falsified" |
| E2 | A single peer-reviewed study / systematic evaluation | Can set a direction; alone not enough for "verified" |
| E3 | Production practice reproducible by many users | Can support "verified" for workflow-type claims |
| E4 | Demos, case write-ups, vendor material | Only qualifies to trigger an investigation |
| E5 | Hearsay, intuition, self-report | Does not go into the evidence column |

**Rule of use.** A row's status is decided by its highest-level evidence. A row whose evidence column holds only E4 / E5 drops to "still exploring" at once.

---

## C. Suggested review cadence

| Current status | Cadence | Example trigger events |
|---|---|---|
| Verified | Every 6 months, or at once on a field-level event | A new model generation ships; the workflow you depend on changes heavily |
| Still exploring (evidence accumulating) | Every 3 months | A new paper of the type the fourth column describes appears |
| Still exploring (nobody knows) | Event-driven + one scan every 6 months | The evidence the fourth column describes shows up for the first time |
| Falsified | Not reviewed, tombstone kept | / |
| ⬜ Pending backfill | Tied to when the experiment / event completes | A preregistered experiment reports results |

**Review action list.**

1. Run only the fifth column, row by row. It is the ready-made search instruction. Do not reread all the literature.
2. Only three moves allowed: change the status (the evidence arrived) / change the evidence (a harder source replaced it) / change the date (checked, nothing moved).
3. **Even when only the date changes, it must change.** A map whose review dates do not move is a dead map.
4. Log one line per review: date, which rows moved, why.
5. AI runs only the fifth column's searches. Status changes must pass through a human. Let AI change the status directly and you get a map where every row is fluent and confident, and fluency is exactly what you are guarding against.
