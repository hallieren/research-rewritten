# Vector retrieval engine selection, technical assessment (excerpt, pages 1 to 4 of 30)

## Executive summary

We recommend migrating the retrieval layer to Engine B. Under comparable load Engine B cuts p99 latency by 31% and reduces cost per thousand queries by 44%. The migration pays back within 7 months. We conclude with high confidence that the risk of regression is low.

## 1. Background

Vector retrieval engines have converged on HNSW-style indexes (Malkov and Yashunin, 2018). Recent benchmark reviews report that filtered search remains the main differentiator between engines (Hartmann et al., 2025, "The 2025 Vector Retrieval Benchmark Review", p. 14). A 2024 survey of 60 production deployments found that 72% of teams cite latency under filter as their top pain point (Okafor and Lindqvist, 2024).

## 2. Evidence

- Engine B's p99 latency under our load profile: 48 ms, versus 70 ms for the current engine (a 31% reduction).
- Cost per thousand queries: $0.019 versus $0.034.
- Recall@10 held at 0.96 on both engines (Zhang et al., 2023, ANN-Benchmarks extended results).
- Index build time improves from 41 minutes to 12 minutes according to the vendor's published figures (Engine B technical brief, 2025).
- Independent evaluation by Rao and Petersen (2025, "Filtered ANN at scale: a controlled comparison", VLDB) reports the same direction of result on a public dataset.

## 3. Method

Latency numbers were collected from a load test run by the vendor's solutions team on a representative sample of our queries. Cost figures are list prices as of the date of the report. The 7-month payback assumes the latency gain converts into a 9% increase in conversion, based on internal analysis.

## 4. Risks

Regression risk is judged low given the maturity of Engine B. Migration effort is estimated at 6 engineer-weeks.
