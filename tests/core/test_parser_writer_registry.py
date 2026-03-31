"""
Tests for parser-writer registry with auto-discovery.
"""
import pytest
from eb_model.core.parser_writer_registry import get_writer, get_writer_for_module, get_module_name
from eb_model.parser.core.os_xdm_parser import OsXdmParser
from eb_model.parser.core.rte_xdm_parser import RteXdmParser
from eb_model.parser.mem_stack.nvm_xdm_parser import NvMXdmParser
from eb_model.parser.core.pbcfgm_xdm_parser import PbcfgMXdmParser


def test_get_writer_auto_discovery():
    """Test that writer is auto-discovered from parser class."""
    writer = get_writer(OsXdmParser)
    assert writer is not None
    assert writer.__name__ == "OsXdmXlsWriter"


def test_get_writer_for_module_name():
    """Test getting writer by module name."""
    writer = get_writer_for_module("Os")
    assert writer is not None
    assert writer.__name__ == "OsXdmXlsWriter"


def test_get_writer_invalid_module():
    """Test that invalid module returns None."""
    writer = get_writer_for_module("NonExistent")
    assert writer is None


def test_get_module_name_from_parser():
    """Test extracting module name from parser class."""
    assert get_module_name(OsXdmParser) == "Os"
    assert get_module_name(RteXdmParser) == "Rte"
    assert get_module_name(NvMXdmParser) == "NvM"
    assert get_module_name(PbcfgMXdmParser) == "PbcfgM"


def test_get_writer_multiple_parsers():
    """Test getting writers for multiple parsers."""
    assert get_writer(OsXdmParser).__name__ == "OsXdmXlsWriter"
    assert get_writer(RteXdmParser).__name__ == "RteXdmXlsWriter"
    assert get_writer(NvMXdmParser).__name__ == "NvMXdmXlsWriter"


def test_get_writer_mem_stack():
    """Test getting writer for memory stack module."""
    # NvMXdmParser is already imported at the top of the file
    writer = get_writer(NvMXdmParser)
    assert writer is not None
    assert writer.__name__ == "NvMXdmXlsWriter"


def test_get_writer_for_module_case_sensitive():
    """Test that module name lookup is case-sensitive."""
    assert get_writer_for_module("Os") is not None
    assert get_writer_for_module("os") is None  # lowercase should not match
    assert get_writer_for_module("OS") is None  # uppercase should not match