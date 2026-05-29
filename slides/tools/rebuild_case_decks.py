from pathlib import Path
from html import escape


ROOT = Path(__file__).resolve().parents[2]
SLIDES = ROOT / "slides"


def card(title, body, tone="primary"):
    return f"""
      <div class="card {tone}">
        <h3>{escape(title)}</h3>
        <div>{body}</div>
      </div>"""


def ul(items):
    return "<ul>" + "".join(f"<li>{escape(item)}</li>" for item in items) + "</ul>"


def numbered(items):
    return "<ol>" + "".join(f"<li>{escape(item)}</li>" for item in items) + "</ol>"


def prompt_box(label, text):
    return f"""
      <div class="prompt-box">
        <p class="prompt-label">{escape(label)}</p>
        <p>{escape(text)}</p>
      </div>"""


def slide_shell(day, page, total, meta, title, inner, extra_class=""):
    return f"""
<section class="slide {extra_class}" id="slide-{page}">
  <div class="top-bar"></div>
  <div class="slide-header">
    <img src="../../materials/logo-v2.svg" alt="Logo">
    <p class="page-meta">Day {day:02d} · {escape(meta)}</p>
  </div>
  <div class="content content-enter">
    <div class="kicker"><span></span><p>{escape(meta)}</p></div>
    <h1 class="page-title">{escape(title)}</h1>
    {inner}
  </div>
  <div class="slide-footer">
    <p>AI 工具实战训练营</p>
    <p>{page} / {total}</p>
  </div>
</section>"""


def cover(day, total, title, subtitle, tags, image="case-learning-hero.png"):
    course_days = 5 if day <= 5 else 6
    footer_left = """
    <div class="cover-course-meta">
      <span><b>主题：</b>AI实战训练营</span>
      <span><b>讲师：</b>吴家文</span>
      <span><b>时间：</b>2026年6月</span>
    </div>""" if day <= 5 else "<p>案例驱动 · 教师带做 · 学生实操 · 复盘迭代</p>"
    return f"""
<section class="slide cover active" id="slide-1">
  <div class="cover-top-bar"></div>
  <img class="cover-image" src="../assets/{image}" alt="">
  <div class="cover-shade"></div>
  <div class="cover-logo">
    <img src="../../materials/logo-v2.svg" alt="Logo">
    <p>AI 工具实战训练营</p>
  </div>
  <div class="cover-tag">{course_days} 天案例课 · 第 {day} 天</div>
  <div class="cover-hero">
    <p class="day-label">DAY {day:02d}</p>
    <h1>{escape(title)}</h1>
    <p class="subtitle">{escape(subtitle)}</p>
    <div class="tag-row">{''.join(f'<span>{escape(t)}</span>' for t in tags)}</div>
  </div>
  <div class="slide-footer cover-footer">
    {footer_left}
    <p>1 / {total}</p>
  </div>
</section>"""


def image_slide(day, page, total, meta, title, img, caption, mode="contain"):
    return slide_shell(day, page, total, meta, title, f"""
    <div class="image-slide">
      <img class="{mode}" src="../assets/{img}" alt="{escape(title)}">
      <div class="caption">{escape(caption)}</div>
    </div>
    """, "image-heavy")


def evolution_slide(day, page, total):
    return slide_shell(day, page, total, "演进图总览", "从 Vibe Coding 到 Agentic Engineering", f"""
    <div class="evolution-explain">
      <div class="evolution-steps">
        {card("1. Software 1.0", ul(["人写规则和代码", "AI 不是主角", "学生理解：传统开发更依赖编码能力"]), "primary")}
        {card("2. Software 2.0", ul(["模型从数据中学习规律", "代表：机器学习、深度学习", "学生理解：训练模型门槛高，不是本课重点"]), "accent")}
        {card("3. AI Copilot", ul(["AI 辅助写代码、补全文档", "人仍然逐行控制", "学生理解：AI 是助手，不是项目负责人"]), "success")}
        {card("4. Vibe Coding", ul(["人用自然语言说清产品感觉和功能", "AI 生成页面、交互和初版代码", "学生理解：重点是需求、审美和验收"]), "primary")}
        {card("5. Agentic Engineering", ul(["目标、角色、工具、测试、记忆、复盘形成流程", "AI 可以分工协作，但需要人设边界", "学生理解：像带一个小团队做项目"]), "accent")}
      </div>
      <div class="evolution-image-wrap">
        <img class="zoomable-image" src="../assets/vibe-agentic-evolution.jpg" alt="从 Vibe Coding 到 Agentic Engineering 演进图" data-zoomable="true">
        <div class="zoom-hint">点击图片全屏查看；滚轮放大，拖动查看；双击或 Esc 还原。原图等比显示，不裁切。</div>
      </div>
    </div>""")


def agentic_battle_map_slide(day, page, total):
    return slide_shell(day, page, total, "Agentic Engineering", "Day 5 项目作战图：不是重复演进史，而是进入项目执行", f"""
    <div class="agentic-map">
      <div class="agentic-left">
        {card("今天的核心变化", ul(["Day 3 看演进：理解 Vibe Coding 为什么出现", "Day 5 做项目：把 AI 当协作团队来组织", "从单次提示词，升级为目标、角色、工具、验收", "从效果好不好看，升级为能否交付、能否复盘"]), "primary")}
        {card("项目指挥官要做什么", ul(["定目标：只做 1 个用户、1 条主流程", "拆任务：谁负责内容、页面、测试、路演", "控边界：不做登录、后端、真实 API", "收证据：工作流、版本、Bug、截图、知识卡", "做决策：AI 给方案，人判断取舍"]), "accent")}
        {card("课堂判断", ul(["能不能说清用户和场景", "能不能把任务交给不同 AI 工具", "能不能测试主流程是否能跑", "能不能记录 Bug 和修复过程", "能不能讲清个人贡献"]), "success")}
      </div>
      <div class="agentic-flow">
        <div class="flow-node planner"><b>Planner</b><span>需求卡 / 主流程 / 验收标准</span></div>
        <div class="flow-arrow">→</div>
        <div class="flow-node builder"><b>Builder</b><span>页面 / 文档 / PPT / 版本截图</span></div>
        <div class="flow-arrow">→</div>
        <div class="flow-node tester"><b>Tester</b><span>测试清单 / Bug 记录 / 复测结论</span></div>
        <div class="flow-arrow">→</div>
        <div class="flow-node speaker"><b>Speaker</b><span>路演稿 / 简历项目 / 问答准备</span></div>
        <div class="agentic-evidence">
          {card("必须留下的证据", ul(["需求卡：为什么做这个", "工作流图：每一步谁负责", "测试清单：怎么证明能跑", "Bug 记录：怎么证明迭代过", "LLM-Wiki：怎么沉淀复用"]), "primary")}
          {card("讲师过渡话术", ul(["这不是再看一遍演进图", "从这一页开始，每个小组就是一个 AI 项目团队", "AI 可以干活，但项目经理必须是人", "今天看的是交付证据，不是口头说会用 AI"]), "accent")}
        </div>
      </div>
    </div>""")


def two_col(left, right):
    return f'<div class="two-col"><div>{left}</div><div>{right}</div></div>'


def three_col(cards):
    return '<div class="three-col">' + "".join(cards) + '</div>'


def timeline(rows):
    return '<div class="timeline">' + "".join(
        f'<div class="time-row"><b>{escape(t)}</b><span>{escape(c)}</span></div>' for t, c in rows
    ) + '</div>'


def schedule_slide(day, page, total, rows, outcomes):
    left = card("今日四段课", timeline(rows), "primary")
    right = card("今日产出", ul(outcomes), "success")
    return slide_shell(day, page, total, "时间表", "今天怎么上：四段课都要有产出", two_col(left, right))


def case_slide(day, page, total, case_no, name, feature, scenario, output, skills):
    left = card(f"案例 {case_no}：{name}", f"<p class='lead'>{escape(feature)}</p>{ul([scenario])}", "accent")
    right = card("学生最终要交什么", ul(output), "success") + card("训练能力", ul(skills), "primary")
    return slide_shell(day, page, total, "案例说明", name, two_col(left, right))


def demo_slide(day, page, total, title, steps, teacher_note):
    left = card("教师带做步骤", numbered(steps), "primary")
    right = card("讲师提醒", f"<p>{escape(teacher_note)}</p>", "accent")
    return slide_shell(day, page, total, "教师带做", title, two_col(left, right))


def prompt_slide(day, page, total, title, basic, advanced, fix):
    body = prompt_box("基础版：照着能用", basic) + prompt_box("进阶版：结果更专业", advanced) + prompt_box("纠错版：结果不满意时", fix)
    return slide_shell(day, page, total, "提示词模板", title, body)


def practice_slide(day, page, total, title, tasks, checks, submit):
    left = card("学生实操任务", ul(tasks), "primary")
    right = card("完成标准", ul(checks), "success") + card("提交物", f"<p>{escape(submit)}</p>", "accent")
    return slide_shell(day, page, total, "学生实操", title, two_col(left, right))


def step_cards(items):
    return '<div class="step-list">' + ''.join(
        f"""
        <div class="step-card">
          <div class="step-num">{idx}</div>
          <div>
            <h4>{escape(title)}</h4>
            <p>{escape(text)}</p>
          </div>
        </div>""" for idx, (title, text) in enumerate(items, 1)
    ) + '</div>'


def split_note(title, body, tone="primary"):
    return f"""
    <div class="note-box {tone}">
      <h3>{escape(title)}</h3>
      <p>{escape(body)}</p>
    </div>"""


def compare_cols(left_title, left_items, right_title, right_items):
    return f"""
    <div class="compare-grid">
      <div class="compare-col bad">
        <h3>{escape(left_title)}</h3>
        {ul(left_items)}
      </div>
      <div class="compare-col good">
        <h3>{escape(right_title)}</h3>
        {ul(right_items)}
      </div>
    </div>"""


def rubric_grid(items):
    return '<div class="rubric-grid">' + ''.join(
        f"""
        <div class="rubric-item">
          <b>{escape(weight)}</b>
          <h3>{escape(title)}</h3>
          <p>{escape(desc)}</p>
        </div>""" for weight, title, desc in items
    ) + '</div>'


def pyramid(items):
    return '<div class="pyramid">' + ''.join(
        f'<div class="pyramid-layer layer-{idx}"><h4>{escape(title)}</h4><p>{escape(text)}</p></div>'
        for idx, (title, text) in enumerate(items, 1)
    ) + '</div>'


def compact_table(headers, rows):
    head = "".join(f"<th>{escape(h)}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{escape(cell)}</td>" for cell in row) + "</tr>"
        for row in rows
    )
    return f'<table class="compact-table"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def runbook_slide(day, page, total, case_no, name, tool, prep, teacher_steps, student_steps, prompt, problems):
    return slide_shell(day, page, total, f"案例 {case_no} 操作手册", f"{name}：课堂怎么带着做", f"""
    <div class="runbook">
      <div class="runbook-main">
        {card("工具与课前准备", ul([f"使用工具：{tool}"] + prep), "primary")}
        {card("教师演示步骤", numbered(teacher_steps), "accent")}
        {card("学生跟做步骤", numbered(student_steps), "success")}
      </div>
      <div class="runbook-side">
        <div class="prompt-script">
          <h3>可直接投屏的提示词</h3>
          <p>{escape(prompt)}</p>
        </div>
        <div class="trouble-box">
          <h3>常见问题与处理</h3>
          {compact_table(["问题", "处理办法"], problems)}
        </div>
        <div class="check-strip">
          <h3>课堂检查点</h3>
          <div><span>能复述任务</span><span>能独立操作</span><span>能发现问题</span><span>能提交产出</span></div>
        </div>
      </div>
    </div>
    """)


def drill_slide(day, page, total, title, minutes, teacher, students, output, checks):
    return slide_shell(day, page, total, "课堂执行", title, f"""
    <div class="classroom-grid">
      {card("时间分配", ul(minutes), "primary")}
      {card("讲师动作", ul(teacher), "accent")}
      {card("学生动作", ul(students), "success")}
      {card("产出物", ul(output), "primary")}
      {card("现场检查", ul(checks), "success")}
    </div>
    """)


def troubleshooting_slide(day, page, total, title, rows):
    return slide_shell(day, page, total, "翻车点处理", title, f"""
    <div class="troubleshooting-full">
      {compact_table(["课堂现象", "原因判断", "讲师处理话术/动作"], rows)}
    </div>
    """)


def project_board(day, page, total, title, columns):
    return slide_shell(day, page, total, "项目推进", title, '<div class="board-grid">' + ''.join(
        card(name, ul(items), tone) for name, items, tone in columns
    ) + '</div>')


def summary_slide(day, page, total, learned, next_text):
    return slide_shell(day, page, total, "日终复盘", f"Day {day} 总结", two_col(
        card("今天学会了什么", ul(learned), "success"),
        card("下一步", f"<p>{escape(next_text)}</p>", "accent"),
    ))


