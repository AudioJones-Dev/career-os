# Job Ingestion MVP

## Purpose

Convert externally collected job postings into a normalized, auditable dataset and apply the Career OS qualification policy consistently.

This MVP does **not** bypass website terms, authentication, robots controls, or application workflows. Collection adapters must use permitted APIs, public company ATS feeds, user-provided exports, or manually saved posting data.

## Accepted input

The CLI accepts JSON or JSONL. Required fields are:

- `source`
- `source_id`
- `title`
- `company`
- `url`

High-value qualification fields:

- `remote_status`
- `florida_eligible`
- `salary_min`
- `salary_max`
- `description`
- `requirements`
- `responsibilities`

## Run

```bash
python -m pip install -e .
career-os data/sample-jobs.json --output applications/scored-opportunities.csv
```

## Decision policy

- `priority`: score 80–100
- `apply`: score 70–79
- `review`: score 55–69
- `reject`: score below 55 or a hard disqualifier

Hard disqualifiers currently include:

- Florida explicitly excluded
- Published salary ceiling below $90,000

Unknown salary or Florida eligibility is treated as a verification gap, not silently assumed.

## Planned adapters

1. Greenhouse public job-board API
2. Lever public postings API
3. Ashby public job-board data where permitted
4. Company career-page imports
5. Indeed/LinkedIn user-export or manually captured postings

Each adapter must preserve the source URL, retrieval time, raw payload, and normalization warnings.
