"""Integration tests for CLI installation and entry points."""
import pytest


def test_cli_entry_point_exists():
    """Test that the CLI entry point can be imported and run."""
    from eb_model.cli.eb_convert import create_argument_parser

    parser = create_argument_parser()
    assert parser.prog == "eb-convert"


def test_cli_help():
    """Test that CLI help can be displayed."""
    from eb_model.cli.eb_convert import create_argument_parser

    parser = create_argument_parser()
    help_text = parser.format_help()
    assert "eb-convert" in help_text
    assert "XDM" in help_text