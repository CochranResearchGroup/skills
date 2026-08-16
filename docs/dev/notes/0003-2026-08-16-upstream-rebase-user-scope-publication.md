# Upstream Rebase And Codex User-Scope Publication Receipt

- Date: 2026-08-16
- Upstream: `mattpocock/skills` `main` at
  `068b6e0c62393147daf03530149cdce209c93da8`
- Clean mirror: local `main` at the exact upstream commit
- Downstream carry: `eco/main`, eleven commits ahead and zero behind after the
  source integration commit `9addf28`
- Recovery ref: `backup/eco-main/2026-08-16-pre-rebase` at `47a58e4`
- User-scope destination: `/home/ecochran76/.agents/skills`

## Outcome

The local Codex/workstation overlay was rebased onto the reviewed upstream tip.
The promoted manifest now contains 24 skills, including the upstream additions
`wayfinder`, `research`, `wizard`, `to-questionnaire`, `wait-what`, and
`writing-for-agents`. The retired `to-prd`, `to-issues`, and
`writing-great-skills` names are not installed. `implement` remains in the
source checkout for upstream comparability but is neither promoted nor
installed because its automatic commit behavior conflicts with the downstream
authority boundary.

The publisher created symlinks only for the 24 curated manifest entries. No
same-name or retired user-scope installations existed, so this live run did not
need to create a backup. Future replacement runs preserve prior installations
under `/home/ecochran76/.agents/skill-backups/mapocock/<timestamp>/`.

## Validation Receipt

- `npm run check-plugin-version`: pass; plugin version `1.2.3` is synchronized.
- `python3 -m unittest discover -s .codex/skills/repo-policy-selector/tests -p
  'test_*.py'`: pass; 35 tests.
- Active-only planning contract audit: pass after closing Plan 0002; no open
  plans or problems remain, and the recorded ROADMAP/RUNBOOK baseline applies.
- Goal-execution contract audit: pass.
- Promoted-skill validation: pass; 24 unique names, matching skill-directory
  names, Codex UI metadata, and Claude/Codex invocation parity.
- Documentation validation: pass; local links resolved across 20 engineering
  documentation files.
- Publisher validation: pass in an isolated destination, including replacement,
  retirement, external backup placement, publication, and identity check.
- Live installed identity: pass; all 24 user-scope entries are symlinks to the
  rebased checkout and contain `SKILL.md` plus `agents/openai.yaml`.
- Retired-name check: pass; `implement`, `to-prd`, `to-issues`, and
  `writing-great-skills` are absent from user scope.

No remote branch, tag, plugin release, or GitHub release was published.

## Follow-Up

Start a fresh Codex session before relying on the refreshed skill inventory.
For future upstream intake, fetch into `upstream/main`, keep local `main` as the
clean mirror, and rebase `eco/main` only after creating a new dated recovery
ref.
