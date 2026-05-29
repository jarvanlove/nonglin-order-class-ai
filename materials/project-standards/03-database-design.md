# 03 - 数据库设计规范

> 目标：让学生理解如何用自然语言描述需求，再让 AI 生成规范的数据库表结构。

---

## 核心原则

1. **一张表只做一件事**：不要把用户信息、订单信息、商品信息混在一张表里
2. **每个表必须有主键**：统一使用 `id`（自增整数或 UUID）
3. **外键要建立关联**：如果 A 表引用了 B 表的数据，必须建立外键关系
4. **字段要有注释**：每个字段都要说明它存储什么数据
5. **不要用保留字做字段名**：如 `order`、`user`、`select` 等

---

## 命名规范

| 对象 | 规范 | 示例 |
|------|------|------|
| 表名 | 小写，复数形式，下划线连接 | `users`, `order_items` |
| 字段名 | 小写，下划线连接 | `created_at`, `user_name` |
| 主键 | 统一叫 `id` | `id` |
| 外键 | 关联表名单数 + `_id` | `user_id`, `order_id` |
| 时间字段 | `created_at`, `updated_at` | 统一使用这两个名字 |

---

## 常用字段类型对照

| 数据含义 | PostgreSQL 类型 | 说明 |
|----------|----------------|------|
| 自增主键 | `SERIAL` | 自动递增的整数 |
| UUID | `UUID` | 全局唯一标识符 |
| 短文本 | `VARCHAR(255)` | 用户名、标题等 |
| 长文本 | `TEXT` | 文章内容、描述等 |
| 整数 | `INTEGER` | 数量、年龄等 |
| 金额 | `DECIMAL(10,2)` | 精确到分的价格 |
| 布尔值 | `BOOLEAN` | 是/否 |
| 时间戳 | `TIMESTAMP WITH TIME ZONE` | 创建时间、更新时间 |
| 枚举 | `VARCHAR` + CHECK 约束 | 状态：pending/approved/rejected |
| JSON | `JSONB` | 灵活存储结构化数据 |

---

## 设计示例

### 场景：学生做一个"农产品信息管理系统"

**需求描述（自然语言）：**
> 系统需要记录农产品信息，包括名称、种类、产地、价格、库存数量。每个农产品有一个发布者（用户）。用户有用户名、手机号、角色（管理员/普通用户）。

**AI 生成表结构提示词：**

```
请根据以下需求，设计 PostgreSQL 数据库表结构：

需求：
1. 用户表：存储用户信息，包括用户名、手机号、密码、角色（管理员/普通用户）
2. 农产品表：存储农产品信息，包括名称、种类、产地、价格、库存数量、发布者
3. 用户和农产品是一对多关系（一个用户可以发布多个农产品）

要求：
- 使用 PostgreSQL 语法
- 每个表包含 id、created_at、updated_at
- 建立外键关联
- 字段添加注释
- 生成 CREATE TABLE SQL 语句
```

**预期输出：**

```sql
-- 用户表
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL COMMENT '用户名',
    phone VARCHAR(20) UNIQUE COMMENT '手机号',
    password_hash VARCHAR(255) NOT NULL COMMENT '密码哈希',
    role VARCHAR(20) DEFAULT 'user' CHECK (role IN ('admin', 'user')) COMMENT '角色',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 农产品表
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL COMMENT '农产品名称',
    category VARCHAR(100) COMMENT '种类（水果/蔬菜/粮油等）',
    origin VARCHAR(255) COMMENT '产地',
    price DECIMAL(10,2) COMMENT '价格（元）',
    stock INTEGER DEFAULT 0 COMMENT '库存数量',
    user_id INTEGER NOT NULL COMMENT '发布者ID',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

---

## SQLAlchemy 模型规范（Python）

FastAPI 中使用 SQLAlchemy 定义模型时，遵循以下规范：

```python
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(255), nullable=False)
    phone = Column(String(20), unique=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="user")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100))
    origin = Column(String(255))
    price = Column(DECIMAL(10, 2))
    stock = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

---

## 字段设计 Checklist

设计每张表时，对照以下清单检查：

- [ ] 是否有主键 `id`？
- [ ] 是否有 `created_at` 和 `updated_at`？
- [ ] 每个字段是否都有明确的数据类型？
- [ ] 是否对可能重复的字段加了唯一约束（如手机号、邮箱）？
- [ ] 外键是否建立了关联？
- [ ] 是否有合理的默认值？
- [ ] 字段名是否避免使用 SQL 保留字？
