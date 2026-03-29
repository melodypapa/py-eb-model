"""
NvM Model Tests - Tests for NVM module model classes.
"""
import pytest
from ...models.nvm_xdm import NvM, NvMCommon, NvMBlockDescriptor
from ...models.eb_doc import EBModel


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


class TestCommonPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        # Will be implemented in Task 6
        pass