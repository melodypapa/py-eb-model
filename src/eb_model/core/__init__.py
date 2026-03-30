"""
Core package for py_eb_model.

Provides central registry and infrastructure for CLI operations.
"""
from .cli_options_registry import CLI_OPTIONS, get_cli_options, get_all_cli_options

__all__ = ['CLI_OPTIONS', 'get_cli_options', 'get_all_cli_options']