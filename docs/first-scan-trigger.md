# First Scan Trigger

The opportunity-scan workflow supports manual dispatch and weekday scheduling. It also runs when either of these operational files changes on `main`:

- `config/companies.json`
- `.github/workflows/opportunity-scan.yml`

This narrow push trigger allows registry changes to be validated immediately without running an external scan on unrelated code changes.
