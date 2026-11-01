"""Optional native checks; set HOMELAB_ENGINE_DIR to a patched engine checkout."""

import os
from pathlib import Path
import subprocess
import sys
import unittest


@unittest.skipUnless(os.environ.get("HOMELAB_ENGINE_DIR"), "Set HOMELAB_ENGINE_DIR to run the compiled work-buffer contract")
class TestNativeWorkBuffer(unittest.TestCase):
    def test_work_buffer_contract(self):
        runner = Path(__file__).resolve().parents[1] / "native/run_native_tests.py"
        subprocess.run([sys.executable, str(runner), "--engine", os.environ["HOMELAB_ENGINE_DIR"],
                        "--contract-only"], check=True)


if __name__ == "__main__":
    unittest.main()
