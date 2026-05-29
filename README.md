# 农林高校 AI 工具实训课程

> 面向农林高校应届毕业生的 6 天 AI 工具实训课程，理论 + 实践，就业导向。

---

## 课程概览

| 属性 | 内容 |
|------|------|
| 授课对象 | 农林高校应届毕业生（计算机 + 非计算机混编，30 人） |
| 授课时长 | 6 天 × 6.5 小时/天 |
| 核心工具 | QClaw（信息搜集）+ WorkBuddy（办公自动化）+ Trae（AI 编程） |
| 课程目标 | 掌握国产 AI 工具技能，建立全球 AI 生态认知，产出可写进简历的跨工具项目 |
| 后续计划 | 6 天课程结束后沉淀 2-3 天，再为学校老师讲课 |

## 文件结构

```
nonglin-order-class-ai/
├── content/                          # 6 天详细授课内容
│   ├── day01-ai-overview/            # Day 1: AI 全景认知 + QClaw 上手
│   ├── day02-agent-deep/             # Day 2: Agent 深度 + WorkBuddy 办公
│   ├── day03-coding-ecosystem/       # Day 3: 编程工具生态 + 项目启动
│   ├── day04-project-sprint1/        # Day 4: 项目冲刺 I
│   ├── day05-project-sprint2/        # Day 5: 项目冲刺 II
│   ├── day06-polish-career/          # Day 6: 项目打磨 + 就业锦囊 + LLM-Wiki + 路演结业
│   └── llm-wiki-lecture/             # LLM-Wiki 授课标准（老师课复用）
├── slides/                           # 演讲幻灯片（huashu-design 产物）
│   └── slides-master-outline.md      # 幻灯片总大纲与视觉风格指南
├── materials/                        # 学员手册 + 实践指导书 + 验收标准
│   ├── student-handbook.md           # 学员手册（课前预习 + 工具准备）
│   ├── practice-guide.md             # 实践指导书（给助教的详细步骤）
│   ├── project-rubric.md             # 项目验收标准与评分细则
│   └── templates/                    # 模板文件
│       ├── project-proposal-template.md
│       ├── weekly-report-template.md
│       └── resume-template.md
└── README.md                         # 本文件
```

## 快速导航

### 讲师备课
1. 先读 `PRODUCT_SPEC.md` 和 `ARCHITECTURE.md` 了解当前 6 天课程范围
2. 按天阅读 `content/day0X-xxx/` 下的授课内容
3. 参考 `materials/practice-guide.md` 了解实践环节细节
4. 使用 `slides/` 下的幻灯片进行授课

### 老师课复用（后续给学校老师讲课）

以下模块可直接抽取使用：

| 模块 | 来源文件 | 给老师讲课时的价值 |
|------|---------|-------------------|
| AI 通识 | Day 1 上午 | 建立 AI 全景认知 |
| Agent 原理 | Day 2 上午 | 技术前沿洞察 |
| 工具选型 | Day 3 上午 | 教学中如何选择 AI 工具 |
| 教师 AI 素养 | Day 6 下午 | 日常办公提效 + 安全规范 |
| 知识管理 | Day 6 + `llm-wiki-lecture/lecture-standard.md` | 教师个人知识管理体系 |

建议重组方案：
- **Day A**：AI 通识（Day 1）+ 工具选型（Day 3 精简版）
- **Day B**：教师 AI 素养（Day 6 改编版）
- **Day C**：知识管理（`lecture-standard.md`）

## 内容统计

| 类别 | 文件数 | 字数（约） |
|------|--------|-----------|
| 6 天详细授课内容 | 21 个 | 约 24 万字 |
| 学员手册 | 1 个 | 1.0 万字 |
| 实践指导书 | 1 个 | 7.7 万字 |
| 项目验收标准 | 1 个 | 0.8 万字 |
| 模板文件 | 3 个 | 1.4 万字 |
| **合计** | **27 个** | **约 35 万字** |

## 关键约束

- 实践阶段禁止使用国外 AI 工具（Claude、Codex、ChatGPT、Cursor）和 VPN
- 理论课可以介绍国外工具，建立全球视野
- 不对学生分 A/B 轨道，统一难度，确保 30 人都能跟上
- QClaw / WorkBuddy / Trae 是教学载体，不是职业标准工具

## 版本记录

| 版本 | 日期 | 说明 |
|------|------|------|
| v1.0 | 2026-04-27 | 课程设计规格书定稿 + 全部授课内容完成 |

---

*本项目基于 ObsidianToWiki 知识管理体系设计。*
