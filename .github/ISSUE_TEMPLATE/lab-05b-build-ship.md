---
name: "Lab 05b: Build and Ship It"
about: "Execute your wave plan with /nextwave and ship a working MCP server"
labels: ["lab"]
---

**Start branch:** `lab/05-start`
**Solution tag:** `lab/05b-solution`
**Session replay:** `labs/05b/session.jsonl`
**Curated session:** `lab-05b-build-and-ship-it`

## Objective
Execute the wave plan you created in Lab 05a. Watch agents implement your design in parallel, review their work, merge PRs, and end up with a working MCP server registered in your Claude Code session.

This lab teaches the **execution phase** of the workflow.

## Prerequisites
- [x] ccwork kit installed (`install.sh --check` all green)
- [ ] This repo forked and cloned
- [ ] Completed Lab 05a (required — you need a wave plan to execute)

## Steps

### Step 1: Verify your plan is ready
**Do:** Check that your `/prepwaves` plan from Lab 05a is still active. Review the wave map and confirm the issues are ready.
**Verify:** Task list shows wave tasks with issue references
**Learn:** Plans survive between sessions via the task list. If context was lost, `/engage` restores it.

### Step 2: Execute Wave 1
**Do:** Run `/nextwave`. Watch what happens:
- Pre-flight checks verify the branch is clean
- Planning agents analyze each issue and report file targets
- Issues are partitioned into flights (conflict-free groups)
- Execution agents implement each issue on isolated worktrees
- Pre-commit checklists are presented for your review
**Verify:** Wave 1 PRs are merged to main
**Learn:** The flight model prevents merge conflicts by detecting file-level overlaps before agents start coding. Planning before execution — the same principle from Lab 05a, applied at the code level.

### Step 3: Execute remaining waves
**Do:** Run `/nextwave` again for each remaining wave. Between waves, notice:
- Re-validation agents check if previous merges affect upcoming work
- Feature branches are rebased onto updated main
- Agents read fresh code, not stale snapshots
**Verify:** All waves complete, all PRs merged
**Learn:** Each wave builds on the previous one's merged code. This is why dependency order matters — Wave 2 agents see Wave 1's work because it's already on main.

### Step 4: Install your MCP server
**Do:** Register your server with Claude Code:
```bash
claude mcp add --scope project --transport stdio my-server -- bun index.ts
```
**Verify:** `claude mcp list` shows your server. Start a new Claude Code session and ask Claude to use one of your tools.
**Learn:** MCP servers are registered per-project or per-user. The `--transport stdio` flag means your server communicates over stdin/stdout — the simplest and most common transport.

### Step 5: Test it for real
**Do:** In a Claude Code session, ask Claude to use each of your server's tools. Verify the results are correct.
**Verify:** All tools respond correctly when called by Claude
**Learn:** The ultimate test — not "does the test suite pass" but "does it actually work when Claude calls it?" This is why the workflow insists on testing scripts, not just linting them.

### Step 6: Retrospective
**Do:** Review what happened:
- How closely did the implementation match your PRD?
- Did any agent escalate a design issue?
- Were there merge conflicts between flights?
- How did the pre-commit review findings look?
**Verify:** You can articulate one thing you'd do differently in the design phase
**Learn:** Design quality determines execution quality. Vague specs produce agents that guess. Precise specs produce agents that execute. The retrospective closes the feedback loop.

## You Learned
- [ ] Wave execution with /nextwave
- [ ] Flight partitioning and conflict avoidance
- [ ] Pre-commit review and approval workflow
- [ ] Inter-wave re-validation
- [ ] MCP server registration and testing
- [ ] The full design-to-ship lifecycle

## Congratulations
You've completed the full Claude Code workflow — from PRD to running code, with parallel agent execution, automated code review, and wave-based delivery. The MCP server you built is yours to keep and extend.

## Stuck?
Watch the curated walkthrough on [Clawback](https://clawback.apps.oakai.waveeng.com/?session=lab-05b-build-and-ship-it&autoplay=true) — an example execution session.
