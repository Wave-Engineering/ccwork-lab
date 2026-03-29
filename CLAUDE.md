# Project Instructions for Claude Code

This is the **ccwork-lab** training repository. It contains hands-on lab exercises
for learning the Claude Code workflow kit.

## Project Structure

- `LAB.md` -- marker file listing available labs and completion status
- `.github/ISSUE_TEMPLATE/lab-*.yml` -- lab exercise templates
- `labs/NN/session.jsonl` -- Clawback session replays for each lab
- `src/` -- source files (vary per lab branch)
- `tests/` -- test files (vary per lab branch)
- `scripts/ci/` -- CI validation scripts

## Lab Branches

Each lab has a starting branch and a solution tag:

- `lab/01-start` -- Your First Workflow (planted bug in calculator)
- `lab/02-start` -- Identity and Check-In (clean state)
- `lab/01-solution` -- Solution tag for lab 01
- `lab/02-solution` -- Solution tag for lab 02

## Testing

```bash
pytest tests/
ruff check src/ tests/
```

## Commit Convention

```
type(scope): brief description
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
