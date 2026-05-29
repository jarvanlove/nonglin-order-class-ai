# Deployment

## Delivery Model

This project is delivered as files, not a hosted backend application.

Deliverables:

- Markdown course content under `content/`.
- Student/instructor materials under `materials/`.
- HTML slides under `slides/`.
- Generated exports under `outputs/` when needed.

## Local Preview

For slides, open the relevant HTML file in a browser:

```text
slides/index.html
slides/day01.html
slides/day02.html
slides/day03.html
slides/day04.html
slides/day05.html
slides/day06.html
```

If browser security affects local asset loading, serve the repository with a simple static server from the project root.

## Export

Use existing slide export/generation scripts only when the task requires regenerated artifacts:

```bash
python slides/export_pptx.py
python slides/generate_slides.py
```

Do not regenerate all decks for a narrow content edit unless necessary.

## Rollback

- Revert the specific content/material/slide files changed.
- If generated screenshots or exports were produced, remove only artifacts from the current change.
- Reopen affected slide deck and re-check navigation/overflow.

## Release Checklist

- README still describes the course accurately.
- `content/`, `materials/`, and `slides/` are aligned.
- Student-facing files do not reference forbidden practice tools.
- Instructor guide matches the latest lesson plan.
