---
name: 腾讯云架构师长沙同盟PPT模板适配Skill
version: "3.2"
description: 腾讯云架构师长沙同盟沙龙/技术分享 PPT 模板适配 Skill。锁定四项品牌资产——背景、字体、Logo、配色合规——其余内容、版式、图表、图片风格全部交由其他 PPT Skill 或讲师自由发挥。适用于（1）从主题/大纲生成新 PPT 后套用模板，或（2）将讲师/嘉宾已有 PPT 迁移到模板，或（3）将 HTML 内容直接转换为品牌合规 PPT。该 Skill 应在 PPT 生命周期的"最后一公里"被调用，作为模板适配层而非内容生成器。触发场景：基于腾讯云架构师长沙同盟模板生成沙龙 PPT、把 PPT 套到模板、嘉宾 PPT 换统一模板、HTML/网页/文章转 PPT、保留内容只替换背景/字体/Logo/配色、PPT 要符合腾讯云架构师长沙同盟模板规范。
agent_created: true
---

# 腾讯云架构师长沙同盟 PPT 模板适配 Skill

## 一、Skill 定位

这是一个 **PPT 模板适配 Skill**，不是内容创作器。

它的唯一职责：在不破坏讲师/嘉宾创作成果的前提下，让最终 PPT 继承腾讯云架构师长沙同盟模板的四项品牌资产：

1. **背景**（背景图 / 背景色）
2. **字体**（中文 + 西文统一 TencentSans W3/W7）
3. **Logo**（位置、尺寸锁死）
4. **配色合规**（禁用色替换为品牌安全色）
5. **文字对比度修复**（浅色背景+浅色文字 → 自动翻转为深灰）
6. **元素溢出检测**（内容溢出页面边界或侵入 Logo 安全区时报告警告）

**只锁前四样。5/6 是辅助迁移能力，仅修复/报告不改布局。其他一切——版式、内容、图表数据、图片风格、动画、信息架构——都不强制。**

---

## 二、核心铁律（不可违反）

1. **只做四项适配**（背景 / 字体 / Logo / 配色合规），其余字段不主动改写。
2. 不得擅自重构页面内容、改写讲师文案、删减原始信息。
3. 不得为了"模板统一"而强制所有页面使用完全相同版式。
4. 原 PPT 中的文本、图片、图表、表格、SmartArt 应**尽量保留原状**。
5. 若内容超出页面边界，可做**轻量排版优化**（缩小字号），但不得改变原意或删除信息。
6. **Logo**：不得拉伸变形、不得被遮挡、保持原始宽高比 463:50。
7. **字体**：必须统一为 `TencentSans W7`（标题）/ `TencentSans W3`（正文），代码块可保留等宽字体。
8. **背景**：必须使用公司模板背景图，不允许出现无关品牌背景。
9. 不得引入与公司无关的第三方品牌 Logo、水印、装饰元素。
10. 输出必须是 `.pptx` 格式。
11. **配色**：上游 PPT Skill 生成内容时必须从 §4.4 安全调色板取色，禁用蓝紫/绿色/青色/粉色/彩色渐变。
12. **背景可见性**：禁止使用撑满整页的不透明大白卡承载内容（否则模板背景被完全遮挡）。
13. **字体名锁定**：只能写 `TencentSans W3` / `TencentSans W7`（英文带空格），禁止中文别名和 PostScript 名。
14. **Logo 位置锁死**（按页面类型区分，`classify_page` 返回 cover/section/end/content）：
    - cover/section/end 页：`logo-main.png` 放**左上角** `(x=0.65", y=0.61", w=4.88", h=0.53")`
    - content 页：`logo-main.png` 放**右上角** `(x=14.60", y=0.49", w=4.88", h=0.53")`（logo-corner 已移除不再使用）
15. **Logo 安全区**：封面/扉页左上角 0-5.60" x 0-1.20"、内容页右上角 14.50-20" x 0-1.10" 不得放置内容元素。
16. **实测优先**：任何模板规范设定必须先解析模板 XML 实测，禁止凭直觉猜。
17. **HTML→PPT 迁移铁律**：执行 HTML→PPT 转换时，**必须先走 §十五阶段零**判定自动/手动路线，然后严格遵守 §十三（35 条经验）+ §十五 Checklist + §十六异常处理。生成后必须运行 `verify_output.py` 验证。手动构建时必须从 §13.31 复用标准辅助函数模板，禁止重新实现。

---

## 三、模板资产清单

```
assets/
├── templates/
│   └── changsha-architect-salon-template.pptx   # 基准模板（实际尺寸 18305463x10296525 EMU，约 20.02x11.26 inch）
├── backgrounds/
│   ├── bg-cover.jpeg                            # 封面/章节扉页背景（米黄底+红色城市线稿+烟花）
│   └── bg-content.jpeg                          # 内容页背景（淡米黄+浅红色低饱和水印）
├── logos/
│   ├── logo-main.png                            # 主 Logo「腾讯云架构师技术同盟」横排文字（PNG 透明底，4.88"x0.53"）
│   └── logo-corner.png                          # [已弃用] 左上角小图标，不再插入
└── fonts/                                       # 已内置 TencentSans W3/W7 字体文件（TTF + OTF）
    ├── TencentSans-W3.ttf
    ├── TencentSans-W7.ttf
    └── README.md                                # 字体安装说明
```

**多城市支持**：执行 `scripts/extract_template_assets.py --pptx <城市模板.pptx> --city <city>` 提取新城市资产。提取后的背景文件命名为 `{city}-bg-cover.jpeg` / `{city}-bg-content.jpeg`。

---

## 四、品牌规范

> 详细补充见 `references/brand-rules.md`。

### 4.1 背景规范

| 页面类型 | 背景文件 | 说明 |
| --- | --- | --- |
| 封面页 / 章节扉页 / 结尾页 | `bg-cover.jpeg` | 米黄底+饱和红色城市线稿（**整体色调偏浅**） |
| 内容页 | `bg-content.jpeg` | 淡水印浅米黄 |
| 全屏图表 / 全屏代码 | 允许纯白 `#FFFFFF` | Logo 必须保留 |

背景图铺满整页（z-order 最底层），不得加滤镜、不得换色。

> ⚠️ **文字颜色强制规则**：`bg-cover.jpeg` 和 `bg-content.jpeg` 均为**浅色底**（米黄/淡米黄），因此封面页、章节扉页、结尾页上的**所有文字必须以深色显示**（`#222222` 或 `#000000`），禁止使用白色/浅灰等浅色文字，否则将完全不可读。此规则也适用于适配脚本覆盖背景后可能出现的浅色文字残留场景。

**实现方式**（Python）：`scripts/apply_template.py` 中的 `set_slide_background(slide, image_path)` 函数：
1. **先清除 `<p:bg>`**：移除上游 Skill 可能写入的纯色/渐变背景填充（`cSld.remove(bg_elem)`），防止底色透出
2. 添加全屏图片并将 pic 元素移到 spTree 最前位置（z-order 最底）

> ⚠️ **常见 BUG（已修复）**：如果 `set_slide_background()` 不清除 `<p:bg>`，任何上游 Skill（PptxGenJS、python-pptx 等）通过 `slide.background = {...}` 设置的纯色填充会残留在图片底层，导致"底部露出一截纯色"。修复方法：在插入背景图之前通过 `cSld.find(qn('p:bg'))` 定位并 `cSld.remove()` 清除。

> ⚠️ **上游 Skill 建议**：尽管适配脚本已能清除 `<p:bg>`，仍建议上游 Skill 在封面/章节/结尾页**不设 `slide.background`**（保持透明），避免生成阶段预览时出现误导色。同时不要在封面/章节/结尾页添加全高装饰条块——模板背景图 `bg-cover.jpeg` 自带设计元素，额外条块会叠加产生视觉干扰。

### 4.2 字体规范

| 用途 | family name |
| --- | --- |
| 标题 / 强调（字号 >= 24pt） | **`TencentSans W7`** |
| 正文 | **`TencentSans W3`** |
| 代码块（含 Mono/Consolas/Menlo/Courier） | 保留不替换 |

