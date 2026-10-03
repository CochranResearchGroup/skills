---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace by default.

If the user asks for a durable note, repo policy handoff, plan continuation, or a handoff "per policy", read `AGENTS.md` and relevant files under `docs/dev/policies/`, then write the handoff where the repo says continuity artifacts live, commonly `docs/dev/notes/`.

Include a "suggested skills" section in the document, naming which skills the next agent should read the available skill instructions for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

Include exact paths, commands run, validation results, and remaining blockers when those are needed for the next agent to continue safely.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
