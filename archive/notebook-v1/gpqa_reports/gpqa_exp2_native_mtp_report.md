# GPQA (20 Questions) & Long-Context Report: Exp 2: Native MTP Speculation

- **Timestamp:** `2026-09-02 17:51:57`
- **Command:** `numactl --cpunodebind=0 --membind=0 /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 10 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa isolate -fa 1 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1`
- **GPQA Score:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`14.50 t/s`**
- **Average Prompt Speed:** **`104.32 t/s`**
- **4K Context Needle Passkey:** **PASSED**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `14.20 t/s` | 384 |
| 2 | `gpqa_42` | **A** | `A` | PASSED | `14.66 t/s` | 384 |
| 3 | `gpqa_2` | **B** | `None` | FAILED | `15.39 t/s` | 384 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `13.65 t/s` | 384 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `14.09 t/s` | 384 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `14.41 t/s` | 384 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `14.03 t/s` | 384 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `14.32 t/s` | 384 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `13.18 t/s` | 384 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `14.88 t/s` | 384 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `14.94 t/s` | 384 |
| 12 | `gpqa_185` | **A** | `A` | PASSED | `14.84 t/s` | 384 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `14.90 t/s` | 384 |
| 14 | `gpqa_165` | **C** | `None` | FAILED | `14.42 t/s` | 384 |
| 15 | `gpqa_169` | **C** | `A` | FAILED | `14.76 t/s` | 384 |
| 16 | `gpqa_15` | **D** | `C` | FAILED | `13.90 t/s` | 384 |
| 17 | `gpqa_159` | **A** | `C` | FAILED | `14.82 t/s` | 384 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `15.31 t/s` | 384 |
| 19 | `gpqa_134` | **D** | `None` | FAILED | `14.49 t/s` | 384 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `14.83 t/s` | 384 |

| - | `passkey_4k` | **Match** | `Match` | PASSED | `117.48 t/s` | Needle |
