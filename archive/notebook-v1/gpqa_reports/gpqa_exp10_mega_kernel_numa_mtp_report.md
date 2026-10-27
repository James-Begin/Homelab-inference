# GPQA (20 Questions) & Long-Context Report: Exp 10: Dual NUMA + AVX2 Prefetching Mega-Kernel + Native MTP

- **Timestamp:** `2026-09-06 15:27:47`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --interleave=all /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 14 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa distribute -fa 1 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1`
- **GPQA Score:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`19.98 t/s`**
- **Peak Generation Speed:** **`21.44 t/s`**
- **Average Prompt Speed:** **`123.55 t/s`**
- **4K Context Needle Passkey:** **PASSED (165.24 t/s)**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `19.57 t/s` | 384 |
| 2 | `gpqa_42` | **A** | `A` | PASSED | `19.94 t/s` | 384 |
| 3 | `gpqa_2` | **B** | `None` | FAILED | `21.44 t/s` | 384 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `18.23 t/s` | 384 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `18.95 t/s` | 384 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `19.60 t/s` | 384 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `19.43 t/s` | 384 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `19.44 t/s` | 384 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `17.61 t/s` | 384 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `20.83 t/s` | 384 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `20.96 t/s` | 384 |
| 12 | `gpqa_185` | **A** | `A` | PASSED | `20.63 t/s` | 384 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `20.99 t/s` | 384 |
| 14 | `gpqa_165` | **C** | `None` | FAILED | `19.80 t/s` | 384 |
| 15 | `gpqa_169` | **C** | `A` | FAILED | `20.50 t/s` | 384 |
| 16 | `gpqa_15` | **D** | `C` | FAILED | `19.09 t/s` | 384 |
| 17 | `gpqa_159` | **A** | `C` | FAILED | `20.66 t/s` | 384 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `21.36 t/s` | 384 |
| 19 | `gpqa_134` | **D** | `None` | FAILED | `20.00 t/s` | 384 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `20.49 t/s` | 384 |

| - | `passkey_4k` | **Match** | `Match` | PASSED | `165.24 t/s` | Needle |
