# 02 - 项目架子规范

> 目标：统一全栈项目的目录结构，让前后端代码组织清晰、易于协作。

---

## 技术栈

| 层级 | 技术 | 版本 |
|------|------|------|
| 前端 | React + Vite + TypeScript | React 18, Vite 5 |
| 后端 | Python + FastAPI | Python 3.10+ |
| 数据库 | PostgreSQL | 15+ |
| 包管理 | pnpm（前端）/ pip（后端） | - |

---

## 项目目录结构

```
my-project/                 # 项目根目录（学生自选名称）
├── README.md               # 项目说明
├── .gitignore              # Git 忽略规则
│
├── frontend/               # 前端目录
│   ├── index.html          # 入口 HTML
│   ├── vite.config.ts      # Vite 配置
│   ├── tsconfig.json       # TypeScript 配置
│   ├── package.json        # 前端依赖
│   ├── src/
│   │   ├── main.tsx        # 应用入口
│   │   ├── App.tsx         # 根组件
│   │   ├── components/     # 公共组件
│   │   │   ├── Header.tsx
│   │   │   ├── Footer.tsx
│   │   │   └── Button.tsx
│   │   ├── pages/          # 页面组件
│   │   │   ├── Home.tsx
│   │   │   ├── List.tsx
│   │   │   └── Detail.tsx
│   │   ├── hooks/          # 自定义 Hooks
│   │   ├── utils/          # 工具函数
│   │   ├── types/          # TypeScript 类型定义
│   │   └── api/            # API 请求封装
│   └── public/             # 静态资源
│
├── backend/                # 后端目录
│   ├── main.py             # FastAPI 入口
│   ├── requirements.txt    # Python 依赖
│   ├── .env                # 环境变量（数据库连接等）
│   ├── routers/            # 路由模块
│   │   ├── items.py
│   │   └── users.py
│   ├── models/             # 数据库模型（SQLAlchemy）
│   │   ├── item.py
│   │   └── user.py
│   ├── schemas/            # Pydantic 数据校验模型
│   │   ├── item.py
│   │   └── user.py
│   └── database.py         # 数据库连接配置
│
└── docs/                   # 项目文档（可选）
    └── api.md              # 接口文档
```

---

## 初始化步骤（Vibe Coding 用）

### 前端初始化提示词模板

```
请帮我创建一个 React + Vite + TypeScript 项目，项目名称为 [学生自选]。

要求：
1. 使用 Vite 作为构建工具
2. 使用 TypeScript，开启严格模式
3. 目录结构按照以下规范：
   - src/components/ 放公共组件
   - src/pages/ 放页面组件
   - src/api/ 放 API 请求封装
   - src/types/ 放类型定义
4. 安装 lucide-react 作为图标库
5. 安装 axios 用于 HTTP 请求
6. 创建一个简单的首页，显示 "Hello Vibe Coding"

请生成完整的项目代码，包括 package.json、vite.config.ts、tsconfig.json。
```

### 后端初始化提示词模板

```
请帮我创建一个 Python FastAPI 项目，作为 [项目名称] 的后端服务。

要求：
1. 使用 FastAPI 框架
2. 使用 SQLAlchemy 作为 ORM
3. 使用 Pydantic 做数据校验
4. 数据库使用 PostgreSQL，连接信息从环境变量读取
5. 目录结构：
   - main.py: 应用入口
   - database.py: 数据库连接
   - models/: 数据库模型
   - schemas/: Pydantic 模型
   - routers/: API 路由
6. 创建一个简单的 /health 接口，返回 {"status": "ok"}
7. 生成 requirements.txt

请生成完整的项目代码。
```

---

## 前后端联调配置

### 前端代理配置（vite.config.ts）

开发时前端跑在 `http://localhost:5173`，后端跑在 `http://localhost:8000`，需要配置代理：

```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      }
    }
  }
})
```

### 后端 CORS 配置（main.py）

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 命名规范

| 类型 | 规范 | 示例 |
|------|------|------|
| 项目目录 | 小写，短横线连接 | `my-project` |
| React 组件 | PascalCase | `UserCard.tsx` |
| TS 类型/接口 | PascalCase | `UserType` |
| TS 函数/变量 | camelCase | `getUserList` |
| Python 文件 | 小写，下划线连接 | `user_model.py` |
| Python 类 | PascalCase | `UserModel` |
| Python 函数 | 小写，下划线连接 | `get_user_list` |
| API 路由 | 小写，短横线连接 | `/api/v1/user-list` |
