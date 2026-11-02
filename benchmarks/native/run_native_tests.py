#!/usr/bin/env python3
"""Compile the work-buffer contract and call the patched MoE kernels."""

import argparse
import os
from pathlib import Path
import platform
import re
import subprocess
import tempfile


def run(command):
    print("+", " ".join(map(str, command)), flush=True)
    subprocess.run(list(map(str, command)), check=True)


def buffer_contract(engine, compiler, temporary):
    source = (engine / "ggml/src/iqk/iqk_mul_mat.cpp").read_text()
    match = re.search(r"struct AlignedBuffer \{.*?\n\};", source, re.S)
    if not match:
        raise SystemExit("AlignedBuffer was not found in the engine source")
    test = temporary / "buffer_contract.cpp"
    test.write_text("""#include <cassert>
#include <cstddef>
#include <cstdint>
#include <cstring>
#include <cstdio>
#include <vector>
#define GGML_ASSERT assert
""" + match.group() + """
int main() {
    for (size_t first = 1; first <= 256; ++first) {
        AlignedBuffer f;
        assert(f.size() == 0);
        for (size_t request : {first, first + 1, first + 63, first + 64, first + 129, first + 4096}) {
            if (f.size() < request) f.resize(request);
            assert(f.size() >= request);
            assert((uintptr_t(f.data()) & 63) == 0);
            assert(f.data() >= f.buf.data());
            assert(f.data() + f.size() <= f.buf.data() + f.buf.size());
            memset(f.data(), 0x5a, f.size());
        }
    }
    puts("PASS aligned buffer: capacity, alignment, growth, full reported-size writes");
}
""")
    executable = temporary / "buffer_contract"
    run([compiler, "-std=c++17", "-O1", "-g", "-fsanitize=address,undefined",
         "-fno-omit-frame-pointer", test, "-o", executable])
    run([executable])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine", type=Path, required=True)
    parser.add_argument("--build-dir", type=Path)
    parser.add_argument("--configure", action="store_true", help="Configure and build a separate AVX2 ggml library")
    parser.add_argument("--sanitizers", action="store_true", help="Instrument the ggml library and native test with ASan/UBSan")
    parser.add_argument("--contract-only", action="store_true", help="Run only the portable extracted work-buffer contract")
    parser.add_argument("--jobs", type=int, default=4)
    args = parser.parse_args()
    engine = args.engine.resolve()
    build = (args.build_dir or engine / "build-native-tests").resolve()
    compiler = os.environ.get("CXX", "c++")
    with tempfile.TemporaryDirectory(prefix="homelab-native-") as folder:
        temporary = Path(folder)
        buffer_contract(engine, compiler, temporary)
        if args.contract_only:
            return
        if platform.machine().lower() not in {"x86_64", "amd64"}:
            raise SystemExit("The full native test requires x86-64 AVX2; use --contract-only on this machine")
        if args.configure:
            run(["cmake", "-S", engine, "-B", build,
                 "-DCMAKE_BUILD_TYPE=RelWithDebInfo", "-DGGML_NATIVE=OFF", "-DGGML_AVX2=ON",
                 "-DGGML_FMA=ON", "-DGGML_F16C=ON", "-DGGML_AVX512=OFF", "-DGGML_OPENMP=OFF",
                 "-DGGML_METAL=OFF", "-DGGML_ACCELERATE=OFF", "-DGGML_CUDA=OFF",
                 "-DBUILD_SHARED_LIBS=ON", "-DLLAMA_BUILD_TESTS=OFF", "-DLLAMA_BUILD_EXAMPLES=OFF",
                 f"-DGGML_SANITIZE_ADDRESS={'ON' if args.sanitizers else 'OFF'}",
                 f"-DGGML_SANITIZE_UNDEFINED={'ON' if args.sanitizers else 'OFF'}"])
            run(["cmake", "--build", build, "--target", "ggml", "-j", args.jobs])
        libraries = list(build.rglob("libggml.so")) + list(build.rglob("libggml.dylib"))
        if len(libraries) != 1:
            raise SystemExit(f"Expected one shared ggml library under {build}; found {len(libraries)}")
        library = libraries[0]
        executable = temporary / "test_moe"
        command = [compiler, "-std=c++17", "-O1", "-g", "-pthread", "-mavx2", "-mfma", "-mf16c",
                   "-I", engine / "ggml/include", "-I", engine / "ggml/src", "-I", engine / "ggml/src/iqk",
                   Path(__file__).with_name("test_moe.cpp"), library, f"-Wl,-rpath,{library.parent}", "-o", executable]
        if args.sanitizers:
            command += ["-fsanitize=address,undefined", "-fno-omit-frame-pointer"]
        run(command)
        run([executable])


if __name__ == "__main__":
    main()
