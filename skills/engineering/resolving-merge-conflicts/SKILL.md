---
name: resolving-merge-conflicts
description: "Use when you need to resolve an in-progress git merge/rebase conflict."
---

1. **See the current state** of the merge/rebase. Check git history, and the conflicting files.

2. **Find the primary sources** for each conflict. Understand deeply why each change was made, and what the original intent was. Read the commit messages, check the PRs, check original issues/tickets.

3. **Resolve each hunk by intent.** Preserve both intents where possible. Where
   incompatible, pick the one matching the merge's stated goal and note the
   trade-off. Do **not** invent new behaviour or trust a favor option as semantic
   proof.

4. **Stop safely when proof is missing.** Abort or restart from a verified
   recovery ref when either side's intent cannot be established, the recovery
   point is uncertain, or the proposed result cannot be validated safely.

5. Discover the project's **automated checks** and frozen semantic invariants.
   Run both; syntax and tests alone do not prove carry behavior survived.

6. **Finish only after validation.** Stage and continue or commit when the
   resolved result is proved. Record an abort/restart as the correct fail-closed
   outcome when completion was unsafe.
