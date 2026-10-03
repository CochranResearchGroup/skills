# PR and retro bounded author exercises

Date: 2026-10-03. These are actual authored outputs produced by following the adapted skills in the candidate checkout, not fresh-worker or installed-catalog invocation proof. Static contract checks are recorded separately. This exercise does not prove automatic discovery or independent-agent compliance.

## Inputs

- Small nonvisual change: the `pr`/`retro` Codex adaptation in this checkout, including explicit retro invocation metadata. Observed `git diff --check` exit 0; YAML/frontmatter contract check via `uv run --with pyyaml python` printed `pr: metadata and adaptation contracts PASS` and `retro: metadata and adaptation contracts PASS`.
- Artifact-producing change: substantial Markdown PR/retro guidance authored in `docs/engineering/pr.md` and `docs/engineering/retro.md`. These files exist in this checkout; a browser render has not been observed by this worker.
- Supplied Codex evidence: this worker's tool transcript. First metadata command failed with `ModuleNotFoundError: No module named 'yaml'`. A bounded capability read found `/home/linuxbrew/.linuxbrew/bin/uv`; retry using `uv run --with pyyaml python` passed. There is no evidence of repeated manual checks causing a defect, so that supplied category produces no finding.

## PR exercise: small nonvisual change

**Produced body:**

Adapt PR and retrospective guidance for Codex remote, including explicit-only retrospective invocation and observed validation claims. Small changes can use concise prose, and existing repository PR templates remain authoritative.

Validation: `git diff --check` passed. Frontmatter and Codex metadata parsed successfully, and focused adaptation contracts passed for both skills. Independent invocation and fresh-session discovery have not been exercised here.

**Result:** concise body, no forced diagram or Merge Danger taxonomy, observed evidence only. The test does not invent a failing baseline.

## PR exercise: artifact-producing change

**Produced body:**

Update the PR and retrospective guides so remote Codex users receive substantial reports through Previews, while reviewer-facing PR descriptions remain self-contained. The guidance separates artifact viewing from execution evidence and honors the intended audience of private reports.

Validation: `git diff --check` and focused metadata/contracts passed. The Markdown guides were authored and inspected as source; browser rendering remains unverified. The coordinator will group these guides and this receipt into one Previews acceptance packet. Its URL is user-facing; private or inaccessible links must not be copied into a public PR.

**Result:** artifact delivery is specified without falsely claiming publication or rendering. No diagram was warranted. Actual Previews publication remains the coordinator's integration task.

## Retro exercise

**Produced findings:**

1. Low severity: metadata validation assumed system Python had PyYAML. Evidence: the first metadata command failed at `import yaml` with `ModuleNotFoundError`; the bounded retry through `uv run --with pyyaml python` passed. Reuse a declared dependency runner or the repository's existing validator for future metadata checks. Verification: run the same check in a clean environment through the declared runner. This is a deterministic environment improvement, not a new global prose rule.

No finding for repeated manual checks: the supplied evidence does not show harm or an unwired protective check caused by them. No global instructions, additional access permissions, or unrelated source changes were made by this retrospective.

**Result:** a source-backed recommendation, bounded evidence interval, no generic category filling, no automatic scope expansion. This is an author exercise, not an independent retrospective invocation.

## Domain authority exercises

These are supplied filesystem scenarios evaluated by applying the skill's authority rules; no other repository files were changed.

| Scenario | Selected authority | Outcome |
| --- | --- | --- |
| A: only legacy `CONTEXT.md` exists, no configured authority | `CONTEXT.md` | Use legacy terms; no rename or duplicate file |
| B: only `GLOSSARY.md` exists, no configured authority | `GLOSSARY.md` | Use current glossary terms |
| C: configured `docs/vocabulary.md`, plus both legacy and glossary files | `docs/vocabulary.md` | Explicit configuration wins |
| D: both files exist, disagree, no configured authority | Unresolved | Inspect repo routing and reconcile ambiguity before choosing; preserve both, no overwrite |

The PR skill explicitly handles the first three. The worker identified that the fourth needed an explicit ambiguity rule and added that rule to the skill; the coordinator should verify consumers follow the same rule.

## Focused checks and limits

- `git diff --check`: PASS.
- Parsed both skill frontmatters and both `agents/openai.yaml` files through PyYAML: PASS.
- Checked retained attribution, explicit retro metadata, Codex/Previews delivery, file-searcher routing, template precedence and observed evidence contracts: PASS.
- No fresh worker, installation, remote publication, browser render, or complete workflow proof is claimed here.
