# CLAUDE.md

Guidance for AI assistants working in this repository.

## What this repository is

`mostafadriouiche/mostafadriouiche` is a **GitHub profile repository**. Because the
repository name matches the owner's username, GitHub renders its `README.md` at the
top of the owner's public profile page (https://github.com/mostafadriouiche).

There is no application code, build system, dependency manifest, test suite, or CI
configuration. The repository's only "product" is the rendered profile README.

## Structure

```
.
├── README.md   # Profile content shown on the GitHub profile page
└── CLAUDE.md   # This file (AI assistant guidance; not shown on the profile)
```

### README.md

- Built from GitHub's default profile template: a bulleted list of emoji-prefixed
  lines (interests, learning, collaboration, contact, pronouns, fun fact).
- Current stated focus: **data analytics** (interested in it, currently learning it).
- Several template lines are still unfilled placeholders (`...` or trailing
  "I'm looking to collaborate on" with no value). Only fill these with content the
  owner provides — never invent contact details, pronouns, or personal facts.
- Ends with an HTML comment (`<!--- ... --->`) explaining the special profile
  repository behavior. It is invisible on the rendered page; leave it unless asked
  to remove it.

## Development workflow

- **No build, lint, or test commands exist.** Changes are plain Markdown edits.
- To check how a change renders, view the file on GitHub (or use any
  GitHub-Flavored Markdown previewer). GitHub profile READMEs support GFM, inline
  HTML (sanitized), images, and badges; they do not run scripts or custom CSS.
- Changes go live on the profile as soon as they land on the default branch
  (`main`).

## Conventions for AI assistants

- Keep edits minimal and scoped to what was asked; this is a personal page, so tone
  and content are the owner's choice.
- Preserve the existing style (emoji-prefixed bullet list) unless asked to redesign.
- Do not fabricate personal information (emails, social links, pronouns, employers,
  projects). Ask the owner or leave the placeholder.
- External images/badges (e.g. GitHub stats cards, skill icons) are fine when
  requested; prefer stable, widely used sources and include alt text.
- Do not add tooling (package.json, workflows, etc.) unless explicitly requested —
  for example, a GitHub Action to auto-update the README would be a deliberate,
  owner-approved addition.
- Develop on the designated feature branch and do not open pull requests unless
  asked.
