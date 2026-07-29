from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from career_os.http import fetch_json
from career_os.models import JobOpportunity

from .common import clean_html, extract_salary, infer_florida_eligibility, infer_remote_status


def normalize_greenhouse_job(job: dict[str, Any], company: str) -> JobOpportunity:
    location = str((job.get("location") or {}).get("name", ""))
    description = clean_html(str(job.get("content", "")))
    salary_min, salary_max = extract_salary(description)
    remote_status = infer_remote_status(location, description)
    return JobOpportunity(
        source="greenhouse",
        source_id=str(job.get("id", job.get("absolute_url", "unknown"))),
        title=str(job.get("title", "Untitled role")),
        company=company,
        url=str(job.get("absolute_url", "")),
        description=description,
        location=location,
        remote_status=remote_status,
        florida_eligible=infer_florida_eligibility(location, description) if remote_status == "remote" else None,
        salary_min=salary_min,
        salary_max=salary_max,
        posted_at=str(job.get("updated_at")) if job.get("updated_at") else None,
        retrieved_at=datetime.now(timezone.utc).isoformat(),
        raw=job,
    )


def fetch_greenhouse_jobs(board_token: str, company: str) -> list[JobOpportunity]:
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs?content=true"
    payload = fetch_json(url)
    rows = payload.get("jobs", []) if isinstance(payload, dict) else []
    return [normalize_greenhouse_job(row, company=company) for row in rows]
