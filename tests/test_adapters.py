from career_os.adapters.greenhouse import normalize_greenhouse_job
from career_os.adapters.lever import normalize_lever_job


def test_greenhouse_normalizes_remote_salary() -> None:
    job = normalize_greenhouse_job({
        "id": 123,
        "title": "Business Operations Manager",
        "absolute_url": "https://example.com/jobs/123",
        "location": {"name": "Remote, United States"},
        "content": "<p>Salary range: $100,000 - $140,000.</p>",
    }, company="Example")
    assert job.remote_status == "remote"
    assert job.salary_min == 100000
    assert job.salary_max == 140000
    assert job.source == "greenhouse"


def test_lever_normalizes_remote_salary_and_type() -> None:
    job = normalize_lever_job({
        "id": "abc",
        "text": "Implementation Manager",
        "hostedUrl": "https://jobs.lever.co/example/abc",
        "descriptionPlain": "Remote within the United States. Compensation $95k to $125k.",
        "categories": {"location": "Remote", "commitment": "Full-time"},
        "lists": [],
    }, company="Example")
    assert job.remote_status == "remote"
    assert job.salary_min == 95000
    assert job.salary_max == 125000
    assert job.employment_type == "full-time"
    assert job.source == "lever"
