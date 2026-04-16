from __future__ import annotations

from datetime import UTC, datetime
import unittest
from unittest.mock import patch

from scripts.check_site_health import (
    HttpCheckResult,
    _build_basic_auth_header,
    _days_until,
    _parse_not_after,
    _require_authenticated_access,
    _require_unauthenticated_protection,
    run_checks,
)


class CheckSiteHealthTests(unittest.TestCase):
    def test_build_basic_auth_header_uses_expected_scheme(self) -> None:
        self.assertEqual(
            _build_basic_auth_header("admin", "secret"),
            "Basic YWRtaW46c2VjcmV0",
        )

    def test_parse_not_after_returns_utc_datetime(self) -> None:
        parsed = _parse_not_after("Wed, 30 Apr 2026 12:00:00 GMT")
        self.assertEqual(parsed.tzinfo, UTC)
        self.assertEqual(parsed.year, 2026)
        self.assertEqual(parsed.month, 4)
        self.assertEqual(parsed.day, 30)

    def test_days_until_never_returns_negative_values(self) -> None:
        now = datetime(2026, 4, 16, tzinfo=UTC)
        self.assertEqual(_days_until(datetime(2026, 4, 20, tzinfo=UTC), now=now), 4)
        self.assertEqual(_days_until(datetime(2026, 4, 10, tzinfo=UTC), now=now), 0)

    def test_require_unauthenticated_protection_rejects_missing_basic_challenge(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "Basic auth"):
            _require_unauthenticated_protection(
                HttpCheckResult(status=401, headers={}, body=""),
                "https://coderlap.com",
            )

    def test_require_authenticated_access_rejects_missing_body_token(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "expected body token"):
            _require_authenticated_access(
                HttpCheckResult(status=200, headers={}, body="wrong body"),
                "https://coderlap.com",
                "CoderLAP",
            )

    def test_run_checks_calls_dns_tls_and_http_for_each_url(self) -> None:
        with (
            patch("scripts.check_site_health._resolve_host", return_value=["203.0.113.10"]) as resolve_host,
            patch(
                "scripts.check_site_health._fetch_cert_expiry",
                return_value=datetime(2026, 5, 30, tzinfo=UTC),
            ) as fetch_cert_expiry,
            patch(
                "scripts.check_site_health._fetch_url",
                side_effect=[
                    HttpCheckResult(status=401, headers={"www-authenticate": "Basic realm=\"restricted\""}, body=""),
                    HttpCheckResult(status=200, headers={}, body="CoderLAP ready"),
                    HttpCheckResult(status=401, headers={"www-authenticate": "Basic realm=\"restricted\""}, body=""),
                    HttpCheckResult(status=200, headers={}, body="CoderLAP ready"),
                ],
            ) as fetch_url,
        ):
            lines = run_checks(
                urls=["https://coderlap.com", "https://www.coderlap.com"],
                username="admin",
                password="secret",
                timeout=10,
                min_cert_days=7,
                body_token="CoderLAP",
            )

        self.assertEqual(resolve_host.call_count, 2)
        self.assertEqual(fetch_cert_expiry.call_count, 2)
        self.assertEqual(fetch_url.call_count, 4)
        self.assertEqual(len(lines), 8)


if __name__ == "__main__":
    unittest.main()
