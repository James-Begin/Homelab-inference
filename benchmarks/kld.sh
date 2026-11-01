#!/usr/bin/env bash
# Compare a candidate distribution against a cached reference distribution.
set -euo pipefail

if [[ $# -ne 4 ]]; then
    echo "Usage: $0 REFERENCE.gguf CANDIDATE.gguf CORPUS.txt OUTPUT_DIR" >&2
    exit 2
fi
MODEL_REF="$1"
MODEL_CAND="$2"
CORPUS_FILE="$3"
OUT_DIR="$4"
PERPLEXITY_BIN="${IK_LLAMA_BIN:-${IK_LLAMA_HOME:-$HOME/ik_llama.cpp}/build/bin}/llama-perplexity"
for artifact in "$MODEL_REF" "$MODEL_CAND" "$CORPUS_FILE" "$PERPLEXITY_BIN"; do
    [[ -s "$artifact" ]] || { echo "Missing or empty input: $artifact" >&2; exit 1; }
done
[[ -x "$PERPLEXITY_BIN" ]] || { echo "Not executable: $PERPLEXITY_BIN" >&2; exit 1; }
mkdir -p "$OUT_DIR"
REFERENCE_KEY=$(python3 - "$MODEL_REF" "$CORPUS_FILE" "$PERPLEXITY_BIN" <<'PY'
import hashlib
from pathlib import Path
import sys
h = hashlib.sha256(b"context=2048,batch=512,threads=28,interleave=all\0")
for filename in sys.argv[1:]:
    content = hashlib.sha256()
    with Path(filename).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            content.update(chunk)
    h.update(content.digest())
print(h.hexdigest())
PY
)
BASE_KLD="$OUT_DIR/ref_${REFERENCE_KEY}.kld"
if [[ ! -s "$BASE_KLD" ]]; then
    TEMP_BASE="$BASE_KLD.tmp.$$"
    trap 'rm -f "$TEMP_BASE"' EXIT
    numactl --interleave=all "$PERPLEXITY_BIN" -m "$MODEL_REF" -f "$CORPUS_FILE" \
        -c 2048 -b 512 -t 28 --kl-divergence-base "$TEMP_BASE"
    [[ -s "$TEMP_BASE" ]] || { echo "Reference distribution was not produced" >&2; exit 1; }
    mv "$TEMP_BASE" "$BASE_KLD"
    trap - EXIT
fi
numactl --interleave=all "$PERPLEXITY_BIN" -m "$MODEL_CAND" -f "$CORPUS_FILE" \
    -c 2048 -b 512 -t 28 --kl-divergence-base "$BASE_KLD" --kl-divergence 2>&1 | tee "$OUT_DIR/candidate_eval.log"
python3 - "$OUT_DIR/candidate_eval.log" <<'PY'
import math
from pathlib import Path
import re
import sys
text = Path(sys.argv[1]).read_text()
match = re.search(r"Mean\s+KLD:\s+([-+\d.eE]+)", text)
if match is None or not math.isfinite(float(match[1])):
    sys.exit("Candidate did not produce a finite mean KLD statistic")
print(f"Recorded mean KLD: {float(match[1]):.6f}. No acceptance threshold is implied.")
PY
