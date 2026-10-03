
## Domain authority compatibility

Use the repository's configured domain-document authority first. Otherwise use an existing GLOSSARY-MAP.md or CONTEXT-MAP.md and its relevant files; for a single glossary use existing GLOSSARY.md or CONTEXT.md. If both conventions exist without configured authority, reconcile their intent before editing rather than choosing by recency. For a new unconfigured repo, use GLOSSARY.md (and GLOSSARY-MAP.md only when multiple contexts require it). Read and update the selected authority; filename examples below do not authorize creating competing files or renaming other repos.

# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- **`GLOSSARY.md`** at the repo root, or
- **`GLOSSARY-MAP.md`** at the repo root if it exists: it points at one `GLOSSARY.md` per context. Read each one relevant to the topic.
- **`docs/adr/`**: read ADRs that touch the area you're about to work in. In multi-context repos, also check `src/<context>/docs/adr/` for context-scoped decisions.
- **`docs/dev/policies/`**: if present, read the relevant repo policy before changing plans, docs, runtime behavior, or validation expectations.
- **`docs/agents/codex-stack.md`**: if present, follow its Codex-specific discovery, runtime, and commit rules.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The `/domain-modeling` skill (reached via `/grill-with-docs` and `/improve-codebase-architecture`) creates them lazily when terms or decisions actually get resolved.

## File structure

Single-context repo (most repos):

```
/
├── GLOSSARY.md
├── docs/adr/
│   ├── 0001-event-sourced-orders.md
│   └── 0002-postgres-for-write-model.md
└── src/
```

Multi-context repo (presence of `GLOSSARY-MAP.md` at the root):

```
/
├── GLOSSARY-MAP.md
├── docs/adr/                          ← system-wide decisions
└── src/
    ├── ordering/
    │   ├── GLOSSARY.md
    │   └── docs/adr/                  ← context-specific decisions
    └── billing/
        ├── GLOSSARY.md
        └── docs/adr/
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `GLOSSARY.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Code discovery

If `docs/agents/codex-code-discovery.md` exists, read it before structural code exploration. Prefer graph tools for definitions, callers, callees, traces, and impact analysis when the repo advertises them.

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 (event-sourced orders): but worth reopening because…_
