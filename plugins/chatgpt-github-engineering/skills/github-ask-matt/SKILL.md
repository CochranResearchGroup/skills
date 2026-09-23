---
name: github-ask-matt
description: Route a repository question to the most useful ChatGPT GitHub engineering workflow. Use when the user is unsure whether they need review, research, architecture analysis, a specification, tickets, or a handoff.
---

# GitHub Workflow Router

Use the connected GitHub app to establish which authorized repository and
artifact the request concerns. Ask for the repository only when it cannot be
resolved from the conversation or available connector context.

Route by desired outcome:

- unclear idea or decision: `$github-grill-with-docs`
- repository or dependency research: `$github-research`
- fixed change or pull-request review: `$github-code-review`
- module or interface design: `$github-codebase-design`
- vocabulary or domain-boundary work: `$github-domain-modeling`
- architecture improvement survey: `$github-architecture-survey`
- implementation-ready specification: `$github-to-spec`
- tracer-bullet work breakdown: `$github-to-tickets`
- long-horizon decision map: `$github-wayfinder`
- continuation packet for another agent: `$github-handoff`
- agent-facing instruction design: `$github-writing-for-agents`
- plain-language interview without repository editing: `$github-grill-me`

Explain the shortest useful flow and start it when the user's request already
provides enough information. Do not claim the GitHub app can edit files, run
tests, create issues, push commits, or open pull requests. When writes are
needed, produce a proposed artifact or a handoff for a write-capable coding
environment.
