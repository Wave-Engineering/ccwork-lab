"""Simple script that prints agent identity information.

This is the starting point for Lab 02: Identity and Check-In.
The learner will modify this to display their session identity.
"""

import hashlib
import json
import subprocess


def get_project_root() -> str:
    """Get the git repository root directory."""
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else "."


def get_agent_identity() -> dict:
    """Read the agent identity file for this project.

    Returns:
        dict with dev_team, dev_name, dev_avatar (or empty dict if not found).
    """
    project_root = get_project_root()
    dir_hash = hashlib.md5(project_root.encode()).hexdigest()
    agent_file = f"/tmp/claude-agent-{dir_hash}.json"

    try:
        with open(agent_file) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def main():
    """Print agent identity -- to be updated by the learner."""
    # TODO: Update this to print your Dev-Name and Dev-Team
    print("Hello from ccwork-lab!")
    print("Run /name to see your agent identity, then update this script.")


if __name__ == "__main__":
    main()
