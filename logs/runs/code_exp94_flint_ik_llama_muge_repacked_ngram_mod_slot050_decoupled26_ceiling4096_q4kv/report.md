# Coding Benchmark Report: Exp 94: Recursive Flint 40B MoE on ik_llama.cpp (Merged Up/Gate -muge 1 + AVX2 64-Byte Repacking Q4_0_R8 + N-Gram Mod Speculation n_max=4, match=4 + Slot Cache 0.50 + Decoupled Prefill -tb 26)
- **Run ID:** `code_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv`
- **Protocol:** Protocol C-code-v1 (EvalPlus HumanEval+)
- **Model:** `RecursiveSI_flint-Q4_0_Repacked.gguf`
- **Total Problems:** 164
- **Base Pass@1:** **96.95%**
- **Plus Pass@1:** **90.85%**
- **Average Decode Speed:** 20.77 tokens/sec
- **Total Wall Time:** 17955.0s (299.2 min)
- **Average Time Per Task:** 109.48s
