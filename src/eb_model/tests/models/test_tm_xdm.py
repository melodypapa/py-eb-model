"""
Tm Model Tests - Tests for TM module model classes.
"""
import pytest
from ...models.core.tm_xdm import Tm, TmGeneral, CommonPublishedInformation, PublishedInformation
from ...models.core.eb_doc import EBModel


class TestTmGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        general = TmGeneral(root, "TmGeneral")

        assert general.getName() == "TmGeneral"
        assert general.getParent() == root
        assert general.getTmDevErrorDetect() is None
        assert general.getTmMainWindowProtect() is None

    def test_set_tm_dev_error_detect(self):
        root = EBModel.getInstance()
        general = TmGeneral(root, "TmGeneral")

        assert general.setTmDevErrorDetect(True) == general
        assert general.getTmDevErrorDetect() is True

        assert general.setTmDevErrorDetect(False) == general
        assert general.getTmDevErrorDetect() is False

    def test_set_tm_main_window_protect(self):
        root = EBModel.getInstance()
        general = TmGeneral(root, "TmGeneral")

        assert general.setTmMainWindowProtect(True) == general
        assert general.getTmMainWindowProtect() is True

        assert general.setTmMainWindowProtect(False) == general
        assert general.getTmMainWindowProtect() is False

    def test_set_tm_version_info_api(self):
        root = EBModel.getInstance()
        general = TmGeneral(root, "TmGeneral")

        assert general.setTmVersionInfoApi(True) == general
        assert general.getTmVersionInfoApi() is True

        assert general.setTmVersionInfoApi(False) == general
        assert general.getTmVersionInfoApi() is False

    def test_set_tm_enable_predef_timer_1us_16bit(self):
        root = EBModel.getInstance()
        general = TmGeneral(root, "TmGeneral")

        assert general.setTmEnablePredefTimer1us16bit(True) == general
        assert general.getTmEnablePredefTimer1us16bit() is True

        assert general.setTmEnablePredefTimer1us16bit(False) == general
        assert general.getTmEnablePredefTimer1us16bit() is False

    def test_set_tm_enable_predef_timer_1us_24bit(self):
        root = EBModel.getInstance()
        general = TmGeneral(root, "TmGeneral")

        assert general.setTmEnablePredefTimer1us24bit(True) == general
        assert general.getTmEnablePredefTimer1us24bit() is True

        assert general.setTmEnablePredefTimer1us24bit(False) == general
        assert general.getTmEnablePredefTimer1us24bit() is False

    def test_set_tm_enable_predef_timer_1us_32bit(self):
        root = EBModel.getInstance()
        general = TmGeneral(root, "TmGeneral")

        assert general.setTmEnablePredefTimer1us32bit(True) == general
        assert general.getTmEnablePredefTimer1us32bit() is True

        assert general.setTmEnablePredefTimer1us32bit(False) == general
        assert general.getTmEnablePredefTimer1us32bit() is False

    def test_set_tm_enable_predef_timer_100us_32bit(self):
        root = EBModel.getInstance()
        general = TmGeneral(root, "TmGeneral")

        assert general.setTmEnablePredefTimer100us32bit(True) == general
        assert general.getTmEnablePredefTimer100us32bit() is True

        assert general.setTmEnablePredefTimer100us32bit(False) == general
        assert general.getTmEnablePredefTimer100us32bit() is False


class TestCommonPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert info.getName() == "CommonPublishedInformation"
        assert info.getParent() == root
        assert info.getArMajorVersion() is None
        assert info.getArMinorVersion() is None
        assert info.getArPatchVersion() is None
        assert info.getSwMajorVersion() is None
        assert info.getSwMinorVersion() is None
        assert info.getSwPatchVersion() is None

    def test_ar_major_version(self):
        root = EBModel.getInstance()
        info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert info.setArMajorVersion(4) == info
        assert info.getArMajorVersion() == 4

        assert info.setArMajorVersion(5) == info
        assert info.getArMajorVersion() == 5

    def test_ar_minor_version(self):
        root = EBModel.getInstance()
        info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert info.setArMinorVersion(3) == info
        assert info.getArMinorVersion() == 3

        assert info.setArMinorVersion(4) == info
        assert info.getArMinorVersion() == 4

    def test_ar_patch_version(self):
        root = EBModel.getInstance()
        info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert info.setArPatchVersion(1) == info
        assert info.getArPatchVersion() == 1

        assert info.setArPatchVersion(2) == info
        assert info.getArPatchVersion() == 2

    def test_sw_major_version(self):
        root = EBModel.getInstance()
        info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert info.setSwMajorVersion(1) == info
        assert info.getSwMajorVersion() == 1

        assert info.setSwMajorVersion(2) == info
        assert info.getSwMajorVersion() == 2

    def test_sw_minor_version(self):
        root = EBModel.getInstance()
        info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert info.setSwMinorVersion(0) == info
        assert info.getSwMinorVersion() == 0

        assert info.setSwMinorVersion(1) == info
        assert info.getSwMinorVersion() == 1

    def test_sw_patch_version(self):
        root = EBModel.getInstance()
        info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert info.setSwPatchVersion(0) == info
        assert info.getSwPatchVersion() == 0

        assert info.setSwPatchVersion(1) == info
        assert info.getSwPatchVersion() == 1


class TestPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        info = PublishedInformation(root, "PublishedInformation")

        assert info.getName() == "PublishedInformation"
        assert info.getParent() == root
        assert info.getVendorId() is None
        assert info.getArReleaseMajorVersion() is None
        assert info.getArReleaseMinorVersion() is None
        assert info.getArReleasePatchVersion() is None
        assert info.getSwMajorVersion() is None
        assert info.getSwMinorVersion() is None
        assert info.getSwPatchVersion() is None

    def test_vendor_id(self):
        root = EBModel.getInstance()
        info = PublishedInformation(root, "PublishedInformation")

        assert info.setVendorId("EB") == info
        assert info.getVendorId() == "EB"

        assert info.setVendorId("Vector") == info
        assert info.getVendorId() == "Vector"

    def test_ar_release_major_version(self):
        root = EBModel.getInstance()
        info = PublishedInformation(root, "PublishedInformation")

        assert info.setArReleaseMajorVersion("4") == info
        assert info.getArReleaseMajorVersion() == "4"

        assert info.setArReleaseMajorVersion("5") == info
        assert info.getArReleaseMajorVersion() == "5"

    def test_ar_release_minor_version(self):
        root = EBModel.getInstance()
        info = PublishedInformation(root, "PublishedInformation")

        assert info.setArReleaseMinorVersion("3") == info
        assert info.getArReleaseMinorVersion() == "3"

        assert info.setArReleaseMinorVersion("4") == info
        assert info.getArReleaseMinorVersion() == "4"

    def test_ar_release_patch_version(self):
        root = EBModel.getInstance()
        info = PublishedInformation(root, "PublishedInformation")

        assert info.setArReleasePatchVersion("1") == info
        assert info.getArReleasePatchVersion() == "1"

        assert info.setArReleasePatchVersion("2") == info
        assert info.getArReleasePatchVersion() == "2"

    def test_sw_major_version(self):
        root = EBModel.getInstance()
        info = PublishedInformation(root, "PublishedInformation")

        assert info.setSwMajorVersion("1") == info
        assert info.getSwMajorVersion() == "1"

        assert info.setSwMajorVersion("2") == info
        assert info.getSwMajorVersion() == "2"

    def test_sw_minor_version(self):
        root = EBModel.getInstance()
        info = PublishedInformation(root, "PublishedInformation")

        assert info.setSwMinorVersion("0") == info
        assert info.getSwMinorVersion() == "0"

        assert info.setSwMinorVersion("1") == info
        assert info.getSwMinorVersion() == "1"

    def test_sw_patch_version(self):
        root = EBModel.getInstance()
        info = PublishedInformation(root, "PublishedInformation")

        assert info.setSwPatchVersion("0") == info
        assert info.getSwPatchVersion() == "0"

        assert info.setSwPatchVersion("1") == info
        assert info.getSwPatchVersion() == "1"
