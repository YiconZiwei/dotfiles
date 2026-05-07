#!/usr/bin/env python3
"""
iTerm2 紫微斗数 · 十六星曜 ANSI Color Map
==========================================
14 主星 + 文昌(辅星) + 天刑(杂星) = 16 ANSI colors

暗曜 (Normal 0-7):
  0 巨门·暗  #1a1b26  Giant Gate — 水·暗 (darkness, secrets, void)
  1 七杀·红  #EF4444  Seven Kills — 金·杀 (fierce, errors, destruction)
  2 天梁·绿  #10B981  Heavenly Beam — 土·荫 (support, protection, success)
  3 武曲·金  #F59E0B  Military Star — 金·刚 (gold, efficiency, metal)
  4 天机·蓝  #3B82F6  Heavenly Machine — 木·智 (strategy, structure)
  5 紫微·紫  #9333EA  Emperor Star — 土·帝 (imperial purple, primary)
  6 太阴·青  #06B6D4  Moon — 水·柔 (serene, cool, water)
  7 天同·柔  #a9b1d6  Heavenly Unity — 水·和 (harmony, soft white)

明曜 (Bright 8-15):
  8  天刑·铁  #565f89  Heavenly Punishment — 火·刑 (steel, law, discipline)
  9  廉贞·赤  #DC2626  Pure Honesty — 火·烈 (deep crimson, passion)
  10 天府·翠  #34D399  Heavenly Treasury — 土·库 (verdant wealth, abundance)
  11 太阳·黄  #FBBF24  Sun — 火·明 (radiance, broadcast, brightest)
  12 天相·靛  #818CF8  Heavenly Minister — 水·印 (diplomatic, indigo)
  13 贪狼·桃  #F472B6  Greedy Wolf — 木·欲 (desire, peach blossom, charm)
  14 文昌·碧  #22D3EE  Literary Star — 金·文 (jade, elegance, writing)
  15 破军·光  #dfdef4  Army Breaker — 水·变 (explosive transformation, light)

Usage: python3 ~/.config/iterm2_configure.py
IMPORTANT: Close iTerm2 before running!
"""

import plistlib, shutil, sys
from pathlib import Path
from datetime import datetime

PLIST_PATH = Path.home() / "Library/Preferences/com.googlecode.iterm2.plist"


def hex_to_iterm(h, alpha=1.0):
    h = h.lstrip("#")
    return {
        "Red Component": int(h[0:2], 16) / 255.0,
        "Green Component": int(h[2:4], 16) / 255.0,
        "Blue Component": int(h[4:6], 16) / 255.0,
        "Alpha Component": alpha,
        "Color Space": "sRGB",
    }


# ─── 十六星曜 ANSI Color Map ────────────────────────────────────

ANSI_16 = {
    # 暗曜 Normal (dim)
    "Ansi 0 Color":  ("#1a1b26", "巨门·暗"),   # Black  — Giant Gate (void)
    "Ansi 1 Color":  ("#EF4444", "七杀·红"),   # Red    — Seven Kills (fierce)
    "Ansi 2 Color":  ("#10B981", "天梁·绿"),   # Green  — Heavenly Beam (success)
    "Ansi 3 Color":  ("#F59E0B", "武曲·金"),   # Yellow — Military Star (gold)
    "Ansi 4 Color":  ("#3B82F6", "天机·蓝"),   # Blue   — Heavenly Machine (strategy)
    "Ansi 5 Color":  ("#9333EA", "紫微·紫"),   # Magenta— Emperor Star (primary)
    "Ansi 6 Color":  ("#06B6D4", "太阴·青"),   # Cyan   — Moon (serene)
    "Ansi 7 Color":  ("#a9b1d6", "天同·柔"),   # White  — Heavenly Unity (harmony)
    # 明曜 Bright
    "Ansi 8 Color":  ("#565f89", "天刑·铁"),   # Br.Blk — Heavenly Punishment (steel)
    "Ansi 9 Color":  ("#DC2626", "廉贞·赤"),   # Br.Red — Pure Honesty (crimson fire)
    "Ansi 10 Color": ("#34D399", "天府·翠"),   # Br.Grn — Heavenly Treasury (verdant)
    "Ansi 11 Color": ("#FBBF24", "太阳·黄"),   # Br.Yel — Sun (radiance)
    "Ansi 12 Color": ("#818CF8", "天相·靛"),   # Br.Blu — Heavenly Minister (indigo)
    "Ansi 13 Color": ("#F472B6", "贪狼·桃"),   # Br.Mag — Greedy Wolf (peach blossom)
    "Ansi 14 Color": ("#22D3EE", "文昌·碧"),   # Br.Cyn — Literary Star (jade)
    "Ansi 15 Color": ("#dfdef4", "破军·光"),   # Br.Wht — Army Breaker (light)
}

