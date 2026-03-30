import pytest
from eb_model.core import __all__


def test_core_package_exists():
    """Test that core package can be imported and has empty exports."""
    assert __all__ == []