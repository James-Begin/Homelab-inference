# GPQA (50 Questions, 1536 Tokens) Report: Exp 0: Baseline (Single NUMA Pure Decode)

- **Timestamp:** `2026-09-08 04:14:06`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --cpunodebind=0 --membind=0 /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 14 -tb 14 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack -fa 1`
- **GPQA 50Q Score:** **16 / 50 (32.0%)**
- **GPQA 20Q Baseline Subset Score:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`11.16 t/s`**
- **Peak Generation Speed:** **`11.27 t/s`**
- **Average Prompt Speed:** **`111.94 t/s`**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `11.09 t/s` | 1536 |
| 2 | `gpqa_42` | **A** | `A` | PASSED | `11.09 t/s` | 1536 |
| 3 | `gpqa_2` | **B** | `B` | PASSED | `11.15 t/s` | 1087 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `11.13 t/s` | 1536 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `11.13 t/s` | 1536 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `11.11 t/s` | 1536 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `11.17 t/s` | 1536 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `11.15 t/s` | 1536 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `10.87 t/s` | 1536 |
| 10 | `gpqa_69` | **C** | `A` | FAILED | `11.15 t/s` | 1536 |
| 11 | `gpqa_3` | **C** | `D` | FAILED | `11.15 t/s` | 1536 |
| 12 | `gpqa_185` | **A** | `C` | FAILED | `11.15 t/s` | 1536 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `11.16 t/s` | 1536 |
| 14 | `gpqa_165` | **C** | `A` | FAILED | `11.06 t/s` | 1536 |
| 15 | `gpqa_169` | **C** | `A` | FAILED | `11.16 t/s` | 1536 |
| 16 | `gpqa_15` | **D** | `A` | FAILED | `11.14 t/s` | 1536 |
| 17 | `gpqa_159` | **A** | `A` | PASSED | `11.17 t/s` | 1018 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `11.15 t/s` | 1536 |
| 19 | `gpqa_134` | **D** | `A` | FAILED | `11.14 t/s` | 1265 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `11.15 t/s` | 1536 |
| 21 | `gpqa_5` | **C** | `C` | PASSED | `11.12 t/s` | 1536 |
| 22 | `gpqa_53` | **B** | `A` | FAILED | `11.14 t/s` | 1536 |
| 23 | `gpqa_84` | **B** | `A` | FAILED | `11.13 t/s` | 1536 |
| 24 | `gpqa_80` | **D** | `A` | FAILED | `11.13 t/s` | 1536 |
| 25 | `gpqa_64` | **D** | `A` | FAILED | `11.13 t/s` | 1536 |
| 26 | `gpqa_73` | **D** | `A` | FAILED | `11.13 t/s` | 1536 |
| 27 | `gpqa_37` | **A** | `B` | FAILED | `11.18 t/s` | 1536 |
| 28 | `gpqa_126` | **B** | `A` | FAILED | `11.22 t/s` | 1536 |
| 29 | `gpqa_122` | **B** | `B` | PASSED | `11.22 t/s` | 1536 |
| 30 | `gpqa_78` | **A** | `A` | PASSED | `11.20 t/s` | 1536 |
| 31 | `gpqa_160` | **A** | `A` | PASSED | `11.23 t/s` | 1536 |
| 32 | `gpqa_66` | **C** | `A` | FAILED | `11.23 t/s` | 1536 |
| 33 | `gpqa_45` | **C** | `C` | PASSED | `11.24 t/s` | 1536 |
| 34 | `gpqa_184` | **C** | `C` | PASSED | `11.27 t/s` | 835 |
| 35 | `gpqa_32` | **B** | `None` | FAILED | `11.20 t/s` | 1536 |
| 36 | `gpqa_52` | **D** | `A` | FAILED | `11.20 t/s` | 1536 |
| 37 | `gpqa_192` | **C** | `A` | FAILED | `11.21 t/s` | 1536 |
| 38 | `gpqa_174` | **B** | `A` | FAILED | `11.21 t/s` | 1536 |
| 39 | `gpqa_10` | **B** | `A` | FAILED | `11.15 t/s` | 1536 |
| 40 | `gpqa_60` | **D** | `C` | FAILED | `11.18 t/s` | 1536 |
| 41 | `gpqa_170` | **C** | `A` | FAILED | `11.21 t/s` | 1536 |
| 42 | `gpqa_47` | **A** | `A` | PASSED | `11.22 t/s` | 1536 |
| 43 | `gpqa_131` | **A** | `A` | PASSED | `11.21 t/s` | 1536 |
| 44 | `gpqa_103` | **B** | `A` | FAILED | `11.22 t/s` | 1536 |
| 45 | `gpqa_193` | **D** | `A` | FAILED | `11.20 t/s` | 1536 |
| 46 | `gpqa_95` | **D** | `A` | FAILED | `11.20 t/s` | 1536 |
| 47 | `gpqa_144` | **C** | `C` | PASSED | `11.19 t/s` | 1536 |
| 48 | `gpqa_100` | **D** | `A` | FAILED | `11.20 t/s` | 1536 |
| 49 | `gpqa_142` | **C** | `A` | FAILED | `11.18 t/s` | 1536 |
| 50 | `gpqa_61` | **B** | `A` | FAILED | `11.20 t/s` | 1536 |
