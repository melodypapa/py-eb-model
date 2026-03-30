"""
Tests for CLI Options Registry.
"""
import pytest
from eb_model.core.cli_options_registry import CLI_OPTIONS, get_cli_options


def test_cli_options_exists():
    """Test that CLI_OPTIONS dictionary exists."""
    assert isinstance(CLI_OPTIONS, dict)


def test_get_cli_options():
    """Test retrieving CLI options for a parser."""
    options = get_cli_options("OsXdmParser")
    assert isinstance(options, list)


def test_get_cli_options_nonexistent_parser():
    """Test that nonexistent parser returns empty list."""
    options = get_cli_options("NonExistentParser")
    assert options == []


def test_os_parser_options():
    """Test that OsXdmParser has skip-os-task option."""
    options = get_cli_options("OsXdmParser")
    option_names = [opt.get("name") for opt in options]
    assert "--skip-os-task" in option_names