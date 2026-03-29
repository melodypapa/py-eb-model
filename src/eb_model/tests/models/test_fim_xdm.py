"""
FiM Model Tests - Tests for FiM module model classes.
"""
import pytest
from ...models.fim_xdm import FiM, FiMGeneral
from ...models.eb_doc import EBModel
from ...models.abstract import EcucParamConfContainerDef


class TestFiM:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "FiM")
        fim = FiM(container)

        assert fim.getName() == "FiM"
        assert fim.getParent() == container

    def test_module_properties(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "FiM")
        fim = FiM(container)

        # Verify inherited Module properties
        assert isinstance(fim.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(fim.getSwVersion(), type(root.getOs().getSwVersion()))
        assert fim.getTotalElement() == 0

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "FiM")
        fim = FiM(container)

        general = FiMGeneral(fim, "FiMGeneral")
        general.setFimDevErrorDetect(True)
        fim.setFimGeneral(general)

        assert fim.getFimGeneral() is not None
        assert fim.getFimGeneral().getFimDevErrorDetect() is True


class TestFiMGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "FiM")
        fim = FiM(container)

        general = FiMGeneral(fim, "FiMGeneral")

        assert general.getName() == "FiMGeneral"
        assert general.getParent() == fim

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "FiM")
        fim = FiM(container)

        general = FiMGeneral(fim, "FiMGeneral")
        general.setFimDevErrorDetect(True)

        assert general.getFimDevErrorDetect() is True

    def test_get_set_fim_enabled(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "FiM")
        fim = FiM(container)

        general = FiMGeneral(fim, "FiMGeneral")
        general.setFimEnabled(True)

        assert general.getFimEnabled() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "FiM")
        fim = FiM(container)

        general = FiMGeneral(fim, "FiMGeneral")
        result = general.setFimDevErrorDetect(False)

        assert result is general
        assert general.getFimDevErrorDetect() is False

        # Test chain setter returns self
        result = general.setFimEnabled(True)

        assert result is general
        assert general.getFimEnabled() is True