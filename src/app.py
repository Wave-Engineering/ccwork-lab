"""A simple application — your starting point for Lab 01: Project Setup.

This project has no CLAUDE.md yet. Your first task is to set one up
using /ccfold and configure it for this project.
"""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}! Welcome to ccwork-lab."


def main():
    """Run the application."""
    print(greet("developer"))
    print("This project needs a CLAUDE.md — run /ccfold to set one up.")


if __name__ == "__main__":
    main()
