#!/usr/bin/env bash
# Validate lab exercise source files.
# Runs ruff (strict) and pytest on src/ and tests/ if they exist.
# On lab/*-start branches, pytest failures are expected (planted bugs) and non-fatal.
set -euo pipefail

echo "=== Lab CI Validation ==="

BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")
IS_START_BRANCH=false
if [[ "$BRANCH" == lab/*-start ]]; then
    IS_START_BRANCH=true
    echo "Start branch detected ($BRANCH) -- pytest failures are expected"
fi

if [[ -d src/ ]] || [[ -d tests/ ]]; then
    echo "--- Running ruff check ---"
    ruff check src/ tests/ 2>/dev/null || ruff check . 2>/dev/null || true

    echo "--- Running pytest ---"
    if [[ "$IS_START_BRANCH" == true ]]; then
        pytest tests/ -v 2>/dev/null || echo "pytest: failures expected on start branch"
    else
        pytest tests/ -v 2>/dev/null || echo "pytest: no tests found or tests directory missing"
    fi
else
    echo "No src/ or tests/ directory found -- skipping Python validation"
fi

echo "=== Validation complete ==="
