# GPQA (20 Questions) & Long-Context Report: Exp 5: Dual-Socket NUMA + Native MTP

- **Timestamp:** `2026-09-02 18:23:21`
- **Command:** `numactl --interleave=all /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 14 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa distribute -fa 1 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1`
- **GPQA Score:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`21.02 t/s`**
- **Average Prompt Speed:** **`135.46 t/s`**
- **4K Context Needle Passkey:** **PASSED**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `17.84 t/s` | 384 |
| 2 | `gpqa_42` | **A** | `A` | PASSED | `21.54 t/s` | 384 |
| 3 | `gpqa_2` | **B** | `None` | FAILED | `22.91 t/s` | 384 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `19.51 t/s` | 384 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `20.24 t/s` | 384 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `20.92 t/s` | 384 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `20.38 t/s` | 384 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `20.88 t/s` | 384 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `18.75 t/s` | 384 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `21.94 t/s` | 384 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `22.18 t/s` | 384 |
| 12 | `gpqa_185` | **A** | `A` | PASSED | `21.86 t/s` | 384 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `22.13 t/s` | 384 |
| 14 | `gpqa_165` | **C** | `None` | FAILED | `20.74 t/s` | 384 |
| 15 | `gpqa_169` | **C** | `A` | FAILED | `21.58 t/s` | 384 |
| 16 | `gpqa_15` | **D** | `C` | FAILED | `20.18 t/s` | 384 |
| 17 | `gpqa_159` | **A** | `C` | FAILED | `21.80 t/s` | 384 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `22.68 t/s` | 384 |
| 19 | `gpqa_134` | **D** | `None` | FAILED | `20.95 t/s` | 384 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `21.47 t/s` | 384 |

| - | `passkey_4k` | **Match** | `Match` | PASSED | `177.57 t/s` | Needle |
