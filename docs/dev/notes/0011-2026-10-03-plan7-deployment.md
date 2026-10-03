# Plan 7 adoption and deployment receipt

## Outcome

Upstream d81f3a183412e71a5b1e84ca21bc1a35eea03a60 is integrated. Adapted pr/retro are promoted; curated membership is 27. Codex remote routing, Previews delivery, legacy/configured glossary compatibility and our conflict-resolution/implement-spec carry are retained. Source checkpoint b39275882a557513b322aaa15802c2d628df59a1 contains adaptations and source-backed trial receipts.

## Installation and discovery

Permanent checkout: /home/ecochran76/workspace.local/mapocock.skills on eco/plan7. Publisher checks pass for ~/.agents/skills and ~/.codex/shared/skills; ~/.codex/skills resolves consistently. Independently verified all 27 links against source and zero broken links across all three roots. pr/retro were newly added, so no old entries were replaced; unchanged symlink targets retain source recovery through backup/eco-main/2026-10-03-pre-plan7 at f99b249.

Fresh codex exec session 01a10274-0d43-7f53-8862-23570227329d discovered pr in its model-visible catalog and explicitly loaded retro/implement-spec from installed source. Model-visible catalog omission for explicit-only skills did not prove an installation failure.

Independent fresh codex app-server stdio skills/list request with forceReload=true returned enabled user-scope entries mattpocock-skills:pr, mattpocock-skills:retro and mattpocock-skills:implement-spec, with exact permanent source SKILL.md paths. Combined client discovery, YAML invocation policy and actual explicit instruction loading prove intended discovery/invocation boundaries. Raw local readback: /tmp/mapocock-plan7-client-skills.json; fresh instruction-loading output: /tmp/mapocock-plan7-fresh-catalog.md. The one-shot app-server was terminated after readback.

## Validation summary

Metadata, relative links, shell syntax, plugin version/strict compatibility, planning audit and publisher semantic contracts pass. Selector suite: 124 tests pass in a harness with the actual policy source; the earlier installed-layout failure is preserved in Note 0010. Actual implement-spec fixture trial and fresh skill exercises pass within declared limits. Primary independently reran integration acceptance and verified complete recovery bundle. Notes 0007–0010 preserve delegated handles, evidence and primary reconciliation.

Two simultaneous Codex workers, host restart recovery and provider/production execution were not tested and are not claimed. The trial did exercise actual Codex delegation, explicit isolation, concurrent shell work, failed/skipped-test gates, serial integration, ledger resume and recoverable cleanup. Nonblocking review suggestions for a named validation harness and CI remain backlog.

## Publication boundary

origin is CochranResearchGroup/skills, verified PUBLIC. Completed ordinary push to adoption/plan7 at b39275882a557513b322aaa15802c2d628df59a1; exact remote SHA readback matched. Remote eco/main remains 833ea53f222029ed62a07adcf087b4005724e251. Local upstream mirror main is d81f3a1. Acceptance session: https://previews.ecochran.dyndns.org/s/d0c06c7ed800. Preview session and artifact ingress return HTTP200 login pages, as expected for authenticated viewing; actual logged-in visual inspection is not claimed. MCP publication confirms the copied Markdown artifact family and external browser URL. Final documentation checkpoint is pushed and independently read back at closeout. No package release or tag is part of this adoption.

Memory disposition: not_durable; exact-run receipts and adoption authority are retained in committed repo artifacts rather than seeded as separate long-lived agent memory.
