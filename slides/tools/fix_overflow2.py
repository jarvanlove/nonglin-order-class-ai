import re

def fix_day01_aggressive():
    with open('slides/day01/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    head_end = html.find('</style>') + len('</style>')
    head = html[:head_end]
    body = html[head_end:]

    # === Aggressive CSS compressions in head ===
    reps_head = [
        # Shrink header bars to give more space to content
        (r'(\.obj-header-bar \{[^}]*?height:) 180pt;', r'\1 140pt;'),
        (r'(\.obj-content \{[^}]*?top:) 180pt;', r'\1 140pt;'),
        (r'(\.intro-header-bar \{[^}]*?height:) 130pt;', r'\1 105pt;'),
        (r'(\.intro-content \{[^}]*?top:) 130pt;', r'\1 105pt;'),
        # Reduce section header margin
        (r'(\.section-header-bar \{[^}]*?margin-bottom:) var\(--space-6\);', r'\1 var(--space-4);'),
        # More compact content blocks
        (r'(\.content-block \{[^}]*?padding:) var\(--space-4\);', r'\1 var(--space-3);'),
        (r'(\.content-block h3 \{[^}]*?margin-bottom:) var\(--space-3\);', r'\1 var(--space-2);'),
        (r'(\.content-block p \{[^}]*?margin: 0 0 )var\(--space-3\)( 0;)', r'\1 var(--space-2)\2'),
        (r'(\.content-block ul li \{[^}]*?margin-bottom:) var\(--space-2\);', r'\1 var(--space-1);'),
        (r'(\.key-point \{[^}]*?padding:) var\(--space-3\) var\(--space-4\);([^}]*?margin-top:) var\(--space-3\);', r'\1 var(--space-2) var(--space-3);\2 var(--space-2);'),
        # More compact task/practice
        (r'(\.task-card \{[^}]*?padding:) var\(--space-4\);', r'\1 var(--space-3);'),
        (r'(\.task-card h3 \{[^}]*?margin-bottom:) var\(--space-3\);', r'\1 var(--space-2);'),
        (r'(\.task-card p \{[^}]*?margin: 0 0 )var\(--space-3\)( 0;)', r'\1 var(--space-2)\2'),
        (r'(\.practice-card \{[^}]*?padding:) var\(--space-4\);', r'\1 var(--space-3);'),
        (r'(\.practice-card h3 \{[^}]*?margin-bottom:) var\(--space-3\);', r'\1 var(--space-2);'),
        (r'(\.tip-box \{[^}]*?padding:) var\(--space-3\) var\(--space-4\);', r'\1 var(--space-2) var(--space-3);'),
        (r'(\.warning-box \{[^}]*?padding:) var\(--space-3\) var\(--space-4\);', r'\1 var(--space-2) var(--space-3);'),
        (r'(\.time-control \{[^}]*?padding:) var\(--space-3\) var\(--space-4\);', r'\1 var(--space-2) var(--space-3);'),
        (r'(\.deliverable-box \{[^}]*?padding:) var\(--space-3\) var\(--space-4\);', r'\1 var(--space-2) var(--space-3);'),
        # More compact end page
        (r'(\.end-summary \{[^}]*?padding:) var\(--space-4\);([^}]*?margin-bottom:) var\(--space-6\);', r'\1 var(--space-3);\2 var(--space-4);'),
        (r'(\.end-summary h3 \{[^}]*?margin-bottom:) var\(--space-3\);', r'\1 var(--space-2);'),
        (r'(\.end-summary li \{[^}]*?margin-bottom:) var\(--space-2\);', r'\1 var(--space-1);'),
        (r'(\.end-next \{[^}]*?padding:) var\(--space-3\) var\(--space-4\);', r'\1 var(--space-2) var(--space-3);'),
        # Reduce gaps further
        (r'(\.content-two-col \{[^}]*?gap:) var\(--space-4\);', r'\1 var(--space-3);'),
        (r'(\.content-col \{[^}]*?gap:) var\(--space-3\);', r'\1 var(--space-2);'),
        (r'(\.task-layout \{[^}]*?gap:) var\(--space-4\);', r'\1 var(--space-3);'),
        (r'(\.task-main \{[^}]*?gap:) var\(--space-3\);', r'\1 var(--space-2);'),
        (r'(\.task-sidebar \{[^}]*?gap:) var\(--space-3\);', r'\1 var(--space-2);'),
        (r'(\.practice-layout \{[^}]*?gap:) var\(--space-4\);', r'\1 var(--space-3);'),
        (r'(\.practice-col \{[^}]*?gap:) var\(--space-3\);', r'\1 var(--space-2);'),
        # Smaller obj/intro card gaps
        (r'(\.cards-row \{[^}]*?gap:) 10pt;', r'\1 8pt;'),
        (r'(\.intro-layout \{[^}]*?gap:) 12pt;', r'\1 10pt;'),
        # Reduce obj-card and intro-card padding further
        (r'(\.obj-card \{[^}]*?padding:) 10pt;', r'\1 8pt;'),
        (r'(\.intro-card \{[^}]*?padding:) 10pt;', r'\1 8pt;'),
        (r'(\.obj-card h3 \{[^}]*?margin-bottom:) 6pt;', r'\1 4pt;'),
        (r'(\.intro-card h3 \{[^}]*?margin-bottom:) 6pt;', r'\1 4pt;'),
        (r'(\.obj-card \.highlight-box \{[^}]*?padding:) 6pt 8pt;', r'\1 4pt 6pt;'),
        # Step list tighter
        (r'(\.step-list li \{[^}]*?margin-bottom:) var\(--space-3\);', r'\1 var(--space-2);'),
        # Font-size override for all text in content areas (not titles)
        # We inject a rule at the end of the style block
    ]
    for pat, repl in reps_head:
        head = re.sub(pat, repl, head)

    # Inject font-size reduction for body text inside slides
    # Add before </style>
    font_override = """
  /* === overflow fix: reduce body text size === */
  .obj-card li, .intro-card p, .content-block p, .content-block li, .task-card p, .practice-card p, .end-summary li, .step-text, .tip-box p, .warning-box p, .time-control p, .deliverable-box p { font-size: 10.5pt; }
  .key-point p { font-size: 10.5pt; }
  .obj-card .highlight-box p, .intro-card .highlight-box p { font-size: 9pt; }
"""
    head = head.replace('</style>', font_override + '</style>')

    # === Body inline style replacements ===
    # Remaining line-height: 1.8
    body = body.replace('line-height: 1.8;', 'line-height: 1.45;')
    # Remaining padding: 20pt 32pt (should be gone, but just in case)
    body = body.replace('padding: 20pt 32pt;', 'padding: 12pt 20pt;')
    # Any remaining large margins
    body = body.replace('margin-bottom: var(--space-4);', 'margin-bottom: var(--space-3);')
    body = body.replace('margin-top: var(--space-4);', 'margin-top: var(--space-3);')
    body = body.replace('padding: var(--space-5);', 'padding: var(--space-4);')
    body = body.replace('gap: var(--space-6);', 'gap: var(--space-4);')

    with open('slides/day01/index.html', 'w', encoding='utf-8') as f:
        f.write(head + body)
    print('day01 aggressive fix done')


def fix_day06_aggressive():
    with open('slides/day06/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    reps = [
        (r'(\.card \{[^}]*?padding:) 4pt 6pt;', r'\1 3pt 5pt;'),
        (r'(\.card h3 \{[^}]*?margin-bottom:) 2pt;', r'\1 1pt;'),
        (r'(\.hint-box \{[^}]*?padding:) 3pt 6pt;', r'\1 2pt 4pt;'),
        (r'(\.roadmap-wrap \{[^}]*?margin-bottom:) 6pt;', r'\1 4pt;'),
        (r'(\.roadmap-item \{[^}]*?padding:) 5pt;', r'\1 4pt;'),
        (r'(\.factor-card \{[^}]*?padding:) 4pt 6pt;', r'\1 3pt 5pt;'),
        (r'(\.redline-card \{[^}]*?margin-bottom:) 4pt;', r'\1 3pt;'),
        (r'(\.award-card \{[^}]*?margin-bottom:) 3pt;', r'\1 2pt;'),
        (r'(\.timeline-item \{[^}]*?margin-bottom:) 4pt;', r'\1 3pt;'),
        (r'(\.layer-item \{[^}]*?padding:) 4pt 8pt;', r'\1 3pt 6pt;'),
        (r'(\.task-card \{[^}]*?padding:) 8pt 10pt;', r'\1 6pt 8pt;'),
        (r'(\.prompt-box \{[^}]*?padding:) 4pt 6pt;', r'\1 3pt 5pt;'),
        (r'(\.prompt-box p \{[^}]*?line-height:) 1\.35;', r'\1 1.25;'),
        (r'(\.compare-table th \{[^}]*?padding:) 2pt 4pt;', r'\1 1pt 3pt;'),
        (r'(\.compare-table td \{[^}]*?padding:) 2pt 4pt;', r'\1 1pt 3pt;'),
        # Slightly smaller text for cards
        (r'(\.card p, \.card li \{[^}]*?font-size:) 9pt;', r'\1 8.5pt;'),
        (r'(\.card p, \.card li \{[^}]*?line-height:) 1\.35;', r'\1 1.25;'),
        # Tighter bullet list
        (r'(\.bullet-list li \{[^}]*?padding-left:) 14pt;', r'\1 12pt;'),
    ]
    for pat, repl in reps:
        html = re.sub(pat, repl, html)

    # Target slide 4: compress the two-col height calc and screenshot min-height
    html = html.replace('height:calc(100% - 90pt)', 'height:calc(100% - 102pt)', 1)

    with open('slides/day06/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('day06 aggressive fix done')


if __name__ == '__main__':
    fix_day01_aggressive()
    fix_day06_aggressive()
