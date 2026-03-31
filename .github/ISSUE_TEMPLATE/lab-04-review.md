---
name: "Lab 04: Code Review"
about: "Use /review to catch quality issues, interpret findings, and fix them"
labels: ["lab"]
---

**Start branch:** `lab/04-start`
**Init tag:** `lab/04-init`
**Solution tag:** `lab/04-solution`
**Session replay:** `labs/04/session.jsonl`
**Curated session:** `lab-04-code-review`

## Objective
Learn how to use `/review` to catch code quality issues, interpret findings by severity, and fix them before they ship.

## Prerequisites
- [x] ccwork kit installed (`install.sh --check` all green)
- [ ] This repo forked/created from template and cloned
- [ ] Completed Labs 01-03 (recommended)

## Steps

### Step 1: Explore the flawed code
**Do:** Run `/view src/formatter.py` to open the code in your editor. Notice the style violations, dead code, and subtle bugs.
**Verify:** You can identify at least 2 issues by reading the code
**Learn:** Code review isn't just about style — it catches logic bugs that tests might miss.

### Step 2: Run the tests
**Do:** Run `pytest tests/test_formatter.py`
**Verify:** All tests pass — despite the code issues
**Learn:** Passing tests don't mean clean code. Tests verify behavior; review verifies quality.

### Step 3: Run /review
**Do:** Run `/review` on the source code.
**Verify:** The reviewer reports findings with severity ratings
**Learn:** The code-reviewer agent uses confidence-based filtering — it only reports issues it's sure about, rated by risk level.

### Step 4: Categorize the findings
**Do:** Read each finding. Categorize as: critical (must fix), important (should fix), or cosmetic (nice to fix).
**Verify:** You can explain why each finding matters or doesn't
**Learn:** Not all findings are equal. Critical findings block commits; cosmetic ones are judgment calls.

### Step 5: Fix the high-risk findings
**Do:** Fix all findings rated high risk or above. Leave cosmetic ones for now.
**Verify:** Re-run `/review` — no high-risk findings remain
**Learn:** The precheck gate requires high-risk findings to be resolved before commit.

### Step 6: Commit via the workflow
**Do:** Run `/precheck`, then choose your commit skill after approval.
**Verify:** Clean commit with code review passed in the checklist
**Learn:** Code review is built into the pre-commit gate — it's not optional, it's structural.

### Step 7: Exercise — make your own judgment calls
**Do:** Now address the remaining cosmetic findings. For each one, decide: fix it, or leave it and explain why. Create an issue for the work using `/issue chore` — describe the cosmetic cleanup and your judgment rationale. Then commit your decisions via the full workflow.
**Verify:** You can justify each decision (fix or leave) with a clear reason
**Learn:** Senior engineering judgment isn't about following every rule — it's about knowing when a rule serves the code and when it doesn't.

## You Learned
- [ ] How /review works and what it checks
- [ ] Confidence-based severity filtering
- [ ] The difference between "tests pass" and "code is clean"
- [ ] How code review integrates into the precheck gate
- [ ] Making and justifying judgment calls on findings
- [ ] Using /issue to track even small decisions
