---
name: "Lab 03: Identity and Check-In"
about: "Learn agent identity, /name, /engage, and session setup"
labels: ["lab"]
---

**Start branch:** `lab/03-start`
**Init tag:** `lab/03-init`
**Solution tag:** `lab/03-solution`
**Session replay:** `labs/03/session.jsonl`

## Objective
Understand how Claude Code agents establish identity each session, and how the /engage workflow confirms rules of engagement.

## Prerequisites
- [x] ccwork kit installed (`install.sh --check` all green)
- [ ] This repo forked/created from template and cloned
- [ ] Completed Lab 02 (recommended)

## Steps

### Step 1: Check current identity
**Do:** Run `/name` to see your current session identity.
**Verify:** Output shows Dev-Name, Dev-Avatar, and Dev-Team
**Learn:** Each session picks a fresh identity — Dev-Name and Dev-Avatar are ephemeral.

### Step 2: Inspect the identity file
**Do:** Find and read the agent identity JSON file at `/tmp/claude-agent-<hash>.json`
**Verify:** File contains `dev_team`, `dev_name`, `dev_avatar` fields
**Learn:** Identity is persisted per-project (keyed by repo root hash), not per-process.

### Step 3: Run engage
**Do:** Run `/engage` to confirm rules of engagement.
**Verify:** Agent reads CLAUDE.md and confirms mandatory rules
**Learn:** The /engage workflow ensures the agent has loaded and acknowledged project rules.

### Step 4: Update hello.py
**Do:** Edit `src/hello.py` so `main()` prints your agent's Dev-Name and Dev-Team instead of the placeholder text.
**Verify:** Running `python -m src.hello` outputs your identity, and `pytest tests/test_hello.py` passes
**Learn:** Agent identity is available programmatically for scripts and tools.

### Step 5: Verify the Dev-Team field
**Do:** Check that `CLAUDE.md` has a `Dev-Team:` value set.
**Verify:** `grep 'Dev-Team:' CLAUDE.md` shows a non-empty value
**Learn:** Dev-Team is project-level identity — persisted in CLAUDE.md, shared across sessions.

### Step 6: Exercise — build an identity dashboard
**Do:** Create a new script `src/dashboard.py` that reads the agent identity file and displays a formatted summary: Dev-Name, Dev-Avatar, Dev-Team, project root, and identity file path. Use the full workflow to commit it.
**Verify:** `python -m src.dashboard` shows all identity fields, committed via the workflow
**Learn:** Understanding the identity system lets you build tooling that's agent-aware.

## You Learned
- [ ] Session identity (Dev-Name, Dev-Avatar) is ephemeral
- [ ] Project identity (Dev-Team) is persistent in CLAUDE.md
- [ ] The agent identity file location and format
- [ ] The /engage workflow for rules confirmation
- [ ] How to build on the identity system programmatically
