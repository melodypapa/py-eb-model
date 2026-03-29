"""
Tm Model Tests - Tests for TM module model classes.
"""
import pytest
from ...models.tm_xdm import Tm, TmGeneral, TmInterruptSynchronization, TmTickTime, TmTrigger
from ...models.eb_doc import EBModel
from ...models.abstract import EcucRefType


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

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        general = TmGeneral(root, "TmGeneral")

        result = (general
                  .setTmDevErrorDetect(True)
                  .setTmMainWindowProtect(False))

        assert result == general
        assert general.getTmDevErrorDetect() is True
        assert general.getTmMainWindowProtect() is False


class TestTmInterruptSynchronization:

    def test_initialization(self):
        root = EBModel.getInstance()
        sync = TmInterruptSynchronization(root, "TmInterruptSynchronization")

        assert sync.getName() == "TmInterruptSynchronization"
        assert sync.getParent() == root
        assert sync.getTmSyncMode() is None

    def test_set_tm_sync_mode(self):
        root = EBModel.getInstance()
        sync = TmInterruptSynchronization(root, "TmInterruptSynchronization")

        assert sync.setTmSyncMode("SYNC") == sync
        assert sync.getTmSyncMode() == "SYNC"

        assert sync.setTmSyncMode("ASYNC") == sync
        assert sync.getTmSyncMode() == "ASYNC"


class TestTmTickTime:

    def test_initialization(self):
        root = EBModel.getInstance()
        tickTime = TmTickTime(root, "TmTickTime")

        assert tickTime.getName() == "TmTickTime"
        assert tickTime.getParent() == root
        assert tickTime.getTmTickTimeBase() is None
        assert tickTime.getTmTickPriority() is None

    def test_set_tm_tick_time_base(self):
        root = EBModel.getInstance()
        tickTime = TmTickTime(root, "TmTickTime")

        assert tickTime.setTmTickTimeBase(100) == tickTime
        assert tickTime.getTmTickTimeBase() == 100

        assert tickTime.setTmTickTimeBase(1000) == tickTime
        assert tickTime.getTmTickTimeBase() == 1000

    def test_set_tm_tick_priority(self):
        root = EBModel.getInstance()
        tickTime = TmTickTime(root, "TmTickTime")

        assert tickTime.setTmTickPriority(5) == tickTime
        assert tickTime.getTmTickPriority() == 5

        assert tickTime.setTmTickPriority(10) == tickTime
        assert tickTime.getTmTickPriority() == 10

    def test_fluent_interface(self):
        root = EBModel.getInstance()
        tickTime = TmTickTime(root, "TmTickTime")

        result = (tickTime
                  .setTmTickTimeBase(100)
                  .setTmTickPriority(10))

        assert result == tickTime
        assert tickTime.getTmTickTimeBase() == 100
        assert tickTime.getTmTickPriority() == 10


class TestTmTrigger:

    def test_initialization(self):
        root = EBModel.getInstance()
        trigger = TmTrigger(root, "TmTrigger1")

        assert trigger.getName() == "TmTrigger1"
        assert trigger.getParent() == root
        assert trigger.getTmTriggerChannelRef() is None

    def test_set_tm_trigger_channel_ref(self):
        root = EBModel.getInstance()
        trigger = TmTrigger(root, "TmTrigger1")

        ref = EcucRefType("/Os/Task1")
        assert trigger.setTmTriggerChannelRef(ref) == trigger
        assert trigger.getTmTriggerChannelRef() == ref


class TestTm:

    def test_initialization(self):
        root = EBModel.getInstance()
        tm = Tm(root)

        assert tm.getName() == "Tm"
        assert tm.getParent() == root
        assert tm.getTmGeneral() is None
        assert tm.getTmInterruptSynchronization() is None
        assert tm.getTmTickTime() is None
        assert len(tm.getTmTriggerList()) == 0

    def test_set_tm_general(self):
        root = EBModel.getInstance()
        tm = Tm(root)
        general = TmGeneral(tm, "TmGeneral")

        assert tm.setTmGeneral(general) == tm
        assert tm.getTmGeneral() == general

    def test_set_tm_interrupt_synchronization(self):
        root = EBModel.getInstance()
        tm = Tm(root)
        sync = TmInterruptSynchronization(tm, "TmInterruptSynchronization")

        assert tm.setTmInterruptSynchronization(sync) == tm
        assert tm.getTmInterruptSynchronization() == sync

    def test_set_tm_tick_time(self):
        root = EBModel.getInstance()
        tm = Tm(root)
        tickTime = TmTickTime(tm, "TmTickTime")

        assert tm.setTmTickTime(tickTime) == tm
        assert tm.getTmTickTime() == tickTime

    def test_add_tm_trigger(self):
        root = EBModel.getInstance()
        tm = Tm(root)
        trigger1 = TmTrigger(tm, "Trigger1")
        trigger2 = TmTrigger(tm, "Trigger2")

        assert tm.addTmTrigger(trigger1) == tm
        assert tm.addTmTrigger(trigger2) == tm

        assert len(tm.getTmTriggerList()) == 2
        assert len(tm.tmTriggers) == 2
        assert trigger1 in tm.getTmTriggerList()
        assert trigger2 in tm.getTmTriggerList()

    def test_get_tm_trigger_list_sorted(self):
        root = EBModel.getInstance()
        tm = Tm(root)
        trigger2 = TmTrigger(tm, "Trigger2")
        trigger1 = TmTrigger(tm, "Trigger1")
        trigger3 = TmTrigger(tm, "Trigger3")

        tm.addTmTrigger(trigger2)
        tm.addTmTrigger(trigger1)
        tm.addTmTrigger(trigger3)

        trigger_list = tm.getTmTriggerList()
        assert trigger_list[0] == trigger1
        assert trigger_list[1] == trigger2
        assert trigger_list[2] == trigger3

    def test_tm_trigger_registered_in_elements(self):
        root = EBModel.getInstance()
        tm = Tm(root)
        trigger = TmTrigger(tm, "Trigger1")

        tm.addTmTrigger(trigger)

        assert tm.getElement("Trigger1") == trigger
        assert tm.getTotalElement() == 1
