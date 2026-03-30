---
name: "Lab 01: Project Setup"
about: "Set up CLAUDE.md with /ccfold, configure Dev-Team, and learn /engage"
labels: ["lab"]
---

**Start branch:** `lab/01-start`
**Init tag:** `lab/01-init`
**Solution tag:** `lab/01-solution`
**Session replay:** `labs/01/session.jsonl`

## Objective
Set up a project for Claude Code workflow development. Learn how `/ccfold` generates CLAUDE.md, how platform detection works, and how `/engage` confirms the rules of engagement.

## Prerequisites
- [x] ccwork kit installed (`install.sh --check` all green)
- [ ] This repo forked/created from template and cloned

## Steps

### Step 1: Observe the missing CLAUDE.md
**Do:** Check if CLAUDE.md exists in the project root.
**Verify:** No CLAUDE.md file exists
**Learn:** Without CLAUDE.md, the agent has no project-specific rules — no branching strategy, no pre-commit gate, no issue tracking workflow.

### Step 2: Run /ccfold
**Do:** Run `/ccfold` to generate CLAUDE.md from the upstream template.
**Verify:** CLAUDE.md exists and contains platform detection, branching strategy, and mandatory rules
**Learn:** `/ccfold` detects your platform (GitHub/GitLab), generates `.claude-project.md` for cached config, and installs the full rule set.

### Step 3: Inspect the generated files
**Do:** Read CLAUDE.md and `.claude-project.md`. Understand:
- How platform detection works (git remote URL → GitHub/GitLab)
- The branching strategy (trunk-based flow)
- The mandatory gates (pre-commit, issue tracking, testing before push)
**Verify:** You can explain what each mandatory section enforces
**Learn:** CLAUDE.md is the agent's constitution — it overrides default behavior and establishes the workflow contract.

### Step 4: Set the Dev-Team field
**Do:** Find the `Dev-Team:` field in CLAUDE.md and set it to a team name of your choice.
**Verify:** `grep 'Dev-Team:' CLAUDE.md` shows your team name
**Learn:** Dev-Team is project-level identity — shared across all sessions, used for Discord check-in and cross-agent addressing.

### Step 5: Run /engage
**Do:** Run `/engage` to confirm rules of engagement.
**Verify:** Agent reads CLAUDE.md and confirms it has loaded and understood the mandatory rules
**Learn:** `/engage` is the handshake — the agent proves it has read and will follow the project rules.

### Step 6: Exercise — customize a rule
**Do:** Add a project-specific section to CLAUDE.md. For example, add a "## Project Conventions" section with a rule like "All functions must have docstrings" or "Prefer list comprehensions over map/filter." Then make a small code change to `src/app.py` that follows your new rule, using the full workflow (create issue, branch, precheck, scp).
**Verify:** The change follows both the standard workflow rules AND your custom rule
**Learn:** CLAUDE.md is extensible — teams add project-specific conventions that the agent enforces alongside the standard gates. Your custom rules have the same weight as the built-in ones.

## You Learned
- [ ] What CLAUDE.md does and why it matters
- [ ] How /ccfold generates project configuration
- [ ] Platform detection (GitHub vs GitLab)
- [ ] Dev-Team identity and its purpose
- [ ] The /engage handshake
- [ ] How to extend CLAUDE.md with custom rules
