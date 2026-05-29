#!/usr/bin/env python3
"""
Slide generator for AI training course.
Generates a complete day index.html from structured slide data.
Style based on day04/day05 self-contained template.
"""
import os
import sys
from pathlib import Path

# ------------------------------------------------------------------
# CSS + JS template (extracted from day04)
# ------------------------------------------------------------------
HEAD_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ width: 100%; height: 100%; overflow: hidden; font-family: "Microsoft YaHei", "PingFang SC", sans-serif; background: #F8FBFF; }}
  .slide {{ width: 960pt; height: 540pt; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); display: none; overflow: hidden; }}
  .slide.active {{ display: block; }}

  .content > *, .hero > * {{
    opacity: 0; transform: translateY(12px) scale(0.98);
    animation: slideInUp 0.55s cubic-bezier(0.22, 1, 0.36, 1) forwards;
  }}
  .content > *:nth-child(1), .hero > *:nth-child(1) {{ animation-delay: 0.04s; }}
  .content > *:nth-child(2), .hero > *:nth-child(2) {{ animation-delay: 0.10s; }}
  .content > *:nth-child(3), .hero > *:nth-child(3) {{ animation-delay: 0.16s; }}
  .content > *:nth-child(4), .hero > *:nth-child(4) {{ animation-delay: 0.22s; }}
  .content > *:nth-child(5), .hero > *:nth-child(5) {{ animation-delay: 0.28s; }}
  .content > *:nth-child(6), .hero > *:nth-child(6) {{ animation-delay: 0.34s; }}
  .content > *:nth-child(7), .hero > *:nth-child(7) {{ animation-delay: 0.40s; }}
  .content > *:nth-child(8), .hero > *:nth-child(8) {{ animation-delay: 0.46s; }}
  @keyframes slideInUp {{ to {{ opacity: 1; transform: translateY(0) scale(1); }} }}

  .top-bar {{ position: absolute; top: 0; left: 0; right: 0; height: 4pt; background: #084E8F; z-index: 100; }}
  .slide-header {{ position: absolute; top: 4pt; left: 0; right: 0; height: 36pt; display: flex; align-items: center; justify-content: space-between; padding: 0 28pt; background: #ffffff; border-bottom: 1pt solid #e2e8f0; z-index: 10; }}
  .slide-header img {{ height: 22pt; width: auto; }}
  .slide-header .page-meta {{ font-size: 10pt; color: #666666; }}
  .slide-footer {{ position: absolute; bottom: 0; left: 0; right: 0; height: 28pt; display: flex; align-items: center; justify-content: space-between; padding: 0 28pt; background: #ffffff; border-top: 1pt solid #e2e8f0; z-index: 10; }}
  .slide-footer p {{ font-size: 9pt; color: #666666; }}
  .content {{ position: absolute; top: 40pt; bottom: 28pt; left: 0; right: 0; padding: 14pt 28pt; box-sizing: border-box; overflow: hidden; }}
  .kicker {{ display: inline-flex; align-items: center; gap: 8pt; margin-bottom: 6pt; }}
  .kicker .bar {{ width: 18pt; height: 3pt; background: #EE822F; border-radius: 2pt; }}
  .kicker p {{ font-size: 11pt; color: #EE822F; font-weight: 700; letter-spacing: 0.06em; }}
  .page-title {{ font-size: 24pt; font-weight: 700; color: #084E8F; line-height: 1.2; margin-bottom: 10pt; }}
  .two-col {{ display: flex; gap: 14pt; height: calc(100% - 56pt); }}
  .col {{ flex: 1; display: flex; flex-direction: column; gap: 8pt; }}
  .card {{ background: #ffffff; border: 1pt solid #e2e8f0; border-radius: 6pt; padding: 10pt 12pt; }}
  .card h3 {{ font-size: 13pt; color: #084E8F; font-weight: 700; margin-bottom: 6pt; }}
  .card p, .card li {{ font-size: 10pt; color: #333333; line-height: 1.6; }}
  .hint-box {{ background: rgba(8,78,143,0.04); border-left: 3pt solid #084E8F; border-radius: 0 4pt 4pt 0; padding: 8pt 10pt; }}
  .hint-box.warning {{ background: rgba(238,130,47,0.06); border-left-color: #EE822F; }}
  .hint-box.success {{ background: rgba(117,189,66,0.06); border-left-color: #75BD42; }}
  .hint-box.danger {{ background: rgba(255,0,0,0.04); border-left-color: #FF0000; }}
  .hint-box .label {{ font-size: 9pt; font-weight: 700; margin-bottom: 2pt; }}
  .hint-box p {{ font-size: 10pt; line-height: 1.5; margin: 0; }}
  .bullet-list {{ list-style: none; padding: 0; margin: 0; }}
  .bullet-list li {{ padding-left: 14pt; position: relative; margin-bottom: 4pt; }}
  .bullet-list li::before {{ content: ""; position: absolute; left: 0; top: 7pt; width: 5pt; height: 5pt; border-radius: 50%; background: #084E8F; }}
  .tag {{ display: inline-block; padding: 2pt 8pt; border-radius: 999pt; font-size: 9pt; font-weight: 700; margin-top: 4pt; }}
  .tag-primary {{ background: rgba(8,78,143,0.10); color: #084E8F; }}
  .tag-accent {{ background: rgba(238,130,47,0.12); color: #EE822F; }}
  .tag-success {{ background: rgba(117,189,66,0.12); color: #75BD42; }}
  .screenshot-area {{ background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%); border: 2pt dashed #e2e8f0; border-radius: 6pt; display: flex; align-items: center; justify-content: center; min-height: 80pt; color: #666666; font-size: 10pt; }}
  .screenshot-area img {{ max-width: 100%; max-height: 140pt; border-radius: 4pt; }}
  .compare-table {{ width: 100%; border-collapse: collapse; font-size: 10pt; }}
  .compare-table th {{ background: #084E8F; color: #ffffff; padding: 5pt 8pt; text-align: left; font-weight: 700; }}
  .compare-table td {{ padding: 5pt 8pt; border-bottom: 1pt solid #e2e8f0; color: #333333; }}
  .compare-table tr:nth-child(even) {{ background: rgba(8,78,143,0.02); }}

  .cover-body {{ background: #F8FBFF; }}
  .cover-top-bar {{ position: absolute; top: 0; left: 0; right: 0; height: 6pt; background: #084E8F; z-index: 100; }}
  .deco-shape {{ position: absolute; right: 0; top: 0; width: 220pt; height: 540pt; background: #084E8F; clip-path: polygon(40% 0, 100% 0, 100% 100%, 0% 100%); z-index: 0; }}
  .deco-accent {{ position: absolute; right: 180pt; top: 120pt; width: 80pt; height: 80pt; background: #EE822F; border-radius: 50%; opacity: 0.15; z-index: 0; }}
  .deco-green {{ position: absolute; right: 60pt; bottom: 80pt; width: 120pt; height: 120pt; background: #75BD42; border-radius: 50%; opacity: 0.12; z-index: 0; }}
  .logo-wrap {{ position: absolute; top: 20pt; left: 32pt; display: flex; align-items: center; gap: 10pt; z-index: 1; }}
  .logo-wrap img {{ height: 28pt; width: auto; }}
  .logo-text {{ font-size: 12pt; color: #084E8F; font-weight: 700; letter-spacing: 0.05em; }}
  .course-tag {{ position: absolute; top: 22pt; right: 32pt; background: rgba(8,78,143,0.08); padding: 4pt 12pt; border-radius: 999pt; font-size: 11pt; color: #084E8F; font-weight: 500; z-index: 1; }}
  .hero {{ position: absolute; top: 90pt; left: 48pt; right: 48pt; z-index: 1; }}
  .day-label {{ display: inline-flex; align-items: center; gap: 8pt; margin-bottom: 16pt; }}
  .day-label .bar {{ width: 24pt; height: 3pt; background: #EE822F; border-radius: 2pt; }}
  .day-label p {{ font-size: 14pt; color: #EE822F; font-weight: 700; letter-spacing: 0.08em; }}
  .main-title {{ font-size: 44pt; font-weight: 700; color: #084E8F; line-height: 1.2; margin-bottom: 16pt; }}
  .main-title span {{ color: #EE822F; }}
  .sub-title {{ font-size: 18pt; color: #333333; line-height: 1.6; margin-bottom: 40pt; }}
  .bottom-info {{ position: absolute; bottom: 40pt; left: 48pt; right: 48pt; display: flex; justify-content: space-between; align-items: flex-end; z-index: 1; }}
  .bottom-info p {{ font-size: 12pt; color: #666666; line-height: 1.8; }}

  .obj-card {{ flex: 1; background: #ffffff; border: 1pt solid #e2e8f0; border-radius: 6pt; padding: 14pt; display: flex; flex-direction: column; }}
  .obj-card .card-icon {{ width: 36pt; height: 36pt; border-radius: 8pt; display: flex; align-items: center; justify-content: center; margin-bottom: 10pt; font-size: 18pt; font-weight: 700; color: #ffffff; }}
  .obj-card:nth-child(1) .card-icon {{ background: #084E8F; }}
  .obj-card:nth-child(2) .card-icon {{ background: #EE822F; }}
  .obj-card:nth-child(3) .card-icon {{ background: #75BD42; }}
  .obj-card h3 {{ font-size: 15pt; color: #084E8F; font-weight: 700; margin-bottom: 10pt; }}
  .obj-card li {{ font-size: 11pt; color: #333333; line-height: 1.7; padding-left: 14pt; position: relative; margin-bottom: 6pt; }}
  .obj-card li::before {{ content: ""; position: absolute; left: 0; top: 8pt; width: 5pt; height: 5pt; border-radius: 50%; background: #084E8F; }}
  .obj-card:nth-child(2) li::before {{ background: #EE822F; }}
  .obj-card:nth-child(3) li::before {{ background: #75BD42; }}
  .obj-card .highlight-box {{ background: rgba(8,78,143,0.04); border-left: 2pt solid #084E8F; padding: 8pt 10pt; border-radius: 0 4pt 4pt 0; margin-top: auto; }}
  .obj-card:nth-child(2) .highlight-box {{ border-left-color: #EE822F; background: rgba(238,130,47,0.04); }}
  .obj-card:nth-child(3) .highlight-box {{ border-left-color: #75BD42; background: rgba(117,189,66,0.04); }}
  .obj-card .highlight-box p {{ font-size: 10pt; color: #666666; line-height: 1.5; }}

  .question-box {{ background: #ffffff; border: 1pt solid #e2e8f0; border-radius: 8pt; padding: 20pt 24pt; margin-bottom: 16pt; position: relative; }}
  .question-box::before {{ content: ""; position: absolute; left: 0; top: 16pt; bottom: 16pt; width: 4pt; background: #EE822F; border-radius: 0 2pt 2pt 0; }}
  .question-label {{ display: inline-flex; align-items: center; gap: 6pt; margin-bottom: 8pt; }}
  .question-label .dot {{ width: 6pt; height: 6pt; background: #EE822F; border-radius: 50%; }}
  .question-label p {{ font-size: 11pt; color: #EE822F; font-weight: 700; }}
  .question-box h2 {{ font-size: 20pt; color: #084E8F; font-weight: 700; line-height: 1.4; margin-bottom: 10pt; }}
  .question-box .sub-q {{ font-size: 12pt; color: #666666; line-height: 1.6; }}
  .answer-row {{ display: flex; gap: 14pt; }}
  .answer-card {{ flex: 1; background: #ffffff; border: 1pt solid #e2e8f0; border-radius: 6pt; padding: 12pt 14pt; }}
  .answer-card h4 {{ font-size: 12pt; color: #084E8F; font-weight: 700; margin-bottom: 6pt; }}
  .answer-card p {{ font-size: 11pt; color: #333333; line-height: 1.6; }}

  .end-hero {{ position: absolute; top: 50%; left: 48pt; right: 300pt; transform: translateY(-50%); z-index: 1; }}
  .end-title {{ font-size: 44pt; font-weight: 700; color: #084E8F; line-height: 1.2; margin-bottom: 16pt; }}
  .end-subtitle {{ font-size: 16pt; color: #333333; line-height: 1.6; margin-bottom: 20pt; }}
  .end-summary {{ background: #ffffff; border: 1pt solid #e2e8f0; border-radius: 6pt; padding: 12pt 14pt; margin-bottom: 16pt; }}
  .end-summary h3 {{ font-size: 13pt; color: #084E8F; font-weight: 700; margin-bottom: 8pt; }}
  .end-summary li {{ font-size: 11pt; color: #333333; line-height: 1.7; padding-left: 16pt; position: relative; margin-bottom: 4pt; }}
  .end-summary li::before {{ content: "✓"; position: absolute; left: 0; color: #75BD42; font-weight: 700; }}
  .end-next {{ background: rgba(238,130,47,0.06); border-left: 3pt solid #EE822F; border-radius: 0 4pt 4pt 0; padding: 8pt 12pt; }}
  .end-next .label {{ font-size: 10pt; color: #EE822F; font-weight: 700; margin-bottom: 2pt; }}
  .end-next p {{ font-size: 11pt; color: #333333; line-height: 1.5; }}

  .step-bar {{ display: flex; gap: 4pt; align-items: center; margin-bottom: 8pt; }}
  .step-item {{ display: flex; align-items: center; gap: 4pt; }}
  .step-dot {{ width: 20pt; height: 20pt; border-radius: 50%; background: #084E8F; color: #ffffff; font-size: 9pt; font-weight: 700; display: flex; align-items: center; justify-content: center; }}
  .step-line {{ width: 16pt; height: 2pt; background: #e2e8f0; }}

  .code-block {{ background: #1e293b; color: #e2e8f0; padding: 8pt 10pt; border-radius: 4pt; font-family: "Consolas", monospace; font-size: 9pt; line-height: 1.5; overflow-x: auto; }}
  .prompt-box {{ background: rgba(8,78,143,0.04); border-left: 3pt solid #084E8F; border-radius: 0 4pt 4pt 0; padding: 6pt 8pt; margin-bottom: 6pt; }}
  .prompt-box .label {{ font-size: 9pt; color: #084E8F; font-weight: 700; margin-bottom: 2pt; }}
  .prompt-box p {{ font-size: 9pt; color: #333333; line-height: 1.5; }}

  .factor-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8pt; }}
  .factor-card {{ background: #ffffff; border-left: 3pt solid #084E8F; border-top: 1pt solid #e2e8f0; border-right: 1pt solid #e2e8f0; border-bottom: 1pt solid #e2e8f0; border-radius: 0 4pt 4pt 0; padding: 6pt 8pt; }}
  .factor-card h4 {{ font-size: 11pt; color: #084E8F; font-weight: 700; margin-bottom: 2pt; }}
  .factor-card p {{ font-size: 9pt; color: #333333; line-height: 1.4; }}
  .factor-card:nth-child(2) {{ border-left-color: #92181A; }} .factor-card:nth-child(2) h4 {{ color: #92181A; }}
  .factor-card:nth-child(3) {{ border-left-color: #EE822F; }} .factor-card:nth-child(3) h4 {{ color: #EE822F; }}
  .factor-card:nth-child(4) {{ border-left-color: #75BD42; }} .factor-card:nth-child(4) h4 {{ color: #75BD42; }}

  .nav-overlay {{ position: fixed; bottom: 20pt; right: 20pt; display: flex; gap: 6pt; z-index: 9999; }}
  .nav-btn {{ background: #084E8F; color: #ffffff; border: none; border-radius: 4pt; padding: 6pt 12pt; font-size: 10pt; cursor: pointer; }}
  .nav-btn:hover {{ background: #073A76; }}
  .page-indicator {{ background: #ffffff; border: 1pt solid #e2e8f0; border-radius: 4pt; padding: 6pt 10pt; font-size: 10pt; color: #666666; }}

  @media print {{ .slide {{ position: relative; top: auto; left: auto; transform: none; page-break-after: always; display: block !important; }} .nav-overlay {{ display: none; }} }}
</style>
</head>
<body>
'''

FOOTER_TEMPLATE = '''
<!-- Navigation -->
<div class="nav-overlay">
  <button class="nav-btn" onclick="prevSlide()">上一页</button>
  <div class="page-indicator"><span id="page-num">1 / {total}</span></div>
  <button class="nav-btn" onclick="nextSlide()">下一页</button>
</div>

<script>
  let currentSlide = 1;
  const totalSlides = {total};
  function showSlide(n) {{
    document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
    document.getElementById('slide-' + n).classList.add('active');
    document.getElementById('page-num').textContent = n + ' / ' + totalSlides;
  }}
  function nextSlide() {{ if (currentSlide < totalSlides) {{ currentSlide++; showSlide(currentSlide); }} }}
  function prevSlide() {{ if (currentSlide > 1) {{ currentSlide--; showSlide(currentSlide); }} }}
  document.addEventListener('keydown', function(e) {{
    if (e.key === 'ArrowRight' || e.key === ' ') nextSlide();
    if (e.key === 'ArrowLeft') prevSlide();
  }});
</script>
</body>
</html>
'''


def render_cover(day_num, day_title, subtitle, active=True):
    cls = 'slide active cover-body' if active else 'slide cover-body'
    return f'''
<section class="{cls}" id="slide-1">
  <div class="cover-top-bar"></div>
  <div class="deco-shape"></div>
  <div class="deco-accent"></div>
  <div class="deco-green"></div>
  <div class="logo-wrap">
    <img src="../../materials/logo.svg" alt="公司 Logo">
    <p class="logo-text">AI 智能体工具实训</p>
  </div>
  <div class="course-tag"><p>6 天集训 · 第 {day_num} 天</p></div>
  <div class="hero">
    <div class="day-label"><div class="bar"></div><p>DAY 0{day_num}</p></div>
    <h1 class="main-title">{day_title}</h1>
    <p class="sub-title">{subtitle}</p>
  </div>
  <div class="bottom-info">
    <div><p>授课对象：农林高校应届毕业生（计算机 + 非计算机混编，30 人）</p><p>授课时长：上午 3 小时 + 下午 3 小时</p></div>
    <div style="text-align:right"><p>2026 年 5 月</p><p>主讲讲师</p></div>
  </div>
</section>
'''


def render_objectives(page, day_num, knowledge, skills, literacy):
    k_items = '\n'.join(f'<li>{x}</li>' for x in knowledge)
    s_items = '\n'.join(f'<li>{x}</li>' for x in skills)
    l_items = '\n'.join(f'<li>{x}</li>' for x in literacy)
    return f'''
<section class="slide" id="slide-{page}">
  <div class="top-bar"></div>
  <div class="slide-header">
    <img src="../../materials/logo.svg" alt="公司 Logo">
    <p class="page-meta">Day {day_num} · 学习目标</p>
  </div>
  <div class="content">
    <div class="kicker"><div class="bar"></div><p>课程导览</p></div>
    <h1 class="page-title">今天你要带走什么？</h1>
    <div style="display:flex;gap:14pt;height:calc(100% - 80pt)">
      <div class="obj-card">
        <div class="card-icon"><p>知</p></div>
        <h3>知识目标</h3>
        <ul>{k_items}</ul>
        <div class="highlight-box"><p>核心认知：{knowledge[-1] if knowledge else ''}</p></div>
      </div>
      <div class="obj-card">
        <div class="card-icon"><p>技</p></div>
        <h3>技能目标</h3>
        <ul>{s_items}</ul>
        <div class="highlight-box"><p>实战产出：{skills[-1] if skills else ''}</p></div>
      </div>
      <div class="obj-card">
        <div class="card-icon"><p>养</p></div>
        <h3>素养目标</h3>
        <ul>{l_items}</ul>
        <div class="highlight-box"><p>思维转变：{literacy[-1] if literacy else ''}</p></div>
      </div>
    </div>
  </div>
  <div class="slide-footer"><p>AI 智能体工具实训 · 农林高校 2026</p><p>{page} / __TOTAL__</p></div>
</section>
'''


def render_content(page, day_num, section_title, kicker, title, left_cards, right_cards):
    """Render a two-column content slide."""
    def render_card(card):
        if card.get('type') == 'image':
            img = card.get('src', '')
            alt = card.get('alt', '插图')
            return f'<div class="card"><h3>{card["title"]}</h3><div class="screenshot-area"><img src="{img}" alt="{alt}"></div></div>'
        elif card.get('type') == 'hint':
            return f'<div class="card"><div class="hint-box {card.get("variant", "")}"><p class="label">{card["title"]}</p><p>{card["text"]}</p></div></div>'
        elif card.get('type') == 'table':
            rows = '\n'.join(
                f'<tr><td>{c[0]}</td><td>{c[1]}</td><td>{c[2]}</td></tr>' if len(c) == 3 else f'<tr><td>{c[0]}</td><td>{c[1]}</td></tr>'
                for c in card.get('rows', [])
            )
            headers = ''.join(f'<th>{h}</th>' for h in card.get('headers', []))
            return f'<div class="card"><h3>{card["title"]}</h3><table class="compare-table"><thead><tr>{headers}</tr></thead><tbody>{rows}</tbody></table></div>'
        elif card.get('type') == 'prompt':
            return f'<div class="card"><div class="prompt-box"><p class="label">{card["title"]}</p><p>{card["text"]}</p></div></div>'
        elif card.get('type') == 'code':
            return f'<div class="card"><h3>{card["title"]}</h3><div class="code-block">{card["text"]}</div></div>'
        else:
            items = '\n'.join(f'<li>{x}</li>' for x in card.get('items', []))
            body = f'<ul class="bullet-list">{items}</ul>' if items else f'<p>{card.get("text", "")}</p>'
            return f'<div class="card"><h3>{card["title"]}</h3>{body}</div>'

    left_html = '\n'.join(render_card(c) for c in left_cards)
    right_html = '\n'.join(render_card(c) for c in right_cards)

    return f'''
<section class="slide" id="slide-{page}">
  <div class="top-bar"></div>
  <div class="slide-header">
    <img src="../../materials/logo.svg" alt="公司 Logo">
    <p class="page-meta">Day {day_num} · {section_title}</p>
  </div>
  <div class="content">
    <div class="kicker"><div class="bar"></div><p>{kicker}</p></div>
    <h1 class="page-title">{title}</h1>
    <div class="two-col">
      <div class="col">{left_html}</div>
      <div class="col">{right_html}</div>
    </div>
  </div>
  <div class="slide-footer"><p>AI 智能体工具实训 · 农林高校 2026</p><p>{page} / __TOTAL__</p></div>
</section>
'''


def render_intro(page, day_num, question, subtitle, cards):
    card_html = '\n'.join(
        f'<div class="answer-card"><h4>{c["title"]}</h4><p>{c["text"]}</p><span class="tag {c.get("tag_class", "tag-primary")}">{c["tag"]}</span></div>'
        for c in cards
    )
    return f'''
<section class="slide" id="slide-{page}">
  <div class="top-bar"></div>
  <div class="slide-header">
    <img src="../../materials/logo.svg" alt="公司 Logo">
    <p class="page-meta">Day {day_num} · 课程导入</p>
  </div>
  <div class="content">
    <div class="question-box">
      <div class="question-label"><div class="dot"></div><p>课前思考</p></div>
      <h2>{question}</h2>
      <p class="sub-q">{subtitle}</p>
    </div>
    <div class="answer-row">{card_html}</div>
  </div>
  <div class="slide-footer"><p>AI 智能体工具实训 · 农林高校 2026</p><p>{page} / __TOTAL__</p></div>
</section>
'''


def render_task(page, day_num, title, steps, deliverables, standards):
    step_html = '\n'.join(
        f'<div class="card"><div style="display:flex;gap:10pt;align-items:flex-start"><div class="step-num">{i+1}</div><div><h3>{s["title"]}</h3><p>{s["text"]}</p></div></div></div>'
        for i, s in enumerate(steps)
    )
    deliv_html = '\n'.join(f'<li>{x}</li>' for x in deliverables)
    std_html = '\n'.join(f'<li>{x}</li>' for x in standards)
    return f'''
<section class="slide" id="slide-{page}">
  <div class="top-bar"></div>
  <div class="slide-header">
    <img src="../../materials/logo.svg" alt="公司 Logo">
    <p class="page-meta">Day {day_num} · 任务布置</p>
  </div>
  <div class="content">
    <div class="kicker"><div class="bar"></div><p>下午实战</p></div>
    <h1 class="page-title">{title}</h1>
    <div class="two-col">
      <div class="col">
        <div class="card"><h3>任务步骤</h3></div>
        {step_html}
      </div>
      <div class="col">
        <div class="card"><h3>交付物清单</h3><ul class="bullet-list">{deliv_html}</ul></div>
        <div class="card"><h3>评分标准</h3><ul class="bullet-list">{std_html}</ul></div>
        <div class="hint-box warning"><p class="label">时间提醒</p><p>下午共 3 小时，请合理分配时间，建议每步预留 10 分钟缓冲。</p></div>
      </div>
    </div>
  </div>
  <div class="slide-footer"><p>AI 智能体工具实训 · 农林高校 2026</p><p>{page} / __TOTAL__</p></div>
</section>
'''


def render_practice(page, day_num, title, steps):
    step_html = '\n'.join(
        f'<div class="card"><h3>步骤 {i+1}：{s["title"]}</h3><p>{s["text"]}</p><div class="screenshot-area"><p>[ 截图区：{s.get("screenshot", "操作示意图")} ]</p></div></div>'
        for i, s in enumerate(steps)
    )
    return f'''
<section class="slide" id="slide-{page}">
  <div class="top-bar"></div>
  <div class="slide-header">
    <img src="../../materials/logo.svg" alt="公司 Logo">
    <p class="page-meta">Day {day_num} · 课堂实操</p>
  </div>
  <div class="content">
    <div class="kicker"><div class="bar"></div><p>动手环节</p></div>
    <h1 class="page-title">{title}</h1>
    <div class="two-col">
      <div class="col">{step_html}</div>
      <div class="col">
        <div class="hint-box success"><p class="label">技巧提示</p><p>遇到困难时，先检查工具是否已正确登录，再检查输入格式是否符合要求。</p></div>
        <div class="hint-box warning"><p class="label">常见错误</p><p>不要一次性输入过多需求，建议分步骤验证每个功能是否正常。</p></div>
        <div class="hint-box"><p class="label">助教支持</p><p>任何技术问题随时举手，助教会在 2 分钟内到达。</p></div>
      </div>
    </div>
  </div>
  <div class="slide-footer"><p>AI 智能体工具实训 · 农林高校 2026</p><p>{page} / __TOTAL__</p></div>
</section>
'''


def render_quiz(page, day_num, questions):
    parts = []
    for i, q in enumerate(questions):
        opts = ''
        if q.get('options'):
            opts = '<ul class="bullet-list">' + ''.join(f'<li>{o}</li>' for o in q['options']) + '</ul>'
        card = (
            f'<div class="card"><h3>题 {i+1}（{q["type"]}）</h3>'
            f'<p>{q["question"]}</p>{opts}'
            f'<div class="hint-box success"><p class="label">答案解析</p>'
            f'<p>{q["answer"]}</p></div></div>'
        )
        parts.append(card)
    q_html = '\n'.join(parts)
    return f'''
<section class="slide" id="slide-{page}">
  <div class="top-bar"></div>
  <div class="slide-header">
    <img src="../../materials/logo.svg" alt="公司 Logo">
    <p class="page-meta">Day {day_num} · 课堂习题</p>
  </div>
  <div class="content">
    <div class="kicker"><div class="bar"></div><p>巩固练习</p></div>
    <h1 class="page-title">今日习题</h1>
    <div class="two-col">
      <div class="col">{q_html}</div>
      <div class="col">
        <div class="card"><h3>答题小贴士</h3><ul class="bullet-list"><li>认真审题，抓住关键词</li><li>结合实际案例思考</li><li>不确定时，回忆课堂实操步骤</li></ul></div>
        <div class="hint-box"><p class="label">评分方式</p><p>每题 10 分，共 {len(questions)*10} 分。举手回答或写在便签纸上交给助教。</p></div>
      </div>
    </div>
  </div>
  <div class="slide-footer"><p>AI 智能体工具实训 · 农林高校 2026</p><p>{page} / __TOTAL__</p></div>
</section>
'''


def render_end(page, day_num, day_title, summary_points, next_day_title, next_preview):
    summary_html = '\n'.join(f'<li>{x}</li>' for x in summary_points)
    return f'''
<section class="slide cover-body" id="slide-{page}">
  <div class="cover-top-bar"></div>
  <div class="deco-shape"></div>
  <div class="deco-accent"></div>
  <div class="deco-green"></div>
  <div class="logo-wrap">
    <img src="../../materials/logo.svg" alt="公司 Logo">
    <p class="logo-text">AI 智能体工具实训</p>
  </div>
  <div class="end-hero">
    <h1 class="end-title">Day {day_num} 总结</h1>
    <p class="end-subtitle">{day_title}</p>
    <div class="end-summary">
      <h3>今日要点回顾</h3>
      <ul>{summary_html}</ul>
    </div>
    <div class="end-next">
      <p class="label">下次预告 · Day {day_num+1}</p>
      <p>{next_preview}</p>
    </div>
  </div>
  <div class="bottom-info">
    <div><p>AI 智能体工具实训 · 农林高校 2026</p></div>
    <div style="text-align:right"><p>感谢聆听 · 欢迎交流</p></div>
  </div>
</section>
'''


def build_day(day_num, day_title, subtitle, slides_data):
    """Build a complete day index.html from slide data."""
    title = f"Day {day_num} · {day_title}"
    parts = [HEAD_TEMPLATE.format(title=title)]

    for i, slide in enumerate(slides_data, 1):
        stype = slide['type']
        if stype == 'cover':
            parts.append(render_cover(day_num, day_title, subtitle, active=(i==1)))
        elif stype == 'objectives':
            parts.append(render_objectives(i, day_num, slide['knowledge'], slide['skills'], slide['literacy']))
        elif stype == 'intro':
            parts.append(render_intro(i, day_num, slide['question'], slide.get('subtitle', ''), slide['cards']))
        elif stype == 'content':
            parts.append(render_content(i, day_num, slide.get('section', '知识储备'), slide.get('kicker', '核心内容'), slide['title'], slide['left'], slide['right']))
        elif stype == 'task':
            parts.append(render_task(i, day_num, slide['title'], slide['steps'], slide['deliverables'], slide['standards']))
        elif stype == 'practice':
            parts.append(render_practice(i, day_num, slide['title'], slide['steps']))
        elif stype == 'quiz':
            parts.append(render_quiz(i, day_num, slide['questions']))
        elif stype == 'end':
            parts.append(render_end(i, day_num, day_title, slide['summary'], slide['next_title'], slide['next_preview']))
        else:
            raise ValueError(f"Unknown slide type: {stype}")

    total = len(slides_data)
    html = '\n'.join(parts)
    html = html.replace('__TOTAL__', str(total))
    html += FOOTER_TEMPLATE.format(total=total)

    return html


if __name__ == '__main__':
    import importlib.util
    if len(sys.argv) > 1:
        data_path = sys.argv[1]
        # Support both .py and .json
        if data_path.endswith('.py'):
            spec = importlib.util.spec_from_file_location("slide_data", data_path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            config = {
                'day_num': mod.day_num,
                'day_title': mod.day_title,
                'subtitle': mod.subtitle,
                'output': mod.output,
                'slides': mod.slides
            }
        else:
            import json
            with open(data_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        html = build_day(config['day_num'], config['day_title'], config['subtitle'], config['slides'])
        out_path = Path(config['output'])
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated {out_path} with {len(config['slides'])} slides.")
    else:
        print("Usage: python generate_slides.py config.py|config.json")