def html_doc(day, title, slides):
    total = len(slides)
    css = """
*{box-sizing:border-box}html,body{margin:0;width:100vw;height:100vh;overflow:hidden;background:#1a1a1a;font-family:"Microsoft YaHei","PingFang SC",sans-serif}.deck-container{width:100vw;height:100vh;display:flex;align-items:center;justify-content:center}.slide-wrapper{transform-origin:center center;transition:transform .2s ease}.slide{width:960pt;height:540pt;position:relative;display:none;overflow:hidden;background:#f8fbff;box-shadow:0 8pt 32pt rgba(0,0,0,.3)}.slide.active{display:block}.top-bar{position:absolute;left:0;right:0;top:0;height:4pt;background:#084e8f}.slide-header{position:absolute;left:0;right:0;top:4pt;height:36pt;display:flex;align-items:center;justify-content:space-between;padding:0 28pt;background:#fff;border-bottom:1pt solid #e2e8f0}.slide-header img{height:22pt}.page-meta{font-size:10pt;color:#666}.slide-footer{position:absolute;left:0;right:0;bottom:0;height:24pt;display:flex;align-items:center;justify-content:space-between;padding:0 28pt;background:#fff;border-top:1pt solid #e2e8f0}.slide-footer p{font-size:9.5pt;color:#666;margin:0}.content{position:absolute;left:0;right:0;top:40pt;bottom:24pt;padding:15pt 28pt;overflow:hidden}.kicker{display:flex;align-items:center;gap:8pt;margin-bottom:7pt}.kicker span{width:18pt;height:3pt;background:#ee822f;border-radius:2pt}.kicker p{font-size:10.5pt;color:#ee822f;font-weight:700;letter-spacing:.06em;margin:0}.page-title{font-size:24pt;line-height:1.16;color:#084e8f;margin:0 0 12pt 0}.lead{font-size:12pt!important;color:#084e8f!important;font-weight:700}.two-col{display:grid;grid-template-columns:1fr 1fr;gap:16pt;height:calc(100% - 68pt)}.three-col{display:grid;grid-template-columns:repeat(3,1fr);gap:12pt;height:calc(100% - 68pt)}.card{background:#fff;border:1pt solid #e2e8f0;border-radius:6pt;padding:11pt 13pt;margin-bottom:9pt}.card h3{font-size:13pt;color:#084e8f;margin:0 0 7pt 0}.card p,.card li{font-size:10.5pt;line-height:1.5;color:#333}.card ul,.card ol{padding-left:16pt;margin:0}.card li{margin-bottom:4pt}.card.accent{border-left:4pt solid #ee822f}.card.success{border-left:4pt solid #75bd42}.card.primary{border-left:4pt solid #084e8f}.prompt-box{background:#fff;border-left:4pt solid #084e8f;border-top:1pt solid #e2e8f0;border-right:1pt solid #e2e8f0;border-bottom:1pt solid #e2e8f0;border-radius:0 6pt 6pt 0;padding:10pt 12pt;margin-bottom:8pt}.prompt-label{font-size:11pt!important;color:#ee822f!important;font-weight:700;margin:0 0 4pt 0}.prompt-box p{font-size:11.5pt;line-height:1.5;color:#333;margin:0}.timeline{display:flex;flex-direction:column;gap:7pt}.time-row{display:grid;grid-template-columns:92pt 1fr;gap:8pt;align-items:start;background:#f8fbff;border:1pt solid #e2e8f0;border-radius:5pt;padding:7pt 9pt}.time-row b{font-size:11pt;color:#084e8f}.time-row span{font-size:11pt;color:#333;line-height:1.35}.step-list{display:flex;flex-direction:column;gap:8pt;height:100%}.step-card{background:#fff;border:1pt solid #e2e8f0;border-radius:6pt;padding:10pt 12pt;display:grid;grid-template-columns:26pt 1fr;gap:10pt;align-items:start}.step-num{width:24pt;height:24pt;border-radius:50%;background:#084e8f;color:#fff;font-size:12pt;font-weight:700;display:flex;align-items:center;justify-content:center}.step-card h4{font-size:12pt;color:#084e8f;margin:0 0 4pt}.step-card p{font-size:10pt;color:#333;line-height:1.45;margin:0}.note-box{border-radius:6pt;padding:12pt 14pt}.note-box h3{font-size:13pt;margin:0 0 6pt}.note-box p{font-size:11pt;line-height:1.55;margin:0}.note-box.primary{background:#084e8f;color:#fff}.note-box.primary h3,.note-box.primary p{color:#fff}.note-box.accent{background:rgba(238,130,47,.08);border:1pt solid rgba(238,130,47,.25)}.note-box.accent h3{color:#ee822f}.compare-grid{display:grid;grid-template-columns:1fr 1fr;gap:16pt;height:calc(100% - 68pt)}.compare-col{background:#fff;border:1pt solid #e2e8f0;border-radius:6pt;padding:13pt 15pt}.compare-col h3{font-size:14pt;margin:0 0 10pt}.compare-col.bad{border-top:4pt solid #92181a}.compare-col.bad h3{color:#92181a}.compare-col.good{border-top:4pt solid #75bd42}.compare-col.good h3{color:#75bd42}.compare-col li{font-size:11pt;line-height:1.55;margin-bottom:6pt}.rubric-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:8pt;height:calc(100% - 68pt)}.rubric-item{background:#fff;border:1pt solid #e2e8f0;border-radius:6pt;padding:10pt}.rubric-item b{display:inline-block;color:#ee822f;font-size:18pt;margin-bottom:5pt}.rubric-item h3{font-size:12pt;color:#084e8f;margin:0 0 5pt}.rubric-item p{font-size:9.5pt;line-height:1.45;color:#333;margin:0}.pyramid{height:calc(100% - 68pt);display:flex;flex-direction:column-reverse;align-items:center;justify-content:center;gap:7pt}.pyramid-layer{border-radius:6pt;padding:9pt 16pt;text-align:center;border:1pt solid #e2e8f0;background:#fff}.pyramid-layer h4{font-size:13pt;margin:0 0 3pt}.pyramid-layer p{font-size:10.5pt;margin:0;color:#333}.layer-1{width:90%;border-color:#92181a}.layer-1 h4{color:#92181a}.layer-2{width:75%;border-color:#75bd42}.layer-2 h4{color:#75bd42}.layer-3{width:60%;border-color:#084e8f}.layer-3 h4{color:#084e8f}.layer-4{width:45%;border-color:#ee822f}.layer-4 h4{color:#ee822f}.image-slide{height:calc(100% - 68pt);display:grid;grid-template-rows:minmax(0,1fr) auto;gap:8pt}.image-slide img{width:100%;height:100%;object-fit:contain;background:#fff;border:1pt solid #e2e8f0;border-radius:8pt}.image-slide .caption{font-size:11pt;color:#666;text-align:center}.cover{background:#f8fbff}.cover-image{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.cover-shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(248,251,255,.96) 0%,rgba(248,251,255,.9) 42%,rgba(248,251,255,.22) 100%)}.cover-top-bar{position:absolute;left:0;right:0;top:0;height:6pt;background:#084e8f;z-index:3}.cover-logo{position:absolute;left:32pt;top:20pt;display:flex;align-items:center;gap:10pt;z-index:4}.cover-logo img{height:28pt}.cover-logo p{font-size:12pt;color:#084e8f;font-weight:700}.cover-tag{position:absolute;right:32pt;top:22pt;background:rgba(8,78,143,.08);color:#084e8f;border-radius:999pt;padding:5pt 12pt;font-size:10pt;z-index:4}.cover-hero{position:absolute;left:48pt;top:96pt;width:560pt;z-index:4}.day-label{font-size:12pt;color:#ee822f;font-weight:700;letter-spacing:.08em}.cover h1{font-size:42pt;line-height:1.12;color:#084e8f;margin:12pt 0}.subtitle{font-size:17pt;line-height:1.45;color:#333}.tag-row{display:flex;flex-wrap:wrap;gap:8pt;margin-top:20pt}.tag-row span{background:#fff;border:1pt solid #e2e8f0;border-radius:999pt;padding:5pt 12pt;font-size:11pt;color:#084e8f}.cover-footer{z-index:4}.content-enter>*{opacity:0;transform:translateY(10pt);animation:in .45s ease forwards}.content-enter>*:nth-child(2){animation-delay:.06s}.content-enter>*:nth-child(3){animation-delay:.12s}.content-enter>*:nth-child(4){animation-delay:.18s}@keyframes in{to{opacity:1;transform:none}}@media print{.slide{display:block!important;page-break-after:always;box-shadow:none}}
"""
    extra_css = """
.runbook{display:grid;grid-template-columns:1.12fr .88fr;gap:12pt;height:calc(100% - 64pt)}.runbook-main{display:grid;grid-template-rows:1fr 1.35fr 1.2fr;gap:7pt;min-height:0}.runbook-main .card{margin:0;padding:8pt 10pt;overflow:hidden}.runbook-main .card h3{font-size:11.5pt;margin-bottom:4pt}.runbook-main .card li{font-size:9.4pt;line-height:1.33;margin-bottom:2pt}.runbook-side{display:grid;grid-template-rows:auto auto 1fr;gap:8pt;min-height:0}.prompt-script{background:#fff;border-left:4pt solid #084e8f;border-top:1pt solid #e2e8f0;border-right:1pt solid #e2e8f0;border-bottom:1pt solid #e2e8f0;border-radius:0 6pt 6pt 0;padding:9pt 11pt}.prompt-script h3,.trouble-box h3,.check-strip h3{font-size:11.5pt;color:#084e8f;margin:0 0 5pt}.prompt-script p{font-size:9.7pt;line-height:1.42;color:#333;margin:0}.trouble-box{background:#fff;border:1pt solid #e2e8f0;border-radius:6pt;padding:9pt 10pt;overflow:hidden}.check-strip{background:#073f73;border-radius:6pt;padding:10pt 11pt;color:#fff}.check-strip h3{color:#fff}.check-strip div{display:grid;grid-template-columns:1fr 1fr;gap:6pt}.check-strip span{font-size:9.2pt;background:rgba(255,255,255,.12);border:1pt solid rgba(255,255,255,.18);border-radius:4pt;padding:5pt 6pt}.compact-table{width:100%;border-collapse:collapse}.compact-table th{background:#084e8f;color:#fff;font-size:9pt;text-align:left;padding:5pt 6pt}.compact-table td{font-size:8.7pt;line-height:1.33;color:#333;padding:5pt 6pt;border:1pt solid #e2e8f0;vertical-align:top}.content>.compact-table{height:calc(100% - 64pt);background:#fff;border:1pt solid #dbe7f1}.content>.compact-table th{font-size:10pt;padding:7pt 8pt}.content>.compact-table td{font-size:9.5pt;line-height:1.42;padding:8pt 9pt;vertical-align:middle}.classroom-grid{display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:9pt;height:calc(100% - 64pt)}.classroom-grid .card{margin:0;padding:9pt 10pt}.classroom-grid .card:last-child{grid-column:2/4}.classroom-grid .card h3{font-size:11.5pt}.classroom-grid .card li{font-size:9.5pt;line-height:1.38;margin-bottom:2pt}.troubleshooting-full{height:calc(100% - 64pt);background:#fff;border:1pt solid #e2e8f0;border-radius:6pt;padding:10pt}.troubleshooting-full .compact-table th{font-size:10pt}.troubleshooting-full .compact-table td{font-size:9.4pt;line-height:1.42}.board-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:9pt;height:calc(100% - 64pt)}.board-grid .card{margin:0;padding:9pt 10pt}.board-grid .card h3{font-size:11.5pt}.board-grid .card li{font-size:9.4pt;line-height:1.34}.agentic-map{display:grid;grid-template-columns:.9fr 1.1fr;gap:12pt;height:calc(100% - 64pt)}.agentic-left{display:grid;grid-template-rows:1fr 1fr 1fr;gap:9pt}.agentic-left .card{margin:0;padding:9pt 10pt}.agentic-left .card h3{font-size:11.5pt}.agentic-left .card li{font-size:9pt;line-height:1.32;margin-bottom:2pt}.agentic-flow{background:#fff;border:1pt solid #dbe7f1;border-radius:8pt;padding:13pt;display:grid;grid-template-rows:1fr auto 1fr auto 1fr auto 1fr 1.4fr;gap:7pt;min-height:0}.flow-node{border-radius:8pt;border:1pt solid #dbe7f1;padding:9pt 12pt;display:flex;align-items:center;justify-content:space-between;gap:10pt}.flow-node b{font-size:14pt;color:#084e8f}.flow-node span{font-size:10pt;color:#334155;text-align:right}.flow-node.planner{border-left:5pt solid #084e8f}.flow-node.builder{border-left:5pt solid #ee822f}.flow-node.tester{border-left:5pt solid #75bd42}.flow-node.speaker{border-left:5pt solid #30c0b4}.flow-arrow{text-align:center;color:#ee822f;font-size:16pt;font-weight:800;line-height:1}.agentic-evidence{display:grid;grid-template-columns:1fr 1fr;gap:9pt;min-height:0}.agentic-evidence .card{margin:0;padding:9pt 10pt}.agentic-evidence .card h3{font-size:11.2pt}.agentic-evidence .card li{font-size:8.6pt;line-height:1.26;margin-bottom:1pt}.evolution-grid{display:grid;grid-template-columns:1.42fr .58fr;gap:10pt;height:calc(100% - 64pt)}.evolution-main{display:grid;grid-template-rows:auto 1fr;gap:9pt;min-height:0}.evolution-table{background:#fff;border:1pt solid #e2e8f0;border-radius:6pt;overflow:hidden}.evolution-table .compact-table th{font-size:8.2pt}.evolution-table .compact-table td{font-size:7.7pt;line-height:1.22;padding:3.8pt 5pt}.evolution-bottom{display:grid;grid-template-columns:1fr 1fr;gap:9pt;min-height:0}.evolution-bottom .card{margin:0;padding:9pt 10pt}.evolution-bottom .card h3{font-size:11.3pt}.evolution-bottom .card li{font-size:8.9pt;line-height:1.32;margin-bottom:2pt}.evolution-side{display:grid;grid-template-rows:1fr 1fr 1fr;gap:8pt}.evolution-side .card{margin:0;padding:8pt 9pt}.evolution-side .card h3{font-size:11.2pt}.evolution-side .card li{font-size:8.8pt;line-height:1.32;margin-bottom:2pt}.evolution-explain{display:grid;grid-template-columns:.82fr 1.18fr;gap:12pt;height:calc(100% - 64pt)}.evolution-steps{display:grid;grid-template-rows:repeat(5,1fr);gap:6pt;min-height:0}.evolution-steps .card{margin:0;padding:7pt 8pt}.evolution-steps .card h3{font-size:10.8pt;margin-bottom:3pt}.evolution-steps .card li{font-size:8.15pt;line-height:1.22;margin-bottom:1pt}.evolution-image-wrap{display:grid;grid-template-rows:minmax(0,1fr) auto;gap:6pt;background:#fff;border:1pt solid #dbe7f1;border-radius:8pt;padding:8pt;min-height:0}.evolution-image-wrap img{width:100%;height:100%;object-fit:contain;border-radius:5pt;cursor:zoom-in}.zoom-hint{font-size:9pt;color:#5b6b7a;text-align:center}.image-zoom-overlay{position:fixed;inset:0;background:rgba(6,18,30,.94);z-index:9999;overflow:auto;padding:30px;cursor:grab}.image-zoom-overlay.dragging{cursor:grabbing}.image-zoom-stage{min-width:100%;min-height:100%;display:flex;align-items:center;justify-content:center}.image-zoom-overlay img{max-width:none;max-height:none;width:auto;height:auto;transform-origin:center center;image-rendering:auto;box-shadow:0 20px 70px rgba(0,0,0,.45);cursor:zoom-in}.timeline-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:8pt;height:calc(100% - 64pt)}.timeline-grid .card{margin:0;padding:9pt 9pt}.timeline-grid .card h3{font-size:17pt;margin-bottom:6pt}.timeline-grid .card li{font-size:8.7pt;line-height:1.34;margin-bottom:3pt}.video-grid{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1.12fr .88fr;gap:10pt;height:calc(100% - 64pt)}.video-grid .card{margin:0;padding:10pt 12pt;overflow:hidden}.video-grid .card:nth-child(n+3){padding:9pt 10pt}.video-grid .card:nth-child(3){grid-column:1/2}.video-grid .card:nth-child(4){grid-column:2/3}.video-grid .card:nth-child(5){grid-column:1/3}.video-grid .card h3{font-size:12pt}.video-grid .card li{font-size:9.2pt;line-height:1.34;margin-bottom:2pt}.term-video-grid{display:grid;grid-template-columns:1.18fr .82fr;gap:12pt;height:calc(100% - 64pt)}.video-panel{background:#071522;border-radius:8pt;padding:8pt;box-shadow:0 10pt 24pt rgba(7,21,34,.18)}.video-panel video{width:100%;height:100%;object-fit:contain;border-radius:5pt;background:#000}.term-video-side{display:grid;grid-template-rows:1fr 1fr 1fr;gap:8pt}.term-video-side .card{margin:0;padding:9pt 10pt}.term-video-side .card h3{font-size:11.5pt}.term-video-side .card li{font-size:9.1pt;line-height:1.34;margin-bottom:2pt}.term-board{height:calc(100% - 64pt);display:grid;grid-template-rows:auto 1fr;gap:8pt}.term-table-wrap{background:#fff;border:1pt solid #e2e8f0;border-radius:6pt;overflow:hidden}.term-board .compact-table th{font-size:7.8pt;padding:3.8pt 5pt}.term-board .compact-table td{font-size:7.05pt;line-height:1.15;padding:3pt 5pt}.term-bottom{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8pt;min-height:0}.term-bottom .card{margin:0;padding:8pt 9pt}.term-bottom .card h3{font-size:11pt}.term-bottom .card li{font-size:8.7pt;line-height:1.28;margin-bottom:1.5pt}.source-link{font-size:13pt!important;font-weight:800;margin:0 0 10pt}.source-link a{color:#084e8f;text-decoration:none;border-bottom:1.5pt solid #ee822f}.cover-course-meta{display:flex;align-items:center;gap:18pt;color:#334155}.cover-course-meta span{font-size:10.5pt;color:#334155}.cover-course-meta b{display:inline-block;margin-right:4pt;color:#084e8f;font-weight:800}.content{padding:12pt 26pt}.page-title{font-size:21pt;margin-bottom:9pt}.kicker{margin-bottom:5pt}.card p,.card li{font-size:10pt}.image-slide{height:calc(100% - 64pt)}.content-enter>*{opacity:1!important;transform:none!important;animation:none!important}.slide{background:linear-gradient(135deg,#f6f9fc 0%,#eef5fb 100%)}.slide-header{box-shadow:0 1pt 0 rgba(8,78,143,.08)}.card,.prompt-script,.trouble-box,.compare-col,.rubric-item,.check-strip{box-shadow:0 8pt 22pt rgba(8,78,143,.055)}.page-title{letter-spacing:0}.kicker p{color:#d96f19}.compact-table th{background:#073f73}.compact-table tr:nth-child(even) td{background:#f8fbff}
"""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Day {day:02d} · {escape(title)}</title>
<style>{css}
{extra_css}</style>
</head>
<body>
<div class="deck-container"><div class="slide-wrapper" id="slideWrapper">
{''.join(slides)}
</div></div>
<script>
function resizeSlides(){{
  const wrapper=document.getElementById('slideWrapper');
  const scale=Math.min(window.innerWidth/(960*1.333),window.innerHeight/(540*1.333));
  wrapper.style.transform='scale('+scale+')';
}}
window.addEventListener('resize',resizeSlides);resizeSlides();
let currentSlide=1;const totalSlides={len(slides)};
function showSlide(n){{document.querySelectorAll('.slide').forEach(s=>s.classList.remove('active'));const el=document.getElementById('slide-'+n);if(el)el.classList.add('active');}}
function nextSlide(){{if(currentSlide<totalSlides){{currentSlide++;showSlide(currentSlide);}}}}
function prevSlide(){{if(currentSlide>1){{currentSlide--;showSlide(currentSlide);}}}}
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight'||e.key===' ')nextSlide();if(e.key==='ArrowLeft')prevSlide();}});
let zoomScale=1,zoomDragging=false,zoomStartX=0,zoomStartY=0,zoomScrollX=0,zoomScrollY=0;
function closeImageZoom(){{const overlay=document.querySelector('.image-zoom-overlay');if(overlay)overlay.remove();}}
function setZoomScale(scale){{const img=document.querySelector('.image-zoom-overlay img');if(!img)return;zoomScale=Math.max(.5,Math.min(5,scale));img.style.transform='scale('+zoomScale+')';}}
function openImageZoom(img){{closeImageZoom();zoomScale=1;const overlay=document.createElement('div');overlay.className='image-zoom-overlay';const stage=document.createElement('div');stage.className='image-zoom-stage';const clone=document.createElement('img');clone.src=img.currentSrc||img.src;clone.alt=img.alt||'';stage.appendChild(clone);overlay.appendChild(stage);overlay.addEventListener('wheel',e=>{{e.preventDefault();setZoomScale(zoomScale+(e.deltaY<0?.2:-.2));}},{{passive:false}});overlay.addEventListener('mousedown',e=>{{zoomDragging=true;overlay.classList.add('dragging');zoomStartX=e.clientX;zoomStartY=e.clientY;zoomScrollX=overlay.scrollLeft;zoomScrollY=overlay.scrollTop;}});window.addEventListener('mousemove',e=>{{if(!zoomDragging)return;overlay.scrollLeft=zoomScrollX-(e.clientX-zoomStartX);overlay.scrollTop=zoomScrollY-(e.clientY-zoomStartY);}});window.addEventListener('mouseup',()=>{{zoomDragging=false;overlay.classList.remove('dragging');}});clone.addEventListener('click',e=>{{e.stopPropagation();setZoomScale(zoomScale>=2?1:zoomScale+1);}});overlay.addEventListener('dblclick',e=>{{e.stopPropagation();closeImageZoom();}});document.body.appendChild(overlay);}}
document.addEventListener('keydown',e=>{{if(e.key==='Escape')closeImageZoom();}});
document.addEventListener('click',e=>{{const zoomImg=e.target.closest('[data-zoomable="true"]');if(zoomImg){{e.stopPropagation();openImageZoom(zoomImg);return;}}if(e.target.closest('.image-zoom-overlay'))return;const active=document.querySelector('.slide.active');if(!active)return;const r=active.getBoundingClientRect();const x=e.clientX-r.left;if(x>r.width*.7)nextSlide();else if(x<r.width*.3)prevSlide();}});
</script>
</body>
</html>"""


def build_day_1():
    day, total = 1, 16
    slides = [
        cover(day, total, "AI 基础操作与信息整理", "从会聊天，到会查证、会整理、会复盘", ["案例 1 AI 搜索侦探", "案例 2 知识卡片", "提示词清单 v1"]),
        schedule_slide(day, 2, total, [
            ("08:30-09:50", "开场 + AI 使用底线 + 案例 1 教师完整演示"),
            ("10:05-11:25", "案例 1 学生换题实操，完成调研卡片"),
            ("13:00-14:20", "案例 2 教师演示：杂乱资料整理成知识卡片"),
            ("14:35-15:55", "案例 2 学生实操 + 互评 + 提示词清单 v1"),
        ], ["1 页调研卡片", "1 页知识卡片", "提示词清单 v1", "问题记录表"]),
        drill_slide(day, 3, total, "开场 20 分钟：先建立课堂规则", ["5 分钟：问学生平时怎么用 AI", "5 分钟：展示同一个问题的好坏提示词", "5 分钟：说明事实/观点/判断", "5 分钟：发放今日材料"], ["现场投屏，不讲 AI 发展史", "明确今天只看输出质量", "要求学生保留每次提示词"], ["打开 QClaw 或同类搜索工具", "新建今日文件夹", "准备记录“问题-提示词-结果”"], ["今日练习文件夹", "个人提示词记录表"], ["能打开工具", "知道今天要交什么", "能区分来源和结论"]),
        slide_shell(day, 4, total, "最小理论", "只讲能马上用的 4 个概念", three_col([
            card("任务说明", ul(["你要 AI 做什么", "给谁用", "输出成什么格式", "有哪些限制"]), "primary"),
            card("上下文材料", ul(["把题目、背景、样例给足", "没有材料就不要让 AI 编", "让 AI 先问缺什么"]), "accent"),
            card("检查意识", ul(["来源是否存在", "结论是否过时", "有没有把观点当事实"]), "success"),
        ])),
        runbook_slide(day, 5, total, 1, "AI 搜索侦探", "QClaw / 支持联网检索的 AI 搜索工具", ["讲师准备 3 个可选主题", "学生准备一个记录文档", "要求所有结果都必须带来源"], ["输入一个很差的提示词：帮我查 AI 工具", "让学生评价为什么不能直接交", "改成结构化提示词并执行", "点开 2 个来源，示范如何核对", "把结论改写成调研卡片"], ["选择一个主题", "复制进阶提示词并替换主题", "保留 3 条有来源的结论", "写出 1 条自己的判断", "标记 1 条不确定信息"], "请围绕【主题】做快速调研，输出 5 条结论。每条必须包含：结论、证据、来源链接、适用场景、不确定性。最后请用 3 句话总结我可以怎么使用这些信息。", [("AI 不给来源", "追问：请补充每条结论的来源链接；没有来源的结论单独列出"), ("来源打不开", "换一个来源，或把该条标记为待确认"), ("结果太泛", "限制时间、对象和输出字段，例如“面向大学生就业”")]),
        drill_slide(day, 6, total, "案例 1 学生实操：从主题到卡片", ["10 分钟：选题和写提示词", "20 分钟：检索并核对来源", "20 分钟：整理调研卡片", "20 分钟：同桌互查"], ["巡场只问 3 个问题：主题是什么、来源在哪、你的判断是什么", "发现空泛答案时现场改提示词", "挑 1 个好例子投屏"], ["主题三选一或自选", "每条结论保留来源", "同桌检查来源是否能打开"], ["1 页调研卡片", "至少 3 条来源", "1 条不确定信息"], ["结论和来源分开", "没有大段复制", "能说出自己的判断"]),
        troubleshooting_slide(day, 7, total, "案例 1 常见翻车点", [("学生直接复制 AI 大段回答", "没有理解结构化输出", "要求改成四列表格：结论/证据/来源/我的判断"), ("学生只找到了广告软文", "不会筛选来源", "示范优先看官网、媒体报道、机构报告，软文只能做参考"), ("学生不知道选什么主题", "任务太开放", "给模板：某工具变化、某职业影响、某 App 爆火原因")]),
        runbook_slide(day, 8, total, 2, "一键整理资料包", "QClaw + 文档编辑器 / WorkBuddy 文档处理", ["讲师准备一份混合资料：网页摘录、聊天记录、课程笔记", "资料里故意放重复和无关内容", "学生复制到同一个文档"], ["先让 AI 不加限制地总结一次", "指出问题：像文章、不能复习、没有行动", "要求按知识卡片重新整理", "示范人工删除空话", "补充“我还不懂的问题”"], ["导入资料包", "生成第一版知识卡片", "删除重复和空话", "补充自己的问题", "保存为 Day1-知识卡片"], "请把下面资料整理成知识卡片，字段包括：主题摘要、关键概念、能用在什么任务里、下一步行动、我还不懂的问题。要求每条不超过 2 行，不要写成长文章。", [("整理结果像作文", "明确要求卡片字段和每条字数"), ("AI 漏掉重要内容", "让 AI 先列资料目录，再逐段整理"), ("学生不知道怎么二次整理", "要求每人删掉 3 句废话、补 2 个自己的问题")]),
        drill_slide(day, 9, total, "案例 2 教师演示：资料先分类，再总结", ["8 分钟：展示杂乱资料", "12 分钟：AI 初步分类", "15 分钟：生成知识卡片", "10 分钟：人工二次整理", "10 分钟：展示成品"], ["边操作边解释为什么要先分类", "故意保留一个错误让学生发现", "强调最终材料是学生自己的笔记"], ["跟随教师同屏操作", "在自己的文档中记录分类结果", "标出不懂的问题"], ["知识卡片初稿", "分类目录", "疑问清单"], ["不是整段复制", "有行动项", "有疑问"]),
        practice_slide(day, 10, total, "案例 2 学生换资料练习", ["领取第二份资料包", "先让 AI 输出资料目录", "再生成知识卡片", "人工删改至少 5 处", "同桌互评"], ["摘要能复习", "分类不是乱列标题", "行动清单具体", "问题不是空泛的“我还不懂”"], "结构化知识卡片"),
        slide_shell(day, 11, total, "提示词拆解", "今天所有提示词都按 5 段写", five_prompt := compact_table(["字段", "写法", "例子"], [
            ("角色", "让 AI 扮演谁", "你是课程助教/资料整理员"),
            ("任务", "要完成什么", "整理成一页知识卡片"),
            ("材料", "给它看什么", "下面是网页摘录和课堂笔记"),
            ("格式", "输出成什么", "表格：摘要/概念/行动/问题"),
            ("限制", "不能做什么", "不要编造、每条不超过 2 行"),
        ])),
        slide_shell(day, 12, total, "课堂互评", "互评不是看谁写得多，而是看谁能用", two_col(
            card("互评问题", ul(["我能不能 30 秒看懂主题？", "有没有来源或依据？", "能不能指导下一步行动？", "哪些句子是空话？"]), "primary"),
            card("投屏点评", ul(["选一份好卡片", "选一份问题卡片", "现场改提示词", "让学生看到修改前后差异"]), "accent"),
        )),
        slide_shell(day, 13, total, "今日沉淀", "建立个人提示词清单 v1", three_col([
            card("搜索类", ul(["主题 + 时间范围", "结论 + 来源", "事实/观点分开"]), "primary"),
            card("整理类", ul(["先分类", "再卡片化", "最后人工删改"]), "accent"),
            card("纠错类", ul(["太泛就加对象", "太长就限字数", "没来源就追问"]), "success"),
        ])),
        troubleshooting_slide(day, 14, total, "Day 1 课堂控场问题", [("学生只聊天不做产出", "任务边界不清", "每 20 分钟收一次中间产物：主题、来源、卡片"), ("学生认为 AI 说的都对", "缺少查证意识", "要求每组找出 1 条不确定信息"), ("学生跟不上工具操作", "窗口太多", "只保留 AI 工具和一个文档，讲师投屏同步")]),
        slide_shell(day, 15, total, "提交标准", "Day 1 下课前检查清单", three_col([
            card("调研卡片", ul(["主题明确", "3 条来源", "1 条判断", "1 条不确定信息"]), "success"),
            card("知识卡片", ul(["摘要", "概念", "行动", "问题", "人工删改痕迹"]), "success"),
            card("提示词记录", ul(["基础版", "进阶版", "纠错版", "至少 3 条"]), "success"),
        ])),
        summary_slide(day, 16, total, ["会让 AI 带来源地查资料", "会把杂乱材料整理成可复习卡片", "开始记录自己的可复用提示词"], "明天进入 AI 办公自动化：用 WorkBuddy 处理表格、发现异常、生成正式周报。"),
    ]
    return "AI 基础操作与信息整理", slides


def build_day_2():
    day, total = 2, 16
    slides = [
        cover(day, total, "AI 办公自动化", "让 AI 处理表格、生成报告、减少重复劳动", ["案例 3 Excel 救火队", "案例 4 自动周报", "不编造原则"]),
        schedule_slide(day, 2, total, [
            ("08:30-09:50", "案例 3：人工找错 + WorkBuddy 找错，建立脏数据意识"),
            ("10:05-11:25", "案例 3：清洗、生成异常说明和数据摘要"),
            ("13:00-14:20", "案例 4：从任务记录生成正式周报"),
            ("14:35-15:55", "三种对象版本 + 事实核查 + 日终提交"),
        ], ["清洗后的表格", "异常问题清单", "100 字数据摘要", "正式周报"]),
        drill_slide(day, 3, total, "开场 15 分钟：先让学生人工找错", ["5 分钟：发放乱表", "5 分钟：学生圈出问题", "5 分钟：汇总空值、重复、格式、异常"], ["不要一开始就开 AI", "让学生先感受人工找错的低效", "把错误类型写在白板上"], ["打开表格文件", "先不使用 AI", "用颜色标出疑似问题"], ["人工问题清单"], ["至少找到 3 个问题", "能说出为什么是问题"]),
        runbook_slide(day, 4, total, 3, "Excel 救火队", "WorkBuddy / Excel / WPS 表格", ["准备含空值、重复、日期混乱、金额异常的模拟表", "保留原始表，不直接覆盖", "要求学生截图或复制清洗前后对比"], ["导入表格到 WorkBuddy", "要求 AI 先输出问题清单，不允许直接改", "逐项确认清洗动作", "生成清洗说明", "让 AI 写 100 字摘要"], ["上传或打开表格", "先让 AI 找问题", "确认后执行清洗", "把修改说明复制到文档", "生成摘要并人工核对"], "请检查这份表格的空值、重复项、日期格式、分类字段和异常数值。先输出问题清单和修改建议，不要直接删除数据；等我确认后再给清洗步骤。", [("AI 直接改数据", "要求先列问题和理由，再确认执行"), ("摘要出现不存在的数据", "让学生用原表核对数字，删除无依据句子"), ("学生找不到清洗前后差异", "要求复制一份原始表，清洗只在副本上做")]),
        drill_slide(day, 5, total, "案例 3 教师演示：完整清洗流程", ["10 分钟：导入和问题扫描", "15 分钟：确认清洗策略", "15 分钟：执行清洗并保存副本", "15 分钟：生成摘要和异常说明"], ["每做一步都说明为什么", "强调原始数据不可丢", "演示如何让 AI 停下来先解释"], ["跟随同屏完成", "记录每一类问题", "保存清洗副本"], ["清洗表", "异常说明", "数据摘要"], ["原始表保留", "异常有解释", "摘要不编造"]),
        troubleshooting_slide(day, 6, total, "案例 3 常见问题", [("学生上传不了文件", "工具权限或文件格式问题", "改用复制表格片段；或保存为 xlsx/csv 后重试"), ("AI 把空值随便补了", "没有设置约束", "提示：缺失值只标记，不允许自动猜测填充"), ("日期格式越改越乱", "区域格式混杂", "先统一目标格式：YYYY-MM-DD，再让 AI 生成转换规则")]),
        practice_slide(day, 7, total, "案例 3 学生实操", ["领取第二份乱表", "人工找 3 个问题", "用 WorkBuddy 找问题", "执行清洗并写说明", "生成 100 字数据摘要"], ["至少发现 4 类问题", "清洗动作可解释", "保留原始表", "摘要有数字依据"], "清洗表格 + 异常问题清单 + 摘要"),
        slide_shell(day, 8, total, "办公理论", "数据到报告，中间必须经过人工审核", three_col([
            card("AI 擅长", ul(["发现模式", "批量整理", "生成摘要", "改写措辞"]), "primary"),
            card("人要负责", ul(["确认数据含义", "判断异常是否合理", "决定是否删除", "承担最终报告责任"]), "accent"),
            card("课堂红线", ul(["不能覆盖原始表", "不能编造缺失数据", "不能不看就提交"]), "success"),
        ])),
        runbook_slide(day, 9, total, 4, "自动周报生成器", "WorkBuddy / 文档 AI / WPS 文档", ["准备一周任务记录：日期、事项、完成状态、问题备注", "明确读者：老师/领导/同学", "给出四段式周报模板"], ["导入任务记录", "指定读者为老师", "生成四段式周报", "现场找出夸大句", "改成领导版和同学版"], ["选择读者", "生成周报初稿", "删除无依据成绩", "调整语气", "输出最终版"], "请根据以下任务记录生成给【老师/领导】看的周报。结构：本周完成、遇到问题、下周计划、需要支持。语气正式，不要编造记录中没有的数据。", [("周报像口号", "要求每一句都对应原始记录"), ("语气不合适", "指定读者和场景：给老师/领导/同学"), ("问题被写得太严重", "要求分为已解决、待解决、需要支持")]),
        drill_slide(day, 10, total, "案例 4 教师演示：同一材料三种写法", ["10 分钟：生成老师版", "10 分钟：指出问题和润色", "10 分钟：生成领导版", "10 分钟：生成同学协作版", "10 分钟：对比差异"], ["投屏对比三版差异", "标红 AI 编造句", "让学生判断哪版适合谁"], ["记录三版差异", "圈出夸张表达", "修改最终版"], ["三版周报", "事实核查记录"], ["结构完整", "对象明确", "无编造"]),
        prompt_slide(day, 11, total, "案例 4 纠错提示词", "请写正式一点。", "请把这份周报改成给学院老师看的版本。要求：语气正式、保留真实问题、不要夸大成果、每段控制在 80 字以内。", "你加入了记录中没有的数据和成绩。请删除无依据内容，只基于我提供的任务记录重写。"),
        troubleshooting_slide(day, 12, total, "案例 4 常见问题", [("学生不愿写问题", "担心显得做得不好", "解释：报告不是报喜，问题和计划能体现成熟度"), ("AI 写得很浮夸", "提示词没有限制", "加入“不要夸大、不要编造、只基于记录”"), ("周报太长", "没有字数限制", "要求每段 60-80 字，适合微信或邮件发送")]),
        practice_slide(day, 13, total, "案例 4 学生实操", ["把自己的表格摘要转为周报", "生成老师版和领导版", "标记 3 处需要人工审核的句子", "提交最终版"], ["四段结构", "语气匹配对象", "问题和计划具体", "没有虚构事实"], "正式周报 + 事实核查记录"),
        slide_shell(day, 14, total, "课堂互评", "两组互换周报，专门找“编造句”", two_col(
            card("互评任务", ul(["找 1 句没有数据依据的话", "找 1 句语气不合适的话", "找 1 个下周计划不具体的问题"]), "primary"),
            card("修改动作", ul(["删除无依据内容", "补充真实数据来源", "把空话改成动作"]), "accent"),
        )),
        slide_shell(day, 15, total, "提交标准", "Day 2 下课前检查清单", three_col([
            card("表格", ul(["原始表", "清洗副本", "异常说明"]), "success"),
            card("摘要", ul(["100 字以内", "数字有依据", "不编造"]), "success"),
            card("周报", ul(["四段结构", "对象明确", "人工审核痕迹"]), "success"),
        ])),
        summary_slide(day, 16, total, ["会用 AI 发现并清洗表格问题", "会把任务记录转成正式周报", "知道办公自动化必须保留人工审核"], "明天进入 Vibe Design 和 Vibe Coding：把内容变成可展示页面。"),
    ]
    return "AI 办公自动化", slides


def build_day_3():
    day, total = 3, 17
    slides = [
        cover(3, total, "Vibe Design + Vibe Coding 入门", "先做视觉方案，再进入自然语言生成页面", ["案例 5 Vibe Design", "案例 6 页面生成", "演进图总览"]),
        schedule_slide(3, 2, total, [
            ("08:30-09:50", "案例 5：Vibe Design，活动海报/页面首屏方案"),
            ("10:05-11:25", "案例 5：审美反馈与二次迭代，形成设计说明"),
            ("13:00-14:20", "演进图只出现一次：解释 Vibe Coding 位置，再写页面需求"),
            ("14:35-15:55", "案例 6：用 Trae 生成第一个单页 HTML 页面"),
        ], ["视觉方案", "修改前后对比", "页面需求说明", "单页 HTML 雏形"]),
        runbook_slide(3, 3, total, 5, "Vibe Design 视觉方案", "QClaw / 图像生成工具 / Trae 设计预览", ["准备 4 个主题：AI 分享会、个人作品集、社团招新、小组项目发布页", "给学生看一个好案例和一个差案例", "明确只做视觉方案，不急着做代码"], ["选主题：校园 AI 工具分享会", "定义受众：大学生、零基础、想提升效率", "让 AI 输出风格、文案、配色、布局", "指出第一版哪里像模板", "要求第二版减少装饰、增强层级"], ["选择主题", "写出受众和用途", "生成第一版方案", "写 3 条修改意见", "生成第二版并保存"], "请为【主题】设计一个活动海报/网页首屏方案。受众是【受众】，目标是【目标】。请输出：主标题、副标题、核心卖点、视觉风格、颜色、布局、图片建议和不适合使用的元素。", [("学生只说高级一点", "要求把高级拆成留白、字体、颜色、层级"), ("AI 给的文案太营销", "指定受众和语气：校园、清楚、不夸张"), ("颜色太乱", "限制主色 1 个、辅助色 1 个、强调色 1 个")]),
        drill_slide(3, 4, total, "案例 5 课堂节奏：设计先讲判断标准", ["10 分钟：好坏设计对比", "20 分钟：教师生成第一版", "20 分钟：教师带着改第二版", "30 分钟：学生自己做"], ["不要求学生会 PS/Figma", "重点问：第一眼知道主题吗", "现场改 1 个学生方案"], ["写主题和受众", "生成两版设计", "记录修改理由"], ["视觉方案", "修改前后对比"], ["标题清楚", "颜色不超过 3 种", "文案可直接上屏"]),
        troubleshooting_slide(3, 5, total, "案例 5 常见问题", [("页面看起来像模板", "提示词只给了主题，没有给受众和限制", "加入受众、场景、禁用元素和参考风格"), ("文案太长", "没有给版面限制", "要求主标题 12 字以内、副标题 24 字以内"), ("学生不会评价好坏", "缺少标准", "只用 4 个标准：看懂、重点、对齐、留白")]),
        practice_slide(3, 6, total, "案例 5 学生实操", ["从 4 个主题选 1 个", "生成第一版视觉方案", "写 3 条具体修改意见", "生成第二版", "同桌讲清楚为什么更好"], ["受众明确", "文案短", "风格具体", "有修改前后差异"], "视觉方案 + 修改记录"),
        image_slide(3, 7, total, "演进图总览", "从 Vibe Coding 到 Agentic Engineering", "vibe-agentic-evolution.jpg", "这张图只在 Day 3 做第一次总览：今天进入 Vibe Coding，Day 5 再讲 Agentic Engineering。"),
        slide_shell(3, 8, total, "概念落地", "学生只需要听懂这 3 个层级", three_col([
            card("Vibe Design", ul(["描述视觉感受", "生成风格和文案", "用反馈迭代"]), "accent"),
            card("Vibe Coding", ul(["描述功能和页面", "AI 生成可运行代码", "打开测试再修改"]), "primary"),
            card("Agentic Engineering", ul(["明确目标和验收", "拆角色和流程", "记录迭代证据"]), "success"),
        ])),
        runbook_slide(3, 9, total, 6, "Vibe Coding 页面生成", "Trae Builder / Trae IDE", ["学生安装并打开 Trae", "准备上午的视觉方案", "准备一个项目文件夹", "只要求单文件 HTML"], ["新建项目文件夹", "输入页面需求", "要求 AI 生成单文件 HTML", "打开预览", "检查标题、卡片、按钮"], ["把视觉方案改成页面需求", "在 Trae 中生成 HTML", "保存并预览", "记录 3 个问题", "让 AI 修第一处问题"], "请创建一个单文件 HTML 页面，主题是【主题】。页面需要包含：顶部标题、副标题、3 个内容卡片、一个按钮、点击按钮后的提示。风格参考我上午的设计方案，要求可直接在浏览器打开。", [("Trae 生成多个文件", "补充：所有 HTML/CSS/JS 写在一个文件里"), ("按钮没反应", "让 AI 检查 click 事件绑定"), ("页面太花", "要求减少颜色、卡片固定宽度、增加留白")]),
        drill_slide(3, 10, total, "案例 6 教师演示：从需求到页面", ["10 分钟：写需求清单", "15 分钟：Trae 生成代码", "10 分钟：打开预览", "15 分钟：发现问题并修第一轮", "10 分钟：保存版本"], ["强调需求越具体越好", "不要解释代码细节", "只解释结构、样式、交互"], ["跟着创建文件夹", "复制提示词", "打开预览", "记录问题"], ["HTML 页面 v1", "问题记录"], ["能打开", "按钮有反应", "页面主题清楚"]),
        prompt_slide(3, 11, total, "案例 6 提示词升级", "帮我做一个网页。", "请基于以下视觉方案，生成一个适合课堂展示的单文件 HTML 页面。页面结构：Hero、3 个亮点卡片、流程区、行动按钮。按钮点击后弹出提示。请保证文字不溢出、移动端也能看。", "页面生成了但不好看。请保持内容不变，只调整排版：标题更突出、卡片对齐、颜色控制在 3 种以内、按钮状态明显。"),
        troubleshooting_slide(3, 12, total, "案例 6 常见问题", [("学生复制代码不知道放哪里", "没有项目文件夹概念", "讲师统一要求：新建 day03-tool/index.html"), ("页面打开是乱码", "编码或保存格式问题", "确认文件 UTF-8，后缀是 .html"), ("页面空白", "代码缺失或 JS 报错", "让 Trae 检查完整 HTML 结构和控制台错误")]),
        practice_slide(3, 13, total, "案例 6 学生实操：页面雏形", ["把自己的视觉方案转成页面需求", "用 Trae 生成 HTML", "打开浏览器预览", "记录 3 个问题", "修 1 个最明显问题"], ["单文件", "可打开", "内容不是空白", "按钮有反馈"], "HTML 页面雏形 + 问题记录"),
        slide_shell(3, 14, total, "互评标准", "页面不是越花越好，先保证能讲清楚", three_col([
            card("第一眼", ul(["知道主题", "知道面向谁", "知道要做什么"]), "primary"),
            card("可读性", ul(["字号够大", "文字不溢出", "卡片不重叠"]), "accent"),
            card("可操作", ul(["按钮能点", "反馈明确", "链接或提示可用"]), "success"),
        ])),
        project_board(3, 15, total, "从今天开始为综合项目留素材", [
            ("可复用素材", ["主题文案", "风格描述", "页面结构", "按钮逻辑"], "primary"),
            ("记录证据", ["提示词", "截图", "修改意见", "版本文件"], "accent"),
            ("明天继续", ["加功能", "修 Bug", "做小工具", "写测试"], "success"),
            ("不要做", ["追求复杂后端", "换太多主题", "无节制装饰", "不保存版本"], "primary"),
        ]),
        slide_shell(3, 16, total, "提交标准", "Day 3 下课前检查清单", three_col([
            card("视觉方案", ul(["主题", "受众", "配色", "布局", "文案"]), "success"),
            card("HTML 页面", ul(["单文件", "能打开", "按钮可点", "无明显重叠"]), "success"),
            card("修改记录", ul(["第一版问题", "修改提示词", "第二版截图"]), "success"),
        ])),
        summary_slide(3, 17, total, ["会用自然语言描述设计", "会把设计方案转成页面需求", "会用 Trae 生成第一个可展示页面"], "明天进入 Vibe Coding 深度：完成可运行小工具，并系统学习 Bug 修理。"),
    ]
    return "Vibe Design + Vibe Coding 入门", slides


def build_day_4():
    day, total = 4, 16
    slides = [
        cover(4, total, "Vibe Coding 深度 + Bug 修理铺", "让学生做出可运行小工具，并学会让 AI 修错", ["案例 6 深化", "案例 7 Debug", "可运行小工具"]),
        schedule_slide(4, 2, total, [
            ("08:30-09:50", "案例 6 深化：待办/随机分组/预算计算器三选一"),
            ("10:05-11:25", "功能增强：输入、按钮、统计、状态变化"),
            ("13:00-14:20", "案例 7：Bug 修理铺，老师提供故障页面"),
            ("14:35-15:55", "学生修自己的小工具，完成修复记录"),
        ], ["小工具 v1", "小工具 v2", "Bug 描述清单", "最终小工具"]),
        slide_shell(4, 3, total, "最小理论", "网页小工具只看 3 件事", three_col([
            card("结构", ul(["页面有哪些区域", "标题、输入框、按钮、结果区"]), "primary"),
            card("样式", ul(["颜色、间距、字号", "能读、整齐、不重叠"]), "accent"),
            card("交互", ul(["点击后发生什么", "输入后输出什么"]), "success"),
        ])),
        runbook_slide(4, 4, total, 6, "Vibe Coding 小工具", "Trae Builder / Trae IDE / 浏览器预览", ["准备 3 个工具选题：待办清单、随机分组、预算计算器", "统一要求单文件 HTML", "准备测试清单：输入、点击、删除、刷新"], ["选择待办清单做示范", "把功能拆成输入、处理、输出", "要求 AI 先做 MVP", "打开页面测试 3 次", "只增加一个关键功能"], ["三选一确定方向", "写功能清单", "用 Trae 生成 MVP", "逐个测试按钮", "记录失败现象"], "请做一个单文件 HTML【工具名称】。必须包含：输入区、操作按钮、结果区、清空/删除功能、状态统计。无需后端，可直接在浏览器打开。请先做最小可用版本，不要加入复杂功能。", [("AI 一次做太复杂", "要求先做 MVP：一个输入、一个按钮、一个结果"), ("按钮没反应", "让 AI 检查事件绑定和元素 id"), ("页面刷新后数据丢失", "先说明这是正常现象；进阶再加 localStorage")]),
        drill_slide(4, 5, total, "案例 6 深化：教师带做完整过程", ["10 分钟：写功能清单", "20 分钟：生成 MVP", "15 分钟：浏览器测试", "20 分钟：加一个功能", "15 分钟：保存 v1/v2"], ["不解释每行代码", "解释输入-处理-输出", "让学生看到测试失败也正常"], ["复制需求模板", "生成自己的工具", "按测试清单打勾"], ["小工具 v1", "测试清单"], ["可运行", "至少 2 个交互", "有结果显示"]),
        prompt_slide(4, 6, total, "案例 6 深化提示词", "请帮我做一个小工具。", "请做一个适合大学生课堂使用的随机分组工具。要求：输入名单、设置组数、点击生成分组、显示每组成员、可以复制结果。所有代码写在一个 HTML 文件里。", "现在点击生成按钮没有反应。请检查 JavaScript 事件绑定，只修复按钮功能，并告诉我修改了哪里。"),
        practice_slide(4, 7, total, "学生完成小工具 v1", ["三选一确定工具方向", "写输入/处理/输出", "生成单文件 HTML", "测试每个按钮", "保存 v1"], ["单文件可运行", "至少 2 个交互", "有结果显示", "记录测试结果"], "小工具 v1 + 功能清单"),
        slide_shell(4, 8, total, "功能增强", "从 MVP 到 v2：只加一个关键功能", three_col([
            card("待办清单", ul(["任务统计", "清空已完成", "本地保存"]), "primary"),
            card("随机分组", ul(["设置组数", "避免重复", "复制结果"]), "accent"),
            card("预算计算器", ul(["分类合计", "超支提醒", "图表占位"]), "success"),
        ])),
        runbook_slide(4, 9, total, 7, "Bug 修理铺", "Trae / 浏览器控制台 / 故障 HTML 页面", ["讲师准备一个故障页面", "故障包括按钮无反应、文字溢出、undefined", "要求学生一次只修一个问题"], ["打开故障页面", "演示错误描述：点击按钮无反应", "复制控制台报错或截图描述", "让 AI 只修一个问题", "修完立即重新测试"], ["领取故障页面", "列出 3 个 Bug", "按优先级修第 1 个", "测试通过后再修第 2 个", "记录修改前后"], "点击【按钮名称】后没有任何反应。请检查 HTML/JS 中的按钮事件绑定，只修复这个问题，不要重写整个页面。修复后请说明你改了哪几处。", [("学生只说坏了", "要求写清楚：操作-现象-期望结果"), ("AI 重写整个页面", "补充：保持原样式，只修指定问题"), ("越修越乱", "恢复上一版本，一次只修一个 Bug")]),
        drill_slide(4, 10, total, "案例 7 教师演示：标准 Debug 流程", ["8 分钟：复现问题", "8 分钟：描述现象", "12 分钟：让 AI 定位", "12 分钟：应用修复", "10 分钟：回归测试"], ["强调“先复现再修”", "不要直接相信 AI 解释", "修完必须点击验证"], ["记录操作步骤", "复制错误信息", "保存修复版"], ["Bug 描述", "修复记录", "测试结果"], ["现象具体", "一次一改", "修完能复现通过"]),
        troubleshooting_slide(4, 11, total, "Bug 修理铺常见问题", [("AI 修改后样式变了", "指令范围太大", "补充：保持视觉不变，只修功能"), ("学生不知道控制台在哪", "浏览器工具不熟", "讲师统一演示 F12/右键检查，找 Console"), ("修复一个 Bug 又出新 Bug", "没有版本保存", "要求每次修复前复制一份 v1/v2")]),
        practice_slide(4, 12, total, "学生修自己的小工具", ["列出自己的 3 个问题", "按优先级逐个修", "每修一次就测试一次", "记录修改前后截图", "保存最终版"], ["问题描述具体", "修复步骤清楚", "最终版本可用", "保留修复记录"], "最终小工具 + Bug 修复记录"),
        project_board(4, 13, total, "小工具验收看板", [
            ("功能", ["输入有效", "按钮有效", "结果有效", "删除/清空有效"], "primary"),
            ("视觉", ["标题清楚", "卡片对齐", "文字不溢出", "颜色统一"], "accent"),
            ("测试", ["正常输入", "空输入", "重复输入", "极端输入"], "success"),
            ("证据", ["v1 文件", "v2 文件", "Bug 记录", "截图"], "primary"),
        ]),
        slide_shell(4, 14, total, "今日提交物", "Day 4 提交清单", three_col([
            card("小工具 v2", ul(["可运行", "有交互", "有基本样式"]), "success"),
            card("Bug 记录", ul(["现象", "原因猜测", "修复提示词"]), "success"),
            card("测试清单", ul(["按钮", "输入", "输出", "边界情况"]), "success"),
        ])),
        troubleshooting_slide(4, 15, total, "Day 4 课堂控场问题", [("学生沉迷改颜色", "目标偏离功能", "规定 14:20 前只修功能，不调配色"), ("学生复制同一个工具", "选题太少", "要求至少改主题、字段和按钮逻辑"), ("学生害怕代码", "把任务讲成测试和描述", "提醒：今天考的是描述需求和验证结果，不是背代码")]),
        summary_slide(4, 16, total, ["能用自然语言做可运行小工具", "能描述 Bug 并让 AI 修复", "知道版本保存和测试清单的重要性"], "明天进入 Agentic Engineering：把单个工具升级成综合项目工作流。"),
    ]
    return "Vibe Coding 深度 + Bug 修理铺", slides


def build_day_5():
    day, total = 5, 17
    slides = [
        cover(day, total, "Agentic Engineering + 综合项目", "从生成一个东西，升级为组织 AI 完成复杂任务", ["案例 8 Workflow", "案例 9 综合项目", "目标/约束/验收"]),
        schedule_slide(day, 2, total, [
            ("08:30-09:50", "案例 8：Agentic Workflow 设计，目标、约束、验收标准"),
            ("10:05-11:25", "小组综合项目选题 + 工作流拆解"),
            ("13:00-14:20", "案例 9：综合项目制作 I，资料、内容、页面"),
            ("14:35-15:55", "综合项目制作 II，调试、文档、路演结构"),
        ], ["工作流图", "Demo 初版", "项目说明文档", "PPT 初稿"]),
        image_slide(day, 3, total, "Agentic Engineering", "从 Vibe Coding 升级到 Agentic Engineering", "vibe-agentic-evolution.jpg", "本页重点讲中间偏右区域：Planner、Builder、Tester、Reviewer、Memory/Trace。"),
        slide_shell(day, 4, total, "最小理论", "Agentic Engineering 用学生能听懂的 6 个词", three_col([
            card("目标 Goal", ul(["我们到底要做什么", "谁会使用这个成果"]), "primary"),
            card("约束 Constraint", ul(["时间、工具、能力边界", "不能做什么"]), "accent"),
            card("验收 Acceptance", ul(["做到什么算完成", "怎么判断可用"]), "success"),
            card("拆解 Plan", ul(["先做最小版本", "再逐步增强"]), "primary"),
            card("角色 Agent", ul(["Builder 做", "Tester 查", "Reviewer 评"]), "accent"),
            card("记录 Trace", ul(["问题怎么来", "怎么改过"]), "success"),
        ])),
        runbook_slide(day, 5, total, 8, "Agentic Workflow 设计", "QClaw + WorkBuddy + Trae + 文档工具", ["准备 6 个项目方向", "每组 4-6 人", "统一模板：目标/约束/步骤/角色/验收"], ["选示例：学习资料整理助手", "写目标和用户", "列约束：单文件、当天完成、无后端", "拆成 5 步流程", "分配 Builder/Tester/Reviewer"], ["确定小组主题", "写目标和约束", "拆 5 步流程", "每步写输入输出", "写验收标准"], "我的目标是做一个【项目名称】。限制：今天完成、零基础可做、只用现有 AI 工具、尽量单文件 HTML。请帮我拆成 5 个步骤，并为每一步写输入、输出、负责角色和验收标准。", [("计划太大", "删除登录、数据库、后端、复杂算法"), ("角色不清", "按 Builder/Tester/Writer/Speaker 分工"), ("验收标准空泛", "改成可检查句子：能打开、能点击、能显示结果")]),
        drill_slide(day, 6, total, "案例 8 教师带做：把想法拆成工程任务", ["10 分钟：示范目标卡", "15 分钟：示范约束", "20 分钟：拆 5 步流程", "20 分钟：写验收标准", "15 分钟：小组套模板"], ["反复追问：今天能完成吗", "把大项目砍成 MVP", "不要讲复杂工程术语"], ["用模板填写", "每组派一人读目标", "全班判断是否过大"], ["目标卡", "工作流图"], ["目标具体", "约束明确", "验收可检查"]),
        prompt_slide(day, 7, total, "案例 8 提示词模板", "请帮我规划项目。", "请把这个项目拆成适合 5 小时完成的课堂 MVP。输出表格：步骤、输入、AI 工具、学生要做什么、验收标准、可能风险。不要包含登录、后端、数据库和复杂算法。", "这个计划太复杂。请压缩成今天能完成的版本，只保留核心展示流程，并说明删掉了哪些功能。"),
        practice_slide(day, 8, total, "小组工作流设计", ["确定项目方向", "写目标和约束", "拆 5 步流程", "分配 Builder/Tester/Writer/Speaker", "写验收标准"], ["能一天内完成", "角色清楚", "每一步有输出", "验收标准可检查"], "Agentic Workflow 图"),
        troubleshooting_slide(day, 9, total, "案例 8 常见问题", [("小组想做大平台", "项目范围失控", "强制改成单页面展示或小工具"), ("没人愿意当 Tester", "觉得测试不重要", "说明路演翻车多数来自没测试，Tester 是核心角色"), ("验收标准写“好看”", "不可验证", "改成：字号不小于、按钮能点击、内容不重叠")]),
        slide_shell(day, 10, total, "项目方向", "推荐 6 个低门槛综合项目", three_col([
            card("AI 简历优化小助手", ul(["输入经历", "输出项目描述", "给出改进建议"]), "primary"),
            card("学习资料整理助手", ul(["导入材料", "生成知识卡片", "输出复习清单"]), "accent"),
            card("校园活动展示页", ul(["活动信息", "亮点卡片", "报名按钮"]), "success"),
            card("热点摘要看板", ul(["主题调研", "摘要卡片", "来源列表"]), "primary"),
            card("小组任务管理看板", ul(["成员任务", "状态统计", "风险提示"]), "accent"),
            card("个人作品集生成器", ul(["项目列表", "技能标签", "展示页面"]), "success"),
        ])),
        runbook_slide(day, 11, total, 9, "小组综合项目", "QClaw 搜集 + WorkBuddy 整理 + Trae 构建 + 文档工具路演", ["每组选择一个主题", "必须保留提示词和截图", "Demo 优先单文件或可直接打开"], ["示范项目目录结构", "用 QClaw 搜集内容", "用 WorkBuddy 整理成文案/数据", "用 Trae 生成页面", "用测试清单修关键 bug"], ["按角色分工", "先做资料和页面结构", "生成 Demo 初版", "测试核心流程", "写说明文档和 PPT"], "请根据我们的项目目标和资料，生成一个课堂路演用的单页 Demo。要求包含：项目背景、核心功能、操作流程、成果展示、团队分工。先保证能打开和能演示，不要做登录和后端。", [("内容和 Demo 脱节", "先写页面结构，再填内容"), ("成员都在改同一文件", "指定一个 Builder 合并，其他人写文案/测试"), ("最后没有 PPT", "用 5 页结构先出文字版：痛点/方案/流程/Demo/反思")]),
        project_board(day, 12, total, "案例 9 制作看板：四条线并行", [
            ("资料线", ["QClaw 搜集", "记录来源", "整理结论", "删掉无关内容"], "primary"),
            ("内容线", ["WorkBuddy 整理", "生成说明", "写页面文案", "准备 PPT"], "accent"),
            ("Demo 线", ["Trae 生成", "测试按钮", "修布局", "保存版本"], "success"),
            ("展示线", ["分工", "演示脚本", "备用截图", "问答准备"], "primary"),
        ]),
        practice_slide(day, 13, total, "综合项目制作 I：先跑通", ["用 AI 搜集/整理项目内容", "确定页面结构", "生成 Demo 初版", "保存所有提示词", "完成第一次演示测试"], ["有明确主题", "页面能打开", "内容不是空白", "能说明内容来源"], "Demo 初版 + 提示词记录"),
        practice_slide(day, 14, total, "综合项目制作 II：再打磨", ["修复关键 bug", "整理项目说明", "生成路演 PPT 初稿", "每人写个人贡献", "准备备用截图"], ["核心流程跑通", "说明文档完整", "PPT 不超过 5 页", "分工明确"], "Demo + 文档 + PPT 初稿"),
        slide_shell(day, 15, total, "验收标准", "今天下课前必须能现场演示", two_col(
            card("最低标准", ul(["页面/工具能打开", "有真实内容", "至少一个交互", "能讲清楚用途"]), "primary"),
            card("加分标准", ul(["工作流清楚", "Bug 记录完整", "视觉统一", "每人都有贡献"]), "success"),
        )),
        troubleshooting_slide(day, 16, total, "Day 5 课堂控场问题", [("小组一直讨论不动手", "目标没有收敛", "给 10 分钟截止：必须选一个项目并写目标卡"), ("Demo 做不完", "范围过大", "砍掉次要功能，只保留能演示的一条主流程"), ("组内分工混乱", "所有人都找 AI 生成不同版本", "指定一个文件负责人，其余人产出文案/测试/展示")]),
        summary_slide(day, 17, total, ["会把项目目标拆成工作流", "会按角色推进综合项目", "完成可演示 Demo 和路演初稿"], "明天上午做最终包装、安全与知识管理，下午正式路演。"),
    ]
    return "Agentic Engineering + 综合项目", slides


def build_day_6():
    day, total = 6, 18
    slides = [
        cover(day, total, "项目打磨 + 就业锦囊", "稳定 Demo、路演展示、简历优化、职场 AI 规范与 LLM-Wiki", ["最终调试", "就业转化", "正式路演"]),
        schedule_slide(day, 2, total, [
            ("08:30-09:50", "案例 10：简历 AI 优化 + 职场 AI 安全红线"),
            ("10:05-11:25", "LLM-Wiki 知识管理 + 课程全景回顾 + 路演最终检查"),
            ("13:00-14:20", "正式路演：规则说明、项目展示、评委合议"),
            ("14:35-15:55", "评选颁奖、讲师总结、个人复盘与结业"),
        ], ["优化版简历草稿", "职场 AI 安全手册", "知识管理收件箱", "最终 Demo + 路演"]),
        slide_shell(day, 3, total, "案例 10", "简历不是自传，是 6 秒内建立匹配感", two_col(
            step_cards([
                ("岗位关键词", "先看目标岗位需要什么，再决定课程项目怎么表达。"),
                ("成果导向", "把“参与了项目”改成“负责了什么、产出了什么、解决了什么”。"),
                ("多版本策略", "同一段经历可以为技术岗、运营岗、行政岗准备不同表达。"),
            ]),
            split_note("讲师话术", "AI 是简历顾问，不是经历制造机。所有优化必须基于学生真实做过的任务，尤其不能虚构数据、职位和成果。", "primary")
        )),
        slide_shell(day, 4, total, "简历案例", "同样的经历，不同的表达效果", compare_cols(
            "Before：表达太弱",
            ["参与小组项目", "使用了一些 AI 工具", "做了网页和 PPT", "协助完成展示"],
            "After：真实但更具体",
            ["负责用 AI 整理项目资料并形成结构化方案", "使用 Trae 生成单页 Demo，并记录 3 个 Bug 修复过程", "整理 5 页路演文案，完成项目背景和分工说明", "在小组展示中负责功能演示和答问"]
        )),
        prompt_slide(day, 5, total, "案例 10 提示词模板", "请帮我优化简历。", "我是一名应届生，目标岗位是【岗位名称】。下面是我在 6 天 AI 实训中的真实贡献，请帮我改写成一段简历项目经历，要求突出工具使用、个人职责、产出物，控制在 120 字以内，不要夸大。", "你写得太像负责人，也加入了我没做过的成果。请只保留我实际负责的部分，删除没有证据的量化数据。"),
        slide_shell(day, 6, total, "安全红线", "职场 AI 使用的 3 条底线", three_col([
            card("公司机密不进 AI", ul(["内部文件", "客户数据", "未公开策略", "合同和报价"]), "primary"),
            card("个人隐私要脱敏", ul(["姓名电话", "身份证号", "住址", "同学/客户信息"]), "accent"),
            card("输出内容要审核", ul(["事实核对", "数据核对", "引用核对", "版权风险"]), "success"),
        ])),
        slide_shell(day, 7, total, "安全案例讨论", "三组讨论：这件事错在哪里？", three_col([
            card("案例 A", ul(["把实习单位客户表发给 AI", "让 AI 生成客户跟进话术", "问题：客户隐私泄露"]), "primary"),
            card("案例 B", ul(["复制未公开项目方案", "让 AI 润色成汇报稿", "问题：公司机密外流"]), "accent"),
            card("案例 C", ul(["直接提交 AI 报告", "里面有过时数据", "问题：责任仍在提交人"]), "success"),
        ])),
        slide_shell(day, 8, total, "知识管理", "为什么需要 LLM-Wiki：不要让 6 天成果散掉", two_col(
            card("常见痛点", ul(["截图散落在微信和桌面", "提示词用完就忘", "项目踩坑没有记录", "面试时说不清自己做过什么"]), "primary"),
            card("今天要做的事", ul(["建立 AI 实训收件箱", "把项目资料分层", "沉淀可复用提示词", "为作品集和简历留证据"]), "success"),
        )),
        slide_shell(day, 9, total, "LLM-Wiki 方法论", "5 条核心思想 + 4 层知识结构", two_col(
            card("五条核心思想", ul(["资料先进收件箱，再沉淀", "项目记忆不等于个人知识", "知识要分层", "自然语言驱动", "任意窗口恢复上下文"]), "primary"),
            pyramid([
                ("项目层", "具体项目事实、截图、Bug、提示词"),
                ("个人层", "长期适用的方法和技巧"),
                ("共享层", "可以教给别人的经验"),
                ("输出层", "简历、作品集、路演、文章"),
            ])
        )),
        project_board(day, 10, total, "课程全景回顾：6 天到底掌握了什么", [
            ("Day 1-2", ["会查证资料", "会整理知识卡片", "会清洗表格", "会生成周报"], "primary"),
            ("Day 3-4", ["会描述设计", "会生成页面", "会做小工具", "会描述并修 Bug"], "accent"),
            ("Day 5", ["会拆项目目标", "会分配 AI 协作角色", "会做综合 Demo", "会准备路演"], "success"),
            ("Day 6", ["会写简历项目经历", "会遵守 AI 安全红线", "会沉淀知识", "会展示作品"], "primary"),
        ]),
        slide_shell(day, 11, total, "最终检查", "午饭前只做能降低路演风险的事", two_col(
            step_cards([
                ("Demo 检查", "页面能打开、按钮能点、核心结果能出现。"),
                ("PPT 检查", "5 页以内：痛点、方案、工作流、演示、复盘。"),
                ("分工检查", "谁讲背景、谁演示、谁答问、谁控时间。"),
                ("备份检查", "准备截图或录屏，现场故障时不慌。"),
            ]),
            split_note("取舍原则", "不要在最后 30 分钟追新功能。优先保证核心流程稳定，展示时能讲清楚为什么这样做。", "accent")
        )),
        slide_shell(day, 12, total, "路演规则", "每组 8-10 分钟展示 + 2-3 分钟问答", two_col(
            card("标准结构", ul(["1 分钟：项目背景", "1-2 分钟：解决方案", "4-5 分钟：现场演示", "1 分钟：团队分工", "1 分钟：收获反思"]), "primary"),
            card("现场要求", ul(["必须展示真实 Demo", "至少 2 名组员参与", "答不上来可以诚实说明", "故障时切备用截图/录屏"]), "accent"),
        )),
        slide_shell(day, 13, total, "评分标准", "评委看什么：不要只拼页面好看", rubric_grid([
            ("30%", "功能完整性", "核心流程是否跑通，是否能解决一个明确问题。"),
            ("25%", "工具使用", "是否体现 AI 搜集、整理、设计、开发或调试过程。"),
            ("20%", "团队协作", "分工是否清楚，成员是否都有贡献。"),
            ("15%", "路演表现", "表达是否清晰，时间是否控制得住。"),
            ("10%", "创新性", "是否有独特场景、交互或工作流设计。"),
        ])),
        slide_shell(day, 14, total, "正式路演", "13:00-14:20：讲师现场控节奏", two_col(
            card("讲师 / 助教动作", ul(["开场说明规则", "严格计时", "记录亮点和问题", "协助处理技术故障"]), "primary"),
            card("学生动作", ul(["按分工上台", "先讲场景再演示", "演示失败时切备用材料", "问答时只答自己知道的"]), "success"),
        )),
        slide_shell(day, 15, total, "评选颁奖", "14:35-15:20：把评价变成正向反馈", two_col(
            card("建议奖项", ul(["最佳项目奖", "最佳技术实现奖", "最佳演示奖", "最佳团队协作奖", "最具创新奖"]), "accent"),
            card("点评口径", ul(["先说每组最值得保留的亮点", "再给 1 条最重要改进建议", "不公开羞辱具体错误", "把问题转成后续优化方向"]), "primary"),
        )),
        practice_slide(day, 16, total, "个人资产整理实践", ["把最终 Demo、截图、提示词放入收件箱", "写一段简历项目经历", "写 1 分钟面试介绍", "列出 3 条后续优化计划"], ["真实不夸大", "能和项目证据对应", "能说出口", "有下一步"], "个人作品包：Demo 链接 + 简历段落 + 1 分钟介绍"),
        slide_shell(day, 17, total, "结业复盘", "每人写 5 句话，把课程真正带走", two_col(
            card("个人复盘问题", ul(["我最有用的一个提示词是什么？", "我做出的一个作品是什么？", "我遇到的一个 Bug 是什么？", "我下次会怎么改？", "我能写进简历的一句话是什么？"]), "primary"),
            card("后续路径", ul(["每月做一个 AI 小工具", "持续维护个人作品集", "把提示词和踩坑沉淀到知识库", "面试时讲清楚人机协作过程"]), "success"),
        )),
        summary_slide(day, 18, total, ["完成路演和项目收官", "把课程成果转成就业表达", "建立职场安全和知识沉淀意识"], "课程结束后保留作品、提示词、Bug 记录和复盘。工具会变，但查证、表达、构建和复盘的方法会一直有用。"),
    ]
    return "项目打磨 + 就业锦囊", slides


def write_deck(day, title, slides):
    out = SLIDES / f"day{day:02d}" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_doc(day, title, slides), encoding="utf-8")


def write_nav():
    days = [
        ("01", "AI 基础操作与信息整理", "会查证、会整理、会复盘", ["AI 搜索侦探", "知识卡片", "提示词 v1"], "16 页"),
        ("02", "AI 办公自动化", "表格清洗、数据摘要、正式汇报", ["Excel 救火队", "自动周报", "不编造"], "16 页"),
        ("03", "Vibe Design + Vibe Coding 入门", "从视觉方案到第一个 HTML 页面", ["Vibe Design", "演进图", "页面生成"], "17 页"),
        ("04", "Vibe Coding 深度 + Bug 修理铺", "做出可运行小工具并学会修错", ["小工具", "Debug", "测试记录"], "16 页"),
        ("05", "Agentic Engineering + 综合项目", "目标、约束、验收标准与项目冲刺", ["Workflow", "综合项目", "Demo 初版"], "17 页"),
        ("06", "项目打磨 + 就业锦囊", "路演、简历、安全规范、LLM-Wiki 与结业", ["正式路演", "就业转化", "课程复盘"], "18 页"),
    ]
    cards = []
    for no, title, sub, tags, count in days:
        cards.append(f"""
  <a class="day-card" href="day{no}/index.html" target="_blank">
    <div class="day-header"><div class="day-badge">{no}</div><div><div class="day-title">{escape(title)}</div><div class="day-subtitle">{escape(sub)}</div></div></div>
    <div class="day-topics">{''.join(f'<span class="topic-tag">{escape(t)}</span>' for t in tags)}</div>
    <div class="day-meta"><span>{count}</span><span>打开课件</span></div>
  </a>""")
    nav = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>AI 工具实战训练营 · 课件导航</title>
<style>*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:"Microsoft YaHei","PingFang SC",sans-serif;background:#f8fbff;min-height:100vh;padding:40px}}.header{{text-align:center;margin-bottom:32px}}.header h1{{font-size:32px;color:#084e8f;margin-bottom:8px}}.header p{{font-size:16px;color:#666}}.stats{{display:flex;justify-content:center;gap:20px;margin-bottom:32px;flex-wrap:wrap}}.stat-item{{text-align:center;background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:14px 22px}}.num{{font-size:26px;font-weight:700;color:#084e8f}}.label{{font-size:13px;color:#666;margin-top:4px}}.days-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:20px;max-width:1200px;margin:0 auto}}.day-card{{background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:24px;text-decoration:none;color:inherit;display:block;transition:.2s}}.day-card:hover{{box-shadow:0 4px 16px rgba(8,78,143,.12);transform:translateY(-2px);border-color:#084e8f}}.day-header{{display:flex;align-items:center;gap:12px;margin-bottom:12px}}.day-badge{{width:48px;height:48px;border-radius:10px;background:#084e8f;color:#fff;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:700;flex-shrink:0}}.day-card:nth-child(2) .day-badge{{background:#ee822f}}.day-card:nth-child(3) .day-badge{{background:#75bd42}}.day-card:nth-child(4) .day-badge{{background:#92181a}}.day-card:nth-child(5) .day-badge{{background:#30c0b4}}.day-card:nth-child(6) .day-badge{{background:#44546a}}.day-title{{font-size:18px;font-weight:700;color:#084e8f}}.day-subtitle{{font-size:13px;color:#666;margin-top:2px}}.day-topics{{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}}.topic-tag{{font-size:12px;color:#084e8f;background:rgba(8,78,143,.06);padding:4px 10px;border-radius:999px}}.day-meta{{display:flex;justify-content:space-between;margin-top:16px;padding-top:12px;border-top:1px solid #f0f0f0;font-size:12px;color:#999}}.footer{{text-align:center;margin-top:44px;font-size:13px;color:#999}}</style></head>
<body><div class="header"><h1>AI 工具实战训练营</h1><p>6 天案例驱动课件 · Vibe Design / Vibe Coding / Agentic Engineering</p></div>
<div class="stats"><div class="stat-item"><div class="num">6</div><div class="label">学习天数</div></div><div class="stat-item"><div class="num">10</div><div class="label">核心案例</div></div><div class="stat-item"><div class="num">100</div><div class="label">课件页数</div></div><div class="stat-item"><div class="num">1</div><div class="label">综合项目</div></div></div>
<div class="days-grid">{''.join(cards)}</div><div class="footer"><p>理论小于实践 · 教师带做 · 学生多动手 · 每半天有产出</p></div></body></html>"""
    (SLIDES / "index.html").write_text(nav, encoding="utf-8")


