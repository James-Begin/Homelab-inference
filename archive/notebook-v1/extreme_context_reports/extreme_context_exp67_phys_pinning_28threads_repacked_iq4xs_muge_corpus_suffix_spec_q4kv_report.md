# Extreme Context Needle Retrieval Ladder: Exp67_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Corpus_Suffix_Spec_Q4KV

- **Timestamp:** `2026-10-04 00:32:53`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48,suffix_corpus=/home/james/Homelab-inference/benchmarks/code_corpus.json -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,063 | **PASSED (100%)** | **`138.71 t/s`** | 173.5s | `16.68 t/s` | 21708.4 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.12 t/s`** | 470.7s | `14.63 t/s` | 21708.5 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.43 t/s`** | 1468.3s | `12.02 t/s` | 21709.3 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.92 t/s`** | 5064.8s | `8.53 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,063 tokens)
- **Expected Passkey:** `8986`
- **Decoded Snippet:** `The pass key is 8986.

main: decoded 6 tokens in 0.37 s, speed: 16.20 t/s

llama_print_timings:        load time =  197122.08 ms
llama_print_timings:      sample time =       2.31 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `46415`
- **Decoded Snippet:** `The pass key is 46415.

The pass key is 464

main: decoded 16 tokens in 1.12 s, speed: 14.29 t/s

llama_print_timings:        load time =  493801.12 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `34993`
- **Decoded Snippet:** `The pass key is 34993.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.36 s, speed: 11.79 t/s

llama_print_timings:        load time = 1490982.55 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `17572`
- **Decoded Snippet:** `The pass key is 17572.



main: decoded 8 tokens in 0.95 s, speed: 8.41 t/s

llama_print_timings:        load time = 5087788.26 ms
llama_print_timings:      sample time =       3.04 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

