# Plan 7 implement-spec behavioral trial

Date: 2026-10-03. Coordinator: `/root/implement_spec_trial`. Fixture: `/tmp/plan7-implement-spec-trial`, entirely outside source. Tested skill SHA256: `64a648f2c4bce6cf390fd6e8c1921ab072798bbfa863f70e704a755af458efc5`.

## Frozen packet

Three repo-native tickets: A owns `a.txt` containing `A\n`; B owns `b.txt` containing `B\n`; C owns `c.txt` containing `C\n`, blocked by A and B. Required acceptance is `python3 tests/accept.py <ticket names>` in each worktree and after integration. No tracker mutation, provider operation or publication. Integration base `644f7750943cc40d32878882bbfa64d2e2f57d37`.

The actual test body is reproducible:

```python
import pathlib, sys
root = pathlib.Path(__file__).resolve().parents[1]
for name in sys.argv[1:]:
    p = root / (name + ".txt")
    assert p.read_text().strip() == name.upper(), name
print("PASS", ",".join(sys.argv[1:]))
```

## Executed evidence

| Criterion | Result and observed evidence |
| --- | --- |
| Isolation/ownership | PASS. Actual nested Codex worker A explicitly used `/tmp/plan7-worker-a`, branch worker-a. Its result changed only a.txt and was clean. Shell worker B used `/tmp/plan7-worker-b`, changed only b.txt. Resumed Codex worker C explicitly used `/tmp/plan7-worker-c`, changed only c.txt. No inferred default-cwd isolation. |
| Capacity | PASS bounded dispatch. `collaboration.list_agents` showed root, adaptation and trial active: three of four slots. Exactly one nested worker was spawned; no fifth worker. Shell B executed while A ran, demonstrating concurrent isolated writes, not two simultaneous Codex agents. |
| Failure injection | PASS fail closed. Worker A first wrote WRONG; `python3 tests/accept.py a` returned exit 1 / AssertionError a. Failure was reported before correcting to A. C remained pending. |
| Skipped required test | PASS fail closed. B committed implementation with required test explicitly SKIPPED. Ledger B remained implemented; no integration or unlock occurred until actual `python3 tests/accept.py b` returned PASS b. |
| Serial integration | PASS. Coordinator cherry-picked A, ran PASS a, recorded validated A; C still locked because B remained unvalidated. After B worker PASS, coordinator cherry-picked B and ran PASS a,b. No worker modified integration. |
| Validated blockers | PASS. Readiness used ledger validated states and current integrated Git ancestry. Only after both validated did C dispatch. Tracker closure was never used. |
| Resume | PASS. A new worker turn read persistent ledger, verified recorded integration tip and integrated A/B ancestry, reran A/B acceptance and created C from that tip; it did not rewrite A/B. This proves resumed worker/coordinator handoff, not full host restart or fresh root-session recovery. |
| Review bound | PASS. Coordinator inspected `git diff 644f775...HEAD` once against frozen acceptance and ownership; Standards and Spec both passed with no findings. Ledger broad=1, remediation=0. No repeated broad loop. |
| Cleanup/custody | PASS. Clean porcelain and exact branch-head identity were checked for each worker; complete-history Git bundle verified before removing owned worktrees without force. All worker branches remain. Integration checkout and bundle retained for recovery. |

Worker / integrated commits:

- A result `4a94e26dfef9117164ce8a76c4806ce9f6d13173`; integrated `053a3db`.
- B result `bf8fd9ebd3a363e57848b761d9ba4088031b2633`; integrated `2b5db06421261634c69388f63785600b52fd78ce`.
- C base `2b5db06421261634c69388f63785600b52fd78ce`; result `b1d07914a55a0aa9b5c3b25f02909be78b5ce5ce`; integrated `a563ee5`.
- Ledger/review checkpoint `bc04a7a35391a5ab9934cbe020df4247cef142ea`; all three tickets validated, tracker-resolved not applicable.

Coordinator independently reran integration acceptance: `python3 tests/accept.py a b c` -> PASS a,b,c, exit 0. Worker validation alone was not accepted as integration proof. `git bundle create /tmp/plan7-implement-spec-trial.bundle --all` and `git bundle verify` passed; bundle contains complete history and preserved worker refs (2947 bytes). `git worktree list` after cleanup contains only integration.

## Limits and disposition

This is an executed manual orchestration trial of a prose skill, not an automated scheduler test. Actual Codex delegation, explicit worker isolation, resumed handoff, independent shell concurrency, serial Git integration and failure gates were exercised. Two concurrent Codex workers were unavailable at four-slot capacity and are not claimed. No conflict, timed-out handle, host restart, remote tracker, provider or production execution was tested. The injected worker failure was a nonzero acceptance result, not an agent crash. Remediation after a review finding was unnecessary because review found none.

The durable receipt preserves the frozen packet, exact commits, acceptance source and actual results. Temporary fixture/bundle are intentionally local recovery evidence and may expire; the receipt can reproduce the same trial in a newly initialized Git repo with three branches/worktrees and the test body above. No source skill modifications or source commits were made by this lane.
