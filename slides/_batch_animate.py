import os
import glob

# Unified entrance animation CSS block
ANIMATION_CSS = """
/* ===== Unified Entrance Animation ===== */
.content > *, .hero > * {
  opacity: 0;
  transform: translateY(12px) scale(0.98);
  animation: slideInUp 0.55s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}
.content > *:nth-child(1), .hero > *:nth-child(1) { animation-delay: 0.04s; }
.content > *:nth-child(2), .hero > *:nth-child(2) { animation-delay: 0.10s; }
.content > *:nth-child(3), .hero > *:nth-child(3) { animation-delay: 0.16s; }
.content > *:nth-child(4), .hero > *:nth-child(4) { animation-delay: 0.22s; }
.content > *:nth-child(5), .hero > *:nth-child(5) { animation-delay: 0.28s; }
.content > *:nth-child(6), .hero > *:nth-child(6) { animation-delay: 0.34s; }
.content > *:nth-child(7), .hero > *:nth-child(7) { animation-delay: 0.40s; }
.content > *:nth-child(8), .hero > *:nth-child(8) { animation-delay: 0.46s; }
.content > *:nth-child(9), .hero > *:nth-child(9) { animation-delay: 0.52s; }
.content > *:nth-child(10), .hero > *:nth-child(10) { animation-delay: 0.58s; }
.content > *:nth-child(11), .hero > *:nth-child(11) { animation-delay: 0.64s; }
.content > *:nth-child(12), .hero > *:nth-child(12) { animation-delay: 0.70s; }

@keyframes slideInUp {
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}
"""

processed = 0
skipped = 0
errors = 0

files = sorted(glob.glob("slides/day*/*.html"))
print(f"Found {len(files)} slide files.")

for path in files:
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Skip if already has keyframe animations
        if "@keyframes" in content:
            skipped += 1
            continue

        # Skip if already has the unified animation
        if "slideInUp" in content:
            skipped += 1
            continue

        # Find the last </style> tag and insert before it
        if "</style>" not in content:
            errors += 1
            print(f"  WARN: no </style> found in {path}")
            continue

        # Insert animation CSS before the last </style>
        idx = content.rfind("</style>")
        new_content = content[:idx] + ANIMATION_CSS + content[idx:]

        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)

        processed += 1
        print(f"  OK: {path}")

    except Exception as e:
        errors += 1
        print(f"  ERR: {path} -> {e}")

print(f"\nDone: {processed} processed, {skipped} skipped, {errors} errors.")
