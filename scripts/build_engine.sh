#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
UPSTREAM_SHA="87fc8701ff4da81a7d2a91ec0695f95eb3066a47"
ENGINE_DIR="${IK_LLAMA_HOME:-$REPO_ROOT/.build/ik_llama.cpp}"
MODE=build
POSITIONAL=0

while [[ $# -gt 0 ]]; do
    case "$1" in
        --check) MODE=check ;;
        --prepare-only) MODE=prepare ;;
        --help)
            echo "Usage: $0 [--check | --prepare-only] [ENGINE_DIR]"
            echo "--check validates source state without changing it."
            echo "--prepare-only clones and applies patches without compiling."
            exit 0 ;;
        -*) echo "Unknown option: $1" >&2; exit 2 ;;
        *)
            if [[ $POSITIONAL -eq 1 ]]; then
                echo "Only one engine directory may be supplied." >&2
                exit 2
            fi
            ENGINE_DIR="$1"
            POSITIONAL=1 ;;
    esac
    shift
done

PATCHES=(
    "$REPO_ROOT/patches/0000-all-homelab-optimizations.patch"
    "$REPO_ROOT/patches/0007-fix-buffer-capacity-and-moe-partitioning.patch"
)
for patch in "${PATCHES[@]}"; do
    [[ -f "$patch" ]] || { echo "Missing patch: $patch" >&2; exit 1; }
done

if [[ ! -d "$ENGINE_DIR/.git" && ! -f "$ENGINE_DIR/.git" ]]; then
    if [[ "$MODE" == check ]]; then
        echo "No engine checkout at $ENGINE_DIR" >&2
        exit 1
    fi
    if [[ -e "$ENGINE_DIR" ]]; then
        echo "Refusing to replace an existing non-Git directory: $ENGINE_DIR" >&2
        exit 1
    fi
    git clone --filter=blob:none --no-checkout https://github.com/ikawrakow/ik_llama.cpp.git "$ENGINE_DIR"
    git -C "$ENGINE_DIR" checkout --detach "$UPSTREAM_SHA"
fi
git -C "$ENGINE_DIR" cat-file -e "$UPSTREAM_SHA^{commit}"

PATCH_STATE_DIR="$(mktemp -d "${TMPDIR:-/tmp}/homelab-patches.XXXXXX")"
trap 'rm -rf "$PATCH_STATE_DIR"' EXIT
PATCH_INDEX="$PATCH_STATE_DIR/index"
GIT_INDEX_FILE="$PATCH_INDEX" git -C "$ENGINE_DIR" read-tree "$UPSTREAM_SHA"
MATCHED_STATE=-1

# Compare the full source tree, including files added by patches.
for ((state=0; state<=${#PATCHES[@]}; state++)); do
    if GIT_INDEX_FILE="$PATCH_INDEX" git -C "$ENGINE_DIR" diff --quiet -- && \
       [[ -z "$(GIT_INDEX_FILE="$PATCH_INDEX" git -C "$ENGINE_DIR" ls-files --others --exclude-standard)" ]]; then
        MATCHED_STATE=$state
    fi
    if [[ $state -lt ${#PATCHES[@]} ]]; then
        GIT_INDEX_FILE="$PATCH_INDEX" git -C "$ENGINE_DIR" apply --cached "${PATCHES[$state]}"
    fi
done

if [[ $MATCHED_STATE -lt 0 ]]; then
    echo "Engine source differs from the pinned base or a known patch state." >&2
    echo "Use a separate checkout; this script does not reset local changes." >&2
    exit 1
fi

if [[ "$MODE" == check ]]; then
    echo "Source matches patch state $MATCHED_STATE/${#PATCHES[@]}; the complete patch stack applies."
    exit 0
fi

for ((state=MATCHED_STATE; state<${#PATCHES[@]}; state++)); do
    git -C "$ENGINE_DIR" apply --check "${PATCHES[$state]}"
    git -C "$ENGINE_DIR" apply "${PATCHES[$state]}"
done
echo "Source prepared from $UPSTREAM_SHA with ${#PATCHES[@]} patch files."
[[ "$MODE" == prepare ]] && exit 0

BUILD_DIR="${IK_LLAMA_BUILD:-$ENGINE_DIR/build}"
JOBS="${HOMELAB_BUILD_JOBS:-$(getconf _NPROCESSORS_ONLN)}"
cmake -S "$ENGINE_DIR" -B "$BUILD_DIR" \
    -DCMAKE_BUILD_TYPE=Release \
    -DGGML_AVX2=ON -DGGML_FMA=ON -DGGML_F16C=ON \
    -DGGML_OPENMP=ON -DGGML_NATIVE=ON
cmake --build "$BUILD_DIR" --config Release --parallel "$JOBS" --target \
    llama-cli llama-server llama-quantize llama-passkey llama-perplexity
echo "Build completed: $BUILD_DIR/bin"