字体文件已内置于 `assets/fonts/`，使用前需安装到系统：
- Windows: 双击 .ttf 安装，或复制到 `%LOCALAPPDATA%\Microsoft\Windows\Fonts\`
- macOS: 复制到 `~/Library/Fonts/`
- Linux: 复制到 `~/.fonts/` 后运行 `fc-cache -fv`

安装后重启 Office 进程。

**禁用字体名**：`腾讯体 W3/W7`（中文别名）、`TencentSansW3/W7`（无空格 PostScript 名）、`TTTGB Medium`、`Helvetica`、`PingFang SC`、`微软雅黑`。

**替换策略**：`replace_fonts_in_slide()` 遍历每个 text run 的 `a:latin / a:ea / a:cs`，按字号阈值统一替换。需递归处理组合形状（GroupShape）和表格单元格内的文本。

### 4.3 Logo 规范

Logo 位置按**页面类型**区分（基于模板 Layout XML 实测，**基准尺寸 20.02"×11.26"**）：

| 页面类型 | 文件 | 位置 | 尺寸 |
| --- | --- | --- | --- |
| 封面页/章节扉页/结尾页 | `logo-main.png` | **左上角** x=0.65" y=0.61" | 4.88" x 0.53" |
| 内容页 | `logo-main.png` | **右上角** x=14.60" y=0.49" | 4.88" x 0.53" |

Logo 铁律：位置锁死、保持宽高比、不可变色/描边/阴影/旋转、不可被遮挡。

**实现方式**：`add_logo(slide, page_type, slide_w, slide_h, ...)` 函数，根据 `page_type` 决定位置，**按输入 PPT 实际尺寸等比缩放**（`scale = slide_w / Inches(20.02)`），插入前通过 `_logo_already_exists()` 去重检测。

> ⚠️ **常见 BUG**：如果 `add_logo` 不按输入 PPT 尺寸缩放而直接硬编码 `Inches(14.60)`，当输入 PPT 尺寸与模板不一致时（例如 PptxGenJS 默认 10"×5.625"），内容页 Logo 会飞出右边界。修复方法：所有坐标和尺寸均乘以 `slide_w / Inches(TEMPLATE_W_INCH)` 缩放因子。

### 4.4 配色规范

模板背景是米黄底+红色城市线稿，需要安全调色板避免撞色。

#### 主色（Brand Core）

| HEX | 用途 |
| --- | --- |
| `#D80C01` | 品牌红（主标题、强调、CTA） |
| `#FF0000` | 品牌红亮（高亮、警示） |
| `#000000` | 经典黑 |
| `#222222` | 深灰文字（正文） |
| `#666666` / `#888888` | 中灰 / 浅灰 |
| `#FFFFFF` | 纯白（卡片底） |
| `#FAF6EE` | 米白（与模板同色系） |
| `#E7E6E6` | 浅边线灰 |

#### 辅助色（Accent，最多取 2 个，暖色优先）

> ⚠️ `#08194B` 深蓝已移入禁用色，不再作为辅助色使用。内容色块必须优先选暖色系。

| HEX | 用途 |
| --- | --- |
| `#FAD16A` | 暖淡黄（多系列对比，首选暖色） |
| `#F19D19` | 提示金（警告、过渡步骤） |
| `#1D6FA9` | 商务蓝（仅数据系列/流程图，非色块） |
| `#4A5D52` | 高级灰绿（中性图表配色） |

#### 暖色调内容色块（扩展）

珊瑚粉 `#E8A090`、暖杏色 `#D4A574`、浅金橙 `#E8B84A`、玫瑰木 `#C4A484`、浅赭色 `#D49A6A`。单页最多 3 种，文字仅用黑/白/品牌红。

#### 文字与色块对比度规则（强制）

> ⚠️ **禁止同色系文字放在同色系色块上**——文字必须与其直接背景有足够对比度。

| 色块背景色 | 允许的文字色 | 禁止的文字色 |
| --- | --- | --- |
| 品牌红 `#D80C01` / `#FF0000` / 红色半透明 | **白色 `#FFFFFF`** | ❌ 红色（红字红底完全不可读） |
| 暖杏色 `#D4A574` / 暖色系色块 | **白色 `#FFFFFF`** 或 **深灰 `#222222`** | ❌ 同色系暖色 |
| 白色 / 米白 `#FAF6EE` | **深灰 `#222222`** 或 **品牌红 `#D80C01`** | ❌ 白色、浅灰 |
| 深色（`#222222` / `#000000`） | **白色 `#FFFFFF`** | ❌ 深色 |

**常见 BUG（已修复）**：使用红色半透明色块（`fill: brandRed, transparency: 12-15%`）做强调条，同时文字也用品牌红——视觉上红字完全淹没在红色底中。修复方法：红色色块上的文字统一用白色 `#FFFFFF`。

#### 图表标准色板（按顺序取，最多 6 系列）

`#D80C01` → `#D4A574`（暖杏色）→ `#FAD16A` → `#666666` → `#1D6FA9` → `#F19D19`

#### 禁用色

`#08194B` 深蓝（已从品牌色移入）、蓝紫/紫色、鲜绿、青色/Teal、粉色/玫红、彩色渐变、玻璃拟态、霓虹色。

#### 配色合规实现

`scripts/apply_template.py` 中 `replace_colors_in_slide()` + `replace_theme_colors()` 实现：
- **CIEDE2000 色差算法**判断颜色是否为禁用色
- **禁用色黑名单**（14+ 条规则）命中时强制替换为最近品牌安全色
- **主题色覆写**：解析 theme XML 的 clrScheme，将禁用色槽直接覆写
- 默认启用 `--color-compliance`，可通过 CLI 关闭

### 4.5 背景可见性规范

| 规则 | 说明 |
| --- | --- |
| 禁止 | 整页大白卡（width > 10", height > 4" 不透明） |
| 推荐 | 分散小卡 + 卡片间 0.2-0.4" 间隙 |
| 推荐 | 半透明白色托盘（transparency 15-30%） |
| 推荐 | 标题直接放米黄底 + 左侧红色锚条 |
| 推荐 | 每页四周至少留 0.3" 无元素区 |

---

## 五、页面尺寸

模板实际尺寸（通过解析 XML 实测）：
- **EMU**: `cx=18305463, cy=10296525`
- **Inch**: 约 20.02 x 11.26 inch
- **宽高比**: 16:9

脚本读取 `pres.slide_width` / `pres.slide_height` 获取实际值，不硬编码。

---

## 六、统一入口（自动格式识别）

**★ 核心设计：一个入口 `apply_template.py`，根据 `--input` 文件扩展名自动路由。**

```
python scripts/apply_template.py --input <任意格式文件> --output <out.pptx> [选项...]
```

| 输入格式 | 扩展名 | 路由管线 | 说明 |
| --- | --- | --- | --- |
| PPTX | `.pptx` | 迁移适配 | 保留内容，替换品牌四件套 |
| HTML | `.html` `.htm` `.xhtml` | HTML→PPT | 解析结构，从零生成 |
| Markdown | `.md` `.markdown` `.mdown` | MD→HTML→PPT | 先转 HTML 再生成 |

### 模式 A：从零生成 PPT（模板优先）

```
[输入：主题 + 大纲]  →  调用上游 Skill 生成内容稿  →  apply_template.py --input out.pptx 适配  →  输出 .pptx
```

### 模式 B：迁移已有 PPT（内容优先）

```
[输入：原始 .pptx]  →  apply_template.py --input guest.pptx --mode full  →  输出适配后 .pptx + 适配报告
```

### 模式 C：HTML/Markdown 转 PPT（自动路由）

```
[输入：.html / .md]  →  apply_template.py --input article.html  →  直接输出品牌合规 .pptx
```

**支持的 HTML 元素映射（v2 增强版）：**

| HTML 元素 | PPT 呈现 |
| --- | --- |
| `<h1>` | 章节扇页（bg-cover 背景） |
| `<h2>` | 内容页标题（40pt TencentSans W7） |
| `<h3>`/`<h4>` | 内容页副标题（22-28pt TencentSans W7） |
| `<p>` | 正文段落（20pt TencentSans W3） |
| `<ul>`/`<ol>` | 列表（支持嵌套, 20pt TencentSans W3） |
| `<table>` | 表格页（暖杏色表头+白色数据行） |
| `<pre><code>` | 代码块页（深色圆角背景+等宽字体 16pt） |
| `<img>` | 图片页（居中展示） |
| `<blockquote>` | 引用框（米白底+左侧红色锚条, 20pt W3） |
| `.card-row` / `.card` | 卡片布局（标题26pt W7 / 正文20pt W3 / 标签16pt W7） |
| `.two-col` / `.col` | 双栏布局（列标题28pt W7 / 内嵌卡片24pt+20pt / 列表20pt W3） |
| `.flow-row` / `.flow-step` | 流程图（步骤22pt W7 / 箭头28pt 品牌红） |
| `.highlight-box` | 高亮框（20pt W3 + 左侧红色锚条） |
| `.prob-row` / `.prob-bar` | 概率条形图（模拟token概率分布可视化） |
| `.info-card` | 信息卡片（20pt 标题 + 16pt 正文） |
| `.gpt-letters` | 大字展示（120pt 品牌色大字） |
| inline-style flex容器 | 自动识别并渲染为卡片布局（28pt 标题 + 20pt 描述） |
| `.policy-grid` / `.policy-card` | 策略对比卡片（emoji 42pt / label 28pt W7 / desc 20pt W3） |
| `.summary-grid` / `.summary-card` | 总结网格卡片 |

**字体大小标准（锁死规范，基于 20 英寸宽幅面）：**
- 页面主标题：**40pt**（章节页 **48pt**）TencentSans W7
- 编号（section-num）：**18pt** TencentSans W7
- 副标题：**22pt** TencentSans W3
- 卡片标题：**26pt** TencentSans W7
- 列标题（双栏）：**28pt** TencentSans W7
- 正文 / 卡片正文：**20pt** TencentSans W3
- 列表项：**20pt** TencentSans W3
- 流程图步骤：**22pt** TencentSans W7
- 流程图箭头：**28pt** 品牌红
- 高亮框文字：**20pt** TencentSans W3
- 策略对比 Emoji：**42pt**
- 策略对比 Label：**28pt** TencentSans W7
- 策略对比 描述/who：**20pt** TencentSans W3
- 标签 / 脚注：14-16pt TencentSans W7
- 代码块：14-16pt 保留等宽字体

> ⚠️ 以上为 20 英寸（模板实际宽度 20.02"）幅面下的字号。若 PPT 宽度不同，按 `scale = actual_width / 10` 比例调整。

