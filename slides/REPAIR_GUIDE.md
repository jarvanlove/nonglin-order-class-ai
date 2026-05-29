# HTML 课件修复规范

> 版本: v2.1 | 日期: 2026-05-18
> 适用范围: 农林高校 AI 工具实训课程全部 HTML 幻灯片

---

## 一、字号标准（投影场景可读性优先）

| 用途 | CSS 变量 | 最小值 | 推荐值 | 绝对禁止 |
|------|---------|--------|--------|----------|
| 正文、列表 | `--text-base` | 11pt | **11.5pt** | < 11pt |
| 小标题、卡片标题 | `--text-xl` / `--text-2xl` | 15pt | 17pt / 19pt | < 14pt |
| 章节标题 | `--text-3xl` | 20pt | 22pt | < 18pt |
| 封面主标题 | `--text-5xl` | 40pt | 48pt | < 32pt |
| 标注、提示 | `--text-xs` | 10pt | **11pt** | < 10pt |
| 页码、版权 | `--text-2xs` | 9pt | **10pt** | < 9pt |
| 代码块 | `--text-xs` | 10pt | 11pt | < 9pt |

### 行高标准
- 正文 `line-height` 最低 **1.5**，推荐 **1.55**
- 标题 `line-height` 最低 **1.15**，推荐 **1.2**
- 列表项 `line-height` 最低 **1.5**，推荐 **1.6**

### 修复操作
1. 搜索所有 HTML 文件中的 `font-size:` 内联样式
2. 凡小于对应用途最小值的，一律提升到最小值
3. 优先使用 CSS 变量（如 `font-size: var(--text-base)`），避免硬编码 pt 值

---

## 二、Padding 与间距标准

| 元素 | CSS 变量 | 最小值 | 当前值 |
|------|---------|--------|--------|
| 通用卡片 `.card` | `--space-6` | 12pt | 14pt |
| 图标卡片 `.icon-card` | `--space-5` | 10pt | 12pt |
| 步骤卡片 `.step-card` | `--space-5` | 10pt | 12pt |
| 提示框 `.hint-box` | `--space-5` `--space-6` | 10pt / 12pt | 12pt / 14pt |
| Prompt 框 `.prompt-box` | `--space-4` `--space-5` | 10pt / 12pt | 10pt / 12pt |
| FAQ 条目 `.faq-item` | `--space-4` | 10pt | 10pt |
| 表格单元格 `.compare-table td/th` | `--space-4` `--space-5` | 10pt / 12pt | 10pt / 12pt |
| 内容区左右边距 | `--content-pad-x` | 20pt | 24pt |
| 内容区上下边距 | `--content-pad-y` | 10pt | **14pt** |

### 修复操作
1. 搜索所有 HTML 文件中的 `padding:` 内联样式
2. 凡卡片/容器 padding < 8pt 的，一律提升到至少 8pt
3. 列表项间距 `margin-bottom` 最低 6pt

---

## 三、布局规则（防止内容遮挡）

### 3.1 图片安全规则
- **禁止**使用 `position: absolute` 的图片直接覆盖在文字上方
- 装饰性图片必须使用 `.deco-layer` 或 `.img-safe` 类
- 内容图片必须与文字处于同一文档流，或使用 `.content-layer` 包裹文字

```html
<!-- 正确：装饰层不拦截事件 -->
<div class="deco-layer">
  <img src="deco.png" class="img-safe">
</div>
<div class="content-layer">
  <h2>标题文字</h2>
</div>

<!-- 错误：图片遮挡文字 -->
<img style="position:absolute; top:0; left:0; z-index:5;">
<div style="position:relative; z-index:1;">被遮挡的文字</div>
```

### 3.2 Grid / Flex 间距
- 两栏/三栏布局 `gap` 最低 **10pt**（`var(--space-5)`）
- Grid 列间距 `gap` 最低 **10pt**
- 禁止为压缩内容把 `gap` 设为 0 或 < 6pt

