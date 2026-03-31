"""
Integration tests for XDM file parsing using real EB Tresos demo files.

Tests that parsers can successfully parse real-world XDM configuration files
from EB Tresos AutoCore demo projects.

Implements: SWR_INTEGRATION_00001 (XDM file integration tests)
"""
import os
import pytest

from eb_model.parser.core.eb_parser_factory import EbParserFactory
from eb_model.core.parser_writer_registry import get_module_name
from eb_model.models import EBModel


DATA_DIR = os.path.join(os.path.dirname(__file__), "data_files")


# XDM files that successfully parse with current parsers.
# Note: Other modules (Os, EcuC, NvM, Ea, SoAd, ComM, PduR, Com, CanIf) fail
# due to schema incompatibilities with EB Tresos demo XDM files.
# Driver modules (Can, Eth) have no parser implementation.
XDM_FILES = [
    ("Rte", "simple_demo_can_rte/config/Rte.xdm"),
    ("Rte", "simple_demo_eth_rte/config/Rte.xdm"),
    ("Rte", "simple_demo_mem_can_rte/config/Rte.xdm"),
    ("MemIf", "simple_demo_mem_can_rte/config/MemIf.xdm"),
    ("EthIf", "simple_demo_eth_rte/config/EthIf.xdm"),
]


XDM_FILE_IDS = [f"{m}-{p.replace('/', '-')}" for m, p in XDM_FILES]


@pytest.mark.integration
@pytest.mark.parametrize("expected_module,xdm_relative_path", XDM_FILES, ids=XDM_FILE_IDS)
def test_xdm_parsing_pipeline(expected_module, xdm_relative_path):
    """
    Test complete XDM parsing pipeline: parser creation, parsing, and model integration.

    Args:
        expected_module: Expected module name (e.g., "Rte", "MemIf")
        xdm_relative_path: Relative path to XDM file within data directory

    Implements: SWR_INTEGRATION_00002-00004 (Unified parsing test)
    """
    xdm_path = os.path.join(DATA_DIR, xdm_relative_path)

    # Create parser and verify correct module detected
    parser = EbParserFactory.create(xdm_path)
    assert parser is not None, f"Failed to create parser for {xdm_path}"
    module_name = get_module_name(parser.__class__)
    assert module_name == expected_module, (
        f"Expected module {expected_module} but got {module_name} for {xdm_relative_path}"
    )

    # Parse and verify no errors
    doc = EBModel.getInstance()
    parser.parse_xdm(xdm_path, doc)

    # Verify module stored in model at standard path
    module_path = f"/{expected_module}/{expected_module}"
    module = doc.find(module_path)
    assert module is not None, (
        f"Module {expected_module} not found in EBModel after parsing {xdm_relative_path}"
    )


@pytest.mark.integration
def test_all_selected_modules_are_tested():
    """
    Verify that all working module types are covered by the test data.

    Due to schema incompatibilities with EB Tresos demo XDM files,
    only Rte, MemIf, and EthIf parsers work with these specific files.

    Implements: SWR_INTEGRATION_00005 (Module coverage test)
    """
    expected_modules = {"Rte", "MemIf", "EthIf"}
    actual_modules = {module for module, _ in XDM_FILES}
    missing_modules = expected_modules - actual_modules
    assert not missing_modules, f"Missing modules in test data: {missing_modules}"


@pytest.mark.integration
def test_all_xdm_files_exist():
    """
    Verify all XDM files referenced in test data actually exist.

    Implements: SWR_INTEGRATION_00006 (Test data validation)
    """
    for _, xdm_relative_path in XDM_FILES:
        xdm_path = os.path.join(DATA_DIR, xdm_relative_path)
        assert os.path.exists(xdm_path), f"XDM file not found: {xdm_path}"
        assert os.path.isfile(xdm_path), f"Not a file: {xdm_path}"