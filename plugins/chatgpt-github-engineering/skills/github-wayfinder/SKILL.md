---
name: github-wayfinder
description: Map a large, uncertain repository initiative into decision tickets and a bounded frontier using connected GitHub evidence.
---

# GitHub Wayfinder

Use this when the destination is known but the route is too uncertain for an
implementation plan. Inspect the repository's current architecture, roadmap,
issues, ADRs, and prior related changes.

Create a decision map rather than a disguised task backlog. Each node should be
one question whose answer changes the route. Classify it as:

- repository research;
- external research;
- prototype or experiment requiring a write-capable environment;
- human product or tradeoff decision;
- prerequisite task needed before a decision can be made.

Record blocking edges, known facts, evidence, and the next decision frontier.
Resolve repository-research nodes directly when the connector has sufficient
evidence. Return copy-ready map and ticket text; do not create or update GitHub
issues.
