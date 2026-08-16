# Policy | Upstream Fork Maintenance

## Policy

- Keep the public upstream on a distinct `upstream` remote and reserve `origin`
  for an owned fork if one is configured later.
- Keep local `main` as a clean mirror of `upstream/main`.
- Carry repo-local policy, Codex adaptations, and curated skill exposure on the
  rebase-managed `eco/main` branch.
- Before a substantive upstream rebase, create a dated `backup/eco-main/*` ref
  at the prior carry tip.
- Rebase `eco/main` onto a freshly fetched `upstream/main` when the local delta
  remains small and reviewable.
- Do not force-push or otherwise publish rewritten history unless the exact
  destination is confirmed to be owned, private, and rebase-managed.
- Record recurrent semantic conflicts and intentionally retained divergences in
  a dated repo note so later rebases do not rediscover them from scratch.
- Keep downstream installation and user-scope publication separate from source
  release, tagging, and remote push.

## Adoption Notes

This repository is a local downstream of `mattpocock/skills`. The stable local
delta is policy governance, Codex/workstation discovery and runtime proof,
repo-native planning, preview-based artifact review, and a curated promoted
skill set that excludes auto-commit behavior.