**支持的输入来源：**
- 普通 HTML 文件
- Markdown 文件（需安装 `pip install markdown`）
- 网页文章/博客
- Jupyter Notebook 导出的 HTML

**智能特性：**
- 自动从 `<title>` 或第一个 `<h1>` 提取标题
- 智能分页（避免单页过满）
- 表格/代码块/图片自动独立成页
- 封面+结尾页自动生成
- 所有页面直接品牌合规（字体/配色/背景/Logo）

**迁移铁律**：统一使用 `--mode full`。不允许以"原 PPT 是深色背景"为由切换 `light` 模式绕过背景替换。深色背景撞色时应调整内容配色，而非绕过。

| 适配深度 | 使用场景 | 改动范围 |
| --- | --- | --- |
| `--mode full`（默认） | 所有迁移场景 | 背景 + 字体 + Logo + 配色合规 |
| `--mode light` | 仅限用户明确要求保留原背景 | 字体 + Logo + 配色合规 |
| `--mode logo-only` | 仅补 Logo（极少使用） | 仅 Logo |

---

## 七、执行步骤

1. **确认意图**：从零生成（模式 A）、迁移 PPT（模式 B）、还是 HTML/MD 转 PPT（模式 C）。
2. **校验资产**：检查 backgrounds/、logos/、fonts/ 是否齐全。
3. **准备内容**：模式 A 调用上游 Skill；模式 B/C 直接提供输入文件。
4. **运行适配**（统一入口，自动识别格式）：
   ```bash
   # PPTX 迁移
   python scripts/apply_template.py --input guest.pptx --output out.pptx --mode full

   # HTML 转 PPT
   python scripts/apply_template.py --input article.html --output out.pptx --title "标题" --author "讲师"

   # Markdown 转 PPT
   python scripts/apply_template.py --input notes.md --output out.pptx --title "标题"
   ```
5. **检查报告**：查看适配报告中的 warnings。
6. **输出**：`<原文件名>-tpl-adapted.pptx` + 适配报告。

---

## 八、质量检查清单（输出前必跑）

- [ ] 每页使用正确背景（封面=bg-cover，内容=bg-content）
- [ ] 所有文本字体为 `TencentSans W3` / `TencentSans W7`
- [ ] Logo 封面/扉页/结尾页在左上角 (0.65, 0.61, 4.88, 0.53)
- [ ] Logo 内容页在右上角 (14.60, 0.49, 4.88, 0.53)
- [ ] Logo 保持宽高比，未变形
- [ ] 完整保留原 PPT 的文本、图片、图表、表格
- [ ] 未引入无关品牌 Logo/水印
- [ ] 所有文字字号 >= 12pt
- [ ] 配色在安全调色板范围内，无禁用色残留
- [ ] Logo 安全区（0-3.1" x 0-0.5"）未被内容侵入
- [ ] 模板背景在每页可见（卡片间隙或四周可见米黄底+城市线稿）

---

## 九、脚本说明

| 脚本 | 用途 | 关键函数 |
| --- | --- | --- |
| `apply_template.py` | **统一入口 v8**（自动路由：PPTX迁移 / HTML生成 / MD生成） | `main()`, `_detect_input_format()`, `_run_html_pipeline()`, `adapt()` |
| `html_to_pptx.py` | HTML→PPTX 核心模块（被 apply_template.py 自动调用） | `parse_html()`, `PptxGenerator.generate()`, `_paginate_content()` |
| `verify_output.py` | **输出验证**（shapes/字号/Logo/背景/页数对比） | `main()` — 退出码 0=通过 1=警告 2=错误 |
| `extract_template_assets.py` | 从城市模板提取背景/Logo | `classify_background()`, `is_logo()` |
| `brand_palette.py` | 配色辅助（校验/prompt 生成） | `validate_color()`, `get_prompt()` |
| `test_v5.py` | 42 项自动化测试 | unittest 套件 |

调用示例（统一入口，自动识别格式）：

```bash
# ★ 所有格式都用 apply_template.py，自动识别 ★

# PPTX → 迁移适配
python scripts/apply_template.py --input guest.pptx --output guest-adapted.pptx

# HTML → 品牌合规 PPT
python scripts/apply_template.py --input article.html --output output.pptx --title "标题" --author "讲师"

# Markdown → 品牌合规 PPT
python scripts/apply_template.py --input notes.md --output output.pptx --title "标题"

# 预览（不写入，仅 PPTX 模式）
python scripts/apply_template.py --input guest.pptx --output /tmp/out.pptx --dry-run

# 提取新城市模板资产
python scripts/extract_template_assets.py --pptx "成都模板.pptx" --city chengdu

# 校验颜色是否安全
python scripts/brand_palette.py --validate "#7B61FF"

# ★ 输出验证（生成后必跑）
python scripts/verify_output.py --pptx output.pptx --html source.html --strict
```

依赖：`pip install python-pptx Pillow beautifulsoup4 lxml`
可选：`pip install markdown`（Markdown 支持）

---

## 十、AI 思考优先级：预对齐工作流（与上游 Skill 协作时强制执行）

### 核心原则

**先注入，后生成，最后轻量适配。** 不要让适配脚本做本应在生成阶段就能避免的纠偏工作。

### 三步思考法

```
┌─────────────────────────────────────────────────────────────────┐
│  Step 1: 读取本 Skill §4 品牌规范 + §12 上游协作指令              │
│          ↓ 提取安全调色板、禁用色列表、背景可见性约束              │
│                                                                  │
│  Step 2: 将约束直接嵌入上游生成逻辑（颜色常量、布局规则）           │
│          ↓ 生成阶段即产出合规内容，零禁用色                        │
│                                                                  │
│  Step 3: 适配脚本收尾——背景图铺底 + 字体替换 + Logo + theme覆写    │
│          ↓ 色块颜色替换次数应趋近于 0                             │
└─────────────────────────────────────────────────────────────────┘
```

### 实操对比：两次真实生成结果

| 指标 | 随手配色（浪费型） | 预对齐配色（推荐） |
|---|---|---|
| 生成前是否读 §4.4 安全调色板 | ❌ 否 | ✅ 是 |
| 覆盖/章节页背景色 | #08194B 深蓝（禁用） | #D80C01 品牌红 / #D4A574 暖杏 |
| 图表色板 | #D80C01, #08194B, #FAD16A, ... | #D80C01, #D4A574, #FAD16A, #666666, #1D6FA9, #F19D19 |
| 步骤色阶 | 深蓝→商务蓝→黄→金→红 | 暖杏→珊瑚粉→暖黄→金→红 |
| 表格表头底色 | #08194B 深蓝 | #D4A574 暖杏 |
| 生成后适配脚本色块替换 | **21 次** | **9 次**（全部为 theme schema 层覆写，非用户色块） |
| 禁用色 #08194B 残留 | **12 处**（依赖脚本纠偏） | **0 处** |
| 封面/章节/结尾页文字色 | 白色（模板背景浅，不可读） | #222222 深灰（可读） |
| 封面/章节/结尾页 slide.background | 设了纯色（底色透出） | **不设**（保持透明） |
| 封面/章节/结尾页左侧全高红色条块 | 有（与模板背景叠加干扰） | **无**（模板自带设计元素） |
| 红色色块上的文字色 | 红色（红字红底不可读） | **白色**（高对比度可读） |

### 代码层面的具体做法

生成脚本的配色常量应直接从本 Skill 的安全调色板搬运，不做二次创作：

```js
// ✅ 预对齐：直接从 §4.4 搬运
const C = {
  brandRed: "D80C01",       // 品牌红
  darkText: "222222",        // 深灰（§4.1 安全色，替代被禁的 #08194B）
  warmApricot: "D4A574",    // 暖杏色（§4.4 暖色色块首选——封面/章节页背景）
  coralPink: "E8A090",      // 珊瑚粉（§4.4 暖色色块）
  warmYellow: "FAD16A",     // 暖淡黄（§4.4 辅助色首选）
  gold: "F19D19",            // 提示金（§4.4 辅助色）
  lightGold: "E8B84A",      // 浅金橙（§4.4 暖色色块）
  // ... 其余全部来自 §4.4
};
// 图表色板严格按 §4.4 顺序
const chartColors = ["D80C01", "D4A574", "FAD16A", "666666", "1D6FA9", "F19D19"];
```

```python
# ❌ 浪费型：自己编颜色，等适配脚本擦屁股
darkBlue = "08194B"     # 根本没查规范，用了禁用色
```

### 适配脚本只需做这些（不应额外增加工作）

| 适配项 | 是否可由生成阶段避免 |
|---|---|
| 背景图铺底 | ❌ 不可（模板图片路径只有脚本知道） |
| 字体 TencentSans 替换 | ❌ 不可（字体安装路径不同，统一替换最可靠） |
| Logo 定位插入 | ❌ 不可（尺寸/位置由模板决定 + **必须按输入PPT尺寸等比缩放**） |
| 主题色 schema 覆写 | ❌ 不可（OOXML 主题色槽结构性差异） |
| **用户色块颜色纠偏** | ✅ 可通过预对齐完全避免 |

---

## 十一、与其他 PPT Skill 的协作

