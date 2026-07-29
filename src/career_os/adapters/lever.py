from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from career_os.http import fetch_json
from career_os.models import JobOpportunity

from .common import clean_html, extract_salary, flatten_parts, infer_florida_eligibility, infer_remote_status


def normalize_lever_job(job: dict[str, Any], company: str) -> JobOpportunity:
    categories = job.get("categories") or {}
    location = str(categories.get("location", ""))
    parts = job.get("lists") or []
    description = "\n\n".join(
        chunk
        for chunk in (
            clean_html(str(job.get("descriptionPlain", job.get("description", "")))),
            flatten_parts(parts),
            clean_html(str(job.get("additionalPlain", job.get("additional", "")))),
        )
        if chunk
    )
    salary_min, salary_max = extract_salary(description)
    remote_status = infer_remote_status(location, description)
    return JobOpportunity(
        source="lever",
        source_id=str(job.get("id", job.get("hostedUrl", "unknown"))),
        title=str(job.get("text", "Untitled role")),
        company=company,
        url=str(job.get("hostedUrl", job.get("applyUrl", ""))),
        description=description,
        location=location,
        remote_status=remote_status,
        florida_eligible=infer_florida_eligibility(location, description) if remote_status == "remote" else None,
        employment_type=str(categories.get("commitment", "full-time") or "full-time").lower(),
        salary_min=salary_min,
        salary_max=salary_max,
        retrieved_at=datetime.now(timezone.utc).isoformat(),
        raw=job,
    )


def fetch_lever_jobs(site: str, company: str) -> list[JobOpportunity]:
    url = f"https://api.lever.co/v0/postings/{site}?mode=json"
    payload = fetch_json(url)
    rows = payload if isinstance(payload, list) else []
    return [normalize_lever_job(row, company=company) for row in rows]
