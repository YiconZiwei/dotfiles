# 紫微星系 · Dotfiles

Terminal configuration for iTerm2 + Claude Code + Starship, unified under the 紫微斗数 十六星曜 color system.

## Structure
```
config/
  iterm2_configure.py     → ~/.config/     iTerm2 plist configurator
  iterm2-ziwei-README.md  → ~/.config/     Full color map documentation
  starship.toml           → ~/.config/     Starship prompt theme
claude/
  themes/ziwei.json       → ~/.claude/themes/  Claude Code custom theme
  statusline-command.sh   → ~/.claude/         Claude Code status line
zsh/
  zshrc                   → ~/.zshrc       Shell config
```

## Install
```bash
# Link files to their expected locations
cp config/iterm2_configure.py ~/.config/
cp config/starship.toml ~/.config/
cp claude/themes/ziwei.json ~/.claude/themes/
cp claude/statusline-command.sh ~/.claude/
cp zsh/zshrc ~/.zshrc

# Apply iTerm2 settings (close iTerm2 first)
python3 ~/.config/iterm2_configure.py

# Regenerate starship cache
source ~/.zshrc
```

See `config/iterm2-ziwei-README.md` for the full color palette reference.