| 阶段 | 推荐 Skill | 职责 |
| --- | --- | --- |
| 1. 读取约束 | 本 Skill §4 + §12 | 提取安全调色板、禁用色、背景可见性要求 |
| 2. 内容创作 | course-ppt-generator / illustrated-ppt-generator / baoyu-slide-deck / PptxGenJS | 大纲、文案、图文——**已将约束嵌入生成逻辑** |
| 3. 模板适配（最后一步） | 本 Skill scripts/apply_template.py | 背景图 + 字体 + Logo + theme覆写——**不应再做用户色块纠偏** |

调用上游 Skill 前必须注入配色 + 背景可见性约束（通过 `brand_palette.py --prompt` 一键生成）。

> **Fallback**：如上游 Skill 不可用或未安装，可直接使用模式 C（HTML→PPT）绕过上游依赖——本 Skill 的 `html_to_pptx.py` 可独立完成内容结构化 + 品牌适配，无需其他 Skill 协助。

---

## 十二、上游 Skill 协作指令（必须注入）

```
配色约束（强制）：
- 主色：#D80C01（品牌红）、#000000、#FFFFFF、#222222
- 辅助色（≤2种，优先暖色系）：#FAD16A（暖淡黄，首选）、#F19D19（提示金）、#1D6FA9（商务蓝，仅数据系列/流程图）
- 深蓝 #08194B 已弃用为禁用色，禁止用作色块/卡片背景
- 暖色调色块（优先使用，最多 3 种）：#E8A090、#D4A574、#E8B84A、#C4A484、#D49A6A
- 图表按标准色板：#D80C01 → #D4A574（暖杏色）→ #FAD16A → #666666 → #1D6FA9 → #F19D19
- 数据卡片：暖杏色 #D4A574 底 + #FFFFFF 字（替代原 #08194B 深蓝）
- 禁用：深蓝（含 #08194B）、蓝紫、绿色、青色、粉色、彩色渐变、玻璃拟态、霓虹色
- 卡片不透明度 >= 95%
- 色块面积 > 30% 时必须使用安全色

背景可见性约束（强制）：
- 不要给 slide 设置背景色（保持透明让模板背景透出）
- 不要使用撑满整页（>10" 宽 + >4" 高）的不透明大白卡
- 内容容器优先半透明白色托盘（不透明度 70-85%）
- 卡片间留 0.2-0.4" 间隙
- 每页四周至少留 0.3" 无元素安全区
- 标题直接放米黄底 + 左侧 0.1" 红色锚条
- ⚠️ 封面/章节扉页/结尾页文字必须用深色（#222222 或 #000000），禁止白色/浅灰（模板背景为浅色米黄底，浅色文字完全不可读）
- ⚠️ 封面/章节扉页/结尾页不要设 slide.background（保持透明让适配脚本的 bg-cover.jpeg 完整覆盖，不留底色透出）
- ⚠️ 封面/章节扉页/结尾页不要添加全高装饰条块（模板背景图 bg-cover.jpeg 自带红色城市线稿设计元素，额外条块会叠加产生视觉干扰）
- ⚠️ 红色色块（`#D80C01`/`#FF0000`/红色半透明）上的文字必须用白色 `#FFFFFF`，禁止用红色文字（红字红底完全不可读）。同理，任何色块上的文字色必须与色块背景形成足够对比度
```

---

## 十三、HTML→PPT 迁移经验库（35 条，含完整代码示例）

> ⚠️ **这是从实际迁移失败中提炼的铁律，每条都带代码。执行 HTML→PPT 迁移时必须逐条遵守。**
> 配合 §十五 Checklist 执行。

---

### 第一部分：渲染逻辑（§13.1~13.10）

#### 13.1 elif 链互斥导致结构丢失

**问题**：`_add_structured_slide()` 中如果使用 `elif` 链处理多种结构类型（cards / columns / policy_cards / summary_cards），那么**同一页面**有多种结构时只渲染第一种命中的，后续全部丢失。

**典型表现**：Slide 12 同时有 `cards` + `policy_cards` + `highlights`，但 elif 链命中 cards 后 policy_cards 被跳过。

**修复铁律**：所有结构类型渲染必须使用**独立 if 块**，不用 elif：

```python
# ✅ 正确：独立 if 块，允许共存
if sc.highlights:
    for hl_text in sc.highlights:
        y_cursor = self._render_highlight_box(slide, hl_text, y_cursor)
if sc.cards:
    y_cursor = self._render_cards(slide, sc.cards, y_cursor)
if sc.columns:
    y_cursor = self._render_columns(slide, sc.columns, y_cursor)
if sc.policy_cards:
    y_cursor = self._render_policy_grid(slide, sc.policy_cards, y_cursor)
if sc.summary_cards:
    y_cursor = self._render_summary_grid(slide, sc.summary_cards, y_cursor)

# ❌ 错误：elif 链
if sc.cards:
    y_cursor = self._render_cards(...)
elif sc.columns:            # ← cards 存在时 columns 永远跳过
    y_cursor = self._render_columns(...)
elif sc.policy_cards:       # ← 永远不会执行
    y_cursor = self._render_policy_grid(...)
```

#### 13.2 渲染顺序：高亮框置顶

**问题**：某些页面的高亮框（highlight-box）是**页面顶部的定义框**（如"策略 (Policy) = 大模型本身"），应该在卡片/双栏之前渲染，而不是放在最后。

**修复**：渲染顺序固定为：

```
高亮框 → GPT大字/Flex → 卡片 → 双栏 → 策略对比 → 总结网格 → 剩余文本 → 流程图 → 概率图 → 信息卡
```

#### 13.3 双栏内 card 的文本重复提取

**问题**：双栏 (`.two-col > .col`) 内嵌套了 `.card`，而 card 内部有 `.col-text`。如果双栏提取时不排除在 card 内的元素，`col-text` 的文本会被同时提取到 `col_data['text']` 和 `card_data['body']` 中，造成重复。

**修复**：

```python
# 提取 col-text 时排除在 card 内的
for ct_elem in col.find_all(class_='col-text'):
    if ct_elem.find_parent(class_='card'):
        continue  # card 内的已由 _extract_card_data 处理
    col_data['text'] = _clean_html_text(ct_elem)

# 提取 col-list 时同理
for col_list in col.find_all(class_='col-list'):
    if col_list.find_parent(class_='card'):
        continue

# 提取 highlight-box 时同理
for hb in col.find_all(class_='highlight-box'):
    if hb.find_parent(class_='card'):
        continue
```

#### 13.4 卡片风格检测不完整（inline-style 兜底）

**问题**：`_extract_card_data()` 只检测 `class` 名（如 `accent` / `blue`），但很多 HTML 用 `style="border-color:var(--red)"` 或 `style="border-color:var(--accent)"` 来标记风格，导致所有卡片都被判为 `default` 风格。

**修复**：class 检测优先，inline-style 兜底：

```python
card_inline_style = card.get('style', '')
if 'accent' in card_classes:
    card_data['style'] = 'accent'
elif 'blue' in card_classes:
    card_data['style'] = 'blue'
# inline-style 兜底
elif 'red' in card_inline_style or '--red' in card_inline_style or '--accent' in card_inline_style:
    card_data['style'] = 'accent'
elif '--blue' in card_inline_style:
    card_data['style'] = 'blue'
else:
    card_data['style'] = 'default'
```

#### 13.5 policy_card 的 emoji 提取

**问题**：策略对比卡片（`.policy-card`）中的大 emoji（如 👦→👦）放在 `font-size:42px` 的 div 中，如果不专门提取，emoji 会丢失或被合并到描述文本中。

**修复**：在解析 policy_card 时，遍历直接子 div，检测 inline-style 中的大字号：

```python
pdata['emoji'] = ''
for d in pc.find_all('div', recursive=False):
    style = d.get('style', '').replace(' ', '')
    if 'font-size:42px' in style or 'font-size:48px' in style:
        pdata['emoji'] = d.get_text(strip=True)
        break
```

渲染时 emoji 用 42pt，label 用 28pt W7 粗体。

#### 13.6 _extract_card_data 的多路径 body 提取与去重

**问题**：卡片结构多样（有 `.card-body`、有 `.col-text`、有 `.col-list`、有纯文本），单一提取路径无法覆盖所有情况。同时如果全文 fallback 提取包含了标题文本，会导致 body 与 title 重复。

**修复**：多路径 fallback + 去重：

```python
# 路径1: card-body
card_data['body'] = _clean_html_text(cb) if cb else ''

# 路径2: col-text（卡片内嵌套的正文块）
if not card_data['body']:
    col_text = card.find(class_='col-text')
    if col_text:
        card_data['body'] = _clean_html_text(col_text)

# 路径3: col-list（卡片内嵌套的列表）
if not card_data['body']:
    col_list = card.find(class_='col-list')
    if col_list:
        items = [li.get_text(strip=True) for li in col_list.find_all('li')]
        card_data['body'] = '\n'.join(f'* {item}' for item in items)

# 路径4: 无标题无正文时 fallback 全文
if not card_data['body'] and not card_data['title']:
    card_data['body'] = _clean_html_text(card)

# 去重：body 以 title 开头时截掉重复部分
if card_data['title'] and card_data['body'] and card_data['body'].startswith(card_data['title']):
    remaining = card_data['body'][len(card_data['title']):].strip()
    if remaining:
        card_data['body'] = remaining
