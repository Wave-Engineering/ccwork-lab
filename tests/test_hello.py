"""Tests for the hello module."""

import subprocess
import sys

from src.hello import get_project_root


def test_get_project_root():
    """Project root should return a non-empty string."""
    root = get_project_root()
    assert isinstance(root, str)
    assert len(root) > 0


def test_main_prints_identity():
    """main() should print agent identity, not the default placeholder."""
    result = subprocess.run(
        [sys.executable, "-m", "src.hello"],
        capture_output=True,
        text=True,
    )
    output = result.stdout
    # The default placeholder must be replaced with real identity output
    assert "Hello from ccwork-lab!" not in output, (
        "main() still prints the default placeholder — "
        "update it to display your agent identity"
    )
