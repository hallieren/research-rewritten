# Caching layer evaluation, criteria

Hypothesis: the new caching layer lowers p99 latency compared with the current layer under production-like traffic.

Arms: current layer (the baseline, what runs in production today) and new layer.

Primary basis: p99 latency on the week's traffic sample.
Sensitivity basis: p95 latency and mean latency, reported alongside.

Win: p99 latency improves by at least 20% against the baseline.

Method: replay one week of sampled requests through both layers, compute p99 per arm, compare.

Confounders: region mix (us, eu, apac) and time-of-day traffic shape; the same replay set feeds both arms.

Filing: results land in results/, and any change to this file is recorded in CHANGES.md.
