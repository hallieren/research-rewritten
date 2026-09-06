# Data licensing check (Task 0, 2026-07-24)

## Verdict

**WVS Wave 7 is usable for this project.** Non-commercial book research is a
permitted use; the raw respondent-level CSV must NOT be committed to this (or
any public) repo. `data/` stays gitignored and the code ships a loader only.

## ① Can we use WVS-7 for non-commercial book research?

**Yes.** WVS data is freely available at no cost for non-commercial purposes
(research, academic publications, teaching). Access requires a lightweight
registration at download time: you enter your name and intended data usage and
tick an "I have read the Conditions of Use" box before the download starts.
The IHSN catalog entry for the USA WVS-7 study states the data "is freely
available from the World Values Survey website at no cost" with a mandatory
citation and a no-liability disclaimer for the collectors/distributors.

Required citation (from the IHSN/WVS access-conditions text):

> Haerpfer, C., Inglehart, R., Moreno, A., Welzel, C., Kizilova, K.,
> Diez-Medrano J., M. Lagos, P. Norris, E. Ponarin & B. Puranen (eds.). 2022.
> World Values Survey: Round Seven — Country-Pooled Datafile Version 6.0.
> Madrid, Spain & Vienna, Austria: JD Systems Institute & WVSA Secretariat.

## ② Can the raw CSV be committed to a public repo?

**No.** The WVS conditions of use accepted at download time prohibit
redistribution of the original respondent-level data files; each user must
download their own copy from worldvaluessurvey.org (this is why third-party
tutorials walk users through the official download flow instead of mirroring
the file). Consequence for this repo: `data/` is in `.gitignore`, the code
contains only a loader (`src/persona_panel/wvs.py`), and the README instructs
the author to download the CSV themselves.

## ③ Download steps for the author

1. Go to https://www.worldvaluessurvey.org → Data and Documentation → Data
   Download → Wave 7 (2017-2022) (direct entry point:
   https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp).
2. Pick the cross-national data file, version **6.0**, in **CSV** format
   (regular layout or the "inverted" release with P-suffixed columns, the
   prepare script accepts either) (also offered: R,
   SAS, Stata, SPSS).
3. Fill in name + intended usage, tick "I have read the Conditions of Use",
   download the .zip, extract the CSV.
4. Run `uv run python scripts/prepare_wvs.py <path-to-official-csv>` to write
   the USA slice as `data/wvs7_usa.csv` in this repo (gitignored) plus the
   committed aggregates; for the inverted layout the script maps the P-suffixed
   columns back to official-codebook coding.

## ④ What the repo ships instead (added 2026-09-05)

`data/wvs7_usa_aggregates.json`: for each of the six pre-registered subgroups
and each of the 15 questions, the count of respondents per answer option
(WVS missing codes already dropped). These are derived summary statistics of
the kind published in any paper that uses WVS, not the respondent-level file
the conditions of use protect, so committing them is within the license as we
read it. Anyone who wants the rows still downloads them from WVS; the
aggregates exist so `report` can reproduce the readout without registration.
Attribution requirement (the citation above) applies to the aggregates too.

## Fallback: Pew Research Center datasets

Checked as the designated fallback; usable but not needed. Pew grants a
"nonexclusive, non-sublicensable, non-transferable, revocable, worldwide, and
royalty-free license" to use its survey datasets, but any reproduction or
distribution "is limited to excerpts and may not be reproduced ... in full or
substantially in full", i.e. the same no-raw-data-in-repo constraint applies.
Download requires a free Pew account and acceptance of their terms; required
disclaimer: "Pew Research Center bears no responsibility for the analyses or
interpretations of the data presented here."

## Sources consulted (2026-07-24)

- WVS documentation / Wave 7 download entry:
  https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp
- IHSN survey catalog, "United States — World Values Survey — Wave 7, 2017"
  (access policy, citation requirement, disclaimer):
  https://datacatalog.ihsn.org/catalog/12312
- Third-party walkthrough of the official WVS download flow (registration,
  purpose statement, conditions-of-use checkbox, CSV format):
  https://github.com/maugavilla/well_hello_stats/blob/main/tutorials/2_1_download_WVS.md
- Pew Research Center Terms of Use (dataset license, excerpt-only
  redistribution, attribution):
  https://www.pewresearch.org/about/terms-and-conditions/
- Pew dataset download instructions (account required):
  https://www.pewresearch.org/instructions-for-downloading-datasets/
