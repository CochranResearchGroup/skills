---
name: github-code-review
description: Review a fixed GitHub pull request, commit range, or diff for correctness and specification conformance using repository evidence.
---

# GitHub Code Review

Require a fixed review target: pull request, commit, tag range, or supplied diff.
Resolve the exact repository and target before drawing conclusions. Inspect the
diff, affected call sites, tests, contributor guidance, and governing issue or
specification when available.

Review on two independent axes:

- Standards: correctness, security, compatibility, maintainability, and test
  protection.
- Specification: whether the change satisfies the documented intent without
  unrelated scope.

Only report actionable findings supported by a concrete code path or violated
contract. For each finding include severity, file and symbol or line locator,
failure scenario, evidence, and a bounded correction. Distinguish confirmed
defects from questions and residual risks.

Do not manufacture approval status, CI results, runtime evidence, or repository
writes. If execution is needed to prove a concern, state the exact test or
experiment a write-capable environment should run.
