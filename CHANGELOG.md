# Changelog

本文件遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 规范。

## [v3.3.2] - 2026-06-12

### Added
- `.gitignore` 文件，排除 Python 缓存和系统文件
- `LICENSE` (MIT) 开源协议
- `requirements.txt` 依赖清单
- `CONTRIBUTING.md` 贡献指南
- `CHANGELOG.md` 版本变更日志
- `assets/fonts/README.md` 补充字体版权声明

### Changed
- 仓库重命名：`-PPT-` → `tencent-architect-changsha-ppt-adapter`
- `README.md` 全面重新设计（badges、能力卡片、流程图、触发场景标签）
- `assets/fonts/README.md` 修正文件引用（移除不存在的 .otf 引用）
- `SKILL.md` 更新至 v3.2（补充手动构建经验）

### Removed
- 清理已跟踪的 `__pycache__/*.pyc` 缓存文件

## [v3.2.0] - 2026-06-10

### Changed
- SKILL.md 从 1126 行扩充至 1479 行
- 新增手动构建经验章节（26 条迁移代码示例的实战补充）
- HTML→PPTX 转换脚本字号回调修复（v4）

## [v3.1.0] - 2026-06-09

### Added
- 删除冗余 .otf 字体文件，仅保留 .ttf 格式（减小仓库体积）
- 添加 README.md 项目说明文档

## [v3.0.0] - 2026-06-08

### Added
- 完整 Skill 框架初始发布
- `SKILL.md` 主文档（1126 行），含完整品牌规范 + 26 条迁移经验代码示例
- `scripts/` 6 个 Python 脚本：
  - `apply_template.py` — PPT 模板适配引擎（full/light/logo-only 三档模式）
  - `html_to_pptx.py` — HTML→PPTX 转换器
  - `verify_output.py` — 输出质量验证（字号/字体/配色/Logo 10 项检查）
  - `brand_palette.py` — 品牌安全调色板（9 主色 + 5 辅助色 + 6 图表色）
  - `extract_template_assets.py` — 模板资产提取（支持多城市扩展）
  - `test_v5.py` — 集成测试脚本
- `assets/` 品牌资产全套：
  - 背景图（封面 `bg-cover.jpeg` + 内容页 `bg-content.jpeg`）
  - Logo（腾讯云架构师技术同盟标识）
  - 字体（TencentSans W3 / W7 TTF）
  - 基准模板 .pptx
- `references/` 参考文档：
  - `brand-rules.md` — 品牌视觉规范（配色/字体/排版硬规则）
  - `changelog-v1-v5.md` — v1→v5 实战踩坑经验教训

---

## 版本命名规则

- **主版本号 (Major)**：Skill 框架重大重构
- **次版本号 (Minor)**：新增功能或文档大幅更新
- **修订号 (Patch)**：Bug 修复、文档小修、项目规范化
