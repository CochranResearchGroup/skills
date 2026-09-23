---
name: github-grill-me
description: Interview the user to resolve a plan, product decision, or design while grounding factual repository questions in connected GitHub evidence.
---

# Repository-Grounded Grilling

Interview the user about decisions only they can make. Use the connected GitHub
app for facts the repository can answer; do not ask the user to recall file
contents, module names, or recorded decisions that can be retrieved.

Maintain a compact decision frontier:

- settled facts, with repository citations;
- settled user decisions;
- open decisions;
- assumptions that still need evidence.

Ask one coherent group of related questions at a time. Follow answers to their
consequences instead of marching through a generic questionnaire. Challenge
contradictions and vague success criteria directly.

Finish when the material branches are resolved or the user stops the interview.
Return the decisions, unresolved questions, repository evidence, and recommended
next workflow. Do not mutate GitHub or represent a draft as repository state.
