# CLAUDE.md

This workspace is bridged to the private ObsidianToWiki vault for read-only consultation.

When you start working in this repo, treat the wiki as the project memory layer.
Read the entries below before answering domain questions or making durable decisions.

## Wiki Bootstrap

- wiki_root: `C:\Work\note\ObsidianToWiki-private`
- project_repo_root: `C:\Work\note\CursorWorkSpace\nonglin-order-class-ai`
- project_slug: `nonglin-order-class-ai`
- access_mode: `full`  # 已创建项目页闭环，可读写 wiki

## Default Wiki Entry Points

Use these as the read-first entry points:

- wiki_home: `Home.md`
- wiki_quickstart: `快速开始.md`
- wiki_phrasebook: `标准自然语言话术清单.md`
- wiki_session_start: `会话启动页.md`
- default_project_index: `20_projects/索引.md`
- default_shared_index: `30_shared/索引.md`
- default_personal_index: `10_personal/索引.md`
- default_output_index: `40_outputs/索引.md`

## Project Pages (not yet created)

This project has not yet built its wiki page closure under `20_projects/active/nonglin-order-class-ai/`.
When the project accumulates durable content (architecture decisions, sources, tasks),
upgrade to full onboarding by creating:

- `20_projects/active/nonglin-order-class-ai/索引.md`
- `20_projects/active/nonglin-order-class-ai/概览.md`
- `20_projects/active/nonglin-order-class-ai/架构.md`
- `20_projects/active/nonglin-order-class-ai/决策.md`
- `20_projects/active/nonglin-order-class-ai/任务.md`
- `20_projects/active/nonglin-order-class-ai/来源.md`
- `20_projects/active/nonglin-order-class-ai/关系.md`
- `20_projects/active/nonglin-order-class-ai/风险.md`
- `20_projects/active/nonglin-order-class-ai/时间线.md`
- `20_projects/active/nonglin-order-class-ai/project.memory.md`

To upgrade, follow `30_shared/prompts/项目首次接入提示词.md` in the wiki.

## Working Rules

- Treat the wiki as **read-only reference** until project pages are created.
- Search the wiki (`30_shared/`, `20_projects/active/*`) before reinventing solutions
  that may already exist in other projects.
- When a reusable pattern shows up, mention it instead of duplicating logic.
- Do not write back to the wiki under `access_mode: read-consult` unless the user
  explicitly asks "把这次结论记下来" or "帮我升级为完整接入".
- Project deliverables stay in this repo; durable cross-project knowledge belongs in `30_shared/`.

## Local Project Control Files

This repository is a course-content and slide-delivery project, not an application codebase. For local work, read these files before changing durable content:

1. `PRODUCT_SPEC.md`
2. `ARCHITECTURE.md`
3. `TASKS.md`
4. `TESTING.md`
5. `DEPLOYMENT.md`
6. `OPERATIONS.md`

Rules:

- Do not change the 6-day course scope without updating `PRODUCT_SPEC.md`.
- Do not modify slides without running the relevant visual/overflow checks from `TESTING.md` where practical.
- Keep student-facing materials, instructor materials, slides, and content outlines aligned.
- Wiki writeback remains governed by the access-mode rules above; local control files do not imply automatic wiki writes.
