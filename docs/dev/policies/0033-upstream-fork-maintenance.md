# Policy | Upstream Fork Maintenance

## Policy

- Keep the public upstream on a distinct `upstream` remote and reserve `origin`
  for an owned fork if one is configured later.
- Keep local `main` as a clean mirror of `upstream/main`.
- Carry repo-local policy, Codex adaptations, and curated skill exposure on the
  rebase-managed `eco/main` branch.
- Before a substantive upstream rebase, create a dated `backup/eco-main/*` ref
  at the prior carry tip.
- Freeze the downstream semantic invariants that must survive, including the
  curated promoted set, excluded automatic-commit behavior, Codex routing,
  runtime proof, and publication boundaries.
- Rebase `eco/main` onto a freshly fetched `upstream/main` when the local delta
  remains small and reviewable.
- Do not force-push or otherwise publish rewritten history unless the exact
  destination is confirmed to be owned, private, and rebase-managed.
- Record recurrent semantic conflicts and intentionally retained divergences in
  a dated repo note so later rebases do not rediscover them from scratch.
- Resolve conflicts from both sides' primary-source intent. A favor option or a
  conflict-free rebase is textual evidence, not proof that downstream semantics
  survived.
- Verify the frozen invariants separately from syntax, manifest, and test-runner
  checks. If semantic verification fails, rebuild from the preserved tip and
  old/new upstream inputs or abort and restart from the recovery ref.
- Do not make completion mandatory when intent or recovery safety is uncertain.
- Keep source presence, promoted membership, user-scope installation, source
  release, remote push, and publication as separate proof boundaries.
- Keep downstream installation and user-scope publication separate from source
  release, tagging, and remote push.
- Use a distinct upstream remote when the repo carries private or local features on top of a non-owned active upstream.
- Keep private feature work isolated from the branch used to mirror or track upstream state.
- Rebase private branches onto fresh upstream state when the goal is to keep a small, understandable delta over an active upstream.
- Prefer force-push only on branches that are explicitly private, unshared, or documented as rebase-managed.
- Do not rewrite shared branch history casually when other collaborators, CI systems, or deployments may already depend on it.
- Keep one branch or tag that records the last known clean upstream sync point before heavy private divergence.
- Before rewriting a downstream carry, preserve its exact prior tip and freeze
  the downstream semantic invariants that must survive, such as excluded
  features, promotion membership, authority boundaries, runtime behavior, or
  publication scope.
- Record conflict-prone patches, local carry patches, or intentionally retained divergences somewhere durable when they are likely to recur across rebases.
- Resolve conflicts from each side's intent and primary sources. A favor option
  or conflict-free operation is only a textual result; it is not proof that the
  downstream semantics survived.
- After the operation, verify the frozen downstream invariants independently of
  syntax, manifest, and test-runner checks. When semantic verification fails,
  rebuild from the preserved tip and old/new upstream inputs or abort and
  restart from the recovery point.
- Do not make merge or rebase completion mandatory. Abort or restart is the
  safe disposition when intent is unavailable, the recovery point is
  uncertain, or the proposed resolution cannot be validated without inventing
  behavior.
- Keep source presence, promoted or enabled membership, local installation,
  release publication, and remote publication as separate proof boundaries.
- Be explicit about whether downstream release tags are cut from rebased private branches, merge-based integration branches, or snapshots after upstream sync.
- If a private feature is becoming long-lived and hard to rebase, reconsider whether it should remain a fork-local patch set or become a maintained downstream branch line.

## Adoption Notes

This repository is a local downstream of `mattpocock/skills`. The stable local
delta is policy governance, Codex/workstation discovery and runtime proof,
repo-native planning, preview-based artifact review, and a curated promoted
skill set that excludes auto-commit behavior.
