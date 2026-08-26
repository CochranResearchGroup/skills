# Note 0005 | Policy Identity And Skill Conformance

Date: 2026-08-25

## Decision

Adopted-policy identity is semantic and must be unique; the filename ordinal is
only a local locator. Mapocock retained the newest applicable policy generation
for each of seven duplicate identities and removed the superseded copies and
wire-in entries.

The roadmap/runbook governance module was also retired. This repository has no
canonical `ROADMAP.md` or `RUNBOOK.md`, and the module's adoption notes limit it
to repositories that already carry those planning surfaces or have suffered
that form of drift. The former audit baseline merely accepted their absence;
retaining both the module and the exception would preserve a false contract.

## Promoted Skill Contract

- Review findings are candidate evidence for primary-agent disposition;
  standards/conformance and specification/objective correctness remain
  separate axes.
- Delegation is conditional on authority and usefulness, with a serial primary
  path when delegation is unavailable.
- Conflict resolution is intent-based and may safely abort/restart when
  recovery or semantic evidence is insufficient.
- Diagnosis uses bounded productive probes instead of persistence slogans.
- Regression tests target the narrowest stable real seam; when no such seam
  exists, the unprotected risk is recorded as a testability gap.

`scripts/publish-codex-skills.sh` now checks these semantics before any curated
publication and continues to exclude `implement`, `implement-spec`, and
`retro`.

## Evidence And Custody

- Implementation commit: `29dbd06c756617e384311482a7d92e718c8bb1d8`.
- Shared source contract: agent-policies commit `c375eee`.
- Passed: active-plan audit, goal-contract audit, strict Claude plugin
  validation, plugin-version sync, 37 skill-frontmatter parses, links in 65
  Markdown files, and the 24-skill publication `--check`.
- The source selector reports zero duplicate identities and no validation
  problems. It still recommends the intentionally inapplicable
  roadmap/runbook companion based on broad repository signals.
- `eco/main` is two local commits ahead of owned `origin/eco/main` and 19 ahead
  of tracked `upstream/main` before this note's closeout commit.
- No push, publication, installation, rebase, or remote mutation occurred.

## Reusable Lesson

A generic profile recommendation is not adoption authority. Enforce uniqueness
for modules that are adopted, but evaluate optional companion modules against
their stated prerequisites instead of manufacturing repository structures to
make the recommendation appear satisfied.
