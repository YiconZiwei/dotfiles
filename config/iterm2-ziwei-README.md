# 紫微斗数 · 十六星曜 Terminal Configuration

iTerm2 + Claude Code unified color system based on 紫微斗数 (Purple Star Astrology).
14 主星 + 文昌(辅星) + 天刑(杂星) = 16 ANSI colors.

## Quick Reference

### Run Configuration
```bash
# Apply iTerm2 settings (close iTerm2 first!)
python3 ~/.config/iterm2_configure.py

# Test colors (run inside iTerm2 紫微星系 profile)
bash /tmp/ziwei_color_test.sh
```

### Files
| File | Purpose |
|------|---------|
| `~/.config/iterm2_configure.py` | iTerm2 plist configurator (profiles, colors, fonts) |
| `~/.config/starship.toml` | Starship prompt theme (紫微 palette) |
| `~/.claude/themes/ziwei.json` | Claude Code custom theme |
| `~/.claude/statusline-command.sh` | Claude Code status line (uses same ANSI indices) |
| `~/.zshrc` | Shell config (starship cache, iTerm2 integration, Claude badge) |

---

## 十六星曜 ANSI Color Map

### 暗曜 Normal (0-7)
```
ANSI  星曜       Hex       五行·象意              Terminal Function
────  ─────────  ────────  ─────────────────────  ──────────────────
 0    巨门·暗    #1a1b26   水·暗 — 深渊、秘密     Black (background-like)
 1    七杀·红    #EF4444   金·杀 — 破坏、阻断     Red (errors, failures)
 2    天梁·绿    #10B981   土·荫 — 庇护、验证     Green (success, staged)
 3    武曲·金    #F59E0B   金·刚 — 效率、财务     Yellow (warnings, duration)
 4    天机·蓝    #3B82F6   木·智 — 策略、架构     Blue (info, git branches)
 5    紫微·紫    #9333EA   土·帝 — 帝星、主宰     Magenta (primary accent)
 6    太阴·青    #06B6D4   水·柔 — 月亮、沉静     Cyan (links, secondary info)
 7    天同·柔    #a9b1d6   水·和 — 和谐、柔光     White (normal text, soft)
```

### 明曜 Bright (8-15)
```
ANSI  星曜       Hex       五行·象意              Terminal Function
────  ─────────  ────────  ─────────────────────  ──────────────────
 8    天刑·铁    #565f89   火·刑 — 法律、纪律     Bright Black (dim text, timestamps)
 9    廉贞·赤    #DC2626   火·烈 — 烈焰、深红     Bright Red (deletions, critical)
10    天府·翠    #34D399   土·库 — 财库、丰盈     Bright Green (additions, wealth)
11    太阳·黄    #FBBF24   火·明 — 光辉、广播     Bright Yellow (highlights, untracked)
12    天相·靛    #818CF8   水·印 — 外交、印信     Bright Blue (diff hunks, diplomatic)
13    贪狼·桃    #F472B6   木·欲 — 桃花、魅力     Bright Magenta (special, charm)
14    文昌·碧    #22D3EE   金·文 — 文采、玉碧     Bright Cyan (docs, literary)
15    破军·光    #dfdef4   水·变 — 爆裂、变革     Bright White (foreground, bold)
```

### Special Colors
```
Element       Hex       星曜象意
────────────  ────────  ──────────
Background    #0f0e16   命盘底色 (chart base)
Foreground    #dfdef4   星光前景 (starlight)
Bold          #ffffff   明曜加持 (bright boost)
Cursor        #9333EA   紫微帝星 (emperor cursor)
Cursor Text   #0f0e16   帝星反色 (inverse)
Selection     #28264d   暗紫选区 (dark purple)
Selected Text #dfdef4   选中星光 (selected starlight)
Link          #3B82F6   天机链接 (strategy link)
Tab Color     #9333EA   紫微标签 (emperor tab)
```

---

## Three-Layer Consistency

