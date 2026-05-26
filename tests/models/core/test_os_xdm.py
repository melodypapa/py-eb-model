"""
Os Model Tests - Tests for OS module model classes.

Implements: TC_UNIT_OS_00002, TC_UNIT_OS_00005, TC_UNIT_OS_00015, TC_UNIT_OS_00016
"""
import pytest
from eb_model.models.core.os_xdm import Os, OsTask, OsApplication, OsAlarm, OsCounter, OsEvent, OsSpinlock
from eb_model.models.core.eb_doc import EBModel


class TestOsTask:

    def test_initialization(self):
        root = EBModel.getInstance()
        task = OsTask(root, "OsTask")

        assert task.getName() == "OsTask"
        assert task.getParent() == root
        assert task.getOsTaskActivation() is None
        assert task.getOsTaskPriority() is None

    def test_set_os_task_activation(self):
        root = EBModel.getInstance()
        task = OsTask(root, "OsTask")

        assert task.setOsTaskActivation(1) == task
        assert task.getOsTaskActivation() == 1


class TestOsApplication:

    def test_initialization(self):
        root = EBModel.getInstance()
        app = OsApplication(root, "OsApplication")

        assert app.getName() == "OsApplication"
        assert app.getParent() == root
        assert app.getOsTrusted() is False


class TestOsAlarm:

    def test_initialization(self):
        root = EBModel.getInstance()
        alarm = OsAlarm(root, "OsAlarm")

        assert alarm.getName() == "OsAlarm"
        assert alarm.getParent() == root
        assert alarm.getOsAlarmCounterRef() is None

class TestOsCounter:

    def test_initialization(self):
        root = EBModel.getInstance()
        os = root.getOs()
        counter = OsCounter(os, "Counter1")

        assert counter.getName() == "Counter1"
        assert counter.getParent() == os
        assert counter.getOsCounterMaxAllowedValue() is None

    def test_counter_setters(self):
        root = EBModel.getInstance()
        os = root.getOs()
        counter = OsCounter(os, "Counter1")

        counter.setOsCounterMaxAllowedValue(65535)
        counter.setOsCounterMinCycle(1)
        counter.setOsCounterTicksPerBase(1000)
        counter.setOsCounterType("SOFTWARE")

        assert counter.getOsCounterMaxAllowedValue() == 65535
        assert counter.getOsCounterMinCycle() == 1
        assert counter.getOsCounterTicksPerBase() == 1000
        assert counter.getOsCounterType() == "SOFTWARE"

class TestOsEvent:

    def test_initialization(self):
        root = EBModel.getInstance()
        os = root.getOs()
        event = OsEvent(os, "Event1")

        assert event.getName() == "Event1"
        assert event.getParent() == os
        assert event.getOsEventMask() is None

    def test_event_mask(self):
        root = EBModel.getInstance()
        os = root.getOs()
        event = OsEvent(os, "Event1")

        event.setOsEventMask(4)

        assert event.getOsEventMask() == 4

class TestOsSpinlock:

    def test_initialization(self):
        root = EBModel.getInstance()
        os = root.getOs()
        spinlock = OsSpinlock(os, "Spinlock1")

        assert spinlock.getName() == "Spinlock1"
        assert spinlock.getParent() == os
        assert spinlock.getOsSpinlockLockMethod() is None

    def test_spinlock_attributes(self):
        root = EBModel.getInstance()
        os = root.getOs()
        spinlock = OsSpinlock(os, "Spinlock1")

        spinlock.setOsSpinlockLockMethod("LOCK_AND_TRY")
        spinlock.setOsSpinlockSuccessor("Spinlock2")

        assert spinlock.getOsSpinlockLockMethod() == "LOCK_AND_TRY"
        assert spinlock.getOsSpinlockSuccessor() == "Spinlock2"
