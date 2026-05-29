# Architecture

## Repository Shape

This is a curriculum, training-material, and HTML slide project.

| Area | Owns |
|---|---|
| `content/` | 6-day lesson content, daily theory/practice, slide outlines |
| `materials/` | student handbook, instructor guide, practice guide, rubric, templates |
| `slides/` | HTML slide decks, shared styles, generation/repair/export scripts, screenshots |
| `outputs/` | generated outputs and exports |

## Content Boundaries

- `content/day0X-*` is the canonical daily teaching content.
- `materials/practice-guide.md` and `materials/instructor-manual.md` are operational teaching guides.
- `materials/project-rubric*.md` is the assessment source.
- `slides/` renders selected teaching content visually and must stay aligned with outlines.
- `content/llm-wiki-lecture/` is reusable teacher-training content.

## Slide System

- Main generated decks: `slides/day01.html` through `slides/day06.html`.
- Per-day modular decks: `slides/day0X/`.
- Shared tokens/components: `slides/shared/`.
- Generation and repair scripts live under `slides/` and `slides/tools/`.
- Screenshots under `slides/_screenshots/` are evidence artifacts, not source content.

## Invariants

- Practice stage forbids foreign AI tools and VPN use.
- Theory can discuss global tools for perspective.
- Keep one unified learner track.
- QClaw / WorkBuddy / Trae are teaching carriers, not career-standard claims.
- Course changes must preserve employment-oriented output and project roadshow.

## Change Rule

When changing content, identify whether the change impacts:

- daily lesson content
- instructor operations
- student materials
- slides
- project rubric
- teacher-reuse module

If it affects more than one area, update all affected files or add a task to `TASKS.md`.
