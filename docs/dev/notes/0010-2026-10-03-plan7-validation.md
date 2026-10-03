# Plan 7 source and integration validation

## Inputs and reconciliation

Source candidate: adoption/plan7, rebased onto upstream d81f3a183412e71a5b1e84ca21bc1a35eea03a60. Recovery ref backup/eco-main/2026-10-03-pre-plan7 at f99b249. Upstream is an ancestor. Retained Codex discovery/runtime/preview/planning carry, bounded diagnostics, adjudicated review, stable TDD seams and safe conflict recovery. Rebase conflicts reconciled downstream semantics with glossary naming; upstream pr/retro retained and adapted. Restored conflict-resolution metadata and manifest membership after upstream deletion. Policies and separate ChatGPT plugin have no diff from recovery ref.

## Source checks

- All skill YAML frontmatter and 27 promoted Codex metadata blocks parse with PyYAML via uv.
- Non-example relative links resolve across promoted skills, README/index and engineering/productivity docs. Markdown fenced examples excluded; their fictional paths are not source links.
- Plugin version synchronization: PASS, 1.2.3.
- Strict Claude plugin/marketplace validation: PASS; verifies upstream compatibility only, not Codex runtime.
- Publisher shell syntax, semantic contract checks and disposable 27-link publication: PASS.
- Planning audit: PASS after normalizing Plans 6/7 to parser-supported Status headers.
- git diff --check: PASS.

## Selector suite

Direct installed-bundle invocation ran 124 tests with ten errors: source-repository contract tests expected .codex/skills/modules and catalog.yaml, which are not included beside installed tests. No policy change was required.

A disposable harness copied the candidate selector bundle and linked modules, profiles and catalog.yaml from the existing /home/ecochran76/workspace.local/agent-policies source. Fixture-only author/committer environment was supplied. Command: python3 -m unittest discover -s /tmp/mapocock-policy-tests-abyswp7r/repo-policy-selector/tests -v. Result: 124 tests in 35.760s, OK. Output /tmp/mapocock-plan7-selector-harness.log. This compares actual source modules with the bundled library, not the bundle with itself. No external repository was modified.

## Behavioral evidence

Worker lane /root/implement_spec_trial produced Note 0007. Primary independently reran python3 /tmp/plan7-implement-spec-trial/tests/accept.py a b c: PASS; verified fixture HEAD bc04a7a35391a5ab9934cbe020df4247cef142ea and complete-history bundle. Tested implement-spec hash 64a648f2c4bce6cf390fd6e8c1921ab072798bbfa863f70e704a755af458efc5 matches source. Capacity limits permit one Codex and one shell worker concurrently; two concurrent Codex workers are not claimed. Ledger-resumed worker, not host restart, was tested.

Worker lane /root/adapt_pr_retro produced Note 0008 with adapted source and author exercises. Primary inspected source and receipts; independent fresh review is recorded separately in Note 0009 when complete. Publication and installed catalog proof remain separate checks.

No installed trees or remote branch were changed by these source checks.
