## What it does

`pr` helps write a concise Markdown pull request body: the concrete problem and resulting behavior, observed validation, and material risk. It preserves the format ideas credited to Dex Horthy and Humanlayer in the skill metadata. It does not itself authorize pushing, opening, or merging a PR.

## Using it in Codex

Invoke `$pr` through the available Codex skill interface, or let the agent use it while writing a PR body. Read the repository template and instructions first. Required template fields win; use Summary, Evidence, and Merge Danger only where they fit. Use configured domain language, falling back to an existing `GLOSSARY.md` or legacy `CONTEXT.md`.

If both legacy and glossary files disagree without configuration, reconcile their authority before selecting terms; preserve both rather than overwriting one.

A small nonvisual change can use two sentences and its check result. Complex control flow may benefit from pseudocode, a call tree, a shaped diff, or Mermaid. Visuals and risk taxonomies are optional; they should clarify a consequential boundary instead of making every PR longer.

## Evidence and risk

Report checks actually run and their outcomes, plus skipped checks or relevant limitations. Before/after evidence is useful when captured. Do not invent a failing baseline. Pseudocode explains a test but does not prove it ran. For a visual change, screenshots or a browser artifact can support the behavior claim.

Explain reversibility and affected consumers when material. Reverting a commit does not necessarily undo external effects. Keep risk proportional to the change and comply with any required repository risk fields.

## Remote artifact review

Use `$previews` for substantial review packets and visual artifacts. Publish related outputs in one session and return its browser URL to the user. The PR body stays self-contained: private reports and preview links inaccessible to public reviewers do not belong in a public PR. Use approval feedback only when the task requires approval. If Previews is unavailable, state the limitation and provide accessible Markdown or artifact locators.

With `gh`, write multiline bodies to a file and pass `--body-file`, preserving actual newlines. Updating an existing PR or creating one follows existing authorization and repository policy.

## It is working if

- A reviewer can understand the problem and resulting behavior without conversation history.
- Evidence distinguishes observed outcomes from unexecuted checks.
- The body follows the repository template and scales to the change.
- Artifacts are accessible to their intended audience.

Use `code-review` to assess code and `retro` to learn from the session; `pr` describes the resulting change. Rewrite the body when the final implementation changes substantially.
