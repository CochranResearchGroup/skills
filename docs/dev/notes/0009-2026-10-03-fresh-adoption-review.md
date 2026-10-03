# Fresh-context adoption review

Date: 2026-10-03. Evaluator: `/root/fresh_adoption_review`. Scope: Plan 7 bounded behavioral acceptance, using actual file-invoked pr, retro, domain-modeling and implement-spec skills in the candidate checkout. Also loaded writing-for-agents as retro requires. No source changes, installation, public PR creation or tracker mutations were performed. Coordinator owns publication of this report with the acceptance packet in Previews.

## PR output: trivial validation fix

Use a dependency-declared runner for skill metadata validation so the check works when system Python lacks PyYAML.

Validation: the initial system-Python check failed with `ModuleNotFoundError: No module named yaml`; the bounded retry through `uv run --with pyyaml python` passed the pr and retro metadata/contracts (receipt 0008). Independently observed `git diff --check` exit 0 in the candidate checkout. This is validation environment evidence; it does not prove fresh installed skill discovery.

Result: PASS. Concrete trigger and resulting behavior, concise prose, real evidence, no forced diagram or risk taxonomy. No repository PR template was found in the bounded repository file search. This is an authored body for the supplied small validation-change scenario, not a claim that a separate code fix or PR was created.

## Retro output: reviewed run only

Reviewed evidence: receipts 0007/0008, current package scripts and release workflow, and actual logs `/tmp/mapocock-plan7-selector-tests.log` and `/tmp/mapocock-plan7-selector-harness.log`. Full parent transcript was not supplied. Findings are recommendations; no environment or global instruction changes are authorized by this review.

1. Low severity: dependency assumptions caused an avoidable metadata-check failure. Receipt 0008 records system Python missing PyYAML and uv resolving the dependency successfully. Prefer the existing dependency-declared runner for metadata checks. Verification: repeat the check in a clean Python environment with that runner. Maintenance cost: small, an explicit dependency declaration rather than another prose policy.
2. Low severity: the bundled selector suite assumes the agent-policies source layout, which differs from the installed skill layout. The direct log records 124 tests, 10 errors, including missing `.codex/skills/modules/git-worktree-hygiene.md`; the synthetic harness log records the same 124 tests passing in 35.760 seconds. The coordinator reports the harness links modules/profiles/catalog.yaml to actual agent-policies source. Prefer a named harness entry point with explicit source roots and identity checks. Verification: the wrong layout should give a clear prerequisite error; the declared harness should run the full suite against actual source. Maintenance cost: one harness path, preserving the suite instead of duplicating it. Passing the harness does not erase the direct failure.
3. Low severity, nonblocking backlog: current package scripts provide `check-plugin-version`, but the inspected release workflow runs install/version publication and does not execute that check or the source acceptance checks. A scoped deterministic CI validation entry would catch metadata/version drift before publication. Verification: inject a plugin version mismatch and confirm the check fails. Broader CI work remains outside this adoption review; no new implementation requirement is imposed.

No findings for unavailable logs, expensive calls, or global instructions: evidence does not justify them. Result: PASS source-backed recommendations, deterministic improvements, bounded interval, no unrelated edits.

## Domain-authority decisions

| Supplied scenario | Selected authority | Result |
| --- | --- | --- |
| Only legacy CONTEXT.md, no configured authority/map | CONTEXT.md; read/update existing terms, create no second glossary | PASS |
| Only GLOSSARY.md, no configured authority/map | GLOSSARY.md | PASS |
| Configured docs/vocabulary.md and both conventions | docs/vocabulary.md; configuration wins | PASS |
| Both conventions disagree without configuration | Unresolved until routing/intent reconciliation; preserve both | PASS |

These are actual fresh-worker applications of the file instructions to supplied scenarios, not disk fixtures or modifications to another repository.

## Independent fixture verification

Executed in `/tmp/plan7-implement-spec-trial`:

- `python3 tests/accept.py a b c` returned `PASS a,b,c`, exit 0.
- `git bundle verify /tmp/plan7-implement-spec-trial.bundle` returned exit 0, complete history, integration `bc04a7a35391a5ab9934cbe020df4247cef142ea` plus preserved worker-a/b/c refs.
- Read ledger: all tickets validated; C blocked on A/B, result `b1d07914a55a0aa9b5c3b25f02909be78b5ce5ce`; broad review 1, remediation 0.

PASS for retained final acceptance and recoverable history. Earlier failure/skip gating and real worker dispatch are reported evidence in receipt 0007, not independently replayed here. Receipt honestly limits concurrency to one Codex worker plus independent shell B and limits recovery to resumed handoff; no host restart or simultaneous two-Codex-worker proof is claimed.

## Adjudicated acceptance

| Axis/criterion | Verdict | Evidence and limit |
| --- | --- | --- |
| Repository standards | PASS for this review | Relevant validation/doc policies read; only this note written; candidate diff whitespace check passes |
| PR simple output | PASS | Actual concise body above; observed results and reported receipt evidence distinguished |
| PR artifact delivery | PASS contract, execution pending coordinator | Skill specifies grouped Previews and audience safety; receipt 0008 artifact exercise makes no render claim |
| Retro source grounding | PASS | Actual log tails inspected, prior failure retained, source scripts/workflow read |
| Domain compatibility | PASS supplied scenarios | Decisions above follow configured/legacy/current authority rules |
| implement-spec retained fixture | PASS with declared limits | Independent acceptance and bundle verification, exact ledger read |
| Installed discovery/push/Previews render | NOT EVALUATED | Coordinator-owned remaining Plan 7 checks; this file invocation does not establish discovery |

No blocking findings. CI/harness recommendations are nonblocking backlog; they do not expand Plan 7. Evidence for earlier runtime behavior is accepted as reported by the trial worker with the independent checks above, rather than relabeled as this evaluator execution.

Skill identities at review: pr `49692fe2e290a150b19bdc4e4498f0049710e3669f24b7313c4791edcfe54eef`; retro `36e19e5d56bd2565c0ac454669692f080a466ed29117ed08b56f7a22061bc434`; domain-modeling `b44c8a45d0def59dbaa4c5a9ceef4dac27f3aece5cfadcadb71bba2f9610d9b7`; implement-spec `64a648f2c4bce6cf390fd6e8c1921ab072798bbfa863f70e704a755af458efc5`.
