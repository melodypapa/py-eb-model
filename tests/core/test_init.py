"""
Tests for core package initialization.
"""
import pytest
from eb_model.core import __all__


def test_core_package_exports():
    """Test that core package exports the expected symbols."""
    # Verify expected exports exist
    assert 'CLI_OPTIONS' in __all__
    assert 'get_cli_options' in __all__
    assert 'get_all_cli_options' in __all__
    assert 'get_writer' in __all__
    assert 'get_writer_for_module' in __all__
    assert 'get_module_name' in __all__
    assert 'register_writer' in __all__
    # Should have exactly 7 exports
    assert len(__all__) == 7