from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class JobOpportunity:
    source: str
    source_id: str
    title: str
    company: str
    url: str
    description: str = ""
    location: str = ""
    remote_status: str = "unknown"
    florida_eligible: bool | None = None
    employment_type: str = "full-time"
    salary_min: int | None = None
    salary_max: int | None = None
    currency: str = "USD"
    requirements: list[str] = field(default_factory=list)
    responsibilities: list[str] = field(default_factory=list)
    posted_at: str | None = None
    retrieved_at: str | None = None
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "JobOpportunity":
        known = {f.name for f in cls.__dataclass_fields__.values()}
        payload = {k: v for k, v in data.items() if k in known}
        payload.setdefault("source", "manual")
        payload.setdefault("source_id", data.get("id", data.get("url", "unknown")))
        payload.setdefault("raw", {k: v for k, v in data.items() if k not in known})
        return cls(**payload)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
