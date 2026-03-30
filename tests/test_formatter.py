"""Tests for the formatter module.

These tests verify functional behavior. They will pass even though the
source code has style issues — that's the point of Lab 04. Passing tests
don't mean clean code.
"""

from src.formatter import (
    format_heading,
    format_table_row,
    formatTitle,
    strip_html,
    truncate,
    wrap_lines,
)


def test_format_title():
    assert formatTitle("hello world") == "HELLO WORLD"
    assert formatTitle("") == ""
    assert formatTitle("Already UPPER") == "ALREADY UPPER"


def test_format_heading():
    assert format_heading("Title") == "# Title"
    assert format_heading("Sub", level=2) == "## Sub"
    assert format_heading("Deep", level=4) == "#### Deep"


def test_truncate_short_text():
    assert truncate("hi", 10) == "hi"


def test_truncate_long_text():
    assert truncate("hello world this is long", 10) == "hello w..."


def test_wrap_lines():
    text = "the quick brown fox jumps over the lazy dog"
    lines = wrap_lines(text, width=20)
    assert all(len(line) <= 20 for line in lines)
    assert " ".join(lines) == text


def test_strip_html():
    assert strip_html("<b>bold</b>") == "bold"
    assert strip_html("no tags here") == "no tags here"
    assert strip_html("<p>one</p><p>two</p>") == "onetwo"


def test_format_table_row():
    row = format_table_row(["Name", "Age"], [10, 5])
    assert row.startswith("| ")
    assert row.endswith(" |")
    assert "Name" in row
    assert "Age" in row
