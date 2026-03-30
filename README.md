# ccwork-lab

Hands-on training ground for the [Claude Code workflow kit](https://gitlab.com/waveeng/claudecode-workflow).

> **Also available on GitHub:** [github.com/Wave-Engineering/ccwork-lab](https://github.com/Wave-Engineering/ccwork-lab)

## Quick Start

1. **Fork this project** — click "Fork" on GitLab to create your own copy
2. **Clone your fork**: `git clone <your-fork-url>`
3. **Open Claude Code**: `cd ccwork-lab && claude`
4. **Start the first lab**: `/ccwork lab "Project Setup"`

## Available Labs

| Lab | What You Learn | Time |
|-----|---------------|------|
| 01 - Project Setup | /ccfold, CLAUDE.md, /engage, Dev-Team | ~15 min |
| 02 - Your First Workflow | issue → branch → code → precheck → scp → MR → close | ~15 min |
| 03 - Identity and Check-In | /name, agent identity, /engage, session setup | ~10 min |
| 04 - Code Review | /review, severity ratings, fixing findings | ~15 min |
| 05a - Design Your MCP Server | PRD writing, issue decomposition, /prepwaves | ~20 min |
| 05b - Build and Ship It | /nextwave, flight partitioning, MCP registration | ~30 min |

### The Capstone: Labs 05a + 05b

Labs 05a and 05b are an end-to-end project where you design and build your own MCP tool server. Unlike Labs 01-04 which have guided solutions, **you pick what to build** — making it a real design exercise, not a tutorial.

The MCP server you build is yours to keep and use with Claude Code.

## Three Ways to Learn

Each lab supports three learning styles:

- **Do it** — `/ccwork lab "<name>"` guides you hands-on
- **Watch it** — Load `labs/NN/session.jsonl` into [Clawback](https://github.com/bakeb7j0/clawback) to watch how it was solved
- **Read it** — Browse the issue template and solution tag for static reference

## Lab Branches and Tags

Each lab has a starting branch, an init tag (immutable reset point), and a solution tag:

```
lab/01-start    → lab/01-init (tag)    → lab/01-solution (tag)
lab/02-start    → lab/02-init (tag)    → lab/02-solution (tag)
...
```

If you need to reset a lab: `git checkout -B lab/NN-start lab/NN-init`

## Prerequisites

- [Claude Code workflow kit](https://gitlab.com/waveeng/claudecode-workflow) installed (`install.sh --check` all green)
- GitLab CLI (`glab`) authenticated
- Python 3.10+ (for lab exercises)
- Bun runtime (for Lab 05 MCP server)
