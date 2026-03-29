"""
Dlt Model Tests - Tests for Dlt module model classes.
"""
import pytest
from eb_model.models.diag_stack.dlt_xdm import Dlt, DltGeneral
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.core.abstract import EcucParamConfContainerDef


class TestDlt:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dlt")
        dlt = Dlt(container)

        assert dlt.getName() == "Dlt"
        assert dlt.getParent() == container

    def test_module_properties(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dlt")
        dlt = Dlt(container)

        # Verify inherited Module properties
        assert isinstance(dlt.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(dlt.getSwVersion(), type(root.getOs().getSwVersion()))
        assert dlt.getTotalElement() == 0

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dlt")
        dlt = Dlt(container)

        general = DltGeneral(dlt, "DltGeneral")
        general.setDltDevErrorDetect(True)
        dlt.setDltGeneral(general)

        assert dlt.getDltGeneral() is not None
        assert dlt.getDltGeneral().getDltDevErrorDetect() is True


class TestDltGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dlt")
        dlt = Dlt(container)

        general = DltGeneral(dlt, "DltGeneral")

        assert general.getName() == "DltGeneral"
        assert general.getParent() == dlt

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dlt")
        dlt = Dlt(container)

        general = DltGeneral(dlt, "DltGeneral")
        general.setDltDevErrorDetect(True)

        assert general.getDltDevErrorDetect() is True

    def test_get_set_dlt_enabled(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dlt")
        dlt = Dlt(container)

        general = DltGeneral(dlt, "DltGeneral")
        general.setDltEnabled(True)

        assert general.getDltEnabled() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dlt")
        dlt = Dlt(container)

        general = DltGeneral(dlt, "DltGeneral")
        result = general.setDltDevErrorDetect(False)

        assert result is general
        assert general.getDltDevErrorDetect() is False

        # Test chain setter returns self
        result = general.setDltEnabled(True)

        assert result is general
        assert general.getDltEnabled() is True