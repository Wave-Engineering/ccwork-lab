---
name: "Lab 02: Your First Workflow"
about: "Learn the issue → branch → code → precheck → scp → PR → close loop"
labels: ["lab"]
---

**Start branch:** `lab/02-start`
**Init tag:** `lab/02-init`
**Solution tag:** `lab/02-solution`
**Session replay:** `labs/02/session.jsonl`

## Objective
Learn the full mandatory workflow: issue → branch → code → /precheck → /scp → PR → close.

## Prerequisites
- [x] ccwork kit installed (`install.sh --check` all green)
- [ ] This repo forked/created from template and cloned
- [ ] Completed Lab 01 (recommended)

## Steps

### Step 1: Create a branch
**Do:** Create a feature branch for this issue.
**Verify:** `git branch --show-current` starts with `feature/`
**Learn:** Branch naming convention — `<type>/<issue>-<description>`

### Step 2: Find and fix the bug
**Do:** There's an off-by-one bug in `src/calculator.py`. Find it and fix it.
**Verify:** `pytest tests/test_calculator.py` passes
**Learn:** Always run tests before committing — the precheck gate enforces this.

### Step 3: Run precheck
**Do:** Run `/precheck`
**Verify:** Checklist is presented with all items green
**Learn:** The precheck gate — code review, validation, and compliance verification before any commit.

### Step 4: Stage, commit, and push
**Do:** Run `/scp`
**Verify:** Branch is pushed to origin, commit message follows `type(scope): description` convention
**Learn:** The scp workflow — stage, commit, push in one skill.

### Step 5: Create a PR
**Do:** Create a PR targeting `main` using `gh pr create`
**Verify:** PR exists and references this issue with `Closes #N`
**Learn:** PR descriptions link to issues so they auto-close on merge.

### Step 6: Close this issue
**Do:** Merge the PR and verify this issue closes
**Verify:** Issue state is Closed
**Learn:** Issue lifecycle — work is tracked from creation to closure.

### Step 7: Exercise — add a new operation
**Do:** Add a `modulo(a, b)` function to `calculator.py` with proper tests. This time, use `/issue feature` to create the issue — describe what you want to add and the skill will draft a properly structured issue with the right template and labels. Then go through the full workflow: branch, code, precheck, choose your commit skill, PR, merge. Do it without step-by-step prompting — you know the loop now.
**Verify:** New function exists, tests pass, PR merged, issue closed
**Learn:** The second time through the loop should feel natural. `/issue` handles the template and labels so you focus on the work, not the format.

## You Learned
- [ ] Branch naming and issue association
- [ ] The precheck gate
- [ ] The scp workflow
- [ ] PR creation with issue linkage
- [ ] Issue lifecycle
- [ ] Structured issue creation with /issue
- [ ] Confidence to run the loop independently