```

#### 13.7 双栏渲染时 cards 优先级

**问题**：双栏内同时有 `cards` + `items` + `text`，如果用 `if not items and not text:` 作为 cards 渲染条件，cards 会被跳过。

**修复**：cards 始终优先渲染（用 `if col.get('cards'):`），后续 items/text 用 `elif` 互斥（与 cards 不互斥）：

```python
# 优先渲染内部卡片
if col.get('cards'):
    for cc in col['cards'][:2]:
        # 渲染卡片标题+正文...

# 列表项（仅在无 cards 时）
elif col.get('items'):
    ...

# 正文（仅在无 cards 也无 items 时）
elif col.get('text'):
    ...
```

#### 13.8 双栏背景色跟随卡片风格

**问题**：双栏的列框（`col`）始终用默认米白色，即使内部卡片是 accent（红色）风格，视觉上没有区分度。

**修复**：列框背景色根据第一个内部 card 的 style 设置：

```python
col_fill_color = COLOR_CREAM
col_line_color = COLOR_LINE_GRAY
if col.get('cards'):
    first_card_style = col['cards'][0].get('style', 'default')
    if first_card_style == 'accent':
        col_fill_color = RGBColor(0xFE, 0xF5, 0xEB)  # 暖橙底
        col_line_color = COLOR_BRAND_RED               # 红边框
    elif first_card_style == 'blue':
        col_fill_color = RGBColor(0xEB, 0xF5, 0xFF)  # 淡蓝底
        col_line_color = RGBColor(0x4A, 0x90, 0xD9)  # 蓝边框
```

#### 13.9 字体按 PPT 幅面比例放大

**问题**：PPT 为 20 英寸宽幅面，如果字号按标准 10 英寸屏幕规格设置（如标题 36pt），在 20 英寸幅面上视觉偏小。

**修复规则**：当 PPT 实际宽度超过 16 英寸时，按 `scale = actual_width / 10` 比例放大。20 英寸即放大 1 档（约 +2~4pt）。具体数值参见 §六字体大小标准表。

#### 13.10 独立 card 与 two-col 内 card 的去重

**问题**：页面提取独立 card（不在 card-row 内）时，如果不排除在 two-col 内的 card，会导致双栏内的卡片被**重复提取**到 `sc.cards` 和 `sc.columns[x]['cards']` 两处。

**修复**：

```python
# 提取独立 card 时排除在 two-col 内的
standalone_cards = slide_elem.find_all(class_='card', recursive=True)
two_col_elem = slide_elem.find(class_='two-col')
for card in standalone_cards:
    if two_col_elem and card.find_parent(class_='two-col'):
        continue  # 归双栏处理，不重复提取
    sc.cards.append(_extract_card_data(card))
```

---

### 第二部分：架构设计（§13.11~13.20）

#### 13.11 幻灯片型 HTML vs 文章型 HTML 的自动检测

**问题**：输入 HTML 可能是两种完全不同的结构——幻灯片型（每个 `div.slide` 是一页）和文章型（连续 h1/h2/p/ul 流式内容）。如果不检测就用错解析器，输出完全混乱。

**修复**：入口处先用 `is_slide_deck_html()` 检测，满足条件走 `parse_html_slides()`，否则走 `parse_html()` + 智能分页：

```python
def is_slide_deck_html(html_content: str) -> bool:
    """存在 3 个以上 div.slide / div[data-slide] / section.slide -> 幻灯片型"""
    soup = BeautifulSoup(html_content, 'lxml')
    slides = soup.find_all('div', class_=re.compile(r'\bslide\b'))
    if len(slides) >= 3:
        return True
    slides_by_attr = soup.find_all('div', attrs={'data-slide': True})
    if len(slides_by_attr) >= 3:
        return True
    slides_section = soup.find_all('section', class_=re.compile(r'\bslide\b'))
    return len(slides_section) >= 3
```

#### 13.12 页面类型自动判定规则

**问题**：`SlideContent.slide_type` 必须正确判定为 cover/section/content/end，否则背景图和 Logo 位置全部错误。

**修复**：检测规则：

| 条件 | 判定为 |
|---|---|
| class 含 `title-page` 或 `slide-title` | `cover` |
| class 含 `slide-center` + 文本含"谢谢/thanks" | `end` |
| class 含 `slide-center` + 无"谢谢" | `section` |
| 无结构化内容 + 仅有标题 + 无副标题 | `section`（退化判定） |
| 其余情况 | `content` |

#### 13.13 智能分页常量（文章型 HTML）

**问题**：文章型 HTML 内容量不固定，如果不分页会在一页上堆满文字。

**修复**：设定分页阈值，超出自动拆为新页：

```python
MAX_LINES_PER_SLIDE = 12        # 段落型内容最大行数
MAX_LIST_ITEMS_PER_SLIDE = 10   # 列表项最大条数
MAX_TABLE_ROWS_PER_SLIDE = 8    # 表格行最大数
```

表格/代码块/图片始终独立成页（不与其他内容共享页面）。

#### 13.14 内容区域安全边距

**问题**：不遵守安全边距会导致内容侵入 Logo 区域或溢出页面。

**修复**：20 英寸幅面下的内容安全区：

```python
CONTENT_LEFT   = Inches(1.0)    # 左边距
CONTENT_TOP    = Inches(1.5)    # 上边距（Logo 安全区下方）
CONTENT_WIDTH  = Inches(18.0)   # 可用宽度
CONTENT_HEIGHT = Inches(9.0)    # 可用高度（页底留 0.7"）
```

y_cursor 超过 `Inches(9.0~9.5)` 时必须停止添加新元素或换页。

#### 13.15 概率图与 info-card 的层级关系

**问题**：HTML 中 `.info-card` 可能是概率图的外部容器（包含 `.prob-row`），如果不排除，概率图容器会被重复提取为信息卡片。

**修复**：提取 info-card 时检查内部是否包含 prob-row，有则跳过：

```python
for ic in info_cards:
    if ic.find(class_='prob-row'):
        continue  # 这是概率图的容器，不重复提取
    # 正常提取 info-card 数据...
```

#### 13.16 GPT 大字 + Flex 解释块的级联提取

**问题**：`.gpt-letters` 的大字下方通常跟着一个 `display:flex` 的解释块（3~4 个图标+标题+描述的组合）。如果只提取大字不提取 flex 块，信息不完整。

**修复**：在提取 gpt_letters 后，向上找 parent，在同级兄弟中检测 `display:flex` inline-style 的 div，逐个提取子项的 icon/title/desc：

```python
# flex 子项识别规则：
# font-size:52px -> icon（大emoji）
# font-weight:800 / font-bold -> title
# font-size:19px -> desc（描述文字）
```

#### 13.17 独立 card 提取的完整优先级链

**问题**：卡片分布在多种容器中（card-row / standalone / two-col），提取顺序不对会重复或遗漏。

**修复**：三级提取链：

```
1. card-row 内的 card -> 全部收入 sc.cards（最高优先级）
2. 无 card-row 时：standalone card -> 排除在 two-col 内的 -> 收入 sc.cards
3. two-col > col 内的 card -> 收入 sc.columns[x]['cards']（归双栏管理）
```

**注意**：第 1、2 步是互斥的（`if not card_rows:` 才走 standalone 提取），避免 card-row 内的 card 被重复提取。

#### 13.18 封面页 author 信息提取

**问题**：封面页的作者信息格式多样（如"张三 | 腾讯云架构师"），如果用固定 class 提取会漏掉。

**修复**：在封面页中遍历所有 div，满足「含'|'且长度<100」的文本视为作者信息：

```python
if sc.slide_type == 'cover':
    for div in slide_elem.find_all('div', recursive=True):
        text = div.get_text(strip=True)
        if '|' in text and len(text) < 100:
            sc.author = text
            break
```

#### 13.19 剩余文本块只在无结构化内容时收集

**问题**：如果页面已有 cards/columns/policy_cards 等结构化内容，再收集 `raw_text_blocks` 会导致大量噪音文本（如 card 内的文字被重复提取到 raw_text_blocks）。

**修复**：双重门控——提取时 `if not has_structured:` 才收集，渲染时 `if not has_main_content:` 才输出：

```python
# 提取阶段
has_structured = (sc.cards or sc.columns or sc.summary_cards or sc.policy_cards
                 or sc.prob_charts or sc.info_cards or sc.gpt_letters
                 or sc.inline_flex_blocks)
if not has_structured:
    # 才收集剩余文本...

# 渲染阶段
has_main_content = (sc.cards or sc.columns or sc.policy_cards or
                   sc.summary_cards or sc.gpt_letters or sc.inline_flex_blocks)
if sc.raw_text_blocks and not has_main_content:
    # 才渲染剩余文本...
```

#### 13.20 表格/代码块/引用框的渲染规范

**HTML 表格 -> PPT 表格**：
- 表头行：暖杏色 `#D4A574` 底 + 白色文字 20pt W7
- 数据行：白色底 + 深灰文字 18pt W3
- 自动独立成页（不与其他内容混排）
- 超过 8 行自动分页

**代码块 -> PPT 代码框**：
- 深色圆角背景（`#2D2D2D`）
- 等宽字体 14-16pt JetBrains Mono
- 白色文字
- 自动独立成页

**引用框 -> PPT 引用**：
- 米白底 + 左侧红色锚条（与 highlight-box 相同视觉规范）
- 正文 20pt W3

---

### 第三部分：python-pptx 底层操作坑（§13.21~13.26）

#### 13.21 python-pptx 中文字体必须手动设置 `a:ea` XML

