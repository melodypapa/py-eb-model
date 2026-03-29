"""
EcuM Model Tests - Tests for ECUM module model classes.
"""
import pytest
from ...models.ecum_xdm import EcuM, EcuMGeneral, EcuMStartup
from ...models.eb_doc import EBModel


class TestEcuMGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        general = EcuMGeneral(root, "EcuMGeneral")

        assert general.getName() == "EcuMGeneral"
        assert general.getParent() == root
        assert general.getEcumDevErrorDetect() is None
        assert general.getEcumConfigurationVariant() is None

    def test_set_ecum_dev_error_detect(self):
        root = EBModel.getInstance()
        general = EcuMGeneral(root, "EcuMGeneral")

        assert general.setEcumDevErrorDetect(True) == general
        assert general.getEcumDevErrorDetect() is True

        assert general.setEcumDevErrorDetect(False) == general
        assert general.getEcumDevErrorDetect() is False

    def test_set_ecum_configuration_variant(self):
        root = EBModel.getInstance()
        general = EcuMGeneral(root, "EcuMGeneral")

        assert general.setEcumConfigurationVariant("PBcfg") == general
        assert general.getEcumConfigurationVariant() == "PBcfg"

        assert general.setEcumConfigurationVariant("PBVar") == general
        assert general.getEcumConfigurationVariant() == "PBVar"


class TestEcuMStartup:

    def test_initialization(self):
        root = EBModel.getInstance()
        startup = EcuMStartup(root, "EcuMStartup")

        assert startup.getName() == "EcuMStartup"
        assert startup.getParent() == root
        assert startup.getEcumEnableUserMcuStartup() is None
        assert startup.getEcumUserMcuStartupRef() is None


class TestEcuM:

    def test_initialization(self):
        root = EBModel.getInstance()
        ecum = EcuM(root)

        assert ecum.getName() == "EcuM"
        assert ecum.getParent() == root
        assert ecum.getEcumGeneral() is None
        assert ecum.getEcumStartup() is None
        assert ecum.getEcumShutdown() is None

    def test_set_ecum_general(self):
        root = EBModel.getInstance()
        ecum = EcuM(root)
        general = EcuMGeneral(root, "EcuMGeneral")

        assert ecum.setEcumGeneral(general) == ecum
        assert ecum.getEcumGeneral() == general

    def test_set_ecum_startup(self):
        root = EBModel.getInstance()
        ecum = EcuM(root)
        startup = EcuMStartup(root, "EcuMStartup")

        assert ecum.setEcumStartup(startup) == ecum
        assert ecum.getEcumStartup() == startup
