# Plan 0002 | Upstream Rebase And Codex User-Scope Publication

Status: OPEN

## Current State

The local tailoring packet is committed at `88dcfe0`. The local branch is nine
commits ahead of and 295 commits behind upstream `main` at
`068b6e0c62393147daf03530149cdce209c93da8`. The active Codex user-scoped skill
directory is `/home/ecochran76/.agents/skills`.

## Scope

- Preserve the public upstream as a clean tracking line.
- Rebase the local policy and Codex/workstation overlay onto upstream `main`.
- Reconcile upstream skill renames, additions, invocation semantics, Codex
  metadata, and the local repo-native planning/runtime/preview adaptations.
- Keep `implement` out of the promoted and installed set while it still commits
  automatically.
- Publish the reconciled promoted skills to Codex user scope.

## Non-Goals

- Do not push, tag, or publish a GitHub release.
- Do not install deprecated, personal, or unfinished draft skills.
- Do not overwrite unrelated user-scoped skills.

## Acceptance Criteria

- A safety ref preserves the pre-rebase local history.
- Local `main` mirrors the fetched upstream `main`, and the local carry branch
  is rebased onto that exact upstream commit.
- Repo-local policy, plans, notes, and the selector bundle remain present.
- Promoted skills use upstream current behavior plus the retained local Codex
  overlay; `to-spec` and `to-tickets` replace `to-prd` and `to-issues`.
- `implement` is absent from the promoted manifest and Codex user-scope links.
- Repository policy audits, metadata checks, link checks, and relevant package
  validation pass.
- Every promoted skill is available under `/home/ecochran76/.agents/skills`
  and resolves to the rebased source checkout.

## Definition Of Done

The rebased carry branch is clean, validation is green, the upstream mirror and
safety ref are inspectable, and the Codex user-scope skill links resolve to the
validated promoted skill set.
