"""
J1939Dcm Model Tests - Tests for J1939Dcm module model classes.
"""
import pytest
from eb_model.models.j1939_stack.j1939dcm_xdm import J1939Dcm, J1939DcmGeneral
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.core.abstract import EcucParamConfContainerDef


class TestJ1939Dcm:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Dcm")
        j1939dcm = J1939Dcm(container)

        assert j1939dcm.getName() == "J1939Dcm"
        assert j1939dcm.getParent() == container

    def test_module_properties(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Dcm")
        j1939dcm = J1939Dcm(container)

        # Verify inherited Module properties
        assert isinstance(j1939dcm.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(j1939dcm.getSwVersion(), type(root.getOs().getSwVersion()))
        assert j1939dcm.getTotalElement() == 0

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Dcm")
        j1939dcm = J1939Dcm(container)

        general = J1939DcmGeneral(j1939dcm, "J1939DcmGeneral")
        general.setJ1939DcmDevErrorDetect(True)
        j1939dcm.setJ1939DcmGeneral(general)

        assert j1939dcm.getJ1939DcmGeneral() is not None
        assert j1939dcm.getJ1939DcmGeneral().getJ1939DcmDevErrorDetect() is True


class TestJ1939DcmGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Dcm")
        j1939dcm = J1939Dcm(container)

        general = J1939DcmGeneral(j1939dcm, "J1939DcmGeneral")

        assert general.getName() == "J1939DcmGeneral"
        assert general.getParent() == j1939dcm

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Dcm")
        j1939dcm = J1939Dcm(container)

        general = J1939DcmGeneral(j1939dcm, "J1939DcmGeneral")
        general.setJ1939DcmDevErrorDetect(True)

        assert general.getJ1939DcmDevErrorDetect() is True

    def test_get_set_j1939dcm_enabled(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Dcm")
        j1939dcm = J1939Dcm(container)

        general = J1939DcmGeneral(j1939dcm, "J1939DcmGeneral")
        general.setJ1939DcmEnabled(True)

        assert general.getJ1939DcmEnabled() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Dcm")
        j1939dcm = J1939Dcm(container)

        general = J1939DcmGeneral(j1939dcm, "J1939DcmGeneral")
        result = general.setJ1939DcmDevErrorDetect(False)

        assert result is general
        assert general.getJ1939DcmDevErrorDetect() is False

        # Test chain setter returns self
        result = general.setJ1939DcmEnabled(True)

        assert result is general
        assert general.getJ1939DcmEnabled() is True