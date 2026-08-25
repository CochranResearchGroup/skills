# Upstream Rebase Receipt

- Date: 2026-08-25
- Upstream: `mattpocock/skills` `main` at
  `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`
- Clean mirror: local `main` at the exact upstream commit
- Downstream carry: `eco/main`, rebased with `upstream/main` as an ancestor
- Recovery ref: `backup/eco-main/2026-08-25-pre-rebase` at
  `7cc86a833fb2d70d4fb4def1a4193dd956102902`
- Source reconciliation: `11c362c`

## Outcome

The downstream policy and Codex/workstation carry was rebased onto the fetched
upstream tip without skipping a commit. Upstream's `wait-what` context-map fix,
quoted YAML descriptions, grilling question separators, and new
`implement-spec` and `retro` in-progress skills are present. The two new skills
remain unpromoted. `implement` remains in source for upstream comparability but
is absent from the promoted indexes, plugin manifest, and curated Codex
publication set.

## Conflict Decisions

The rebase stopped first at the Codex workflow-tailoring commit and then at the
curated-publication commit. Sixteen files overlapped overall. Their upstream
side mostly normalized punctuation, while the downstream side carried
repo-native planning, graph-backed discovery, preview delivery, runtime proof,
and no-automatic-commit authority rules.

The initial merge-helper favor direction retained the upstream side in conflict
hunks. A post-rebase semantic audit detected the regression because `implement`
reappeared in both promoted indexes while the manifest still excluded it. The
conflicted files were rebuilt from the recovery ref with the old upstream base
and new upstream tip as three-way inputs. Downstream semantics were retained at
conflicts, non-conflicting upstream changes were incorporated, em dashes in the
reconciled files were normalized, and colon-bearing YAML descriptions were
quoted. Commit `11c362c` records that correction.

## Validation Receipt

- `npm run check-plugin-version`: pass; plugin version `1.2.3` is synchronized.
- `npx -y @anthropic-ai/claude-code plugin validate . --strict`: pass.
- Repo-policy selector suite: pass; 76 tests. Fixture-scoped Git author and
  committer variables were supplied because temporary repositories do not
  inherit this checkout's local identity.
- Promoted publication check: pass; 24 curated Codex user-scope skill links
  resolve correctly. The command was check-only and performed no publication.
- Documentation validation: pass; relative links resolve across 25 promoted
  documentation files.
- Frontmatter validation: pass; all 37 `SKILL.md` YAML blocks parse.
- Planning audits: rerun after Plan 0003 closes so the repo's accepted
  ROADMAP/RUNBOOK baseline is evaluated in its steady-state scope.

No remote branch, tag, release, plugin, or user-scope skill publication was
written during this rebase.
