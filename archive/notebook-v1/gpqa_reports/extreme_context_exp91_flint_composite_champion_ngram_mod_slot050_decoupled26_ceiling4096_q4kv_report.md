# Extreme Context Needle Retrieval Ladder: Exp91_Flint_Composite_Champion_Ngram_Mod_Slot050_Decoupled26_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-24 03:02:26`
- **Model:** `/home/james/ik_llama.cpp/build/models/RecursiveSI_flint-Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 26 --spec-type ngram-mod --spec-ngram-mod-n-max 4 --spec-ngram-mod-n-match 4 -ctk q4_0 -ctv q4_0 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 25,000 | **FAILED** | **`0.00 t/s`** | 0.0s | `0.00 t/s` | 11.8 MB |
| **32K Context** | 50,000 | **FAILED** | **`0.00 t/s`** | 0.0s | `0.00 t/s` | 11.4 MB |
| **64K Context** | 100,000 | **FAILED** | **`0.00 t/s`** | 0.0s | `0.00 t/s` | 11.4 MB |
| **128K Context** | 200,000 | **FAILED** | **`0.00 t/s`** | 0.0s | `0.00 t/s` | 11.4 MB |

## Detailed Needle Extractions

### 16K Context (25,000 tokens)
- **Expected Passkey:** `None`
- **Decoded Snippet:** ``
- **Status:** MISMATCH

### 32K Context (50,000 tokens)
- **Expected Passkey:** `None`
- **Decoded Snippet:** ``
- **Status:** MISMATCH

### 64K Context (100,000 tokens)
- **Expected Passkey:** `None`
- **Decoded Snippet:** ``
- **Status:** MISMATCH

### 128K Context (200,000 tokens)
- **Expected Passkey:** `None`
- **Decoded Snippet:** ``
- **Status:** MISMATCH

