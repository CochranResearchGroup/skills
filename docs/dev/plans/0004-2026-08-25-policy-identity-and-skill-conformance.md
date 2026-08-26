# Plan 0004 | Policy Identity And Skill Conformance

Status: CLOSED

## Current State

Implementation is committed on `eco/main` at `29dbd06`. Seven duplicate module
identities have been reconciled to one retained path apiece, the inapplicable
roadmap/runbook module and its exception baseline are retired, and promoted
skill contracts now match the adopted evaluator, retry, testing, and Git safety
rules. Validation is complete; only this closeout record remains to commit.

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

Publish or push only under separate authority. A future policy release may
carry the shared duplicate-identity guard; no release or installation occurred
in this plan.

## Checkpoint 1 | Identity Reconciliation

Progress classification: outcome progress.

- Shared selector enforcement landed locally in `agent-policies` commit
  `c375eee` before downstream reconciliation began.
- Mapocock commit `29dbd06` removed seven superseded policy generations and
  retained one wired file per adopted identity.
- Roadmap/runbook governance was retired because its documented prerequisites
  are absent; no synthetic authority files were created.

## Checkpoint 2 | Skill Contract Repair

Progress classification: outcome progress.

- Promoted review, conflict-resolution, research, diagnosis, and TDD guidance
  now preserve primary adjudication, conditional delegation, bounded retries,
  safe abort/restart, semantic rebase validation, and stable regression seams.
- Deterministic publication checks now reject the superseded unsafe phrases and
  prevent promotion of `implement`, `implement-spec`, and `retro`.

## Checkpoint 3 | Acceptance And Custody

Progress classification: outcome evidence.

- Policy identity audit: zero duplicates and no validation problems. The sole
  source-selector recommendation is the intentionally inapplicable
  `roadmap-runbook-governance` companion module.
- Active-plan and goal-contract audits passed after retiring that module and
  its exact legacy baseline.
- Plugin version sync, strict plugin validation, 37 skill-frontmatter parses,
  relative links across 65 Markdown files, and the 24-skill user-scope
  publication check all passed without publication.
- The first frontmatter-check attempt could not import optional Python package
  `yaml`; the check was rerun with Ruby's standard YAML parser and passed. This
  was a validator-environment issue, not a product-test retry.
- Local branch `eco/main` is two commits ahead of owned
  `origin/eco/main` (`4c3e166`, `29dbd06`) and 19 commits ahead of tracked
  public `upstream/main`. Nothing was pushed, published, installed, or rebased.
