#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
brand_palette.py — 配色协作辅助模块

提供给上游 PPT Skill 使用：
  1) 输出"安全调色板" prompt 片段（注入到内容生成 Skill 的指令中）
  2) 校验给定 HEX 是否在安全色范围内
  3) 提供 Python dict 形式的色板，便于程序化生成图表配色

用法：
  # 命令行直接拿 prompt
  python scripts/brand_palette.py --prompt

  # 校验颜色
  python scripts/brand_palette.py --validate "#7B61FF"

  # 列出图表色板
  python scripts/brand_palette.py --chart
"""

import argparse
import sys
import re

# ---------- 配色定义 ----------

CORE_COLORS = {
    "brand_red_dark": "#D80C01",
    "brand_red": "#FF0000",
    "black": "#000000",
    "text_dark": "#222222",
    "text_mid": "#666666",
    "text_light": "#888888",
    "white": "#FFFFFF",
    "milk_white": "#FAF6EE",
    "border_gray": "#E7E6E6",
}

ACCENT_COLORS = {
    # §4.2 辅助色（暖色优先，最多同时取 2 个作为内容色块；图表可全部使用）
    # #08194B 深蓝已移入禁用色 → 优先使用暖色系做卡片/色块
    "warm_pale_yellow": "#FAD16A",   # 暖淡黄（首选暖色）
    "tip_gold": "#F19D19",           # 提示金
    "business_blue": "#1D6FA9",      # 商务蓝（数据系列、流程图）
    "elegant_gray_green": "#4A5D52", # 高级灰绿
}

# §4.4 WarmTone — 暖色调内容色块专区（仅用于信息卡/步骤框/标签等内容型色块）
# 单页最多 3 种，不可大面积铺背景
# 步骤/流程推荐渐进顺序：珊瑚粉 → 暖杏色 → 浅赭色
WARM_TONE_COLORS = {
    "coral_pink":   "#E8A090",  # 珊瑚粉（Step 1）
    "warm_apricot": "#D4A574",  # 暖杏色（Step 2）
    "light_gold_orange": "#E8B84A",  # 浅金橙
    "rose_wood":    "#C4A484",  # 玫瑰木
    "light_ochre":  "#D49A6A",  # 浅赭色（Step 3）
}

CHART_PALETTE = [
    "#D80C01",  # 系列 1 — 品牌红
    "#D4A574",  # 系列 2 — 暖杏色（替代原 #08194B 深蓝）
    "#FAD16A",  # 系列 3 — 暖淡黄
    "#666666",  # 系列 4 — 中灰
    "#1D6FA9",  # 系列 5 — 商务蓝
    "#F19D19",  # 系列 6 — 提示金
]

CARD_RULES = {
    "default": {"bg": "#FFFFFF", "text": "#222222"},
    "milk":    {"bg": "#FAF6EE", "text": "#222222"},
    "emphasis":{"bg": "#D80C01", "text": "#FFFFFF"},
    "data":    {"bg": "#D4A574", "text": "#FFFFFF"},  # 暖杏色（原 #08194B 深蓝已弃用）
    "code":    {"bg": "#1E1E1E", "text": "#FFFFFF"},
}

# 禁用色判定（HSV 范围）
FORBIDDEN_HUE_RANGES = [
    # 蓝紫 / 紫色：H 240–290
    (240, 290),
    # 鲜亮绿：H 90–160 且高饱和高明度
    # 青色 / Teal：H 160–200
    (160, 200),
    # 粉色 / 玫红：H 300–340（避开品牌红 0–10）
    (300, 340),
]

ALLOWED_LIST = set(
    list(CORE_COLORS.values())
    + list(ACCENT_COLORS.values())
    + list(WARM_TONE_COLORS.values())
    + CHART_PALETTE
)


def hex_to_hsv(hex_color: str):
    """简单 HEX → HSV 转换（H: 0–360, S/V: 0–1）"""
    h = hex_color.lstrip("#")
    if len(h) != 6:
        return None
    r = int(h[0:2], 16) / 255
    g = int(h[2:4], 16) / 255
    b = int(h[4:6], 16) / 255
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if df == 0:
        hue = 0
    elif mx == r:
        hue = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        hue = (60 * ((b - r) / df) + 120) % 360
    else:
        hue = (60 * ((r - g) / df) + 240) % 360
    sat = 0 if mx == 0 else df / mx
    val = mx
    return hue, sat, val


def validate_color(hex_color: str) -> dict:
    """校验颜色是否在安全色范围内。返回 {'safe': bool, 'reason': str}"""
    hex_color = hex_color.upper()
    if not re.fullmatch(r"#[A-F0-9]{6}", hex_color):
        return {"safe": False, "reason": "格式非法（应为 #RRGGBB）"}

    if hex_color in ALLOWED_LIST:
        return {"safe": True, "reason": "在白名单中"}

    hsv = hex_to_hsv(hex_color)
    if hsv is None:
        return {"safe": False, "reason": "解析失败"}
    h, s, v = hsv

    # 极低饱和（接近灰白黑）通常安全
    if s < 0.15:
        return {"safe": True, "reason": "低饱和中性色，可作为辅助灰阶"}

    # 检查是否落在禁用色相区
    for lo, hi in FORBIDDEN_HUE_RANGES:
        if lo <= h <= hi and s > 0.3:
            return {
                "safe": False,
                "reason": f"色相 H={h:.0f}° 落入禁用区间 [{lo}°–{hi}°]，"
                          f"会与红色城市背景撞色",
            }

    # 高饱和绿色单独判
    if 90 <= h <= 160 and s > 0.4 and v > 0.5:
        return {
            "safe": False,
            "reason": f"鲜亮绿色（H={h:.0f}°），红配绿大忌",
        }

    return {
        "safe": True,
        "reason": f"色相 H={h:.0f}° 不在禁用区间，但建议尽量使用调色板中的标准色",
    }


def get_prompt_snippet() -> str:
    """返回注入给上游 PPT Skill 的配色 + 背景可见性约束 prompt"""
    return """配色约束（强制遵守，不可偏离）：
