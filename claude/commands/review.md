Review the staged changes (`git diff --staged`) and check for:
1. **Logic errors** — off-by-one, null/undefined handling, race conditions
2. **Security** — hardcoded secrets, SQL injection, path traversal, unsafe input
3. **Style** — naming consistency, dead code, missing type hints/docstrings
4. **Tests** — are new paths tested? Any edge cases missing?
5. **Performance** — unnecessary loops, N+1 queries, large allocations

Output a brief verdict: ✅ PASS / ⚠️ CONDITIONAL (with fixes) / 🔴 REJECT (with reasons).
