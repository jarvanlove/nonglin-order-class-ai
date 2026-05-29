# Product Spec

## Product

- Name: 农林高校 AI 工具实训课程.
- Target users: agricultural/forestry university graduating students, mixed technical and non-technical background, around 30 learners.
- Core problem: students need practical domestic AI tool skills, AI ecosystem awareness, and portfolio-ready project experience for employment.
- Promise: deliver a 6-day, employment-oriented AI tools training course with theory, hands-on practice, project sprint, roadshow, and teacher-reusable modules.

## Current Scope

Must have:

- 6-day course structure with morning theory and afternoon practice.
- QClaw, WorkBuddy, and Trae as teaching carriers.
- Student handbook, instructor/practice guide, project rubric, and templates.
- HTML slide decks for each course day.
- LLM-Wiki lecture module for later teacher training reuse.
- Constraints around domestic tools during practice.

Explicitly not doing unless added to `TASKS.md`:

- Splitting students into A/B tracks.
- Replacing the domestic practice-tool requirement.
- Adding foreign AI tools into practice sessions.
- Turning this repository into a software application.
- Changing the 6-day duration or target audience without updating course scope and materials.

## Core Delivery Flows

### Student training delivery

- Entry: instructor prepares with README, design spec, lesson plans, and slides.
- Steps: daily theory -> guided practice -> project sprint -> polish -> roadshow.
- Success: students complete project artifacts and can explain tool workflow in employment context.

### Instructor preparation

- Entry: `materials/instructor-manual.md`, lesson plans, day content, and slide decks.
- Steps: review objectives -> rehearse demo -> prepare tools/accounts -> run class.
- Success: instructor can teach without improvising core structure.

### Teacher reuse course

- Entry: `content/llm-wiki-lecture/lecture-standard.md` and selected modules.
- Steps: reorganize Day 1/3/6 content into teacher-facing 2-3 day training.
- Success: teacher course reuses validated modules without breaking student course.

## Acceptance Criteria

- Any content change identifies affected `content/`, `materials/`, and `slides/` files.
- Any slide change checks visual overflow or explains why not run.
- Any course-scope change updates this file and relevant plans/specs.
- Student-facing and instructor-facing materials remain consistent.
- Practice sessions continue to avoid foreign AI tools and VPN use.

## Change Log

| Date | Change | Reason | Impact |
|---|---|---|---|
| 2026-05-19 | Added project-level AI control spec | Make course/slides work scoped and verifiable | Documentation/control-plane only |
| 2026-05-20 | Confirmed current course scope as 6 days | Remove legacy seventh-day scope and align materials | Content/slides/docs cleanup |
