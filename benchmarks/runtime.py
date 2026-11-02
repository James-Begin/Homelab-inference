"""Server lifecycle and response metadata shared by the benchmark clients."""

import math
import os
import signal
import socket
import subprocess
import time
import urllib.request


def require_free_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind(("127.0.0.1", port))
        except OSError as exc:
            raise RuntimeError(f"Port {port} is in use; stop its owner or choose --port.") from exc


def wait_for_server(url, proc, timeout=120):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if proc.poll() is not None:
            return False
        try:
            with urllib.request.urlopen(url, timeout=2) as response:
                if response.status == 200:
                    return proc.poll() is None
        except (OSError, ValueError):
            pass
        time.sleep(1)
    return False


def stop_process_group(proc):
    if proc.poll() is not None:
        return
    try:
        os.killpg(proc.pid, signal.SIGTERM)
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGKILL)
        proc.wait(timeout=5)
    except ProcessLookupError:
        proc.wait()


def positive_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and value > 0


def decode_rate(tokens, predicted_ms):
    if positive_number(tokens) and positive_number(predicted_ms):
        return tokens * 1000.0 / predicted_ms
    return None


def stopping_metadata(response, token_count, ceiling, finish_reason=None):
    flags = {key: response[key] for key in ("stopped_eos", "stopped_word", "stopped_limit", "truncated", "stop_type") if key in response}
    hit_limit = response.get("stopped_limit") is True or finish_reason == "length"
    at_ceiling = isinstance(token_count, (int, float)) and token_count >= ceiling
    if hit_limit or at_ceiling:
        reason = "length"
    elif response.get("stopped_eos") is True or response.get("stopped_word") is True:
        reason = "stop"
    else:
        reason = finish_reason or "unknown"
    return {"finish_reason": reason, "max_tokens_hit": hit_limit or at_ceiling, "raw_stopping": flags}
