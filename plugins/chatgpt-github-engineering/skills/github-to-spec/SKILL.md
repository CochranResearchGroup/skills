---
name: github-to-spec
description: Turn an established conversation and connected GitHub evidence into an implementation-ready specification without reopening the design interview.
---

# GitHub Specification

Use the decisions already made in the conversation. Inspect the authorized
repository to verify current behavior, relevant modules, terminology,
constraints, and existing tests. Ask only for a missing decision that would
materially change scope or acceptance.

Produce a specification containing:

- problem and intended outcome;
- repository-grounded current state;
- scope and non-goals;
- proposed behavior and interfaces;
- affected components and compatibility constraints;
- failure cases and security or privacy considerations;
- acceptance criteria and validation plan;
- unresolved questions and evidence limits.

Cite repository paths, issues, pull requests, or commits for current-state
claims. Return the specification in the chat as a proposed artifact. Do not
state that it was filed as an issue or committed.
