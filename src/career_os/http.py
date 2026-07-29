from __future__ import annotations

import json
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class FetchError(RuntimeError):
    """Raised when a public job feed cannot be retrieved or decoded."""


def fetch_json(url: str, timeout: float = 20.0) -> Any:
    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "CareerOS/0.1 (+https://github.com/AudioJones-Dev/career-os)",
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            payload = response.read().decode(charset)
    except HTTPError as exc:
        raise FetchError(f"HTTP {exc.code} while fetching {url}") from exc
    except URLError as exc:
        raise FetchError(f"Network error while fetching {url}: {exc.reason}") from exc

    try:
        return json.loads(payload)
    except json.JSONDecodeError as exc:
        raise FetchError(f"Invalid JSON returned by {url}") from exc
