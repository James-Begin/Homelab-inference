#!/usr/bin/env bash
# Automated Engine Build & Patch Pipeline
# Implements Phase 4 (Task 4.3) of improvement-plan.md.
# Clones or updates ik_llama.cpp, applies patches, and compiles with Broadwell AVX2 flags.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ENGINE_DIR="${1:-/home/james/ik_llama.cpp}"
UPSTREAM_SHA="87fc8701"
PATCH_FILE="$REPO_ROOT/patches/0000-all-homelab-optimizations.patch"

echo "=========================================================="
echo "Homelab Inference: Engine Build & Provenance Pipeline"
echo "Engine Directory: $ENGINE_DIR"
echo "Target Base SHA:  $UPSTREAM_SHA"
echo "Patch File:       $PATCH_FILE"
echo "=========================================================="

if [[ ! -d "$ENGINE_DIR/.git" ]]; then
    echo "Cloning ik_llama.cpp from upstream..."
    git clone https://github.com/ikawrakow/ik_llama.cpp.git "$ENGINE_DIR"
fi

cd "$ENGINE_DIR"

CURRENT_SHA="$(git rev-parse HEAD)"
echo "Current commit SHA: $CURRENT_SHA"

# Check if patches are already applied
if git log -n 1 --oneline | grep -q "feat(flint)"; then
    echo "Engine already contains Homelab optimization commit."
else
    echo "Checking out upstream base commit $UPSTREAM_SHA..."
    git checkout "$UPSTREAM_SHA"
    echo "Applying Homelab optimization patches..."
    git apply "$PATCH_FILE"
    echo "Patches applied cleanly."
fi

echo "Configuring CMake for Broadwell AVX2+FMA3+OpenMP..."
mkdir -p build && cd build

cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DGGML_AVX2=ON \
    -DGGML_FMA=ON \
    -DGGML_F16C=ON \
    -DGGML_OPENMP=ON \
    -DGGML_NATIVE=ON

echo "Compiling core targets..."
cmake --build . --config Release -j "$(nproc)" --target \
    llama-cli \
    llama-server \
    llama-quantize \
    llama-passkey \
    llama-perplexity

echo "=========================================================="
echo "BUILD COMPLETE AND CERTIFIED:"
echo "Engine SHA:       $(git rev-parse HEAD)"
echo "Compiler Version: $(c++ --version | head -n 1)"
echo "Binaries Built:   $ENGINE_DIR/build/bin/{llama-cli,llama-server,llama-quantize,llama-passkey,llama-perplexity}"
echo "=========================================================="
