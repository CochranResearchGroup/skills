# Plan 0005 | ChatGPT GitHub Skills

Status: CLOSED

## Current State

The additive ChatGPT package is implemented on
`feature/chatgpt-github-skills`. It contains fourteen GitHub-oriented skills, a
portable plugin manifest, a repository marketplace entry, and deterministic
individual-skill and plugin ZIP packaging. Existing skill files remain
unchanged.

## Scope

- Add ChatGPT-specific editions of the selected analysis, planning, review,
  and writing skills under a new plugin root.
- Add deterministic packaging for individual skill ZIPs and one plugin ZIP.
- Add a repository marketplace catalog suitable for import from the
  `CochranResearchGroup/skills` GitHub repository.
- Document installation and the boundary between the skill package and the
  separately authorized GitHub app.

## Non-Goals

- Do not modify the existing skills or Claude plugin manifests.
- Do not add write-capable GitHub tools, create issues, push, publish, import,
  or install the marketplace.
- Do not imply that ChatGPT's native GitHub app can edit repository state.

## Acceptance Criteria

- The new plugin contains fourteen focused ChatGPT skills and a portable root
  manifest.
- Each individual skill can be packaged as a self-contained ZIP.
- The full plugin can be packaged as one ZIP.
- `.agents/plugins/marketplace.json` resolves to the new plugin directory.
- Deterministic validation checks JSON, YAML frontmatter, package contents,
  internal links, connector boundaries, and absence of changes under the
  existing `skills/` and `.claude-plugin/` trees.

## Definition Of Done

All three additive distribution forms are present and locally validated:
individual skill ZIPs, bundled plugin ZIP, and a GitHub-importable marketplace.

## Next Action

Review and publish the branch when desired. Marketplace import, ChatGPT
installation, and any remote push remain separate operator actions.

## Completion Evidence

- `packaging/build.py` produced fourteen individual skill ZIPs and one bundled
  plugin ZIP twice with identical SHA-256 output.
- `packaging/validate.py` validated the manifest/marketplace relationship,
  exact skill inventory, skill frontmatter, and all fifteen archives.
- The portable `plugin.json` passed the published Agent Plugins 1.0.0 JSON
  schema using `check-jsonschema` in an ephemeral environment.
- The active planning and goal-contract audits passed.
- `git diff --check` passed, and the changed-path readback contains no path
  below the existing `skills/` or `.claude-plugin/` trees.
