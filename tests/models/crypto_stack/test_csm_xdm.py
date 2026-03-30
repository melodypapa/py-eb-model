"""
Csm Model Tests - Tests for Csm module model classes.
"""
import pytest
from eb_model.models.crypto_stack.csm_xdm import Csm, CsmGeneral
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.core.abstract import EcucParamConfContainerDef


class TestCsm:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Csm")
        csm = Csm(container)

        assert csm.getName() == "Csm"
        assert csm.getParent() == container

    def test_module_properties(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Csm")
        csm = Csm(container)

        # Verify inherited Module properties
        assert isinstance(csm.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(csm.getSwVersion(), type(root.getOs().getSwVersion()))
        assert csm.getTotalElement() == 0

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Csm")
        csm = Csm(container)

        general = CsmGeneral(csm, "CsmGeneral")
        general.setCsmDevErrorDetect(True)
        csm.setCsmGeneral(general)

        assert csm.getCsmGeneral() is not None
        assert csm.getCsmGeneral().getCsmDevErrorDetect() is True


class TestCsmGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Csm")
        csm = Csm(container)

        general = CsmGeneral(csm, "CsmGeneral")

        assert general.getName() == "CsmGeneral"
        assert general.getParent() == csm

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Csm")
        csm = Csm(container)

        general = CsmGeneral(csm, "CsmGeneral")
        general.setCsmDevErrorDetect(True)

        assert general.getCsmDevErrorDetect() is True

    def test_get_set_csm_enabled(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Csm")
        csm = Csm(container)

        general = CsmGeneral(csm, "CsmGeneral")
        general.setCsmEnabled(True)

        assert general.getCsmEnabled() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Csm")
        csm = Csm(container)

        general = CsmGeneral(csm, "CsmGeneral")
        result = general.setCsmDevErrorDetect(False)

        assert result is general
        assert general.getCsmDevErrorDetect() is False

        # Test chain setter returns self
        result = general.setCsmEnabled(True)

        assert result is general
        assert general.getCsmEnabled() is True
