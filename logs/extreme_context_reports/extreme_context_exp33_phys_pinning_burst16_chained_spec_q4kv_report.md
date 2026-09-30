# Extreme Context Needle Retrieval Ladder: Exp33_Phys_Pinning_Burst16_Chained_Spec_Q4KV

- **Timestamp:** `2026-09-17 19:41:27`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 14 -tb 28 --spec-type ngram-mod:n_max=16,ngram_size_n=8,ngram_size_m=24,ngram_min_hits=2 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`149.47 t/s`** | 161.0s | `149.47 t/s` | 20966.2 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`107.76 t/s`** | 446.0s | `107.76 t/s` | 20990.5 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.64 t/s`** | 1420.3s | `67.64 t/s` | 21037.4 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.68 t/s`** | 4965.3s | `38.68 t/s` | 21137.6 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `13203`
- **Decoded Snippet:** `The pass key is 13203. Remember it. 13203

main: decoded 16 tokens in 1.23 s, speed: 12.98 t/s

llama_print_timings:        load time =  178038.70 ms
llama_print_timings:      sample time =       5.5`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `45316`
- **Decoded Snippet:** `The pass key is 45316.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.48 s, speed: 10.80 t/s

llama_print_timings:        load time =  463287.74 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `49649`
- **Decoded Snippet:** `The pass key is 49649.

main: decoded 7 tokens in 0.87 s, speed: 8.05 t/s

llama_print_timings:        load time = 1437596.34 ms
llama_print_timings:      sample time =       2.59 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `43565`
- **Decoded Snippet:** `The pass key is 43565.

main: decoded 7 tokens in 1.28 s, speed: 5.48 t/s

llama_print_timings:        load time = 4982593.63 ms
llama_print_timings:      sample time =       2.50 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

