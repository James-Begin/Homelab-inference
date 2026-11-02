#!/usr/bin/env python3
"""Extract GPQA answers outside thinking blocks and classify each response."""

from enum import Enum
import re
from typing import Optional, Tuple


class RowStatus(str, Enum):
    CORRECT = "correct"
    WRONG = "wrong"
    NO_ANSWER_TRUNCATED = "no_answer_truncated"
    NO_ANSWER_FORMAT = "no_answer_format"
    ERROR = "error"


def extract_clean_answer_text(completion_text: str) -> Tuple[Optional[str], bool]:
    """Remove balanced thinking blocks; reject any unfinished or malformed block."""
    depth = 0
    cursor = 0
    outside = []
    first_tag = True
    for tag in re.finditer(r"</?think>", completion_text):
        if tag.group() == "<think>":
            if depth == 0:
                outside.append(completion_text[cursor:tag.start()])
            depth += 1
        elif depth > 0:
            depth -= 1
            if depth == 0:
                cursor = tag.end()
        elif first_tag:
            # A template can supply the opening tag before generated text begins.
            outside = []
            cursor = tag.end()
        else:
            return None, False
        first_tag = False
    if depth:
        return None, False
    outside.append(completion_text[cursor:])
    return "".join(outside), True


def extract_answer_strict(completion_text: str) -> Optional[str]:
    """
    Accepted final-answer forms:
    1. Rejects unclosed reasoning blocks (<think> without </think>).
    2. Takes only text outside the reasoning block.
    3. Requires the last match of:
       - ^\\s*Final answer:\\s*\\(?([A-D])\\)?\\s*$ (multiline)
       - or \\boxed{\\s*\\(?([A-D])\\)?\\s*}
    """
    clean_text, is_closed = extract_clean_answer_text(completion_text)
    if not is_closed or clean_text is None:
        return None

    # Search for standard Final answer pattern (allowing optional markdown asterisks)
    matches = re.findall(
        r"^\s*(?:\*{1,2})?(?:Final answer|The correct answer is|Correct answer is|The final answer is)[:\*\s]*\s*(?:\(?([A-D])\)?)(?:\*{1,2})?[\.\s]*$",
        clean_text,
        re.MULTILINE | re.IGNORECASE,
    )
    if matches:
        return matches[-1].upper()

    # Search for boxed format (common in LaTeX reasoning outputs)
    boxed_matches = re.findall(r"\\boxed\{\s*\(?([A-D])\)?\s*\}", clean_text)
    if boxed_matches:
        return boxed_matches[-1].upper()

    return None


def extract_answer_lenient(completion_text: str) -> Optional[str]:
    """
    Permissive extractor (for comparative auditing):
    If strict extractor succeeds, lenient agrees with strict.
    Otherwise searches for the LAST choice/option assertion or lone A-D at the end of the text.
    """
    strict = extract_answer_strict(completion_text)
    if strict:
        return strict

    clean_text, is_closed = extract_clean_answer_text(completion_text)
    if not is_closed or clean_text is None:
        return None

    matches = re.findall(
        r"(?:final answer is|the correct answer is|correct answer is|the answer is|answer is|choice|option)[:\*\s]*\s*(?:\(?([A-D])\)?)(?:[\s\.\*\)\:\n]|$)",
        clean_text,
        re.IGNORECASE,
    )
    if matches:
        return matches[-1].upper()

    boxed_matches = re.findall(r"\\boxed\{\s*\(?([A-D])\)?\s*\}", clean_text)
    if boxed_matches:
        return boxed_matches[-1].upper()

    lines = [line.strip() for line in clean_text.splitlines() if line.strip()]
    if lines:
        match = re.search(r"\b([A-D])\b", lines[-1])
        if match:
            return match.group(1).upper()

    return None


def grade_response(
    content: str,
    gold: str,
    finish_reason: Optional[str] = None,
    max_tokens_hit: bool = False,
) -> Tuple[RowStatus, Optional[str], Optional[str]]:
    """
    Grades a single question response.
    Returns: (status: RowStatus, strict_ans: Optional[str], lenient_ans: Optional[str])
    """
    if content is None:
        return RowStatus.ERROR, None, None

    strict_ans = extract_answer_strict(content)
    lenient_ans = extract_answer_lenient(content)

    clean_text, is_closed = extract_clean_answer_text(content)

    if not is_closed or max_tokens_hit or finish_reason == "length":
        if strict_ans is None:
            return RowStatus.NO_ANSWER_TRUNCATED, None, lenient_ans

    if strict_ans is None:
        return RowStatus.NO_ANSWER_FORMAT, None, lenient_ans

    if strict_ans.upper() == gold.upper():
        return RowStatus.CORRECT, strict_ans, lenient_ans
    else:
        return RowStatus.WRONG, strict_ans, lenient_ans
