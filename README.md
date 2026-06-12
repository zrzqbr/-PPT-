<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/python--pptx-0.6.21+-orange" alt="python-pptx">
  <img src="https://img.shields.io/badge/Platform-WorkBuddy%20Skill-blueviolet" alt="Platform">
</p>

<h1 align="center">Tencent Architect Changsha PPT Adapter</h1>

<p align="center">
  <strong>腾讯云架构师长沙同盟 PPT 模板适配 Skill</strong><br>
  <sub>一键将任意 PPT 适配为专属腾讯云架构师长沙同盟品牌风格</sub>
</p>

<p align="center">
  <a href="#-快速开始">快速开始</a> &bull;
  <a href="#-核心能力">核心能力</a> &bull;
  <a href="#-使用模式">使用模式</a> &bull;
  <a href="#-目录结构">目录结构</a> &bull;
  <a href="#-反馈">反馈</a>
</p>

---

## 💡 这是什么

> **这是一个 PPT 品牌适配工具，不是内容创作器。**

它的唯一职责：在不破坏讲师/嘉宾创作成果的前提下，让最终 PPT 继承统一模板的品牌资产。

**核心原则** — 只锁四项品牌资产，其他一切不强制：

```
背景 ✓ · 字体 ✓ · Logo ✓ · 配色 ✓ · 内容 ✗ · 版式 ✗ · 图表 ✗
```

---

## ✨ 核心能力

<table>
  <tr>
    <td align="center" width="25%"><h3>🎨</h3><strong>背景适配</strong><br><sub>自动替换为品牌模板背景图</sub></td>
    <td align="center" width="25%"><h3>🔤</h3><strong>字体统一</strong><br><sub>替换为 TencentSans W7/W3</sub></td>
    <td align="center" width="25%"><h3>🏷️</h3><strong>Logo 定位</strong><br><sub>按页面类型精准插入 Logo</sub></td>
    <td align="center" width="25%"><h3>🎯</h3><strong>配色合规</strong><br><sub>检测禁用色并自动替换</sub></td>
  </tr>
</table>

---

## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/zrzqbr/tencent-architect-changsha-ppt-adapter.git
cd tencent-architect-changsha-ppt-adapter

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行适配
python scripts/apply_template.py --input your.pptx --output branded.pptx
```

### 环境要求

- Python 3.9+
- 依赖：`python-pptx` · `lxml` · `Pillow` · `beautifulsoup4`

---

## 📋 使用模式

### 模式 A：生成 + 适配

```
输入主题 + 大纲  →  PPT 生成 Skill + 本适配 Skill 协同  →  品牌化 .pptx
```

### 模式 B：迁移已有 PPT

```
原始 .pptx  →  模板适配  →  品牌化 .pptx
```

---

## 💬 提示词模板

<details>
<summary><strong>场景一：配合 PPT 生成 Skill 使用</strong></summary>

```text
请帮我制作一份腾讯云架构师技术同盟沙龙 PPT。

主题：[在此填写你的主题，例如：云原生架构落地实践]
大纲：
1. [章节一标题]
2. [章节二标题]
3. [章节三标题]
4. [章节四标题]

要求：
- 搭配我常用的 PPT 生成 Skill 与腾讯云架构师长沙同盟 PPT 模板适配 Skill 协同完成
- 内容详实，结构清晰
- 包含完整页面结构：封面页、目录页、章节扉页、结尾页
- 统一品牌配色规范
```

</details>

<details>
<summary><strong>场景二：迁移已有 PPT 到品牌模板</strong></summary>

```text
请帮我将附件中的 PPT 迁移到腾讯云架构师长沙同盟模板。

要求：
- 调用腾讯云架构师长沙同盟 PPT 模板适配 Skill 完成迁移
- 保留原始 PPT 的所有内容、版式和图表，不要修改文案
- 替换背景为品牌模板背景
- 字体统一为 TencentSans
- 插入品牌 Logo（封面左上角，内容页右上角）
- 检查配色合规性，替换禁用色
```

</details>

---

## 🔑 触发关键词

以下关键词会触发本 Skill：

`腾讯云架构师技术同盟模板` · `长沙同盟 PPT` · `把 PPT 套到模板` · `嘉宾 PPT 换统一模板` · `沙龙模板适配` · `保留内容只替换背景/字体/Logo/配色`

---

## 📁 目录结构

```
tencent-architect-changsha-ppt-adapter/
├── 📄 SKILL.md                         # 主文档（1479 行，含完整迁移经验）
├── 📄 README.md                        # 本文件
├── 📄 LICENSE                          # MIT 协议
├── 📄 requirements.txt                 # Python 依赖
├── 📂 scripts/
│   ├── apply_template.py               # 统一入口脚本 v8
│   ├── html_to_pptx.py                # HTML → PPTX 核心转换
│   ├── verify_output.py               # 输出质量验证（42 项检查）
│   ├── brand_palette.py               # 配色校验 + 上游约束
│   ├── extract_template_assets.py     # 模板资产提取
│   └── test_v5.py                     # 自动化测试套件
├── 📂 assets/
│   ├── backgrounds/                   # 品牌背景图
│   ├── logos/                         # 品牌 Logo
│   ├── fonts/                         # TencentSans W3/W7
│   └── templates/                     # 城市模板源文件
└── 📂 references/
    ├── brand-rules.md                 # 品牌规范补充
    └── changelog-v1-v5.md             # 实战经验沉淀
```

---

## ⚠️ 注意事项

- 本工具**只做风格适配**，不会修改你的文案内容和页面布局
- 支持多种输入格式：`.pptx`、`HTML`、`Markdown`
- 迁移模式需将原始 PPT 作为附件上传
- TencentSans 字体为腾讯品牌字体，请确认使用授权

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📬 反馈

- **意见反馈问卷：** https://wj.qq.com/s2/26990654/bded

---

<p align="center">
  <sub>本工具不创作 PPT，它让 PPT 形成专属腾讯云架构师长沙同盟的统一风格。</sub><br>
  <sub>Made with ❤️ by <a href="https://github.com/zrzqbr">zrzqbr</a></sub>
</p>
