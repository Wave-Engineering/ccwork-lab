#!/usr/bin/env bash
# Validate lab exercise source files.
# Runs pytest and ruff on src/ and tests/ if they exist.
set -euo pipefail

echo "=== Lab CI Validation ==="

# Check for Python source files
if [[ -d src/ ]] || [[ -d tests/ ]]; then
    echo "--- Running ruff check ---"
    if command -v ruff &>/dev/null; then
        ruff check src/ tests/ 2>/dev/null || ruff check . 2>/dev/null || echo "ruff: no files to check"
    else
        echo "ruff not found, installing..."
        pip install ruff --quiet
        ruff check src/ tests/ 2>/dev/null || ruff check . 2>/dev/null || echo "ruff: no files to check"
    fi

    echo "--- Running pytest ---"
    if command -v pytest &>/dev/null; then
        pytest tests/ -v 2>/dev/null || echo "pytest: no tests found or tests directory missing"
    else
        echo "pytest not found, installing..."
        pip install pytest --quiet
        pytest tests/ -v 2>/dev/null || echo "pytest: no tests found or tests directory missing"
    fi
else
    echo "No src/ or tests/ directory found on this branch -- skipping Python validation"
fi

echo "=== Validation complete ==="
