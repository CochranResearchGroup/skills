# Codex Code Discovery

Use this reference when exploring code in a Codex-operated repo.

## Structural questions

Prefer CodeGraph or codebase-memory MCP tools for:

- symbol definitions and signatures
- callers and callees
- impact analysis
- flow traces
- architecture context
- file inventory inside indexed code areas

Do not rebuild a graph manually with broad grep when a graph tool can answer the structural question directly.

## Literal and non-code searches

Use `rg` or direct file reads for:

- string literals
- comments and docs
- config values
- log messages
- shell scripts and Dockerfiles
- generated artifacts
- cases where graph tools are missing, stale, or not initialized

## Freshness

After editing files, assume graph indexes may lag. Use direct source reads and validation for the files just changed.

## Fallback

If a repo advertises CodeGraph or codebase-memory MCP but the tools are not exposed in the current turn, keep working with normal repo inspection. State the fallback in handoff or closeout only when it materially affects confidence.
