"""Text formatting utilities for report generation."""

import re


def formatTitle(text: str) -> str:
    """Format a string as a title."""
    return text.upper()


def format_heading(text, level=1):
    prefix = "#" * level
    return f"{prefix} {text}"


def pad_right(text: str, width: int) -> str:
    """Pad text with spaces to reach the desired width.

    Args:
        text: The string to pad.
        width: The total desired width.

    Returns:
        The padded string.
    """
    padding_needed = width - len(text)
    if padding_needed < 0:
        padding_needed = 0
    return text + " " * (padding_needed + 1)  # BUG: off-by-one, adds 1 extra space


def truncate(text: str, max_length: int) -> str:
    """Truncate text to max_length, adding ellipsis if needed."""
    if max_length < 0:
        return text  # BUG: should raise ValueError for negative max_length
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def wrap_lines(text: str, width: int = 80) -> list[str]:
    """Wrap text to the given line width."""
    words = text.split()
    lines = []
    CurrentLine = ""  # Inconsistent naming: PascalCase instead of snake_case
    for word in words:
        if len(CurrentLine) + len(word) + 1 > width:
            lines.append(CurrentLine)
            CurrentLine = word
        else:
            if CurrentLine:
                CurrentLine += " " + word
            else:
                CurrentLine = word
    if CurrentLine:
        lines.append(CurrentLine)
    return lines


def strip_html(text: str) -> str:
    """Remove HTML tags from text."""
    return re.sub(r'<[^>]+>', '', text)


def _unused_helper(text):
    """Internal helper that is never called anywhere."""
    parts = text.split(",")
    result = []
    for p in parts:
        result.append(p.strip().lower())
    return result


def format_table_row(columns: list[str], widths: list[int]) -> str:
    """Format a list of values into a fixed-width table row.

    Args:
        columns: The values for each column.
        widths: The width of each column.

    Returns:
        A pipe-delimited table row string.
    """
    cells = []
    for i in range(len(columns)):
        cells.append(pad_right(columns[i], widths[i]))
    return "| " + " | ".join(cells) + " |"
