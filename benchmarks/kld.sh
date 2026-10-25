#!/usr/bin/env bash
# Protocol Q: KL Divergence & Perplexity Evaluation (Q-kld-v1)
# Implements Phase 3 (Protocol Q) of improvement-plan.md.
# Evaluates distributional shift and top-1 token agreement for lossy changes.

set -euo pipefail

MODEL_REF="${1:-/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf}"
MODEL_CAND="${2:-/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf}"
CORPUS_FILE="${3:-/home/james/Homelab-inference/benchmarks/corpus_kld.txt}"
OUT_DIR="${4:-/home/james/Homelab-inference/logs/kld}"
PERPLEXITY_BIN="/home/james/ik_llama.cpp/build/bin/llama-perplexity"

mkdir -p "$OUT_DIR"
BASE_KLD="$OUT_DIR/ref_baseline.kld"

echo "=========================================================="
echo "Protocol Q: KL Divergence & Distribution Divergence (Q-kld-v1)"
echo "Reference Model: $MODEL_REF"
echo "Candidate Model: $MODEL_CAND"
echo "Corpus:          $CORPUS_FILE"
echo "=========================================================="

# Check if reference KLD baseline needs generation
if [[ ! -f "$BASE_KLD" ]]; then
    echo "Computing reference base distribution ($BASE_KLD)..."
    numactl --interleave=all "$PERPLEXITY_BIN" \
        -m "$MODEL_REF" \
        -f "$CORPUS_FILE" \
        -c 2048 -b 512 \
        -t 28 \
        --kl-divergence-base "$BASE_KLD"
    echo "Reference base distribution computed."
fi

echo "Evaluating candidate model against reference base..."
numactl --interleave=all "$PERPLEXITY_BIN" \
    -m "$MODEL_CAND" \
    -f "$CORPUS_FILE" \
    -c 2048 -b 512 \
    -t 28 \
    --kl-divergence-base "$BASE_KLD" \
    --kl-divergence 2>&1 | tee "$OUT_DIR/candidate_eval.log"

echo "Protocol Q evaluation complete. Output saved to $OUT_DIR/candidate_eval.log."
