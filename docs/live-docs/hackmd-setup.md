# HackMD-Style Setup for EDU498 Live Docs

This setup gives us a workflow that feels closer to Google Docs while keeping the repo as the long-term archive.

## Option A: Fastest workflow using HackMD

1. Create a new note in HackMD.
2. Copy the contents of `live-doc-template.md` or another Markdown file from this folder into the HackMD note.
3. Share the HackMD note link with collaborators.
4. Collaborate in HackMD using its live editor.
5. When the document is ready, export/copy the Markdown back into this folder.
6. Commit the updated `.md` file to GitHub.

This is the easiest workflow because everyone can edit in a browser without needing to use Git directly.

## Option B: Git-first workflow

1. Edit the `.md` files directly in GitHub.
2. Use pull requests for major changes.
3. Use GitHub history to track revisions.
4. Use GitHub Pages or MkDocs later if you want a polished website version.

This is less Google-Docs-like but has the cleanest version control.

## Option C: Wiki.js later

Wiki.js is the stronger long-term option if we want:

- user accounts and permissions,
- a cleaner wiki interface,
- search,
- navigation menus,
- Git-backed storage,
- and a more polished editing experience.

It requires hosting, so it is better as a later step after the Markdown workflow is stable.

## Recommended EDU498 workflow

Use HackMD for live collaboration and GitHub for final storage:

```text
HackMD note -> final Markdown -> GitHub repo -> optional PDF / website export
```

## Naming convention

Use clear filenames:

```text
class8-mini-unit-live.md
class9-reading-response-live.md
final-project-guide-live.md
```

When a document is final, remove `-live` or copy it into the appropriate module folder.

## Rule for source of truth

During active collaboration, HackMD is the working draft.

After submission or final revision, GitHub is the source of truth.
