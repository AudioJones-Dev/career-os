# Portfolio Link Strategy

Governs which URLs are attached to an application, by role family. Replaces per-application improvisation with a default and a documented reason to deviate.

## Canonical Surfaces

| Surface | Use in applications | Rationale |
|---|---|---|
| https://tyronenelms.com | **Default portfolio link** | Employer-facing, individually owned, positioning matches the search thesis |
| https://github.com/AudioJones-Dev | Default for technical evaluators | Evidence repositories, browsable depth |
| https://www.linkedin.com/in/audiojones | Include when the form has a LinkedIn field | Recruiter-standard surface |
| https://audiojones.com | **Excluded by default** | Client-facing consultancy sales surface — see Exclusions |
| GitHub Pages portal (`site/` of Tyrone-Nelms-Resume) | Not until deploy status is confirmed | Deploy unverified; audience overlaps tyronenelms.com |

The registry of record for these surfaces is `docs/public-surfaces.md` in the Tyrone-Nelms-Resume repository. Career OS consumes that registry; it does not redefine it.

## Default Package

Unless a role family below overrides it, every application attaches:

1. **Portfolio:** https://tyronenelms.com
2. **GitHub:** https://github.com/AudioJones-Dev
3. **LinkedIn:** https://www.linkedin.com/in/audiojones — only where a field exists for it

Attach the portfolio link even when the form marks it optional. A governed portfolio surface is a differentiator in operations and implementation hiring, where most applicants submit a resume alone.

## By Role Family

Role families follow `strategy/search-strategy.md`. "Lead with" names the case study or evidence source to foreground in the cover letter or a portfolio-context field — not a different URL.

### Business operations and operational excellence (40% of targeting)

- Links: default package
- Lead with: Florida Ramp & Lift FieldOps (operational pilot), enterprise operations record
- Emphasis: process design, operational controls, service delivery under real constraints

### Implementation and professional services (25%, shared with program delivery)

- Links: default package
- Lead with: Florida Ramp & Lift FieldOps, VPL Flow (`specified`)
- Emphasis: requirements engineering, stakeholder discovery, approval gates, rollout sequencing
- Note: VPL Flow is specification-stage. State that plainly — requirements-heavy roles value the artifact honestly labeled, and overclaiming it is the fastest way to lose a technical screen.

### Program and project delivery

- Links: default package
- Lead with: Florida Ramp & Lift FieldOps, Google Project Management credential
- Emphasis: schedule, coordination, contractor and vendor management, governance

### Customer and service operations (15%)

- Links: default package; GitHub is optional and lower value here
- Lead with: enterprise customer operations record (Salesforce, escalations, adherence, mentoring)
- Emphasis: verified employment evidence over project artifacts — this family rewards operating history

### Business systems and CRM operations (10%)

- Links: default package
- Lead with: AJ Digital OS V1, Business Memory Architecture
- Emphasis: systems analysis, data and information modeling, integration surfaces

### Digital transformation and AI operations (10%, stretch)

- Links: default package, GitHub weighted equally with the portfolio
- Lead with: AJ Digital OS V1, HDIKIT
- Emphasis: AI-enabled workflow design, operator controls, governance
- Note: this is the one family where referencing AJ Digital as an operating consultancy is contextually appropriate — as background establishing that the entity is real, never as a services pitch, and never with its published performance metrics.

### Knowledge operations and AI governance

- Links: default package
- Lead with: HDIKIT, Business Memory Architecture
- Emphasis: evidence management, claim verification, decision traceability, provenance

## Exclusions

### audiojones.com

Not attached to employment applications. Two independent reasons:

1. **Audience mismatch.** It sells consulting services to founder-led businesses. A hiring manager evaluating a full-time candidate reads an active sales funnel as a competing commitment, not as evidence of capability.
2. **Metric contamination.** The site publishes engagement-performance percentages whose measurement basis is not documented in the evidence chain. Linking it inside an application implicitly submits those figures as part of the candidate claim. That conflicts with the evidence rules in `evidence/portfolio-index.md`.

If an employer asks directly about the consultancy, answer honestly and reference it — the entity is real and is part of the record. That is a conversation, not a link in a submission package.

### Never in an application package

- Private repositories (HDIKIT, the Florida Ramp & Lift operational pilot, VPL Flow) — offer a walkthrough instead
- Any percentage, revenue effect, or cost saving not present in the canonical accomplishment record
- Client-identifying detail from AJ Digital or Florida Ramp & Lift engagements

## Pre-Submission Check

Before submitting, confirm:

- [ ] Portfolio link resolves and the destination reflects the current positioning
- [ ] No link in the package leads to a surface carrying unverified metrics
- [ ] Every private-repository reference is framed as "walkthrough available," not as a link
- [ ] Maturity labels in any linked or described artifact match `architecture/repository-boundaries.md`
- [ ] The featured evidence matches the role family above, or the deviation is recorded in the application brief

## Maintenance

Surfaces change without this repository being touched. Re-verify the destinations quarterly, and immediately after any known site redeploy. When `docs/public-surfaces.md` changes in the resume repository, reconcile this file in the same week.
