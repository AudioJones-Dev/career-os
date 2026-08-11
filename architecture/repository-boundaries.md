# Repository Boundaries

Career OS coordinates career acquisition work without duplicating canonical content or technical evidence.

## 1. Career OS

Repository: https://github.com/AudioJones-Dev/career-os

Owns:

- job sourcing and normalization
- opportunity scoring
- application decisions
- tailoring instructions
- recruiter and company research
- application tracking
- interview preparation
- compensation and offer comparison
- market-feedback analysis

Career OS may reference external repositories but does not silently rewrite their canonical content.

## 2. Tyrone-Nelms-Resume

Repository: https://github.com/AudioJones-Dev/Tyrone-Nelms-Resume

Owns:

- master resume
- role-specific resume variants
- LinkedIn and Indeed profile copy
- professional biographies
- achievement library
- capability statements
- employer-facing case-study copy
- exported PDF and DOCX resume artifacts

Career OS records which resume version was used for each application by repository path and commit SHA.

## 3. Evidence Repositories

Evidence repositories support specific portfolio claims.

Current priority sources:

- AJ Digital OS V1: https://github.com/AudioJones-Dev/AJ-DIGITAL-OS-V1
- HDIKIT: private repository — walkthrough available
- Florida Ramp & Lift operational pilot: private repository — walkthrough available
- Florida Ramp & Lift planning and governance foundation: https://github.com/AudioJones-Dev/florida-ramp-and-lift-ops
- VPL Flow specified operations architecture: private repository — walkthrough available; no application code or production claim
- Founder Intelligence System: https://github.com/AudioJones-Dev/founder-intelligence-system
- ResponseOS: https://github.com/AudioJones-Dev/responseos

Each external claim must identify the supporting repository, file or artifact, and maturity state.

## 4. Public Web Surfaces

The recruiter-facing portfolio anticipated by earlier versions of this document **now exists and is live.** This section is corrected accordingly.

### tyronenelms.com

The primary employer-facing portfolio. Owns presentation and navigation only; it sources verified content from the resume and evidence repositories and must not originate facts.

Career OS treats it as the default portfolio link for applications and as a surface subject to the same maturity vocabulary as any evidence repository.

### audiojones.com

The AJ Digital LLC commercial brand surface. Owned by the consulting entity, **not** by the career system. It serves prospective clients, not employers.

Career OS does not govern its content and does not link it in application packages. Performance metrics published there are outside this system's evidence chain and are barred from career artifacts.

### GitHub Pages portal

`site/` in Tyrone-Nelms-Resume deploys to GitHub Pages and carries no custom domain — it does not serve tyronenelms.com. Deploy status is unconfirmed and its audience overlaps tyronenelms.com. Not used in applications until that overlap is resolved.

### Governance

The registry of record is `docs/public-surfaces.md` in Tyrone-Nelms-Resume. Link selection is governed by `strategy/portfolio-link-strategy.md`. Career OS consumes both; it does not silently rewrite the surface registry, consistent with §1.

No new portfolio repository or public surface may be created until its content model, privacy boundaries, and publication plan are approved.

## Maturity Vocabulary

Use only these maturity labels:

- `concept`: articulated idea without a formal specification
- `specified`: requirements, architecture, schemas, or workflows documented
- `prototype`: functional demonstration with limited operational scope
- `operational_pilot`: usable in a bounded real-world operating context
- `production`: deployed, supported, and used for live operations
- `frozen_reference`: retained as reviewed source material but not an active runtime

Roadmap functionality must never be described as implemented functionality.
