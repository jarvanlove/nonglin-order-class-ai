# 05 - 编码规范

> 目标：统一前后端代码风格，让代码可读、可维护，便于 AI 理解和生成。

---

## 前端规范（TypeScript + React）

### 文件组织

- 每个组件一个文件，文件名与组件名一致
- 类型定义单独放在 `src/types/` 目录
- 工具函数放在 `src/utils/` 目录
- API 请求按模块分文件放在 `src/api/` 目录

### 命名规范

| 类型 | 规范 | 示例 |
|------|------|------|
| 组件文件 | PascalCase.tsx | `UserCard.tsx` |
| 组件名 | PascalCase | `function UserCard() {}` |
| Props 类型 | 组件名 + Props | `interface UserCardProps {}` |
| Hooks | use + 功能 | `useUserList` |
| 工具函数 | camelCase | `formatPrice` |
| 常量 | UPPER_SNAKE_CASE | `API_BASE_URL` |
| 布尔变量 | is / has / can 前缀 | `isLoading`, `hasError` |

### 组件写法规范

```tsx
// ✅ 推荐：函数组件 + 显式返回类型
import React from 'react'
import { User } from '../types/user'

interface UserCardProps {
  user: User
  onSelect?: (id: number) => void
}

export const UserCard: React.FC<UserCardProps> = ({ user, onSelect }) => {
  const handleClick = () => {
    onSelect?.(user.id)
  }

  return (
    <div className="user-card" onClick={handleClick}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </div>
  )
}
```

### 类型定义规范

```typescript
// ✅ 推荐：接口用于对象，类型别名用于联合类型

// 对象用 interface
export interface Product {
  id: number
  name: string
  price: number
  createdAt: string
}

// 创建/更新用 Omit/Partial
export type ProductCreate = Omit<Product, 'id' | 'createdAt'>
export type ProductUpdate = Partial<ProductCreate>

// 联合类型用 type
export type Status = 'pending' | 'approved' | 'rejected'
```

### 禁止事项

- ❌ 不要使用 `any` 类型（除非万不得已，必须加注释说明）
- ❌ 不要在一个文件里定义多个组件
- ❌ 不要直接修改 props（props 是只读的）
- ❌ 不要在 render 里写复杂逻辑（抽成函数或 useMemo）

---

## 后端规范（Python + FastAPI）

### 文件组织

- 路由按模块分文件放在 `routers/` 目录
- 数据库模型放在 `models/` 目录
- Pydantic 模型放在 `schemas/` 目录
- 工具函数放在 `utils/` 目录

### 命名规范

| 类型 | 规范 | 示例 |
|------|------|------|
| Python 文件 | 小写 + 下划线 | `product_router.py` |
| 类名 | PascalCase | `class ProductModel:` |
| 函数名 | 小写 + 下划线 | `def get_product_list():` |
| 常量 | 大写 + 下划线 | `DEFAULT_PAGE_SIZE = 10` |
| 私有函数 | 单下划线前缀 | `def _validate_data():` |

### 路由写法规范

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas.product import ProductCreate, ProductResponse
from models.product import ProductModel

router = APIRouter(prefix="/api/products", tags=["products"])

@router.get("/", response_model=List[ProductResponse])
def get_product_list(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)
):
    """
    获取产品列表
    
    - page: 页码，从1开始
    - page_size: 每页数量，默认10
    """
    offset = (page - 1) * page_size
    products = db.query(ProductModel).offset(offset).limit(page_size).all()
    return products

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """创建新产品"""
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
```

### Pydantic 模型规范

```python
from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal

class ProductBase(BaseModel):
    """产品基础字段"""
    name: str = Field(..., min_length=1, max_length=255, description="产品名称")
    category: Optional[str] = Field(None, description="产品种类")
    origin: Optional[str] = Field(None, description="产地")
    price: Optional[Decimal] = Field(None, ge=0, description="价格")
    stock: int = Field(default=0, ge=0, description="库存")

class ProductCreate(ProductBase):
    """创建产品请求"""
    pass

class ProductUpdate(ProductBase):
    """更新产品请求"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)

class ProductResponse(ProductBase):
    """产品响应"""
    id: int
    user_id: int
    created_at: str
    updated_at: str
    
    class Config:
        from_attributes = True
```

### 错误处理规范

```python
# ✅ 推荐：使用 HTTPException 返回标准错误
from fastapi import HTTPException, status

@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"产品 ID {product_id} 不存在"
        )
    return product
```

### 禁止事项

- ❌ 不要在路由函数里写 SQL 字符串（用 ORM）
- ❌ 不要直接返回数据库模型（用 Pydantic 模型转换）
- ❌ 不要把密码明文存储或返回（必须哈希处理）
- ❌ 不要忽略异常处理（所有外部调用都要 try-except）

---

## 注释规范

### 前端注释

```typescript
// ✅ 单行注释：解释"为什么"
// 使用防抖避免频繁请求
const debouncedSearch = useDebounce(search, 300)

/**
 * ✅ 函数注释：说明参数和返回值
 * 格式化价格，保留两位小数
 * @param price 原始价格（分）
 * @returns 格式化后的价格字符串（元）
 */
function formatPrice(price: number): string {
  return (price / 100).toFixed(2)
}
```

### 后端注释

```python
# ✅ 函数使用 docstring 说明
def calculate_total(price: Decimal, quantity: int) -> Decimal:
    """
    计算订单总价
    
    Args:
        price: 单价
        quantity: 数量
        
    Returns:
        总价（单价 * 数量）
        
    Raises:
        ValueError: 数量小于0时抛出
    """
    if quantity < 0:
        raise ValueError("数量不能为负数")
    return price * quantity
```
