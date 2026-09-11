# Local Semgrep audit

Date: `2026-09-11`. Baseline: `4c0436bcce15e0cde9db355a1ee7ec9fae8645ae`.
CLI: Semgrep `1.172.0`, OSS engine, native Windows.

## Scope and results

Scanned the working tree with `p/security-audit`, `p/python`, `p/javascript`
and `p/github-actions`, then separately with `p/secrets`. Metrics and version
checks were disabled. Rules were downloaded from the registry; these local
commands did not publish findings to the Semgrep platform.

| Scan | Scanned paths | Findings | Scanner errors |
| --- | ---: | ---: | ---: |
| Initial code audit | 556 | 16 warnings | 8 |
| Code audit after helper fix, excluding three Pro-only rules | 556 | 16 warnings | 2 |
| Secret patterns | 556 | 0 | 0 |

This is not a clean, exhaustive security verdict. Semgrep's default exclusions
omit tests, vendored code and ignored generated output. Dependency vulnerability
scanning, Git history, live server settings and cloud CI configuration were not
covered. Raw reports stay outside the repository because they may contain source
snippets or sensitive values.

## Findings reviewed

- **5 template URL warnings:** `base.html`, `module_pack.html` and `topic.html`
  use generated local navigation URLs. Language roots are configured internally;
  topic path segments are validated by the loader. No visitor-controlled URL
  reaches these template attributes.
- **5 script-tag warnings:** JSON data in `home.html`, `module_pack.html` and
  `topic.html` uses Jinja `tojson` inside `application/json` elements. A manual
  closing-script payload check confirmed HTML escaping and JSON round-trip.
- **3 `safe` warnings:** legal, topic and pack HTML comes through the Markdown
  renderer and allowlist sanitizer before the template's `safe` filter. Existing
  tests cover raw scripts, unsafe URLs and malformed HTML. Keep that boundary.
- **3 dynamic urllib warnings:** the health-check URL is operator-supplied CLI
  input; font downloads run only in the optional developer helper. These are not
  visitor-facing request endpoints. Manual inspection found that the font URL
  regex also accepted hostname suffixes and userinfo spoofing. The fix requires
  `/` immediately after `fonts.gstatic.com`; a regression test covers misleading
  hosts and unsupported schemes. Redirect handling was not changed.

The audit found no confirmed exploitable runtime vulnerability in these paths.
The 16 audit warnings remain visible; none were globally suppressed.

## Scanner limitations and repeat commands

Three registry rules require Pro-only module matching. They generated six errors
across the two JavaScript files; the repeat run excluded only those rules:

```powershell
semgrep scan --config p/security-audit --config p/python --config p/javascript --config p/github-actions --exclude-rule javascript.crypto-js.cryptojs-weak-algorithm.cryptojs-weak-algorithm --exclude-rule javascript.express.web.cors-default-config-express.cors-default-config-express --exclude-rule javascript.koa.web.cors-default-config-koa.cors-default-config-koa --metrics off --disable-version-check --json-output "$env:TEMP/coderlap-semgrep-code.json" --quiet .
semgrep scan --config p/secrets --metrics off --disable-version-check --json-output "$env:TEMP/coderlap-semgrep-secrets.json" --quiet .
```

These commands default to OSS on the tested installation. The registry packs
can change, so later results may differ even with the same CLI version. Keep
console output local too; it may include matched source.

Two partial-parsing errors remain for the `curl-eval` and `gha-curl-pipe-shell`
rules at `.github/workflows/coderlap-static-cicd.yml:114`. Manual inspection found
a GitHub `${{ github.sha }}` expression in a build-summary echo, not a shell
download/execution pipeline. The valid workflow was not changed to satisfy the
scanner. Recheck these coverage gaps when upgrading Semgrep or its rules.

Validation: all 81 Python tests and 8 JavaScript interaction tests passed, and
the bilingual static build succeeded. Both CSS-referenced WOFF2 files returned
HTTP 200 from a temporary local server with valid WOFF2 headers. Both font
licenses were copied byte-for-byte into `dist/`; font loading already used local
files.
Cloud Semgrep CI remains a separate follow-up: preserve the prepared workflow
in the original working copy and review its token and upload settings before
enabling it.


## Workshop release repeat — 2026-09-11

The assembled release tree (maintenance commit `19cef04`, tree identical to
`e289105` on dev) was scanned locally with the commands above. No cloud
workflow was included; raw reports remain in the local temporary directory.

- Code audit: 570 scanned paths, 20 audit warnings, 2 partial-parsing errors.
- Secret-pattern scan: 570 scanned paths, 0 findings, 0 errors.
- The four additional warnings are one generated footer home URL and three in
  the newly integrated, manual-only design prototype: two generated local URLs
  and the trusted repository lesson HTML passed to `safe`. The prototype
  renderer has no sanitizer and must not accept untrusted Markdown. The normal
  production build excludes these preview pages; its sanitizer is unchanged.
- The previous 16 warning paths retain the same trust boundaries described
  above. The workflow parser gaps moved to line 117, still the commit-summary
  echo containing a GitHub expression.
- 83 Python tests, 35 JavaScript tests and the bilingual build passed. The
  main-only deploy condition and YAML parsing were checked separately.

No warning was globally suppressed. These results are an audit with the noted
coverage gaps, not an exhaustive clean-security claim.
