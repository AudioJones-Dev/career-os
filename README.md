# Career OS

Career OS is Tyrone Nelms' operating system for securing a full-time remote U.S. role with a target base salary of **$90,000 or more**.

It coordinates career positioning, job sourcing, opportunity scoring, tailored application assets, portfolio evidence, interview preparation, and application tracking.

## Canonical Sources

- Resume source of truth: https://github.com/AudioJones-Dev/Tyrone-Nelms-Resume
- LinkedIn: https://www.linkedin.com/in/audiojones
- GitHub portfolio: https://github.com/AudioJones-Dev

## Target Positioning

**Operations & Business Systems Leader | Process Improvement | AI-Enabled Workflows | Program Delivery**

Primary target roles:

- Business Operations Manager
- Operations Manager
- Business Systems Manager
- Implementation Manager
- Program Manager
- Customer Operations Manager
- Service Operations Manager
- Digital Transformation Manager
- AI Operations Manager
- Knowledge Operations Manager
- Process Improvement Manager

## Compensation and Work Constraints

- Minimum target base salary: **$90,000**
- Preferred arrangement: **Remote, full-time, United States**
- Geographic plan: Florida relocation flexibility, including Fort Myers, Cape Coral, and surrounding areas
- Reject roles that are nominally remote but exclude Florida unless the role provides a viable relocation path

## Operating Model

1. Source verified openings from company career pages and reputable job platforms.
2. Normalize title, employer, salary, location restrictions, responsibilities, and requirements.
3. Score each opportunity against the career criteria in `strategy/opportunity-scoring.md`.
4. Tailor the resume and supporting materials only for roles that clear the application threshold.
5. Track submissions, follow-ups, interviews, outcomes, and evidence learned from the market.
6. Update positioning based on observed response rates rather than assumptions.

## Evidence Standard

Career OS follows an explicit evidence policy:

- **Verified:** directly supported by a repository, credential, employment record, job posting, or measurable artifact.
- **Inferred:** reasonable interpretation of verified evidence, clearly labeled.
- **Unverified:** excluded from external applications until confirmed.
- **Planned:** roadmap work; never represented as deployed or production-proven.

## Initial Structure

```text
career-os/
├── README.md
├── strategy/
│   ├── search-strategy.md
│   └── opportunity-scoring.md
├── applications/
│   ├── application-record.schema.json
│   └── tracker.csv
├── templates/
│   ├── application-brief.md
│   └── interview-story.md
└── evidence/
    └── portfolio-index.md
```

## Current Status

Foundation initialized. The next implementation stage is the job-ingestion and scoring workflow, followed by Indeed/LinkedIn profile execution and application tracking.
