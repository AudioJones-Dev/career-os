# Opportunity Scan Operations

Career OS runs the verified company registry through GitHub Actions and retains each ranked queue as a workflow artifact.

## Schedule

The workflow runs Monday through Friday at `12:15 UTC`. GitHub cron schedules use UTC and may start several minutes after the requested time.

The workflow can also be started manually from **Actions → opportunity-scan → Run workflow**. The optional `registry` input defaults to `config/companies.json`.

## Outputs

Each run uploads a 30-day artifact named `career-opportunity-scan-<run-number>` containing:

- `ranked-opportunities.csv`
- `ingestion-errors.log`
- `scan-metadata.txt`

The workflow summary displays the opportunity count and the first ten ranked records. The CSV remains the authoritative output.

## Failure behavior

A failure from one configured employer is written to `ingestion-errors.log` while the remaining sources continue. Workflow-level failures are reserved for installation problems, a missing registry, failure to produce artifacts, or an unhandled application error.

## Evidence controls

- Only enabled registry records are scanned.
- ATS identifiers must be verified against official employer career infrastructure.
- Unknown salary or Florida eligibility remains unresolved rather than being treated as favorable.
- The workflow does not submit applications or access authenticated job platforms.

## Manual command

The GitHub Actions workflow executes the equivalent of:

```bash
career-os batch config/companies.json \
  --output applications/scan-results/ranked-opportunities.csv \
  --errors applications/scan-results/ingestion-errors.log
```
