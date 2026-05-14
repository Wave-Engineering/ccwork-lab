---
name: "Lab 06: Your First Wave"
about: "Learn the wave pattern with a 2-issue serial wave on ccwork-testtarget"
labels: ["lab"]
---

**Start branch:** `lab/06-start`
**Init tag:** `lab/06-init`
**Solution tag:** `lab/06-solution`
**Session replay:** `labs/06/session.jsonl`
**Curated session:** `lab-06-your-first-wave`

## Objective
Learn the wave-pattern execution pipeline: create issues → assess → plan → execute → verify merge. Uses a 2-issue serial wave on the ccwork-testtarget sandbox repo.

## Prerequisites
- [x] ccwork kit installed (`install.sh --check` all green)
- [ ] Completed Lab 02 (mandatory — you must know the basic workflow loop)
- [ ] GitHub CLI authenticated (`gh auth status`)
- [ ] Access to `Wave-Engineering/ccwork-testtarget` repo (or fork it)

## Context

The wave pattern decomposes work into dependency-ordered batches and executes each batch with lifecycle tracking. Even fully sequential work benefits from the dashboard, audit trail, and structured execution. This lab uses the simplest possible wave: 2 issues, serial topology (one depends on the other).

**Target repo:** `Wave-Engineering/ccwork-testtarget` — a sandbox repo designed for safe experimentation. Nothing you do here affects real projects.

## Steps

### Step 1: Create two issues on ccwork-testtarget
**Do:** Create two feature issues in the ccwork-testtarget repo. The second should depend on the first.

Example issues:
- Issue A: "Add greeting module" — create `src/greeting.py` with a `hello(name)` function
- Issue B: "Add farewell module using greeting" — create `src/farewell.py` that imports from greeting

Use `/issue feature` for each, targeting the `ccwork-testtarget` repo. Make sure Issue B has a `**Dependencies:** #A` line in its body.

**Verify:** Two issues exist in ccwork-testtarget with proper structure (Changes / Tests / AC sections). Issue B references Issue A as a dependency.
**Learn:** Wave planning reads the `Dependencies` field to determine execution order. Without it, both issues would land in the same wave (parallel).

### Step 2: Assess wave suitability
**Do:** Run `/assesswaves` with both issue numbers from ccwork-testtarget.
**Verify:** The assessment returns a verdict card showing: wave-able = yes, topology = serial, 2 waves (A in wave 1, B in wave 2).
**Learn:** `/assesswaves` is the quick triage — it tells you whether wave-pattern execution makes sense and what shape it would take. Serial is a valid topology; waves provide tracking and audit trail regardless of parallelism.

### Step 3: Create a Plan tracking issue
**Do:** Create a Plan tracking issue in ccwork-testtarget that references both sub-issues. Use `/issue plan` or create manually with the `type::plan` label. The body should list both issues.
**Verify:** Plan issue exists with `type::plan` label and both sub-issues referenced.
**Learn:** The Plan is the top-level container. `/prepwaves` reads it to find sub-issues.

### Step 4: Plan the waves
**Do:** Run `/prepwaves #<plan-number>` (using the Plan issue number from Step 3).
**Verify:** Pre-flight table shows both issues as READY. Wave plan shows Wave 1 (Issue A) → Wave 2 (Issue B). `wave-status show` reports the plan.
**Learn:** `/prepwaves` validates specs, computes topological sort from dependencies, and persists the plan. It refuses to include issues with missing Changes/Tests/AC sections.

### Step 5: Execute Wave 1
**Do:** Run `/nextwave`
**Verify:** A Flight Agent implements Issue A (greeting module). After completion, the PR is created, CI passes, and it merges. `wave-status show` reports Wave 1 as complete.
**Learn:** `/nextwave` picks the next pending wave and executes it. In serial topology, one flight per wave — straightforward. The Flight Agent reads the issue spec, implements it, runs precheck, and reports PASS/FAIL.

### Step 6: Execute Wave 2
**Do:** Run `/nextwave` again.
**Verify:** A Flight Agent implements Issue B (farewell module that imports greeting). It can see the greeting module because Wave 1 already merged. PR created, CI passes, merges. `wave-status show` reports all waves complete.
**Learn:** Serial ordering guarantees Wave 2 can build on Wave 1's output. The dependency you declared in Step 1 ensured this ordering.

### Step 7: Verify the result
**Do:** Check both issues are closed, both PRs are merged, and `wave-status show` reports the plan as complete.
**Verify:** Both issues closed, both PRs merged, wave-status shows all waves done.
**Learn:** The wave pattern provides end-to-end traceability: Plan → Wave → Flight → PR → merged commit. Every decision is tracked, every merge is gated by CI.

## You Learned
- [ ] How to create issues with dependency relationships
- [ ] `/assesswaves` — quick triage for wave suitability
- [ ] `/prepwaves` — spec validation and wave planning
- [ ] `/nextwave` — single-wave execution
- [ ] Serial wave topology (dependency-ordered sequential execution)
- [ ] `wave-status show` — monitoring wave progress
- [ ] The Plan → Wave → Flight → PR traceability chain

## Going Further
- Try a **parallel** wave: create 2 independent issues (no dependencies) and watch them execute on isolated worktrees simultaneously
- Try `/wavemachine` for automated multi-wave execution
- Run `/ccwork tour advanced` for the full pipeline walkthrough
- See the [KAHUNA Guide](https://github.com/Wave-Engineering/claudecode-workflow/blob/main/docs/kahuna-guide.md) for the integration-branch pattern used in autonomous runs
