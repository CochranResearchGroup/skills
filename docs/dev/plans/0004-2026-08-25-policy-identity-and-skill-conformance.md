# Plan 0004 | Policy Identity And Skill Conformance

Status: OPEN

## Current State

The repository is clean on `eco/main` at `4d5e03c`. Its `v0.1.20` policy
adoption wires seven duplicate module identities: four byte-identical pairs and
three pairs where an older generation coexists with the current policy. The
promoted `code-review` and `resolving-merge-conflicts` skills also contain
instructions that conflict with the adopted evaluator and Git safety contract.

## Scope

- Reconcile each duplicate identity to one canonical retained policy path.
- Retire roadmap/runbook governance and its exact legacy baseline because this
  lightweight skill repo has neither authority surface and the module's stated
  prerequisites are not met.
- Preserve any unique repo-local semantics before removing superseded files.
- Repair `AGENTS.md` so it wires each retained policy exactly once.
- Keep Standards and Spec review separate while making findings candidates for
  primary adjudication and respecting runtime delegation constraints.
- Replace mandatory conflict completion with intent-based resolution plus a
  safe abort/restart path when evidence or recovery safety is insufficient.
- Keep `implement`, `implement-spec`, and `retro` unpromoted.

## Non-Goals

- Do not rebase, push, publish, install user-scoped skills, change plugin
  membership, or modify unrelated upstream skill behavior.
- Do not silently select a divergent duplicate or delete unique local policy.

## Acceptance Criteria

- Exactly one policy file and one `AGENTS.md` entry remain per module identity.
- Retained policy content includes all still-applicable unique local clauses.
- Promoted review and conflict-resolution skills conform to adopted policy.
- Plugin, policy, frontmatter, documentation-link, and curated-publication
  checks pass without publication.
- The final worktree is clean at a local committed checkpoint with exact
  branch, upstream, and publication disposition recorded.

## Definition Of Done

Policy identity and promoted-skill semantics are deterministic, validated, and
recoverable without changing remote or user-scope state.

## Next Action

Wait for the shared selector enforcement checkpoint, then reconcile duplicates
and skill text against that source contract.