### 3.3 溢出控制
- 单页内容确实过多时，**优先删减内容**而非压缩字号/padding
- 允许拆分为两页
- `body` 和 `.slide-content` 的 `overflow: hidden` 是 Canvas 级别的硬边界（防止打印时内容跨页），不应被当作内容溢出的"遮羞布"
- 如果预览时发现内容被截断，说明该页需要精简或拆分，而不是依赖隐藏溢出

---

## 四、动画使用规范

### 4.1 页面转场（slide 切换）
给 `<body>` 或 `.slide` 添加 `.slide-enter` 类：
```html
<body class="slide-enter">
```
效果：淡入 + 轻微上滑，0.4s，cubic-bezier(0.22, 1, 0.36, 1)

### 4.2 元素依次入场
给内容容器添加 `.content-enter` 或 `.stagger-children`：
```html
<div class="slide-content content-enter">
  <div>第1个元素</div>
  <div>第2个元素（延迟 0.1s）</div>
  <div>第3个元素（延迟 0.2s）</div>
</div>
```

### 4.3 悬浮特效
- 卡片悬浮：添加 `.hover-lift` 类（上浮 2pt + 阴影加深）
- 按钮悬浮：添加 `.btn-hover` 类（亮度提升 + 阴影）
- 发光悬浮：添加 `.hover-glow` 类（外发光环）

### 4.4 点击/聚焦反馈
- 可点击元素添加 `.active-scale`（点击时轻微缩小 0.96）
- 可聚焦元素添加 `.focus-ring`（聚焦时显示品牌色外环）

### 4.5 性能约束
- 动画只使用 `transform` 和 `opacity`，禁止动画 `width/height/margin`
- 打印时自动禁用所有动画（已内置 `@media print`）

---

## 五、给后续修复师的操作指南

### Step 1: 扫描问题
```bash
# 查找过小的字号（包含小数，如 8.5pt）
grep -rnE "font-size:\s*[0-9]+(\.[0-9]+)?pt" slides/

# 查找过小的 padding（包含小数）
grep -rnE "padding[^:]*:\s*([0-9]+(\.[0-9]+)?pt\s+){1,3}[0-4](\.[0-9]+)?pt" slides/

# 查找绝对定位的图片
grep -rn "position:\s*absolute" slides/ | grep -i "img"
```

### Step 2: 批量修复策略
1. **先改共享 CSS**：确保 `shared/tokens.css`、`shared/components.css`、`shared/layout.css` 已更新到本规范版本
2. **再改 HTML 内联样式**：逐个打开 HTML 文件，删除或提升过小的 `font-size` 和 `padding`
3. **最后加动画**：在关键页面（封面、章节页、目标页）添加 `.slide-enter` 和 `.content-enter`

### Step 3: 验证清单
- [ ] 正文最小 11pt，标注最小 10pt，页码最小 9pt
- [ ] 卡片 padding 最小 8pt，普遍 10pt+
- [ ] 没有 absolute 图片遮挡文字
- [ ] Grid/Flex gap 最小 10pt
- [ ] 动画使用 transform/opacity -only
- [ ] 打印预览正常（无动画残留、无内容截断）

### Step 4: 溢出处理
如果修复后某页出现溢出：
1. 检查是否内容确实过多（> 300 字正文 + 多图）
2. 尝试精简文字（删除冗余修饰语）
3. 尝试拆分为两页
4. **最后手段**：微调该页特定元素的 padding（仅该页，不动共享 CSS）

---

## 六、品牌色（禁止修改）

```css
--primary:       #084E8F;  /* 深蓝 */
--secondary:     #92181A;  /* 深红 */
--accent:        #EE822F;  /* 橙色 */
--success:       #75BD42;  /* 绿色 */
```

---

## 七、Canvas 尺寸

- 宽度: **960pt**
- 高度: **540pt**
- 比例: **16:9**
- 禁止修改 body 宽高
