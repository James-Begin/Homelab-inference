# Extreme Context Needle Retrieval Ladder: Exp85_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Corpus_Suffix_Slot050_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-13 16:38:16`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --slot-save-path /tmp/slots/ --slot-prompt-similarity 0.50 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32,suffix_corpus=/home/james/Homelab-inference/benchmarks/code_corpus.json --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.46 t/s`** | 173.8s | `16.80 t/s` | 21708.9 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.15 t/s`** | 470.5s | `14.90 t/s` | 21708.7 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`65.41 t/s`** | 1468.6s | `12.10 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.94 t/s`** | 5062.1s | `8.64 t/s` | 21709.9 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `35062`
- **Decoded Snippet:** `The pass key is 35062.

main: decoded 7 tokens in 0.43 s, speed: 16.31 t/s

llama_print_timings:        load time =  196603.93 ms
llama_print_timings:      sample time =       2.72 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `15483`
- **Decoded Snippet:** `The pass key is 15483.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `4622`
- **Decoded Snippet:** `The pass key is 4622.

main: decoded 6 tokens in 0.51 s, speed: 11.85 t/s

llama_print_timings:        load time = 1491669.93 ms
llama_print_timings:      sample time =       2.23 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `20978`
- **Decoded Snippet:** `The pass key is 20978.`
- **Status:** MATCH - ZERO REGRESSION

