"""
Com Model Tests - Tests for COM module model classes.
"""
import pytest
from ...models.com_xdm import Com, ComGeneral
from ...models.eb_doc import EBModel


class TestComGeneral:

    def test_initialization(self):
        root = EBModel.getInstance()
        general = ComGeneral(root, "ComGeneral")

        assert general.getName() == "ComGeneral"
        assert general.getParent() == root
        assert general.getComEnableUserSupport() is None
        assert general.getComUserInitSignal() is None
        assert general.getComUserStatusSupport() is None
        assert general.getComUserTxConfirmation() is None
        assert general.getComUserRxIndication() is None

    def test_set_com_enable_user_support(self):
        root = EBModel.getInstance()
        general = ComGeneral(root, "ComGeneral")

        assert general.setComEnableUserSupport(True) == general
        assert general.getComEnableUserSupport() is True

        assert general.setComEnableUserSupport(False) == general
        assert general.getComEnableUserSupport() is False

    def test_set_com_enable_user_support_none(self):
        root = EBModel.getInstance()
        general = ComGeneral(root, "ComGeneral")

        assert general.getComEnableUserSupport() is None
        general.setComEnableUserSupport(None)
        assert general.getComEnableUserSupport() is None

    def test_set_com_user_init_signal(self):
        root = EBModel.getInstance()
        general = ComGeneral(root, "ComGeneral")

        assert general.setComUserInitSignal(True) == general
        assert general.getComUserInitSignal() is True

        assert general.setComUserInitSignal(False) == general
        assert general.getComUserInitSignal() is False

    def test_set_com_user_status_support(self):
        root = EBModel.getInstance()
        general = ComGeneral(root, "ComGeneral")

        assert general.setComUserStatusSupport(True) == general
        assert general.getComUserStatusSupport() is True

        assert general.setComUserStatusSupport(False) == general
        assert general.getComUserStatusSupport() is False

    def test_set_com_user_tx_confirmation(self):
        root = EBModel.getInstance()
        general = ComGeneral(root, "ComGeneral")

        assert general.setComUserTxConfirmation(True) == general
        assert general.getComUserTxConfirmation() is True

        assert general.setComUserTxConfirmation(False) == general
        assert general.getComUserTxConfirmation() is False

    def test_set_com_user_rx_indication(self):
        root = EBModel.getInstance()
        general = ComGeneral(root, "ComGeneral")

        assert general.setComUserRxIndication(True) == general
        assert general.getComUserRxIndication() is True

        assert general.setComUserRxIndication(False) == general
        assert general.getComUserRxIndication() is False

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        general = ComGeneral(root, "ComGeneral")

        result = (general
                  .setComEnableUserSupport(True)
                  .setComUserInitSignal(False)
                  .setComUserStatusSupport(True)
                  .setComUserTxConfirmation(False)
                  .setComUserRxIndication(True))

        assert result == general
        assert general.getComEnableUserSupport() is True
        assert general.getComUserInitSignal() is False
        assert general.getComUserStatusSupport() is True
        assert general.getComUserTxConfirmation() is False
        assert general.getComUserRxIndication() is True


class TestCom:

    def test_initialization(self):
        root = EBModel.getInstance()
        com = Com(root)

        assert com.getName() == "Com"
        assert com.getParent() == root
        assert com.getComGeneral() is None

    def test_set_com_general(self):
        root = EBModel.getInstance()
        com = Com(root)
        general = ComGeneral(com, "ComGeneral")

        assert com.setComGeneral(general) == com
        assert com.getComGeneral() == general

    def test_set_com_general_none(self):
        root = EBModel.getInstance()
        com = Com(root)
        general = ComGeneral(com, "ComGeneral")

        com.setComGeneral(general)
        assert com.getComGeneral() == general

        com.setComGeneral(None)
        assert com.getComGeneral() == general  # None is ignored
