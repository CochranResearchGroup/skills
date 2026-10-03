# Adopt Implement Spec

- State: CLOSED
- Owner: primary agent
- Scope: adapt and promote implement-spec; install both local skill roots
- Non-goals: upstream rebase, other skill adoption, remote publication

## Current State

Adapted source, metadata, manifest, publisher and routing are validated and installed.

## Acceptance

Scheduling requires validated blockers, safe worktree custody, explicit ownership, resumable evidence and bounded adjudicated review. Publisher rejects missing semantic contracts. Both local roots must resolve the promoted skill to the same source. Definition of done: source checks, publisher validation and exact installed readback recorded. Behavioral execution is a separate unrun acceptance boundary.

## Validation And Deployment Receipt

Plugin version synchronization and shell syntax pass. All 25 promoted skill frontmatter and Codex metadata blocks parse with PyYAML. Workflow contract checks pass. Both publisher runs verify 25 installed links; ~/.codex/skills also resolves implement-spec to the promoted source. Initial system Python lacked PyYAML; validation succeeded through uv with pyyaml.

No end-to-end worker trial was run; static contract checks do not establish runtime scheduling correctness. Adoption and local installation are complete; behavioral trial remains a follow-up. No upstream rebase or remote push occurred.
