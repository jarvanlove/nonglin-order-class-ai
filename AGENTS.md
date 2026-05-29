# AGENTS.md

Bootstrap for Codex working in this repo.

This repo is bridged to a private ObsidianToWiki vault as a **read-only reference**.

## Wiki Bootstrap

- wiki_root: `C:\Work\note\ObsidianToWiki-private`
- project_repo_root: `C:\Work\note\CursorWorkSpace\nonglin-order-class-ai`
- project_slug: `nonglin-order-class-ai`
- access_mode: `read-consult`

## How To Start

1. Read this `AGENTS.md` as the Codex entrypoint.
2. Open `Home.md` and `标准自然语言话术清单.md` inside the wiki to learn the canonical commands.
3. When asked a domain question, search the wiki first:
   - `30_shared/` for reusable knowledge
   - `20_projects/active/*` for prior project decisions
4. Do not create project pages under `20_projects/active/nonglin-order-class-ai/` yet.
   This project is in **read-consult mode** until the user asks to upgrade.

## Upgrading To Full Onboarding

When the project starts producing durable artifacts (architecture, decisions, sources),
ask the user: "要把这个项目升级为完整 wiki 接入吗？"

If yes, follow `30_shared/prompts/项目首次接入提示词.md` and create the full
project page closure in the wiki.

## Local Project Control Files

For local repository work, Codex reads these project control files directly:

1. `PRODUCT_SPEC.md`
2. `ARCHITECTURE.md`
3. `TASKS.md`
4. `TESTING.md`
5. `DEPLOYMENT.md`
6. `OPERATIONS.md`

Codex execution rules:

- Treat this as a course/content/slides project.
- Before editing, state whether the task touches `content/`, `materials/`, or `slides/`.
- Keep curriculum, practice guide, rubric, and slides aligned.
- Do not write to the wiki unless explicitly asked by the user.
- Report which validation from `TESTING.md` was run or why it was skipped.