The same hex values are shared across iTerm2, Claude Code, and the statusline:

```
Token        Star       iTerm2 ANSI   Claude Theme    Statusline ANSI
───────────  ─────────  ───────────   ─────────────   ───────────────
accent       紫微·紫    5 (magenta)   claude          \033[35m
error        七杀·红    1 (red)       error           \033[31m
success      天梁·绿    2 (green)     success         \033[32m
warning      武曲·金    3 (yellow)    warning         \033[33m
info         天机·蓝    4 (blue)      planMode        \033[34m
dim          天刑·铁    8 (br.black)  inactive        \033[90m
foreground   破军·光    15 (br.white) text            (default)
border       暗紫选区   Selection     subtle          —
```

The statusline uses context-aware coloring for ctx% usage:
- `< 60%` → 天梁·绿 (safe)
- `60-80%` → 武曲·金 (caution)
- `> 80%` → 七杀·红 (danger)

---

## Shell Optimizations (.zshrc)

### Starship Cache (18× faster startup)
Startup went from 2.05s → 0.11s by caching `starship init zsh`:
```bash
if [[ ! -f ~/.starship_init.zsh ]] || [[ ~/.config/starship.toml -nt ~/.starship_init.zsh ]]; then
  starship init zsh > ~/.starship_init.zsh
fi
source ~/.starship_init.zsh
```
Cache auto-regenerates when `starship.toml` changes.

### iTerm2 Shell Integration
```bash
test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"
```
Enables: command markers (blue gutter), ⌘+Shift+↑/↓ navigation, output capture.

### Claude Code Badge
Shows 🤖 in iTerm2 badge when Claude Code is active:
```bash
if [ "$ITERM_SESSION_ID" ]; then
  function iterm2_print_user_vars() {
    if [[ -n "$CLAUDE_SESSION_ID" ]]; then
      iterm2_set_user_var claude_active "🤖"
    fi
  }
fi
```

### Shell Options for Claude Code
```bash
setopt no_nomatch           # Don't error on unmatched globs
setopt interactive_comments # Allow # comments in interactive shell
setopt extended_history     # Timestamps in history
```

---

## iTerm2 Profile Settings

Applied to both profiles (Default + 紫微星系):

| Setting | Value | Why |
|---------|-------|-----|
| Option Key | Esc+ | Claude Code shortcuts (⌥P model, ⌥T thinking, ⌥Enter newline) |
| Font | JetBrains Mono Nerd Font 14 | Nerd Font icons + ligatures |
| Window | 140×42 | Wide enough for Claude Code output |
| Clipboard Access | On | Claude Code `/copy` works |
| Mark Indicators | On | Blue gutter markers per command |
| Scrollback | 10000 | Balance history vs memory |
| Copy on Select | On | Instant clipboard |
| Status Bar | On | directory / git / CPU / memory |

紫微星系 profile additionally has:
- Tab color: #9333EA (紫微·紫)
- Badge: ✦ + session name
- Transparency: 3% + blur
- Cursor guide line (紫微 purple, 8% opacity)

---

## Maintenance

### Re-apply after iTerm2 resets
iTerm2 writes its in-memory state on quit, which can overwrite plist changes.
Safe procedure:
1. Quit iTerm2 (or `kill -9 $(pgrep -x iTerm2)`)
2. `python3 ~/.config/iterm2_configure.py`
3. `open -a iTerm`

### Edit colors
Modify `ANSI_16` dict in `~/.config/iterm2_configure.py`, then re-run.

### Edit Claude Code theme
Edit `~/.claude/themes/ziwei.json` directly — Claude Code hot-reloads on file change.

### Regenerate starship cache
After editing `~/.config/starship.toml`:
```bash
starship init zsh > ~/.starship_init.zsh
```
Or just open a new shell — the cache check in `.zshrc` handles it automatically.

---

*Configuration created 2026-05-07. 紫微星系 · 杀破狼格局.*
