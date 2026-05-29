# Operations

## Working Modes

- Course authoring: edit `content/` and `materials/`.
- Slide production: edit or regenerate `slides/`.
- Instructor preparation: read README, design spec, lesson plans, and instructor/practice guides.
- Teacher reuse: use `content/llm-wiki-lecture/` plus selected Day 1/3/6/7 content.

## Common Issues

| Symptom | Check | Fix |
|---|---|---|
| Slide text overflows | affected day deck, overflow scripts | Adjust slide content/CSS and rerun targeted check |
| Content and slides disagree | `content/day0X-*` vs `slides/day0X*` | Update one side and record affected files |
| Instructor guide outdated | `materials/instructor-manual.md` and lesson plans | Sync operational steps with current day content |
| Practice violates tool policy | README constraints and affected practice file | Replace with allowed domestic-tool workflow |
| Teacher reuse module drifts | `content/llm-wiki-lecture/` | Update teacher-specific module separately from student course |

## Evidence Artifacts

- Screenshots under `slides/_screenshots/` can be used as visual evidence.
- Overflow reports under `slides/overflow_report*.md` document slide QA results.
- Generated outputs under `outputs/` should be treated as artifacts, not canonical source.

## Maintenance Rules

- Keep source content and generated outputs conceptually separate.
- Prefer targeted updates over global rewrites.
- When changing the course promise, update README and `PRODUCT_SPEC.md`.
- When changing assessment, update rubric and relevant project templates.
