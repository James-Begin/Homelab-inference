# GPQA (20 Questions) & Long-Context Report: Exp7b: Dual NUMA MTP (threads=28)

- **Timestamp:** `2026-09-05 18:24:22`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --interleave=all /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8084 -c 8192 -t 28 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa isolate -fa 1 --numa distribute --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1`
- **GPQA Score:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`20.34 t/s`**
- **Average Prompt Speed:** **`133.23 t/s`**
- **4K Context Needle Passkey:** **PASSED**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `20.14 t/s` | 384 |
| 2 | `gpqa_42` | **A** | `A` | PASSED | `20.64 t/s` | 384 |
| 3 | `gpqa_2` | **B** | `None` | FAILED | `21.88 t/s` | 384 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `19.32 t/s` | 384 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `19.85 t/s` | 384 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `20.39 t/s` | 384 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `19.99 t/s` | 384 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `20.35 t/s` | 384 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `18.22 t/s` | 384 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `21.12 t/s` | 384 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `21.27 t/s` | 384 |
| 12 | `gpqa_185` | **A** | `A` | PASSED | `20.96 t/s` | 384 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `21.30 t/s` | 384 |
| 14 | `gpqa_165` | **C** | `None` | FAILED | `20.16 t/s` | 384 |
| 15 | `gpqa_169` | **C** | `A` | FAILED | `20.93 t/s` | 384 |
| 16 | `gpqa_15` | **D** | `C` | FAILED | `19.72 t/s` | 384 |
| 17 | `gpqa_159` | **A** | `C` | FAILED | `20.89 t/s` | 384 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `20.21 t/s` | 384 |
| 19 | `gpqa_134` | **D** | `None` | FAILED | `18.47 t/s` | 384 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `21.04 t/s` | 384 |

| - | `passkey_4k` | **Match** | `Match` | PASSED | `166.27 t/s` | Needle |
