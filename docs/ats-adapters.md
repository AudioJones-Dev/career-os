# Public ATS Adapters

Career OS currently supports structured public feeds from Greenhouse and Lever.

## Greenhouse

```bash
career-os greenhouse <board-token> --company "Company Name" --output applications/company.csv
```

The board token is the identifier used by the employer's public Greenhouse board. The adapter requests the public board API with job content enabled, then normalizes title, location, description, URL, salary evidence, remote status, and Florida eligibility.

## Lever

```bash
career-os lever <site> --company "Company Name" --output applications/company.csv
```

The site value is the employer identifier used in its public Lever URL. The adapter requests the public postings endpoint in JSON mode and normalizes the returned records.

## Evidence behavior

- Salary is extracted only when the posting includes a recognizable U.S. dollar range.
- Florida eligibility remains unknown unless the posting explicitly includes or excludes Florida.
- A generic U.S.-remote label does not prove Florida eligibility.
- Raw source payloads remain attached to normalized records for auditability.
- The adapters do not submit applications, bypass access controls, or scrape authenticated pages.
