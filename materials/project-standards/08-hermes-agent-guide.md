# 08 - Hermes Agent 配置指南

> 目标：安装 Hermes Agent 后，完成 Cloud API 连接、工具注册和调试，让 Agent 能调用学生项目的 API。

---

## Hermes Agent 是什么？

Hermes Agent 是一个开源 AI Agent 框架，让 AI 不仅能"回答问题"，还能"自主执行任务"。

**与普通 Chatbot 的区别**：

| | Chatbot（豆包/DeepSeek） | Agent（Hermes） |
|--|------------------------|----------------|
| 交互方式 | 一问一答 | 你给目标，它自己拆解执行 |
| 工具调用 | 不能调用外部工具 | 能调用数据库、API、浏览器等 |
| 任务持续性 | 对话结束就停止 | 可持续运行，循环检查进度 |
| 使用场景 | 查资料、写文案 | 自动整理数据、定时任务、智能推荐 |

**架构图（Cloud API 模式）**：

```
┌─────────────────────────────────────────────┐
│              你的电脑（本地）                  │
│  ┌───────────────────────────────────────┐  │
│  │         Hermes Agent 框架               │  │
│  │  ┌─────────┐  ┌─────────┐  ┌────────┐ │  │
│  │  │ 任务拆解 │→│ 工具调用 │→│ 结果汇总│ │  │
│  │  └─────────┘  └─────────┘  └────────┘ │  │
│  │         ↑ 读取本地工具配置               │  │
│  └─────────┬─────────────────────────────┘  │
│            │                                 │
│  ┌─────────▼─────────┐   ┌───────────────┐  │
│  │   你的项目 API     │   │   浏览器工具   │  │
│  │ (FastAPI 后端)     │   │  (Chromium)   │  │
│  └───────────────────┘   └───────────────┘  │
└─────────────────────┬───────────────────────┘
                      │ HTTPS
                      ▼
┌─────────────────────────────────────────────┐
│           云端大模型 API                     │
│    (DeepSeek / OpenRouter / Anthropic)      │
└─────────────────────────────────────────────┘
```

**工作流程**：
1. 你给 Hermes Agent 一个目标（如："把今天上传的农产品自动分类"）
2. Agent 拆解成步骤：① 读取数据库 ② 分析内容 ③ 更新分类字段
3. Agent 调用你的项目 API（FastAPI 后端）执行操作
4. Agent 检查执行结果，如果失败则重试或报错

---

## 安装步骤

### 前提条件

- Node.js v20+（已安装）
- npm 或 pnpm

### 安装命令

```bash
npm install -g hermes-agent
```

验证安装：

```bash
hermes --version
```

---

## Cloud API 配置

### 1. 获取 API Key

Hermes Agent 需要连接一个云端大模型。教学场景下，使用 DeepSeek API（性价比高，中文好）：

- API Key 由讲师统一提供
- 或自行在 DeepSeek 官网申请

### 2. 配置模型连接

创建配置文件 `~/.hermes/config.json`：

```json
{
  "model": {
    "provider": "deepseek",
    "api_key": "sk-xxxxxxxxxxxxxxxx",  // 由讲师提供
    "model_name": "deepseek-chat",
    "base_url": "https://api.deepseek.com/v1"
  }
}
```

### 3. 验证连接

```bash
hermes chat
```

输入 "你好"，如果能收到回复，说明配置成功。

---

## 工具注册

Hermes Agent 的强大之处在于能"调用工具"。你需要把项目 API 注册为 Agent 的工具。

### 注册项目 API 为工具

创建工具定义文件 `~/.hermes/tools/my-project-api.json`：

```json
{
  "name": "product_api",
  "description": "农产品管理系统 API",
  "tools": [
    {
      "name": "get_products",
      "description": "获取所有农产品列表",
      "method": "GET",
      "url": "http://localhost:8000/api/products",
      "parameters": {
        "page": { "type": "integer", "description": "页码" },
        "page_size": { "type": "integer", "description": "每页数量" }
      }
    },
    {
      "name": "create_product",
      "description": "创建新农产品",
      "method": "POST",
      "url": "http://localhost:8000/api/products",
      "parameters": {
        "name": { "type": "string", "description": "产品名称" },
        "category": { "type": "string", "description": "种类" },
        "price": { "type": "number", "description": "价格" }
      }
    },
    {
      "name": "update_product",
      "description": "更新农产品信息",
      "method": "PUT",
      "url": "http://localhost:8000/api/products/{id}",
      "parameters": {
        "id": { "type": "integer", "description": "产品ID" },
        "name": { "type": "string", "description": "产品名称" },
        "stock": { "type": "integer", "description": "库存" }
      }
    }
  ]
}
```

### 测试工具调用

```bash
hermes run "帮我把所有库存为0的农产品标记为'缺货'"
```

Agent 会自动：
1. 调用 `get_products` 获取所有产品
2. 筛选出库存为 0 的产品
3. 调用 `update_product` 更新状态

---

## 调试技巧

### 查看 Agent 执行日志

```bash
hermes run "帮我把所有库存为0的农产品标记为'缺货'" --verbose
```

`--verbose` 会显示 Agent 每一步的思考和工具调用过程。

### 单步调试

```bash
hermes run "帮我把所有库存为0的农产品标记为'缺货'" --step
```

`--step` 模式下，Agent 每执行一步都会暂停，等你确认后再继续。

### 常见错误排查

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| "API connection failed" | API Key 错误或网络问题 | 检查 config.json 中的 api_key 和 base_url |
| "Tool not found" | 工具配置文件路径错误 | 检查 `~/.hermes/tools/` 目录下的 JSON 文件 |
| "HTTP 404" | API 路由错误 | 检查工具定义中的 url 是否与后端路由一致 |
| "HTTP 500" | 后端报错 | 查看后端终端日志，修复后端代码 |

---

## 教学场景下的使用建议

### 场景 1：自动数据整理

学生上传一批农产品图片和描述，Agent 自动：
1. 读取图片和描述
2. 调用 AI 分析内容，提取关键信息（名称、种类、产地）
3. 自动写入数据库

**提示词模板**：
```
我有一批农产品数据需要录入系统，文件在 ./data/ 目录下。

请帮我：
1. 读取所有 .txt 文件
2. 提取产品名称、种类、产地、价格
3. 调用 product_api 的 create_product 工具录入系统
4. 完成后告诉我录入了多少条
```

### 场景 2：智能库存监控

Agent 定时检查库存，自动提醒：

```
请检查系统中所有农产品的库存，把库存低于 10 的产品名称和库存数量列出来。
```

### 场景 3：自动分类

Agent 根据产品描述自动分类：

```
请读取所有未分类的农产品，根据产品名称和描述自动判断种类（水果/蔬菜/粮油），并更新分类字段。
```

---

## 与 Claude Code CLI 的分工

| 工具 | 主要用途 | 使用阶段 |
|------|---------|---------|
| **Claude Code CLI** | 生成代码、修改代码、修复 Bug | Day 1-5 全程 |
| **Hermes Agent** | 执行自动化任务、调用项目 API | Day 4（进阶） |

**不要混淆**：
- Claude Code CLI 是"代码生成器"，帮你写代码
- Hermes Agent 是"任务执行器"，帮你自动运行已写好的代码
