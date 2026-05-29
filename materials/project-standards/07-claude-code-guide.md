# 07 - Claude Code CLI 配置指南

> 目标：安装 Claude Code CLI 后，完成配置、调教，让它成为高效的 Vibe Coding 助手。

---

## Claude Code CLI 是什么？

Claude Code CLI 是 Anthropic 官方推出的命令行 AI 编程助手。它不仅能生成代码，还能：
- 读取和修改你项目中的文件
- 运行终端命令（测试、构建、Git 操作）
- 理解整个代码库的上下文
- 自动修复报错

**架构图（简化版）**：

```
┌─────────────────────────────────────────────┐
│              你的电脑（本地）                  │
│  ┌─────────────┐      ┌──────────────────┐  │
│  │  终端 / VS Code │◄──►│ Claude Code CLI  │  │
│  └─────────────┘      └────────┬─────────┘  │
│                                │            │
│  ┌─────────────────────────────▼─────────┐  │
│  │           你的项目代码文件夹             │  │
│  │  (React + FastAPI + PostgreSQL)        │  │
│  └────────────────────────────────────────┘  │
└─────────────────────┬───────────────────────┘
                      │ HTTPS
                      ▼
┌─────────────────────────────────────────────┐
│         Anthropic 云端服务器                 │
│         (Claude Sonnet / Opus)              │
└─────────────────────────────────────────────┘
```

**工作流程**：
1. 你在终端输入需求（自然语言）
2. Claude Code CLI 读取相关代码文件作为上下文
3. 发送到云端 Claude 模型处理
4. 返回代码修改建议或新生成的代码
5. 你可以选择接受（Y）、拒绝（N）或让 AI 调整

---

## 安装后配置

### 1. 首次登录

安装完成后，运行：

```bash
claude
```

按提示输入 API Key（由讲师统一提供）。

### 2. 配置默认模型

Claude Code CLI 支持多个模型，推荐配置：

```bash
# 查看当前配置
claude config get model

# 设置为 Sonnet（平衡速度和质量，适合教学）
claude config set model claude-sonnet-4

# 或设置为 Opus（质量最高，但较慢较贵）
claude config set model claude-opus-4
```

### 3. 配置工作目录

Claude Code CLI 默认在**当前目录**工作。进入你的项目目录后再运行 `claude`：

```bash
cd my-project
claude
```

---

## 常用命令速查

### 基础命令

| 命令 | 作用 | 示例 |
|------|------|------|
| `claude` | 启动交互式会话 | `claude` |
| `/clear` | 清除当前对话上下文 | `/clear` |
| `/exit` | 退出会话 | `/exit` |
| `/help` | 查看所有命令 | `/help` |

### 代码操作命令

| 命令 | 作用 | 示例 |
|------|------|------|
| `/edit <文件>` | 编辑指定文件 | `/edit src/App.tsx` |
| `/explain <文件>` | 解释代码逻辑 | `/explain backend/main.py` |
| `/refactor <文件>` | 重构代码 | `/refactor src/utils/api.ts` |
| `/test <文件>` | 生成单元测试 | `/test src/components/Button.tsx` |
| `/fix` | 修复当前报错 | `/fix` |

### 系统命令

在 Claude Code CLI 中，你可以直接运行系统命令（前面加 `!`）：

```bash
# 查看当前目录文件
!ls

# 运行前端开发服务器
!pnpm dev

# 运行后端服务
!uvicorn main:app --reload

# Git 操作
!git status
!git add .
!git commit -m "feat: 添加登录功能"
```

---

## Skill / MCP / Plugin 配置

### Skill（技能）

Skill 是预定义的提示词模板，让 Claude Code CLI 在特定场景下表现更好。

**创建自定义 Skill**：

在项目根目录创建 `.claude/skills/` 目录：

```bash
mkdir -p .claude/skills
```

创建 `react-component.md`：

```markdown
# React 组件开发

你是一名 React + TypeScript 专家。生成组件时遵循以下规则：

1. 使用函数组件 + FC 类型
2. Props 使用 interface 定义
3. 组件名使用 PascalCase
4. 添加必要的注释
5. 使用 lucide-react 作为图标库
```

使用时在对话中说：
```
使用 react-component skill，帮我生成一个用户卡片组件
```

### MCP（Model Context Protocol）

MCP 让 Claude Code CLI 能连接外部工具（如数据库、文件系统、浏览器等）。

**常用 MCP 工具**：

| MCP 工具 | 作用 |
|---------|------|
| `filesystem` | 读写本地文件 |
| `postgres` | 直接查询 PostgreSQL 数据库 |
| `fetch` | 发起 HTTP 请求 |

**配置 MCP**（在 `.claude/mcp.json` 中）：

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://user:pass@localhost:5432/mydb"]
    }
  }
}
```

### Plugin（插件）

Claude Code CLI 的插件系统可以扩展其功能。教学场景下，主要使用内置功能即可，暂不深入插件开发。

---

## 调教技巧

### 技巧 1：给足上下文

❌ 差的提示词：
```
帮我写一个登录页面
```

✅ 好的提示词：
```
我在做一个农产品信息管理系统，使用 React + TypeScript + Tailwind CSS。

请帮我写一个登录页面，要求：
1. 包含用户名和密码输入框
2. 有登录按钮和"忘记密码"链接
3. 调用后端 /api/users/login 接口（POST，参数：{username, password}）
4. 登录成功后跳转到首页 /
5. 使用 lucide-react 的 Lock 和 User 图标
6. 样式要美观，有圆角卡片和阴影

请生成完整的 Login.tsx 组件代码。
```

### 技巧 2：分步迭代

不要一次性让 AI 做太多事。先让 AI 生成基础版本，确认后再添加功能：

```
第一步：生成一个基础的产品列表页面，只显示产品名称和价格
第二步：给每个产品添加图片和"查看详情"按钮
第三步：添加分页功能
```

### 技巧 3：让 AI 解释再修改

如果 AI 生成的代码你看不懂，先让它解释：

```
/explain src/components/ProductList.tsx
```

理解后再提出修改需求。

### 技巧 4：用 `/fix` 处理报错

当前端或后端报错时，不要手动找 Bug，直接：

```bash
claude
/fix
```

Claude Code CLI 会自动读取报错信息并尝试修复。

### 技巧 5：保存常用提示词

把常用的提示词模板保存为 Skill（见上文），避免每次重复输入。

---

## 常见问题

| 问题 | 解决方案 |
|------|---------|
| API Key 失效 | 联系讲师重新获取 |
| 响应太慢 | 切换到 Sonnet 模型，或检查网络 |
| 生成的代码不符合项目结构 | 在提示词中明确说明目录结构和命名规范 |
| Claude 修改了不该改的文件 | 使用 `/edit` 指定具体文件，而非让 AI 全局搜索 |
| 不想把代码发到云端 | 教学场景下使用讲师提供的 API Key，数据已脱敏 |