**问题**：python-pptx 的 `run.font.name = "TencentSans W7"` 只写入 `a:latin` 属性，中文字符不会使用该字体（PowerPoint 对中文走 `a:ea` 属性）。结果：标题显示英文用 TencentSans，中文用宋体/黑体。

**修复**：每次设置字体时，必须同时写 `a:ea` 和 `a:latin`：

```python
from pptx.oxml.ns import qn
from lxml import etree

def _set_font(run, font_name, size_pt, bold=False, color=None):
    """设置字体 - 必须同时处理 latin + ea"""
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    if color:
        run.font.color.rgb = color
    # 必须手动操作 XML 设置中文字体
    rPr = run._r.get_or_add_rPr()
    # 设置 a:latin（西文）
    latin = rPr.find(qn('a:latin'))
    if latin is None:
        latin = etree.SubElement(rPr, qn('a:latin'))
    latin.set('typeface', font_name)
    # 设置 a:ea（东亚/中文）- 关键！
    ea = rPr.find(qn('a:ea'))
    if ea is None:
        ea = etree.SubElement(rPr, qn('a:ea'))
    ea.set('typeface', font_name)
```

**铁律**：代码中**禁止**出现只写 `run.font.name` 不操作 XML 的情况。全局搜索 `run.font.name` 确认无遗漏。

#### 13.22 背景图 z-order 必须手动调整为最底层

**问题**：`slide.shapes.add_picture()` 默认把新图片放在 spTree 末尾（z-order 最顶层），背景图会遮盖所有内容。

**修复**：添加背景图后立刻移到 spTree 最前面：

```python
pic = slide.shapes.add_picture(bg_path, 0, 0, SLIDE_WIDTH_EMU, SLIDE_HEIGHT_EMU)
sp_tree = slide.shapes._spTree
pic_elem = pic._element
sp_tree.remove(pic_elem)
sp_tree.insert(2, pic_elem)  # index 2 = 在 nvGrpSpPr(0) 和 grpSpPr(1) 之后
```

**注意**：`insert(0)` 或 `insert(1)` 会破坏 spTree 必要的头元素，必须从 index 2 开始。

#### 13.23 卡片/列框动态高度计算与剩余空间约束

**问题**：卡片高度固定（如一律 3.5 英寸）导致两个问题——内容多时截断、内容少时浪费空间、多卡片累计超出页面。

**修复**：动态计算 + 安全上限 + 剩余空间兜底：

```python
# 1. 基于内容行数动态计算
max_body_lines = max(len(card['body'].split('\n')) for card in cards) if cards else 3
card_height = Inches(min(max(3.5, max_body_lines * 0.45 + 2.0), 6.0))

# 2. 不得超过剩余可用空间
available = Inches(9.5) - y_cursor
card_height = min(card_height, available)

# 3. 如果剩余空间不足最小卡片高度（2 英寸），跳过渲染（不溢出）
if available < Inches(2.0):
    return y_cursor  # 放弃，留给下一页
```

#### 13.24 表格单元格背景色必须操作 XML

**问题**：python-pptx 的 `cell.fill.solid()` 在某些版本下不生效，或生成的 XML 格式不符合 PowerPoint 预期。

**修复**：直接操作 `tcPr` XML 节点：

```python
from pptx.oxml.ns import qn
from lxml import etree

def _set_cell_fill(cell, hex_color):
    """安全设置表格单元格背景色"""
    tcPr = cell._tc.get_or_add_tcPr()
    # 移除已有填充
    for old_fill in tcPr.findall(qn('a:solidFill')):
        tcPr.remove(old_fill)
    # 创建新填充
    solidFill = etree.SubElement(tcPr, qn('a:solidFill'))
    srgbClr = etree.SubElement(solidFill, qn('a:srgbClr'))
    srgbClr.set('val', hex_color)  # 如 'D4A574'
```

#### 13.25 圆角矩形 `adjustments[0]` 标准值表

**问题**：不同元素的圆角弧度不一致，凭感觉调导致视觉混乱。

**修复**：固定圆角值（`adjustments[0]` 值为 0~1 之间的比例）：

| 元素类型 | adjustments[0] | 视觉效果 |
|---|---|---|
| 内容卡片 / 列框 | **0.04** | 微圆角 |
| 高亮框 | **0.02** | 近直角 |
| 策略对比卡片 | **0.05** | 中等圆角 |
| 流程图步骤 | **0.10** | 明显圆角 |
| GPT 大字框 | **0.03** | 轻圆角 |

```python
shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ...)
shape.adjustments[0] = 0.04  # 按上表设置
```

#### 13.26 文章型 HTML 的「累积-刷新」分页模式

**问题**：§13.13 只提了分页阈值常量，但没有说明分页**架构设计**。如果不理解模式，新代码可能逐元素创建新页（浪费）或不分页（溢出）。

**修复**：`_paginate_content()` 使用累积-刷新（accumulate-flush）模式：

```
核心逻辑：
1. 维护一个 current_slide_content 缓冲区
2. 遍历 HTML 元素：
   a. 遇到 H1/H2 -> flush 当前缓冲区为一页 -> 新页开始
   b. 遇到 <table>/<pre>/<img> -> flush -> 该元素独立成页
   c. 遇到 <p>/<li> -> 累积到缓冲区
   d. 缓冲区行数超过 MAX_LINES_PER_SLIDE -> flush
3. 遍历结束 -> flush 剩余内容
```

**关键**：flush 触发点有 4 类——标题切换、重型元素、行数超限、遍历结束。漏掉任何一类都会导致内容堆积或切割不合理。

---

### 第四部分：高保真手动构建 HTML→PPT 的实战坑（§13.27~13.35）

> ⚠️ 以下经验来自 2026-06-11 迁移「深耕光电-数智无疆-AI重构美亚智造新范式.html」时的实际失误。
> 该 HTML 包含 scene-card / product-card / sales-flow / timeline / roadmap / question-card / kpi-row / stat-block 等自定义 CSS class，
> `html_to_pptx.py` 的自动映射无法识别这些结构，必须编写专用脚本逐页手动构建。

#### 13.27 自动脚本对自定义 CSS class 的致命盲区

**问题**：`html_to_pptx.py` 只识别有限的 CSS class（card / card-row / two-col / flow-row / highlight-box / prob-row / info-card / gpt-letters / policy-grid / summary-grid 等共约 16 种）。当 HTML 使用自定义 class 时（如 scene-card / sales-flow / sales-step / product-card / timeline / kpi-row / stat-block / roadmap / roadmap-phase / question-card / banner / grid-2 / grid-3 / compact-column），这些元素的内容**全部被跳过**，PPT 只剩纯文字堆砌。

**判断标准**：在运行自动脚本前，先扫描 HTML 中的所有 class，与 `html_to_pptx.py` 支持的 class 列表做交集。如果匹配率低于 60%，**直接放弃自动脚本**，改用手动逐页构建。

**自动扫描代码**：

```python
from bs4 import BeautifulSoup
import re

SUPPORTED_CLASSES = {
    'card', 'card-row', 'two-col', 'flow-row', 'highlight-box',
    'prob-row', 'info-card', 'gpt-letters', 'policy-grid',
    'summary-grid', 'slide', 'title-page', 'slide-center',
    'col-text', 'col-list', 'col'
}

def scan_html_class_coverage(html_content: str) -> float:
    """返回 HTML class 与自动脚本支持 class 的匹配率 (0~1)"""
    soup = BeautifulSoup(html_content, 'lxml')
    all_classes = set()
    for tag in soup.find_all(True, class_=True):
        for cls in tag.get('class', []):
            all_classes.add(cls)
    if not all_classes:
        return 0.0
    matched = all_classes & SUPPORTED_CLASSES
    return len(matched) / len(all_classes)
```

**铁律**：匹配率 < 60% → 手动构建；60%~85% → 自动脚本 + 手动补缺页；> 85% → 自动脚本即可。

#### 13.28 Python 字符串中嵌套中文引号导致 SyntaxError

**问题**：手动构建脚本中，中文内容经常包含中文引号 `"..."` 和 `'...'`（U+201C/U+201D/U+2018/U+2019）。当这些内容被放在 Python 的 `"..."` 双引号字符串中时：
- 中文左双引号 `"` (U+201C) 和右双引号 `"` (U+201D) 在某些环境下会导致 `SyntaxError: invalid character`
- 更隐蔽的情况：中文双引号 `""...""` 恰好形成了 Python 空字符串 + 裸中文文本 + 另一个空字符串的误解析

**修复规则**：

```python
# ❌ 错误写法 - 中文引号可能与 Python 引号冲突
title = "从"卖设备"到"持续交付 AI 能力""

# ✅ 正确写法 1 - 外层用单引号包裹
title = '从"卖设备"到"持续交付 AI 能力"'

# ✅ 正确写法 2 - 用英文引号替代中文引号
title = '从"卖设备"到"持续交付 AI 能力"'

# ✅ 正确写法 3 - 中文引号用 unicode 转义
title = "从\u201c卖设备\u201d到\u201c持续交付 AI 能力\u201d"
```

**铁律**：在手动构建脚本中，**所有包含中文引号的字符串，外层必须用单引号 `'...'` 包裹**。写完后必须运行 `py_compile.compile()` 做语法检查，再执行脚本。

#### 13.29 RGBColor 对象的 RGB 分量访问方式

