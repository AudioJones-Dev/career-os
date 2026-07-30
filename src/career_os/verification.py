from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timezone

from .models import JobOpportunity


@dataclass(slots=True)
class VerificationResult:
    status: str
    confidence: float
    florida_eligible: bool | None = None
    remote_status: str | None = None
    employment_type: str | None = None
    salary_min: int | None = None
    salary_max: int | None = None
    travel_percentage: int | None = None
    clearance_required: bool | None = None
    sponsorship_status: str | None = None
    evidence: list[str] = field(default_factory=list)
    unresolved: list[str] = field(default_factory=list)
    verified_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


_MONEY = re.compile(r"\$\s?([0-9]{2,3}(?:,[0-9]{3})+|[0-9]{2,3})\s*(?:-|–|to)\s*\$?\s?([0-9]{2,3}(?:,[0-9]{3})+|[0-9]{2,3})", re.I)
_TRAVEL = re.compile(r"(?:up to\s+)?(\d{1,2})%\s+travel", re.I)


def _money(value: str) -> int:
    number = int(value.replace(",", ""))
    return number * 1000 if number < 1000 else number


def verify_job(job: JobOpportunity) -> VerificationResult:
    text = " ".join([job.title, job.location, job.description, *job.requirements, *job.responsibilities]).lower()
    evidence: list[str] = []

    florida = job.florida_eligible
    if florida is None:
        if re.search(r"(?:not available|excluding|exclude[s]?|cannot hire|not eligible).{0,80}\bflorida\b", text):
            florida = False
            evidence.append("Posting language explicitly excludes Florida.")
        elif re.search(r"(?:anywhere in|throughout|within) (?:the )?(?:united states|u\.s\.)", text) or "remote (usa)" in text or "remote - us" in text:
            florida = True
            evidence.append("Posting permits remote work throughout the United States.")

    remote = job.remote_status
    if remote.lower() in {"unknown", ""}:
        if re.search(r"\bfully remote\b|\b100% remote\b|\bremote (?:within|anywhere|in) (?:the )?(?:united states|u\.s\.)", text):
            remote = "remote"
            evidence.append("Posting explicitly describes the role as fully remote.")
        elif re.search(r"\bhybrid\b", text):
            remote = "hybrid"
            evidence.append("Posting explicitly describes a hybrid arrangement.")
        elif re.search(r"\bon[- ]site\b|\bonsite\b", text):
            remote = "onsite"
            evidence.append("Posting explicitly requires on-site work.")

    employment = job.employment_type
    if employment.lower().strip() not in {"full-time", "full time", "fte"}:
        if re.search(r"\bfull[- ]time\b|\bregular employee\b", text):
            employment = "full-time"
            evidence.append("Posting explicitly identifies full-time employment.")
        elif re.search(r"\bcontract(?:or)?\b|\btemporary\b|\bpart[- ]time\b", text):
            employment = "contract"
            evidence.append("Posting indicates non-full-time employment.")

    salary_min, salary_max = job.salary_min, job.salary_max
    if salary_min is None or salary_max is None:
        match = _MONEY.search(text)
        if match:
            extracted_min, extracted_max = _money(match.group(1)), _money(match.group(2))
            salary_min = salary_min or extracted_min
            salary_max = salary_max or extracted_max
            evidence.append(f"Posting states a base range of ${extracted_min:,}–${extracted_max:,}.")

    travel = None
    travel_match = _TRAVEL.search(text)
    if travel_match:
        travel = int(travel_match.group(1))
        evidence.append(f"Posting states up to {travel}% travel.")

    clearance: bool | None = None
    if re.search(r"\b(?:active )?(?:security |secret |top secret |ts\/sci )clearance\b", text):
        clearance = True
        evidence.append("Posting requires or references a security clearance.")
    elif "no security clearance" in text:
        clearance = False
        evidence.append("Posting explicitly states that no clearance is required.")

    sponsorship: str | None = None
    if re.search(r"(?:unable|cannot|do not) (?:to )?sponsor|no visa sponsorship|without sponsorship", text):
        sponsorship = "not-offered"
        evidence.append("Posting states that employment sponsorship is not offered.")
    elif re.search(r"visa sponsorship (?:is )?available|will sponsor", text):
        sponsorship = "available"
        evidence.append("Posting states that sponsorship is available.")

    unresolved: list[str] = []
    if florida is None:
        unresolved.append("florida_eligibility")
    if remote.lower() in {"unknown", ""}:
        unresolved.append("remote_status")
    if employment.lower().strip() not in {"full-time", "full time", "fte"}:
        unresolved.append("employment_type")
    if salary_min is None and salary_max is None:
        unresolved.append("compensation")

    resolved = 4 - len(unresolved)
    confidence = round(min(0.98, 0.45 + resolved * 0.12 + min(len(evidence), 4) * 0.02), 2)
    status = "complete" if not unresolved else "partial" if evidence else "unresolved"
    return VerificationResult(
        status=status,
        confidence=confidence,
        florida_eligible=florida,
        remote_status=remote,
        employment_type=employment,
        salary_min=salary_min,
        salary_max=salary_max,
        travel_percentage=travel,
        clearance_required=clearance,
        sponsorship_status=sponsorship,
        evidence=evidence,
        unresolved=unresolved,
    )


def apply_verification(job: JobOpportunity, result: VerificationResult) -> JobOpportunity:
    job.florida_eligible = result.florida_eligible
    job.remote_status = result.remote_status or job.remote_status
    job.employment_type = result.employment_type or job.employment_type
    job.salary_min = result.salary_min
    job.salary_max = result.salary_max
    return job
