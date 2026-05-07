# Global Context · 紫微星系

## System
- macOS (Apple Silicon) · zsh 5.9 · bash 3.2
- Homebrew: /opt/homebrew
- Python: brew 3.13 (`/opt/homebrew/bin/python3.13`) — Apple 3.9 deprecated
- Rust: stable via rustup (`~/.cargo/bin`)
- Node: project-local only (no global install)
- Terminal: iTerm2 (primary, 紫微星系 profile) · Warp · Ghostty
- Git host: GitHub (`YiconZiwei`)

## Coding Conventions
- Commits: conventional (`feat:`, `fix:`, `docs:`, `chore:`)
- Python: type hints, docstrings, ruff lint
- Rust: cargo clippy + cargo fmt
- Shell: shellcheck-clean, `set -euo pipefail` in scripts
- Always verify changes compile/run before committing
- Never commit secrets, `.env`, or API keys

## Project Layout
- `~/Ziwei/` — monorepo (紫微AI星系), project CLAUDE.md has star system context
- `~/.dotfiles/` — terminal configs (iTerm2, starship, zsh, bash, Claude themes)

## Preferences
- Language: match the user (中文→中文, English→English)
- Be concise — power user, 700+ sessions
- Shell aliases available: `gst` `glog` `gd` `ll` `mkcd` `portfind` `portkill`
- Starship cached — regen: `starship init zsh > ~/.starship_init.zsh`
- iTerm2 config script: `python3 ~/.config/iterm2_configure.py` (close iTerm2 first)