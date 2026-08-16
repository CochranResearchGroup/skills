# Preview Artifact Policy Update | 2026-06-24

## Decision

Adopted `preview-artifact-review` as a local policy override because this repo is usually operated over remote shell and `xdg-open` is not a reliable review path.

## Changed

- Added `docs/dev/policies/0021-preview-artifact-review.md`.
- Wired the policy into `AGENTS.md`.
- Updated Codex stack guidance to prefer `previews` for human-review artifacts when available.
- Updated architecture-review and UI-prototype skills to use Previews for browser review before falling back to local paths or `xdg-open`.

## Rationale

Generated reports and UI review surfaces should reach the user as browser URLs, not as local desktop-open attempts that fail or open on the wrong machine.
