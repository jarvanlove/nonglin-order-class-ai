# Testing

## Content Validation

For content-only changes:

- Check affected day files in `content/`.
- Check related instructor/student materials in `materials/`.
- Check whether slide outlines or decks need updates.
- Verify the change does not violate domestic-tool practice constraints.

## Slide Validation

Available scripts observed in the repository:

```bash
python slides/tools/analyze_ppt.py
python slides/tools/check_overflow_strict.py
python slides/tools/check_overflow_v2.py
python slides/tools/check_overflow_v3.py
python slides/tools/check_overflow_v4.py
python slides/check_overflow.py
python slides/check_overflow_v2.py
python slides/generate_slides.py
python slides/export_pptx.py
```

Use the narrowest script that matches the task. If a script expects local browser/Python dependencies that are not installed, state the blocker and perform a manual browser check of the affected `slides/*.html`.

## Minimum Verification Matrix

| Change type | Required checks |
|---|---|
| Daily content | Related `content/day0X-*` read-through and consistency with README |
| Student/instructor material | Cross-check with affected day content and rubric |
| Slide HTML/CSS | Browser check plus overflow script where practical |
| Slide data/generation script | Regenerate or run targeted script, then visual check |
| Course scope/rubric | Update `PRODUCT_SPEC.md`, relevant materials, and README if needed |

## Manual Smoke Tests

- Open `slides/index.html` or the affected day deck in a browser.
- Navigate next/previous slides.
- Check speaker/overview mode if the deck supports it.
- Inspect long text, footers, and mobile/viewport scaling when relevant.

## Completion Rule

Report exactly which content files and slide decks were checked. Do not claim slide quality without a visual or script-based check.
