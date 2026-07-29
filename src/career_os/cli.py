from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from .adapters import fetch_greenhouse_jobs, fetch_lever_jobs
from .models import JobOpportunity
from .scoring import score_job


def load_jobs(path: Path) -> list[JobOpportunity]:
    if path.suffix.lower() == ".jsonl":
        return [JobOpportunity.from_dict(json.loads(line)) for line in path.read_text().splitlines() if line.strip()]
    data = json.loads(path.read_text())
    rows = data if isinstance(data, list) else data.get("jobs", [])
    return [JobOpportunity.from_dict(row) for row in rows]


def write_scored(jobs: list[JobOpportunity], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "source", "source_id", "company", "title", "url", "location", "remote_status",
        "florida_eligible", "salary_min", "salary_max", "score", "decision", "reasons", "gaps",
    ]
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for job in jobs:
            result = score_job(job)
            writer.writerow({
                "source": job.source, "source_id": job.source_id, "company": job.company,
                "title": job.title, "url": job.url, "location": job.location,
                "remote_status": job.remote_status, "florida_eligible": job.florida_eligible,
                "salary_min": job.salary_min, "salary_max": job.salary_max,
                "score": result.score, "decision": result.decision,
                "reasons": " | ".join(result.reasons), "gaps": " | ".join(result.gaps),
            })


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest, normalize, and score remote job opportunities.")
    sub = parser.add_subparsers(dest="command", required=True)

    file_cmd = sub.add_parser("file", help="Score normalized JSON or JSONL jobs")
    file_cmd.add_argument("input", type=Path)
    file_cmd.add_argument("--output", type=Path, default=Path("applications/scored-opportunities.csv"))

    gh_cmd = sub.add_parser("greenhouse", help="Fetch a public Greenhouse board")
    gh_cmd.add_argument("board_token")
    gh_cmd.add_argument("--company", required=True)
    gh_cmd.add_argument("--output", type=Path, default=Path("applications/greenhouse-opportunities.csv"))

    lever_cmd = sub.add_parser("lever", help="Fetch a public Lever site")
    lever_cmd.add_argument("site")
    lever_cmd.add_argument("--company", required=True)
    lever_cmd.add_argument("--output", type=Path, default=Path("applications/lever-opportunities.csv"))

    args = parser.parse_args()
    if args.command == "file":
        jobs = load_jobs(args.input)
    elif args.command == "greenhouse":
        jobs = fetch_greenhouse_jobs(args.board_token, args.company)
    else:
        jobs = fetch_lever_jobs(args.site, args.company)

    write_scored(jobs, args.output)
    print(f"Scored {len(jobs)} opportunities -> {args.output}")


if __name__ == "__main__":
    main()
