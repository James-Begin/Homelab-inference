# GPQA (50 Questions, 1536 Tokens) Report: Exp 4 / 9: Dual NUMA Interleaved Pure Decode (Mega-Kernel)

- **Timestamp:** `2026-09-07 23:44:24`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --interleave=all /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 14 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa distribute -fa 1`
- **GPQA 50Q Score:** **18 / 50 (36.0%)**
- **GPQA 20Q Baseline Subset Score:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`15.72 t/s`**
- **Peak Generation Speed:** **`15.89 t/s`**
- **Average Prompt Speed:** **`135.32 t/s`**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `15.76 t/s` | 1536 |
| 2 | `gpqa_42` | **A** | `A` | PASSED | `15.85 t/s` | 1536 |
| 3 | `gpqa_2` | **B** | `A` | FAILED | `15.71 t/s` | 1536 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `15.78 t/s` | 438 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `15.65 t/s` | 1536 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `15.64 t/s` | 1536 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `15.72 t/s` | 1536 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `15.89 t/s` | 1536 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `15.32 t/s` | 1536 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `15.87 t/s` | 1536 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `15.79 t/s` | 1536 |
| 12 | `gpqa_185` | **A** | `C` | FAILED | `15.75 t/s` | 1536 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `15.83 t/s` | 1536 |
| 14 | `gpqa_165` | **C** | `A` | FAILED | `15.54 t/s` | 1536 |
| 15 | `gpqa_169` | **C** | `C` | PASSED | `15.82 t/s` | 1164 |
| 16 | `gpqa_15` | **D** | `A` | FAILED | `15.85 t/s` | 1536 |
| 17 | `gpqa_159` | **A** | `C` | FAILED | `15.74 t/s` | 1536 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `15.76 t/s` | 1536 |
| 19 | `gpqa_134` | **D** | `A` | FAILED | `15.83 t/s` | 1536 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `15.87 t/s` | 1536 |
| 21 | `gpqa_5` | **C** | `D` | FAILED | `15.74 t/s` | 1536 |
| 22 | `gpqa_53` | **B** | `C` | FAILED | `15.80 t/s` | 1536 |
| 23 | `gpqa_84` | **B** | `C` | FAILED | `15.59 t/s` | 1536 |
| 24 | `gpqa_80` | **D** | `A` | FAILED | `15.57 t/s` | 1536 |
| 25 | `gpqa_64` | **D** | `A` | FAILED | `15.77 t/s` | 1536 |
| 26 | `gpqa_73` | **D** | `A` | FAILED | `15.78 t/s` | 1536 |
| 27 | `gpqa_37` | **A** | `A` | PASSED | `15.58 t/s` | 1536 |
| 28 | `gpqa_126` | **B** | `C` | FAILED | `15.78 t/s` | 1536 |
| 29 | `gpqa_122` | **B** | `A` | FAILED | `15.72 t/s` | 1536 |
| 30 | `gpqa_78` | **A** | `A` | PASSED | `15.62 t/s` | 1536 |
| 31 | `gpqa_160` | **A** | `C` | FAILED | `15.68 t/s` | 1536 |
| 32 | `gpqa_66` | **C** | `C` | PASSED | `15.71 t/s` | 1536 |
| 33 | `gpqa_45` | **C** | `C` | PASSED | `15.74 t/s` | 1536 |
| 34 | `gpqa_184` | **C** | `C` | PASSED | `15.69 t/s` | 950 |
| 35 | `gpqa_32` | **B** | `A` | FAILED | `15.63 t/s` | 1536 |
| 36 | `gpqa_52` | **D** | `C` | FAILED | `15.67 t/s` | 1536 |
| 37 | `gpqa_192` | **C** | `C` | PASSED | `15.72 t/s` | 1536 |
| 38 | `gpqa_174` | **B** | `A` | FAILED | `15.82 t/s` | 1536 |
| 39 | `gpqa_10` | **B** | `A` | FAILED | `15.69 t/s` | 1536 |
| 40 | `gpqa_60` | **D** | `C` | FAILED | `15.64 t/s` | 1536 |
| 41 | `gpqa_170` | **C** | `A` | FAILED | `15.68 t/s` | 1536 |
| 42 | `gpqa_47` | **A** | `A` | PASSED | `15.72 t/s` | 1536 |
| 43 | `gpqa_131` | **A** | `A` | PASSED | `15.68 t/s` | 1536 |
| 44 | `gpqa_103` | **B** | `A` | FAILED | `15.68 t/s` | 1536 |
| 45 | `gpqa_193` | **D** | `D` | PASSED | `15.70 t/s` | 1536 |
| 46 | `gpqa_95` | **D** | `D` | PASSED | `15.68 t/s` | 1536 |
| 47 | `gpqa_144` | **C** | `C` | PASSED | `15.67 t/s` | 1536 |
| 48 | `gpqa_100` | **D** | `B` | FAILED | `15.80 t/s` | 1536 |
| 49 | `gpqa_142` | **C** | `A` | FAILED | `15.68 t/s` | 1536 |
| 50 | `gpqa_61` | **B** | `A` | FAILED | `15.68 t/s` | 1536 |
