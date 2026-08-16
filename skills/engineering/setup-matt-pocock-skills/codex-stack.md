# Codex Stack

Use this when the repo will be operated by Codex or by agents following an `AGENTS.md` policy contract.

## Policy entrypoint

- Prefer `AGENTS.md` as the repo loading contract.
- If both `AGENTS.md` and `CLAUDE.md` exist, update `AGENTS.md` for Codex behavior and preserve `CLAUDE.md` unless the user explicitly asks to change it.
- If `docs/dev/policies/` exists, reference those files from the Agent skills block instead of duplicating policy text into `docs/agents/`.
- Treat `docs/dev/policies/` as durable repo-local policy and `docs/agents/` as configuration for these skills.

## Code discovery

- Use CodeGraph or codebase-memory MCP for structural questions when the repo advertises those tools.
- Use `rg` for literal strings, config values, scripts, docs, logs, or when MCP tools are unavailable.
- If an advertised graph tool is not available in the current session, proceed with direct repo inspection and record the fallback when it affects confidence.

## Runtime truth surfaces

- For Codex MCP wiring, prefer live checks such as `~/.codex/config.toml`, `codex mcp list`, and `codex mcp get <name>`.
- For user-scoped services, tenant runtimes, Slack/OpenClaw bindings, browser routes, or generated artifacts, verify the actual runtime/config/artifact path before claiming completion.
- If runtime evidence disagrees with stale docs or manifests, prefer runtime evidence and report the mismatch.

## Artifact review

- Remote shell is common on this workstation; do not assume `xdg-open`, `open`, or OS desktop launching will show the user the artifact.
- When a generated artifact needs browser review and the `previews` skill/service is available, publish one preview session and return the session URL.
- Prefer Previews for HTML reports, rendered docs, PDFs, Office documents, image galleries, UI prototype review surfaces, approval packets, and artifact families.
- Use local paths or `xdg-open` only when Previews is unavailable or the user explicitly asks for a local desktop-open path.

## Commit behavior

- Do not commit automatically unless the user explicitly asks for a commit.
- If another skill says to commit by default, treat that as overridden by this Codex stack rule.
