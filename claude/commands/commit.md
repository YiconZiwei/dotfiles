Generate a conventional commit for the current staged changes:
1. Run `git diff --staged --stat` to see what files changed
2. Run `git diff --staged` to understand the actual changes
3. Generate a commit message following conventional commits format:
   - `feat:` new feature
   - `fix:` bug fix
   - `docs:` documentation
   - `chore:` maintenance
   - `refactor:` code restructuring
   - Include scope if obvious, e.g. `feat(auth):`
4. Body should explain WHY, not WHAT (the diff shows what)
5. Show the proposed message and ask for confirmation before committing
