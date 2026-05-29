# Day 3 slide data

day_num = 3
day_title = "Trae 编程 + 项目开发基础"
subtitle = "AI IDE 演进 · Trae Builder 模式 · 自然语言编程 · 项目核心开发"
output = "slides/day03/index.html"

slides = [
    {"type": "cover"},
    {
        "type": "objectives",
        "knowledge": [
            "了解 AI IDE 发展历史和全球工具生态",
            "理解 Trae Builder 模式的工作原理",
            "掌握 Trae 的安装配置和基础操作",
            "理解 API 基础概念和项目技术方案"
        ],
        "skills": [
            "能独立完成 Trae 的安装和首个 Builder 项目",
            "能用自然语言描述需求并生成可运行代码",
            "能使用 Trae 的 Chat 模式调试和优化代码",
            "能用 Trae 开发项目的核心功能模块"
        ],
        "literacy": [
            "建立用自然语言驱动开发的思维方式",
            "理解 AI 编程不是取代程序员，而是改变工作方式",
            "培养遇到问题先找 AI 辅助，再人工审核的习惯"
        ]
    },
    {
        "type": "intro",
        "question": "如果你不会写代码，但想做一个能显示天气预报的网页，你需要学多久？",
        "subtitle": "传统答案：学 HTML/CSS/JavaScript，至少 3-6 个月。今天之后你的答案：10 分钟——用 Trae 的 Builder 模式。",
        "cards": [
            {"title": "QClaw：信息搜集", "text": "获取数据和信息", "tag": "已完成", "tag_class": "tag-primary"},
            {"title": "WorkBuddy：数据处理", "text": "清洗、分析、生成报告", "tag": "已完成", "tag_class": "tag-accent"},
            {"title": "Trae：展示开发", "text": "把数据和逻辑变成可交互的网页/应用", "tag": "今天学习", "tag_class": "tag-success"}
        ]
    },
    {
        "type": "content",
        "section": "知识储备",
        "kicker": "历史演进",
        "title": "AI IDE 发展简史：从手写代码到零代码开发",
        "left": [
            {"title": "传统编程时代", "text": "程序员打开编辑器，一行一行手写代码，遇到不会的就去查文档、搜 Stack Overflow。开发一个简单网页需要数天甚至数周。", "items": []},
            {"title": "AI 辅助编程时代（2021-2023）", "items": [
                "2021：GitHub Copilot 发布，首次实现代码自动补全",
                "2022：Cursor 发布，AI 原生编辑器概念诞生",
                "2023：各种 AI 编程工具爆发，国内开始跟进"
            ]}
        ],
        "right": [
            {"title": "零代码开发时代（2024-至今）", "items": [
                "2024：Trae 发布 Builder 模式，零代码开发成为可能",
                "2025-2026：AI IDE 成为开发者标配",
                "未来：自然语言描述需求 = 可运行产品"
            ]},
            {"type": "hint", "title": "核心转变", "text": "从手写每一行代码 → 描述需求让 AI 生成代码 → 人工审核和调整。程序员的工作从编码转向设计和审核。", "variant": "success"}
        ]
    },
    {
        "type": "content",
        "section": "知识储备",
        "kicker": "工具对比",
        "title": "全球 AI IDE 全景对比",
        "left": [
            {"title": "国外三大巨头", "items": [
                "Cursor：AI 原生编辑器，代码补全和重构最强",
                "GitHub Copilot：与 GitHub 深度整合，生态最成熟",
                "Replit：云端 IDE，适合初学者"
            ]},
            {"title": "国产替代方案", "items": [
                "Trae：字节跳动出品，Builder 模式是最大亮点",
                "通义灵码：阿里出品，VS Code 插件形式",
                "CodeBuddy：腾讯出品，与微信生态整合"
            ]}
        ],
        "right": [
            {"title": "Cursor vs Trae 对比", "type": "table", "headers": ["维度", "Cursor", "Trae"], "rows": [
                ["定位", "专业开发者", "零基础友好"],
                ["核心模式", "Chat + 补全", "Builder + Chat + Solo"],
                ["学习曲线", "中等", "极低"],
                ["代码质量", "高（需审核）", "中（够用）"],
                ["适用场景", "企业级开发", "快速原型/MVP"]
            ]},
            {"type": "hint", "title": "课程选择", "text": "本课程使用 Trae，因为它的 Builder 模式对零基础同学最友好，用自然语言就能生成可运行代码。", "variant": "success"}
        ]
    },
    {
        "type": "content",
        "section": "知识储备",
        "kicker": "核心工具",
        "title": "Trae 三模式详解",
        "left": [
            {"title": "Builder 模式（零基础首选）", "text": "用自然语言描述完整需求，AI 自动生成项目结构和代码。适合从零开始做一个新功能或新项目。", "items": [
                "输入：我要一个显示天气预报的网页",
                "输出：完整的 HTML/CSS/JS 代码 + 文件结构",
                "适用：快速原型、MVP 开发、学习练手"
            ]},
            {"title": "Chat 模式（调试优化）", "text": "像和同事聊天一样，向 AI 描述问题或需求，AI 给出代码建议并直接修改文件。", "items": [
                "输入：这个按钮点击没反应，帮我看看为什么",
                "输出：问题分析 + 修复代码 + 修改建议",
                "适用：Bug 修复、功能优化、代码重构"
            ]}
        ],
        "right": [
            {"title": "Solo 模式（专注编码）", "text": "AI 在后台实时补全代码，像有一个经验丰富的程序员坐在你旁边，每写一行都给你建议。", "items": [
                "输入：你写 function calc(",
                "输出：AI 自动补全函数体和参数",
                "适用：已有代码库的维护、精细调整"
            ]},
            {"type": "hint", "title": "课程重点", "text": "本课程主要使用 Builder 模式快速生成项目骨架，用 Chat 模式调试优化。Solo 模式作为补充了解。", "variant": "success"}
        ]
    },
    {
        "type": "content",
        "section": "知识储备",
        "kicker": "实战演示",
        "title": "Builder 模式：10 分钟做一个天气预报网页",
        "left": [
            {"type": "prompt", "title": "Step 1：描述需求", "text": "我要一个天气预报网页，显示当前城市的温度、湿度、风速，未来 3 天的预报，用卡片式布局，背景根据天气类型变化。"},
            {"type": "prompt", "title": "Step 2：补充细节", "text": "添加一个城市搜索框，用户可以切换城市。用渐变色背景，卡片有圆角和阴影，整体风格简洁现代。"}
        ],
        "right": [
            {"title": "Trae 生成的代码结构", "items": [
                "index.html：页面结构和内容",
                "style.css：样式和动画",
                "app.js：数据获取和交互逻辑",
                "（Trae 会自动创建这些文件）"
            ]},
            {"type": "hint", "title": "关键技巧", "text": "描述需求时遵循 5W1H 原则：What（做什么）、Who（给谁用）、Where（什么场景）、When（什么时候）、Why（为什么）、How（什么风格）。", "variant": "success"}
        ]
    },
    {
        "type": "content",
        "section": "知识储备",
        "kicker": "技术基础",
        "title": "API 是什么？为什么项目需要它？",
        "left": [
            {"title": "API 通俗解释", "text": "API（应用程序接口）就像餐厅的服务员。你不需要进厨房做饭，只需要看菜单点菜，服务员把菜端给你。API 让不同的软件系统能互相通信。", "items": []},
            {"title": "项目中的 API 作用", "items": [
                "QClaw 通过 API 获取天气/新闻/数据",
                "WorkBuddy 通过 API 读取和写入文件",
                "Trae 生成的网页通过 API 获取实时数据",
                "三个工具之间通过 API 交换信息"
            ]}
        ],
        "right": [
            {"title": "常见 API 类型", "items": [
                "天气 API：获取实时天气数据",
                "地图 API：获取地理位置和距离",
                "翻译 API：中英文自动转换",
                "AI 大模型 API：文本生成、图像识别"
            ]},
            {"type": "hint", "title": "零基础友好", "text": "Trae 会自动帮你写 API 调用代码。你只需要告诉它：我要用某某 API，它就会生成完整的调用逻辑。", "variant": "success"}
        ]
    },
    {
        "type": "content",
        "section": "知识储备",
        "kicker": "项目规划",
        "title": "技术方案细化：从想法到可执行计划",
        "left": [
            {"title": "技术方案四要素", "items": [
                "数据层：用什么 API？数据格式是什么？",
                "处理层：WorkBuddy 做什么清洗/分析？",
                "展示层：Trae 生成什么界面？有什么交互？",
                "联调层：三个模块如何交换数据？"
            ]},
            {"title": "MVP 边界控制", "text": "不要试图一次性做完美。先回答：最核心的一个功能是什么？只做这一个，其他都放到 v2。", "items": []}
        ],
        "right": [
            {"title": "示例：农产品价格监测", "items": [
                "数据层：QClaw 搜集某农产品每日价格",
                "处理层：WorkBuddy 计算周均价和涨跌幅",
                "展示层：Trae 生成折线图 + 预警提示",
                "MVP：只监测 1 种农产品，只显示最近 7 天"
            ]},
            {"type": "hint", "title": "成功标准", "text": "MVP 成功的标准：数据能从 QClaw 流入 WorkBuddy，再流入 Trae，最终用户能看到结果。", "variant": "success"}
        ]
    },
    {
        "type": "task",
        "title": "下午实战任务：Trae 项目核心功能开发 I & II",
        "steps": [
            {"title": "Trae 安装与首个 Builder 项目（45 分钟）", "text": "完成 Trae 安装，用 Builder 模式生成项目基础界面（首页 + 数据展示页）。"},
            {"title": "核心功能开发 I（60 分钟）", "text": "实现数据展示模块：从 QClaw 搜集结果或模拟数据，在 Trae 生成的页面上显示表格/图表。"},
            {"title": "核心功能开发 II（60 分钟）", "text": "实现交互功能：搜索、筛选、刷新。用 Chat 模式调试和优化代码。"},
            {"title": "MVP 验证（15 分钟）", "text": "组内演示：数据能从入口流入，在页面上正确显示。记录 Bug 清单。"}
        ],
        "deliverables": [
            "Trae 安装完成截图",
            "项目基础代码（至少 2 个页面）",
            "可运行的数据展示模块",
            "Bug 清单和修复计划"
        ],
        "standards": [
            "界面完整：至少包含首页和数据展示页",
            "数据流通：能从数据源正确显示到页面上",
            "交互可用：至少实现 1 个交互功能（搜索/筛选/刷新）",
            "代码规范：文件结构清晰，注释完整"
        ]
    },
    {
        "type": "practice",
        "title": "Trae Builder 模式分步指导",
        "steps": [
            {"title": "新建项目", "text": "打开 Trae → 点击 New Project → 选择 Blank Project → 命名项目", "screenshot": "Trae 新建项目界面"},
            {"title": "进入 Builder 模式", "text": "点击左侧 Builder 图标 → 在输入框描述你的项目需求", "screenshot": "Builder 模式输入区"},
            {"title": "审核生成方案", "text": "Trae 会给出项目结构和文件清单，确认无误后点击 Generate", "screenshot": "项目结构预览"},
            {"title": "预览和调试", "text": "点击 Preview 查看效果，有问题用 Chat 模式提问并修复", "screenshot": "预览窗口和 Chat 面板"}
        ]
    },
    {
        "type": "practice",
        "title": "Chat 模式调试技巧",
        "steps": [
            {"title": "描述问题", "text": "选中出错的代码 → 右键 Ask AI → 输入：这个函数返回 undefined，请帮我检查", "screenshot": "选中代码 + Ask AI"},
            {"title": "查看分析", "text": "Trae 会分析问题原因，给出修复建议和修改后的代码", "screenshot": "AI 分析结果"},
            {"title": "应用修复", "text": "点击 Apply Change 直接应用修改，或 Copy 手动粘贴", "screenshot": "Apply Change 按钮"},
            {"title": "验证结果", "text": "重新运行 Preview，确认 Bug 已修复", "screenshot": "修复后的预览效果"}
        ]
    },
    {
        "type": "content",
        "section": "任务拓展",
        "kicker": "进阶思考",
        "title": "AI 编程的边界在哪里？",
        "left": [
            {"title": "AI 擅长的事", "items": [
                "生成标准套路代码（表单、表格、图表）",
                "Bug 定位和修复建议",
                "代码重构和优化",
                "技术文档和注释生成"
            ]},
            {"title": "AI 不擅长的事", "items": [
                "复杂业务逻辑设计",
                "系统架构决策",
                "安全性和性能优化",
                "用户体验的深度打磨"
            ]}
        ],
        "right": [
            {"title": "人类的不可替代性", "items": [
                "需求理解：真正理解用户想要什么",
                "质量把关：审核 AI 生成的代码是否可靠",
                "创新设计：想出 AI 训练语料里没有的解决方案",
                "伦理判断：决定什么该做、什么不该做"
            ]},
            {"type": "hint", "title": "未来趋势", "text": "AI 不会取代程序员，但会用 AI 的程序员会取代不会用 AI 的程序员。本课程让你成为前者。", "variant": "success"}
        ]
    },
    {
        "type": "quiz",
        "questions": [
            {
                "type": "单选",
                "question": "Trae 的 Builder 模式最适合什么场景？",
                "options": ["A. 调试已有代码的 Bug", "B. 从零开始生成新项目", "C. 优化代码性能", "D. 管理代码版本"],
                "answer": "B. Builder 模式用自然语言描述需求，自动生成完整的项目结构和代码，最适合从零开始。"
            },
            {
                "type": "多选",
                "question": "一个好的 Builder Prompt 应该包含哪些要素？",
                "options": ["A. 做什么（功能描述）", "B. 给谁用（目标用户）", "C. 什么风格（UI 风格）", "D. 用什么框架（技术栈）"],
                "answer": "A、B、C、D 都应该包含。5W1H 原则越完整，AI 生成的结果越符合预期。"
            },
            {
                "type": "简答",
                "question": "如果你的项目需要显示实时数据，但 API 调用失败了，你会怎么处理？",
                "answer": "1) 先检查网络连接；2) 查看 API 文档确认参数是否正确；3) 用 Chat 模式让 Trae 检查代码；4) 添加备用方案（显示模拟数据或友好提示）。"
            }
        ]
    },
    {
        "type": "end",
        "summary": [
            "AI IDE 演进：手写代码 → 代码补全(Copilot) → AI编辑器(Cursor) → 零代码开发(Trae Builder)",
            "Trae 三模式：Builder（从零生成）、Chat（调试优化）、Solo（实时补全）",
            "Builder 模式核心：自然语言描述需求 → AI 生成代码 → 人工审核调整",
            "API 是不同系统之间的通信桥梁，项目中三工具通过数据交换实现联调",
            "MVP 原则：先跑通核心流程，再逐步完善",
            "下午完成项目核心功能开发，实现数据从入口到展示的完整流通"
        ],
        "next_title": "Day 4 预告",
        "next_preview": "上午：QClaw/WorkBuddy 进阶技巧 + 三工具联调方法\n下午：项目冲刺 I —— 功能完善 + 联调测试"
    }
]
