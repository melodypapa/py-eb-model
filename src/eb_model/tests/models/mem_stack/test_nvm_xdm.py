"""
NvM Model Tests - Tests for NVM module model classes.
"""
import pytest
from ....models.mem_stack.nvm_xdm import NvM, NvMCommon, NvMBlockDescriptor, CommonPublishedInformation, PublishedInformation, NvMDefensiveProgramming
from ....models.core.eb_doc import EBModel


class TestNvMCommon:

    def test_initialization(self):
        root = EBModel.getInstance()
        common = NvMCommon(root, "NvMCommon")

        assert common.getName() == "NvMCommon"
        assert common.getParent() == root
        assert common.getNvMApiConfigClass() is None
        assert common.getNvMDevErrorDetect() is None
        assert common.getNvMVersionInfoApi() is None
        assert common.getNvMBufferAlignmentValue() is None
        assert common.getNvMMemAccUsage() is None

    def test_set_nvm_api_config_class(self):
        root = EBModel.getInstance()
        common = NvMCommon(root, "NvMCommon")

        assert common.setNvMApiConfigClass("NVM_CCP") == common
        assert common.getNvMApiConfigClass() == "NVM_CCP"

    def test_set_nvm_dev_error_detect(self):
        root = EBModel.getInstance()
        common = NvMCommon(root, "NvMCommon")

        assert common.setNvMDevErrorDetect(True) == common
        assert common.getNvMDevErrorDetect() is True

    def test_set_nvm_mem_acc_usage(self):
        root = EBModel.getInstance()
        common = NvMCommon(root, "NvMCommon")

        assert common.setNvMMemAccUsage(True) == common
        assert common.getNvMMemAccUsage() is True


class TestCommonPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        pub_info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert pub_info.getName() == "CommonPublishedInformation"
        assert pub_info.getParent() == root
        assert pub_info.getArMajorVersion() is None
        assert pub_info.getArMinorVersion() is None
        assert pub_info.getArPatchVersion() is None
        assert pub_info.getSwMajorVersion() is None
        assert pub_info.getSwMinorVersion() is None
        assert pub_info.getSwPatchVersion() is None

    def test_set_ar_major_version(self):
        root = EBModel.getInstance()
        pub_info = CommonPublishedInformation(root, "CommonPublishedInformation")

        assert pub_info.setArMajorVersion(4) == pub_info
        assert pub_info.getArMajorVersion() == 4


class TestPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        pub_info = PublishedInformation(root, "PublishedInformation")

        assert pub_info.getName() == "PublishedInformation"
        assert pub_info.getParent() == root
        assert pub_info.getVendorId() is None
        assert pub_info.getArReleaseMajorVersion() is None

    def test_set_vendor_id(self):
        root = EBModel.getInstance()
        pub_info = PublishedInformation(root, "PublishedInformation")

        assert pub_info.setVendorId("Vector") == pub_info
        assert pub_info.getVendorId() == "Vector"


class TestNvMDefensiveProgramming:

    def test_initialization(self):
        root = EBModel.getInstance()
        defensive = NvMDefensiveProgramming(root, "NvMDefensiveProgramming")

        assert defensive.getName() == "NvMDefensiveProgramming"
        assert defensive.getParent() == root
        assert defensive.getNvMNullPointerCheck() is None
        assert defensive.getNvMParameterCheck() is None

    def test_set_nvm_null_pointer_check(self):
        root = EBModel.getInstance()
        defensive = NvMDefensiveProgramming(root, "NvMDefensiveProgramming")

        assert defensive.setNvMNullPointerCheck(True) == defensive
        assert defensive.getNvMNullPointerCheck() is True

    def test_set_nvm_parameter_check(self):
        root = EBModel.getInstance()
        defensive = NvMDefensiveProgramming(root, "NvMDefensiveProgramming")

        assert defensive.setNvMParameterCheck(True) == defensive
        assert defensive.getNvMParameterCheck() is True
