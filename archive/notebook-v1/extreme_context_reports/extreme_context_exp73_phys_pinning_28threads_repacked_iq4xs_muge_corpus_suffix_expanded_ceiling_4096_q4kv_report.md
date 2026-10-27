# Extreme Context Needle Retrieval Ladder: Exp73_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Corpus_Suffix_Expanded_Ceiling_4096_Q4KV

- **Timestamp:** `2026-10-05 07:10:12`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32,suffix_corpus=/home/james/Homelab-inference/benchmarks/code_corpus.json -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`137.98 t/s`** | 174.4s | `16.81 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.09 t/s`** | 470.8s | `14.76 t/s` | 21708.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.49 t/s`** | 1466.9s | `12.15 t/s` | 21708.7 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`37.91 t/s`** | 5066.6s | `8.59 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `47032`
- **Decoded Snippet:** `The pass key is 47032.

Please answer on this question's page.

main: decoded 16 tokens in 0.98 s, speed: 16.36 t/s

llama_print_timings:        load time =  198007.74 ms
llama_print_timings:      sa`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `34155`
- **Decoded Snippet:** `The pass key is 34155.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.11 s, speed: 14.42 t/s

llama_print_timings:        load time =  494324.94 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `38402`
- **Decoded Snippet:** `The pass key is 38402.



 The pass key is 38

main: decoded 16 tokens in 1.34 s, speed: 11.91 t/s

llama_print_timings:        load time = 1490489.43 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `1901`
- **Decoded Snippet:** `The pass key is 1901.`
- **Status:** MATCH - ZERO REGRESSION