**问题**：`pptx.dml.color.RGBColor` 对象**没有** `.red` / `.green` / `.blue` 属性。写 `color.red` 会报 `AttributeError: 'RGBColor' object has no attribute 'red'`。

**修复**：RGBColor 的 RGB 分量通过**索引**访问：

```python
from pptx.dml.color import RGBColor

color = RGBColor(0xFF, 0x80, 0x40)

# ❌ 错误
r, g, b = color.red, color.green, color.blue

# ✅ 正确
r, g, b = color[0], color[1], color[2]

# 实际用例：生成浅色背景（tag pill）
light_bg = RGBColor(
    min(255, color[0] + 200),
    min(255, color[1] + 200),
    min(255, color[2] + 200)
)
```

#### 13.30 字号下限与验证脚本的 12pt 硬门槛

**问题**：手动构建时为了视觉效果，标签药丸(tag pill)、副标题等元素使用了 11pt 小字号。但 `verify_output.py` 验证脚本有 **12pt 最低字号** 的硬性检查——任何小于 12pt 的文字都会报 ERROR。

**修复规则**：
- **所有文字元素字号不得低于 12pt**，这是验证脚本的硬门槛
- 即使是 tag pill、阶段编号(PHASE 01)、里程碑描述等小型文字，也必须 ≥12pt
- 如果 12pt 视觉上太大，通过缩短文字或减小元素尺寸来补偿，而不是降低字号

```python
# ❌ 错误 - 11pt 会被验证脚本报 ERROR
_set_font(run, FONT_W7, 11, True, color)

# ✅ 正确 - 最低 12pt
_set_font(run, FONT_W7, 12, True, color)
```

#### 13.31 手动构建脚本的标准代码模板

**问题**：每次手动构建都从零开始写辅助函数（`_set_font` / `_add_bg` / `_add_logo` / `_add_text_box` / `_add_rounded_rect` / `_add_card` 等），容易遗漏关键细节（如 `a:ea` XML 设置、z-order 调整等）。

**修复**：以下是经过验证的标准辅助函数模板，新的手动构建脚本**必须复用**这套函数，不要重新实现：

```python
def _set_font(run, font_name, size_pt, bold=False, color=None, align=None):
    """设置字体 - 同时设置 a:latin + a:ea（§13.21 铁律）"""
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    if color:
        run.font.color.rgb = color
    rPr = run._r.get_or_add_rPr()
    for tag in ('a:latin', 'a:ea'):
        el = rPr.find(qn(tag))
        if el is None:
            el = etree.SubElement(rPr, qn(tag))
        el.set('typeface', font_name)

def _add_bg(slide, bg_path):
    """添加背景图并移到 z-order 最底层（§13.22 铁律）"""
    pic = slide.shapes.add_picture(str(bg_path), 0, 0, SLIDE_W, SLIDE_H)
    sp_tree = slide.shapes._spTree
    pic_elem = pic._element
    sp_tree.remove(pic_elem)
    sp_tree.insert(2, pic_elem)

def _add_logo(slide, is_cover=False):
    """添加 Logo（封面左上，内容页右上）（§铁律14）"""
    if is_cover:
        slide.shapes.add_picture(str(LOGO_MAIN),
            Inches(0.65), Inches(0.61), Inches(4.88), Inches(0.53))
    else:
        slide.shapes.add_picture(str(LOGO_MAIN),
            Inches(14.60), Inches(0.49), Inches(4.88), Inches(0.53))

def _add_text_box(slide, left, top, width, height, text,
                  font_name, size_pt, bold=False, color=None, align=None):
    """添加文本框"""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    if align:
        p.alignment = align
    run = p.add_run()
    run.text = text
    _set_font(run, font_name, size_pt, bold, color)
    return txBox

def _add_rounded_rect(slide, left, top, width, height,
                      fill_color=None, border_color=None, radius=0.04):
    """添加圆角矩形（§13.25 标准圆角值）"""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    if fill_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1)
    else:
        shape.line.fill.background()
    shape.adjustments[0] = radius
    return shape

def _add_card(slide, left, top, width, height, title, body,
              title_color=C_BRAND_GREEN, body_color=C_DARK,
              bg_color=C_CARD_BG, border_color=C_CARD_BORDER):
    """添加标准内容卡片（圆角矩形 + 标题 + 正文）"""
    card = _add_rounded_rect(slide, left, top, width, height,
                             bg_color, border_color, 0.04)
    # 标题
    _add_text_box(slide, left + Inches(0.3), top + Inches(0.2),
                  width - Inches(0.6), Inches(0.5),
                  title, FONT_W7, 18, True, title_color)
    # 正文
    _add_text_box(slide, left + Inches(0.3), top + Inches(0.7),
                  width - Inches(0.6), height - Inches(1.0),
                  body, FONT_W3, 14, False, body_color)
    return card
```

#### 13.32 手动构建脚本的整体架构模式

**问题**：手动构建脚本结构混乱，函数名不统一，没有标准的执行流程。

**修复**：标准架构如下：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高保真 HTML→PPT 转换：[文件名]
逐页手动构建，套用腾讯云架构师长沙同盟模板品牌四件套
"""

# 1. 标准导入
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from lxml import etree

# 2. 品牌常量（从 SKILL.md §二.14 / §四 / §六 复制）

# 3. 标准辅助函数（从 §13.31 复制）

# 4. 每页构建函数：build_slide_N_xxx(prs) -> slide
#    命名规则：build_slide_{页码}_{页面简称}
#    每个函数内部：创建 slide → 添加背景 → 添加 Logo → 添加内容

# 5. 主函数
def main():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]  # 空白版式

    build_slide_1_cover(prs, blank)
    build_slide_2_toc(prs, blank)
    # ... 所有页面

    output_path = "xxx_长沙模板适配v2.pptx"
    prs.save(output_path)
    print(f"已保存：{output_path}")

if __name__ == '__main__':
    main()
```

**关键**：每个 `build_slide_N_xxx()` 函数**必须**按固定顺序执行：① 创建 slide → ② `_add_bg()` → ③ `_add_logo()` → ④ 添加内容元素。

#### 13.33 py_compile 语法预检是手动脚本的第一道门

**问题**：手动构建脚本通常有 500~1000+ 行，直接运行如果报 SyntaxError 只能看到一个错误位置，修完后可能还有下一个。反复运行调试浪费大量时间。

**修复**：脚本写完后，在首次运行前**必须**先执行语法预检：

```python
import py_compile
py_compile.compile('convert_xxx.py', doraise=True)
print('Syntax OK')
```

只有语法预检通过后，才能执行脚本。如果预检报错，先修完**所有**语法错误再运行。

**常见语法陷阱清单**：
- 中文引号 `"..."` 在 Python `"..."` 字符串中（见 §13.28）
- 中文全角逗号 `，` 在非字符串区域
- f-string 中的花括号 `{` `}` 未转义（应写 `{{` `}}`）
- 多行字符串的缩进不一致
- 三引号 `"""` 的配对错误

#### 13.34 何时用自动脚本 vs 何时用手动构建（决策树）

**问题**：面对新的 HTML→PPT 迁移任务，不知道该用自动脚本还是手动构建，导致先跑自动脚本浪费时间、输出质量差、用户不满意。

**决策树**：

```
输入 HTML
  │
  ├─ 有 3+ 个 div.slide ? ──── 是 → 幻灯片型 HTML
  │                                    │
  │                                    ├─ class 匹配率 > 85% ? → 自动脚本 apply_template.py
  │                                    ├─ class 匹配率 60~85% ? → 自动脚本 + 手动补缺页
  │                                    └─ class 匹配率 < 60% ? → **手动构建**
  │
  └─ 否 → 文章型 HTML → 自动脚本（走 parse_html + 智能分页）
```

**手动构建的触发信号**（有任意一条就应手动）：
1. HTML 使用了大量自定义 CSS class（scene-card / product-card / timeline 等）
2. 页面包含复杂的可视化元素（流程图 / 路线图 / KPI 统计块 / 对比矩阵）
3. 每页的布局差异很大（不是统一的"标题+正文"模式）
4. 用户反馈自动转换"差距太大"

#### 13.35 手动构建后必须执行的验证清单

**问题**：手动构建脚本运行成功不代表 PPT 质量过关——字号可能不合规、Logo 可能缺失、背景可能被遮挡。

**修复**：手动构建完成后，**必须**执行以下验证链：

```bash
# 1. 语法预检（写完代码后立即执行）
python -c "import py_compile; py_compile.compile('convert_xxx.py', doraise=True); print('Syntax OK')"

# 2. 运行脚本生成 PPT
python convert_xxx.py

# 3. 运行验证脚本（必须全 PASS）
python scripts/verify_output.py --pptx output.pptx