def theory_lab_slide(day, page, total, title, theory, demo, interaction, output):
    return slide_shell(day, page, total, "理论 + 实操", title, f"""
    <div class="classroom-grid">
      {card("必讲理论", ul(theory), "primary")}
      {card("教师现场演示", ul(demo), "accent")}
      {card("学生互动", ul(interaction), "success")}
      {card("课堂产出", ul(output), "primary")}
      {card("讲师判断标准", ul(["能不能复述方法", "能不能独立改提示词", "能不能指出 AI 输出的问题", "能不能把结果变成自己的作品"]), "success")}
    </div>
    """)


def _day1_v2():
    day, total = 1, 18
    slides = [
        cover(day, total, "AI 使用底层能力", "先学会判断、提问和验证，再进入工具实战", ["提示词结构", "事实核查", "学习助手"]),
        schedule_slide(day, 2, total, [
            ("08:30-09:50", "理论：AI 是概率生成，不是事实机器；案例 1：提示词拆解实验"),
            ("10:05-11:25", "案例 2：AI 学习教练，生成个性化学习计划并迭代"),
            ("13:00-14:20", "案例 3：事实核查实验，查证一个热点问题"),
            ("14:35-15:55", "对抗练习：找出 AI 幻觉、空话和无来源结论"),
        ], ["提示词公式卡", "学习计划 v2", "事实核查卡", "幻觉识别记录"]),
        theory_lab_slide(day, 3, total, "为什么不能上来就让学生直接动手", ["AI 会生成看起来合理但未必真实的内容", "提示词不是咒语，而是任务说明书", "好结果来自：目标、上下文、格式、约束、验收", "学生必须先学会判断“能不能信”"], ["投屏同一个问题的差提示词和好提示词", "让学生投票哪一个能交作业", "现场标出目标/上下文/格式/约束"], ["两人一组改写一个烂提示词", "每组说出自己加了哪个字段"], ["一张 5 要素提示词公式卡"]),
        runbook_slide(day, 4, total, 1, "提示词拆解实验", "QClaw / 任意对话式 AI 工具", ["准备 3 个烂提示词", "准备一张提示词拆解模板", "要求学生保存修改前后结果"], ["输入：帮我写一篇关于 AI 的文章", "让学生指出问题：对象、长度、场景都没有", "改成：给高校学生的 600 字课堂导入", "比较两次输出差异", "总结 5 要素公式"], ["选择一个烂提示词", "补充目标、对象、材料、格式、限制", "生成结果并标出变化", "写一句为什么变好了"], "请把下面这个模糊提示词改写成可执行任务。要求补齐：目标、受众、上下文材料、输出格式、限制条件、验收标准。", [("结果仍然空泛", "继续补充受众、场景和示例"), ("学生只会加“详细一点”", "要求至少补 3 个具体字段"), ("AI 结果太长", "增加字数、结构和交付物限制")]),
        prompt_slide(day, 5, total, "提示词公式", "帮我写一下。", "你是【角色】。我要完成【任务】，面向【对象】。背景材料是【材料】。请输出为【格式】，要求【限制】，最后用【验收标准】自检。", "你刚才输出太泛。请按照“问题-原因-修改建议-最终版本”四栏重写，并删除没有证据的内容。"),
        runbook_slide(day, 6, total, 2, "AI 学习教练", "QClaw / Kimi / 文档 AI", ["准备 3 个学生画像：零基础、时间少、目标模糊", "准备学习计划模板", "准备一段课程材料"], ["输入学生画像", "让 AI 先提问，不直接给计划", "补充约束：每天 30 分钟、5 天内见效", "生成计划", "让 AI 按“可执行性”自评"], ["写自己的学习目标", "让 AI 先问 3 个澄清问题", "回答后生成计划", "删掉不现实任务", "输出 v2"], "我想在 5 天内入门【主题】。我的基础是【基础】，每天可用【时间】。请先问我 3 个澄清问题，再根据回答制定学习计划。计划要包含每天任务、检查方式和遇到困难时的替代方案。", [("计划太鸡汤", "要求每天有可检查动作和产出"), ("计划太满", "限制每天时间和任务数量"), ("学生照单全收", "要求删掉 1 个不现实任务并说明理由")]),
        theory_lab_slide(day, 7, total, "学习类 AI 的理论边界", ["AI 擅长拆任务、给路线、生成练习题", "AI 不知道学生真实掌握程度，必须通过产出验证", "学习计划不是越满越好，而是能坚持", "所有学习建议都要变成当天可交付物"], ["展示一份过度理想化计划", "现场砍掉 50% 任务", "改成最小可执行版本"], ["学生互换计划，找出最不现实的一项"], ["学习计划 v2 + 砍掉内容说明"]),
        runbook_slide(day, 8, total, 3, "事实核查实验", "QClaw / 支持联网检索的 AI 搜索工具", ["准备热点主题：AI 编程、AI 设计、AI 求职、AI 诈骗防范", "要求每条结论必须有来源", "准备事实/观点/判断三色标记"], ["让 AI 检索主题", "要求输出事实、观点和判断", "点开来源核验", "找出一条不确定信息", "改写成事实核查卡"], ["任选一个主题", "获得 5 条结论", "核验 3 个来源", "标记事实/观点/判断", "写自己的结论"], "请围绕【主题】做事实核查。输出表格：结论、它是事实/观点/推测、证据、来源链接、我还需要确认什么。没有来源的内容请放到“待确认”区域。", [("来源不存在", "要求重新检索并替换来源"), ("把观点当事实", "追问：这句话可否被证据证明"), ("主题太大", "缩小到时间、地区、对象")]),
        troubleshooting_slide(day, 9, total, "Day 1 必须讲的翻车点", [("AI 编造来源", "模型试图完成任务但未验证", "让学生点开来源；打不开就不能交"), ("输出很漂亮但没用", "没有验收标准", "要求每个结果附“我怎么使用它”"), ("学生不愿质疑 AI", "权威错觉", "安排“找错挑战”：每组必须找出 1 条可疑结论")]),
        practice_slide(day, 10, total, "事实核查卡实操", ["主题四选一", "输出 5 条结论", "核验 3 条来源", "标记事实/观点/推测", "写 80 字个人判断"], ["有链接", "有分类", "有不确定项", "不是复制粘贴"], "事实核查卡"),
        slide_shell(day, 11, total, "互动设计", "让学生真正动手，而不是看老师表演", three_col([
            card("投票", ul(["哪个提示词更能交作业", "哪个结论最可疑", "哪个计划最现实"]), "primary"),
            card("互评", ul(["同桌检查来源", "互删空话", "互问验收标准"]), "accent"),
            card("上台", ul(["展示一次失败输出", "现场改提示词", "说出改动理由"]), "success"),
        ])),
        slide_shell(day, 12, total, "提示词库", "Day 1 要沉淀 3 类提示词", three_col([
            card("提问前", ul(["请先问我 3 个澄清问题", "请指出任务缺少哪些信息"]), "primary"),
            card("生成中", ul(["按表格输出", "每条附来源", "限制字数和结构"]), "accent"),
            card("生成后", ul(["请自检事实依据", "请删除空话", "请给可执行下一步"]), "success"),
        ])),
        drill_slide(day, 13, total, "14:35-15:10 对抗练习：找 AI 幻觉", ["5 分钟：讲师发一段含错误 AI 输出", "10 分钟：学生找错", "10 分钟：小组解释证据", "10 分钟：讲师复盘"], ["不要直接公布答案", "追问证据在哪里", "把错误类型写在白板"], ["标红可疑句", "写出验证方式", "提交修改版"], ["错误清单", "修正版"], ["能说清错在哪里", "能说明怎么查证"]),
        troubleshooting_slide(day, 14, total, "课堂控场", [("学生觉得理论无聊", "理论没有马上服务任务", "每讲 8 分钟理论，立刻给 5 分钟练习"), ("学生复制答案", "没有个人化要求", "要求写自己的判断和删改痕迹"), ("工具回答不稳定", "模型差异正常", "把不同结果当作比较材料")]),
        slide_shell(day, 15, total, "今日提交物", "每个学生下课前交 4 件东西", three_col([
            card("提示词公式卡", ul(["5 要素", "1 个改写例子", "1 条纠错提示词"]), "success"),
            card("学习计划 v2", ul(["每天任务", "检查方式", "砍掉内容"]), "success"),
            card("事实核查卡", ul(["3 个来源", "事实/观点分类", "个人判断"]), "success"),
        ])),
        summary_slide(day, 16, total, ["知道 AI 为什么会一本正经地错", "掌握提示词 5 要素", "能用来源核查信息"], "Day 2 进入 AI 办公：把杂乱信息变成会议纪要、任务清单和数据报告。"),
        slide_shell(day, 17, total, "讲师备课页", "Day 1 上课前必须准备", two_col(
            card("材料", ul(["3 个烂提示词", "3 个学生画像", "4 个热点主题", "1 段含错误的 AI 输出"]), "primary"),
            card("环境", ul(["QClaw 账号", "联网检索可用", "学生记录模板", "投屏能打开网页来源"]), "accent"),
        )),
        slide_shell(day, 18, total, "下课前 5 分钟话术", "今天不是学会一个工具，而是学会一套判断方式", two_col(
            card("讲师总结", ul(["AI 输出要被验证", "提示词要能被复用", "结果要变成自己的作品"]), "primary"),
            card("预告", ul(["明天处理真实办公任务", "会议纪要", "任务拆解", "表格分析", "正式报告"]), "success"),
        )),
    ]
    return "AI 使用底层能力", slides


