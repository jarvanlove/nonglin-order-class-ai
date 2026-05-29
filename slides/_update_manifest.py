import re

manifest = [
  # Day 1
  { "file": "day01/day01-01-cover.html", "label": "Day 1 · 封面", "notes": "欢迎学员，介绍课程整体安排与讲师背景。" },
  { "file": "day01/day01-02-objectives.html", "label": "Day 1 · 学习目标", "notes": "明确今日学习目标：理解 AI 全景图，掌握 QClaw 基础操作。" },
  { "file": "day01/day01-03-intro.html", "label": "Day 1 · 课程导入", "notes": "通过实际案例引入 AI 工具在农林场景的应用价值。" },
  { "file": "day01/day01-04-history.html", "label": "Day 1 · AI 发展历程", "notes": "简述 AI 发展三波浪潮，重点突出大模型时代的转折点。" },
  { "file": "day01/day01-05-agent-def.html", "label": "Day 1 · 什么是 AI Agent", "notes": "定义 Agent：感知-决策-执行闭环，区别于传统软件。" },
  { "file": "day01/day01-06-agent-4factors.html", "label": "Day 1 · Agent 四要素", "notes": "四要素：模型、工具、记忆、规划。可结合图示讲解。" },
  { "file": "day01/day01-07-tools-global.html", "label": "Day 1 · 全球 AI 工具地图", "notes": "展示全球主流 AI 工具矩阵，ChatGPT、Claude、Gemini 等定位。" },
  { "file": "day01/day01-08-tools-china.html", "label": "Day 1 · 国产 AI 工具生态", "notes": "国产工具全景：文心、通义、讯飞、智谱等，强调自主可控。" },
  { "file": "day01/day01-09-why-domestic.html", "label": "Day 1 · 为什么要学国产工具", "notes": "数据安全、行业适配、政策导向三个维度论证。" },
  { "file": "day01/day01-10-qclaw-intro.html", "label": "Day 1 · QClaw 介绍", "notes": "QClaw 产品定位：面向农林行业的 AI 智能体平台。" },
  { "file": "day01/day01-11-qclaw-install.html", "label": "Day 1 · QClaw 安装与配置", "notes": "现场演示安装流程，注意常见环境问题的排查。" },
  { "file": "day01/day01-12-qclaw-demo.html", "label": "Day 1 · QClaw 实战演示", "notes": "用一个简单的病虫害识别任务演示完整工作流。" },
  { "file": "day01/day01-13-workbuddy-intro.html", "label": "Day 1 · WorkBuddy 介绍", "notes": "WorkBuddy 定位：办公自动化助手，对接 Excel/Word。" },
  { "file": "day01/day01-14-trae-intro.html", "label": "Day 1 · Trae 介绍", "notes": "Trae：AI 原生 IDE，强调 Builder Mode 的革命性。" },
  { "file": "day01/day01-15-task.html", "label": "Day 1 · 下午任务", "notes": "布置下午任务：用 QClaw 完成一个指定场景的智能体搭建。" },
  { "file": "day01/day01-16-practice.html", "label": "Day 1 · 课堂实操", "notes": "学员实操时间，讲师巡回指导，记录共性问题。" },
  { "file": "day01/day01-18-summary.html", "label": "Day 1 · 日终总结", "notes": "回顾今日重点，预告 Day 2 内容，收集学员反馈。" },

  # Day 2
  { "file": "day02/day02-01-cover.html", "label": "Day 2 · 封面", "notes": "Day 2 开场：从工具使用迈向 Agent 深度理解。" },
  { "file": "day02/day02-02-objectives.html", "label": "Day 2 · 学习目标", "notes": "今日目标：掌握 OpenClaw 架构，完成 WorkBuddy 办公自动化案例。" },
  { "file": "day02/day02-03-intro.html", "label": "Day 2 · 课程导入", "notes": "回顾 Day 1，引出今日主题：Agent 的「大脑」与「手脚」。" },
  { "file": "day02/day02-04-openclaw-arch.html", "label": "Day 2 · OpenClaw 架构", "notes": "讲解 OpenClaw 分层架构：内核层、技能层、应用层。" },
  { "file": "day02/day02-04b-openclaw-hardware.html", "label": "Day 2 · OpenClaw 硬件配置", "notes": "本地部署 vs 云端部署的硬件差异，GPU 显存要求与替代方案。" },
  { "file": "day02/day02-05-openclaw-skills.html", "label": "Day 2 · OpenClaw Skills", "notes": "Skills 机制：如何扩展 Agent 能力，内置 Skills 一览。" },
  { "file": "day02/day02-06-hermes-intro.html", "label": "Day 2 · Hermes 介绍", "notes": "Hermes：OpenClaw 的调度中枢，负责任务分解与执行。" },
  { "file": "day02/day02-06b-hermes-security.html", "label": "Day 2 · Hermes 安全与隐私", "notes": "自我进化机制的数据存储边界，农林敏感数据的保护要点。" },
  { "file": "day02/day02-07-gepa.html", "label": "Day 2 · GEPA 框架", "notes": "GEPA 框架：Goal-Execution-Plan-Action 循环详解。" },
  { "file": "day02/day02-08-agent-compare.html", "label": "Day 2 · Agent 对比", "notes": "对比主流 Agent 框架：AutoGPT、LangChain、OpenClaw 优劣。" },
  { "file": "day02/day02-09-workbuddy-intro.html", "label": "Day 2 · WorkBuddy 深度", "notes": "WorkBuddy 进阶功能：批量处理、模板引擎、定时任务。" },
  { "file": "day02/day02-10-workbuddy-install.html", "label": "Day 2 · WorkBuddy 安装", "notes": "插件安装、账号绑定、权限配置注意事项。" },
  { "file": "day02/day02-11-excel-clean.html", "label": "Day 2 · Excel 数据清洗", "notes": "演示：用 WorkBuddy 自动清洗农林实验数据表格。" },
  { "file": "day02/day02-12-report-auto.html", "label": "Day 2 · 报告自动化", "notes": "演示：从数据到 Word 报告的全自动流水线。" },
  { "file": "day02/day02-13-weekly-report.html", "label": "Day 2 · 周报生成", "notes": "学员跟随演示，生成自己的第一份 AI 辅助周报。" },
  { "file": "day02/day02-14-task.html", "label": "Day 2 · 下午任务", "notes": "任务：用 WorkBuddy 完成一份指定格式的数据分析报告。" },
  { "file": "day02/day02-15-practice.html", "label": "Day 2 · 课堂实操", "notes": "学员实操，重点辅导数据清洗环节的公式调试。" },
  { "file": "day02/day02-18-summary.html", "label": "Day 2 · 日终总结", "notes": "总结 Agent 核心概念，强调动手实践的重要性。" },

  # Day 3
  { "file": "day03/day03-01-cover.html", "label": "Day 3 · 封面", "notes": "Day 3：进入编程工具世界，项目正式启动。" },
  { "file": "day03/day03-02-objectives.html", "label": "Day 3 · 学习目标", "notes": "目标：掌握 Trae 核心功能，完成项目选题与组队。" },
  { "file": "day03/day03-03-intro.html", "label": "Day 3 · 课程导入", "notes": "从办公自动化到编程开发，工具能力的跃迁。" },
  { "file": "day03/day03-04-ide-history.html", "label": "Day 3 · IDE 发展历程", "notes": "IDE 演进：从文本编辑器到 AI 原生开发环境。" },
  { "file": "day03/day03-05-ide-landscape.html", "label": "Day 3 · IDE 格局", "notes": "当前 IDE 格局：VS Code、Cursor、Trae、Windsurf 对比。" },
  { "file": "day03/day03-06-trae-intro.html", "label": "Day 3 · Trae 深度介绍", "notes": "Trae 核心卖点：Builder Mode、多模型支持、中文优化。" },
  { "file": "day03/day03-07-builder-mode.html", "label": "Day 3 · Builder Mode", "notes": "Builder Mode 原理：自然语言到完整项目的生成机制。" },
  { "file": "day03/day03-08-builder-demo.html", "label": "Day 3 · Builder 演示", "notes": "现场演示：用一句话描述生成一个完整的 Web 页面。" },
  { "file": "day03/day03-09-trae-install.html", "label": "Day 3 · Trae 安装", "notes": "Trae 安装指南，Mac/Windows 差异点提示。" },
  { "file": "day03/day03-10-first-project.html", "label": "Day 3 · 首个项目", "notes": "学员跟随创建第一个 Trae 项目，熟悉界面布局。" },
  { "file": "day03/day03-11-project-overview.html", "label": "Day 3 · 项目概览", "notes": "介绍实训周项目要求：6 天完成一个 AI 工具应用原型。" },
  { "file": "day03/day03-12-project-topics.html", "label": "Day 3 · 项目选题", "notes": "选题库展示：农林数据分析、智能问答、文档生成等方向。" },
  { "file": "day03/day03-13-team-forming.html", "label": "Day 3 · 团队组建", "notes": "组队规则：5 人一组，每人独立使用 AI 工具产出，最后合并展示。" },
  { "file": "day03/day03-14-requirements.html", "label": "Day 3 · 需求分析", "notes": "需求分析模板：用户故事、功能清单、技术约束。" },
  { "file": "day03/day03-15-tech-plan.html", "label": "Day 3 · 技术方案", "notes": "技术方案框架：工具选型、架构草图、里程碑规划。" },
  { "file": "day03/day03-16-task.html", "label": "Day 3 · 下午任务", "notes": "任务：完成项目选题、组队、需求文档初稿。" },
  { "file": "day03/day03-17-practice.html", "label": "Day 3 · 课堂实操", "notes": "各组讨论选题，讲师逐一确认可行性。" },
  { "file": "day03/day03-20-summary.html", "label": "Day 3 · 日终总结", "notes": "确认各组项目方向，强调版本控制的重要性。" },

  # Day 4
  { "file": "day04/day04-01-cover.html", "label": "Day 4 · 封面", "notes": "Day 4：项目冲刺第一天，聚焦核心功能开发。" },
  { "file": "day04/day04-02-objectives.html", "label": "Day 4 · 学习目标", "notes": "目标：完成项目 MVP 的核心功能模块。" },
  { "file": "day04/day04-03-intro.html", "label": "Day 4 · 课程导入", "notes": "敏捷开发节奏：站会-开发-评审的日循环。" },
  { "file": "day04/day04-04-standup.html", "label": "Day 4 · 每日站会", "notes": "站会模板：昨天做了什么、今天计划、遇到什么阻塞。" },
  { "file": "day04/day04-05-qclaw-advanced.html", "label": "Day 4 · QClaw 进阶", "notes": "进阶技巧：自定义知识库、多轮对话优化、错误处理。" },
  { "file": "day04/day04-06-workbuddy-advanced.html", "label": "Day 4 · WorkBuddy 进阶", "notes": "进阶：API 对接、批量任务调度、异常数据告警。" },
  { "file": "day04/day04-07-mvp.html", "label": "Day 4 · MVP 标准", "notes": "MVP 定义：能跑通核心流程的最小可用版本。" },
  { "file": "day04/day04-08-integration.html", "label": "Day 4 · 三工具联调", "notes": "联调策略：QClaw 负责智能，WorkBuddy 负责数据，Trae 负责实现。" },
  { "file": "day04/day04-09-debug.html", "label": "Day 4 · 联调排错", "notes": "常见联调问题：接口格式、编码问题、权限配置。" },
  { "file": "day04/day04-10-task.html", "label": "Day 4 · 下午任务", "notes": "任务：各组完成 MVP 第一个可演示版本。" },
  { "file": "day04/day04-11-practice.html", "label": "Day 4 · 课堂实操", "notes": "开发时间，讲师作为技术顾问巡回支持。" },
  { "file": "day04/day04-12-extension.html", "label": "Day 4 · 任务拓展", "notes": "拓展：为项目添加一个简单的数据可视化模块。" },
  { "file": "day04/day04-14-summary.html", "label": "Day 4 · 日终总结", "notes": "各组演示 MVP 进展，互相点评。" },

  # Day 5
  { "file": "day05/day05-01-cover.html", "label": "Day 5 · 封面", "notes": "Day 5：项目冲刺第二天，完善功能与质量保障。" },
  { "file": "day05/day05-02-objectives.html", "label": "Day 5 · 学习目标", "notes": "目标：项目功能完善，引入测试与调试。" },
  { "file": "day05/day05-03-intro.html", "label": "Day 5 · 课程导入", "notes": "软件开发完成度：从「能跑」到「好用」的跨越。" },
  { "file": "day05/day05-04-trae-advanced.html", "label": "Day 5 · Trae 进阶", "notes": "Trae 进阶：代码重构、性能分析、Git 集成。" },
  { "file": "day05/day05-05-api-intro.html", "label": "Day 5 · API 介绍", "notes": "API 设计基础：RESTful 规范、文档生成、Postman 测试。" },
  { "file": "day05/day05-06-api-practice.html", "label": "Day 5 · API 实践", "notes": "实践：为项目封装一个可调用的 API 接口。" },
  { "file": "day05/day05-07-debug.html", "label": "Day 5 · 调试技巧", "notes": "调试方法论：日志、断点、二分法定位问题。" },
  { "file": "day05/day05-08-full-integration.html", "label": "Day 5 · 完整联调", "notes": "端到端测试：从用户输入到结果输出的全链路验证。" },
  { "file": "day05/day05-09-testing.html", "label": "Day 5 · 测试方法", "notes": "测试金字塔：单元测试、集成测试、用户验收测试。" },
  { "file": "day05/day05-10-task.html", "label": "Day 5 · 下午任务", "notes": "任务：完成项目主要功能，准备初步演示。" },
  { "file": "day05/day05-11-practice.html", "label": "Day 5 · 课堂实操", "notes": "开发时间，重点支持 API 调试和异常处理。" },
  { "file": "day05/day05-12-extension.html", "label": "Day 5 · 任务拓展", "notes": "拓展：为项目添加用户登录或权限管理功能。" },
  { "file": "day05/day05-14-summary.html", "label": "Day 5 · 日终总结", "notes": "检查各组项目完成度，预告 Day 6 打磨日。" },

  # Day 6
  { "file": "day06/day06-01-cover.html", "label": "Day 6 · 封面", "notes": "Day 6：项目打磨日，从作品到产品的最后一步。" },
  { "file": "day06/day06-02-objectives.html", "label": "Day 6 · 学习目标", "notes": "目标：项目 UI 优化、演示准备、就业技能储备。" },
  { "file": "day06/day06-03-intro.html", "label": "Day 6 · 课程导入", "notes": "打磨的意义：细节决定专业度，演示决定影响力。" },
  { "file": "day06/day06-04-polish.html", "label": "Day 6 · 项目打磨", "notes": "打磨清单：UI 统一、错误处理、加载优化、边界情况。" },
  { "file": "day06/day06-05-demo-prep.html", "label": "Day 6 · 演示准备", "notes": "演示技巧：黄金 3 分钟、故事线、备选方案。" },
  { "file": "day06/day06-06-roadmap.html", "label": "Day 6 · 路演 PPT 制作", "notes": "路演 PPT 结构与制作要点，农林场景演示案例。" },
  { "file": "day06/day06-07-rubric.html", "label": "Day 6 · 评分标准详解", "notes": "评分维度：创新性(30%)、完成度(30%)、演示效果(20%)、团队协作(20%)。" },
  { "file": "day06/day06-07-resume-intro.html", "label": "Day 6 · 简历介绍", "notes": "AI 时代简历新范式：项目驱动、工具熟练度、成果量化。" },
  { "file": "day06/day06-08-resume-before-after.html", "label": "Day 6 · 简历对比", "notes": "对比案例：传统简历 vs AI 工具优化后的简历。" },
  { "file": "day06/day06-09-ai-resume.html", "label": "Day 6 · AI 简历优化", "notes": "现场演示：用 AI 工具分析和优化一份真实简历。" },
  { "file": "day06/day06-10-safety.html", "label": "Day 6 · 安全规范", "notes": "AI 工具使用安全：数据隐私、提示词泄露、合规边界。" },
  { "file": "day06/day06-11-safety-cases.html", "label": "Day 6 · 安全案例", "notes": "真实案例：企业数据泄露事件与防范措施。" },
  { "file": "day06/day06-12-km-problem.html", "label": "Day 6 · 知识管理痛点", "notes": "常见痛点：信息过载、笔记散落、检索困难。" },
  { "file": "day06/day06-13-llm-wiki.html", "label": "Day 6 · LLM-Wiki", "notes": "LLM-Wiki 理念：用 AI 构建第二大脑，自然语言检索。" },
  { "file": "day06/day06-14-km-practice.html", "label": "Day 6 · 知识管理实践", "notes": "实践：将本周学习笔记整理为结构化的 Wiki 知识库。" },
  { "file": "day06/day06-12-task.html", "label": "Day 6 · 下午任务", "notes": "任务：项目最终打磨 + 路演 PPT 制作。" },
  { "file": "day06/day06-13-practice.html", "label": "Day 6 · 课堂实操", "notes": "各组进行内部路演彩排，互相提改进建议。" },
  { "file": "day06/day06-14-extension.html", "label": "Day 6 · 任务拓展", "notes": "拓展：尝试将项目部署到公网或生成可执行文件。" },
  { "file": "day06/day06-17-ceremony.html", "label": "Day 6 · 结业仪式", "notes": "评选颁奖、结业证书、合影留念、纪念品发放。" },
  { "file": "day06/day06-18-feedback.html", "label": "Day 6 · 课程反馈", "notes": "收集学员反馈，用于下一期课程优化。" },
  { "file": "day06/day06-19-resources.html", "label": "Day 6 · 课后资源", "notes": "资源包：课程录像、代码仓库、扩展阅读清单、社区入口。" },
  { "file": "day06/day06-20-summary.html", "label": "Day 6 · 日终总结", "notes": "6 天学习全景回顾，关键知识点串联。" },
]

# Read current index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Build new manifest string
lines = ["window.DECK_MANIFEST = ["]
for i, item in enumerate(manifest):
    comma = "," if i < len(manifest) - 1 else ""
    lines.append(f'  {{ file: "{item["file"]}", label: "{item["label"]}", notes: "{item["notes"]}" }}{comma}')
lines.append("];")
new_manifest_str = "\n".join(lines)

# Replace old manifest
pattern = r'window\.DECK_MANIFEST = \[.*?\];'
new_content = re.sub(pattern, new_manifest_str, content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Updated manifest: {len(manifest)} slides total.")
print("Day 1:", sum(1 for s in manifest if s["file"].startswith("day01/")))
print("Day 2:", sum(1 for s in manifest if s["file"].startswith("day02/")))
print("Day 3:", sum(1 for s in manifest if s["file"].startswith("day03/")))
print("Day 4:", sum(1 for s in manifest if s["file"].startswith("day04/")))
print("Day 5:", sum(1 for s in manifest if s["file"].startswith("day05/")))
print("Day 6:", sum(1 for s in manifest if s["file"].startswith("day06/")))
