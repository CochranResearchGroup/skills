---
name: github-architecture-survey
description: Survey an authorized GitHub repository for high-value module-deepening opportunities and produce a prioritized architecture report.
---

# GitHub Architecture Survey

Establish the repository's purpose, major directories, public entry points,
tests, and architecture guidance. Sample representative modules across the
system; do not rank the whole repository from one subsystem.

Look for evidence-backed opportunities such as duplicated policy, shallow
wrappers, leaky abstractions, scattered invariants, high fan-out change points,
and difficult-to-test boundaries. Exclude pure style preferences and large
rewrites without a clear seam.

For each candidate report:

- repository locations and observed evidence;
- the behavior that should move behind a deeper interface;
- expected reduction in coupling or change surface;
- migration risk and a smallest useful tracer;
- validation that would demonstrate improvement.

Prioritize a short list by impact, evidence strength, and implementation risk.
Return Markdown suitable for discussion. Do not create an HTML artifact or
claim repository-wide completeness when connector visibility is limited.
