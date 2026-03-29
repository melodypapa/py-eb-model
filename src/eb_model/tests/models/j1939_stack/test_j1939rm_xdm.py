"""
J1939Rm Model Tests - Tests for J1939Rm module model classes.
"""
import pytest
from ....models.j1939_stack.j1939rm_xdm import J1939Rm, J1939RmGeneral
from ....models.core.eb_doc import EBModel
from ....models.core.abstract import EcucParamConfContainerDef


class TestJ1939Rm:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Rm")
        j1939rm = J1939Rm(container)

        assert j1939rm.getName() == "J1939Rm"
        assert j1939rm.getParent() == container

    def test_module_properties(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Rm")
        j1939rm = J1939Rm(container)

        # Verify inherited Module properties
        assert isinstance(j1939rm.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(j1939rm.getSwVersion(), type(root.getOs().getSwVersion()))
        assert j1939rm.getTotalElement() == 0

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Rm")
        j1939rm = J1939Rm(container)

        general = J1939RmGeneral(j1939rm, "J1939RmGeneral")
        general.setJ1939RmDevErrorDetect(True)
        j1939rm.setJ1939RmGeneral(general)

        assert j1939rm.getJ1939RmGeneral() is not None
        assert j1939rm.getJ1939RmGeneral().getJ1939RmDevErrorDetect() is True


class TestJ1939RmGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Rm")
        j1939rm = J1939Rm(container)

        general = J1939RmGeneral(j1939rm, "J1939RmGeneral")

        assert general.getName() == "J1939RmGeneral"
        assert general.getParent() == j1939rm

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Rm")
        j1939rm = J1939Rm(container)

        general = J1939RmGeneral(j1939rm, "J1939RmGeneral")
        general.setJ1939RmDevErrorDetect(True)

        assert general.getJ1939RmDevErrorDetect() is True

    def test_get_set_j1939rm_enabled(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Rm")
        j1939rm = J1939Rm(container)

        general = J1939RmGeneral(j1939rm, "J1939RmGeneral")
        general.setJ1939RmEnabled(True)

        assert general.getJ1939RmEnabled() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Rm")
        j1939rm = J1939Rm(container)

        general = J1939RmGeneral(j1939rm, "J1939RmGeneral")
        result = general.setJ1939RmDevErrorDetect(False)

        assert result is general
        assert general.getJ1939RmDevErrorDetect() is False

        # Test chain setter returns self
        result = general.setJ1939RmEnabled(True)

        assert result is general
        assert general.getJ1939RmEnabled() is True