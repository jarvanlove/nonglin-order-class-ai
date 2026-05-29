# 农林政策信息聚合站 — 项目骨架说明

> **适用课程**：AI 智能体工具实训  
> **项目选题**：农林政策信息聚合站  
> **学生水平**：编码基础薄弱（计算机 + 非计算机混编）  
> **核心约束**：纯前端、可直接用浏览器打开、学生只需"填空"

---

## 一、项目整体架构

```
nonglin-policy-hub/
├── index.html              # 首页：项目总览 + 6大政策维度入口
├── list.html               # 政策列表页：展示某维度的政策卡片列表
├── detail.html             # 政策详情页：单条政策的完整信息
├── about.html              # 关于页：团队介绍 + 项目说明
├── css/
│   └── style.css           # 全局样式（学生一般不需要修改）
├── js/
│   ├── data.js             # 数据接口层：读取各组 JSON 数据（学生一般不需要修改）
│   ├── chart-config.js     # 图表配置模板（学生只需改数据和标题）
│   └── app.js              # 交互逻辑（搜索、筛选、排序）
├── data/                   # 各组数据文件（学生主要工作区域）
│   ├── team1-planting.json     # 第1组：种植政策
│   ├── team2-breeding.json     # 第2组：养殖政策
│   ├── team3-subsidy.json      # 第3组：补贴政策
│   ├── team4-environment.json  # 第4组：环保政策
│   ├── team5-forestry.json     # 第5组：林业政策
│   └── team6-scitech.json      # 第6组：科技政策
└── assets/
    └── images/             # 图片资源（logo、banner、团队照片）
```

---

## 二、页面路由设计

| 页面 | 文件名 | 功能说明 | 学生操作 |
|------|--------|---------|---------|
| **首页** | `index.html` | 项目总览、6大维度入口卡片、整体统计图表 | 改标题、改文案、换图片 |
| **列表页** | `list.html` | 某一维度的政策卡片列表，支持搜索/筛选/排序 | 改页面标题、确认数据路径 |
| **详情页** | `detail.html` | 单条政策的完整信息展示 | 一般不需要修改 |
| **关于页** | `about.html` | 团队介绍、项目说明、分工表 | 改团队信息、改照片 |

**页面跳转方式**：纯 HTML 链接跳转，无路由框架。

```html
<!-- 示例：从首页跳转到种植政策列表页 -->
<a href="list.html?category=planting">种植政策</a>

<!-- 从列表页跳转到详情页 -->
<a href="detail.html?id=1&category=planting">查看详情</a>
```

---

## 三、数据接口契约（JSON 格式模板）

### 3.1 单条政策记录结构

```json
{
  "id": "planting-001",
  "title": "2026年水稻良种补贴政策通知",
  "category": "种植政策",
  "subCategory": "良种补贴",
  "source": "农业农村部",
  "publishDate": "2026-03-15",
  "effectiveDate": "2026-04-01",
  "region": "全国",
  "summary": "为稳定水稻生产，2026年继续实施水稻良种补贴政策，每亩补贴标准为...",
  "keyPoints": [
    "补贴对象：种植水稻的农户和合作社",
    "补贴标准：早稻每亩XX元，晚稻每亩XX元",
    "申请方式：向当地农业农村部门申报"
  ],
  "amount": "每亩XX元",
  "targetGroup": "水稻种植户、农业合作社",
  "applicationProcess": "1.申报 → 2.审核 → 3.公示 → 4.发放",
  "url": "https://www.moa.gov.cn/...",
  "tags": ["水稻", "补贴", "良种"],
  "status": "现行有效"
}
```

### 3.2 每组数据文件结构

每组的数据文件是一个 JSON 数组，包含 10-20 条政策记录：

```json
[
  {
    "id": "planting-001",
    "title": "...",
    "category": "种植政策",
    ...
  },
  {
    "id": "planting-002",
    "title": "...",
    "category": "种植政策",
    ...
  }
]
```

### 3.3 字段说明与必填/选填

