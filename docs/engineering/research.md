## What it does

`research` answers a question by reading the sources that own the answer, then leaves a cited Markdown file in the repo. It works only from **[primary sources](https://www.aihero.dev/ai-coding-dictionary/primary-source)**: official docs, source code, specs, first-party APIs. It follows every claim back to the source that owns it, so it will not repeat a blog post's account of an API when the API's own docs are reachable.

It does not answer you in the conversation. The output is a file, written where the repo already keeps such notes, with a link on each claim. That is the point: a document you can react to, hand to another agent, or throw away, rather than an answer that vanishes when the [session](https://www.aihero.dev/ai-coding-dictionary/session) ends.

## When to reach for it

Type `/research`, or the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) reaches for it automatically when a task turns into reading legwork.

Reach for it when the next step is *finding something out* from outside the working directory (how a third-party API behaves, what a spec actually says, whether a version claim holds), and you'd rather not stall your own thread doing the reading. What you need decides which skill:

| What you need | Reach for |
| --- | --- |
| An external fact a decision is waiting on | `research` |
| A decision made *with* you, by interview | [grilling](https://aihero.dev/skills-grilling) |
| A durable architecture decision, written into `CONTEXT.md` and ADRs | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| To find out whether an approach works in your codebase | [prototype](https://aihero.dev/skills-prototype) |
| A plan too big to hold in one session | [wayfinder](https://aihero.dev/skills-wayfinder) |

The line between `research` and `grill-with-docs` is the **shelf life of what comes back**. Research produces short-lived assets: what this library's auth mechanism does as of this week. An ADR records a decision you keep. If what you are producing is a decision rather than a fact, you are [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling), not researching.

## Bounded legwork

The reading may run as a **background agent** when delegation is authorized, available, and useful off the critical path. Otherwise the primary performs the same bounded workflow locally. Research is legwork, not thinking you outsource: you get a document to grill, plan, or design against, and you still make the call.

A delegated researcher works directly and must not delegate again. Every run starts with an exact question, allowed primary-source classes, output path, and stopping criterion.

Where the file lands is decided by the repo, not by the skill: it matches whatever convention already exists for notes, and if there is none it picks somewhere sensible and tells you where. It writes one file per run.

## Common questions

**Should a delegated researcher spawn another research agent?**

No. The downstream skill explicitly tells a delegated worker to perform the research directly. If global or repo policy prohibits delegation, the primary runs the workflow locally instead of quietly doing nothing.

**Where should the file live, and should I commit it?**

The skill puts the file where the repo already keeps notes and does not have an opinion beyond that. The community one is fairly settled: ADRs are kept, research files are not. The sharpest version of it, from a Discord thread on exactly this question: "ADRs yes. Everything else archive or delete after done. It otherwise becomes cruft of work and can poison future repo reads if you've drifted away from the spec/research." A research file records what was true on the day it was written, so a stale one is worse than none. On balance these artifacts don't really belong in git, and there is no canonical home for them: people use Obsidian, a separate knowledge repo, or the issue tracker instead.

**What counts as a "high-trust" primary source, and who decides?**

The [model](https://www.aihero.dev/ai-coding-dictionary/model) does. The skill names the *kinds* of source that qualify (official docs, source code, specs, first-party APIs), and there is no allowlist, no domain gate, and no verification pass. This was the loudest objection when the skill was first proposed and it has never been answered publicly: "Five research subagents pointed at junk just gives you five confident wrong answers faster. How are you gating what counts as high-trust sources?" The mitigation you actually have is the citation on each claim. Follow two or three of them. If they land on a summary of the thing rather than the thing, the run failed at its one job.

**Does a later session reuse what an earlier run found?**

No. Nothing auto-loads a past research file; it is a document sitting in the repo until a human or a skill points at it. This was raised early as the strongest challenge to the design: "the value's the markdown becoming context the agent re-reads later, not the fetch itself. A write-once dead file is just a fancy search." The shipped skill does not solve it. In practice the file earns its keep by being fed into the next step deliberately: attach it to a spec, quote it into a grilling session, point a [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) at it.

**Why not just ask the agent to go read the docs?**

You can. What the skill adds is a bounded question, primary-source constraint, stopping criterion, and cited-file output that stay consistent whether the work runs locally or in the background. If a two-line prompt gets you what you need on a small question, use it.

**When does it stop reading?**

The run stops at its declared evidence or source bound. If the exact answer is still unavailable, it returns partial cited evidence and the missing source instead of widening the topic. A narrow, answerable question (one API, one behaviour, one version claim) remains much better than "research X".

**`/wayfinder` created research tickets. Do I resolve those myself?**

No, it now fires them for you. In the unreleased changes since v1.1, a charting session spawns a `/research` subagent per research ticket and burns them down in parallel, capturing findings on a throwaway `research/<name>` branch with a [context pointer](https://www.aihero.dev/ai-coding-dictionary/context-pointer) from the ticket. Research tickets are the one exception to wayfinder's one-ticket-per-session rule, because they are [AFK](https://www.aihero.dev/ai-coding-dictionary/afk): nothing waits on you. Two known snags with those branches: the subagent has been seen opening a draft PR from a branch that is never meant to merge ([issue #576](https://github.com/mattpocock/skills/issues/576)), and deleting the branch later breaks the context pointers the tickets hold.

## It's working if

- The exact question, source boundary, output path, and stopping criterion are visible before reading begins.
- If delegation is permitted, exactly one background task appears; otherwise the primary completes the same workflow locally.
- One new Markdown file shows up, in the folder the repo already uses for notes, and the agent tells you the path.
- Every claim in it carries a link, and following two at random lands you on an official doc, a spec, or the actual source file, not on someone's write-up of it.
- You can make the decision you were stuck on from the file alone, without going back to the sources yourself.

## Where it fits

A reach-for-it-anytime standalone that feeds the thinking skills rather than sitting in the build chain. Its file is something to take *into* the flow: [grilling](https://aihero.dev/skills-grilling) and [grill-with-docs](https://aihero.dev/skills-grill-with-docs) ask sharper questions when the facts are already on the table, and [to-spec](https://aihero.dev/skills-to-spec) can synthesise against it. [wayfinder](https://aihero.dev/skills-wayfinder) is the one skill that invokes it directly, resolving each research ticket on its map with a `/research` subagent. For the whole map, see [ask-matt](https://aihero.dev/skills-ask-matt).