- 主色仅可用：#D80C01（品牌红）、#000000、#FFFFFF、#222222、#666666（中灰）、#888888（浅灰）、#FAF6EE（米白底）
- 辅助色（≤2种，优先暖色系）：#FAD16A（暖淡黄，首选）、#F19D19（提示金）、#1D6FA9（商务蓝，仅数据系列/流程图）、#4A5D52（高级灰绿）
- 图表多系列按顺序：#D80C01 → #D4A574（暖杏色）→ #FAD16A → #666666 → #1D6FA9 → #F19D19
- 深蓝色块（#08194B 沉稳深蓝）已弃用，禁用！必须用暖色系替代
- 内容色块（信息卡/步骤框/标签，单页 ≤ 3 种，优先暖色系，不可大面积铺背景）：
    #E8A090（珊瑚粉）、#D4A574（暖杏色）、#E8B84A（浅金橙）、#C4A484（玫瑰木）、#D49A6A（浅赭色）
  步骤渐进推荐：珊瑚粉 → 暖杏色 → 浅赭色
- 卡片背景：#FFFFFF 或 #FAF6EE（不透明度 ≥ 95%）
- 强调卡片：#D80C01 底 + #FFFFFF 字
- 数据卡片：#D4A574（暖杏色）底 + #FFFFFF 字（替代原 #08194B 深蓝）
- 代码块：#1E1E1E 底 + #FFFFFF 字
- 严禁：深蓝色（含 #08194B）、蓝紫色、鲜亮绿色、青色 Teal、粉色玫红、彩色渐变、玻璃拟态、霓虹荧光色

背景可见性约束（关键，强制遵守 — 否则模板背景会被遮挡）：
- 不要给 slide 设置背景色（保持透明，让模板的米黄底+红色城市线稿背景透出来）
- 严禁使用撑满整页（宽 > 10 inch 且 高 > 4 inch）的不透明白色大卡作为内容容器
- 内容容器优先使用半透明白色托盘（transparency: 15-30%），保留背景纹理
- 卡片之间必须留 0.2-0.4 inch 间隙
- 每页四周至少留 0.3 inch 无元素安全区
- 标题直接放在米黄背景上，加左侧 0.1 inch 红色锚条；不要用大白卡盖标题
- 流程图节点、小色块、按钮直接画在米黄底上
- Q&A 页、章节扉页、结尾页应让模板红色城市背景大面积显示，文字直接放
- 模板背景为米黄底+红色城市线稿，所有 AI 生成的色块必须避免与之撞色，且必须给背景留出可见区域
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", action="store_true", help="输出配色约束 prompt（用于注入上游 Skill）")
    ap.add_argument("--validate", help="校验某个 HEX 颜色是否安全")
    ap.add_argument("--chart", action="store_true", help="输出图表色板")
    ap.add_argument("--list", action="store_true", help="列出全部安全色")
    args = ap.parse_args()

    if args.prompt:
        print(get_prompt_snippet())
    elif args.validate:
        r = validate_color(args.validate)
        flag = "[SAFE]" if r["safe"] else "[UNSAFE]"
        print(f"{flag}：{args.validate} — {r['reason']}")
        sys.exit(0 if r["safe"] else 1)
    elif args.chart:
        print("图表色板（按系列顺序）：")
        for i, c in enumerate(CHART_PALETTE, 1):
            print(f"  系列 {i}: {c}")
    elif args.list:
        print("Core Colors (Brand):")
        for k, v in CORE_COLORS.items():
            print(f"  {v}  {k}")
        print("\nAccent Colors（暖色优先，最多 2 种）:")
        for k, v in ACCENT_COLORS.items():
            print(f"  {v}  {k}")
        print("\nChart Palette（图表按系列顺序）:")
        for i, c in enumerate(CHART_PALETTE, 1):
            print(f"  系列 {i}: {c}")
        print("\nWarmTone Colors（仅内容色块，单页 <= 3 种）:")
        for k, v in WARM_TONE_COLORS.items():
            print(f"  {v}  {k}")
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
