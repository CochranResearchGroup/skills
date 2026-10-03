## What it does

`retro` reviews a coding session and identifies source-backed improvements to the agent's environment. It is explicitly invoked; Codex metadata disables implicit invocation. Invoke `$retro` through the available skill interface.

## Session evidence in Codex remote

Use the supplied conversation, session export, or exact log artifact; default to the visible current conversation. For unknown external log locations, use `file-searcher` before reading candidates. Do not assume Claude log directories or that a remote session's complete history is present locally. State which interval was reviewed and any missing evidence. A retrospective with no findings is valid.

Read the installed `writing-for-agents` skill through available Codex capabilities, without assuming a Claude Skill tool. Repository instructions remain authoritative.

## Choosing improvements

| Observed problem | Preferred improvement |
| --- | --- |
| Repeated difficulty finding source | A concise navigation pointer to existing authority |
| Mechanical mistake | A deterministic check at the cheapest meaningful layer |
| Existing check not run | Repair its wiring before proposing another check |
| Judgement mistake | Clarify the existing review standards |
| Expensive tool use | Improve the query or tool interface |
| Missing information | Propose the narrow access or logging improvement needed |
| Instructions with no useful effect | Propose removing or clarifying them |

Inspect repository check commands and CI before proposing new guardrails. Assess maintenance cost as well as protective value. Avoid accumulating prose rules for errors a machine can detect. Implementation still follows repository standards; review may need source exploration and execution, not just a diff.

## Delivering and applying findings

Present candidates in severity order. Each includes a specific observed moment or source locator, consequence, proposed improvement, and meaningful verification. Do not invent findings to fill categories.

A retrospective request defaults to recommendations. If the user already authorized in-scope fixes, implement them without a redundant approval request. The skill does not authorize unrelated global instruction edits, broader access grants, or changes to other repositories. When adding a deterministic check, demonstrate that it catches the relevant failure where practical and run it against the correction.

Use `$previews` for substantial reports, grouping findings and suitable supporting artifacts in one session and returning one browser URL. Keep secrets and raw private session logs out of shared artifacts. Use feedback only when approval is required by the task; if the service is unavailable, state the fallback and deliver accessible Markdown.

## It is working if

- Every finding traces to supplied session evidence.
- An existing unwired check is distinguished from an absent check.
- Mechanical errors get proposed deterministic checks, and judgement rules stay focused.
- Changes stay within existing authorization and the report states evidence limitations.

Use `code-review` for a verdict on code correctness. Use `retro` to improve how future sessions find information and avoid repeat mistakes.
