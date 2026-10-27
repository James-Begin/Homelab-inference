# GPQA (20 Questions) & Long-Context Report: Exp8: Dual NUMA MTP (cache-ram=0)

- **Timestamp:** `2026-09-05 18:33:05`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --interleave=all /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8084 -c 8192 -t 20 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa isolate -fa 1 --cache-ram 0 --numa distribute --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1`
- **GPQA Score:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`20.06 t/s`**
- **Average Prompt Speed:** **`134.19 t/s`**
- **4K Context Needle Passkey:** **PASSED**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `19.67 t/s` | 384 |
| 2 | `gpqa_42` | **A** | `A` | PASSED | `20.34 t/s` | 384 |
| 3 | `gpqa_2` | **B** | `None` | FAILED | `21.40 t/s` | 384 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `18.54 t/s` | 384 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `19.14 t/s` | 384 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `19.92 t/s` | 384 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `19.58 t/s` | 384 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `19.54 t/s` | 384 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `17.80 t/s` | 384 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `20.65 t/s` | 384 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `20.81 t/s` | 384 |
| 12 | `gpqa_185` | **A** | `A` | PASSED | `20.54 t/s` | 384 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `21.15 t/s` | 384 |
| 14 | `gpqa_165` | **C** | `None` | FAILED | `19.94 t/s` | 384 |
| 15 | `gpqa_169` | **C** | `A` | FAILED | `20.40 t/s` | 384 |
| 16 | `gpqa_15` | **D** | `C` | FAILED | `18.99 t/s` | 384 |
| 17 | `gpqa_159` | **A** | `C` | FAILED | `20.84 t/s` | 384 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `21.28 t/s` | 384 |
| 19 | `gpqa_134` | **D** | `None` | FAILED | `20.03 t/s` | 384 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `20.56 t/s` | 384 |

| - | `passkey_4k` | **Match** | `Match` | PASSED | `167.30 t/s` | Needle |