def _day2_v2():
    day, total = 2, 18
    slides = [
        cover(2, total, "AI 办公自动化", "会议纪要、任务拆解、表格分析和报告写作", ["会议纪要", "Excel 分析", "正式报告"]),
        schedule_slide(2, 2, total, [("08:30-09:50", "理论：办公自动化不是偷懒，是把信息变成决策"), ("10:05-11:25", "案例 4：会议录音/聊天记录变纪要和任务清单"), ("13:00-14:20", "案例 5：Excel 数据诊断与可视化摘要"), ("14:35-15:55", "案例 6：给不同对象写正式报告")], ["会议纪要", "任务清单", "数据洞察卡", "正式报告"]),
        theory_lab_slide(2, 3, total, "办公 AI 的理论框架：输入-处理-输出-审核", ["输入决定质量：聊天记录、表格、上下文越清楚越好", "处理不是一次完成，要拆成提取、归类、总结、改写", "输出要匹配对象：老师、领导、同学、客户", "最终审核责任在人，不在 AI"], ["用一段杂乱聊天记录演示四步处理", "展示 AI 编造任务负责人时如何纠正"], ["学生判断哪些信息不能写进正式报告"], ["办公自动化流程卡"]),
        runbook_slide(2, 4, total, 4, "会议纪要生成器", "WorkBuddy / 文档 AI / 飞书或微信聊天记录", ["准备一段模拟会议记录", "里面包含任务、争议、截止时间和无关闲聊", "准备纪要模板"], ["导入聊天记录", "让 AI 提取议题和结论", "再提取任务负责人和截止时间", "删除无关闲聊", "生成正式纪要"], ["复制会议记录", "先提取结构", "再生成纪要", "检查负责人和时间", "导出任务清单"], "请把下面会议记录整理成正式纪要。输出：会议主题、参会角色、关键结论、待办任务、负责人、截止时间、风险。无法确定的信息请标“待确认”，不要编造。", [("AI 编了负责人", "要求无法确定就写待确认"), ("纪要太长", "限制每个议题 2 行"), ("闲聊被写进去", "增加：忽略与决策无关内容")]),
        practice_slide(2, 5, total, "学生实操：从聊天记录到任务表", ["领取一段聊天记录", "提取议题", "生成任务表", "标注待确认信息", "把任务表改成可执行版本"], ["任务有负责人", "有截止时间或待确认", "无闲聊", "能直接发给小组"], "会议纪要 + 任务清单"),
        runbook_slide(2, 6, total, 5, "Excel 数据洞察卡", "WorkBuddy / Excel / WPS 表格", ["准备乱表和干净表各一份", "表格字段：日期、类别、金额、状态、备注", "要求先诊断后分析"], ["让 AI 先检查数据质量", "确认清洗建议", "生成 3 条洞察", "让 AI 给每条洞察找数据依据", "输出一页洞察卡"], ["上传表格", "生成质量诊断", "处理重复/空值/格式", "生成洞察", "核对数字"], "请检查这份表格的数据质量，并输出：问题清单、清洗建议、3 条数据洞察、每条洞察的数据依据。不要自动猜测缺失值。", [("AI 直接下结论", "要求每条洞察必须写数据依据"), ("缺失值被乱填", "提示：缺失值只标记，不猜测"), ("学生看不懂洞察", "要求改成“发现-证据-建议”格式")]),
        theory_lab_slide(2, 7, total, "数据分析最小理论", ["描述性分析：发生了什么", "诊断性分析：可能为什么", "建议性分析：下一步做什么", "AI 不能替你承担数据真实性"], ["把同一张表输出成三层分析", "指出“建议”必须来自“发现”"], ["学生判断 3 条结论属于哪一层"], ["数据洞察三层卡"]),
        practice_slide(2, 8, total, "学生实操：做一页数据洞察卡", ["上传表格", "找出数据质量问题", "生成 3 条洞察", "核对每条数据依据", "写 2 条行动建议"], ["有问题清单", "洞察有证据", "建议不空泛", "原始表保留"], "数据洞察卡"),
        runbook_slide(2, 9, total, 6, "正式报告生成器", "WorkBuddy / 文档 AI", ["准备任务记录和数据洞察卡", "设定 3 个读者：老师、领导、同学", "准备报告结构"], ["输入同一份材料", "先生成老师版", "再生成领导版", "对比语气和重点", "删除无依据夸大句"], ["选择读者", "生成报告", "标出事实依据", "改写语气", "提交最终版"], "请根据以下材料写一份给【对象】看的报告。结构：背景、已完成、发现的问题、数据依据、下一步计划、需要支持。要求正式、具体、不要编造材料中没有的信息。", [("报告像口号", "要求每段必须引用材料依据"), ("对象不明确", "先写读者和目的"), ("语气过度包装", "删除“显著提升、全面优化”等无依据词")]),
        prompt_slide(2, 10, total, "办公提示词模板", "整理一下。", "请先提取事实，再生成文档。事实提取表包含：原文依据、任务/结论、负责人、时间、待确认项。确认后再写正式版本。", "你刚才加入了材料中没有的信息。请列出每个结论对应的原文依据，没有依据的删除。"),
        troubleshooting_slide(2, 11, total, "办公场景翻车点", [("纪要里出现不存在的人", "AI 根据上下文猜测", "所有负责人必须来自原文，否则待确认"), ("数据洞察没有证据", "模型在概括而非分析", "要求每条洞察附字段、数值或行数依据"), ("报告太像套话", "缺少对象和目的", "补充读者、场景和长度限制")]),
        drill_slide(2, 12, total, "课堂互动：同一材料三种报告", ["10 分钟：三组分别写老师/领导/同学版", "15 分钟：互换阅读", "10 分钟：判断哪版适合谁", "10 分钟：现场改一版"], ["强调对象决定表达", "指出无依据句子", "让学生看到语气差异"], ["分组生成", "互评语气", "标注依据"], ["三版报告"], ["对象匹配", "事实准确", "结构清楚"]),
        slide_shell(2, 13, total, "工具动作图", "WorkBuddy 不是魔法按钮，而是办公流水线", project_board(2, 13, total, "x", [] ) if False else '<div class="board-grid">' + ''.join([card("导入", ul(["聊天记录", "表格", "任务记录"]), "primary"), card("提取", ul(["事实", "任务", "问题"]), "accent"), card("生成", ul(["纪要", "洞察", "报告"]), "success"), card("审核", ul(["来源", "数字", "语气"]), "primary")]) + '</div>'),
        practice_slide(2, 14, total, "综合练习：从会议到报告", ["用会议记录生成任务清单", "用表格生成洞察卡", "把两者合成周报", "人工审核并标注修改"], ["流程完整", "事实有依据", "报告可发送", "有修改痕迹"], "会议纪要 + 洞察卡 + 周报"),
        troubleshooting_slide(2, 15, total, "课堂控场", [("学生把 AI 当排版工具", "没有理解提取和审核", "要求先交事实提取表，再交报告"), ("学生不看数字", "害怕表格", "每条结论只核对一个数"), ("学生报告千篇一律", "缺少具体读者", "给不同读者和场景")]),
        slide_shell(2, 16, total, "今日提交物", "Day 2 下课交 4 件办公成果", three_col([card("纪要", ul(["议题", "结论", "任务", "待确认"]), "success"), card("洞察卡", ul(["问题清单", "3 条洞察", "数据依据"]), "success"), card("报告", ul(["对象明确", "结构完整", "无编造"]), "success")])),
        summary_slide(2, 17, total, ["会把聊天记录变纪要", "会把表格变洞察", "会面向不同读者写报告"], "Day 3 进入内容创作和 Vibe Design：做一套能发布、能展示的视觉内容。"),
        slide_shell(2, 18, total, "讲师备课页", "Day 2 材料清单", two_col(card("文件", ul(["模拟会议记录", "乱表 Excel", "干净表 Excel", "报告模板"]), "primary"), card("检查", ul(["WorkBuddy 可打开文件", "学生会保存副本", "投屏能展示表格"]), "accent"))),
    ]
    return "AI 办公自动化", slides


