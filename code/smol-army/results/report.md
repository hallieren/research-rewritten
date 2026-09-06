# Results

| family | arm | n | accuracy | USD/query |
|---|---|---|---|---|
| code | army_debate | 100 | 0.940 | 0.00083 |
| code | army_division | 100 | 0.940 | 0.00108 |
| code | army_vote | 300 | 0.937 | 0.00053 |
| code | frontier | 100 | 0.960 | 0.00269 |
| code | probe_gptoss | 20 | 1.000 | 0.00008 |
| code | probe_ministral | 20 | 1.000 | 0.00007 |
| code | probe_qwen | 20 | 1.000 | 0.00011 |
| code | self_consistency | 300 | 0.947 | 0.00041 |
| math | army_debate | 100 | 1.000 | 0.00152 |
| math | army_division | 100 | 1.000 | 0.00103 |
| math | army_vote | 450 | 0.856 | 0.00199 |
| math | frontier | 150 | 0.673 | 0.00195 |
| math | probe_gptoss | 20 | 0.850 | 0.00004 |
| math | probe_ministral | 20 | 0.850 | 0.00006 |
| math | probe_qwen | 20 | 0.200 | 0.00058 |
| math | self_consistency | 450 | 0.733 | 0.00041 |
| mmlu_pro | army_debate | 100 | 0.740 | 0.00228 |
| mmlu_pro | army_division | 100 | 0.630 | 0.00125 |
| mmlu_pro | army_vote | 450 | 0.644 | 0.00223 |
| mmlu_pro | frontier | 150 | 0.793 | 0.00498 |
| mmlu_pro | probe_gptoss | 20 | 0.750 | 0.00013 |
| mmlu_pro | probe_ministral | 20 | 0.700 | 0.00020 |
| mmlu_pro | probe_qwen | 20 | 0.400 | 0.00052 |
| mmlu_pro | self_consistency | 450 | 0.616 | 0.00083 |

## Army vs frontier (paired bootstrap, ε = 2pp)

| family | arm | Δacc (arm − frontier) | 95% CI | verdict |
|---|---|---|---|---|
| code | army_vote | -0.023 | [-0.060, +0.017] | inconclusive |
| code | self_consistency | -0.013 | [-0.037, +0.010] | inconclusive |
| code | army_debate | -0.020 | [-0.070, +0.030] | inconclusive |
| code | army_division | -0.020 | [-0.070, +0.030] | inconclusive |
| math | army_vote | +0.182 | [+0.127, +0.242] | army_ahead |
| math | self_consistency | +0.060 | [+0.031, +0.091] | army_ahead |
| math | army_debate | +0.000 | [+0.000, +0.000] | tie |
| math | army_division | +0.000 | [+0.000, +0.000] | tie |
| mmlu_pro | army_vote | -0.149 | [-0.213, -0.087] | army_behind |
| mmlu_pro | self_consistency | -0.178 | [-0.249, -0.109] | army_behind |
| mmlu_pro | army_debate | -0.080 | [-0.150, -0.010] | inconclusive |
| mmlu_pro | army_division | -0.190 | [-0.280, -0.100] | army_behind |
