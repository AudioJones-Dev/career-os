from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from .adapters import fetch_greenhouse_jobs, fetch_lever_jobs
from .models import JobOpportunity


@dataclass(slots=True)
class CompanySource:
    company: str
    source: str
    identifier: str
    enabled: bool = True
    priority: str = "tier-2"
    notes: str = ""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "CompanySource":
        required = ("company", "source", "identifier")
        missing = [key for key in required if not str(data.get(key, "")).strip()]
        if missing:
            raise ValueError(f"Company source missing required fields: {', '.join(missing)}")
        source = str(data["source"]).lower().strip()
        if source not in {"greenhouse", "lever"}:
            raise ValueError(f"Unsupported source: {source}")
        return cls(
            company=str(data["company"]).strip(),
            source=source,
            identifier=str(data["identifier"]).strip(),
            enabled=bool(data.get("enabled", True)),
            priority=str(data.get("priority", "tier-2")),
            notes=str(data.get("notes", "")),
        )


def load_company_registry(path: Path) -> list[CompanySource]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload if isinstance(payload, list) else payload.get("companies", [])
    return [CompanySource.from_dict(row) for row in rows]


def collect_registered_jobs(sources: list[CompanySource]) -> tuple[list[JobOpportunity], list[str]]:
    jobs: list[JobOpportunity] = []
    errors: list[str] = []
    for item in sources:
        if not item.enabled:
            continue
        try:
            if item.source == "greenhouse":
                jobs.extend(fetch_greenhouse_jobs(item.identifier, item.company))
            else:
                jobs.extend(fetch_lever_jobs(item.identifier, item.company))
        except Exception as exc:  # preserve source failures without aborting the batch
            errors.append(f"{item.company} ({item.source}:{item.identifier}): {exc}")
    return deduplicate_jobs(jobs), errors


def deduplicate_jobs(jobs: list[JobOpportunity]) -> list[JobOpportunity]:
    unique: dict[str, JobOpportunity] = {}
    for job in jobs:
        key = canonical_job_key(job)
        incumbent = unique.get(key)
        if incumbent is None or _completeness(job) > _completeness(incumbent):
            unique[key] = job
    return list(unique.values())


def canonical_job_key(job: JobOpportunity) -> str:
    if job.url:
        parts = urlsplit(job.url)
        normalized_url = urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), "", ""))
        return f"url:{normalized_url}"
    return "text:" + "|".join(
        part.strip().lower() for part in (job.company, job.title, job.location)
    )


def _completeness(job: JobOpportunity) -> int:
    values = (
        job.description,
        job.location,
        job.salary_min,
        job.salary_max,
        job.posted_at,
        job.remote_status != "unknown",
        job.florida_eligible is not None,
    )
    return sum(bool(value) for value in values)
