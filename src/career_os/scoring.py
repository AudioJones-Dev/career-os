from __future__ import annotations

from dataclasses import dataclass

from .models import JobOpportunity

TARGET_TITLES = {
    "business operations manager": 18,
    "operations manager": 18,
    "business systems manager": 17,
    "implementation manager": 17,
    "program manager": 16,
    "customer operations manager": 16,
    "service operations manager": 16,
    "digital transformation manager": 15,
    "ai operations manager": 15,
    "process improvement manager": 15,
}

PROOF_KEYWORDS = {
    "operations": 4,
    "process improvement": 4,
    "implementation": 4,
    "program management": 4,
    "project management": 3,
    "customer operations": 4,
    "crm": 3,
    "salesforce": 3,
    "workflow": 3,
    "automation": 3,
    "stakeholder": 3,
    "sop": 3,
    "knowledge management": 3,
    "ai": 2,
}


@dataclass(slots=True)
class ScoreResult:
    score: int
    decision: str
    reasons: list[str]
    gaps: list[str]


def score_job(job: JobOpportunity) -> ScoreResult:
    reasons: list[str] = []
    gaps: list[str] = []
    text = f"{job.title} {job.description} {' '.join(job.requirements)}".lower()

    if job.florida_eligible is False:
        return ScoreResult(0, "reject", [], ["Remote role explicitly excludes Florida."])
    if job.salary_max is not None and job.salary_max < 90_000:
        return ScoreResult(0, "reject", [], ["Published salary ceiling is below $90,000."])
    if job.employment_type.lower() not in {"full-time", "full time", "fte"}:
        gaps.append("Role is not clearly full-time employment.")

    score = 0
    normalized_title = job.title.lower().strip()
    title_points = max((points for title, points in TARGET_TITLES.items() if title in normalized_title), default=5)
    score += title_points
    reasons.append(f"Role-family alignment: +{title_points}.")

    if job.remote_status.lower() in {"remote", "fully remote", "remote-us", "remote us"}:
        score += 15
        reasons.append("Verified remote arrangement: +15.")
    elif "remote" in job.location.lower():
        score += 10
        reasons.append("Remote indicated in location: +10; eligibility still requires verification.")
    else:
        gaps.append("Remote status is not verified.")

    if job.florida_eligible is True:
        score += 10
        reasons.append("Florida eligibility verified: +10.")
    else:
        gaps.append("Florida eligibility is unknown.")

    if job.salary_min is not None:
        if job.salary_min >= 110_000:
            score += 20
            reasons.append("Published base floor is at least $110,000: +20.")
        elif job.salary_min >= 90_000:
            score += 16
            reasons.append("Published base floor clears $90,000: +16.")
        else:
            score += 5
            gaps.append("Published salary range begins below $90,000.")
    elif job.salary_max is not None and job.salary_max >= 90_000:
        score += 6
        gaps.append("Only salary ceiling clears the target; base floor is unknown.")
    else:
        gaps.append("Compensation is not published or verified.")

    keyword_points = 0
    matched = []
    for keyword, points in PROOF_KEYWORDS.items():
        if keyword in text:
            keyword_points += points
            matched.append(keyword)
    keyword_points = min(keyword_points, 25)
    score += keyword_points
    if matched:
        reasons.append(f"Evidence-aligned keywords ({', '.join(matched[:6])}): +{keyword_points}.")

    if any(term in text for term in ("bachelor's required", "bachelors required", "mba required", "security clearance required")):
        score -= 12
        gaps.append("Posting contains a likely hard credential barrier.")

    score = max(0, min(100, score))
    if score >= 80:
        decision = "priority"
    elif score >= 70:
        decision = "apply"
    elif score >= 55:
        decision = "review"
    else:
        decision = "reject"
    return ScoreResult(score, decision, reasons, gaps)