def _day3_v2():
    day, total = 3, 18
    slides = [
        cover(3, total, "AI 内容创作 + Vibe Design", "从内容策略到视觉成品，做一套能展示的活动传播物料", ["内容策略", "视觉系统", "海报/首屏"]),
        schedule_slide(3, 2, total, [("08:30-09:50", "理论：内容不是让 AI 写作文，而是设计传播目标"), ("10:05-11:25", "案例 7：活动传播三件套，标题/脚本/海报文案"), ("13:00-14:20", "Vibe Design：视觉系统、风格词、版式反馈"), ("14:35-15:55", "生成落地页首屏或海报方案，互评迭代")], ["传播策略卡", "短视频/图文脚本", "视觉风格板", "海报或首屏方案"]),
        theory_lab_slide(3, 3, total, "内容创作最小理论：目标-受众-钩子-证据-行动", ["目标：让谁做什么", "受众：他们关心什么", "钩子：第一句话为什么停下", "证据：为什么相信你", "行动：看完要做什么"], ["拆一个爆款标题：不是玄学，是钩子和利益点", "把同一主题改成学生版、老师版、企业版"], ["学生给同一活动写 3 个标题"], ["传播策略卡"]),
        runbook_slide(3, 4, total, 7, "活动传播三件套", "QClaw / 文档 AI / 图像生成工具", ["准备主题：AI 工具分享会、社团招新、作品集发布", "准备传播模板：标题、短视频脚本、海报文案", "要求每组选择一个受众"], ["确定目标和受众", "生成 10 个标题", "筛选 3 个并解释理由", "生成 30 秒短视频脚本", "生成海报文案"], ["选择主题", "写目标和受众", "生成标题池", "选标题并改写", "输出脚本和海报文案"], "请为【活动/项目】设计一套传播内容。受众是【受众】，目标是【目标】。请输出：10 个标题、3 个开场钩子、30 秒短视频脚本、海报主标题/副标题/行动按钮。语气要适合大学生。", [("标题像广告", "加入校园语境和真实利益点"), ("脚本太长", "限制 30 秒，按镜头分段"), ("没有行动", "最后必须有报名/访问/收藏等动作")]),
        prompt_slide(3, 5, total, "内容创作提示词", "帮我写宣传文案。", "请先问我目标受众、发布平台、行动目标，再生成 10 个标题。每个标题标注：钩子类型、适合平台、可能风险。", "这些标题太夸张。请降低营销感，保留真实利益点，不使用“颠覆、炸裂、必看”等词。"),
        practice_slide(3, 6, total, "学生实操：内容三件套", ["确定活动主题", "写受众和目标", "生成标题池", "完成 30 秒脚本", "写海报文案"], ["标题有钩子", "脚本能拍", "文案不夸张", "行动明确"], "标题池 + 脚本 + 海报文案"),
        image_slide(3, 7, total, "演进图总览", "从 Vibe Coding 到 Agentic Engineering", "vibe-agentic-evolution.jpg", "只在这里解释：Vibe 不是随便说感觉，而是把意图变成可迭代的作品。"),
        theory_lab_slide(3, 8, total, "Vibe Design 理论：风格词必须能落到视觉决策", ["“高级”不是指令，要拆成颜色、留白、字体、层级", "设计反馈要具体：哪里乱、哪里弱、哪里不清楚", "AI 设计初稿必须二次迭代", "视觉服务信息，不是装饰"], ["把“科技感”拆成深色背景、网格、冷色强调、数据元素", "现场把一个花哨方案改干净"], ["学生把“好看”改成 4 条具体反馈"], ["视觉风格板"]),
        runbook_slide(3, 9, total, 8, "Vibe Design 视觉系统", "图像生成工具 / Trae 预览 / 文档 AI", ["准备 3 种风格方向：校园清爽、科技发布会、杂志编辑感", "要求每组只选一种风格", "准备风格板模板"], ["输入内容三件套", "生成风格板", "要求输出颜色、字体感、布局、图片建议", "指出第一版问题", "生成第二版"], ["选择风格方向", "生成风格板", "写 3 条反馈", "生成第二版", "保存前后对比"], "请基于我的活动文案设计视觉风格板。输出：风格关键词、主色/辅助色/强调色、字体气质、版式结构、图片建议、不要使用的元素。然后给一版海报/落地页首屏布局。", [("风格太泛", "要求给颜色和布局，不只给形容词"), ("元素太多", "限制一页只保留主标题、3 个卖点、行动按钮"), ("审美像模板", "要求删除装饰，增强信息层级")]),
        practice_slide(3, 10, total, "学生实操：做视觉风格板", ["把内容三件套交给 AI", "生成风格板", "写反馈", "生成第二版", "同桌评价"], ["颜色不超过 3 种", "标题层级清楚", "文案可读", "有修改理由"], "视觉风格板 v2"),
        runbook_slide(3, 11, total, 9, "落地页首屏/海报方案", "Trae / 图像生成工具", ["准备上午文案和风格板", "只做首屏或海报，不做完整网站", "要求可课堂展示"], ["把风格板转成页面结构", "生成首屏 HTML 或海报方案", "检查文字层级", "要求 AI 按反馈改版", "保存最终截图"], ["输入风格板和文案", "生成首屏/海报", "检查三点：主题、卖点、行动", "迭代一次"], "请根据以下文案和视觉风格板，生成一个活动落地页首屏。包含：主标题、副标题、3 个卖点、活动信息、行动按钮。要求信息层级清楚，适合课堂投屏展示。", [("页面像官网模板", "改成活动首屏，减少模块"), ("文字太多", "保留主标题、副标题、3 个卖点"), ("行动按钮不明确", "按钮文字改成具体动作")]),
        drill_slide(3, 12, total, "互动：全班审稿会", ["10 分钟：每组选 1 张图", "20 分钟：全班按标准打分", "20 分钟：每组现场改 1 次"], ["只评价信息层级和可读性", "不要泛泛说好看/不好看", "要求反馈能执行"], ["展示作品", "接受 2 条修改意见", "现场迭代"], ["修改前后对比"], ["反馈具体", "改动明显", "主题更清楚"]),
        troubleshooting_slide(3, 13, total, "内容和设计翻车点", [("标题党", "AI 迎合营销语气", "要求真实、校园、不要夸大"), ("设计空泛", "风格词没有落地", "必须输出颜色、布局、字体气质"), ("页面漂亮但信息不清", "视觉压过内容", "先读主标题，再看卖点和行动")]),
        project_board(3, 14, total, "Day 3 成果板", [("策略", ["目标", "受众", "平台", "行动"], "primary"), ("内容", ["标题池", "脚本", "海报文案", "风险词"], "accent"), ("视觉", ["风格词", "配色", "布局", "图片建议"], "success"), ("作品", ["海报", "首屏", "截图", "修改记录"], "primary")]),
        slide_shell(3, 15, total, "今日提交物", "Day 3 下课前交 4 件", three_col([card("传播策略卡", ul(["目标", "受众", "平台", "行动"]), "success"), card("内容三件套", ul(["标题", "脚本", "海报文案"]), "success"), card("视觉成品", ul(["风格板", "首屏/海报", "前后对比"]), "success")])),
        summary_slide(3, 16, total, ["会用 AI 做内容策略", "会把风格词变成视觉决策", "会用反馈迭代设计作品"], "Day 4 进入 Vibe Coding：把作品变成可运行的互动页面/小工具。"),
        slide_shell(3, 17, total, "讲师备课页", "Day 3 准备清单", two_col(card("案例素材", ul(["3 个活动主题", "好坏标题例子", "好坏海报例子", "风格方向参考"]), "primary"), card("课堂提醒", ul(["不要只追求好看", "每页必须有行动目标", "保留前后对比"]), "accent"))),
        slide_shell(3, 18, total, "下课前话术", "AI 内容课的重点不是产量，而是判断力", two_col(card("提醒", ul(["标题要真实", "设计要服务信息", "反馈要具体"]), "primary"), card("预告", ul(["明天把首屏变成可运行页面", "做交互", "修 Bug", "保存版本"]), "success"))),
    ]
    return "AI 内容创作 + Vibe Design", slides


def _day4_v2():
    day, total = 4, 18
    slides = [
        cover(4, total, "Vibe Coding 产品实战", "用自然语言做一个能跑、能测、能改的小产品", ["需求表达", "AI 编程", "Debug"]),
        schedule_slide(4, 2, total, [("08:30-09:50", "理论：Vibe Coding 不是许愿，是产品需求表达"), ("10:05-11:25", "案例 10：把 Day 3 首屏变成可运行活动页"), ("13:00-14:20", "案例 11：做一个提示词评分器/学习计划生成器"), ("14:35-15:55", "Bug 修理铺：复现、描述、修复、回归测试")], ["需求说明书", "活动页 v1", "AI 小工具", "Bug 修复记录"]),
        theory_lab_slide(day, 3, total, "Vibe Coding 理论：需求写不好，代码一定烂", ["页面需求包括：用户、场景、输入、动作、输出", "先做 MVP，再做美化，再做增强", "AI 生成代码必须测试，不测试就不能算完成", "不会代码也能做产品经理和测试员"], ["展示一个“帮我做网页”的失败结果", "改成需求说明书后再生成", "对比差异"], ["学生把自己的 Day 3 作品改成需求清单"], ["需求说明书 v1"]),
        slide_shell(day, 4, total, "需求公式", "学生只需要掌握这一张表", compact_table(["字段", "必须写清", "例子"], [("用户", "谁使用", "参加 AI 分享会的学生"), ("场景", "什么时候用", "扫码查看活动信息并报名"), ("输入", "用户提供什么", "姓名、班级、联系方式"), ("动作", "点击后发生什么", "提交、提示、统计"), ("输出", "用户看到什么", "报名成功提示和活动安排"), ("约束", "不能做什么", "不做后端，单文件 HTML") ])),
        runbook_slide(day, 5, total, 10, "活动页生成", "Trae Builder / 浏览器", ["准备 Day 3 文案和风格板", "准备需求公式表", "统一要求单文件 HTML"], ["把文案改成需求说明", "让 Trae 生成 HTML", "打开浏览器预览", "测试按钮", "让 AI 修第一处问题"], ["复制自己的文案", "写用户/场景/输入/动作/输出", "生成活动页", "测试报名按钮", "保存 v1"], "请基于以下活动文案和视觉风格，生成单文件 HTML 活动页。功能：展示活动信息、3 个亮点、报名表单、点击提交后显示报名成功和活动提醒。不需要后端，所有代码放在一个 HTML 文件。", [("生成太多文件", "补充单文件 HTML"), ("按钮无反馈", "要求检查表单 submit/click 事件"), ("报名数据不会保存", "说明无后端限制，只做课堂演示")]),
        practice_slide(day, 6, total, "学生实操：活动页 v1", ["写需求说明", "用 Trae 生成 HTML", "测试表单", "修 1 个问题", "截图保存"], ["可打开", "表单可输入", "按钮有反馈", "视觉沿用 Day 3"], "活动页 v1 + 需求说明"),
        runbook_slide(day, 7, total, 11, "提示词评分器", "Trae / 浏览器 / 文档 AI", ["准备评分维度：目标、上下文、格式、约束、验收", "准备 3 个示例提示词", "要求学生做一个可交互工具"], ["展示评分标准", "让 AI 生成评分器页面", "输入烂提示词测试", "让工具给改进建议", "修复显示问题"], ["生成评分器", "输入自己的提示词", "查看评分和建议", "修改提示词再测一次"], "请做一个单文件 HTML 提示词评分器。用户粘贴提示词后，点击评分，页面按 5 个维度给分：目标、上下文、格式、约束、验收，并给出修改建议。无需调用真实 API，用前端规则模拟即可。", [("学生以为要接大模型 API", "明确：今天用规则模拟，不接 API"), ("评分不准确", "强调这是学习工具，评分规则可人工调整"), ("JS 报错", "复制控制台错误让 Trae 修")]),
        theory_lab_slide(day, 8, total, "为什么提示词评分器适合 AI 课", ["它回扣 Day 1 提示词理论", "它让学生理解评分标准", "它有输入、计算、输出完整交互", "它能成为课程作品集的一部分"], ["现场把烂提示词输入评分器", "根据建议改写后再评分"], ["学生比较改写前后分数"], ["提示词评分器 v1"]),
        practice_slide(day, 9, total, "学生实操：提示词评分器", ["复制工具需求", "生成 HTML", "测试 3 个提示词", "修改评分文案", "保存 v1/v2"], ["能输入", "能评分", "能给建议", "界面不重叠"], "提示词评分器 + 测试记录"),
        runbook_slide(day, 10, total, 12, "Bug 修理铺", "Trae / Chrome 控制台", ["准备故障版本页面", "故障包括按钮无反应、undefined、文字溢出", "准备 Bug 记录模板"], ["复现 Bug", "描述：操作-现象-期望", "复制控制台错误", "让 AI 一次只修一个", "回归测试"], ["列 3 个 Bug", "按优先级修", "每修一次测试", "记录修改前后"], "点击【按钮】后没有任何反应。请检查事件绑定和相关 JavaScript。只修复这个问题，不要重写页面，不要改变视觉样式。修复后说明改了哪里。", [("AI 重写全页", "加限制：不要重写，只改指定区域"), ("修完又坏", "回退到上一版本，重新只修一个问题"), ("学生不会看控制台", "讲师示范 F12/Console")]),
        troubleshooting_slide(day, 11, total, "Debug 必讲理论", [("复现", "能稳定看到问题", "先写操作步骤"), ("定位", "知道大概是按钮、样式还是数据", "看现象和控制台"), ("修复", "一次只改一个问题", "让 AI 说明改动"), ("回归", "确认旧功能没坏", "重新跑测试清单")]),
        project_board(day, 12, total, "测试清单", [("功能", ["按钮", "输入", "输出", "清空"], "primary"), ("边界", ["空输入", "超长文本", "重复点击", "特殊符号"], "accent"), ("视觉", ["不重叠", "字号可读", "移动端基本可看"], "success"), ("证据", ["截图", "Bug 文案", "修复提示词", "版本文件"], "primary")]),
        practice_slide(day, 13, total, "学生实操：修自己的页面", ["打开活动页或评分器", "列出 3 个问题", "修最影响演示的 1 个", "重新测试", "保存最终版"], ["问题描述具体", "修复范围可控", "最终能演示", "有版本记录"], "最终页面 + Bug 修复记录"),
        troubleshooting_slide(day, 14, total, "课堂控场", [("学生沉迷美化", "产品目标偏移", "先功能后视觉，最后 20 分钟才允许改样式"), ("学生害怕代码", "角色理解错", "告诉学生今天是需求描述和测试，不是背代码"), ("全班工具效果不同", "AI 生成不稳定", "把差异当作测试和迭代素材")]),
        slide_shell(day, 15, total, "互评", "两组互测，专门找问题", two_col(card("测试者", ul(["输入空内容", "连续点击", "输入超长文本", "看是否溢出"]), "primary"), card("开发者", ul(["记录 Bug", "问清复现步骤", "只修一个", "修完请对方再测"]), "accent"))),
        slide_shell(day, 16, total, "今日提交物", "Day 4 下课交 4 件", three_col([card("需求说明书", ul(["用户", "场景", "输入", "输出"]), "success"), card("可运行页面", ul(["活动页或评分器", "单文件", "能演示"]), "success"), card("Bug 记录", ul(["现象", "提示词", "修复", "复测"]), "success")])),
        summary_slide(day, 17, total, ["会把想法写成产品需求", "会用 Trae 生成可运行页面", "会按标准流程 Debug"], "Day 5 进入 Agentic Engineering：把单个作品升级成小组综合项目。"),
        slide_shell(day, 18, total, "讲师备课页", "Day 4 准备清单", two_col(card("材料", ul(["Day 3 作品", "评分维度", "故障页面", "测试模板"]), "primary"), card("环境", ul(["Trae 可用", "浏览器控制台演示", "学生知道保存版本"]), "accent"))),
    ]
    return "Vibe Coding 产品实战", slides


