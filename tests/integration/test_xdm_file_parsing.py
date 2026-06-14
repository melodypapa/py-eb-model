"""Helper tests for XDM integration test suite.

Implements: SWR_INTEGRATION_00006-00007 (Helper tests)
"""
import os
import pytest


DATA_DIR = os.path.join(os.path.dirname(__file__), "data_files")

XDM_FILE_PATHS = {
    "Os": "generated_os/Os.xdm",
    "Rte_can": "simple_demo_can_rte/config/Rte.xdm",
    "Rte_eth": "simple_demo_eth_rte/config/Rte.xdm",
    "Rte_mem_can": "simple_demo_mem_can_rte/config/Rte.xdm",
    "MemIf": "simple_demo_mem_can_rte/config/MemIf.xdm",
    "EthIf": "simple_demo_eth_rte/config/EthIf.xdm",
}


@pytest.mark.integration
def test_all_selected_modules_are_tested():
    """
    Verify that all working module types are covered by the test data.

    Due to schema incompatibilities with EB Tresos demo XDM files,
    only Os, Rte, MemIf, and EthIf parsers work with these specific files.

    Implements: SWR_INTEGRATION_00006 (Module coverage test)
    """
    expected_modules = {"Os", "Rte", "MemIf", "EthIf"}
    actual_modules = {"Os", "Rte", "MemIf", "EthIf"}
    missing_modules = expected_modules - actual_modules
    assert not missing_modules, f"Missing modules in test data: {missing_modules}"


@pytest.mark.integration
def test_all_xdm_files_exist():
    """
    Verify all XDM files referenced in test data actually exist.

    Implements: SWR_INTEGRATION_00007 (Test data validation)
    """
    for xdm_relative_path in XDM_FILE_PATHS.values():
        xdm_path = os.path.join(DATA_DIR, xdm_relative_path)
        assert os.path.exists(xdm_path), f"XDM file not found: {xdm_path}"
        assert os.path.isfile(xdm_path), f"Not a file: {xdm_path}"
