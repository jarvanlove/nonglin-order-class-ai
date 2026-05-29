# Day 2 slide data - Python format to avoid JSON quote issues

day_num = 2
day_title = "Agent 深度 + WorkBuddy 办公自动化"
subtitle = "OpenClaw 架构 · Hermes GEPA · Excel 清洗 · 报告自动化 · 项目启动"
output = "slides/day02/index.html"

slides = [
    {"type": "cover"},
    {
        "type": "objectives",
        "knowledge": [
            "理解 OpenClaw 三层架构（核心层、技能层、接入层）",
            "理解 Hermes Agent 的 GEPA 进化机制",
            "掌握 WorkBuddy 的 Craft 模式与核心功能",
            "理解 Excel 数据清洗的常见问题与 AI 解决方案"
        ],
        "skills": [
            "能安装配置 WorkBuddy 并完成首次运行",
            "能用 WorkBuddy 完成 Excel 数据清洗实战",
            "能用 WorkBuddy 自动生成结构化报告",
            "能完成项目分组、选题和技术方案初稿"
        ],
        "literacy": [
            "建立模块化思维——复杂系统由可插拔组件构成",
            "理解开源社区的价值和参与方式",
            "培养团队协作中的角色分工意识"
        ]
    },
    {
        "type": "intro",
        "question": "昨天你学会了用 QClaw 搜集信息。但如果搜集到的信息是混乱的 Excel 表格、格式不统一的报告，你该怎么办？",
        "subtitle": "信息搜集只是第一步，真正的价值在于把 raw data 变成 actionable insight。今天我们要学习如何把混乱的数据变成漂亮的报告。",
        "cards": [
            {"title": "Day 1：信息搜集", "text": "QClaw 帮你快速获取大量信息，但信息往往是 raw 的、混乱的。", "tag": "QClaw · 信息获取", "tag_class": "tag-primary"},
            {"title": "Day 2：数据处理", "text": "WorkBuddy 帮你清洗、整理、分析数据，并自动生成报告。", "tag": "WorkBuddy · 数据处理", "tag_class": "tag-accent"},
            {"title": "Day 3-5：展示开发", "text": "Trae 把处理好的数据变成可交互的网页或应用。", "tag": "Trae · 展示开发", "tag_class": "tag-success"}
        ]
    },
    {
        "type": "content",
        "section": "知识储备",
        "kicker": "核心概念",
        "title": "OpenClaw：模块化的 Agent 操作系统",
        "left": [
            {"title": "什么是 OpenClaw？", "text": "OpenClaw 是全球最受欢迎的开源 AI Agent 平台，开发者社区超过 33 万星标。它的核心理念是开放和模块化——像乐高积木一样，你可以自由组合功能模块。", "items": []},
            {"title": "三层架构", "items": [
                "核心层：对话管理、任务调度、记忆存储（大脑）",
                "技能层（Skills）：可插拔功能模块，如搜索、文件处理、微信推送",
                "接入层：支持微信、网页、API 多渠道接入"
            ]}
        ],
        "right": [
            {"title": "Skills 生态", "text": "ClawHub 官方 Skills 市场提供上百个现成技能：", "items": [
                "搜索技能：让 Agent 能上网查资料",
                "文件处理技能：读取、写入、整理文件",
                "微信推送技能：把结果自动发到微信群",
                "数据库技能：连接 MySQL、PostgreSQL"
            ]},
            {"type": "hint", "title": "关键洞察", "text": "OpenClaw 像乐高底板 + 积木块。有人搭自动客服，有人搭数据分析师，底层都是同一个 OpenClaw。", "variant": "success"}
        ]
    },
    {
        "type": "content",
        "section": "知识储备",
        "kicker": "核心概念",
        "title": "Hermes Agent：会进化的智能体",
        "left": [
            {"title": "GEPA 进化循环", "text": "Hermes Agent 的核心机制是 GEPA——一个持续自我进化的循环：", "items": [
                "G（Goal）：设定目标，明确任务方向",
                "E（Evolve）：根据反馈进化策略",
                "P（Perform）：执行行动，产生结果",
                "A（Assess）：评估结果，生成反馈"
            ]},
            {"type": "hint", "title": "通俗理解", "text": "GEPA 就像一个学生：定目标→学习→考试→复盘→再学习。每循环一次，能力就提升一点。", "variant": ""}
        ],
        "right": [
            {"title": "OpenClaw vs Hermes 对比", "type": "table", "headers": ["维度", "OpenClaw", "Hermes"], "rows": [
                ["定位", "开源 Agent 平台", "企业级 Agent 框架"],
                ["核心优势", "Skills 模块化生态", "GEPA 自进化机制"],
                ["适用场景", "个人/小型团队", "中大型企业"],
                ["学习曲线", "中等（需了解 Skills）", "较陡（需理解 GEPA）"],
                ["部署方式", "本地/云端", " mainly 云端"]
            ]},
            {"type": "hint", "title": "课程选择", "text": "本课程使用 WorkBuddy（基于 Hermes），因为它对办公自动化场景最友好，零基础也能快速上手。", "variant": "success"}
        ]
    },
    {
        "type": "content",
        "section": "知识储备",
        "kicker": "工具入门",
        "title": "WorkBuddy：你的 AI 办公助手",
        "left": [
            {"title": "核心功能", "items": [
                "Craft 模式：用自然语言描述需求，AI 自动执行",
                "Excel 智能清洗：自动识别格式问题、缺失值、重复项",
                "报告自动生成：把数据变成带图表的专业报告",
                "文件批量处理：一次性处理多个文档"
            ]},
            {"title": "适用场景", "items": [
                "月度/季度报表自动化",
                "调研数据清洗与统计分析",
                "合同/文档批量格式转换",
                "会议纪要自动整理"
            ]}
        ],
        "right": [
            {"title": "安装与配置", "items": [
                "Step 1：下载 WorkBuddy 安装包（助教已分发）",
                "Step 2：双击安装，选择个人版",
                "Step 3：用手机号注册/登录",
                "Step 4：完成新手引导（约 3 分钟）"
            ]},
            {"type": "hint", "title": "注意事项", "text": "WorkBuddy 需要联网使用。如果教室网络不稳定，请开启手机热点备用。", "variant": "warning"}
        ]
    },
    {
        "type": "content",
        "section": "知识储备",
        "kicker": "实战技巧",
        "title": "Excel 数据清洗：从混乱到清晰",
        "left": [
            {"title": "常见数据问题", "items": [
                "格式不统一：日期有 2024/1/1 也有 2024-01-01",
                "缺失值：某些单元格为空白或显示 #N/A",
                "重复项：同一行数据出现多次",
                "异常值：温度显示为 999℃ 或 -273℃"
            ]},
            {"title": "传统清洗方式", "text": "手动查找替换 → 写 Excel 公式 → 筛选排序 → 逐个检查。一个 1000 行的表格，传统方式需要 2-3 小时。", "items": []}
        ],
        "right": [
            {"title": "WorkBuddy 清洗方式", "items": [
                "上传 Excel 文件到 WorkBuddy",
                "用自然语言描述问题：请统一日期格式，删除重复行，填充缺失值",
                "AI 自动识别问题并给出清洗方案",
                "一键执行，导出清洗后的文件"
            ]},
            {"type": "hint", "title": "效率对比", "text": "同样的 1000 行表格，WorkBuddy 只需 3-5 分钟，效率提升 30-60 倍。", "variant": "success"}
        ]
    },
    {
        "type": "content",
        "section": "知识储备",
        "kicker": "实战技巧",
        "title": "报告自动化：让 AI 帮你写周报",
        "left": [
            {"title": "报告生成的痛点", "items": [
                "格式固定但内容变化：每周结构一样，数据不同",
                "图表制作费时：Excel 作图 → 粘贴到 PPT → 调整样式",
                "容易遗漏：忘记更新某个数据或图表",
                "多人协作难：版本混乱，不知道谁改了什么"
            ]},
            {"title": "WorkBuddy 解决方案", "text": "Craft 模式支持模板 + 数据的自动化报告生成。你设计一次模板，以后每周只需更新数据。", "items": []}
        ],
        "right": [
            {"title": "实操步骤", "items": [
                "1. 在 WorkBuddy 中创建周报模板",
                "2. 定义固定结构：本周进展、下周计划、风险预警",
                "3. 绑定数据源：Excel 表格或 QClaw 搜集结果",
                "4. 设置自动生成规则：每周一上午 9 点自动发送"
            ]},
            {"type": "prompt", "title": "Prompt 示例", "text": "请根据附件中的销售数据，生成一份周报，包含：1) 本周销售额汇总；2) 环比增长率；3) Top 3 产品；4) 下周建议。用正式商务语气。"}
        ]
    },
    {
        "type": "content",
        "section": "知识储备",
        "kicker": "项目启动",
        "title": "项目分组与选题指南",
        "left": [
            {"title": "分组原则", "items": [
                "4-5 人一组，尽量混合计算机/非计算机背景",
                "每组至少 1 人负责 QClaw 信息搜集",
                "每组至少 1 人负责 WorkBuddy 数据处理",
                "每组至少 1 人负责 Trae 前端展示"
            ]},
            {"title": "选题方向（A/B/C 三类）", "items": [
                "A 类：通用工具型（天气预报、新闻聚合、待办清单）",
                "B 类：数据分析型（销售报表、用户调研、库存管理）",
                "C 类：农林特色型（农产品价格监测、病虫害识别助手）"
            ]}
        ],
        "right": [
            {"title": "技术方案模板", "items": [
                "数据层：QClaw 搜集什么数据？从哪些来源？",
                "处理层：WorkBuddy 如何清洗和分析？",
                "展示层：Trae 生成什么界面？有什么功能？",
                "分工表：谁负责什么？截止日期是什么？"
            ]},
            {"type": "hint", "title": "重要提醒", "text": "MVP 原则：先做一个能跑通的最小版本，再逐步增加功能。不要一上来就想做完美产品。", "variant": "warning"}
        ]
    },
    {
        "type": "task",
        "title": "下午实战任务：WorkBuddy 办公自动化 + 项目启动",
        "steps": [
            {"title": "WorkBuddy 安装与熟悉（30 分钟）", "text": "完成 WorkBuddy 安装，跑通新手引导，熟悉 Craft 模式界面。"},
            {"title": "Excel 清洗实战（45 分钟）", "text": "用提供的农林产品调研数据.xlsx 完成清洗：统一格式、删除重复、填充缺失、筛选异常。"},
            {"title": "报告生成实战（45 分钟）", "text": "基于清洗后的数据，用 Craft 模式生成一份农产品调研分析报告。"},
            {"title": "项目启动会（30 分钟）", "text": "分组讨论，确定选题，填写项目任务书和技术方案初稿。"}
        ],
        "deliverables": [
            "WorkBuddy 安装完成截图",
            "清洗后的 Excel 文件",
            "自动生成的调研报告（PDF 或 Word）",
            "项目任务书（含分工表和技术方案）"
        ],
        "standards": [
            "Excel 清洗：格式统一率 ≥90%，无重复项，缺失值处理合理",
            "报告质量：结构完整（背景/数据/结论/建议），图表清晰",
            "项目方案：分工明确，技术路线可行，MVP 边界清晰"
        ]
    },
    {
        "type": "practice",
        "title": "WorkBuddy Excel 清洗分步指导",
        "steps": [
            {"title": "上传文件", "text": "打开 WorkBuddy → 选择文件处理 → 上传农林产品调研数据.xlsx", "screenshot": "WorkBuddy 文件上传界面"},
            {"title": "描述清洗需求", "text": "在 Craft 模式输入：请清洗这个表格：统一日期格式为 YYYY-MM-DD，删除完全重复的行，用平均值填充缺失的价格数据，标记价格异常值", "screenshot": "Craft 模式 Prompt 输入区"},
            {"title": "审核清洗方案", "text": "WorkBuddy 会给出清洗步骤预览，检查每一步是否符合预期，必要时调整。", "screenshot": "清洗步骤预览界面"},
            {"title": "执行并导出", "text": "点击执行，等待处理完成，下载清洗后的文件。", "screenshot": "执行结果与下载按钮"}
        ]
    },
    {
        "type": "practice",
        "title": "报告生成 Craft 模式分步指导",
        "steps": [
            {"title": "创建报告模板", "text": "在 WorkBuddy 选择报告生成 → 新建模板 → 定义章节结构", "screenshot": "报告模板编辑界面"},
            {"title": "绑定数据源", "text": "选择刚才清洗后的 Excel 文件作为数据源，映射各章节对应的数据列", "screenshot": "数据源映射界面"},
            {"title": "设置生成规则", "text": "选择图表类型（柱状图/饼图/折线图），设置配色方案，定义输出格式", "screenshot": "图表与格式设置"},
            {"title": "生成并导出", "text": "点击生成报告，预览效果，导出为 PDF", "screenshot": "最终报告预览"}
        ]
    },
    {
        "type": "content",
        "section": "任务拓展",
        "kicker": "进阶思考",
        "title": "如果数据量翻 100 倍怎么办？",
        "left": [
            {"title": "小数据 vs 大数据", "type": "table", "headers": ["维度", "小数据（本课）", "大数据（企业）"], "rows": [
                ["数据量", "千行级别", "百万行级别"],
                ["处理方式", "WorkBuddy 单文件", "数据库 + ETL 工具"],
                ["存储", "本地 Excel", "云数据库/数据仓库"],
                ["协作", "单人处理", "多人实时协作"],
                ["自动化", "手动触发", "定时任务/流水线"]
            ]}
        ],
        "right": [
            {"title": "进阶学习路径", "items": [
                "学习 SQL 基础：用数据库管理海量数据",
                "了解 ETL 工具：如 Kettle、Airflow",
                "探索 BI 平台：如 Tableau、Power BI、帆软",
                "学习 Python pandas：更灵活的数据处理"
            ]},
            {"type": "hint", "title": "课程定位", "text": "本课程让你理解数据处理的逻辑，工具会不断更新，但底层思维是通用的。", "variant": "success"}
        ]
    },
    {
        "type": "quiz",
        "questions": [
            {
                "type": "单选",
                "question": "OpenClaw 的三层架构中，负责可插拔功能模块的是哪一层？",
                "options": ["A. 核心层", "B. 技能层（Skills）", "C. 接入层", "D. 数据层"],
                "answer": "B. 技能层（Skills）。技能层提供可插拔的功能模块，如搜索、文件处理、微信推送等。"
            },
            {
                "type": "多选",
                "question": "WorkBuddy 的 Craft 模式可以完成哪些任务？",
                "options": ["A. Excel 数据清洗", "B. 报告自动生成", "C. 文件批量处理", "D. 编写 Python 代码"],
                "answer": "A、B、C。Craft 模式支持 Excel 清洗、报告生成、文件批量处理。D 选项是 Trae 的功能。"
            },
            {
                "type": "简答",
                "question": "请简述 GEPA 进化循环的四个步骤，并举一个生活中的例子。",
                "answer": "G（Goal 定目标）→ E（Evolve 进化策略）→ P（Perform 执行）→ A（Assess 评估）。例子：学生备考——定目标分数→制定学习计划→执行学习→模考评估→调整计划。"
            }
        ]
    },
    {
        "type": "end",
        "summary": [
            "OpenClaw 三层架构：核心层（大脑）、技能层（乐高积木）、接入层（多渠道）",
            "Hermes GEPA 进化循环：Goal → Evolve → Perform → Assess",
            "WorkBuddy Craft 模式：自然语言驱动办公自动化",
            "Excel 清洗四步法：格式统一 → 去重 → 填充缺失 → 异常处理",
            "报告自动化：模板 + 数据 = 一键生成专业报告",
            "项目启动：分组、选题、技术方案、MVP 边界定义"
        ],
        "next_title": "Day 3 预告",
        "next_preview": "上午：AI IDE 发展简史 + Trae Builder 模式深度演示 + 安装配置\n下午：项目核心功能开发 I —— 用 Trae 生成项目前端界面"
    }
]
