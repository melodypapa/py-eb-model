"""
Dem Model Tests - Tests for Dem module model classes.
"""
import pytest
from ....models.diag_stack.dem_xdm import Dem, DemGeneral
from ....models.core.eb_doc import EBModel
from ....models.core.abstract import EcucParamConfContainerDef


class TestDem:

    def test_module_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dem")
        dem = Dem(container)

        assert dem.getName() == "Dem"
        assert dem.getParent() == container

    def test_module_properties(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dem")
        dem = Dem(container)

        # Verify inherited Module properties
        assert isinstance(dem.getArVersion(), type(root.getOs().getArVersion()))
        assert isinstance(dem.getSwVersion(), type(root.getOs().getSwVersion()))
        assert dem.getTotalElement() == 0

    def test_get_set_general(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dem")
        dem = Dem(container)

        general = DemGeneral(dem, "DemGeneral")
        general.setDemDevErrorDetect(True)
        dem.setDemGeneral(general)

        assert dem.getDemGeneral() is not None
        assert dem.getDemGeneral().getDemDevErrorDetect() is True


class TestDemGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dem")
        dem = Dem(container)

        general = DemGeneral(dem, "DemGeneral")

        assert general.getName() == "DemGeneral"
        assert general.getParent() == dem

    def test_get_set_dev_error_detect(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dem")
        dem = Dem(container)

        general = DemGeneral(dem, "DemGeneral")
        general.setDemDevErrorDetect(True)

        assert general.getDemDevErrorDetect() is True

    def test_get_set_dem_enabled(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dem")
        dem = Dem(container)

        general = DemGeneral(dem, "DemGeneral")
        general.setDemEnabled(True)

        assert general.getDemEnabled() is True

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        container = EcucParamConfContainerDef(root, "Dem")
        dem = Dem(container)

        general = DemGeneral(dem, "DemGeneral")
        result = general.setDemDevErrorDetect(False)

        assert result is general
        assert general.getDemDevErrorDetect() is False

        # Test chain setter returns self
        result = general.setDemEnabled(True)

        assert result is general
        assert general.getDemEnabled() is True