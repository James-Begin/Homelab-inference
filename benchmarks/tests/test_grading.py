#!/usr/bin/env python3
"""
Unit tests for grading and answer extraction module (benchmarks/grading.py).
Tests adversarial cases outlined in improvement-plan.md Section 5 (Phase 1.3).
"""

import sys
import unittest
from pathlib import Path

# Add benchmarks directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from grading import (
    RowStatus,
    extract_answer_lenient,
    extract_answer_strict,
    grade_response,
)


class TestGrading(unittest.TestCase):

    def test_unclosed_think_block(self):
        """Unclosed <think> block must evaluate strictly to None (NO_ANSWER_TRUNCATED)."""
        content = "<think>\nLet us consider option B as the primary candidate.\nWe need to compute the integral..."
        strict = extract_answer_strict(content)
        self.assertIsNone(strict)

        status, strict_ans, _ = grade_response(content, gold="B", finish_reason="length")
        self.assertEqual(status, RowStatus.NO_ANSWER_TRUNCATED)
        self.assertIsNone(strict_ans)

    def test_choice_mid_sentence(self):
        """Word 'choice' or 'option' mentioned mid-sentence must not be extracted by strict extractor."""
        content = (
            "<think>\nReasoning complete.\n</think>\n"
            "Our initial choice A seemed viable, but detailed calculation rules it out.\n"
            "Therefore, after checking all possibilities, we reach the conclusion.\n"
            "Final answer: D"
        )
        strict = extract_answer_strict(content)
        self.assertEqual(strict, "D")

    def test_lone_letter_in_prose(self):
        """A lone letter in prose on the last line must not be extracted by strict extractor."""
        content = (
            "<think>Done.</think>\n"
            "The experiment demonstrated that substance A reacted completely."
        )
        strict = extract_answer_strict(content)
        self.assertIsNone(strict)

        # Lenient extractor might pick it up due to legacy regex
        lenient = extract_answer_lenient(content)
        # But strict must refuse it
        status, strict_ans, _ = grade_response(content, gold="A")
        self.assertEqual(status, RowStatus.NO_ANSWER_FORMAT)
        self.assertIsNone(strict_ans)

    def test_standard_final_answer(self):
        """Standard 'Final answer: X' formats."""
        cases = [
            ("Final answer: A", "A"),
            ("Final answer: (B)", "B"),
            ("The correct answer is: C", "C"),
            ("Correct answer is D.", "D"),
            ("The final answer is (A)", "A"),
        ]
        for text, expected in cases:
            content = f"<think>thinking</think>\n{text}"
            self.assertEqual(extract_answer_strict(content), expected)

    def test_boxed_latex_format(self):
        """LaTeX \\boxed{X} formats outside thinking."""
        content = "<think>solved</think>\nThe result is given by \\boxed{C}."
        strict = extract_answer_strict(content)
        self.assertEqual(strict, "C")

        content2 = "<think>solved</think>\nTherefore: \\boxed{(B)}"
        strict2 = extract_answer_strict(content2)
        self.assertEqual(strict2, "B")

    def test_trailing_whitespace_and_markdown(self):
        """Markdown bolding and trailing whitespace handling."""
        content = "<think>done</think>\n\n**Final answer: B**   \n\n"
        strict = extract_answer_strict(content)
        self.assertEqual(strict, "B")

    def test_grade_response_correct_and_wrong(self):
        """Correct vs wrong vs format vs truncation status classification."""
        # Correct
        s, strict, _ = grade_response("<think>ok</think>\nFinal answer: C", gold="C")
        self.assertEqual(s, RowStatus.CORRECT)
        self.assertEqual(strict, "C")

        # Wrong
        s, strict, _ = grade_response("<think>ok</think>\nFinal answer: A", gold="C")
        self.assertEqual(s, RowStatus.WRONG)
        self.assertEqual(strict, "A")

        # Truncation hit
        s, strict, _ = grade_response("<think>in flight", gold="C", max_tokens_hit=True)
        self.assertEqual(s, RowStatus.NO_ANSWER_TRUNCATED)


if __name__ == "__main__":
    unittest.main()
