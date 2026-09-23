---
name: github-domain-modeling
description: Build or sharpen a repository's domain vocabulary and boundaries from code, documentation, tests, and architecture decisions available through GitHub.
---

# GitHub Domain Modeling

Inspect the repository's glossary or context files, domain types, public APIs,
tests, ADRs, and user-facing language. Collect competing terms and identify
where one word names different concepts or several words name the same concept.

Work with the user to choose terms and boundaries. Use edge cases and concrete
scenarios to test whether the model holds. Repository text is evidence of the
current model, not automatic proof that the model is correct.

Return:

- a proposed glossary with definitions and counterexamples;
- bounded-context or module boundaries;
- invariants and ambiguous cases;
- proposed documentation or ADR changes;
- affected repository locations with citations.

Keep all changes explicitly proposed. The connected GitHub app cannot update
the glossary, ADRs, code, or tests.
