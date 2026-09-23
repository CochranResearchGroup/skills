---
name: github-codebase-design
description: Analyze module boundaries and design deeper interfaces from connected GitHub code when the user is planning or improving architecture.
---

# GitHub Codebase Design

Use the connected GitHub app to inspect the relevant module, its public
interface, callers, dependencies, tests, and architecture documentation. Do not
infer system-wide behavior from one file.

Frame the design around a deep module: substantial behavior hidden behind a
small coherent interface. Evaluate information hiding, coupling, change
locality, invariants, and test seams. When alternatives are useful, compare at
least two materially different interface shapes instead of superficial naming
variations.

Return the recommended boundary, proposed interface, responsibilities moved in
or out, migration sequence, affected files, risks, and validation strategy.
Cite repository evidence for current-state claims. Present code only as an
illustrative sketch or proposed patch; the GitHub app cannot apply it.
