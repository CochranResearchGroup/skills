---
name: github-grilling
description: Provide the reusable interview discipline for ChatGPT workflows that must separate repository facts from human decisions.
---

# Grilling Discipline

Use this underneath another workflow when alignment requires an interview.

Separate two kinds of uncertainty:

1. Repository facts: resolve with the connected GitHub app and cite the file,
   pull request, issue, or commit that supports the answer.
2. Human decisions: ask the user and record the answer without silently
   substituting an inferred preference.

Keep a frontier of unresolved decisions. Each round should reduce that frontier
or expose a genuine dependency. Ask concrete scenario questions when abstract
language hides tradeoffs. Restate decisions only when doing so reveals a
conflict or materially changes the next question.

Stop when remaining uncertainty is either immaterial, explicitly deferred, or
blocked by unavailable evidence. Return a concise decision record; do not claim
that it has been written to the repository.
