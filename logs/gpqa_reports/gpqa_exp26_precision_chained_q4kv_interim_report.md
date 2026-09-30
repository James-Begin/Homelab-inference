# Interim GPQA Diamond Report: Exp 26: Precision Chained Speculation (N=8, Hits=3) + Native MTP + Q4_0 KV Cache + SER 2,0.5

- **Experiment ID:** `exp26_precision_chained_q4kv`
- **Execution Status:** **STOPPED ON USER REQUEST** (at Question 11 / 50)
- **Checkpoint File:** [`scratch/exp26_precision_chained_q4kv_checkpoint.json`](file:///home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/scratch/exp26_precision_chained_q4kv_checkpoint.json)
- **Evaluated Questions:** **11 / 50**
- **Score (11Q Interim):** **4 / 11 (36.4%)**
- **Average Generation Speed:** **`18.32 tokens/second`**
- **Peak Generation Speed:** **`20.82 tokens/second`**
- **Configuration:** `numactl --interleave=all ... -t 14 -tb 28 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type ngram-mod:n_max=16,n_min=3,ngram_size_n=8,ngram_min_hits=3 --spec-type mtp:n_max=1,p_min=0.0 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --slot-prompt-similarity 0.0`

## Question-by-Question Breakdown (Evaluated Before Stop)

| # | ID | Gold | Pred | Result | Speed (t/s) |
| :-: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | **CORRECT** | 18.17 |
| 2 | `gpqa_42` | A | A | **CORRECT** | 20.82 |
| 3 | `gpqa_2` | B | None | **WRONG** | 18.38 |
| 4 | `gpqa_156` | A | A | **CORRECT** | 17.93 |
| 5 | `gpqa_128` | A | A | **CORRECT** | 18.93 |
| 6 | `gpqa_12` | D | C | **WRONG** | 18.66 |
| 7 | `gpqa_79` | D | A | **WRONG** | 18.21 |
| 8 | `gpqa_13` | B | C | **WRONG** | 17.00 |
| 9 | `gpqa_127` | D | A | **WRONG** | 15.28 |
| 10 | `gpqa_69` | C | A | **WRONG** | 18.45 |
| 11 | `gpqa_3` | C | B | **WRONG** | 19.66 |

## Interim Summary
All 11 evaluated questions have their completions and timing telemetry preserved in the JSON checkpoint file. Testing was cleanly terminated via `systemctl --user stop` and all server ports were freed.
