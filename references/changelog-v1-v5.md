# 实战经验教训（v1 → v5 沉淀）

> 从《AI 工程化落地》PPT 项目五次迭代踩过的坑与修复，作为执行检查清单。

## 教训 1：背景替换 API 不存在

| 项 | 内容 |
| --- | --- |
| 错误现象 | 30 页全部"背景替换失败" |
| 根因 | 原 `set_slide_background` 用了 python-pptx 不存在的私有 API |
| 修复 | 改成"添加全屏图片 + lxml 把 pic 移到 spTree 最前（z-order 最底）" |
| 检查清单 | 跑完 apply_template.py 后必看适配报告是否有背景替换警告 |

## 教训 2：不要用 light 模式绕过背景

| 项 | 内容 |
| --- | --- |
| 错误现象 | "模板背景没显示" |
| 根因 | 深色内容稿撞色，用 `--mode light` 绕过 → 等于没套模板 |
| 修复 | 迁移必须用 `--mode full`，撞色时改内容稿配色 |
| 检查清单 | 迁移永远用 full；撞色时改内容稿 |

## 教训 3：整页大白卡 = 模板消失

| 项 | 内容 |
| --- | --- |
| 错误现象 | "模板背景被白卡盖住" |
| 根因 | 上游内容稿 width=12.3" 整页大白卡遮挡背景 |
| 修复 | 半透明托盘 + 分散小卡 + 卡片间隙 + 四周安全区 |
| 检查清单 | 每页四周/间隙是否可见米黄底+红色城市线稿 |

## 教训 4：字体中文别名跨平台不识别

| 项 | 内容 |
| --- | --- |
| 错误现象 | 字体显示方块或回退宋体 |
| 根因 | 用了中文别名/多字体回退链 |
| 修复 | 锁定 `TencentSans W3` / `TencentSans W7`，取消回退链，内置字体文件 |
| 检查清单 | 所有 fontFace 严格等于英文带空格名 |

## 教训 5：Logo 凭直觉摆放

| 项 | 内容 |
| --- | --- |
| 错误现象 | Logo 位置不对 |
| 根因 | 凭直觉摆放，没看模板真实位置 |
| 修复 | 解析模板 XML 实测：所有页面 (0.30, 0.18, 2.80, 0.30) |
| 检查清单 | 任何规范设定前先实测模板 XML |

## 教训 6：实测优先于直觉

任何与"模板视觉"相关的设定必须先解析 XML 实测，禁止凭设计直觉猜。

---

# Skill 完善状态总表（截至 v6）

| 维度 | 状态 | 位置 |
| --- | --- | --- |
| 背景替换 | 已修复（z-order 实现） | apply_template.py |
| 三档适配模式 | full/light/logo-only | apply_template.py |
| 配色安全调色板 | 9 主色 + 5 辅助色 + 6 图表色 | brand_palette.py |
| 配色合规替换 | CIEDE2000 + 禁用色黑名单 + 主题色覆写 | apply_template.py |
| 背景可见性规范 | 7 条规则 | SKILL.md §4.5 |
| 字体锁定 | TencentSans W3/W7 | SKILL.md §4.2 |
| 字体内置 | TTF + OTF | assets/fonts/ |
| Logo 位置锁定 | (0.30, 0.18, 2.80, 0.30) | SKILL.md §4.3 |
| Logo 去重 | P0-2 修复 | apply_template.py |
| 全屏遮罩清除 | P0-1 修复 | apply_template.py |
| 上游协作指令 | brand_palette.py --prompt | brand_palette.py |
| 质量检查清单 | 10 项 | SKILL.md §八 |
| 多城市支持 | extract_template_assets.py | scripts/ |
| --dry-run | 不写文件仅分析 | apply_template.py |
