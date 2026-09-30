# GPQA (50 Questions, 1536 Tokens) Report: Exp 5 / 10: Dual NUMA + Native MTP (Mega-Kernel)

- **Timestamp:** `2026-09-08 00:51:31`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --interleave=all /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 14 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa distribute -fa 1 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1`
- **GPQA 50Q Score:** **22 / 50 (44.0%)**
- **GPQA 20Q Baseline Subset Score:** **9 / 20 (45.0%)**
- **Average Generation Speed:** **`19.26 t/s`**
- **Peak Generation Speed:** **`21.10 t/s`**
- **Average Prompt Speed:** **`127.39 t/s`**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `18.97 t/s` | 1536 |
| 2 | `gpqa_42` | **A** | `A` | PASSED | `19.78 t/s` | 1536 |
| 3 | `gpqa_2` | **B** | `None` | FAILED | `21.10 t/s` | 1536 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `18.90 t/s` | 498 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `19.18 t/s` | 1536 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `18.88 t/s` | 1536 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `18.64 t/s` | 1536 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `17.27 t/s` | 1536 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `18.06 t/s` | 1536 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `19.90 t/s` | 1536 |
| 11 | `gpqa_3` | **C** | `A` | FAILED | `19.19 t/s` | 1536 |
| 12 | `gpqa_185` | **A** | `A` | PASSED | `19.28 t/s` | 1536 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `19.21 t/s` | 1536 |
| 14 | `gpqa_165` | **C** | `A` | FAILED | `18.07 t/s` | 1536 |
| 15 | `gpqa_169` | **C** | `C` | PASSED | `21.05 t/s` | 1086 |
| 16 | `gpqa_15` | **D** | `C` | FAILED | `18.79 t/s` | 1536 |
| 17 | `gpqa_159` | **A** | `C` | FAILED | `20.08 t/s` | 1536 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `20.48 t/s` | 1536 |
| 19 | `gpqa_134` | **D** | `A` | FAILED | `19.69 t/s` | 1536 |
| 20 | `gpqa_44` | **C** | `C` | PASSED | `19.78 t/s` | 1536 |
| 21 | `gpqa_5` | **C** | `C` | PASSED | `20.29 t/s` | 1536 |
| 22 | `gpqa_53` | **B** | `C` | FAILED | `18.88 t/s` | 1536 |
| 23 | `gpqa_84` | **B** | `B` | PASSED | `19.61 t/s` | 1356 |
| 24 | `gpqa_80` | **D** | `A` | FAILED | `17.88 t/s` | 1536 |
| 25 | `gpqa_64` | **D** | `A` | FAILED | `18.96 t/s` | 1536 |
| 26 | `gpqa_73` | **D** | `D` | PASSED | `19.76 t/s` | 1536 |
| 27 | `gpqa_37` | **A** | `A` | PASSED | `18.81 t/s` | 1536 |
| 28 | `gpqa_126` | **B** | `A` | FAILED | `19.95 t/s` | 1536 |
| 29 | `gpqa_122` | **B** | `A` | FAILED | `19.78 t/s` | 1536 |
| 30 | `gpqa_78` | **A** | `A` | PASSED | `18.31 t/s` | 1536 |
| 31 | `gpqa_160` | **A** | `C` | FAILED | `18.33 t/s` | 1536 |
| 32 | `gpqa_66` | **C** | `None` | FAILED | `19.68 t/s` | 1536 |
| 33 | `gpqa_45` | **C** | `C` | PASSED | `19.17 t/s` | 1536 |
| 34 | `gpqa_184` | **C** | `C` | PASSED | `20.36 t/s` | 867 |
| 35 | `gpqa_32` | **B** | `A` | FAILED | `18.96 t/s` | 1536 |
| 36 | `gpqa_52` | **D** | `A` | FAILED | `18.72 t/s` | 1536 |
| 37 | `gpqa_192` | **C** | `C` | PASSED | `19.04 t/s` | 1536 |
| 38 | `gpqa_174` | **B** | `A` | FAILED | `19.06 t/s` | 1536 |
| 39 | `gpqa_10` | **B** | `A` | FAILED | `18.11 t/s` | 1536 |
| 40 | `gpqa_60` | **D** | `A` | FAILED | `19.03 t/s` | 1536 |
| 41 | `gpqa_170` | **C** | `A` | FAILED | `18.54 t/s` | 1536 |
| 42 | `gpqa_47` | **A** | `A` | PASSED | `18.86 t/s` | 1536 |
| 43 | `gpqa_131` | **A** | `A` | PASSED | `19.15 t/s` | 1536 |
| 44 | `gpqa_103` | **B** | `A` | FAILED | `19.32 t/s` | 1536 |
| 45 | `gpqa_193` | **D** | `D` | PASSED | `20.43 t/s` | 1536 |
| 46 | `gpqa_95` | **D** | `D` | PASSED | `20.54 t/s` | 1536 |
| 47 | `gpqa_144` | **C** | `C` | PASSED | `19.60 t/s` | 1536 |
| 48 | `gpqa_100` | **D** | `A` | FAILED | `19.01 t/s` | 1536 |
| 49 | `gpqa_142` | **C** | `A` | FAILED | `19.17 t/s` | 1536 |
| 50 | `gpqa_61` | **B** | `A` | FAILED | `19.27 t/s` | 1536 |
