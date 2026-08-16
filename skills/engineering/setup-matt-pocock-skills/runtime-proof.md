# Runtime Proof

Use this reference when a task touches live runtime behavior, local services, MCP wiring, tenant state, Slack/OpenClaw routing, browser automation, or generated evidence artifacts.

## Proof standard

- Prefer a tight pass/fail command or artifact check over prose confidence.
- Verify the surface that actually matters to the user, not only a nearby unit.
- Record the exact command, artifact path, or live check used as evidence.

## Common truth surfaces

- Codex MCP: `~/.codex/config.toml`, `codex mcp list`, `codex mcp get <name>`, and a direct stdio/API smoke when available.
- User services: process manager status, socket/path existence, logs, and direct CLI/API smoke.
- Slack/OpenClaw: resolved account, channel ID, bot membership, tenant binding files, and generated/send artifacts.
- Tenant state: tenant-root files, SQLite rows, actions logs, artifacts, and redacted runtime config.
- Browser/UI: dev server output, Playwright/browser screenshots, console/network evidence, or route-readiness checks.

## Mismatches

If docs, manifests, or plan text disagree with runtime evidence, prefer runtime evidence and report the mismatch explicitly.

## Privilege blockers

If a non-interactive privilege check already failed, stop retrying privileged operations and report the blocker with the exact command/result.
