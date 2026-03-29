# ccwork-lab

Hands-on training ground for the [Claude Code workflow kit](https://github.com/Wave-Engineering/claudecode-workflow).

## Quick Start

1. **Fork this repo** to your own account
2. **Clone your fork**: `gh repo fork Wave-Engineering/ccwork-lab --clone`
3. **Open Claude Code**: `cd ccwork-lab && claude`
4. **List labs**: `/ccwork lab`
5. **Start a lab**: `/ccwork lab "Your First Workflow"`

## How Labs Work

Each lab is a GitHub Issue Template. When you start a lab, the `/ccwork` skill:

1. Creates an issue from the template in your fork
2. Checks out the lab's starting branch (with planted bugs, missing features, etc.)
3. Guides you through the exercise step by step
4. Verifies your work against a known-good solution
5. Offers a Clawback session replay if you want to see how it was solved

Labs teach by doing -- you create real branches, commits, PRs, and closed issues in your own repo.

## Available Labs

| Lab | What You Learn | Time |
|-----|---------------|------|
| 01 - Your First Workflow | issue -> branch -> code -> precheck -> scp -> PR -> close | ~15 min |
| 02 - Identity and Check-In | /name, agent identity, /engage, session setup | ~10 min |
| 05a - Design Your MCP Server | PRD writing, issue decomposition, /prepwaves, wave planning | ~20 min |
| 05b - Build and Ship It | /nextwave, flight partitioning, code review, MCP registration | ~30 min |

### The Capstone: Labs 05a + 05b

Labs 05a and 05b are an end-to-end project where you design and build your own MCP tool server. Unlike Labs 01-02 which have fixed solutions, **you pick what to build** -- making it a real design exercise, not a tutorial.

- **05a** teaches the design phase: PRD, issue decomposition, wave planning
- **05b** teaches the execution phase: parallel agents, flight partitioning, merge, install

The MCP server you build is yours to keep and use with Claude Code.

## Three Ways to Learn

Each lab supports three learning styles:

- **Do it** -- `/ccwork lab "<name>"` guides you hands-on
- **Watch it** -- Load `labs/NN/session.jsonl` into [Clawback](https://github.com/bakeb7j0/clawback) to watch how it was solved
- **Read it** -- Browse the issue template and solution tag for static reference

## Prerequisites

- [Claude Code workflow kit](https://github.com/Wave-Engineering/claudecode-workflow) installed (`install.sh --check` all green)
- GitHub CLI (`gh`) authenticated
- Python 3.10+ (for lab exercises)
- Bun runtime (for Lab 05 MCP server)

## Adding New Labs

Labs are data, not code. To add a new lab:

1. Create `.github/ISSUE_TEMPLATE/lab-NN-name.md`
2. Create a `lab/NN-start` branch with the starting state
3. Solve the exercise, tag as `lab/NN-solution`
4. Place the session replay at `labs/NN/session.jsonl`
5. Update `LAB.md`

No skill code changes needed -- the `/ccwork lab` handler reads templates dynamically.
