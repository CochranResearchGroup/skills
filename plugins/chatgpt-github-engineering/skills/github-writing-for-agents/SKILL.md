---
name: github-writing-for-agents
description: Draft or review repository instructions, skills, runbooks, and agent-facing documents using connected GitHub context.
---

# Writing For Repository Agents

Inspect the repository's existing instruction hierarchy and the documents that
point to the target file. Determine who loads the document, under what trigger,
and what decisions it must change.

Write for selective retrieval:

- put routing conditions in names, descriptions, and pointer text;
- keep the entrypoint short and move conditional detail behind explicit links;
- state non-obvious invariants and authority boundaries;
- remove generic advice, duplication, stale tool assumptions, and contradictory
  requirements;
- make output and stop conditions testable.

Preserve the repository's precedence rules and user intent. Return revised text
or a patch with cited reasons. The connected GitHub app cannot apply the edit,
so label all changes as proposed.
