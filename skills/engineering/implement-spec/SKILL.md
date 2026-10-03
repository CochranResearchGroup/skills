---
name: implement-spec
description: "Implement a spec and dependent tickets on one validated integration branch, using bounded parallel workers when useful."
disable-model-invocation: true
---

# Implement Spec

Explicit invocation authorizes coordinating the supplied spec within the user's scope. Deliver one validated integration branch. Follow repository policy for commits, remote publication, tracker changes and live effects; invocation does not expand that authority.

## Establish the packet

Read the spec, tickets, repository instructions and configured planning/tracker authority. Accept repo-native tickets; do not require an online tracker. Identify acceptance criteria, non-goals, blockers, expected write scopes, shared contracts and validation environments. Reject missing blocker IDs and cycles before dispatch. Infer routine details from authoritative sources; ask only for material missing decisions.

Inspect checkout status and registered worktrees. Reuse the correct integration checkout when safe, otherwise create an isolated branch from a recorded base SHA. Preserve unrelated dirty work. Never reset another checkout to manufacture the expected base.

Keep a resumable ledger in the repo's approved planning surface. Record the spec locator, integration branch/base/tip, ticket dependencies and states, worker handle, owned paths, worker branch/worktree/base/result SHA, validation commands/results and accepted findings. States: pending, running, implemented, integrated, validated, blocked. Tracker closure is separate.

## Execute the graph

The coordinator owns scheduling and integration. A ticket is ready only when every blocker is validated on the integration branch. Compute readiness from the ledger and current Git evidence, not tracker closure or worker claims.

Delegate bounded tickets when permitted and useful; otherwise execute sequentially. Respect available slots and repo concurrency limits. Use shallow workers, compact source pointers and explicit ownership. Serialize overlapping write scopes and give each shared contract one owner. Optional discovery must add evidence rather than repeat structural graph exploration.

Each worker receives its ticket, frozen acceptance, non-goals, base SHA, owned paths, shared contracts and validation requirements. Work in a separate owned worktree/branch. Use the available tdd skill for substantive behavior where appropriate and existing validation for documentation or low-impact edits. Return runtime status, result SHA, changed paths and acceptance evidence; failed, timed-out or unknown runs remain incomplete.

Integrate serially. Verify scope, current base and worker evidence before landing. Reconcile divergence by intent using the available conflict-resolution skill; do not assume a worker's earlier sync guarantees a fast-forward. Validate the resulting integration tip before marking the ticket validated and unlocking dependents. A skipped required test is missing evidence, not success. Provision authorized fixtures or run verification in a suitable isolated environment; do not borrow private data or disturb unrelated dirty work.

## Review and recover

Once all tickets are validated, review the whole integration branch against the frozen spec and repository standards using the available code-review skill. Adjudicate candidate findings as blocking, backlog, rejected or needs-evidence. Run at most one broad review and one bounded remediation pass, followed by focused verification of accepted blockers and critical regressions. Honor stricter existing goal bounds. If blockers remain, report the affected unit and evidence gap; do not restart broad review loops or silently expand scope.

On interruption, re-read the ledger, runtime status, Git tips and validation receipts. Reconcile ambiguous worker outcomes before retrying. Reuse valid integrated work; changed shared contracts invalidate only causally affected evidence. Preserve blocked branches and useful receipts.

## Close out

Report implemented, integrated, validated and tracker-resolved states separately, with exact branch/tip and remaining gates. Create or update PRs and close tickets only within existing authorization and the tracker's acceptance rules; PR readiness does not prove merge or deployment. Local execution can end at the validated branch.

Remove owned worker worktrees only after clean-state, exact commit and durable custody checks required by repo policy. Keep unresolved work recoverable. Do not auto-commit, force-push, deploy or delete branches merely to finish the workflow.
