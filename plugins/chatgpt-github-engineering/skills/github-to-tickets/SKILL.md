---
name: github-to-tickets
description: Break an approved specification or plan into dependency-aware implementation tickets grounded in an authorized GitHub repository.
---

# GitHub Ticket Design

Read the governing specification or conversation and inspect the repository
areas it affects. Build tracer-bullet tickets that each produce one testable,
integrable outcome. Prefer vertical slices over layer-by-layer tasks.

For every ticket include:

- title and outcome;
- repository surface;
- dependencies and blocking edges;
- scope and non-goals;
- implementation notes only where evidence supports them;
- acceptance evidence;
- risks or decisions that remain open.

Order blockers before dependents and identify work that can proceed in parallel
without overlapping writes. Use existing issue vocabulary when the repository
documents it.

The connected GitHub app is read-only. Return copy-ready issue bodies and a
dependency map; do not create issues, labels, milestones, or projects.
