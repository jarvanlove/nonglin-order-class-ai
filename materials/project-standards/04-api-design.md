# 04 - API 接口规范

> 目标：统一前后端接口格式，让联调顺畅，让学生理解 RESTful 设计思想。

---

## RESTful 设计原则

1. **URL 是资源，不是动作**：
   - ✅ `/api/products`（产品资源）
   - ❌ `/api/getProducts` 或 `/api/deleteProduct`

2. **用 HTTP 方法表示动作**：
   - `GET`：获取资源
   - `POST`：创建资源
   - `PUT`：更新资源（全量）
   - `PATCH`：更新资源（部分）
   - `DELETE`：删除资源

3. **使用复数名词**：
   - ✅ `/api/users`
   - ❌ `/api/user`

4. **嵌套表示关联**：
   - `/api/users/1/products`（用户 1 的所有产品）

---

## URL 设计示例

以"农产品信息管理系统"为例：

| 功能 | 方法 | URL | 说明 |
|------|------|-----|------|
| 获取所有农产品 | GET | `/api/products` | 支持分页、筛选 |
| 获取单个农产品 | GET | `/api/products/{id}` | |
| 创建农产品 | POST | `/api/products` | 需要登录 |
| 更新农产品 | PUT | `/api/products/{id}` | 需要登录 + 权限 |
| 删除农产品 | DELETE | `/api/products/{id}` | 需要登录 + 权限 |
| 用户注册 | POST | `/api/users/register` | |
| 用户登录 | POST | `/api/users/login` | 返回 Token |
| 获取当前用户 | GET | `/api/users/me` | 需要登录 |

---

## 请求/响应格式规范

### 统一响应结构

无论成功还是失败，后端返回的 JSON 必须包含以下结构：

```json
{
  "code": 200,
  "message": "success",
  "data": { ... }
}
```

### 成功响应示例

**获取单个产品：**
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "name": "陕西红富士苹果",
    "category": "水果",
    "origin": "陕西洛川",
    "price": 12.50,
    "stock": 100,
    "user_id": 1,
    "created_at": "2026-06-01T10:00:00Z"
  }
}
```

**获取列表（带分页）：**
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "items": [ ... ],
    "total": 100,
    "page": 1,
    "page_size": 10
  }
}
```

### 错误响应示例

```json
{
  "code": 400,
  "message": "参数错误：价格不能为空",
  "data": null
}
```

常见状态码：

| HTTP 状态码 | 含义 | 使用场景 |
|------------|------|---------|
| 200 | 成功 | 正常返回 |
| 201 | 创建成功 | POST 创建资源后返回 |
| 400 | 请求参数错误 | 参数校验失败 |
| 401 | 未授权 | 未登录或 Token 失效 |
| 403 | 禁止访问 | 无权限操作 |
| 404 | 资源不存在 | URL 或 ID 错误 |
| 500 | 服务器内部错误 | 后端异常 |

---

## 分页规范

列表接口必须支持分页，参数统一为：

- `page`：页码，从 1 开始，默认 1
- `page_size`：每页条数，默认 10，最大 100

请求示例：
```
GET /api/products?page=1&page_size=10&category=水果
```

---

## FastAPI 路由组织规范

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import product as product_schema
from models import product as product_model

router = APIRouter(prefix="/api/products", tags=["products"])

@router.get("/")
def get_products(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    """获取产品列表"""
    ...

@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    """获取单个产品"""
    ...

@router.post("/")
def create_product(product: product_schema.ProductCreate, db: Session = Depends(get_db)):
    """创建产品"""
    ...

@router.put("/{product_id}")
def update_product(product_id: int, product: product_schema.ProductUpdate, db: Session = Depends(get_db)):
    """更新产品"""
    ...

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """删除产品"""
    ...
```

---

## 前端 API 封装规范

在 `frontend/src/api/` 目录下创建请求模块：

```typescript
// api/client.ts
import axios from 'axios'

const client = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 响应拦截器：统一处理错误
client.interceptors.response.use(
  (response) => response.data,
  (error) => {
    const message = error.response?.data?.message || '请求失败'
    alert(message)
    return Promise.reject(error)
  }
)

export default client
```

```typescript
// api/product.ts
import client from './client'

export const getProducts = (params?: { page?: number; page_size?: number; category?: string }) =>
  client.get('/products', { params })

export const getProduct = (id: number) =>
  client.get(`/products/${id}`)

export const createProduct = (data: ProductCreate) =>
  client.post('/products', data)

export const updateProduct = (id: number, data: ProductUpdate) =>
  client.put(`/products/${id}`, data)

export const deleteProduct = (id: number) =>
  client.delete(`/products/${id}`)
```
