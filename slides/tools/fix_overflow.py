import re

def fix_day01():
    with open('slides/day01/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    head_end = html.find('</style>') + len('</style>')
    head = html[:head_end]
    body = html[head_end:]

    # ========== HEAD CSS replacements ==========
    reps_head = [
        (r'(\.obj-content \{[^}]*?padding:) 20pt 32pt;', r'\1 12pt 20pt;'),
        (r'(\.cards-row \{[^}]*?gap:) 14pt;', r'\1 10pt;'),
        (r'(\.obj-card \{[^}]*?padding:) 14pt;', r'\1 10pt;'),
        (r'(\.obj-card \.card-icon \{[^}]*?margin-bottom:) 10pt;', r'\1 6pt;'),
        (r'(\.obj-card h3 \{[^}]*?margin-bottom:) 10pt;', r'\1 6pt;'),
        (r'(\.obj-card li \{[^}]*?line-height:) 1\.7;([^}]*?margin-bottom:) 6pt;', r'\1 1.45;\2 3pt;'),
        (r'(\.obj-card \.highlight-box \{[^}]*?padding:) 8pt 10pt;', r'\1 6pt 8pt;'),
        (r'(\.intro-content \{[^}]*?padding:) 20pt 32pt;', r'\1 12pt 20pt;'),
        (r'(\.intro-layout \{[^}]*?gap:) 20pt;', r'\1 12pt;'),
        (r'(\.intro-card \{[^}]*?padding:) 14pt;', r'\1 10pt;'),
        (r'(\.intro-card h3 \{[^}]*?margin-bottom:) 8pt;', r'\1 6pt;'),
        (r'(\.intro-card p \{[^}]*?line-height:) 1\.7;', r'\1 1.45;'),
        (r'(\.case-box \{[^}]*?padding:) 10pt 12pt;([^}]*?margin-top:) 8pt;', r'\1 6pt 8pt;\2 4pt;'),
        (r'(\.question-list li \{[^}]*?line-height:) 1\.8;([^}]*?margin-bottom:) 6pt;', r'\1 1.45;\2 3pt;'),
        (r'(\.content-two-col \{[^}]*?gap:) var\(--space-6\);([^}]*?height: calc\(100% - )50pt\);', r'\1 var(--space-4);\2 36pt);'),
        (r'(\.content-col \{[^}]*?gap:) var\(--space-5\);', r'\1 var(--space-3);'),
        (r'(\.content-block \{[^}]*?padding:) var\(--space-5\);', r'\1 var(--space-4);'),
        (r'(\.content-block h3 \{[^}]*?margin-bottom:) var\(--space-4\);', r'\1 var(--space-3);'),
        (r'(\.content-block p \{[^}]*?line-height:) 1\.7;([^}]*?margin: 0 0 )var\(--space-4\)( 0;)', r'\1 1.45;\2 var(--space-3)\3'),
        (r'(\.content-block ul li \{[^}]*?line-height:) 1\.7;([^}]*?margin-bottom:) var\(--space-3\);', r'\1 1.45;\2 var(--space-2);'),
        (r'(\.key-point \{[^}]*?padding:) var\(--space-4\) var\(--space-5\);([^}]*?margin-top:) var\(--space-4\);', r'\1 var(--space-3) var(--space-4);\2 var(--space-3);'),
        (r'(\.task-layout \{[^}]*?gap:) var\(--space-6\);([^}]*?height: calc\(100% - )50pt\);', r'\1 var(--space-4);\2 36pt);'),
        (r'(\.task-main \{[^}]*?gap:) var\(--space-5\);', r'\1 var(--space-3);'),
        (r'(\.task-sidebar \{[^}]*?gap:) var\(--space-5\);', r'\1 var(--space-3);'),
        (r'(\.task-card \{[^}]*?padding:) var\(--space-5\);', r'\1 var(--space-4);'),
        (r'(\.task-card h3 \{[^}]*?margin-bottom:) var\(--space-4\);', r'\1 var(--space-3);'),
        (r'(\.task-card p \{[^}]*?line-height:) 1\.7;([^}]*?margin: 0 0 )var\(--space-4\)( 0;)', r'\1 1.45;\2 var(--space-3)\3'),
        (r'(\.step-list li \{[^}]*?gap:) var\(--space-4\);([^}]*?margin-bottom:) var\(--space-4\);', r'\1 var(--space-3);\2 var(--space-3);'),
        (r'(\.time-control \{[^}]*?padding:) var\(--space-4\) var\(--space-5\);', r'\1 var(--space-3) var(--space-4);'),
        (r'(\.deliverable-box \{[^}]*?padding:) var\(--space-4\) var\(--space-5\);', r'\1 var(--space-3) var(--space-4);'),
        (r'(\.practice-layout \{[^}]*?gap:) var\(--space-6\);([^}]*?height: calc\(100% - )45pt\);', r'\1 var(--space-4);\2 32pt);'),
        (r'(\.practice-col \{[^}]*?gap:) var\(--space-4\);', r'\1 var(--space-3);'),
        (r'(\.practice-card \{[^}]*?padding:) var\(--space-5\);', r'\1 var(--space-4);'),
        (r'(\.practice-card h3 \{[^}]*?margin-bottom:) var\(--space-4\);', r'\1 var(--space-3);'),
        (r'(\.tip-box \{[^}]*?padding:) var\(--space-4\) var\(--space-5\);', r'\1 var(--space-3) var(--space-4);'),
        (r'(\.warning-box \{[^}]*?padding:) var\(--space-4\) var\(--space-5\);', r'\1 var(--space-3) var(--space-4);'),
        (r'(\.end-summary \{[^}]*?padding:) var\(--space-6\);([^}]*?margin-bottom:) var\(--space-8\);', r'\1 var(--space-4);\2 var(--space-6);'),
        (r'(\.end-summary h3 \{[^}]*?margin-bottom:) var\(--space-4\);', r'\1 var(--space-3);'),
        (r'(\.end-summary li \{[^}]*?line-height:) 1\.7;([^}]*?margin-bottom:) var\(--space-3\);', r'\1 1.45;\2 var(--space-2);'),
        (r'(\.end-next \{[^}]*?padding:) var\(--space-4\) var\(--space-5\);', r'\1 var(--space-3) var(--space-4);'),
        (r'(\.obj-header-bar \{[^}]*?padding:) 30pt 48pt;', r'\1 20pt 32pt;'),
        (r'(\.intro-header-bar \{[^}]*?padding:) 24pt 48pt;', r'\1 18pt 32pt;'),
    ]

    for pat, repl in reps_head:
        head = re.sub(pat, repl, head)

    # ========== BODY inline style replacements ==========
    # Only replace within slide sections (not cover or end if possible)
    # We'll do global replacements for line-height, and targeted for margins/paddings
    reps_body = [
        ('line-height: 1.7;', 'line-height: 1.45;'),
        ('line-height: 1.8;', 'line-height: 1.45;'),
        ('margin-bottom: var(--space-4);', 'margin-bottom: var(--space-3);'),
        ('margin-top: var(--space-4);', 'margin-top: var(--space-3);'),
        ('padding: var(--space-5);', 'padding: var(--space-4);'),
        ('gap: var(--space-6);', 'gap: var(--space-4);'),
    ]
    for old, new in reps_body:
        body = body.replace(old, new)

    with open('slides/day01/index.html', 'w', encoding='utf-8') as f:
        f.write(head + body)
    print('day01 fixed')


def fix_day06():
    with open('slides/day06/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Global CSS compressions
    reps = [
        (r'(\.card \{[^}]*?padding:) 6pt 8pt;', r'\1 4pt 6pt;'),
        (r'(\.card h3 \{[^}]*?margin-bottom:) 4pt;', r'\1 2pt;'),
        (r'(\.bullet-list li \{[^}]*?margin-bottom:) 1pt;', r'\1 0pt;'),
        (r'(\.hint-box \{[^}]*?padding:) 5pt 8pt;', r'\1 3pt 6pt;'),
        (r'(\.roadmap-wrap \{[^}]*?margin-bottom:) 10pt;', r'\1 6pt;'),
        (r'(\.roadmap-item \{[^}]*?padding:) 8pt;', r'\1 5pt;'),
        (r'(\.factor-grid \{[^}]*?gap:) 8pt;', r'\1 6pt;'),
        (r'(\.factor-card \{[^}]*?padding:) 6pt 8pt;', r'\1 4pt 6pt;'),
        (r'(\.redline-card \{[^}]*?margin-bottom:) 6pt;', r'\1 4pt;'),
        (r'(\.award-card \{[^}]*?margin-bottom:) 5pt;', r'\1 3pt;'),
        # Also compress timeline-item and layer-item slightly
        (r'(\.timeline-item \{[^}]*?margin-bottom:) 6pt;', r'\1 4pt;'),
        (r'(\.layer-item \{[^}]*?padding:) 6pt 10pt;', r'\1 4pt 8pt;'),
        # task-card compress
        (r'(\.task-card \{[^}]*?padding:) 10pt 12pt;', r'\1 8pt 10pt;'),
        # prompt-box
        (r'(\.prompt-box \{[^}]*?padding:) 6pt 8pt;', r'\1 4pt 6pt;'),
        (r'(\.prompt-box p \{[^}]*?line-height:) 1\.5;', r'\1 1.35;'),
        # Compare table more compact
        (r'(\.compare-table th \{[^}]*?padding:) 3pt 6pt;', r'\1 2pt 4pt;'),
        (r'(\.compare-table td \{[^}]*?padding:) 3pt 6pt;', r'\1 2pt 4pt;'),
    ]

    for pat, repl in reps:
        html = re.sub(pat, repl, html)

    # Targeted fix for slide 4: reduce its two-col height and card padding inline
    # Actually let's also reduce the min-height of screenshot-area in that slide
    html = html.replace('min-height:60pt', 'min-height:40pt', 1)

    with open('slides/day06/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('day06 fixed')


if __name__ == '__main__':
    fix_day01()
    fix_day06()
