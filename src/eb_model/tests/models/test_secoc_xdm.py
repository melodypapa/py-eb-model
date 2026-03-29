"""
SecOC Model Tests - Tests for SecOC module model classes.
"""
import pytest
from ...models.secoc_xdm import SecOC, SecOCGeneral
from ...models.eb_doc import EBModel
from ...models.abstract import EcucParamConfContainerDef


class TestSecOC:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "SecOC")
        secoc = SecOC(container)

        assert secoc.getName() == "SecOC"
        assert secoc.getParent() == container

    def test_module_properties(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "SecOC")
        secoc = SecOC(container)

        # Verify inherited Module properties
        assert isinstance(secoc.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(secoc.getSwVersion(), type(root.getOs().getSwVersion()))
        assert secoc.getTotalElement() == 0

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "SecOC")
        secoc = SecOC(container)

        general = SecOCGeneral(secoc, "SecOCGeneral")
        general.setSecocDevErrorDetect(True)
        secoc.setSecocGeneral(general)

        assert secoc.getSecocGeneral() is not None
        assert secoc.getSecocGeneral().getSecocDevErrorDetect() is True


class TestSecOCGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "SecOC")
        secoc = SecOC(container)

        general = SecOCGeneral(secoc, "SecOCGeneral")

        assert general.getName() == "SecOCGeneral"
        assert general.getParent() == secoc

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "SecOC")
        secoc = SecOC(container)

        general = SecOCGeneral(secoc, "SecOCGeneral")
        general.setSecocDevErrorDetect(True)

        assert general.getSecocDevErrorDetect() is True

    def test_get_set_secoc_enabled(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "SecOC")
        secoc = SecOC(container)

        general = SecOCGeneral(secoc, "SecOCGeneral")
        general.setSecocEnabled(True)

        assert general.getSecocEnabled() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "SecOC")
        secoc = SecOC(container)

        general = SecOCGeneral(secoc, "SecOCGeneral")
        result = general.setSecocDevErrorDetect(False)

        assert result is general
        assert general.getSecocDevErrorDetect() is False

        # Test chain setter returns self
        result = general.setSecocEnabled(True)

        assert result is general
        assert general.getSecocEnabled() is True