# 4. 如果有 ERROR → 修复后重新生成 → 重新验证，直到全 PASS
```

**验证脚本检查项**：
- 每页 shapes 数量 ≥ 3（至少有背景 + Logo + 内容）
- 所有字号 ≥ 12pt（硬门槛，见 §13.30）
- Logo 存在且位置正确（封面左上 / 内容页右上）
- 背景图/填充存在（不能有空白页）

---

## 十四、写作与执行风格

- **铁律优先于自由发挥**
- **保守优于激进**：宁可少改，不要多改
- **报告优于沉默**：每次输出适配报告
- **不替用户决策**：发现冲突时列出并请示

---

## 十五、HTML→PPT 迁移执行 Checklist（强制执行）

> ⚠️ **每次执行 HTML→PPT 迁移时，必须按此 Checklist 逐项检查**。这不是建议，是强制流程。

### 阶段零：方案选择（最先执行，决定走自动还是手动）

- [ ] 扫描 HTML 中所有 CSS class，计算与 `html_to_pptx.py` 支持列表的匹配率（§13.27）
- [ ] 匹配率 > 85% → 走自动脚本（阶段一~四）
- [ ] 匹配率 60~85% → 走自动脚本 + 识别缺失页面后手动补建
- [ ] 匹配率 < 60% → **跳过自动脚本，直接手动构建**（阶段五~七）
- [ ] 检查是否有复杂可视化元素（流程图 / 路线图 / KPI / 对比矩阵 / 时间线）→ 有则倾向手动
- [ ] 检查每页布局是否高度差异化（不是统一"标题+正文"模式）→ 是则倾向手动

### 阶段一：编码前审查（写代码前必须确认）——适用于自动脚本

- [ ] `_add_structured_slide()` 中所有结构类型（cards/columns/policy_cards/summary_cards/highlights/prob_charts/info_cards/gpt_letters/inline_flex_blocks）是否使用**独立 if 块**而非 elif 链？（§13.1）
- [ ] 渲染顺序是否为：highlights → gpt_letters/flex → cards → columns → policy_cards → summary_cards → raw_text → flow → prob → info？（§13.2）
- [ ] 所有 `run.font.name` 调用是否同时设置了 `a:ea` + `a:latin` XML？（§13.21）
- [ ] 背景图添加后是否执行了 `sp_tree.insert(2, pic_elem)` z-order 调整？（§13.22）
- [ ] 卡片高度是否用动态公式计算 + 剩余空间兜底？（§13.23）

### 阶段二：提取逻辑审查（解析 HTML 时）

- [ ] 双栏内 card 的 `.col-text`/`.col-list`/`.highlight-box` 是否用 `find_parent(class_='card')` 排除？（§13.3）
- [ ] 独立 card 提取是否排除了 `find_parent(class_='two-col')` 内的 card？（§13.10）
- [ ] card-row 与 standalone card 是否互斥提取？（§13.17）
- [ ] 卡片风格检测是否同时检查 class + inline-style？（§13.4）
- [ ] policy_card 的大 emoji 是否通过 `font-size:42px` 检测？（§13.5）
- [ ] card body 是否走多路径 fallback + title 去重？（§13.6）
- [ ] info-card 是否排除了含 prob-row 的容器？（§13.15）
- [ ] raw_text_blocks 是否只在无结构化内容时收集？（§13.19）

### 阶段三：渲染逻辑审查（生成 PPT 时）

- [ ] 双栏内 cards 是否优先渲染（不受 items/text 条件限制）？（§13.7）
- [ ] 双栏背景色是否跟随第一个内部 card 风格？（§13.8）
- [ ] 字号是否按 20 英寸幅面标准设置？（§13.9 + §六字体表）
- [ ] 圆角值 adjustments[0] 是否按标准值表设置？（§13.25）
- [ ] 表格单元格背景是否通过 XML 操作？（§13.24）
- [ ] y_cursor 是否检查不超过 Inches(9.5)？（§13.14）

### 阶段四：输出验证（生成 PPT 后，必须运行脚本）

```bash
python scripts/verify_output.py --pptx output.pptx --html source.html --strict
```

脚本自动检查：
- [ ] 每页 shapes 数量 >=3
- [ ] 字号范围正确（无 <12pt 文字）
- [ ] Logo 存在且位置正确
- [ ] 背景图/填充存在
- [ ] PPT 页数与 HTML 页数大致匹配（差异 <30%）

如脚本报 ERROR → 必须修复后重新生成。报 WARN → 人工确认是否需要修复。

### 阶段五：手动构建——编码规范（阶段零判定为手动时执行）

- [ ] 辅助函数是否从 §13.31 标准模板复制？（不要重新实现）
- [ ] `_set_font()` 是否同时设置了 `a:ea` + `a:latin` XML？（§13.21 + §13.31）
- [ ] `_add_bg()` 是否在添加背景图后执行了 `sp_tree.insert(2, pic_elem)`？（§13.22 + §13.31）
- [ ] 所有包含中文引号 `"..."` 的字符串，外层是否用**单引号** `'...'` 包裹？（§13.28）
- [ ] RGBColor 的分量访问是否用 `color[0]` `color[1]` `color[2]` 而非 `.red` `.green` `.blue`？（§13.29）
- [ ] 所有字号是否 ≥ 12pt？（§13.30，验证脚本硬门槛）
- [ ] 每个 `build_slide_N_xxx()` 函数是否按固定顺序：创建 slide → `_add_bg()` → `_add_logo()` → 内容？（§13.32）

### 阶段六：手动构建——语法预检（写完代码后、运行前必须执行）

```bash
python -c "import py_compile; py_compile.compile('convert_xxx.py', doraise=True); print('Syntax OK')"
```

- [ ] `py_compile` 语法检查是否通过？（§13.33）
- [ ] 如果报错，是否修完**所有**语法错误后才运行脚本？（不要一个一个修-运行-修-运行）

### 阶段七：手动构建——生成与验证（语法预检通过后执行）

- [ ] 运行脚本生成 PPT
- [ ] 运行 `verify_output.py --pptx output.pptx` 验证
- [ ] 验证结果是否全 PASS？（§13.35）
- [ ] 如有 ERROR → 修复 → 重新生成 → 重新验证（循环直到全 PASS）
- [ ] 交付前确认 PPT 页数与 HTML 页数一致

---

## 十六、异常处理与降级策略

> 只说"对的做法"不够——出错时该怎么办？以下是各种异常的处理方案。

### 16.1 字体未安装

| 症状 | 降级方案 |
|---|---|
| TencentSans W3/W7 未安装 | 1. 先尝试自动安装（从 `assets/fonts/` 复制到系统字体目录）<br>2. 安装失败 → 使用 `Microsoft YaHei`（微软雅黑）作为 fallback<br>3. 在输出报告中标注 `[WARN] 使用了 fallback 字体，建议安装 TencentSans` |

### 16.2 背景图文件缺失

| 症状 | 降级方案 |
|---|---|
| `assets/backgrounds/bg-*.jpeg` 不存在 | 1. 检查 `assets/` 目录结构是否完整<br>2. 尝试从模板 `.pptx` 中提取（`extract_template_assets.py`）<br>3. 提取失败 → 使用纯色 `#FAF6EE`（米白）作为背景填充<br>4. 报告中标注 `[WARN] 背景图缺失，使用纯色 fallback` |

### 16.3 HTML 结构完全不匹配

| 症状 | 降级方案 |
|---|---|
| 无 `.slide` div，也无 h1/h2 标题结构 | 1. 尝试按 `<p>` 段落 + 12行阈值做最基础分页<br>2. 每页只生成"标题+正文"最简布局<br>3. 报告中标注 `[WARN] HTML 结构无法识别，使用基础段落分页` |

### 16.4 图片 URL 下载失败

| 症状 | 降级方案 |
|---|---|
| 远程图片 HTTP 超时/404 | 1. 重试 1 次（timeout=10s）<br>2. 仍失败 → 跳过该图片，在对应位置放置一个灰色占位框 + 文字"[图片加载失败]"<br>3. 报告中列出所有失败的 URL |

### 16.5 PPT 生成过程中 python-pptx 报错

| 症状 | 降级方案 |
|---|---|
| `KeyError` / `AttributeError` 等 | 1. 捕获异常，跳过当前 slide 的问题元素<br>2. 继续处理后续 slides<br>3. 在最终报告中列出所有跳过的元素和对应 slide 编号<br>4. 不因单个元素失败而中止整个转换 |

### 16.6 上游 Skill 不可用

| 症状 | 降级方案 |
|---|---|
| 模式 A 需要上游 Skill 但未安装 | 直接切换到模式 C（HTML→PPT）或模式 B（PPT迁移）绕过上游依赖。本 Skill 的 HTML→PPT 能力可独立完成内容生成+品牌适配。 |

---

## 十七、版本历史

| 版本 | 日期 | 变更摘要 |
|---|---|---|
| v1.0 | 2026-06 | 初版：四件套适配（背景/字体/Logo/配色） |
| v2.0 | 2026-06 | 新增 HTML→PPT 能力（16种元素映射），新增 6 种结构化元素解析 |
| v3.0 | 2026-06-10 | 修复渲染互斥/重复提取/字体比例，新增 26 条经验库 + Checklist + 异常处理 + 验证脚本 |
| v3.1 | 2026-06-11 | §13 恢复为完整版（含代码示例），确保 AI 加载时一次性获得全部实现细节 |
| v3.2 | 2026-06-11 | 新增 §13.27~13.35（9 条手动构建经验：CSS class 盲区/中文引号 SyntaxError/RGBColor 索引/12pt 硬门槛/标准辅助函数模板/脚本架构/py_compile 预检/自动vs手动决策树/验证清单）+ §十五新增阶段零（方案选择）和阶段五~七（手动构建专用 Checklist）+ 铁律 17 更新 |

详细变更日志见 `references/changelog-v1-v5.md`。

---

**记住：本 Skill 不创作 PPT，它只让 PPT 看起来属于腾讯云架构师长沙同盟。**
