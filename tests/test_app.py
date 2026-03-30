"""Tests for the app module."""

from src.app import greet


def test_greet():
    result = greet("BJ")
    assert "BJ" in result
    assert "Hello" in result


def test_greet_empty():
    result = greet("")
    assert "Hello" in result
