# Project Instructions for Claude Code

This is the **ccwork-lab** training repository — a hands-on training ground
for learning the Claude Code workflow kit.

## Platform

This project is on **GitHub**. Use `gh` CLI for all operations.

## Project Structure

- `LAB.md` — marker file listing available labs and completion status
- `.github/ISSUE_TEMPLATE/lab-*.md` — lab exercise templates
- `labs/NN/session.jsonl` — Clawback session replays for each lab
- `src/` — source files (vary per lab branch)
- `tests/` — test files (vary per lab branch)
- `scripts/ci/` — CI validation scripts

## Branching Strategy

```
main (protected)
  ├── feature/NNN-description
  └── fix/NNN-description
```

Always branch from `main` or the lab's start branch.

## Testing

```bash
pytest tests/
ruff check src/ tests/
```

## Commit Convention

```
type(scope): brief description

Closes #NNN
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Mandatory Rules

1. **Always have an issue** — never begin work without one
2. **Test before push** — run `pytest` and `ruff check` before pushing
3. **Pre-commit gate** — run `/precheck` before committing

Dev-Team: ccwork-lab