def _day5_v2():
    day, total = 5, 18
    slides = [
        cover(day, total, "Agentic Engineering 综合项目", "把 AI 当协作团队：规划、构建、测试、复盘", ["角色分工", "工作流", "项目冲刺"]),
        schedule_slide(day, 2, total, [("08:30-09:50", "理论：从 Vibe Coding 到 Agentic Engineering"), ("10:05-11:25", "案例 13：AI 求职助手/学习助手综合项目规划"), ("13:00-14:20", "项目冲刺 I：资料、页面、交互、测试并行"), ("14:35-15:55", "项目冲刺 II：路演稿、验收、备用方案")], ["Agentic 工作流图", "综合项目 Demo", "测试报告", "路演初稿"]),
        image_slide(day, 3, total, "Agentic Engineering", "从 Vibe Coding 升级到 Agentic Engineering", "vibe-agentic-evolution.jpg", "这张图只在 Day 5 正式讲：从“让 AI 写一段”升级为“让 AI 按角色协作完成项目”。"),
        theory_lab_slide(day, 4, total, "Agentic Engineering 最小理论", ["Goal：目标清楚", "Plan：拆成步骤", "Role：AI/学生各自负责什么", "Trace：保留提示词和版本记录", "Eval：用验收标准检查"], ["把“做一个求职助手”拆成 5 步", "演示 Builder/Tester/Reviewer 三个角色提示词"], ["小组给自己的项目分配角色"], ["工作流图"]),
        runbook_slide(day, 5, total, 13, "AI 求职助手综合项目", "QClaw + WorkBuddy + Trae + 文档 AI", ["准备项目模板", "要求每组选择求职助手/学习助手/活动助手之一", "统一不做登录、后端、真实 API"], ["用 QClaw 搜集岗位需求或学习资料", "用 WorkBuddy 整理字段", "用 Trae 生成 Demo", "用 Tester 提示词找 Bug", "用 Reviewer 提示词改展示文案"], ["选题", "分角色", "搜集资料", "生成 Demo", "测试并记录"], "我们要在 1 天内完成【项目】MVP。请输出 Agentic 工作流表：步骤、负责角色、使用工具、输入、输出、验收标准、风险。限制：不做后端、不接真实 API、必须能课堂演示。", [("项目过大", "砍到单页 MVP"), ("角色重叠", "明确 Builder/Tester/Writer/Speaker"), ("没有验收", "每一步写可检查标准")]),
        prompt_slide(day, 6, total, "三类 Agent 提示词", "你帮我做完。", "Builder：请根据需求生成最小可用版本；Tester：请按测试清单找 5 个问题；Reviewer：请从路演视角指出最影响理解的 3 个问题。", "计划太大。请保留一条主流程，删除登录、数据库、复杂算法，并说明删减理由。"),
        project_board(day, 7, total, "小组角色", [("Planner", ["定义目标", "拆步骤", "控范围"], "primary"), ("Builder", ["生成页面", "整合内容", "保存版本"], "accent"), ("Tester", ["写测试", "找 Bug", "复测"], "success"), ("Speaker", ["写路演", "讲价值", "答问题"], "primary")]),
        practice_slide(day, 8, total, "项目规划实操", ["确定项目", "写目标和受众", "拆 5 步", "分配 4 个角色", "写验收标准"], ["范围可完成", "角色不重叠", "每步有输出", "风险明确"], "Agentic 工作流图"),
        troubleshooting_slide(day, 9, total, "项目规划翻车点", [("想做万能平台", "范围幻想", "限定 1 个用户、1 个场景、1 条主流程"), ("没有数据", "内容空洞", "先用 QClaw 搜集或用课堂模拟数据"), ("没人负责测试", "测试被低估", "强制每组设置 Tester")]),
        runbook_slide(day, 10, total, 14, "综合项目冲刺", "全工具协同", ["准备项目目录", "准备提示词记录表", "准备演示评分表"], ["示范目录结构", "资料线和 Demo 线并行", "每 30 分钟检查一次产出", "把问题写入风险表", "准备备用截图"], ["按角色并行", "每 30 分钟交中间产物", "合并到 Demo", "测试主流程"], "请根据以下资料和工作流，生成项目 Demo 的页面结构和核心交互。先保证主流程能演示，再考虑视觉优化。输出后请同时给测试清单。", [("每个人都生成一版", "指定 Builder 合并"), ("内容没来源", "资料线必须保留来源"), ("Demo 演示不通", "只保留一条主流程")]),
        project_board(day, 11, total, "四线并行工作台", [("资料线", ["搜集", "来源", "筛选", "摘要"], "primary"), ("Demo线", ["结构", "代码", "交互", "版本"], "accent"), ("测试线", ["用例", "Bug", "复测", "备用"], "success"), ("展示线", ["PPT", "脚本", "分工", "问答"], "primary")]),
        practice_slide(day, 12, total, "冲刺 I：先跑通", ["资料线完成 5 条材料", "Demo 线生成页面", "测试线跑 5 条用例", "展示线写 5 页结构"], ["页面能打开", "内容不空", "主按钮可用", "有 Bug 清单"], "Demo 初版 + 测试清单"),
        practice_slide(day, 13, total, "冲刺 II：再打磨", ["修最严重的 2 个 Bug", "补充说明文档", "生成路演稿", "准备备用截图", "每人写贡献"], ["主流程稳定", "路演不超时", "每人有贡献", "有备用方案"], "Demo v2 + 路演初稿"),
        slide_shell(day, 14, total, "路演结构", "5 页足够讲清一个学生项目", compact_table(["页", "内容", "一句话目标"], [("1", "问题和用户", "让评委知道为什么做"), ("2", "AI 工作流", "说明怎么用 AI 协作"), ("3", "Demo 展示", "证明能跑"), ("4", "测试和迭代", "证明不是一次生成"), ("5", "分工和反思", "证明每个人有收获")])),
        troubleshooting_slide(day, 15, total, "项目冲刺控场", [("还有很多功能想加", "完美主义", "冻结需求，只修 Bug"), ("路演稿像读说明书", "没有故事线", "按问题-方案-Demo-反思重写"), ("现场可能打不开", "没有备用方案", "准备录屏和截图")]),
        slide_shell(day, 16, total, "验收标准", "今天下课前必须能演示", three_col([card("Demo", ul(["能打开", "主流程跑通", "有真实内容"]), "success"), card("工程证据", ul(["提示词", "版本", "Bug", "测试"]), "success"), card("展示", ul(["5 页结构", "分工", "备用材料"]), "success")])),
        summary_slide(day, 17, total, ["理解 Agentic Engineering 的角色协作", "完成综合项目 Demo", "准备好 Day 6 路演材料"], "Day 6 保持原安排：就业锦囊、LLM-Wiki、正式路演和结业。"),
        slide_shell(day, 18, total, "讲师备课页", "Day 5 准备清单", two_col(card("模板", ul(["工作流表", "测试清单", "路演 5 页模板", "评分表"]), "primary"), card("控场", ul(["30 分钟检查一次", "冻结需求时间点", "备用方案提醒"]), "accent"))),
    ]
    return "Agentic Engineering 综合项目", slides


def _day1_env_sample():
    day, total = 1, 25
    slides = [
        cover(day, total, "AI 使用底层能力", "先学会判断、提问和验证，再进入工具实战", ["提示词结构", "事实核查", "学习助手"]),
        slide_shell(day, 2, total, "AI 圈变化", "2022-2026：AI 从聊天窗口变成工作流伙伴", f"""
        <div class="evolution-grid">
          <div class="evolution-main">
            <div class="evolution-table">
              {compact_table(["年份", "代表变化", "高频名词", "给学生的课堂解释"], [
                  ("2022", "ChatGPT 出圈，自然语言交互进入大众视野", "ChatGPT / AIGC / Prompt", "不用写代码，也能让机器帮我生成内容"),
                  ("2023", "模型能力增强，开始连接外部工具", "GPT-4 / Claude / Function Calling / Plugin", "AI 不只回答，还能按格式发出工具调用指令"),
                  ("2024", "多模态爆发，文字、图片、语音、视频、代码打通", "GPT-4o / Claude 3 / Sora / Multimodal", "一个任务里可以同时处理资料、图片、声音和页面"),
                  ("2025", "AI IDE 和 Agent 工作流升温", "Vibe Coding / MCP / RAG / Agent / Context Engineering", "从背提示词变成拆任务、给上下文、验收结果"),
                  ("2026", "AI 成为学习、办公、设计、开发和求职的工具层", "Skill / Memory / Hooks / Subagents / Guardrails", "人的价值转向目标、审美、业务理解、风险判断"),
              ])}
            </div>
            <div class="evolution-bottom">
              {card("讲师串讲脚本", ul(["2022 是入口：AI 开始能听懂普通话式需求", "2023 是连接：模型开始能叫工具干活", "2024 是多模态：资料不再只有文字", "2025-2026 是工作流：能不能交付作品才是重点"]), "primary")}
              {card("现场互动问题", ul(["哪个名词你听过但说不清？", "哪个变化最影响学习和求职？", "如果新名词一直出现，你用什么方法判断它有没有用？"]), "accent")}
            </div>
          </div>
          <div class="evolution-side">
            {card("三条主线", ul(["交互变化：命令行和按钮 → 自然语言", "能力变化：写文字 → 多模态生成与工具调用", "工作方式变化：单次问答 → 可检查的工作流"]), "primary")}
            {card("教师讲法", ul(["不用把历史讲成编年史", "每一年只讲一个变化和一个课堂影响", "最后落到今天的原则：AI 给方案，人做决定"]), "accent")}
            {card("学生要记住", ul(["新名词会不断出现", "先问本质：输入是什么、处理什么、输出什么", "再问价值：它能不能帮我完成作品"]), "success")}
          </div>
        </div>"""),
        slide_shell(day, 3, total, "视频导入", "用 5 分钟建立共同语境：什么是 AI", f"""
        <div class="video-grid">
          {card("课堂播放", '<p class="source-link"><a href="https://www.bilibili.com/video/BV1Qz421X7AG" target="_blank">用5分钟讲明白什么是AI</a></p>' + ul(["播放前先说明：这不是休息，是建立共同语言", "只看 3-5 分钟，抓住 AI 能做什么、不能替人做什么", "播放后马上提问，不让视频变成“看过就算”"]), "primary")}
          {card("看完马上问", ul(["视频里 AI 完成的是哪类任务：识别、生成、决策，还是执行？", "哪一步仍然必须由人来判断？", "如果今天让 AI 帮你学习，你会先让它问你什么？", "把答案写到个人能力目标卡上"]), "accent")}
          {card("教师话术", ul(["今天不要求大家背定义", "我们只抓一个判断：AI 可以生成方案，但人负责目标和取舍", "后面所有工具练习都按这个标准验收"]), "success")}
          {card("学生记录", ul(["写下一个你想让 AI 帮你完成的任务", "写下一个你不放心交给 AI 的环节", "写下今天最想解决的安装或使用问题"]), "primary")}
          {card("自然过渡", ul(["从视频进入时间表", "先完成环境", "再做学习计划和事实核查"]), "accent")}
        </div>"""),
        schedule_slide(day, 4, total, [
            ("08:30-09:50", "AI 时代能力导入 + 电脑配置检查 + Git / Node.js 安装"),
            ("10:05-11:25", "Python / Claude Code CLI 安装 + 第一次命令行体验"),
            ("13:00-14:20", "AI 使用原则：让 AI 提问、给方案，人做决定"),
            ("14:35-15:55", "事实核查 + 今日环境验收 + 学习计划提交"),
        ], ["环境检查表", "Git/Node/Python/Claude Code 安装验证", "第一次 CLI 对话记录", "个人学习计划"]),
        theory_lab_slide(day, 5, total, "先讲清楚：AI 时代人要提升什么能力", ["持续学习：工具一直变，学习方法不能断", "动手实践：只听懂没用，要做出东西", "想象力：会让 AI 发散方案，但不被方案牵着走", "设计美感：让别人愿意看、看得懂、记得住", "业务理解与决策：AI 给建议，人判断取舍"], ["展示一个任务：从“我想学 AI”到“5 天内做出作品”", "让 AI 先问问题，再给 3 个方案", "老师现场选择一个方案并说明理由"], ["学生写下自己最想提升的一个能力", "同桌互问：这个能力能不能通过作品证明"], ["个人能力目标卡"]),
        slide_shell(day, 6, total, "环境准备", "安装前先检查电脑是否能上课", two_col(
            card("建议配置", ul(["Windows 10/11 64 位或 macOS 10.15+", "内存 8GB 以上更稳，最低 4GB 可尝试", "剩余磁盘空间 10GB 以上", "网络可访问工具官网和 npm", "拥有本机管理员权限或能安装软件"]), "primary"),
            card("为什么要先检查", ul(["Claude Code 官方要求 4GB+ 内存、x64 或 ARM64 处理器", "命令行工具依赖系统 PATH", "安装失败大多不是 AI 问题，而是系统、权限、网络问题", "学生先学会自查，后面排错会轻松很多"]), "accent"),
        )),
        slide_shell(day, 7, total, "Windows 检查命令", "先知道自己的电脑情况，再安装", compact_table(["检查项", "PowerShell 命令", "看什么"], [
            ("系统版本", "Get-ComputerInfo | Select-Object OsName,OsVersion,OsArchitecture", "Windows 10/11，64 位"),
            ("内存", "Get-CimInstance Win32_ComputerSystem | Select-Object TotalPhysicalMemory", "建议 8GB+"),
            ("磁盘", "Get-PSDrive C", "Free 大于 10GB"),
            ("包管理器", "winget --version", "能输出版本号"),
            ("网络", "ping nodejs.org", "能解析并返回响应"),
        ])),
        slide_shell(day, 8, total, "macOS 检查命令", "Mac 同学先确认系统、芯片和工具链", compact_table(["检查项", "Terminal 命令", "看什么"], [
            ("系统版本", "sw_vers", "macOS 10.15+"),
            ("芯片架构", "uname -m", "arm64 或 x86_64"),
            ("内存", "sysctl hw.memsize", "建议 8GB+"),
            ("命令行工具", "xcode-select -p", "能输出路径；没有就装 CLT"),
            ("Homebrew", "brew --version", "能输出版本号；没有则先装 Homebrew"),
        ])),
        slide_shell(day, 9, total, "安装 Git", "Git 是项目版本管理工具，也让很多 CLI 工具工作更稳定", three_col([
            card("Windows PowerShell", ul(["winget install --id Git.Git -e --source winget", "关闭并重新打开 PowerShell", "git --version"]), "primary"),
            card("macOS Terminal", ul(["xcode-select --install", "或：brew install git", "git --version"]), "accent"),
            card("验收/注意", ul(["能看到 git version 才算完成", "Windows 安装后必须重开终端", "Git Bash 可作为备用终端", "失败时改用 git-scm.com 安装包"]), "success"),
        ])),
        slide_shell(day, 10, total, "安装 Node.js", "Node.js 提供 npm，后续网页工具和自动化练习会用到", three_col([
            card("Windows PowerShell", ul(["winget install --id OpenJS.NodeJS.LTS -e --source winget", "关闭并重新打开 PowerShell", "node -v", "npm -v"]), "primary"),
            card("macOS Terminal", ul(["brew install node", "node -v", "npm -v", "确认 Node.js 版本 >= 18"]), "accent"),
            card("验收/注意", ul(["课堂统一使用 LTS 版本", "Node >= 18 便于兼容前端工具", "npm 不通时先换网络", "失败时用 nodejs.org 安装包"]), "success"),
        ])),
        slide_shell(day, 11, total, "安装 Python", "Python 用于课堂脚本、数据处理和后续自动化练习", three_col([
            card("Windows PowerShell", ul(["winget install --id Python.Python.3.12 -e --source winget", "关闭并重新打开 PowerShell", "python --version", "py --version"]), "primary"),
            card("macOS Terminal", ul(["brew install python", "python3 --version", "pip3 --version"]), "accent"),
            card("验收/注意", ul(["Windows 可用 py 启动器兜底", "Mac 常用 python3 而不是 python", "pip 用于后续安装数据工具", "不要混装太多 Python 版本"]), "success"),
        ])),
        slide_shell(day, 12, total, "安装 Claude Code CLI", "Claude Code 是命令行 AI 编程/项目协作工具", three_col([
            card("Windows PowerShell", ul(["irm https://claude.ai/install.ps1 | iex", "或：winget install Anthropic.ClaudeCode", "claude --version", "claude doctor"]), "primary"),
            card("macOS Terminal", ul(["curl -fsSL https://claude.ai/install.sh | bash", "或：brew install --cask claude-code", "claude --version", "claude doctor"]), "accent"),
            card("验收/注意", ul(["Windows 推荐先装 Git for Windows", "Claude Code 需要可用账号登录", "只在课堂练习文件夹里运行", "不要让 AI 随意改系统文件"]), "success"),
        ])),
        troubleshooting_slide(day, 13, total, "安装常见问题：先排环境，不要怪 AI", [
            ("winget 不存在", "Windows 应用安装程序过旧", "更新 App Installer，或改用官网安装包"),
            ("brew 不存在", "Mac 未安装 Homebrew", "先安装 Homebrew，或使用官网安装包"),
            ("Claude 安装后打不开", "PATH 未刷新或安装未完成", "关闭终端重开；再执行 claude --version"),
            ("命令安装后找不到", "PATH 未刷新", "关闭终端重新打开，再执行 version 命令"),
            ("网络超时", "npm 源或校园网限制", "换网络或让助教统一准备离线方案"),
        ]),
        slide_shell(day, 14, total, "今日环境验收", "四个工具都要能输出版本号", compact_table(["工具", "验收命令", "通过标准"], [
            ("Git", "git --version", "输出 git 版本"),
            ("Node.js", "node -v", "版本 >= 18"),
            ("npm", "npm -v", "输出 npm 版本"),
            ("Python", "python --version 或 python3 --version", "输出 Python 3.x"),
            ("Claude Code", "claude --version / claude doctor", "能启动并完成检查；认证问题可课后处理"),
        ])),
        theory_lab_slide(day, 15, total, "提示词只讲一句话", ["不要背模板", "不要追求花哨提示词", "先让 AI 问问题，再让 AI 给方案", "人负责目标、取舍和最终决定"], ["老师输入：我想做一个 AI 学习计划，先别回答，请先问我 3 个关键问题，再给我 3 个方案", "老师选择一个方案，说明为什么"], ["学生用自己的学习目标试一次", "只保留自己真正愿意执行的方案"], ["个人学习计划 v1"]),
        slide_shell(day, 16, total, "第一次 Claude Code 体验", "不是为了学代码，而是理解“AI 项目助手”怎么协作", two_col(
            card("教师演示", ul(["新建一个空文件夹", "在终端进入文件夹", "输入 claude", "让 Claude 先问项目目标", "让它生成 README 草稿"]), "primary"),
            card("学生跟做", ul(["创建 ai-first-day 文件夹", "启动 claude", "让它问 3 个问题", "生成一份学习计划 README", "不要让它随便改系统文件"]), "success"),
        )),
        troubleshooting_slide(day, 17, total, "Claude Code 使用安全", [
            ("AI 想修改很多文件", "任务范围没说清", "要求只在当前练习文件夹内操作"),
            ("AI 让你运行看不懂的命令", "风险未知", "先问：这个命令做什么？会修改哪里？"),
            ("登录或认证失败", "账号/网络问题", "先完成环境验收，认证问题课后由助教处理"),
        ]),
        runbook_slide(day, 18, total, 1, "AI 学习路线设计", "任意对话 AI / Claude Code CLI", ["准备自己的学习目标", "准备每天可用时间", "准备一个 ai-learning-plan.md"], ["让 AI 先问 3 个问题", "让 AI 给 3 个方案", "老师选择一个方案", "让 AI 生成 5 天计划", "老师删掉不现实任务"], ["写自己的目标", "回答 AI 的问题", "选择一个方案", "生成计划", "删掉 1 个不现实任务"], "我想学习【主题】。先不要直接给计划，请先问我 3 个关键问题，再给我 3 个方案，并说明优缺点。最终由我选择方案。", [("AI 直接给计划", "补一句：先问问题，不要直接回答"), ("方案太满", "限制每天时间和产出"), ("学生照单全收", "要求删掉 1 项并说明理由")]),
        theory_lab_slide(day, 19, total, "事实核查：AI 会错，人要负责", ["AI 会生成看似合理的错误", "重要信息必须核查来源", "事实、观点、推测要分开", "决策不能外包给 AI"], ["老师让 AI 回答一个热点问题", "要求 AI 标出事实/观点/推测", "点开来源验证其中一条"], ["学生选择一个问题做核查", "标出一条不确定信息"], ["事实核查卡"]),
        practice_slide(day, 20, total, "学生实操：事实核查卡", ["选择一个热点问题", "让 AI 给 3 个观点", "要求每个观点给依据", "标出不确定项", "写出自己的判断"], ["有来源", "有不确定项", "不是复制 AI 原文", "最终判断是学生自己写的"], "事实核查卡"),
        slide_shell(day, 21, total, "AI 名词视频", "先看话术，再拆本质", f"""
        <div class="term-video-grid">
          <div class="video-panel">
            <video src="../assets/ai-terms.mp4" controls preload="metadata"></video>
          </div>
          <div class="term-video-side">
            {card("看视频前先提醒", ul(["不要被新名词吓住", "不要把营销话术当技术革命", "听到一个名词，先问：它到底输入什么、处理什么、输出什么"]), "primary")}
            {card("看视频时记录", ul(["圈出你第一次听到的 3 个名词", "写下它被包装成了什么", "写下它真实像哪个你已经知道的东西"]), "accent")}
            {card("看完马上拆", ul(["Skill 像插件/API 封装", "MCP 像统一接口标准", "RAG 像开卷考试", "Agent 很多时候是调度程序 + LLM"]), "success")}
          </div>
        </div>"""),
        slide_shell(day, 22, total, "AI 热词拆解地图", "名字可以很新，本质要讲清楚", f"""
        <div class="term-board">
          <div class="term-table-wrap">
            {compact_table(["热词", "真实技术内核", "容易被包装成", "课堂判断"], [
              ("LLM", "大规模预训练语言模型", "万能大脑", "能生成语言，但会错，要核查"),
              ("Prompt", "给模型的文本指令和上下文", "神奇咒语", "不用背模板，让 AI 先问问题"),
              ("Function Calling", "让模型按 JSON 等格式发出调用指令", "模型会操作软件", "真正执行的是外部工具/API"),
              ("Tool Use", "模型选择并调用搜索、文件、代码等工具", "全自动助手", "要检查工具输入和输出"),
              ("Skill", "封装好的可复用能力或操作步骤", "全新智能模块", "本质像插件、脚本、API 包装"),
              ("MCP", "模型与外部工具/资源的统一连接协议", "革命性生态", "更像 USB-C：统一接口，降低适配成本"),
              ("RAG", "先检索资料，再把资料交给模型生成", "消灭幻觉", "资料不准，回答仍然不准"),
              ("Memory", "保存偏好、历史、项目约定等上下文", "AI 记住一切", "记忆要可查看、可删除、可纠错"),
              ("Hooks", "在特定动作前后自动触发脚本或检查", "自动化智能", "本质是事件触发器"),
              ("Task / Subagents", "把任务拆给专门角色或子流程处理", "多智能体军团", "关键是分工、交接和验收"),
              ("AI Agent", "目标拆解 + 工具调用 + 状态记录 + 循环执行", "自主智能体", "多数仍要人设范围、看中间结果"),
              ("Vibe Coding", "用自然语言描述产品感觉和功能，AI 生成代码", "不会代码也能做产品", "人必须会描述需求、测试和改错"),
              ("Vibe Design", "用自然语言描述风格、版式、情绪和视觉目标", "不会设计也能变好看", "人要有审美判断和修改意见"),
              ("Agentic Engineering", "把需求、上下文、工具、检查、迭代组织成工程流程", "AI 自动工程师", "本质是可控流程：目标、边界、证据、复盘"),
            ])}
          </div>
          <div class="term-bottom">
            {card("课堂拆词三步法", ul(["第一问：输入是什么？", "第二问：中间处理了什么？", "第三问：输出由谁验收？"]), "primary")}
            {card("学生练习", ul(["任选 1 个热词", "用自己的话说出它像什么", "指出它不能替人做的部分"]), "accent")}
            {card("正确答案示例", ul(["MCP 像统一接口，不是万能智能", "RAG 像开卷考试，不保证资料正确", "Agent 像调度流程，不等于完全自主"]), "success")}
          </div>
        </div>"""),
        slide_shell(day, 23, total, "Day 1 标准答案", "今天不是唯一答案，而是检查标准", three_col([
            card("环境", ul(["4 个工具有版本号", "Claude doctor 能运行", "知道如何重新打开终端刷新 PATH"]), "success"),
            card("学习计划", ul(["AI 先问问题", "给 3 个方案", "学生自己选择", "每天有产出"]), "success"),
            card("事实核查", ul(["来源可打开", "事实/观点分开", "有个人判断"]), "success"),
        ])),
        slide_shell(day, 24, total, "讲师备课页", "Day 1 上课前准备", two_col(
            card("材料", ul(["Git/Node/Python/Claude 官方安装页备用链接", "Windows/macOS 分组名单", "环境检查表", "短视频链接", "学习计划模板"]), "primary"),
            card("风险预案", ul(["校园网限制 npm：准备热点或备用网络", "无管理员权限：准备便携安装方案", "老电脑慢：允许两人一组完成 CLI 部分"]), "accent"),
        )),
        summary_slide(day, 25, total, ["知道 2022-2026 AI 圈主要变化和高频名词", "能拆开常见 AI 热词的真实技术内核", "完成基础环境检查与安装", "理解 AI 使用原则：AI 提问和给方案，人做决定", "完成个人学习计划和事实核查卡"], "Day 2 进入 AI 办公：会议纪要、任务调度、数据洞察和汇报文档。"),
    ]
    return "AI 使用底层能力", slides


