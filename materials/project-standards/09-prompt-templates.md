# 09 - 标准提示词模板

> 目标：提供各阶段的标准提示词模板，学生可以直接复制到 Claude Code CLI 中使用。

---

## 前端提示词模板

### T1：生成 React 组件

```
请帮我创建一个 React 组件，文件路径：src/components/{组件名}.tsx

功能描述：{详细描述组件要做什么}

技术要求：
- 使用 TypeScript，定义 Props 接口
- 使用 Tailwind CSS 做样式
- 使用 lucide-react 图标库（如需要图标）
- 组件名使用 PascalCase
- 添加必要的注释

数据：{描述数据结构和来源}

样式要求：{颜色、布局、响应式等要求}
```

**示例**：
```
请帮我创建一个 React 组件，文件路径：src/components/ProductCard.tsx

功能描述：显示单个农产品的卡片，包含图片、名称、产地、价格和库存。

技术要求：
- 使用 TypeScript，定义 Props 接口
- 使用 Tailwind CSS 做样式
- 使用 lucide-react 的 MapPin 和 Package 图标
- 组件名使用 PascalCase

数据：
interface Product {
  id: number
  name: string
  origin: string
  price: number
  stock: number
  image?: string
}

样式要求：
- 白色背景卡片，圆角，阴影
- 图片在上方，占满宽度，高度 200px，object-fit cover
- 名称用粗体，价格用蓝色
- 库存低时（<10）显示红色警告
- 卡片悬停时阴影加深
```

---

### T2：生成页面

```
请帮我创建一个页面组件，文件路径：src/pages/{页面名}.tsx

功能描述：{页面要展示什么、有什么交互}

包含的组件：{列出需要的子组件}

API 接口：{调用的后端接口}

路由：{页面 URL 路径}
```

**示例**：
```
请帮我创建一个页面组件，文件路径：src/pages/ProductList.tsx

功能描述：农产品列表页面，显示所有产品，支持分页和按种类筛选。

包含的组件：
- ProductCard（产品卡片）
- Pagination（分页组件）
- CategoryFilter（种类筛选）

API 接口：
- GET /api/products?page=1&page_size=10&category=水果

路由：/products
```

---

### T3：生成自定义 Hook

```
请帮我创建一个自定义 Hook，文件路径：src/hooks/{hook名}.ts

功能描述：{Hook 要封装什么逻辑}

参数：{输入参数及类型}

返回值：{返回什么数据和方法}

使用场景：{在什么组件中使用}
```

**示例**：
```
请帮我创建一个自定义 Hook，文件路径：src/hooks/useProducts.ts

功能描述：封装产品数据的获取、分页和筛选逻辑。

参数：
- page: number（页码）
- pageSize: number（每页数量）
- category?: string（种类筛选，可选）

返回值：
- products: Product[]（产品列表）
- loading: boolean（加载状态）
- error: string | null（错误信息）
- total: number（总数量）
- refetch: () => void（重新获取数据）

使用场景：在 ProductList 页面中使用
```

---

## 后端提示词模板

### T4：生成 FastAPI 路由

```
请帮我创建一个 FastAPI 路由模块，文件路径：backend/routers/{模块名}.py

功能描述：{该模块要提供什么 API}

数据库模型：{关联的 SQLAlchemy 模型}

Pydantic 模型：{请求/响应的数据结构}

需要的接口：
- GET /api/xxx - 获取列表（支持分页）
- GET /api/xxx/{id} - 获取单个
- POST /api/xxx - 创建
- PUT /api/xxx/{id} - 更新
- DELETE /api/xxx/{id} - 删除

特殊要求：{权限控制、数据校验等}
```

**示例**：
```
请帮我创建一个 FastAPI 路由模块，文件路径：backend/routers/products.py

功能描述：农产品相关的 CRUD 接口。

数据库模型：
class ProductModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100))
    origin = Column(String(255))
    price = Column(DECIMAL(10, 2))
    stock = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey("users.id"))

Pydantic 模型：
- ProductCreate: name, category, origin, price, stock
- ProductUpdate: 所有字段可选
- ProductResponse: 包含 id, user_id, created_at

需要的接口：
- GET /api/products?page=1&page_size=10 - 获取列表
- GET /api/products/{id} - 获取单个
- POST /api/products - 创建（需要登录）
- PUT /api/products/{id} - 更新（只能更新自己的）
- DELETE /api/products/{id} - 删除（只能删除自己的）

特殊要求：
- 创建/更新/删除需要验证 user_id
- 返回统一的响应格式 {code, message, data}
```

