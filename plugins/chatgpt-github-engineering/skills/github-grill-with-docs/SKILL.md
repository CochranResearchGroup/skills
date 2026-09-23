---
name: github-grill-with-docs
description: Interview the user about an engineering change while checking repository terminology, architecture decisions, and documentation through the connected GitHub app.
---

# Grill With Repository Documentation

Identify the authorized repository and inspect its contributor instructions,
glossary or context document, architecture decisions, and nearby documentation.
Use those sources to establish current terminology and constraints before asking
design questions.

Interview the user using `$github-grilling` discipline:

- retrieve factual answers from GitHub;
- ask the user for product and tradeoff decisions;
- test proposed terms against existing repository language;
- identify documentation and ADR changes the decision would require.

Return:

1. the resolved design;
2. glossary additions or corrections;
3. proposed ADR or documentation text;
4. cited repository evidence;
5. an implementation handoff when code changes are required.

The native GitHub app is read-only. Present documentation changes as a patch or
copy-ready draft and label them as proposed, never applied.
