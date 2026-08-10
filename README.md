# Career OS

Career OS is Tyrone Nelms' operating system for securing a full-time remote U.S. role with a target base salary of **$90,000 or more**.

It coordinates career positioning, job sourcing, opportunity scoring, tailored application assets, portfolio evidence, interview preparation, and application tracking.

## Canonical Sources

- Resume and career-content source of truth: https://github.com/AudioJones-Dev/Tyrone-Nelms-Resume
- LinkedIn: https://www.linkedin.com/in/audiojones
- GitHub portfolio: https://github.com/AudioJones-Dev

Career OS does not duplicate canonical resume content. Every tailored application must record the resume path and commit SHA used.

## Evidence Repositories

- AJ Digital OS V1: https://github.com/AudioJones-Dev/AJ-DIGITAL-OS-V1
- HDIKIT: private repository — walkthrough available
- Florida Ramp & Lift operational pilot: private repository — walkthrough available
- Florida Ramp & Lift planning and governance foundation: https://github.com/AudioJones-Dev/florida-ramp-and-lift-ops
- VPL Flow specified operations architecture: private repository — walkthrough available; no application code or production claim
- Founder Intelligence System: https://github.com/AudioJones-Dev/founder-intelligence-system
- ResponseOS: https://github.com/AudioJones-Dev/responseos

See `architecture/repository-boundaries.md` for ownership rules and maturity labels.

## Target Positioning

**Operations & Business Systems Architect | Business Analysis | Requirements Engineering | Process Design | Systems Implementation | AI-Enabled Workflows**

Primary target roles include Senior Business Systems Analyst, Business Systems Consultant, Business Systems Architect, Operations Systems Architect, Implementation Manager, Systems Implementation Lead, Solutions Consultant, Business Systems Manager, Business Operations Manager, Operations Manager, and Program Manager. Solutions Architect, AI Solutions Architect, and enterprise Business Architect remain evidence-dependent stretch titles rather than default search positioning.

## Compensation and Work Constraints

- Minimum target base salary: **$90,000**
- Preferred arrangement: **Remote, full-time, United States**
- Geographic plan: Florida relocation flexibility, including Fort Myers, Cape Coral, and surrounding areas
- Reject roles that are nominally remote but exclude Florida unless the role provides a viable relocation path

## Installation

```bash
python -m pip install -e .
python -m pytest
```

## Ingestion Commands

Score an existing normalized file:

```bash
career-os file jobs.json --output applications/scored-opportunities.csv
```

Fetch one public ATS board:

```bash
career-os greenhouse <board-token> --company "Company Name"
career-os lever <site> --company "Company Name"
```

Fetch all enabled employers in the registry, tolerate individual source failures, deduplicate results, rank them, and write a single queue:

```bash
career-os batch config/companies.json \
  --output applications/ranked-opportunities.csv \
  --errors applications/ingestion-errors.log
```

`config/companies.json` is intentionally conservative. A company entry should be enabled only after its public Greenhouse board token or Lever site identifier has been verified from the employer's official careers page.

## Operating Model

1. Source verified openings from company career pages and permitted public ATS feeds.
2. Normalize title, employer, salary, location restrictions, responsibilities, and requirements.
3. Deduplicate listings using canonical posting URLs, retaining the more complete record.
4. Score each opportunity against `strategy/opportunity-scoring.md`.
5. Reject openings that fail salary, Florida eligibility, employment-type, or material qualification gates.
6. Produce an application brief for each qualified opening.
7. Tailor canonical resume content only for roles that clear the application threshold.
8. Record the exact resume path and commit SHA used.
9. Track submissions, follow-ups, interviews, outcomes, and evidence learned from the market.
10. Update positioning based on observed response rates rather than assumptions.

## Evidence Standard

- **Verified:** directly supported by a repository, credential, employment record, job posting, or measurable artifact.
- **Inferred:** reasonable interpretation of verified evidence, clearly labeled.
- **Unverified:** excluded from external applications until confirmed.
- **Planned:** roadmap work; never represented as deployed or production-proven.

## Repository Structure

```text
career-os/
├── README.md
├── config/
│   └── companies.json
├── src/career_os/
│   ├── adapters/
│   ├── batch.py
│   ├── cli.py
│   ├── models.py
│   └── scoring.py
├── architecture/
│   └── repository-boundaries.md
├── strategy/
│   ├── search-strategy.md
│   └── opportunity-scoring.md
├── applications/
│   ├── application-record.schema.json
│   └── tracker.csv
├── templates/
│   ├── application-brief.md
│   └── interview-story.md
├── evidence/
│   └── portfolio-index.md
└── tests/
```

## Current Status

The ingestion and scoring core supports local files, Greenhouse, Lever, registry-driven batch collection, deduplication, ranked CSV output, and automated CI tests. The next stage is populating verified target-company identifiers and generating application briefs for qualified roles.
