# Plan 0003 | Upstream Rebase

Status: CLOSED

## Current State

Local `main` and `upstream/main` both resolve to
`6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`. The complete downstream carry is
rebased onto that tip, with the source reconciliation committed at `11c362c`.
The prior v0.1.20 carry tip remains recoverable at
`backup/eco-main/2026-08-25-pre-rebase` (`7cc86a8`). The final validation and
conflict decisions are recorded in
`docs/dev/notes/0004-2026-08-25-upstream-rebase.md`.

## Scope

- Preserve the pre-rebase `eco/main` tip under a dated backup ref.
- Rebase the complete downstream carry onto the fetched `upstream/main` tip.
- Reconcile conflicts semantically, retaining repo-local policy, Codex
  discovery, repo-native planning, runtime-proof, durable-handoff, preview,
  and curated-publication behavior while accepting upstream skill fixes and
  additions.
- Keep `implement`, `implement-spec`, and `retro` in source according to their
  upstream buckets while preventing unintended promotion or user-scope
  publication.
- Validate repository, plugin, policy, documentation, and curated Codex
  publication contracts without pushing or publishing.

## Non-Goals

- Do not push rewritten history, publish user-scope skills, tag a release, or
  publish a GitHub or plugin release.
- Do not adopt unmerged upstream topic branches or the generated changeset
  release branch.
- Do not alter unrelated user-scoped installations or runtime state.

## Execution

The critical path is serialized: create the safety ref, rebase all carry
commits, resolve each conflict against its originating upstream and downstream
intent, then validate the resulting tip. Independent validation commands may
run in parallel only after the rebase finishes and the worktree is coherent.

## Acceptance Criteria

- `backup/eco-main/2026-08-25-pre-rebase` preserves the exact pre-rebase tip
  `7cc86a833fb2d70d4fb4def1a4193dd956102902`.
- `upstream/main` and local `main` remain identical at `6654f6b`.
- `eco/main` has `upstream/main` as an ancestor and is zero commits behind it.
- All fourteen downstream commits are represented in the rebased history with
  their intended policy and Codex/workstation behavior preserved.
- Upstream `wait-what`, YAML-frontmatter, grilling, `implement-spec`, and
  `retro` changes are present without widening the curated promoted set.
- Plugin version, policy planning audits, selector tests, documentation links,
  and `scripts/publish-codex-skills.sh --check` pass.
- The final worktree is clean and no remote write or user-scope publication
  occurs.

## Definition Of Done

The recovery ref and rebased clean branch are inspectable, all required checks
pass against the final commit, a dated receipt records conflict decisions and
validation evidence, and this plan is `CLOSED`.
