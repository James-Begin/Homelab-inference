# GPQA (20 Questions) & Long-Context Report: Exp7a: Dual NUMA MTP (threads=20)

- **Timestamp:** `2026-09-05 18:15:40`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --interleave=all /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8084 -c 8192 -t 20 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa isolate -fa 1 --numa distribute --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1`
- **GPQA Score:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`19.94 t/s`**
- **Average Prompt Speed:** **`129.67 t/s`**
- **4K Context Needle Passkey:** **PASSED**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `19.60 t/s` | 384 |
| 2 | `gpqa_42` | **A** | `A` | PASSED | `20.17 t/s` | 384 |
| 3 | `gpqa_2` | **B** | `None` | FAILED | `21.28 t/s` | 384 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `18.35 t/s` | 384 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `19.36 t/s` | 384 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `19.58 t/s` | 384 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `19.50 t/s` | 384 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `19.62 t/s` | 384 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `17.65 t/s` | 384 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `20.74 t/s` | 384 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `20.59 t/s` | 384 |
| 12 | `gpqa_185` | **A** | `A` | PASSED | `20.45 t/s` | 384 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `20.75 t/s` | 384 |
| 14 | `gpqa_165` | **C** | `None` | FAILED | `19.62 t/s` | 384 |
| 15 | `gpqa_169` | **C** | `A` | FAILED | `20.33 t/s` | 384 |
| 16 | `gpqa_15` | **D** | `C` | FAILED | `19.08 t/s` | 384 |
| 17 | `gpqa_159` | **A** | `C` | FAILED | `20.26 t/s` | 384 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `21.21 t/s` | 384 |
| 19 | `gpqa_134` | **D** | `None` | FAILED | `20.04 t/s` | 384 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `20.63 t/s` | 384 |

| - | `passkey_4k` | **Match** | `Match` | PASSED | `165.77 t/s` | Needle |
