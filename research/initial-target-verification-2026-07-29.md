# Initial Target Verification — 2026-07-29

This file records the first verified public ATS identifiers added to `config/companies.json`.

## Verification standard

An identifier is enabled only when a current public job page or employer job board resolves on the official Greenhouse or Lever domain and exposes the employer-specific path used by the adapter.

## Verified Lever sites

| Company | Lever identifier | Evidence observed | Initial rationale |
|---|---|---|---|
| Arcadia | `arcadia` | Current Implementation Manager posting at `jobs.lever.co/arcadia/...` | Direct match to implementation leadership; remote USA; published range observed at $100,000–$135,000. |
| Swiftly | `goswift` | Current Implementation Manager (SaaS) posting at `jobs.lever.co/goswift/...` | Strong implementation, customer delivery, technical coordination, and operational ownership fit. |
| Vida Health | `vida` | Current Growth Operations Program Manager posting at `jobs.lever.co/vida/...` | Direct operations-program role; United States remote; posting excludes several states but not Florida. |
| Rover | `rover` | Current Manager I, Content Program Management posting at `jobs.lever.co/rover/...` | Knowledge operations, content systems, frontline enablement, and program management alignment; Florida explicitly listed as eligible. |
| Sure | `sure` | Current Product Implementation Manager listing on `jobs.lever.co/sure` | Direct implementation-management fit in a technology company. |
| BAMKO | `bamko` | Current Implementation Manager listing on `jobs.lever.co/bamko` | Remote, full-time implementation role with broad delivery and account-management relevance. |
| Arbital Health | `arbitalhealth` | Current Technical Implementation Manager posting at `jobs.lever.co/arbitalhealth/...` | Strong technical implementation and data-oriented delivery fit; retained as tier 2 because domain-specific healthcare experience may be a material requirement. |
| Agile Defense | `agile-defense` | Current employer board at `jobs.lever.co/agile-defense` with operations and program-management roles | Florida-based program roles and remote operational roles; retained as tier 2 because some positions may require federal-sector credentials or clearance. |

## Excluded from the initial registry

- Jobgether was not enabled because it frequently republishes roles on behalf of undisclosed partner companies, weakening employer attribution and application provenance.
- Stale postings and boards without a current relevant role were not used as the sole basis for activation.

## Review cadence

Re-verify enabled identifiers at least monthly and disable any source that stops resolving, changes ATS provider, or no longer presents a credible target-role pipeline.
