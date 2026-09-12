# Controversy map brief
Kind: GENERATION

**Three disciplines.** 1 Channel independence: the channel that runs this brief is not the session that produced the thing it examines; a different session, a different model, or a person. Sharing no generation context is the requirement, not a preference. 2 No expectation: the brief gives the claim or the material, never its origin, your hope, or which answer would please you. 3 Three-value output: every item comes back as confirmed / falsified / undecidable (VERIFICATION briefs) or as a list of leads with an executable check each (GENERATION briefs); no scores, no agree/disagree, no "broadly credible". Undecidable is a result. It is not pass.
For GENERATION briefs discipline 1 is recommended rather than required; the trailer still states honestly whether context is shared.

Three prompts. The map prompt output lands in templates/controversy-map.md; the paper card prompt fills templates/paper-card.md; the weekly scan runs a fixed half hour (illustrative) once the map exists. Every paper the channel lists gets an existence check by the human before the map goes anywhere; the channel never checks on the human's behalf. Counts in the prompts are illustrative.

## Prompt(s)

Map prompt.

```text
Task: a first-draft map of a field. Field: [your field].
The specific question to answer: [the question].

Give:
1. The 3 to 6 main positions or camps in this field, and each one's core claim;
2. 2 to 3 representative works per camp (title, authors, year, venue);
3. The real points of disagreement between camps, not differences in wording: substantive conflicts of the form "if A is right, B is wrong";
4. The 1 to 2 disagreements most relevant to the question.

Rules: list only papers you can give a real source for; mark anything you are unsure exists as "unsure".
Every paper you list will be checked in an academic search engine; do not call the map complete or trustworthy.
Paste the question at the top of every reply.
```

Paper card prompt. One card per load-bearing paper; the last field stays blank for the human.

```text
Read this paper and distill it in the format below, no embellishment:
- Core claim (one sentence, in the paper's own wording)
- Evidence (what experiment / data / task, at what scale)
- Where the claim applies (limits the authors admit, in the limitations section and hidden in footnotes)
- Which prior work this paper refutes or depends on
- [Blank] Credence I give it:
Leave the last field empty. Quote qualifiers as written; drop none.
```

Weekly scan prompt. Admission rule, locked: a paper enters the skeleton layer if and only if it could change who wins a row of the map; the rest flows past.

```text
This is a controversy map: [paste the table].
This is this week's new literature: [paste search results].
Output three columns: new evidence relevant to the map / signals the map needs changing (name the row) / noise to ignore.
Mark any paper you cannot give a real source for as "unsure". Change no row's status yourself.
```

## Leak self-check
- [ ] The prompt names the camp you favour or the answer the map should show? Delete it; the map will then find your camp.
- [ ] The paper card prompt asks the model to fill "how much I believe it"? That field is human handwriting. Keep the blank.
- [ ] The weekly scan prompt lets the model change a row's status? It proposes signals only. Keep "change no row's status yourself".
- [ ] The map prompt ran in a session that already argued for one position? Fresh session; the trailer states whether context is shared.

## Before you dispatch
`python scripts/leak_check.py brief briefs/controversy-map.md`

## Trailer
Print this line in your transcript when you dispatch:
verification channel: separate session, <model or person>, brief: briefs/controversy-map.md, leak_check: clean
