from __future__ import annotations

import argparse
import base64
import os
import socket
import ssl
from dataclasses import dataclass
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


DEFAULT_BODY_TOKEN = "CoderLAP"
DEFAULT_TIMEOUT_SECONDS = 10
DEFAULT_MIN_CERT_DAYS = 21


@dataclass(frozen=True)
class HttpCheckResult:
    status: int
    headers: dict[str, str]
    body: str


def _build_basic_auth_header(username: str, password: str) -> str:
    raw = f"{username}:{password}".encode("utf-8")
    encoded = base64.b64encode(raw).decode("ascii")
    return f"Basic {encoded}"


def _parse_not_after(not_after: str) -> datetime:
    parsed = parsedate_to_datetime(not_after)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC)


def _days_until(target: datetime, *, now: datetime | None = None) -> int:
    now_utc = now or datetime.now(UTC)
    delta = target - now_utc
    return max(0, delta.days)


def _resolve_host(hostname: str) -> list[str]:
    results = socket.getaddrinfo(hostname, 443, type=socket.SOCK_STREAM)
    resolved: list[str] = []
    for result in results:
        address = result[4][0]
        if address not in resolved:
            resolved.append(address)
    return resolved


def _fetch_url(url: str, *, timeout: int, authorization: str | None = None) -> HttpCheckResult:
    request = Request(url, method="GET")
    request.add_header("User-Agent", "CoderLAP health check")
    if authorization:
        request.add_header("Authorization", authorization)

    try:
        with urlopen(request, timeout=timeout) as response:
            status = response.status
            headers = {key.lower(): value for key, value in response.headers.items()}
            body = response.read().decode("utf-8", errors="ignore")
            return HttpCheckResult(status=status, headers=headers, body=body)
    except HTTPError as error:
        headers = {key.lower(): value for key, value in error.headers.items()}
        body = error.read().decode("utf-8", errors="ignore")
        return HttpCheckResult(status=error.code, headers=headers, body=body)
    except URLError as error:
        raise RuntimeError(f"Request failed for {url}: {error.reason}") from error


def _fetch_cert_expiry(hostname: str, *, timeout: int) -> datetime:
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=timeout) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as tls_sock:
            cert = tls_sock.getpeercert()
    not_after = cert.get("notAfter")
    if not not_after:
        raise RuntimeError(f"TLS certificate for {hostname} does not expose notAfter")
    return _parse_not_after(not_after)


def _require_unauthenticated_protection(result: HttpCheckResult, url: str) -> None:
    if result.status != 401:
        raise RuntimeError(f"{url} returned {result.status} instead of 401 for unauthenticated access")
    challenge = result.headers.get("www-authenticate", "")
    if "basic" not in challenge.lower():
        raise RuntimeError(f"{url} did not advertise Basic auth in WWW-Authenticate")


def _require_authenticated_access(result: HttpCheckResult, url: str, body_token: str) -> None:
    if result.status != 200:
        raise RuntimeError(f"{url} returned {result.status} instead of 200 for authenticated access")
    if body_token and body_token not in result.body:
        raise RuntimeError(f"{url} returned 200 but did not contain expected body token '{body_token}'")


def _write_summary(lines: Iterable[str]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    with open(summary_path, "a", encoding="utf-8") as handle:
        handle.write("### CoderLAP Site Health\n")
        for line in lines:
            handle.write(f"- {line}\n")


def run_checks(
    *,
    urls: list[str],
    username: str,
    password: str,
    timeout: int,
    min_cert_days: int,
    body_token: str,
) -> list[str]:
    lines: list[str] = []
    authorization = _build_basic_auth_header(username, password)

    for url in urls:
        parsed = urlparse(url)
        hostname = parsed.hostname
        if not hostname:
            raise RuntimeError(f"Invalid URL without hostname: {url}")

        resolved = _resolve_host(hostname)
        if not resolved:
            raise RuntimeError(f"DNS resolution returned no addresses for {hostname}")
        lines.append(f"DNS OK: {hostname} -> {', '.join(resolved[:3])}")

        expires_at = _fetch_cert_expiry(hostname, timeout=timeout)
        days_remaining = _days_until(expires_at)
        if days_remaining < min_cert_days:
            raise RuntimeError(
                f"TLS certificate for {hostname} expires in {days_remaining} days, below threshold {min_cert_days}"
            )
        lines.append(f"TLS OK: {hostname} expires {expires_at.date().isoformat()} ({days_remaining} days left)")

        unauthenticated = _fetch_url(url, timeout=timeout)
        _require_unauthenticated_protection(unauthenticated, url)
        lines.append(f"Auth gate OK: {url} returned 401 with Basic challenge")

        authenticated = _fetch_url(url, timeout=timeout, authorization=authorization)
        _require_authenticated_access(authenticated, url, body_token)
        lines.append(f"App OK: {url} returned 200 after Basic auth")

    return lines


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check CoderLAP public health behind Cloudflare and Basic auth.")
    parser.add_argument("--base-url", default="https://coderlap.com")
    parser.add_argument("--www-url", default="https://www.coderlap.com")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--min-cert-days", type=int, default=DEFAULT_MIN_CERT_DAYS)
    parser.add_argument("--body-token", default=DEFAULT_BODY_TOKEN)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    username = os.environ.get("CODERLAP_BASIC_AUTH_USER", "").strip()
    password = os.environ.get("CODERLAP_BASIC_AUTH_PASSWORD", "").strip()
    if not username or not password:
        raise RuntimeError("CODERLAP_BASIC_AUTH_USER and CODERLAP_BASIC_AUTH_PASSWORD must be set")

    urls = [args.base_url]
    if args.www_url and args.www_url != args.base_url:
        urls.append(args.www_url)

    lines = run_checks(
        urls=urls,
        username=username,
        password=password,
        timeout=args.timeout,
        min_cert_days=args.min_cert_days,
        body_token=args.body_token,
    )

    for line in lines:
        print(line)
    _write_summary(lines)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
