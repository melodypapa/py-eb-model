"""
J1939Tp Model Tests - Tests for J1939Tp module model classes.
"""
import pytest
from eb_model.models.j1939_stack.j1939tp_xdm import J1939Tp, J1939TpGeneral
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.core.abstract import EcucParamConfContainerDef


class TestJ1939Tp:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Tp")
        j1939tp = J1939Tp(container)

        assert j1939tp.getName() == "J1939Tp"
        assert j1939tp.getParent() == container

    def test_module_properties(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Tp")
        j1939tp = J1939Tp(container)

        # Verify inherited Module properties
        assert isinstance(j1939tp.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(j1939tp.getSwVersion(), type(root.getOs().getSwVersion()))
        assert j1939tp.getTotalElement() == 0

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Tp")
        j1939tp = J1939Tp(container)

        general = J1939TpGeneral(j1939tp, "J1939TpGeneral")
        general.setJ1939TpDevErrorDetect(True)
        j1939tp.setJ1939TpGeneral(general)

        assert j1939tp.getJ1939TpGeneral() is not None
        assert j1939tp.getJ1939TpGeneral().getJ1939TpDevErrorDetect() is True


class TestJ1939TpGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Tp")
        j1939tp = J1939Tp(container)

        general = J1939TpGeneral(j1939tp, "J1939TpGeneral")

        assert general.getName() == "J1939TpGeneral"
        assert general.getParent() == j1939tp

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Tp")
        j1939tp = J1939Tp(container)

        general = J1939TpGeneral(j1939tp, "J1939TpGeneral")
        general.setJ1939TpDevErrorDetect(True)

        assert general.getJ1939TpDevErrorDetect() is True

    def test_get_set_j1939tp_enabled(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Tp")
        j1939tp = J1939Tp(container)

        general = J1939TpGeneral(j1939tp, "J1939TpGeneral")
        general.setJ1939TpEnabled(True)

        assert general.getJ1939TpEnabled() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "J1939Tp")
        j1939tp = J1939Tp(container)

        general = J1939TpGeneral(j1939tp, "J1939TpGeneral")
        result = general.setJ1939TpDevErrorDetect(False)

        assert result is general
        assert general.getJ1939TpDevErrorDetect() is False

        # Test chain setter returns self
        result = general.setJ1939TpEnabled(True)

        assert result is general
        assert general.getJ1939TpEnabled() is True
