"""
Os Model Tests - Tests for OS module model classes.

Implements: TC_UNIT_OS_00002, TC_UNIT_OS_00005, TC_UNIT_OS_00015, TC_UNIT_OS_00016
"""
import pytest
from eb_model.models.core.os_xdm import (
    Os, OsTask, OsApplication, OsAlarm, OsCounter, OsEvent, OsSpinlock,
    OsAlarmAction, OsAlarmAutostart, OsAlarmActivateTask, OsAlarmSetEvent,
    OsAlarmIncrementCounter, OsAlarmCallback, OsResource, OsHooks,
    OsApplication as OsApplicationExtended
)
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.core.abstract import EcucRefType


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

class TestOsAlarmAction:

    def test_initialization(self):
        """
        Test OsAlarmAction initialization.
        
        Implements: UTS_OS_MODEL_00001
        """
        root = EBModel.getInstance()
        action = OsAlarmAction(root, "TestAction")

        assert action.getName() == "TestAction"
        assert action.getParent() == root

class TestOsAlarmAutostart:

    def test_initialization(self):
        """
        Test OsAlarmAutostart initialization.
        
        Implements: UTS_OS_MODEL_00002
        """
        root = EBModel.getInstance()
        autostart = OsAlarmAutostart(root, "Autostart")

        assert autostart.getName() == "Autostart"
        assert autostart.getOsAlarmAutostartType() is None
        assert autostart.getOsAlarmAlarmTime() is None
        assert autostart.getOsAlarmCycleTime() is None

    def test_set_os_alarm_autostart_type(self):
        """
        Test setting OsAlarmAutostart type.
        
        Implements: UTS_OS_MODEL_00002
        """
        root = EBModel.getInstance()
        autostart = OsAlarmAutostart(root, "Autostart")

        autostart.setOsAlarmAutostartType("ABSOLUTE")
        assert autostart.getOsAlarmAutostartType() == "ABSOLUTE"

    def test_set_os_alarm_alarm_time_boundary_values(self):
        """
        Test setting OsAlarmAlarmTime with boundary values.
        
        Implements: UTS_OS_MODEL_00002
        """
        root = EBModel.getInstance()
        autostart = OsAlarmAutostart(root, "Autostart")

        # Test min value
        autostart.setOsAlarmAlarmTime(0)
        assert autostart.getOsAlarmAlarmTime() == 0

        # Test max value
        autostart.setOsAlarmAlarmTime(65535)
        assert autostart.getOsAlarmAlarmTime() == 65535

        # Test typical value
        autostart.setOsAlarmAlarmTime(1000)
        assert autostart.getOsAlarmAlarmTime() == 1000

    def test_set_os_alarm_cycle_time(self):
        """
        Test setting OsAlarmCycleTime.
        
        Implements: UTS_OS_MODEL_00002
        """
        root = EBModel.getInstance()
        autostart = OsAlarmAutostart(root, "Autostart")

        autostart.setOsAlarmCycleTime(500)
        assert autostart.getOsAlarmCycleTime() == 500

class TestOsCounter:

    def test_initialization(self):
        """
        Test OsCounter initialization.
        
        Implements: UTS_OS_MODEL_00005
        """
        root = EBModel.getInstance()
        os = root.getOs()
        counter = OsCounter(os, "Counter1")

        assert counter.getName() == "Counter1"
        assert counter.getParent() == os
        assert counter.getOsCounterMaxAllowedValue() is None
        assert counter.getOsCounterMinCycle() is None
        assert counter.getOsCounterTicksPerBase() is None
        assert counter.getOsCounterType() is None

    def test_counter_setters(self):
        """
        Test OsCounter setters.
        
        Implements: UTS_OS_MODEL_00005
        """
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

    def test_set_os_counter_max_allowed_value_boundary(self):
        """
        Test OsCounterMaxAllowedValue with boundary values.
        
        Implements: UTS_OS_MODEL_00005
        """
        root = EBModel.getInstance()
        os = root.getOs()
        counter = OsCounter(os, "Counter1")

        # Test min value
        counter.setOsCounterMaxAllowedValue(1)
        assert counter.getOsCounterMaxAllowedValue() == 1

        # Test typical value
        counter.setOsCounterMaxAllowedValue(65535)
        assert counter.getOsCounterMaxAllowedValue() == 65535

        # Test max value
        counter.setOsCounterMaxAllowedValue(4294967295)
        assert counter.getOsCounterMaxAllowedValue() == 4294967295

    def test_set_os_counter_type(self):
        """
        Test OsCounterType with different values.
        
        Implements: UTS_OS_MODEL_00005
        """
        root = EBModel.getInstance()
        os = root.getOs()
        counter = OsCounter(os, "Counter1")

        assert counter.setOsCounterType("SOFTWARE") == counter
        assert counter.getOsCounterType() == "SOFTWARE"

        counter.setOsCounterType("HARDWARE")
        assert counter.getOsCounterType() == "HARDWARE"

    def test_set_os_counter_min_cycle(self):
        """
        Test OsCounterMinCycle.
        
        Implements: UTS_OS_MODEL_00005
        """
        root = EBModel.getInstance()
        os = root.getOs()
        counter = OsCounter(os, "Counter1")

        assert counter.setOsCounterMinCycle(1) == counter
        assert counter.getOsCounterMinCycle() == 1

    def test_set_os_counter_ticks_per_base(self):
        """
        Test OsCounterTicksPerBase.
        
        Implements: UTS_OS_MODEL_00005
        """
        root = EBModel.getInstance()
        os = root.getOs()
        counter = OsCounter(os, "Counter1")

        assert counter.setOsCounterTicksPerBase(1000) == counter
        assert counter.getOsCounterTicksPerBase() == 1000

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
