# Issue tracker: Repo-Native Artifacts

Work for this repo lives in checked-in repo artifacts rather than a remote issue tracker.

## Discovery order

Read the repo loading contract first:

1. `AGENTS.md`
2. relevant files under `docs/dev/policies/`
3. current plan files under `docs/dev/plans/`
4. durable notes under `docs/dev/notes/`
5. `ROADMAP.md`, `RUNBOOK.md`, `PROGRESS.md`, or other repo-specific planning files when present

Use GitHub, Linear, Jira, or another tracker only when those files say that tracker is authoritative for the work.

## When a skill says "publish to the issue tracker"

Create or update a repo-native artifact:

- PRDs and bounded plans: `docs/dev/plans/<NNNN>-<slug>.md`
- handoffs, adoption notes, and continuity records: `docs/dev/notes/<NNNN>-YYYY-MM-DD-<slug>.md`
- roadmap/runbook changes: the repo's existing `ROADMAP.md`, `RUNBOOK.md`, or documented equivalent

Preserve any numbering convention already present in the target directory. If no convention exists, use a zero-padded sequence starting at `0001`.

## When a skill says "fetch the relevant ticket"

Read the referenced plan, note, roadmap item, runbook item, or local artifact path. Do not create a remote issue merely because the skill says "issue tracker."

## Status

Represent status in the artifact itself with a short status line or checklist, matching the local convention if one exists.
