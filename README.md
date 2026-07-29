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
- HDIKIT: https://github.com/AudioJones-Dev/HDIKIT
- Florida Ramp & Lift operational pilot: https://github.com/AudioJones-Dev/FRL-CONTRACTOR-PORTAL
- Florida Ramp & Lift planning and governance foundation: https://github.com/AudioJones-Dev/florida-ramp-and-lift-ops
- Founder Intelligence System: https://github.com/AudioJones-Dev/founder-intelligence-system
- ResponseOS: https://github.com/AudioJones-Dev/responseos

See `architecture/repository-boundaries.md` for ownership rules and maturity labels.

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
3. Score each opportunity against `strategy/opportunity-scoring.md`.
4. Reject openings that fail salary, Florida eligibility, employment-type, or material qualification gates.
5. Produce an application brief for each qualified opening.
6. Tailor canonical resume content only for roles that clear the application threshold.
7. Record the exact resume path and commit SHA used.
8. Track submissions, follow-ups, interviews, outcomes, and evidence learned from the market.
9. Update positioning based on observed response rates rather than assumptions.

## Evidence Standard

Career OS follows an explicit evidence policy:

- **Verified:** directly supported by a repository, credential, employment record, job posting, or measurable artifact.
- **Inferred:** reasonable interpretation of verified evidence, clearly labeled.
- **Unverified:** excluded from external applications until confirmed.
- **Planned:** roadmap work; never represented as deployed or production-proven.

## Repository Structure

```text
career-os/
├── README.md
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
└── evidence/
    └── portfolio-index.md
```

## Current Status

Foundation and repository contracts are initialized. The next implementation stage is job ingestion and normalization, followed by automated scoring, application-brief generation, and profile execution on Indeed and LinkedIn.
