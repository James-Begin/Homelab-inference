# GPQA (20 Questions) & Long-Context Report: Baseline GPQA

- **Timestamp:** `2026-09-02 17:18:00`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --cpunodebind=0 --membind=0 /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8084 -c 8192 -t 10 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa isolate -fa 1 `
- **GPQA Score:** **4 / 20 (20.0%)**
- **Average Generation Speed:** **`11.40 t/s`**
- **Average Prompt Speed:** **`124.31 t/s`**
- **4K Context Needle Passkey:** **PASSED**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `11.04 t/s` | 384 |
| 2 | `gpqa_42` | **A** | `A` | PASSED | `11.41 t/s` | 384 |
| 3 | `gpqa_2` | **B** | `A` | FAILED | `11.43 t/s` | 384 |
| 4 | `gpqa_156` | **A** | `B` | FAILED | `11.35 t/s` | 384 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `11.42 t/s` | 384 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `11.28 t/s` | 384 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `11.48 t/s` | 384 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `11.45 t/s` | 384 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `10.98 t/s` | 384 |
| 10 | `gpqa_69` | **C** | `A` | FAILED | `11.49 t/s` | 384 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `11.50 t/s` | 384 |
| 12 | `gpqa_185` | **A** | `None` | FAILED | `11.46 t/s` | 384 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `11.47 t/s` | 384 |
| 14 | `gpqa_165` | **C** | `D` | FAILED | `11.38 t/s` | 384 |
| 15 | `gpqa_169` | **C** | `None` | FAILED | `11.49 t/s` | 384 |
| 16 | `gpqa_15` | **D** | `A` | FAILED | `11.52 t/s` | 384 |
| 17 | `gpqa_159` | **A** | `B` | FAILED | `11.41 t/s` | 384 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `11.48 t/s` | 384 |
| 19 | `gpqa_134` | **D** | `None` | FAILED | `11.46 t/s` | 384 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `11.48 t/s` | 384 |

| - | `passkey_4k` | **Match** | `Match` | PASSED | `133.57 t/s` | Needle |
