# Extreme Context Needle Retrieval Ladder: Exp43_Phys_Pinning_28threads_Suffix_Nmax8_Match5_Q4KV

- **Timestamp:** `2026-09-20 16:13:57`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`149.71 t/s`** | 160.7s | `149.71 t/s` | 20966.4 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`107.64 t/s`** | 446.5s | `107.64 t/s` | 20991.4 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.74 t/s`** | 1418.2s | `67.74 t/s` | 21037.9 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`38.74 t/s`** | 4958.0s | `38.74 t/s` | 21137.2 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `26929`
- **Decoded Snippet:** `The pass key is 26929.

<think>
The user wants me to identify

main: decoded 16 tokens in 1.10 s, speed: 14.61 t/s

llama_print_timings:        load time =  177981.83 ms
llama_print_timings:      sam`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `13646`
- **Decoded Snippet:** `The pass key is 13646.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `18144`
- **Decoded Snippet:** `The pass key is 18144.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.49 s, speed: 10.71 t/s

llama_print_timings:        load time = 1435477.36 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `5012`
- **Decoded Snippet:** `The pass key is 5012.

main: decoded 6 tokens in 0.76 s, speed: 7.90 t/s

llama_print_timings:        load time = 4975715.91 ms
llama_print_timings:      sample time =       2.17 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

