"""Offline regression tests for run identity, extraction and saved-result aggregation."""

import copy
import json
from pathlib import Path
import socket
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import bench_throughput
import check_equivalence
from code_eval import evaluate_saved_run, extract_python_solution
from manifest import create_manifest, get_build_artifacts, get_file_sha256, verify_resume
from runtime import decode_rate, require_free_port, stopping_metadata, stop_process_group
from summarize_runs import HUMANEVAL_IDS, coding_scores, summarize_coding, summarize_gpqa, timing_summary


class Response:
    def __init__(self, payload):
        self.payload = payload
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return False
    def read(self):
        return json.dumps(self.payload).encode()


class HarnessTests(unittest.TestCase):
    def test_humaneval_plus_requires_both_suites(self):
        data = {"eval": {"a": [{"base_status": "fail", "plus_status": "pass"}],
                         "b": [{"base_status": "pass", "plus_status": "pass"}]}}
        scores = coding_scores(data, ["a", "b"])
        self.assertEqual(scores["extra_only_pass_count"], 2)
        self.assertEqual(scores["plus_pass_count"], 1)
        with self.assertRaises(ValueError):
            coding_scores(data, ["a"])
        data["eval"]["b"].append(data["eval"]["b"][0])
        with self.assertRaises(ValueError):
            coding_scores(data, ["a", "b"])

    def test_saved_primary_runs_reconstruct_corrected_counts(self):
        repo = Path(__file__).resolve().parents[2]
        counts = {}
        for run in (repo / "logs/runs").glob("code_*"):
            if (run / "samples_eval_results.json").exists():
                summary = summarize_coding(run)
                counts[summary["experiment_id"][:5]] = summary["plus_pass_count"]
                expected_rate, expected_rows = (21.31, 163) if summary["experiment_id"].startswith("exp50") else (20.77, 164)
                self.assertEqual(summary["average_decode_tps"], expected_rate)
                self.assertEqual(summary["valid_timing_rows"], expected_rows)
        self.assertEqual(counts, {"exp50": 106, "exp94": 148})

    def test_single_token_and_invalid_rates_do_not_inflate_saved_mean(self):
        rows = [{"tokens": 1, "speed_tps": 1_000_000}, {"tokens": 2, "speed_tps": 20},
                {"tokens": 4, "speed_tps": None}, {"tokens": 4, "speed_tps": float("inf")}]
        summary = timing_summary(rows)
        self.assertEqual(summary["average_decode_tps"], 20)
        self.assertEqual(summary["valid_timing_rows"], 1)
        self.assertEqual(summary["invalid_timing_rows"], 3)

    def test_final_code_preserves_imports_and_ignores_reasoning(self):
        code = "from math import sqrt\n\ndef solve(x):\n    return sqrt(x)"
        text = f"<think>```python\ndef solve(x):\n    return 0\n```</think>\n```python\n{code}\n```"
        self.assertEqual(extract_python_solution(text, "solve"), code)
        self.assertEqual(extract_python_solution("<think>```python\ndef solve(x):\n    return 0\n```", "solve"), "")
        self.assertEqual(extract_python_solution("```python\ndef other():\n    return 0\n```", "solve"), "")
        self.assertEqual(extract_python_solution("```python\ndef solve(:\n    return 0\n```", "solve"), "")

    def test_resume_compares_every_input(self):
        original = {"schema_version": 2, "engine": {"sha": "x"}, "model": {"sha256": "full"}, "request": {"system_prompt": "one"},
                    "server_argv": ["server", "-c", "8192"], "numactl": "--interleave=all", "dataset_sha256": "data", "system": {"affinity": [0, 2]}}
        self.assertEqual(verify_resume(original, copy.deepcopy(original)), (True, None))
        for key in original:
            changed = copy.deepcopy(original)
            changed[key] = "different"
            self.assertFalse(verify_resume(original, changed)[0], key)
        self.assertFalse(verify_resume({"model": {"header_sha256": "old"}}, original)[0])

    def test_model_hash_includes_tail(self):
        with tempfile.TemporaryDirectory() as directory:
            model = Path(directory) / "model.gguf"
            model.write_bytes(b"same-header" + b"a")
            first = get_file_sha256(model)
            model.write_bytes(b"same-header" + b"b")
            self.assertNotEqual(first, get_file_sha256(model))

    def test_changed_build_library_or_cmake_cache_rejects_resume(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = Path(directory) / "engine"
            build = engine / "build"
            binary = build / "bin/llama-server"
            library = build / "ggml/src/ggml-cpu/libggml-cpu.so"
            cache = build / "CMakeCache.txt"
            binary.parent.mkdir(parents=True)
            library.parent.mkdir(parents=True)
            binary.write_bytes(b"unchanged executable")
            library.write_bytes(b"first kernel")
            cache.write_text("GGML_NATIVE:BOOL=ON\n")
            model = Path(directory) / "model.gguf"
            model.write_bytes(b"same weights")
            with patch("manifest.get_git_info", return_value={"sha": "fixed"}), patch("manifest.get_system_topology", return_value={}):
                first = create_manifest({"id": "test"}, engine, model, server_binary=binary)
                library.write_bytes(b"changed kernel")
                second = create_manifest({"id": "test"}, engine, model, server_binary=binary)
                self.assertEqual(first["binary"], second["binary"])
                self.assertFalse(verify_resume(first, second)[0])
                cache.write_text("GGML_NATIVE:BOOL=OFF\n")
                third = create_manifest({"id": "test"}, engine, model, server_binary=binary)
                self.assertFalse(verify_resume(second, third)[0])
            self.assertIn(str(library.resolve()), first["build_artifacts"]["files"])
            self.assertIn(str(cache.resolve()), first["build_artifacts"]["files"])

    def test_custom_build_libraries_are_discovered_from_binary(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = Path(directory) / "engine"
            engine.mkdir()
            custom = Path(directory) / "custom-build"
            binary = custom / "bin/llama-server"
            binary.parent.mkdir(parents=True)
            binary.write_bytes(b"binary")
            (custom / "CMakeCache.txt").write_text("CMAKE_BUILD_TYPE:STRING=Release\n")
            library = custom / "src/libllama.dylib"
            library.parent.mkdir()
            library.write_bytes(b"library")
            identity = get_build_artifacts(engine, binary)
            self.assertIn(str(library.resolve()), identity["files"])
            self.assertEqual(identity["roots"], [str(custom.resolve())])

    def test_raw_length_stop_does_not_depend_on_truncated_flag(self):
        result = stopping_metadata({"stopped_limit": True, "truncated": False}, 4095, 4096)
        self.assertEqual(result["finish_reason"], "length")
        self.assertTrue(result["max_tokens_hit"])
        self.assertEqual(result["raw_stopping"]["truncated"], False)
        self.assertTrue(stopping_metadata({}, 4096, 4096, "stop")["max_tokens_hit"])
        self.assertEqual(stopping_metadata({"stopped_eos": True}, 12, 4096)["finish_reason"], "stop")

    def test_missing_timing_is_not_wall_throughput(self):
        self.assertIsNone(decode_rate(10, 0))
        self.assertIsNone(decode_rate(10, float("nan")))
        self.assertIsNone(decode_rate(True, 100))
        self.assertEqual(decode_rate(10, 500), 20)

    def test_equivalence_rejects_text_empty_and_non_integer_tokens(self):
        for payload in ({"content": "same"}, {"tokens": [1, 2]},
                        {"choices": [{"logprobs": {"content": []}}]},
                        {"choices": [{"logprobs": {"content": [{"id": True}]}}]},
                        {"choices": [{"logprobs": {"content": [{"token": "text", "id": "1"}]}}]}):
            with patch("urllib.request.urlopen", return_value=Response(payload)):
                self.assertIsNone(check_equivalence.query_greedy("http://unused", "test"))
        payload = {"choices": [{"logprobs": {"content": [{"id": 1, "token": "one"}, {"id": 2, "token": "two"}]}}]}
        with patch("urllib.request.urlopen", return_value=Response(payload)) as request:
            self.assertEqual(check_equivalence.query_greedy("http://unused", "test", n_predict=8), [1, 2])
        wire_request = request.call_args[0][0]
        self.assertEqual(wire_request.full_url, "http://unused/v1/completions")
        wire_payload = json.loads(wire_request.data)
        self.assertEqual(wire_payload["logprobs"], 1)
        self.assertEqual(wire_payload["max_tokens"], 8)
        self.assertNotIn("return_tokens", wire_payload)

    def test_invalid_timing_excluded_from_weighted_and_class_rates(self):
        good = {"content": "valid output", "timings": {"predicted_n": 512, "predicted_ms": 25600}}
        missing = {"content": "missing timing", "timings": {"predicted_n": 512, "predicted_ms": 0}}
        prompts = {"code_edit": {"one": "a", "two": "b"}, "code_gen": {}, "prose": {}}
        with patch.object(bench_throughput, "load_prompts", return_value=prompts), patch.object(bench_throughput, "query_server", side_effect=[good, good, missing]):
            result = bench_throughput.run_throughput_benchmark(repetitions=1)
        self.assertEqual(result["summary"]["valid_runs"], 1)
        self.assertFalse(result["summary"]["complete"])
        self.assertEqual(result["summary"]["token_weighted_tps"], 20)
        self.assertEqual(result["summary"]["per_class"]["code_edit"]["mean_decode_tps"], 20)

    def test_busy_port_is_rejected_without_killing_owner(self):
        with socket.socket() as listener:
            listener.bind(("127.0.0.1", 0))
            listener.listen()
            with self.assertRaises(RuntimeError):
                require_free_port(listener.getsockname()[1])

    def test_exited_owned_process_does_not_signal_group(self):
        from unittest.mock import Mock
        process = Mock()
        process.poll.return_value = 0
        with patch("os.killpg") as kill:
            stop_process_group(process)
        kill.assert_not_called()

    def test_fresh_evaluation_does_not_reuse_evalplus_cache(self):
        import types
        with tempfile.TemporaryDirectory() as directory:
            run = Path(directory)
            (run / "samples.jsonl").write_text('{"task_id":"a","solution":"new"}\n')
            results = run / "samples_eval_results.json"
            results.write_text('{"old":"cached"}')
            def evaluate(**kwargs):
                self.assertFalse(results.exists())
                results.write_text('{"fresh":true}')
            fake = types.ModuleType("evalplus.evaluate")
            fake.evaluate = evaluate
            with patch.dict(sys.modules, {"evalplus.evaluate": fake}), patch("code_eval.importlib.metadata.version", return_value="0.3.1"), patch("code_eval.summarize_coding", return_value={"ok": True}):
                self.assertEqual(evaluate_saved_run(run, allow_host_execution=True), {"ok": True})
            backups = list((run / "evaluation-history").glob("*.json"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(json.loads(backups[0].read_text()), {"old": "cached"})
            self.assertEqual(json.loads((run / "evaluation_identity.json").read_text())["evalplus_version"], "0.3.1")

    def test_saved_result_cannot_refer_to_old_solution(self):
        with tempfile.TemporaryDirectory() as directory:
            run = Path(directory)
            rows = [{"task_id": task_id, "solution": "new", "tokens": 1, "speed_tps": 1, "wall_time": 1} for task_id in sorted(HUMANEVAL_IDS)]
            (run / "rows.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows))
            (run / "samples.jsonl").write_text("".join(json.dumps({"task_id": row["task_id"], "solution": "new"}) + "\n" for row in rows))
            results = {row["task_id"]: [{"solution": "new", "base_status": "pass", "plus_status": "pass"}] for row in rows}
            results["HumanEval/0"][0]["solution"] = "old"
            (run / "samples_eval_results.json").write_text(json.dumps({"eval": results}))
            with self.assertRaisesRegex(ValueError, "stale"):
                summarize_coding(run)

    def test_partial_humaneval_run_cannot_be_published(self):
        with tempfile.TemporaryDirectory() as directory:
            run = Path(directory)
            row = {"task_id": "HumanEval/0", "solution": "", "tokens": 0, "speed_tps": None, "wall_time": 1}
            (run / "rows.jsonl").write_text(json.dumps(row) + "\n")
            (run / "samples.jsonl").write_text(json.dumps({"task_id": "HumanEval/0", "solution": ""}) + "\n")
            (run / "samples_eval_results.json").write_text(json.dumps({"eval": {"HumanEval/0": [{"solution": "", "base_status": "fail", "plus_status": "fail"}]}}))
            with self.assertRaisesRegex(ValueError, "Incomplete HumanEval"):
                summarize_coding(run, write=True)
            self.assertFalse((run / "summary.json").exists())
            self.assertFalse((run / "report.md").exists())

    def test_partial_gpqa_run_cannot_be_published(self):
        with tempfile.TemporaryDirectory() as directory:
            run = Path(directory)
            (run / "summary.json").write_text(json.dumps({"max_tokens_ceiling": 8192}))
            (run / "manifest.json").write_text("{}")
            (run / "rows.jsonl").write_text(json.dumps({"id": "gpqa_110", "gold": "A", "pred": "A", "tokens": 10, "speed_tps": 20}) + "\n")
            with self.assertRaisesRegex(ValueError, "Incomplete GPQA"):
                summarize_gpqa(run, write=True)
            self.assertFalse((run / "report.md").exists())

    def test_host_execution_requires_explicit_choice(self):
        with self.assertRaisesRegex(ValueError, "allow-host-execution"):
            evaluate_saved_run(Path("unused"))


if __name__ == "__main__":
    unittest.main()