build_day_1 = _day1_env_sample


def _day2_final():
    day, total = 2, 20
    slides = [
        cover(day, total, "AI 办公自动化", "把杂乱信息变成任务、数据洞察和可发送报告", ["会议纪要", "数据洞察", "任务调度"]),
        schedule_slide(day, 2, total, [
            ("08:30-09:50", "理论：办公自动化的核心不是写得快，而是信息可追踪"),
            ("10:05-11:25", "案例 1：会议指挥台，聊天记录变纪要、任务表、风险清单"),
            ("13:00-14:20", "案例 2：数据侦探，乱表诊断、清洗、洞察和图表说明"),
            ("14:35-15:55", "案例 3：报告导演，把事实材料改成不同对象能看的报告"),
        ], ["会议纪要", "任务调度表", "数据洞察卡", "正式报告"]),
        slide_shell(day, 3, total, "理论导入", "办公 AI 的四步闭环：提取、整理、生成、审核", compact_table(["步骤", "AI 能做什么", "人必须做什么", "课堂检查"], [
            ("提取", "从聊天、表格、记录里找事实", "确认事实是否真的出现过", "每条结论有原文或数据依据"),
            ("整理", "分类、去重、合并同类项", "决定哪些信息重要", "无关闲聊不进入正式材料"),
            ("生成", "写纪要、周报、任务表、邮件", "确定读者、语气和目的", "同一材料能改成不同版本"),
            ("审核", "帮忙找矛盾和缺漏", "对最终文档负责", "没有依据就删掉或标待确认"),
        ])),
        theory_lab_slide(day, 4, total, "课堂示例：同一段聊天，为什么不能直接让 AI 写纪要", ["聊天记录里有闲聊、口头承诺、模糊时间和未确认负责人", "AI 容易把语气当事实，把猜测写成结论", "正式纪要的价值是可执行，不是像公文", "先提取事实表，再生成纪要"], ["投屏一段 12 行模拟聊天", "先让 AI 直接写纪要，指出 3 个问题", "再用“事实表→任务表→纪要”的顺序重做"], ["学生标出：事实、猜测、待确认", "同桌互查有没有编造负责人"], ["事实提取表"]),
        runbook_slide(day, 5, total, 1, "会议指挥台", "WorkBuddy / 文档 AI / 飞书或微信聊天记录", ["准备模拟会议记录", "记录里包含任务、争议、截止时间、无关闲聊", "准备一份纪要模板和任务表模板"], ["导入聊天记录", "先提取事实表", "再生成任务表", "最后生成正式纪要", "标出待确认项"], ["复制记录", "生成事实表", "检查负责人和时间", "生成纪要", "删除无关闲聊"], "请先不要写纪要。先从下面记录里提取事实表：原文依据、事项、负责人、时间、状态、待确认项。没有明确出现的信息写待确认。", [("AI 编负责人", "要求负责人必须来自原文"), ("纪要太长", "每个议题不超过 2 行"), ("闲聊进入正文", "要求只保留影响任务和决策的信息")]),
        practice_slide(day, 6, total, "学生实操：会议记录变任务表", ["领取一段聊天记录", "标出事实/猜测/待确认", "生成任务表", "生成正式纪要", "人工删除 3 句废话"], ["每个任务有依据", "负责人不编造", "截止时间不确定就标待确认", "纪要可直接发给小组"], "纪要 + 任务表"),
        slide_shell(day, 7, total, "正确答案示例", "会议类任务的标准不是漂亮，而是可执行", compact_table(["检查项", "错误示例", "合格示例"], [
            ("负责人", "项目由小王负责", "负责人：待确认；原文只说“我来看看”"),
            ("截止时间", "本周完成", "截止：周五 18:00；依据：第 7 行"),
            ("风险", "大家积极推进", "风险：数据源未确认，需 5 月 22 日前补充"),
            ("纪要语气", "本次会议圆满完成", "本次会议确认 3 项任务，2 项仍待确认"),
        ])),
        slide_shell(day, 8, total, "数据最小理论", "零基础只要先分清三层分析", three_col([
            card("发生了什么", ul(["总量", "排名", "趋势", "异常"]), "primary"),
            card("为什么可能这样", ul(["时间", "类别", "渠道", "缺失值"]), "accent"),
            card("下一步做什么", ul(["补数据", "重点跟进", "调整资源", "继续观察"]), "success"),
        ])),
        runbook_slide(day, 9, total, 2, "数据侦探", "WorkBuddy / Excel / WPS 表格", ["准备一份乱表：空值、重复、格式不统一、异常金额", "准备一份清洗后参考表", "要求先诊断，不急着画图"], ["上传乱表", "让 AI 输出数据质量诊断", "确认清洗规则", "生成 3 条洞察", "要求每条洞察写证据"], ["上传表格", "生成问题清单", "处理重复/空值/格式", "生成洞察卡", "核对 1 个关键数字"], "请检查这份表格，先输出数据质量问题，不要直接写结论。字段包括：问题类型、所在列、影响、处理建议。然后再给 3 条“发现-证据-建议”。", [("AI 直接写结论", "先诊断数据质量"), ("缺失值被乱填", "缺失只标记，不猜测"), ("洞察没证据", "要求附字段、数值或行数依据")]),
        practice_slide(day, 10, total, "学生实操：一页数据洞察卡", ["上传乱表", "列出至少 4 类问题", "清洗 2 类最明显问题", "生成 3 条洞察", "给每条洞察补证据"], ["有问题清单", "保留原始表", "洞察有证据", "建议不是空话"], "数据洞察卡"),
        slide_shell(day, 11, total, "正确答案示例", "数据洞察要按“发现-证据-建议”写", compact_table(["类型", "不合格写法", "合格写法"], [
            ("发现", "销售情况不错", "A 类产品销售额最高，占总额 38%"),
            ("证据", "看起来比较多", "依据：类别透视表，A 类 18,600 元"),
            ("建议", "继续努力", "下周优先补 A 类库存，并核查 B 类退货原因"),
            ("风险", "数据没问题", "日期列存在 3 种格式，趋势分析前需统一"),
        ])),
        runbook_slide(day, 12, total, 3, "报告导演", "WorkBuddy / 文档 AI", ["准备会议纪要和数据洞察卡", "准备 3 个读者：老师、领导、同学", "要求同一材料写 3 个版本"], ["先确定读者和目的", "生成老师版", "生成领导版", "对比重点变化", "删除无依据夸大句"], ["选择一个读者", "写清报告目的", "生成报告", "标出事实依据", "改写最后一段行动建议"], "请根据材料写给【对象】看的报告。结构：背景、完成情况、问题、数据依据、下一步、需要支持。要求具体，不使用材料中没有的信息。", [("报告像套话", "每段必须引用材料依据"), ("对象不明确", "先写读者和目的"), ("过度包装", "删除显著、全面、极大等无依据词")]),
        drill_slide(day, 13, total, "课堂互动：同一材料三种报告", ["10 分钟：三组分别写老师/领导/同学版", "15 分钟：互换阅读", "10 分钟：判断哪版适合谁", "10 分钟：现场改一版"], ["强调对象决定表达", "指出无依据句子", "让学生看到语气差异"], ["生成版本", "互评语气", "标注依据"], ["三版报告"], ["对象匹配", "事实准确", "结构清楚"]),
        slide_shell(day, 14, total, "任务调度", "AI 可以帮你排任务，但优先级要由人判断", compact_table(["任务", "AI 可做", "人要判断", "示例"], [
            ("拆任务", "把目标拆成步骤", "步骤是否真实可做", "资料收集、清洗、写报告、复核"),
            ("排优先级", "按时间/依赖排序", "哪件最影响交付", "先清洗表格，再写数据结论"),
            ("提醒风险", "列出延期、缺资料、责任不清", "风险是否严重", "负责人待确认不能直接写死"),
            ("生成看板", "输出表格或清单", "是否适合团队执行", "今日/明日/待确认"),
        ])),
        troubleshooting_slide(day, 15, total, "办公场景翻车点", [("纪要出现不存在的人", "AI 根据上下文猜测", "负责人必须来自原文，否则待确认"), ("数据洞察没有证据", "模型在概括而非分析", "每条洞察附字段、数值或行数依据"), ("报告像宣传稿", "缺少对象和目的", "补充读者、场景和长度限制"), ("任务排满但没人做", "AI 不知道现实资源", "人删掉不现实任务并说明理由")]),
        project_board(day, 16, total, "Day 2 办公流水线", [("输入", ["聊天", "表格", "记录", "模板"], "primary"), ("提取", ["事实", "任务", "数字", "风险"], "accent"), ("生成", ["纪要", "洞察", "报告", "看板"], "success"), ("审核", ["依据", "对象", "语气", "可执行"], "primary")]),
        practice_slide(day, 17, total, "综合练习：从会议到周报", ["用会议记录生成任务清单", "用表格生成洞察卡", "把两者合成周报", "人工审核并标注修改"], ["流程完整", "事实有依据", "报告可发送", "有修改痕迹"], "纪要 + 洞察卡 + 周报"),
        slide_shell(day, 18, total, "今日提交物", "下课前交 4 件办公成果", three_col([
            card("纪要", ul(["议题", "结论", "任务", "待确认"]), "success"),
            card("洞察卡", ul(["问题清单", "3 条洞察", "数据依据"]), "success"),
            card("周报", ul(["对象明确", "结构完整", "无编造"]), "success"),
        ])),
        summary_slide(day, 19, total, ["会把聊天记录变成纪要和任务表", "会把乱表变成数据洞察卡", "会面向不同对象写正式报告"], "Day 3 进入内容创作和 Vibe Design：把信息做成别人愿意看、看得懂的作品。"),
        slide_shell(day, 20, total, "讲师备课页", "Day 2 上课前准备", two_col(
            card("材料", ul(["模拟会议记录", "乱表 Excel", "清洗参考表", "报告模板", "任务调度表"]), "primary"),
            card("控场", ul(["先事实表再纪要", "每条洞察必须有证据", "每 40 分钟收一次中间产物"]), "accent"),
        )),
    ]
    return "AI 办公自动化", slides


def _day3_final():
    day, total = 3, 20
    slides = [
        cover(day, total, "AI 内容创作 + Vibe Design", "让 AI 先给方案，人负责审美、取舍和表达", ["内容策略", "视觉设计", "PPT 表达"]),
        schedule_slide(day, 2, total, [
            ("08:30-09:50", "理论：内容创作不是让 AI 写作文，而是设计传播目标"),
            ("10:05-11:25", "案例 4：活动传播包，标题、脚本、海报文案一次做清"),
            ("13:00-14:20", "案例 5：Vibe Design，风格板、首屏、海报迭代"),
            ("14:35-15:55", "案例 6：PPT 故事板，把资料变成 5 页路演结构"),
        ], ["传播策略卡", "内容三件套", "视觉风格板", "5 页 PPT 故事板"]),
        slide_shell(day, 3, total, "理论导入", "内容创作的五件事：目标、受众、钩子、证据、行动", compact_table(["要素", "问题", "AI 能帮什么", "人要判断什么"], [
            ("目标", "希望谁做什么", "列出传播目标", "目标是否真实可达"),
            ("受众", "对方为什么关心", "分析痛点和兴趣点", "是否符合校园语境"),
            ("钩子", "第一眼为什么停下", "给标题和开场", "有没有标题党"),
            ("证据", "为什么相信你", "整理事实、案例、数据", "证据是否可靠"),
            ("行动", "看完下一步做什么", "设计按钮和结尾", "动作是否明确"),
        ])),
        theory_lab_slide(day, 4, total, "课堂示例：把“AI 分享会”从空话改成可发布内容", ["坏内容的问题不是短，而是没有对象、没有理由、没有行动", "AI 很擅长给很多版本，但容易夸张", "学生要学会筛选，而不是全收", "内容最终要能被设计和展示承接"], ["投屏一个空泛标题", "让 AI 生成 10 个标题", "用五件事筛掉 7 个", "保留 3 个并改成校园语气"], ["学生给自己的主题写目标和受众", "圈出 1 个夸张词并替换"], ["传播策略卡"]),
        runbook_slide(day, 5, total, 4, "活动传播包", "QClaw / 文档 AI / 图像生成工具", ["准备 4 个主题：AI 工具分享会、社团招新、作品集发布、求职经验会", "准备传播策略卡模板", "要求每组选择一个受众"], ["确定目标和受众", "生成标题池", "筛选 3 个并说明理由", "生成 30 秒脚本", "生成海报文案"], ["选主题", "写受众和目标", "生成标题池", "筛选标题", "输出脚本和海报文案"], "请先问我目标受众、发布平台、行动目标。然后为活动输出：10 个标题、3 个开场钩子、30 秒脚本、海报主标题/副标题/行动按钮。", [("标题像广告", "加入校园语境和真实利益点"), ("脚本太长", "限制 30 秒并按镜头分段"), ("没有行动", "最后必须有报名、访问或收藏动作")]),
        practice_slide(day, 6, total, "学生实操：内容三件套", ["确定活动主题", "写受众和目标", "生成标题池", "完成 30 秒脚本", "写海报文案"], ["标题有钩子", "脚本能拍", "文案不夸张", "行动明确"], "标题池 + 脚本 + 海报文案"),
        slide_shell(day, 7, total, "正确答案示例", "内容不是越热闹越好，而是越具体越好", compact_table(["项目", "不合格", "合格"], [
            ("标题", "AI 时代必看！颠覆你的认知", "不会写代码，也能做出第一个 AI 小工具"),
            ("受众", "所有人", "想做作品集但没有技术基础的大一学生"),
            ("证据", "很有用", "现场完成报名页、评分器、作品截图"),
            ("行动", "欢迎参加", "扫码报名，带电脑到 302 教室"),
        ])),
        evolution_slide(day, 8, total),
        slide_shell(day, 9, total, "Vibe Design 理论", "风格词必须落到颜色、字体、版式和信息层级", compact_table(["学生常说", "需要追问", "可执行表达"], [
            ("高级一点", "高级体现在哪里", "少色彩、大留白、清晰网格、弱装饰"),
            ("科技感", "冷科技还是校园科技", "蓝白主色、数据卡片、线性图标、轻背景"),
            ("年轻活泼", "活泼到什么程度", "明亮色块、圆角卡片、短句标题"),
            ("太乱", "哪里乱", "标题弱、卖点多、按钮不明显、图片抢视线"),
        ])),
        runbook_slide(day, 10, total, 5, "Vibe Design 风格板", "图像生成工具 / Trae 预览 / 文档 AI", ["准备上午内容三件套", "准备 3 种风格方向：校园清爽、科技发布、杂志编辑", "要求每组只选一种风格"], ["把文案交给 AI", "生成风格板", "要求输出颜色、字体、布局、图片建议", "指出第一版问题", "生成第二版"], ["选择风格", "生成风格板", "写 3 条反馈", "生成第二版", "保存前后对比"], "请基于活动文案生成视觉风格板。输出：风格关键词、主色/辅助色/强调色、字体气质、版式结构、图片建议、不要使用的元素。", [("风格太泛", "要求给颜色和布局"), ("元素太多", "限制一页只保留主标题、3 个卖点、行动按钮"), ("像模板", "删除装饰，增强信息层级")]),
        practice_slide(day, 11, total, "学生实操：风格板二次迭代", ["输入内容三件套", "生成第一版风格板", "写 3 条具体反馈", "生成第二版", "同桌评价"], ["颜色不超过 3 种", "标题层级清楚", "文案可读", "有修改理由"], "视觉风格板 v2"),
        runbook_slide(day, 12, total, 6, "海报/落地页首屏", "Trae / 图像生成工具", ["准备上午文案和风格板", "只做首屏或海报，不做完整网站", "要求可课堂展示"], ["把风格板转成页面结构", "生成首屏 HTML 或海报方案", "检查文字层级", "按反馈改版", "保存最终截图"], ["输入风格板和文案", "生成首屏/海报", "检查主题、卖点、行动", "迭代一次"], "请根据文案和视觉风格板，生成一个活动落地页首屏。包含：主标题、副标题、3 个卖点、活动信息、行动按钮。信息层级必须清楚。", [("像官网模板", "改成活动首屏，减少模块"), ("文字太多", "只保留主标题、副标题、3 个卖点"), ("按钮不明确", "按钮文字改成具体动作")]),
        drill_slide(day, 13, total, "互动：全班审稿会", ["10 分钟：每组选 1 张图", "20 分钟：全班按标准打分", "20 分钟：每组现场改 1 次"], ["只评价信息层级和可读性", "不要泛泛说好看/不好看", "要求反馈能执行"], ["展示作品", "接受 2 条修改意见", "现场迭代"], ["修改前后对比"], ["反馈具体", "改动明显", "主题更清楚"]),
        slide_shell(day, 14, total, "PPT 最小理论", "路演 PPT 不是把文档贴上去，而是组织注意力", compact_table(["页", "要回答的问题", "不要做什么"], [
            ("1 问题", "为什么要做", "不要铺长背景"),
            ("2 用户", "给谁用", "不要写所有人"),
            ("3 方案", "怎么解决", "不要堆功能"),
            ("4 结果", "做出了什么", "不要只放概念"),
            ("5 下一步", "如何改进", "不要喊口号"),
        ])),
        runbook_slide(day, 15, total, 7, "5 页 PPT 故事板", "文档 AI / PPT 工具 / Trae 截图", ["准备海报/首屏截图", "准备内容三件套", "统一 5 页结构"], ["把资料整理成 5 页大纲", "每页只保留 1 个重点", "生成讲稿要点", "删除长段文字", "补截图占位"], ["生成 5 页故事板", "每页写一句话目标", "补 1 张截图", "写 1 分钟介绍"], "请把下面资料整理成 5 页路演 PPT 故事板。每页包括：页标题、一句话目标、3 个要点、建议配图。不要写长段落。", [("PPT 像论文", "每页只留 3 个要点"), ("没有视觉证据", "必须放截图或作品图"), ("讲稿太长", "限制 1 分钟介绍")]),
        practice_slide(day, 16, total, "学生实操：5 页故事板", ["整理今天作品", "生成 5 页 PPT 大纲", "每页删到 3 个要点", "补截图位置", "写 1 分钟介绍"], ["每页一个重点", "有作品截图", "文字不拥挤", "能讲出来"], "5 页 PPT 故事板"),
        troubleshooting_slide(day, 17, total, "内容和设计翻车点", [("标题党", "AI 迎合营销语气", "要求真实、校园、不要夸大"), ("设计空泛", "风格词没有落地", "必须输出颜色、布局、字体气质"), ("页面漂亮但信息不清", "视觉压过内容", "先读主标题，再看卖点和行动"), ("PPT 太满", "把文档搬进幻灯片", "一页只讲一个重点")]),
        project_board(day, 18, total, "Day 3 成果板", [("策略", ["目标", "受众", "平台", "行动"], "primary"), ("内容", ["标题池", "脚本", "海报文案", "风险词"], "accent"), ("视觉", ["风格词", "配色", "布局", "图片建议"], "success"), ("展示", ["海报", "首屏", "PPT", "讲稿"], "primary")]),
        summary_slide(day, 19, total, ["会用 AI 做内容策略", "会把风格词变成视觉决策", "会把资料整理成 5 页路演故事板"], "Day 4 进入 Vibe Coding：把作品变成可运行的互动页面/小工具。"),
        slide_shell(day, 20, total, "讲师备课页", "Day 3 上课前准备", two_col(
            card("素材", ul(["4 个活动主题", "好坏标题例子", "好坏海报例子", "风格方向参考", "PPT 故事板模板"]), "primary"),
            card("控场", ul(["不要只追求好看", "反馈必须能执行", "保留前后对比", "PPT 每页只讲一个重点"]), "accent"),
        )),
    ]
    return "AI 内容创作 + Vibe Design", slides


