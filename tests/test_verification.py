from career_os.models import JobOpportunity
from career_os.scoring import score_job
from career_os.verification import apply_verification, verify_job


def test_verifies_us_remote_florida_and_salary() -> None:
    job = JobOpportunity(
        source="test",
        source_id="1",
        title="Implementation Manager",
        company="Example",
        url="https://example.com/1",
        remote_status="unknown",
        florida_eligible=None,
        employment_type="unknown",
        description=(
            "This is a full-time, fully remote role available anywhere in the United States. "
            "The base salary range is $105,000 to $135,000. Up to 10% travel."
        ),
    )
    result = verify_job(job)
    assert result.status == "complete"
    assert result.florida_eligible is True
    assert result.remote_status == "remote"
    assert result.employment_type == "full-time"
    assert result.salary_min == 105_000
    assert result.salary_max == 135_000
    assert result.travel_percentage == 10
    assert result.confidence >= 0.9


def test_detects_florida_exclusion() -> None:
    job = JobOpportunity(
        source="test", source_id="2", title="Operations Manager", company="Example",
        url="https://example.com/2", florida_eligible=None,
        description="Remote in the US, but this position is not available in Florida.",
    )
    result = verify_job(job)
    assert result.florida_eligible is False
    apply_verification(job, result)
    assert score_job(job).decision == "reject"


def test_detects_clearance_and_sponsorship() -> None:
    job = JobOpportunity(
        source="test", source_id="3", title="Program Manager", company="Example",
        url="https://example.com/3",
        description="An active Secret clearance is required. We are unable to sponsor employment visas.",
    )
    result = verify_job(job)
    assert result.clearance_required is True
    assert result.sponsorship_status == "not-offered"


def test_preserves_unresolved_evidence_as_verify() -> None:
    job = JobOpportunity(
        source="test", source_id="4", title="Implementation Manager", company="Example",
        url="https://example.com/4", remote_status="remote", employment_type="full-time",
        description="Lead implementation, workflow automation, and stakeholder management.",
    )
    result = verify_job(job)
    assert result.status == "unresolved"
    assert "florida_eligibility" in result.unresolved
    assert "compensation" in result.unresolved
    apply_verification(job, result)
    assert score_job(job).decision == "verify"
