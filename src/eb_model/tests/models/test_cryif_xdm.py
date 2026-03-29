"""
CryIf Model Tests - Tests for CryIf module model classes.
"""
import pytest
from ...models.cryif_xdm import CryIf, CryIfGeneral
from ...models.eb_doc import EBModel
from ...models.abstract import EcucParamConfContainerDef


class TestCryIf:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "CryIf")
        cryif = CryIf(container)

        assert cryif.getName() == "CryIf"
        assert cryif.getParent() == container

    def test_module_properties(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "CryIf")
        cryif = CryIf(container)

        # Verify inherited Module properties
        assert isinstance(cryif.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(cryif.getSwVersion(), type(root.getOs().getSwVersion()))
        assert cryif.getTotalElement() == 0

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "CryIf")
        cryif = CryIf(container)

        general = CryIfGeneral(cryif, "CryIfGeneral")
        general.setCryIfDevErrorDetect(True)
        cryif.setCryIfGeneral(general)

        assert cryif.getCryIfGeneral() is not None
        assert cryif.getCryIfGeneral().getCryIfDevErrorDetect() is True


class TestCryIfGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "CryIf")
        cryif = CryIf(container)

        general = CryIfGeneral(cryif, "CryIfGeneral")

        assert general.getName() == "CryIfGeneral"
        assert general.getParent() == cryif

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "CryIf")
        cryif = CryIf(container)

        general = CryIfGeneral(cryif, "CryIfGeneral")
        general.setCryIfDevErrorDetect(True)

        assert general.getCryIfDevErrorDetect() is True

    def test_get_set_cryif_enabled(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "CryIf")
        cryif = CryIf(container)

        general = CryIfGeneral(cryif, "CryIfGeneral")
        general.setCryIfEnabled(True)

        assert general.getCryIfEnabled() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "CryIf")
        cryif = CryIf(container)

        general = CryIfGeneral(cryif, "CryIfGeneral")
        result = general.setCryIfDevErrorDetect(False)

        assert result is general
        assert general.getCryIfDevErrorDetect() is False

        # Test chain setter returns self
        result = general.setCryIfEnabled(True)

        assert result is general
        assert general.getCryIfEnabled() is True