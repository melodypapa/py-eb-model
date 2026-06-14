"""Integration test for EthIf.xdm parsing.

Implements: SWR_INTEGRATION_00005 (EthIf parsing)
"""
import os
import pytest

from eb_model.parser.core.eb_parser_factory import EbParserFactory
from eb_model.core.parser_writer_registry import get_module_name
from eb_model.models import EBModel


DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data_files")
XDM_PATH = "simple_demo_eth_rte/config/EthIf.xdm"


@pytest.mark.integration
def test_ethif_simple_eth_xdm_parsing():
    """Test EthIf.xdm parsing from simple_demo_eth_rte."""
    xdm_path = os.path.join(DATA_DIR, XDM_PATH)

    # Create parser and verify correct module detected
    parser = EbParserFactory.create(xdm_path)
    assert parser is not None, f"Failed to create parser for {xdm_path}"
    module_name = get_module_name(parser.__class__)
    assert module_name == "EthIf", f"Expected module EthIf but got {module_name}"

    # Parse and verify no errors
    doc = EBModel.getInstance()
    parser.parse_xdm(xdm_path, doc)

    # Verify module stored in model at standard path
    module = doc.find("/EthIf/EthIf")
    assert module is not None, f"Module EthIf not found in EBModel after parsing {XDM_PATH}"
