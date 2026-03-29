"""
J1939Nm Model Tests - Tests for J1939Nm module model classes.
"""
import pytest
from ...models.j1939nm_xdm import J1939Nm, J1939NmGeneral
from ...models.eb_doc import EBModel
from ...models.abstract import EcucParamConfContainerDef


class TestJ1939Nm:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Nm")
        j1939nm = J1939Nm(container)

        assert j1939nm.getName() == "J1939Nm"
        assert j1939nm.getParent() == container

    def test_module_properties(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Nm")
        j1939nm = J1939Nm(container)

        # Verify inherited Module properties
        assert isinstance(j1939nm.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(j1939nm.getSwVersion(), type(root.getOs().getSwVersion()))
        assert j1939nm.getTotalElement() == 0

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Nm")
        j1939nm = J1939Nm(container)

        general = J1939NmGeneral(j1939nm, "J1939NmGeneral")
        general.setJ1939NmDevErrorDetect(True)
        j1939nm.setJ1939NmGeneral(general)

        assert j1939nm.getJ1939NmGeneral() is not None
        assert j1939nm.getJ1939NmGeneral().getJ1939NmDevErrorDetect() is True


class TestJ1939NmGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Nm")
        j1939nm = J1939Nm(container)

        general = J1939NmGeneral(j1939nm, "J1939NmGeneral")

        assert general.getName() == "J1939NmGeneral"
        assert general.getParent() == j1939nm

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Nm")
        j1939nm = J1939Nm(container)

        general = J1939NmGeneral(j1939nm, "J1939NmGeneral")
        general.setJ1939NmDevErrorDetect(True)

        assert general.getJ1939NmDevErrorDetect() is True

    def test_get_set_j1939nm_enabled(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Nm")
        j1939nm = J1939Nm(container)

        general = J1939NmGeneral(j1939nm, "J1939NmGeneral")
        general.setJ1939NmEnabled(True)

        assert general.getJ1939NmEnabled() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Nm")
        j1939nm = J1939Nm(container)

        general = J1939NmGeneral(j1939nm, "J1939NmGeneral")
        result = general.setJ1939NmDevErrorDetect(False)

        assert result is general
        assert general.getJ1939NmDevErrorDetect() is False

        # Test chain setter returns self
        result = general.setJ1939NmEnabled(True)

        assert result is general
        assert general.getJ1939NmEnabled() is True