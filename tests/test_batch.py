from pathlib import Path

import pytest

from career_os.batch import CompanySource, canonical_job_key, deduplicate_jobs, load_company_registry
from career_os.models import JobOpportunity


def test_company_source_rejects_unknown_adapter() -> None:
    with pytest.raises(ValueError, match="Unsupported source"):
        CompanySource.from_dict({"company": "Acme", "source": "workday", "identifier": "acme"})


def test_registry_loads_enabled_and_disabled_sources(tmp_path: Path) -> None:
    registry = tmp_path / "companies.json"
    registry.write_text(
        '{"companies": ['
        '{"company":"A","source":"greenhouse","identifier":"a","enabled":true},'
        '{"company":"B","source":"lever","identifier":"b","enabled":false}'
        ']}',
        encoding="utf-8",
    )
    rows = load_company_registry(registry)
    assert len(rows) == 2
    assert rows[0].enabled is True
    assert rows[1].enabled is False


def test_deduplicate_prefers_more_complete_record() -> None:
    sparse = JobOpportunity(
        source="greenhouse", source_id="1", company="Acme", title="Operations Manager",
        url="https://jobs.example.com/roles/1?gh_jid=1", location="Remote",
    )
    complete = JobOpportunity(
        source="lever", source_id="x", company="Acme", title="Operations Manager",
        url="https://jobs.example.com/roles/1", location="Remote, United States",
        description="Lead cross-functional operations.", salary_min=100000, salary_max=130000,
        remote_status="remote",
    )
    result = deduplicate_jobs([sparse, complete])
    assert result == [complete]


def test_canonical_key_removes_query_and_trailing_slash() -> None:
    job = JobOpportunity(
        source="manual", source_id="1", company="A", title="Role",
        url="HTTPS://Jobs.Example.com/roles/1/?source=board",
    )
    assert canonical_job_key(job) == "url:https://jobs.example.com/roles/1"
