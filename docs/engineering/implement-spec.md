# Implement Spec

Explicitly invoke `/implement-spec` with a spec and its ticket locators. The coordinator schedules tickets from validated blocker evidence, assigns disjoint write scopes, serially integrates completed work and validates the integration tip before unlocking dependents.

The adapted skill supports repo-native tickets, bounded parallel workers and sequential execution. Its resumable ledger records branch/commit identity, ownership, worker status and validation evidence. It does not require a PR or online tracker.

One broad final review is followed by adjudicated findings, bounded remediation and focused verification. Skipped required tests remain missing evidence. Tracker closure, remote publication and deployment follow existing authorization. Cleanup preserves dirty or unresolved work and requires durable commit custody.

Source: [skill](../../skills/engineering/implement-spec/SKILL.md). Adapted from upstream `d81f3a1`; this adoption does not integrate the remaining upstream upgrade.
