---
name: retro
description: "Conduct a retrospective on a coding session."
disable-model-invocation: true
---

The user has asked for a **retrospective**. You are suggesting improvements to the coding agent's **environment** to improve future runs.

## Steps

1. This skill is explicitly invoked by the user. Load `writing-for-agents` through the available Codex skill interface or read its installed `SKILL.md`; do not assume a Claude Skill tool. Follow repository authority when it differs.

2. Read the provided Codex conversation, session export, or exact log artifact for the specified session; default to the visible current session. For an unknown log location outside the repository, use `file-searcher` first. Do not assume Claude log paths or that a remote Codex session's full history exists locally. If evidence is incomplete, state the reviewed interval and limitations; ask for missing evidence only when needed. Do not fill gaps with remembered struggles.

3. Look for candidates for improvement in these categories.

- **Navigation**: how easy was it for the agent to find the right files? Are there hidden dependencies between files? Would a **navigation pointer** make it easier? _Use when_ the session took a long time to find a piece of information.
- **Automated checks**: are there automated checks that could catch errors the agent made? Linting, typing, tests, filesystem linters? Read the repo's own check command first (its `package.json`/build-tool `lint`/`check` scripts, its CI workflow), so a check that already exists but sits unwired or silently broken is the finding, not a reinvention. A repo with no **guardrail** (no pre-commit hook and no CI job running its lint/typecheck/test command) is itself a finding: an un-linted repo is a standing missed opportunity, not a neutral default. _Use when_ the agent made a mistake an automated check could have caught, or the repo has no guardrail at all.
- **Coding standards**: should the **reviewer agent** be given a new rule to enforce? Should an existing rule be removed or clarified? Classify the violation first: a **mechanical** one (a fixed syntactic pattern, a banned API, an import shape, a file-location rule) gets a deterministic check, full stop: a custom rule in the repo's own linter, a new pre-commit hook, or a new CI job, whichever the repo's language and existing guardrail make cheapest. Default to building the check over writing the rule. Reserve `CODING_STANDARDS.md` for genuine **judgement calls** (cross-file consistency, "matches the surrounding style," anything no guardrail could ever substitute for). _Use when_ the reviewer agent failed to catch a mistake.
- **Global AGENTS.md**: are there any steering instructions that should be moved to coding standards (or automated checks) instead? _Use when_ the AGENTS.md file is particularly large - in the repo OR the user's global scope.
- **Tool economy**: did the agent make expensive tool calls that could be streamlined? Is there any custom tooling (CLI's, MCP's) that is particularly token-inefficient? _Use when_ the agent made an expensive tool call.
- **No-ops**: look for instructions in steering files that don't modify the agent's behavior. _Use when_ the steering files are large and unwieldy.
- **Information access**: look for opportunities to increase the agent's access to information. Teeing dev server logs, readonly access to third-party services. _Use when_ a crucial piece of information was not available to the agent.

4. Present only source-backed candidates in severity order. Each names the observed moment or source locator, consequence, proposed improvement, and cheapest meaningful verification. No finding is a valid result; do not invent advice to fill categories. Distinguish missing checks from checks that exist but are unwired, and assess ongoing maintenance cost.

5. Default to recommendations when asked for a retrospective. Implement candidates already authorized within the task's scope without a redundant approval request; do not expand a retrospective into unrelated global instruction edits, broader access grants, or other repositories. When implementation is authorized, prefer a deterministic check for mechanical errors, verify it detects the failure where practical, and update the relevant docs.

6. For a substantial report, use the `previews` skill and publish findings and supporting artifacts in one session; return one browser URL. Use feedback only when approval is actually required. If unavailable, state the fallback and deliver the report in accessible Markdown. Keep secrets and raw private session logs out of shared artifacts.

## Reference

### Implementation vs Review

Remember that all work goes through two stages: implementation and review. The implementation agent has the most **context pressure**. They are responsible for exploration, writing code, and debugging failures.

A reviewing agent can focus on the diff and relevant source, standards, and specification. Review may still require exploration, execution, or debugging; do not assume the diff alone proves correctness.

Keep detailed judgement guidance available to review without bloating every implementation prompt. Implementation still follows the repository standards and authority. Separate reviewer agents are optional and require applicable delegation authority.

### Files

You have access to several files in the repo:

- `AGENTS.md` (and `CLAUDE.md` where maintained for upstream compatibility): these files are pushed to the context window of any agent working in this repo. They should be used incredibly sparingly, usually only for **navigation pointers** to other files.
- `CODING_STANDARDS.md`: this file is read during review, not implementation. Add **navigation pointers** to docs folders if the standards file gets more than 1,000 lines long.
- Docs: use docs as references files, pointed to by other files. Look for existing docs before writing new ones.
- Skills: use skills for docs (since their description goes into the agent's context window), or for user-invoked commands. Follow the advice in the `writing-for-agents` skill.
