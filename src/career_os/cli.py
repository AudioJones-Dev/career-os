from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from .models import JobOpportunity
from .scoring import score_job


def load_jobs(path: Path) -> list[JobOpportunity]:
    if path.suffix.lower() == ".jsonl":
        return [JobOpportunity.from_dict(json.loads(line)) for line in path.read_text().splitlines() if line.strip()]
    data = json.loads(path.read_text())
    rows = data if isinstance(data, list) else data.get("jobs", [])
    return [JobOpportunity.from_dict(row) for row in rows]


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize and score remote job opportunities.")
    parser.add_argument("input", type=Path, help="JSON or JSONL file containing normalized or partially normalized jobs")
    parser.add_argument("--output", type=Path, default=Path("applications/scored-opportunities.csv"))
    args = parser.parse_args()

    jobs = load_jobs(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "source", "source_id", "company", "title", "url", "location", "remote_status",
        "florida_eligible", "salary_min", "salary_max", "score", "decision", "reasons", "gaps",
    ]
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for job in jobs:
            result = score_job(job)
            writer.writerow({
                "source": job.source,
                "source_id": job.source_id,
                "company": job.company,
                "title": job.title,
                "url": job.url,
                "location": job.location,
                "remote_status": job.remote_status,
                "florida_eligible": job.florida_eligible,
                "salary_min": job.salary_min,
                "salary_max": job.salary_max,
                "score": result.score,
                "decision": result.decision,
                "reasons": " | ".join(result.reasons),
                "gaps": " | ".join(result.gaps),
            })

    print(f"Scored {len(jobs)} opportunities -> {args.output}")


if __name__ == "__main__":
    main()
