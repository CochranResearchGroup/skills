---
name: github-handoff
description: Produce a restart-safe handoff for a coding agent or teammate using the conversation and verified GitHub repository state.
---

# GitHub Handoff

Re-read the relevant authorized repository evidence before summarizing. Treat
conversation claims as context, not proof of current branch, commit, pull
request, test, or issue state.

Produce a compact handoff containing:

- objective and explicit non-goals;
- repository and exact known ref or locator;
- verified current state with citations;
- decisions and their rationale;
- completed work versus proposed work;
- remaining acceptance criteria;
- exact next action and validation commands for a write-capable environment;
- blockers, authority boundaries, and evidence gaps.

Never include credentials or unnecessary private data. Do not claim a clean
working tree, successful tests, unpublished local changes, or runtime state
that the GitHub connector cannot observe.
