import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(src_path))

from eb_model.core import __all__


def test_core_package_exists():
    """Test that core package can be imported."""
    assert __all__ == []