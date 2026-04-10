"""
Tests for CLI Options Registry.
"""
import pytest
from eb_model.core.cli_options_registry import CLI_OPTIONS, get_cli_options, get_all_cli_options


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


def test_rte_parser_options():
    """Test that RteXdmParser has runnable option."""
    options = get_cli_options("RteXdmParser")
    option_names = [opt.get("name") for opt in options]
    assert "--runnable" in option_names


def test_get_all_cli_options():
    """Test getting all registered CLI options."""
    all_options = get_all_cli_options()
    assert isinstance(all_options, dict)
    assert "OsXdmParser" in all_options
    assert "RteXdmParser" in all_options


def test_option_structure():
    """Test that option has all required keys."""
    options = get_cli_options("OsXdmParser")
    option = options[0]
    assert "name" in option
    assert "help" in option
    assert "action" in option
    assert "default" in option


def test_returns_copy():
    """Test that returned dict is a copy, not reference."""
    from eb_model.core.cli_options_registry import CLI_OPTIONS as original_cli_options
    options1 = get_all_cli_options()
    options1["NewParser"] = []
    options2 = get_all_cli_options()
    assert "NewParser" not in options2
    assert "NewParser" not in original_cli_options
