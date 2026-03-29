"""
Dcm Model Tests - Tests for Dcm module model classes.
"""
import pytest
from ....models.diag_stack.dcm_xdm import Dcm, DcmGeneral
from ....models.core.eb_doc import EBModel
from ....models.core.abstract import EcucParamConfContainerDef


class TestDcm:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dcm")
        dcm = Dcm(container)

        assert dcm.getName() == "Dcm"
        assert dcm.getParent() == container

    def test_module_properties(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dcm")
        dcm = Dcm(container)

        # Verify inherited Module properties
        assert isinstance(dcm.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(dcm.getSwVersion(), type(root.getOs().getSwVersion()))
        assert dcm.getTotalElement() == 0

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dcm")
        dcm = Dcm(container)

        general = DcmGeneral(dcm, "DcmGeneral")
        general.setDcmDevErrorDetect(True)
        dcm.setDcmGeneral(general)

        assert dcm.getDcmGeneral() is not None
        assert dcm.getDcmGeneral().getDcmDevErrorDetect() is True


class TestDcmGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dcm")
        dcm = Dcm(container)

        general = DcmGeneral(dcm, "DcmGeneral")

        assert general.getName() == "DcmGeneral"
        assert general.getParent() == dcm

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dcm")
        dcm = Dcm(container)

        general = DcmGeneral(dcm, "DcmGeneral")
        general.setDcmDevErrorDetect(True)

        assert general.getDcmDevErrorDetect() is True

    def test_get_set_dcm_enabled(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dcm")
        dcm = Dcm(container)

        general = DcmGeneral(dcm, "DcmGeneral")
        general.setDcmEnabled(True)

        assert general.getDcmEnabled() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dcm")
        dcm = Dcm(container)

        general = DcmGeneral(dcm, "DcmGeneral")
        result = general.setDcmDevErrorDetect(False)

        assert result is general
        assert general.getDcmDevErrorDetect() is False

        # Test chain setter returns self
        result = general.setDcmEnabled(True)

        assert result is general
        assert general.getDcmEnabled() is True