SPECIAL_COLORS = {
    "Background Color":    ("#0f0e16", "命盘底色"),
    "Foreground Color":    ("#dfdef4", "星光前景"),
    "Bold Color":          ("#ffffff", "明曜加持"),
    "Cursor Color":        ("#9333EA", "紫微帝星"),
    "Cursor Text Color":   ("#0f0e16", "帝星反色"),
    "Selection Color":     ("#28264d", "暗紫选区"),
    "Selected Text Color": ("#dfdef4", "选中星光"),
    "Link Color":          ("#3B82F6", "天机链接"),
    "Badge Color":         ("#9333EA", "紫微徽章"),  # alpha set below
    "Tab Color":           ("#9333EA", "紫微标签"),
    "Cursor Guide Color":  ("#9333EA", "帝星引导"),  # alpha set below
}


def build_ansi_dict():
    """Build ANSI color settings with Dark/Light mode variants."""
    result = {}
    for key, (hexc, _name) in ANSI_16.items():
        c = hex_to_iterm(hexc)
        result[key] = c
        result[f"{key} (Dark)"] = dict(c)
        result[f"{key} (Light)"] = dict(c)
    return result


def build_special_dict():
    result = {}
    for key, (hexc, _name) in SPECIAL_COLORS.items():
        alpha = 1.0
        if "Badge" in key:
            alpha = 0.3
        elif "Guide" in key:
            alpha = 0.08
        c = hex_to_iterm(hexc, alpha)
        result[key] = c
        result[f"{key} (Dark)"] = dict(c)
        result[f"{key} (Light)"] = dict(c)
    return result


# ─── Profile Settings ────────────────────────────────────────────

FONT = "JetBrainsMonoNFM-Regular 14"

COMMON = {
    "Option Key Sends": 2, "Right Option Key Sends": 2,
    "Allow Clipboard Access": True,
    "Normal Font": FONT, "ASCII Anti Aliased": True,
    "Non-ASCII Anti Aliased": True, "Use Ligatures": True,
    "Columns": 140, "Rows": 42,
    "Use Cursor Guide": True, "Minimum Contrast": 0.03,
    "Scrollback Lines": 10000, "Unlimited Scrollback": False,
    "Show Mark Indicators": True, "Terminal Type": "xterm-256color",
    "Copy Selection": True, "Triple Click Selects Full Lines": True,
}

def make_status_bar():
    def comp(cls, pri=5, **k):
        kn = {"base: compression resistance": 1, "base: priority": pri}
        kn.update(k)
        return {"class": cls, "configuration": {"knobs": kn}}
    return {
        "advanced configuration": {
            "algorithm": 0, "font": "JetBrainsMonoNFM-Regular 12.0",
            "remove empty components": True,
        },
        "components": [
            comp("iTermStatusBarWorkingDirectoryComponent", 7,
                 path="reWriteCurrentDirectoryTruncatingHead"),
            comp("iTermStatusBarGitComponent", 6),
            comp("iTermStatusBarSpringComponent", 1),
            comp("iTermStatusBarCPUUtilizationComponent", 3),
            comp("iTermStatusBarMemoryUtilizationComponent", 3),
        ],
    }


def main():
    if not PLIST_PATH.exists():
        print("❌ iTerm2 plist not found"); sys.exit(1)

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = PLIST_PATH.with_suffix(f".plist.backup-{ts}")
    shutil.copy2(PLIST_PATH, backup)
    print(f"📦 Backup: {backup.name}")

    with open(PLIST_PATH, "rb") as f:
        plist = plistlib.load(f)

    profiles = plist.get("New Bookmarks", [])
    ansi = build_ansi_dict()
    special = build_special_dict()
    status_bar = make_status_bar()

    print(f"\n🔧 Configuring {len(profiles)} profile(s)...\n")

    for profile in profiles:
        name = profile.get("Name", "?")
        is_ziwei = "紫微" in name

        settings = dict(COMMON)
        if is_ziwei:
            settings.update(ansi)
            settings.update(special)
            settings.update({
                "Smart Cursor Color": False,
                "Use Tab Color": True,
                "Badge Text": "✦ \\(session.name)",
                "Transparency": 0.03,
                "Blur": True, "Blur Radius": 8.0,
                "Show Status Bar": True,
            })
        else:
            settings["Smart Cursor Color"] = True
            settings["Show Status Bar"] = True

        changes = sum(1 for k, v in settings.items() if profile.get(k) != v)
        for k, v in settings.items():
            profile[k] = v
        profile["Status Bar Layout"] = status_bar

        tag = "✦" if is_ziwei else "○"
        print(f"  {tag} {name}: {changes} settings")
        if is_ziwei:
            print()
            print("    ┌─ 暗曜 (Normal) ────────────────────┐")
            for i in range(8):
                key = f"Ansi {i} Color"
                hexc, sname = ANSI_16[key]
                print(f"    │ {i}  {sname}  {hexc}  │")
            print("    ├─ 明曜 (Bright) ────────────────────┤")
            for i in range(8, 16):
                key = f"Ansi {i} Color"
                hexc, sname = ANSI_16[key]
                print(f"    │ {i:2d} {sname}  {hexc}  │")
            print("    └───────────────────────────────────┘")
            print()

    with open(PLIST_PATH, "wb") as f:
        plistlib.dump(plist, f)

    print("✅ iTerm2 十六星曜 配色完成!")
    print(f"💾 Backup: {backup}")


if __name__ == "__main__":
    main()
