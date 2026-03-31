---
name: "Lab 05a: Design Your MCP Server"
about: "Write a PRD, decompose into wave-quality issues, and plan parallel execution"
labels: ["lab"]
---

**Start branch:** `lab/05-start`
**Solution tag:** `lab/05a-solution`
**Session replay:** `labs/05a/session.jsonl`
**Curated session:** `lab-05a-design-your-mcp-server`

## Objective
Design an MCP (Model Context Protocol) tool server from scratch. You'll pick a domain, write a PRD, decompose it into issues, and plan wave-based parallel execution — all before writing a single line of implementation code.

This lab teaches the **design phase** of the workflow. Lab 05b continues with execution.

## Prerequisites
- [x] ccwork kit installed (`install.sh --check` all green)
- [ ] This repo forked and cloned
- [ ] Completed Labs 01 and 02 (recommended)

## What is MCP?

The Model Context Protocol lets you give Claude Code new capabilities by building tool servers. Your server runs locally, communicates over stdio, and exposes tools that Claude can call during a session. Think of it as writing plugins for your AI assistant.

The start branch includes a scaffold: an empty MCP server that starts, responds to `tools/list` with nothing, and exits cleanly. Your job is to design what it should actually do.

## Steps

### Step 1: Pick your domain
**Do:** Think about what tools would be useful to YOU in a Claude Code session. Some ideas:
- A server that queries your todo list, calendar, or notes app
- A server that looks up documentation for your team's internal APIs
- A server that runs database queries and formats results
- A server that manages git worktrees or branch housekeeping
- A server that interacts with a local service (Home Assistant, Pi-hole, etc.)

Tell Claude what you want to build. Discuss scope — aim for 2-3 tools, not 10.
**Verify:** You can describe your server in one sentence: "An MCP server that ____"
**Learn:** Scoping is the hardest part of design. A focused server with 2-3 great tools beats a sprawling one with 10 mediocre tools.

### Step 2: Write the PRD
**Do:** Work with Claude to write a PRD using the template in `docs/PRD-template.md`. Cover:
- What tools the server provides (name, description, parameters, return values)
- What resources it exposes (if any)
- How it's configured (env vars, config files, etc.)
- How it's tested
- How it's registered with Claude Code
**Verify:** Your PRD has: Summary, Tools section with schemas, Test Plan, and Success Metrics
**Learn:** A PRD is a contract between you (the designer) and the agent (the implementer). Vague PRDs produce vague code. Precise PRDs produce precise code.

### Step 3: Decompose into issues
**Do:** Work with Claude to dice the PRD into implementation issues. Each issue should follow the project's story template with Changes, Tests, and Acceptance Criteria. Aim for 4-6 issues across 2-3 waves.

Typical decomposition:
- **Wave 1:** Server scaffold + first tool (the simplest one)
- **Wave 2:** Remaining tools (parallel if they don't share files) + configuration
- **Wave 3:** Integration tests + documentation + registration script

**Verify:** Each issue has: Implementation Steps (paint-by-numbers), Test Procedures, and Acceptance Criteria that an agent could execute without asking questions
**Learn:** Wave-quality specs mean the agent never has to make design decisions. If an issue says "implement as you see fit," it's underspecified.

### Step 4: Map dependencies and plan waves
**Do:** Run `/prepwaves` with your master issue. Review the dependency graph and wave plan.
**Verify:** `/prepwaves` produces a wave plan with at least 2 waves and some parallelism
**Learn:** Dependencies determine wave order. Independent issues run in parallel. The more precise your specs, the better the planner can partition.

### Step 5: Review and approve
**Do:** Read through the wave plan. Check that:
- No issue requires design decisions
- Dependencies are correct (nothing runs before its prerequisite)
- Wave 2+ issues don't duplicate Wave 1 work
- Test coverage is complete
**Verify:** You've approved the `/prepwaves` plan
**Learn:** This is the last gate before agents start writing code. Everything after this is execution. If the plan is wrong, the code will be wrong — faster.

## You Learned
- [ ] How to scope an MCP server to a useful but buildable size
- [ ] PRD writing as a practical design skill
- [ ] Issue decomposition with wave-quality specs
- [ ] Dependency mapping and wave planning with /prepwaves
- [ ] The design-then-execute mental model

## What's Next
Continue to **Lab 05b: Build and Ship It** to execute your plan with `/nextwave` and end up with a working MCP server.

## Stuck?
Watch the curated walkthrough on [Clawback](https://clawback.apps.oakai.waveeng.com/?session=lab-05a-design-your-mcp-server&autoplay=true) — an example design session for a dice-roller + unit-converter MCP server.
