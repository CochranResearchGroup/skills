# Upstream Upgrade Evaluation

- Date: 2026-10-01
- Scope: fetch and evaluate; no source integration or installation changes
- Fork branch: `eco/main`
- Fork tip: `4964cffd68d3cece472ec098b2db0a6637338034`
- Reviewed upstream: `d81f3a183412e71a5b1e84ca21bc1a35eea03a60`
- Prior common base: `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`
- Divergence: 28 downstream commits, 36 upstream commits
- Upstream delta: 59 files, 653 insertions, 191 deletions

## Recommendations

| Change | Disposition | Required downstream treatment |
| --- | --- | --- |
| CONTEXT.md and CONTEXT-MAP.md become GLOSSARY.md and GLOSSARY-MAP.md | Adopt with compatibility | Prefer configured repo authority; recognize existing CONTEXT files. Do not create competing glossary authorities or rename other repos implicitly. Migrate source, format reference, setup template, docs and routing together. |
| New model-invoked pr skill | Adapt and promote | Preserve concrete before/after evidence and relevant risk description. Scale diagrams and template sections to actual complexity and repo PR templates; avoid mandatory visuals and one-word blast-radius descriptions. Preserve attribution and add Codex metadata. |
| retro graduates to engineering | Adapt, then consider promotion | Keep deterministic checks over repetitive prose rules. Replace Claude Skill-tool assumptions with Codex routing. Present recommendations; distinguish evaluation from authorization to implement checks, edit global instructions or access session logs. |
| implement-spec graduates to engineering | Defer promotion | Reconcile automatic delegation, resetting worktrees, merger-agent authority, unconditional TDD, automatic issue closure, ready-for-review changes and cleanup with repo authority/custody rules. Replace “fix all issues” with adjudicated findings. Source presence need not imply installation. |
| Upstream deletes resolving-merge-conflicts | Retain downstream | Our version establishes intent, recovery refs, safe abort/restart and semantic proof. Publisher explicitly requires this contract. Keep manifest, docs and router consistent. |
| ask-matt expands implementation/PR/retro flow | Selectively adapt | Route only approved promoted skills. Preserve repo-native plans, bounded discovery/runtime proof and commit authority. Do not reintroduce implement or implement-spec through router text. |
| link-skills excludes misc | Accept source change at integration | Curated publisher remains authoritative; upstream dev linker still includes in-progress and overwrites real directories. Do not use it to publish our curated set. |

## Integration Risk And Frozen Carry

`git merge-tree --write-tree HEAD upstream/main` returned conflict status without
changing the checkout or index. Fourteen unique paths conflict: plugin manifest,
README, engineering skill index, ask-matt docs/source, tdd docs/source, to-spec
docs, to-tickets docs, diagnosing-bugs source, improve-codebase-architecture
source, resolving-merge-conflicts source (modify/delete), setup source, and
triage source. This merge simulation is a preview; a replayed rebase can expose
a different per-commit conflict sequence.

Do not overwrite downstream files with upstream versions. Preserve bounded
research and diagnostic loops, CodeGraph/file-searcher/SysRAG routing,
repo-native planning, preview delivery, runtime evidence, adjudicated review,
stable seams without redundant approval, and no automatic commit behavior.
Preserve repo policies and the separate ChatGPT GitHub engineering plugin.
No upstream changes target that plugin directory in this delta.

## Recommended Execution Packet

Create a dated recovery ref before rebasing `eco/main`; retain the old base and
both tips as reconciliation inputs. Integrate upstream source while keeping
implement/implement-spec unpromoted and retaining conflict resolution. Adapt pr
for promotion; adapt retro separately and explicitly decide membership. Update
the manifest, publisher, skill indexes, router, documentation and Codex metadata
as one consistent set. Confirm exact promoted membership before installation.

Validate frontmatter and relative links, plugin version/manifest consistency,
repo-policy selector checks, and publisher semantic contracts. Independently
verify the frozen downstream semantics; syntax alone cannot prove preservation.
Publish only after source validation and separately verify both installed skill
roots. Remote push, tags and releases remain separate actions.

## Evidence And Boundaries

Fetch succeeded against https://github.com/mattpocock/skills.git. Upstream main
is dated 2026-09-29 and merges release/v1.3; upstream package.json still declares
1.2.3, so the branch title does not establish a published 1.3 package version.
Current branch and installed skills were not changed. Local main was not moved.
The dry-run conflict result is expected evaluation evidence, not a failed
installation. No runtime tests were needed for this documentation-only review.
Graph-memory disposition: not_durable; this source-backed evaluation is retained
here and is tied to these exact tips, rather than written as a lasting runtime
fact.
