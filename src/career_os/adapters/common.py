from __future__ import annotations

import html
import re
from typing import Iterable


_TAG_RE = re.compile(r"<[^>]+>")
_SPACE_RE = re.compile(r"\s+")
_SALARY_RANGE_RE = re.compile(
    r"\$\s*(?P<low>\d{2,3}(?:,\d{3})?|\d{2,3})\s*(?P<low_k>[kK])?\s*"
    r"(?:-|–|—|to)\s*\$?\s*(?P<high>\d{2,3}(?:,\d{3})?|\d{2,3})\s*(?P<high_k>[kK])?",
    re.IGNORECASE,
)


def clean_html(value: str | None) -> str:
    if not value:
        return ""
    text = html.unescape(_TAG_RE.sub(" ", value))
    return _SPACE_RE.sub(" ", text).strip()


def infer_remote_status(location: str, text: str = "") -> str:
    combined = f"{location} {text}".lower()
    if "hybrid" in combined:
        return "hybrid"
    if "remote" in combined or "work from home" in combined:
        return "remote"
    if location:
        return "onsite"
    return "unknown"


def infer_florida_eligibility(location: str, text: str = "") -> bool | None:
    combined = f"{location} {text}".lower()
    exclusions = (
        "not available in florida",
        "excluding florida",
        "except florida",
        "florida excluded",
    )
    if any(term in combined for term in exclusions):
        return False
    if "florida" in combined:
        return True
    if "united states" in combined or "u.s." in combined or "usa" in combined or "remote" in combined:
        return None
    return None


def extract_salary(text: str) -> tuple[int | None, int | None]:
    match = _SALARY_RANGE_RE.search(text)
    if not match:
        return None, None
    low = _normalize_salary_number(match.group("low"), bool(match.group("low_k")))
    high = _normalize_salary_number(match.group("high"), bool(match.group("high_k")))
    return low, high


def _normalize_salary_number(raw: str, explicit_k: bool = False) -> int:
    value = int(raw.replace(",", ""))
    return value * 1000 if explicit_k or value < 1000 else value


def flatten_parts(parts: Iterable[dict]) -> str:
    chunks: list[str] = []
    for part in parts:
        heading = clean_html(str(part.get("name", "")))
        body = clean_html(str(part.get("content", part.get("text", ""))))
        if heading:
            chunks.append(heading)
        if body:
            chunks.append(body)
    return "\n\n".join(chunks)