| 字段名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `id` | string | 是 | 唯一标识，格式：`维度缩写-序号` |
| `title` | string | 是 | 政策标题 |
| `category` | string | 是 | 主分类（与组对应） |
| `subCategory` | string | 否 | 子分类 |
| `source` | string | 是 | 发布机构 |
| `publishDate` | string | 是 | 发布日期，格式 `YYYY-MM-DD` |
| `effectiveDate` | string | 否 | 生效日期 |
| `region` | string | 否 | 适用地区 |
| `summary` | string | 是 | 政策摘要（100字以内） |
| `keyPoints` | array | 是 | 关键要点（3-5条） |
| `amount` | string | 否 | 补贴金额/标准 |
| `targetGroup` | string | 否 | 适用对象 |
| `applicationProcess` | string | 否 | 申请流程 |
| `url` | string | 否 | 原文链接 |
| `tags` | array | 否 | 标签 |
| `status` | string | 否 | 政策状态 |

---

## 四、外部库清单

| 库名 | 用途 | 引入方式 | 学生是否需要操作 |
|------|------|---------|----------------|
| **ECharts** | 数据可视化（饼图、柱状图、时间线） | CDN | 只需改 `chart-config.js` 中的数据和标题 |
| **Tailwind CSS** | 样式框架（快速美化） | CDN | 一般不需要修改 |
| **Font Awesome** | 图标库 | CDN | 一般不需要修改 |

**CDN 引入示例（已在 HTML 中预置）**：

```html
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- ECharts -->
<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>

<!-- Font Awesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
```

---

## 五、学生"填空"区域说明

### 5.1 必须修改的文件（每组都要改）

| 文件 | 修改内容 | 难度 |
|------|---------|------|
| `data/teamX-xxx.json` | 替换为真实政策数据 | 低 |
| `about.html` | 修改团队名称、成员、分工 | 低 |
| `index.html` | 修改项目标题、简介文案 | 低 |

### 5.2 可选修改的文件（有余力再做）

| 文件 | 修改内容 | 难度 |
|------|---------|------|
| `js/chart-config.js` | 修改图表标题、颜色、数据 | 中 |
| `css/style.css` | 修改主题色、字体 | 中 |
| `list.html` | 调整列表布局、增加筛选条件 | 中高 |

### 5.3 一般不需要修改的文件

| 文件 | 说明 |
|------|------|
| `js/data.js` | 数据读取接口，已封装好 |
| `js/app.js` | 交互逻辑，已封装好 |
| `detail.html` | 详情页模板，自动渲染 |

---

## 六、快速启动步骤（给学生的极简指南）

### 步骤 1：拿到骨架包
老师提供 `nonglin-policy-hub.zip`，解压到桌面。

### 步骤 2：双击打开首页
双击 `index.html`，用浏览器打开。应该能看到一个带占位数据的网页。

### 步骤 3：替换数据
打开 `data/` 文件夹，找到对应组的 JSON 文件，用记事本/Trae 打开，把里面的示例数据替换成真实采集的政策数据。

### 步骤 4：刷新看效果
保存 JSON 文件后，在浏览器中按 `F5` 刷新，即可看到新数据。

### 步骤 5：修改文案
用 Trae 打开 `index.html` 和 `about.html`，把占位文案改成自己的内容。

---

## 七、常见问题速查

| 问题 | 原因 | 解决 |
|------|------|------|
| 页面显示空白 | 浏览器安全策略阻止本地文件读取 | 用 VS Code 的 Live Server 插件打开，或把项目放到本地服务器 |
| 数据不显示 | JSON 格式错误 | 用在线 JSON 校验工具检查 |
| 图表不显示 | ECharts 容器没有高度 | 检查容器是否有 `height` 样式 |
| 中文乱码 | 文件编码不是 UTF-8 | 用记事本另存为 UTF-8 编码 |
| 样式错乱 | CDN 加载失败 | 检查网络，或换成本地 CSS |

---

## 八、给老师的部署建议

1. **课前准备**：把骨架包提前发给学生，确保每个人都能双击打开 `index.html` 看到效果。
2. **数据备份**：每组的数据文件命名固定，方便后期汇总。
3. **集成方式**：Day 5 整合时，老师只需把 6 个组的 JSON 文件放到 `data/` 目录下，首页会自动加载所有数据。
4. **路演展示**：直接用浏览器打开 `index.html` 演示即可，无需部署服务器。

---

*版本：v1.0*  
*日期：2026-05-18*  
*适用：AI 智能体工具实训课程 — 农林政策信息聚合站项目*
