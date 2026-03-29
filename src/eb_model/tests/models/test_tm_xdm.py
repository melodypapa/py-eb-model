"""
Tm Model Tests - Tests for TM module model classes.
"""
import pytest
from ...models.tm_xdm import TmGeneral
from ...models.eb_doc import EBModel


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


class TestCommonPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        # Will be implemented in Task 2
        pass


class TestPublishedInformation:

    def test_initialization(self):
        root = EBModel.getInstance()
        # Will be implemented in Task 2
        pass
