"""
LdCom Model Tests - Tests for LdCom module model classes.
"""
import pytest
from ....models.com_stack.ldcom_xdm import LdCom
from ....models.core.eb_doc import EBModel


class TestLdCom:

    def test_initialization(self):
        root = EBModel.getInstance()
        ldcom = LdCom(root)

        assert ldcom.getName() == "LdCom"
        assert ldcom.getParent() == root

    def test_module_properties(self):
        root = EBModel.getInstance()
        ldcom = LdCom(root)

        # Verify inherited Module properties
        assert isinstance(ldcom.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(ldcom.getSwVersion(), type(root.getOs().getSwVersion()))
        assert ldcom.getTotalElement() == 0
