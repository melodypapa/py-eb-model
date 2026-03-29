"""
Det Model Tests - Tests for DET module model classes.
"""
import pytest
from ...models.det_xdm import Det, DetGeneral, DetErrorHook
from ...models.eb_doc import EBModel


class TestDetGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.getName() == "DetGeneral"
        assert general.getParent() == root
        assert general.getDetDevErrorDetect() is None
        assert general.getDetEnabled() is None

    def test_set_det_dev_error_detect(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.setDetDevErrorDetect(True) == general
        assert general.getDetDevErrorDetect() is True

        assert general.setDetDevErrorDetect(False) == general
        assert general.getDetDevErrorDetect() is False

    def test_set_det_enabled(self):
        root = EBModel.getInstance()
        general = DetGeneral(root, "DetGeneral")

        assert general.setDetEnabled(True) == general
        assert general.getDetEnabled() is True

        assert general.setDetEnabled(False) == general
        assert general.getDetEnabled() is False


class TestDetErrorHook:

    def test_initialization(self):
        root = EBModel.getInstance()
        error_hook = DetErrorHook(root, "DetErrorHook")

        assert error_hook.getName() == "DetErrorHook"
        assert error_hook.getParent() == root
        assert error_hook.getDetErrorHookCallbackName() is None

    def test_set_det_error_hook_callback_name(self):
        root = EBModel.getInstance()
        error_hook = DetErrorHook(root, "DetErrorHook")

        assert error_hook.setDetErrorHookCallbackName("Det_ErrorHook") == error_hook
        assert error_hook.getDetErrorHookCallbackName() == "Det_ErrorHook"


class TestCommonPublishedInformation:

    def test_initialization(self):
        # Will be implemented in Task 6
        pass


class TestPublishedInformation:

    def test_initialization(self):
        # Will be implemented in Task 6
        pass
