# Extreme Context Needle Retrieval Ladder: Exp63_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_3Experts_Pruning_Q4KV

- **Timestamp:** `2026-10-02 19:16:06`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 -muge --override-kv qwen35moe.expert_used_count=int:3 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,063 | **PASSED (100%)** | **`141.94 t/s`** | 169.5s | `141.94 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`104.01 t/s`** | 462.1s | `104.01 t/s` | 21708.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`66.14 t/s`** | 1452.5s | `66.14 t/s` | 21709.1 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.17 t/s`** | 5032.5s | `38.17 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,063 tokens)
- **Expected Passkey:** `3540`
- **Decoded Snippet:** `The pass key is 3540.



main: decoded 7 tokens in 0.43 s, speed: 16.11 t/s

llama_print_timings:        load time =  192289.28 ms
llama_print_timings:      sample time =       2.67 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `24415`
- **Decoded Snippet:** `The pass key is 24415.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `36963`
- **Decoded Snippet:** `The pass key is 36963.

The pass key is 369

main: decoded 16 tokens in 1.37 s, speed: 11.66 t/s

llama_print_timings:        load time = 1475395.43 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `25768`
- **Decoded Snippet:** `The pass key is 25768.

main: decoded 7 tokens in 0.84 s, speed: 8.38 t/s

llama_print_timings:        load time = 5055446.95 ms
llama_print_timings:      sample time =       2.66 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

