#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_template_assets.py — 从城市模板 PPTX 中提取背景、Logo

用法：
  python scripts/extract_template_assets.py --pptx "/path/to/成都模板.pptx" --city chengdu

会更新 assets/templates/ 与 assets/backgrounds/ 与 assets/logos/。
注意：此脚本假设模板的图像文件在 ppt/media/ 下，且尺寸大致匹配
  - 背景：宽 ≥ 1500，分类为 cover（含强色彩）或 content（淡色）
  - Logo：透明 PNG，且宽 < 1000

依赖：
  pip install Pillow
"""

import argparse
import os
import shutil
import sys
import zipfile
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("[ERROR] 缺少依赖。请运行: pip install Pillow", file=sys.stderr)
    sys.exit(1)

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
ASSETS = SKILL_DIR / "assets"


def is_logo(img_path: Path) -> bool:
    if img_path.suffix.lower() != ".png":
        return False
    try:
        with Image.open(img_path) as im:
            if "A" not in im.getbands():
                return False
            w, h = im.size
            if w > 1000 or h > 600:
                return False
            return True
    except Exception:
        return False


def is_background(img_path: Path) -> bool:
    if img_path.suffix.lower() not in (".jpg", ".jpeg", ".png"):
        return False
    try:
        with Image.open(img_path) as im:
            w, h = im.size
            return w >= 1500 and h >= 800
    except Exception:
        return False


def classify_background(img_path: Path) -> str:
    """通过亮度 + 饱和度综合判断背景类型。
    
    判断逻辑（双指标，降低误判）：
    - cover：亮度 < 220  OR  颜色多样性（最大-最小通道均值差）> 25
      → 深色/饱和的封面/扉页背景（如含红色城市线稿的 bg-cover）
    - content：亮度 >= 220  AND  颜色多样性 <= 25
      → 浅淡/接近单色的内容页背景（如浅米黄底的 bg-content）
    
    单纯亮度判断的误判场景：
    - 整体偏亮但含大面积彩色装饰（如烟花）→ 应判 cover，纯亮度会误判为 content
    - 整体偏暗但是单色低饱和深灰 → 应判 content，纯亮度会误判为 cover
    """
    with Image.open(img_path) as im:
        small = im.convert("RGB").resize((64, 64))
        pixels = list(small.getdata())

    brightness = sum((r + g + b) / 3 for r, g, b in pixels) / len(pixels)
    # 颜色多样性：每像素 max(r,g,b) - min(r,g,b) 的均值，衡量色彩饱和程度
    color_diversity = sum(max(r, g, b) - min(r, g, b) for r, g, b in pixels) / len(pixels)

    if brightness >= 220 and color_diversity <= 25:
        return "content"
    return "cover"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pptx", required=True, help="城市模板 .pptx 路径")
    ap.add_argument("--city", required=True, help="城市标识（changsha/chengdu/...）")
    ap.add_argument("--dry-run", action="store_true", help="只打印计划，不写入")
    args = ap.parse_args()

    src = Path(args.pptx)
    if not src.exists():
        print(f"[ERROR] 不存在：{src}", file=sys.stderr)
        sys.exit(1)

    # 1) 拷贝模板本体
    target_tpl = ASSETS / "templates" / f"{args.city}-architect-salon-template.pptx"
    target_tpl.parent.mkdir(parents=True, exist_ok=True)
    if not args.dry_run:
        shutil.copy(src, target_tpl)
    print(f"[OK] 模板已拷贝 → {target_tpl}")

    # 2) 解压并扫描 media
    extract_dir = SKILL_DIR / ".tmp_extract"
    if extract_dir.exists():
        shutil.rmtree(extract_dir)
    extract_dir.mkdir()
    with zipfile.ZipFile(src) as z:
        z.extractall(extract_dir)

    media_dir = extract_dir / "ppt" / "media"
    if not media_dir.exists():
        print("[WARN] 未找到 ppt/media/", file=sys.stderr)
        sys.exit(2)

    logos = []
    backgrounds = []
    for f in sorted(media_dir.iterdir()):
        if is_logo(f):
            logos.append(f)
        elif is_background(f):
            backgrounds.append(f)

    print(f"[INFO] 检测到 {len(logos)} 个 Logo 候选，{len(backgrounds)} 个背景候选")

    # 3) 写入 logos
    logos_sorted = sorted(logos, key=lambda p: p.stat().st_size, reverse=True)
    if logos_sorted:
        # 最大的视为主 Logo
        if not args.dry_run:
            shutil.copy(logos_sorted[0], ASSETS / "logos" / "logo-main.png")
        print(f"[OK] 主 Logo ← {logos_sorted[0].name}")
        if len(logos_sorted) > 1:
            if not args.dry_run:
                shutil.copy(logos_sorted[-1], ASSETS / "logos" / "logo-corner.png")
            print(f"[OK] 角标 Logo ← {logos_sorted[-1].name}")

    # 4) 写入 backgrounds
    bg_cover_picked = None
    bg_content_picked = None
    for bg in backgrounds:
        cls = classify_background(bg)
        if cls == "cover" and bg_cover_picked is None:
            bg_cover_picked = bg
        elif cls == "content" and bg_content_picked is None:
            bg_content_picked = bg

    if bg_cover_picked:
        # 城市专属命名：{city}-bg-cover.jpeg，长沙同时写通用 bg-cover.jpeg（作为默认回退）
        dst_city = ASSETS / "backgrounds" / f"{args.city}-bg-cover.jpeg"
        if not args.dry_run:
            shutil.copy(bg_cover_picked, dst_city)
            if args.city == "changsha":
                shutil.copy(bg_cover_picked, ASSETS / "backgrounds" / "bg-cover.jpeg")
        print(f"[OK] bg-cover ← {bg_cover_picked.name} → {dst_city.name}")
    if bg_content_picked:
        dst_city = ASSETS / "backgrounds" / f"{args.city}-bg-content.jpeg"
        if not args.dry_run:
            shutil.copy(bg_content_picked, dst_city)
            if args.city == "changsha":
                shutil.copy(bg_content_picked, ASSETS / "backgrounds" / "bg-content.jpeg")
        print(f"[OK] bg-content ← {bg_content_picked.name} → {dst_city.name}")

    shutil.rmtree(extract_dir, ignore_errors=True)
    print("[DONE]")


if __name__ == "__main__":
    main()