---

### T5：生成数据库模型

```
请帮我创建 SQLAlchemy 模型，文件路径：backend/models/{模型名}.py

表名：{表名}

字段：{列出所有字段及类型}

关联关系：{与其他表的关系}

约束：{唯一约束、外键等}
```

**示例**：
```
请帮我创建 SQLAlchemy 模型，文件路径：backend/models/order.py

表名：orders

字段：
- id: 主键，自增
- product_id: 整数，外键关联 products.id
- user_id: 整数，外键关联 users.id
- quantity: 整数，数量
- total_price: DECIMAL(10,2)，总价
- status: 字符串，状态（pending/paid/shipped/completed）
- created_at: 时间戳
- updated_at: 时间戳

关联关系：
- 多对一关联 ProductModel
- 多对一关联 UserModel

约束：
- quantity > 0
- status 只能是预设值之一
```

---

## 数据库提示词模板

### T6：生成表结构 SQL

```
请根据以下需求，生成 PostgreSQL 的 CREATE TABLE 语句：

需求：{自然语言描述}

表名：{表名}

字段说明：{列出字段及含义}

关联：{与其他表的关系}

要求：
- 包含 id, created_at, updated_at
- 添加合适的索引
- 添加注释（COMMENT ON）
- 使用 PostgreSQL 语法
```

**示例**：
```
请根据以下需求，生成 PostgreSQL 的 CREATE TABLE 语句：

需求：记录用户对农产品的评价

表名：reviews

字段说明：
- 评价ID：主键
- 产品ID：关联农产品
- 用户ID：关联用户
- 评分：1-5分
- 评价内容：文本
- 是否匿名：布尔值
- 创建时间

关联：
- 多对一关联 products
- 多对一关联 users

要求：
- 包含 id, created_at, updated_at
- product_id 和 user_id 添加索引
- 添加外键约束
- 评分添加 CHECK 约束（1-5）
```

---

## Agent 提示词模板

### T7：让 Hermes Agent 执行批量任务

```
请帮我完成以下任务：

目标：{要达成的目标}

步骤：
1. {第一步}
2. {第二步}
3. {第三步}

约束：{限制条件}

完成后请告诉我：{需要返回什么信息}
```

**示例**：
```
请帮我完成以下任务：

目标：整理今天新上传的农产品数据

步骤：
1. 读取 ./data/today/ 目录下的所有 .csv 文件
2. 解析每行数据，提取名称、种类、产地、价格
3. 调用 product_api 的 create_product 工具录入系统
4. 记录成功和失败的数量

约束：
- 价格不能为负数，遇到负数跳过并记录
- 名称不能为空，遇到空名称跳过并记录

完成后请告诉我：
- 成功录入了多少条
- 跳过了多少条（分别说明原因）
```

---

## 调试提示词模板

### T8：修复报错

```
我的项目报错了，请帮我修复。

错误信息：{复制报错内容}

相关文件：{涉及的文件路径}

预期行为：{应该发生什么}

实际行为：{实际发生了什么}
```

**示例**：
```
我的项目报错了，请帮我修复。

错误信息：
Error: Cannot read properties of undefined (reading 'name')
    at ProductCard (src/components/ProductCard.tsx:15)

相关文件：src/components/ProductCard.tsx

预期行为：产品卡片正常显示产品信息

实际行为：页面白屏，控制台报上述错误
```

---

### T9：优化代码

```
请帮我优化以下代码：

文件路径：{文件路径}

优化目标：{性能 / 可读性 / 减少重复 / 添加错误处理}

当前代码：{粘贴代码}
```

**示例**：
```
请帮我优化以下代码：

文件路径：src/hooks/useProducts.ts

优化目标：添加错误处理和加载状态

当前代码：
const useProducts = () => {
  const [products, setProducts] = useState([])
  
  useEffect(() => {
    fetch('/api/products')
      .then(res => res.json())
      .then(data => setProducts(data))
  }, [])
  
  return products
}
```

---

## 使用建议

1. **复制模板 → 填空 → 粘贴到 Claude Code CLI**
2. **不要一次性给太多需求**，分步迭代效果更好
3. **生成的代码一定要审查**，AI 不是万能的
4. **遇到报错先用 `/fix`**，比手动找 Bug 快得多