def _day4_final():
    day, total = 4, 20
    slides = [
        cover(day, total, "Vibe Coding 产品实战", "不会写代码也要会描述需求、测试结果和修 Bug", ["需求表达", "AI 编程", "Debug"]),
        schedule_slide(day, 2, total, [
            ("08:30-09:50", "理论：Vibe Coding 不是许愿，是产品需求表达"),
            ("10:05-11:25", "案例 7：把 Day 3 首屏变成可运行活动页"),
            ("13:00-14:20", "案例 8：做一个提示词评分器/学习计划生成器"),
            ("14:35-15:55", "案例 9：Bug 修理铺，复现、描述、修复、回归测试"),
        ], ["需求说明书", "活动页 v1", "AI 小工具", "Bug 修复记录"]),
        slide_shell(day, 3, total, "理论导入", "产品需求的六个字段：用户、场景、输入、动作、输出、约束", compact_table(["字段", "必须写清", "例子"], [
            ("用户", "谁使用", "参加 AI 分享会的学生"),
            ("场景", "什么时候用", "扫码查看活动信息并报名"),
            ("输入", "用户提供什么", "姓名、班级、联系方式"),
            ("动作", "点击后发生什么", "提交、提示、统计"),
            ("输出", "用户看到什么", "报名成功提示和活动安排"),
            ("约束", "不能做什么", "不做后端，单文件 HTML"),
        ])),
        theory_lab_slide(day, 4, total, "课堂示例：为什么“帮我做网页”会失败", ["需求不清，AI 只能猜页面结构", "没有约束，AI 可能生成多文件、后端、复杂依赖", "没有验收，学生不知道算不算完成", "不会代码也能当产品经理和测试员"], ["先输入一句“帮我做活动页”", "展示失败点", "改成六字段需求", "再生成并对比"], ["学生把自己的 Day 3 作品改成六字段需求"], ["需求说明书 v1"]),
        runbook_slide(day, 5, total, 7, "活动页生成", "Trae Builder / 浏览器", ["准备 Day 3 文案和风格板", "准备需求公式表", "统一要求单文件 HTML"], ["把文案改成需求说明", "让 Trae 生成 HTML", "打开浏览器预览", "测试按钮", "让 AI 修第一处问题"], ["复制自己的文案", "写六字段需求", "生成活动页", "测试报名按钮", "保存 v1"], "请基于以下活动文案和视觉风格，生成单文件 HTML 活动页。功能：展示活动信息、3 个亮点、报名表单、点击提交后显示报名成功和活动提醒。不需要后端。", [("生成太多文件", "补充单文件 HTML"), ("按钮无反馈", "检查表单 submit/click 事件"), ("报名数据不会保存", "说明无后端限制，只做课堂演示")]),
        practice_slide(day, 6, total, "学生实操：活动页 v1", ["写六字段需求", "用 Trae 生成 HTML", "测试表单", "修 1 个问题", "截图保存"], ["可打开", "表单可输入", "按钮有反馈", "视觉沿用 Day 3"], "活动页 v1 + 需求说明"),
        slide_shell(day, 7, total, "正确答案示例", "活动页验收看主流程，不看代码多高级", compact_table(["检查", "不合格", "合格"], [
            ("打开", "依赖很多文件，路径报错", "一个 index.html 可直接打开"),
            ("表单", "能输入但提交没反应", "提交后显示成功提示"),
            ("信息", "只有好看背景", "主题、时间、地点、亮点、报名都清楚"),
            ("约束", "要求数据库登录", "课堂演示不做后端，说明限制"),
        ])),
        runbook_slide(day, 8, total, 8, "提示词评分器", "Trae / 浏览器 / 文档 AI", ["准备评分维度：目标、上下文、格式、约束、验收", "准备 3 个示例提示词", "要求学生做一个可交互工具"], ["展示评分标准", "让 AI 生成评分器页面", "输入烂提示词测试", "让工具给改进建议", "修复显示问题"], ["生成评分器", "输入自己的提示词", "查看评分和建议", "修改提示词再测一次"], "请做一个单文件 HTML 提示词评分器。用户粘贴提示词后，点击评分，页面按 5 个维度给分：目标、上下文、格式、约束、验收，并给出修改建议。无需调用真实 API，用前端规则模拟即可。", [("学生以为要接 API", "明确今天用规则模拟"), ("评分不准确", "强调这是学习工具，评分规则可人工调整"), ("JS 报错", "复制控制台错误让 Trae 修")]),
        theory_lab_slide(day, 9, total, "为什么提示词评分器适合 AI 课", ["它回扣 Day 1 的提示词原则", "它让学生理解评价标准", "它有输入、计算、输出完整交互", "它能成为课程作品集的一部分"], ["现场把烂提示词输入评分器", "根据建议改写后再评分"], ["学生比较改写前后分数"], ["提示词评分器 v1"]),
        practice_slide(day, 10, total, "学生实操：提示词评分器", ["复制工具需求", "生成 HTML", "测试 3 个提示词", "修改评分文案", "保存 v1/v2"], ["能输入", "能评分", "能给建议", "界面不重叠"], "提示词评分器 + 测试记录"),
        runbook_slide(day, 11, total, 9, "Bug 修理铺", "Trae / Chrome 控制台", ["准备故障版本页面", "故障包括按钮无反应、undefined、文字溢出", "准备 Bug 记录模板"], ["复现 Bug", "描述：操作-现象-期望", "复制控制台错误", "让 AI 一次只修一个", "回归测试"], ["列 3 个 Bug", "按优先级修", "每修一次测试", "记录修改前后"], "点击【按钮】后没有任何反应。请检查事件绑定和相关 JavaScript。只修复这个问题，不要重写页面，不要改变视觉样式。修复后说明改了哪里。", [("AI 重写全页", "加限制：不要重写，只改指定区域"), ("修完又坏", "回退到上一版本，重新只修一个问题"), ("学生不会看控制台", "讲师示范 F12/Console")]),
        slide_shell(day, 12, total, "Debug 理论", "修 Bug 的四步：复现、定位、修复、回归", compact_table(["步骤", "学生要写什么", "示例"], [
            ("复现", "我做了什么，出现什么", "点击提交后没有成功提示"),
            ("定位", "大概是哪类问题", "按钮事件可能没有绑定"),
            ("修复", "一次只改一处", "只检查 submit/click 事件"),
            ("回归", "修完再测旧功能", "输入为空、正常输入、重复点击都试一次"),
        ])),
        project_board(day, 13, total, "测试清单", [("功能", ["按钮", "输入", "输出", "清空"], "primary"), ("边界", ["空输入", "超长文本", "重复点击", "特殊符号"], "accent"), ("视觉", ["不重叠", "字号可读", "移动端基本可看"], "success"), ("证据", ["截图", "Bug 文案", "修复记录", "版本文件"], "primary")]),
        practice_slide(day, 14, total, "学生实操：修自己的页面", ["打开活动页或评分器", "列出 3 个问题", "修最影响演示的 1 个", "重新测试", "保存最终版"], ["问题描述具体", "修复范围可控", "最终能演示", "有版本记录"], "最终页面 + Bug 修复记录"),
        slide_shell(day, 15, total, "AI 自动化工作流", "把重复任务串起来，而不是每次重新问", compact_table(["场景", "流程", "今天怎么做"], [
            ("学习资料整理", "收集 → 分类 → 摘要 → 复习卡", "输出工作流图和提示顺序"),
            ("项目进度汇总", "任务表 → 风险 → 周报 → 待办", "用 Day 2 材料复用"),
            ("页面迭代", "需求 → 生成 → 测试 → 修复 → 记录", "用 Day 4 页面复用"),
            ("求职准备", "岗位 → 能力差距 → 简历 → 面试话术", "Day 5 会继续使用"),
        ])),
        drill_slide(day, 16, total, "互评：两组互测", ["10 分钟：A 组测 B 组页面", "10 分钟：B 组复现 Bug", "15 分钟：各修 1 个问题", "10 分钟：复测并签字"], ["只找可复现问题", "不评价审美偏好", "要求写清操作步骤"], ["测试对方页面", "提交 Bug", "复测"], ["互测记录"], ["Bug 可复现", "修复有效", "记录完整"]),
        troubleshooting_slide(day, 17, total, "课堂控场", [("学生沉迷美化", "产品目标偏移", "先功能后视觉，最后 20 分钟才允许改样式"), ("学生害怕代码", "角色理解错", "告诉学生今天是需求描述和测试，不是背代码"), ("全班工具效果不同", "AI 生成不稳定", "把差异当作测试和迭代素材")]),
        slide_shell(day, 18, total, "今日提交物", "Day 4 下课交 4 件", three_col([
            card("需求说明书", ul(["用户", "场景", "输入", "输出"]), "success"),
            card("可运行页面", ul(["活动页或评分器", "单文件", "能演示"]), "success"),
            card("Bug 记录", ul(["现象", "提示词", "修复", "复测"]), "success"),
        ])),
        summary_slide(day, 19, total, ["会把想法写成产品需求", "会用 Trae 生成可运行页面", "会按标准流程 Debug", "理解自动化工作流的输入输出"], "Day 5 进入 Agentic Engineering：把个人作品升级成小组综合项目，并完成展示与就业转化。"),
        slide_shell(day, 20, total, "讲师备课页", "Day 4 上课前准备", two_col(
            card("材料", ul(["Day 3 作品", "评分器需求", "故障页面", "测试模板", "Bug 记录表"]), "primary"),
            card("环境", ul(["Trae 可用", "浏览器控制台演示", "学生知道保存 v1/v2", "准备备用 HTML 示例"]), "accent"),
        )),
    ]
    return "Vibe Coding 产品实战", slides


def _day5_final():
    day, total = 5, 22
    slides = [
        cover(day, total, "Agentic Engineering 综合收口", "用 AI 协作完成项目、沉淀知识、包装求职表达", ["综合项目", "LLM-Wiki", "就业锦囊"]),
        schedule_slide(day, 2, total, [
            ("08:30-09:50", "理论：从 Vibe Coding 到 Agentic Engineering，目标、角色、工具、验收"),
            ("10:05-11:25", "案例 10：小组综合项目规划，AI 学习/求职/活动助手三选一"),
            ("13:00-14:20", "项目冲刺 + LLM-Wiki，资料、页面、测试、知识卡并行"),
            ("14:35-15:55", "路演、简历项目经历、就业锦囊和课程复盘"),
        ], ["Agentic 工作流图", "综合项目 Demo", "LLM-Wiki 知识卡", "简历项目经历"]),
        agentic_battle_map_slide(day, 3, total),
        slide_shell(day, 4, total, "理论导入", "Agentic Engineering 的五个控制点", compact_table(["控制点", "解释", "课堂例子"], [
            ("Goal", "目标清楚", "做一个能演示的 AI 求职助手，不做完整平台"),
            ("Context", "上下文足够", "岗位资料、学生经历、页面需求、限制条件"),
            ("Role", "角色分工", "Planner、Builder、Tester、Speaker"),
            ("Trace", "过程留痕", "提示词、版本、Bug、截图、修改原因"),
            ("Eval", "验收标准", "能打开、主流程能跑、内容有依据、能讲清楚"),
        ])),
        theory_lab_slide(day, 5, total, "课堂示例：为什么综合项目不能只靠一句提示词", ["综合项目包含资料、内容、页面、测试、展示", "一个 AI 回答无法同时保证所有环节正确", "Agentic 的价值是分工、交接和验收", "人的角色是项目负责人，不是旁观者"], ["把“做一个求职助手”拆成 5 步", "演示 Builder/Tester/Reviewer 三个角色", "展示每一步的输入输出"], ["小组给自己的项目分配角色", "写出每个角色的交付物"], ["Agentic 工作流图"]),
        runbook_slide(day, 6, total, 10, "综合项目规划", "QClaw + WorkBuddy + Trae + 文档 AI", ["准备项目模板", "三选一：AI 求职助手、学习资料整理助手、校园活动助手", "统一不做登录、后端、真实 API"], ["选题并砍范围", "用 QClaw 搜集资料", "用 WorkBuddy 整理字段", "用 Trae 生成 Demo", "设置 Tester 找 Bug"], ["选题", "分角色", "搜集资料", "生成 Demo", "测试并记录"], "我们要在 1 天内完成【项目】MVP。请输出工作流表：步骤、负责角色、使用工具、输入、输出、验收标准、风险。限制：不做后端、不接真实 API、必须能课堂演示。", [("项目过大", "砍到单页 MVP"), ("角色重叠", "明确 Planner/Builder/Tester/Speaker"), ("没有验收", "每一步写可检查标准")]),
        project_board(day, 7, total, "小组角色", [("Planner", ["定义目标", "拆步骤", "控范围"], "primary"), ("Builder", ["生成页面", "整合内容", "保存版本"], "accent"), ("Tester", ["写测试", "找 Bug", "复测"], "success"), ("Speaker", ["写路演", "讲价值", "答问题"], "primary")]),
        practice_slide(day, 8, total, "项目规划实操", ["确定项目", "写目标和受众", "拆 5 步", "分配 4 个角色", "写验收标准"], ["范围可完成", "角色不重叠", "每步有输出", "风险明确"], "Agentic 工作流图"),
        troubleshooting_slide(day, 9, total, "项目规划翻车点", [("想做万能平台", "范围幻想", "限定 1 个用户、1 个场景、1 条主流程"), ("没有数据", "内容空洞", "先用 QClaw 搜集或用课堂模拟数据"), ("没人负责测试", "测试被低估", "强制每组设置 Tester")]),
        runbook_slide(day, 10, total, 11, "综合项目冲刺", "全工具协同", ["准备项目目录", "准备提示词记录表", "准备演示评分表"], ["示范目录结构", "资料线和 Demo 线并行", "每 30 分钟检查一次产出", "把问题写入风险表", "准备备用截图"], ["按角色并行", "每 30 分钟交中间产物", "合并到 Demo", "测试主流程"], "请根据资料和工作流，生成项目 Demo 的页面结构和核心交互。先保证主流程能演示，再考虑视觉优化。输出后请同时给测试清单。", [("每个人都生成一版", "指定 Builder 合并"), ("内容没来源", "资料线必须保留来源"), ("Demo 演示不通", "只保留一条主流程")]),
        project_board(day, 11, total, "四线并行工作台", [("资料线", ["搜集", "来源", "筛选", "摘要"], "primary"), ("Demo线", ["结构", "代码", "交互", "版本"], "accent"), ("测试线", ["用例", "Bug", "复测", "备用"], "success"), ("展示线", ["PPT", "脚本", "分工", "问答"], "primary")]),
        practice_slide(day, 12, total, "冲刺 I：先跑通", ["资料线完成 5 条材料", "Demo 线生成页面", "测试线跑 5 条用例", "展示线写 5 页结构"], ["页面能打开", "内容不空", "主按钮可用", "有 Bug 清单"], "Demo 初版 + 测试清单"),
        slide_shell(day, 13, total, "LLM-Wiki 知识管理", "把课程成果沉淀成以后能复用的知识卡", compact_table(["问题", "普通文件夹", "LLM-Wiki 思路"], [
            ("资料散", "文件到处放", "按主题和项目组织知识"),
            ("经验丢", "做完就忘", "把提示词、Bug、验收标准写成卡片"),
            ("复用难", "下次重新问", "把可复用流程沉淀为模板"),
            ("判断弱", "只保存结果", "同时保存为什么这样改"),
        ])),
        runbook_slide(day, 14, total, 12, "LLM-Wiki 个人知识卡", "本地 LLM-WIKI / Markdown / 文档 AI", ["准备知识卡模板", "字段：主题、问题、做法、证据、下次复用", "要求每人沉淀 1 张卡"], ["展示 LLM-Wiki 的用途", "把一个 Bug 修复记录变成知识卡", "把一个提示词原则变成知识卡", "说明链接关系"], ["选择一个今天的问题", "写知识卡", "链接到项目", "写下次复用场景"], "请把下面项目经历整理成一张知识卡：主题、遇到的问题、我怎么判断、AI 帮了什么、人做了什么决定、下次如何复用。", [("写成日记", "改成问题-做法-复用"), ("只写结果", "补过程和证据"), ("没有链接", "链接到项目、Bug 或提示词原则")]),
        practice_slide(day, 15, total, "学生实操：写一张 LLM-Wiki 知识卡", ["选择项目中的一个问题", "写主题和问题", "写 AI 帮了什么", "写人做了什么决定", "写下次如何复用"], ["不是流水账", "有判断过程", "有复用场景", "能链接到项目"], "个人知识卡"),
        slide_shell(day, 16, total, "路演结构", "5 页足够讲清一个学生项目", compact_table(["页", "内容", "一句话目标"], [
            ("1", "问题和用户", "让评委知道为什么做"),
            ("2", "AI 工作流", "说明怎么用 AI 协作"),
            ("3", "Demo 展示", "证明能跑"),
            ("4", "测试和迭代", "证明不是一次生成"),
            ("5", "分工和反思", "证明每个人有收获"),
        ])),
        practice_slide(day, 17, total, "冲刺 II：路演和备用方案", ["修最严重的 2 个 Bug", "补充说明文档", "生成路演稿", "准备备用截图", "每人写贡献"], ["主流程稳定", "路演不超时", "每人有贡献", "有备用方案"], "Demo v2 + 路演初稿"),
        slide_shell(day, 18, total, "简历项目经历", "把课程成果写成就业材料，但不能造假", compact_table(["维度", "不要这样写", "建议写法"], [
            ("项目背景", "参加了 AI 课程", "面向校园活动报名场景，完成 AI 辅助活动页 Demo"),
            ("工具", "用了很多 AI", "使用文档 AI 整理需求，Trae 生成页面，人工完成测试和迭代"),
            ("贡献", "我参与开发", "负责需求拆解、Bug 复现、页面测试和路演讲解"),
            ("结果", "效果很好", "交付单文件 HTML Demo、测试清单和 5 页路演稿"),
        ])),
        practice_slide(day, 19, total, "学生实操：个人简历项目经历", ["选择自己真实负责的部分", "写项目背景", "写工具和方法", "写个人贡献", "删掉夸大词"], ["不造假", "能说清自己做了什么", "有作品和证据", "适合面试复述"], "简历项目经历 + 1 分钟介绍"),
        drill_slide(day, 20, total, "正式路演", ["每组 3 分钟展示", "1 分钟问答", "评委按标准打分", "每组记录 2 条改进建议"], ["严格计时", "优先看 Demo 和证据", "不只评价好不好看"], ["展示 Demo", "说明 AI 工作流", "回答问题"], ["最终 Demo + PPT"], ["能运行", "能讲清", "有证据"]),
        slide_shell(day, 21, total, "最终验收", "Day 5 下课前必须留下这些资产", compact_table(["类别", "必须提交", "合格标准", "以后怎么用"], [
            ("作品", "可运行 Demo", "能打开，主流程能跑，核心按钮有反馈", "作品集、路演、面试展示"),
            ("作品", "截图/录屏备用", "现场断网或打不开时仍能展示", "答辩备用材料"),
            ("展示", "5 页 PPT", "问题、工作流、Demo、测试、分工都讲清", "项目路演模板"),
            ("工程证据", "Agentic 工作流图", "每一步有角色、工具、输入、输出、验收", "证明不是一次性生成"),
            ("工程证据", "测试清单 + Bug 记录", "至少 5 条测试，至少 2 个修复记录", "证明会测试和迭代"),
            ("知识沉淀", "LLM-Wiki 知识卡", "写清问题、判断、AI 帮助、人类决策、复用场景", "以后学习和复盘"),
            ("就业", "简历项目经历", "不造假，写清工具、贡献、结果和证据", "简历和面试"),
            ("就业", "1 分钟项目介绍", "能说清我负责什么、解决什么、学到什么", "面试自我表达"),
        ])),
        summary_slide(day, 22, total, ["完成综合项目 Demo 和路演", "理解 Agentic Engineering 的协作方式", "沉淀 LLM-Wiki 知识卡", "把项目转成简历和面试表达"], "课程结束后继续做三件事：持续学习、动手实践、提升审美和业务判断。"),
    ]
    return "Agentic Engineering 综合收口", slides


build_day_2 = _day2_final
build_day_3 = _day3_final
build_day_4 = _day4_final
build_day_5 = _day5_final


def write_nav():
    days = [
        ("01", "AI 使用底层能力", "AI 圈变化、环境搭建、判断、提问、验证", ["AI 变化", "环境安装", "事实核查"], "25 页"),
        ("02", "AI 办公自动化", "会议纪要、数据洞察、任务调度、正式报告", ["纪要", "数据", "报告"], "20 页"),
        ("03", "AI 内容创作 + Vibe Design", "内容策略、视觉风格、海报/首屏、PPT 故事板", ["内容策略", "视觉风格", "PPT"], "20 页"),
        ("04", "Vibe Coding 产品实战", "需求表达、AI 编程、Debug、自动化工作流", ["需求", "页面", "修 Bug"], "20 页"),
        ("05", "Agentic Engineering 综合收口", "综合项目、LLM-Wiki、路演、简历与就业表达", ["工作流", "LLM-Wiki", "就业"], "22 页"),
    ]
    cards = []
    for no, title, sub, tags, count in days:
        cards.append(f"""
  <a class="day-card" href="day{no}/index.html" target="_blank">
    <div class="day-header"><div class="day-badge">{no}</div><div><div class="day-title">{escape(title)}</div><div class="day-subtitle">{escape(sub)}</div></div></div>
    <div class="day-topics">{''.join(f'<span class="topic-tag">{escape(t)}</span>' for t in tags)}</div>
    <div class="day-meta"><span>{count}</span><span>打开课件</span></div>
  </a>""")
    nav = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>AI 工具实战训练营 · 课件导航</title>
<style>*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:"Microsoft YaHei","PingFang SC",sans-serif;background:linear-gradient(135deg,#f5f8fb,#eaf2f8);min-height:100vh;padding:40px}}.header{{text-align:center;margin-bottom:32px}}.header h1{{font-size:36px;color:#073f73;margin-bottom:8px}}.header p{{font-size:16px;color:#4b6175}}.stats{{display:flex;justify-content:center;gap:20px;margin-bottom:32px;flex-wrap:wrap}}.stat-item{{text-align:center;background:#fff;border:1px solid #dce8f2;border-radius:10px;padding:14px 22px;box-shadow:0 10px 30px rgba(8,78,143,.08)}}.num{{font-size:28px;font-weight:800;color:#084e8f}}.label{{font-size:13px;color:#666;margin-top:4px}}.days-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:20px;max-width:1200px;margin:0 auto}}.day-card{{background:#fff;border:1px solid #dce8f2;border-radius:14px;padding:24px;text-decoration:none;color:inherit;display:block;transition:.2s;box-shadow:0 12px 32px rgba(8,78,143,.06)}}.day-card:hover{{box-shadow:0 16px 38px rgba(8,78,143,.14);transform:translateY(-3px);border-color:#084e8f}}.day-header{{display:flex;align-items:center;gap:12px;margin-bottom:12px}}.day-badge{{width:52px;height:52px;border-radius:12px;background:#084e8f;color:#fff;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;flex-shrink:0}}.day-title{{font-size:18px;font-weight:800;color:#073f73}}.day-subtitle{{font-size:13px;color:#60758a;margin-top:2px}}.day-topics{{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}}.topic-tag{{font-size:12px;color:#084e8f;background:rgba(8,78,143,.07);padding:4px 10px;border-radius:999px}}.day-meta{{display:flex;justify-content:space-between;margin-top:16px;padding-top:12px;border-top:1px solid #edf3f7;font-size:12px;color:#789}}.footer{{text-align:center;margin-top:44px;font-size:13px;color:#789}}</style></head>
<body><div class="header"><h1>AI 工具实战训练营</h1><p>理论讲透一点，实践做深一点，作品留下来</p></div>
<div class="stats"><div class="stat-item"><div class="num">5</div><div class="label">学习天数</div></div><div class="stat-item"><div class="num">12</div><div class="label">课堂案例/任务</div></div><div class="stat-item"><div class="num">107</div><div class="label">课件页数</div></div><div class="stat-item"><div class="num">1</div><div class="label">综合项目</div></div></div>
<div class="days-grid">{''.join(cards)}</div><div class="footer"><p>理论小于实践，但理论必须服务每一次操作 · 每半天都有可检查产出</p></div></body></html>"""
    (SLIDES / "index.html").write_text(nav, encoding="utf-8")


def main():
    builders = [build_day_1, build_day_2, build_day_3, build_day_4, build_day_5]
    for i, builder in enumerate(builders, start=1):
        title, slides = builder()
        write_deck(i, title, slides)
    write_nav()


if __name__ == "__main__":
    main()
