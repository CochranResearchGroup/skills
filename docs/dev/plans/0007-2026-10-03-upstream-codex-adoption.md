# Upstream Adoption for Codex Remote

Status: OPEN
- Owner: primary agent
- Fork: eco/main at 833ea53f222029ed62a07adcf087b4005724e251
- Upstream reviewed: d81f3a183412e71a5b1e84ca21bc1a35eea03a60
- Outcome: current upstream workflows adapted for Codex remote, installed locally and published to our fork

## Current State

Preparation and isolated upstream rebase are complete on adoption/plan7. The candidate includes pr/retro promotion, glossary compatibility, Codex routing and retained downstream contracts. Source and fixture validation pass; independent review, final installation, fresh catalog discovery, Previews delivery and candidate publication remain.

Recovery: backup/eco-main/2026-10-03-pre-plan7 at f99b249. The fork is PUBLIC; policy therefore requires ordinary publication to adoption/plan7 rather than a force-push over eco/main. Local eco/main and remote eco/main remain preserved. Selected upstream remains d81f3a183412e71a5b1e84ca21bc1a35eea03a60.

## Scope

Integrate the reviewed upstream source, adopt pr and retro, update glossary conventions and routing, preserve our Codex policies and curated publication, validate and install the result, then publish our fork. Preserve Matt's engineering workflows; change harness assumptions and remote artifact delivery rather than adding redundant approval rules.

No changes to other repositories' instructions or glossary files, no fleet rollout, no live product operations, no unrelated policy upgrade, and no new release tags or package release.

## Five Steps

| Step | Work | Done when |
| --- | --- | --- |
| 1. Prepare | Refresh upstream/origin, inspect branch/worktree ownership, preserve untracked work and create a dated recovery ref. Record the exact selected upstream tip and remote destination. Freeze the downstream contracts listed below. | Inputs and recovery are recorded; no work can be lost. |
| 2. Integrate upstream | Rebase the fork carry onto the selected upstream in an isolated candidate checkout. Resolve by intent; retain our conflict-resolution skill and adapted implement-spec. Advance the local upstream mirror only when its checkout is safe. | Selected upstream is an ancestor and downstream contracts survive. |
| 3. Adapt for Codex | Promote pr and retro, add glossary compatibility, update ask-matt, metadata, publisher, indexes and docs together. Use available Codex tools and Previews for remote artifact review. | All promoted skills, routes and docs agree; expected curated count is 27. |
| 4. Validate and review | Run source checks and bounded workflow trials. Publish one acceptance packet through Previews with exact commits, results and remaining limitations. | Acceptance below passes or each incomplete criterion is explicitly blocked. |
| 5. Install and publish | Checkpoint validated source, publish both local skill roots with backups, verify actual links and a fresh Codex catalog, then push the fork using the established branch policy. Verify remote SHA and close this plan. | Source, installed catalog and remote readback match; recovery remains available. |

## Codex Adaptation Rules

- AGENTS.md and configured repo authorities govern Codex; preserve CLAUDE.md where it remains upstream compatibility material.
- Replace Claude Skill-tool calls, session-log assumptions, background commands and context-reset instructions with capabilities actually available in Codex. Detect worker isolation rather than assuming it.
- Accept repo-native plans/tickets and local validated branches. Existing authorization governs routine fixes, commits and external actions; do not introduce approval gates merely because a skill was adopted.
- Use Previews for substantial Markdown review packets, HTML, PDFs, Office files and image artifacts. Group outputs into one session and return its browser URL. Use feedback only when approval is actually required. If unavailable, state the fallback.
- Respect artifact audience: do not expose private reports or inaccessible preview links through public PRs. Artifact delivery is separate from runtime correctness.

## Exact Adoption Decisions

- pr: promote; retain attribution, concise concrete explanation, evidence and relevant risk. Respect repository PR templates; diagrams are optional and evidence must be observed.
- retro: promote; use supplied Codex conversation/log evidence and locate unknown external files through file-searcher. Prefer deterministic improvements. Implement recommendations only within existing task scope; publish substantial findings through Previews.
- GLOSSARY.md/GLOSSARY-MAP.md: use for new unconfigured repos; respect configured authority and existing CONTEXT.md/CONTEXT-MAP.md. Update format references, setup templates, docs and consumers together. Avoid duplicate authorities and implicit fleet renames.
- ask-matt: route the promoted skills through the supported Codex invocation interface, with remote artifact delivery.
- misc exclusion: accept the upstream dev-linker change; keep our curated publisher authoritative.
- resolving-merge-conflicts: retain our intent, recovery and safe-abort behavior despite upstream deletion.
- implement-spec: retain the adopted version and complete its execution trial; keep implement excluded. Other in-progress/misc skills remain unpromoted.

## Validation And Acceptance

Source checks: parse all skill frontmatter and Codex metadata; validate plugin manifest/version, relative links, shell syntax, promoted membership and publisher semantic contracts. Run the existing repo-policy selector suite and applicable planning checks. Verify that Codex discovery, runtime proof, previews, repo-native planning, bounded review and commit authority survived reconciliation.

Behavioral checks: exercise pr on a small nonvisual change and an artifact-producing change; ensure useful evidence without forced diagrams. Exercise retro on supplied Codex evidence; ensure recommendations are source-backed and no unrelated global edits occur. Exercise glossary lookup with legacy, new and explicitly configured authorities.

For implement-spec, use a disposable fixture repo with two independent tickets and one dependent ticket. Verify worker cwd/write ownership, concurrency limits, serial integration and unlocking only after validated blockers. Inject one worker failure and one skipped required test; neither may unlock dependents. Resume from the ledger, preserve valid work and confirm bounded review and recoverable cleanup. Record actual runtime/tool limitations; static text checks are not behavioral proof.

Installation checks: publisher --check passes in ~/.agents/skills and ~/.codex/shared/skills; ~/.codex/skills resolves consistently. Confirm fresh-session discovery including explicit invocation of implement-spec and retro. Verify 27 promoted skills; retain backups of replaced entries.

Publication checks: verify origin belongs to our fork, inspect current remote tip and record exact published branch/SHA. The planned rebase rewrites history: use force-with-lease only after confirming the destination is owned, private and rebase-managed as policy requires. If that condition cannot be established, publish a new ordinary candidate branch and leave the existing branch untouched, reporting the integration gate. Do not force-push merely to finish.

## Execution And Recovery

Primary agent owns integration. pr and retro adaptations may be delegated to disjoint workers after upstream integration; glossary/routing/manifest changes remain serialized under one owner. Worker trials use isolated fixture write scopes. Parallel execution is optional where runtime capacity or benefit is absent.

Preserve a recovery ref before history changes and backup installed entries before replacement. On failed semantic checks, abort or rebuild from preserved inputs rather than favoring one side blindly. If deployment checks fail, restore affected installation entries. Preserve valid evidence and record the exact remaining gate.

## Definition Of Done

All five steps complete, acceptance evidence is attached to exact source and installed identities, one Previews packet is delivered, our fork's published SHA is verified, and this plan is CLOSED. Full upstream adoption is not complete merely because files merge or installation checks pass.

Execution authorized by the user on 2026-10-03. Preparation is in progress.
