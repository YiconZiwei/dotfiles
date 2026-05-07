#!/bin/sh
# Claude Code status line — 紫微星系 palette
# Uses ANSI color indices matching iTerm2 十六星曜 mapping:
#   5=紫微·紫  8=天刑·铁  4=天机·蓝  3=武曲·金  1=七杀·红  2=天梁·绿

input=$(cat)

dir=$(echo "$input" | jq -r '.workspace.current_dir // .cwd')
basename=$(basename "$dir")
model=$(echo "$input" | jq -r '.model.display_name // ""')
used=$(echo "$input" | jq -r '.context_window.used_percentage // empty')

# 紫微斗数 ANSI colors (indices match iTerm2 profile)
ZIWEI='\033[35m'       # 5 紫微·紫 (magenta)
TIANJI='\033[34m'      # 4 天机·蓝 (blue)
TIANXING='\033[90m'    # 8 天刑·铁 (bright black / gray)
WUQU='\033[33m'        # 3 武曲·金 (yellow)
QISHA='\033[31m'       # 1 七杀·红 (red)
TIANLIANG='\033[32m'   # 2 天梁·绿 (green)
RESET='\033[0m'

# Context usage color: green < 60%, gold < 80%, red >= 80%
ctx_part=""
if [ -n "$used" ]; then
  ctx_color="$TIANLIANG"
  used_int=$(printf '%.0f' "$used" 2>/dev/null || echo 0)
  [ "$used_int" -ge 60 ] && ctx_color="$WUQU"
  [ "$used_int" -ge 80 ] && ctx_color="$QISHA"
  ctx_part=" ${ctx_color}ctx:${used}%${RESET}"
fi

printf "${ZIWEI}✦ %s${RESET} ${TIANXING}%s${RESET}%s" "$basename" "$model" "$ctx_part"
