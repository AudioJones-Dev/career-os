from career_os.models import JobOpportunity
from career_os.scoring import score_job


def test_rejects_salary_ceiling_below_floor() -> None:
    job = JobOpportunity(
        source="test", source_id="1", title="Operations Manager", company="Example", url="https://example.com/1",
        remote_status="remote", florida_eligible=True, salary_min=70_000, salary_max=85_000,
    )
    result = score_job(job)
    assert result.score == 0
    assert result.decision == "reject"


def test_rejects_florida_exclusion() -> None:
    job = JobOpportunity(
        source="test", source_id="2", title="Business Operations Manager", company="Example", url="https://example.com/2",
        remote_status="remote", florida_eligible=False, salary_min=120_000, salary_max=150_000,
    )
    assert score_job(job).decision == "reject"


def test_prioritizes_verified_high_fit_role() -> None:
    job = JobOpportunity(
        source="test", source_id="3", title="Business Operations Manager", company="Example", url="https://example.com/3",
        remote_status="remote", florida_eligible=True, salary_min=115_000, salary_max=145_000,
        description="Lead operations, process improvement, workflow automation, CRM implementation, stakeholder management, and SOP development.",
    )
    result = score_job(job)
    assert result.score >= 80
    assert result.decision == "priority"
