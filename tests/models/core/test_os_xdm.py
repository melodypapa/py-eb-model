"""
Os Model Tests - Tests for OS module model classes.

Implements: TC_UNIT_OS_00002, TC_UNIT_OS_00005, TC_UNIT_OS_00015, TC_UNIT_OS_00016
"""
import pytest
from eb_model.models.core.os_xdm import (
    Os, OsTask, OsApplication, OsAlarm, OsCounter, OsEvent, OsSpinlock,
    OsAlarmAction, OsAlarmAutostart, OsAlarmActivateTask, OsAlarmSetEvent,
    OsAlarmIncrementCounter, OsAlarmCallback, OsResource, OsHooks,
    OsApplication as OsApplicationExtended, OsAppMode, OsIsr, OsPeripheralArea,
    OsScheduleTable
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

class TestOsTaskExtended:

    def test_set_os_task_priority_boundary(self):
        """
        Test OsTaskPriority with boundary values.

        Implements: UTS_OS_MODEL_00006
        """
        root = EBModel.getInstance()
        task = OsTask(root, "Task")

        # Test min priority
        task.setOsTaskPriority(0)
        assert task.getOsTaskPriority() == 0

        # Test max priority
        task.setOsTaskPriority(255)
        assert task.getOsTaskPriority() == 255

        # Test typical priority
        task.setOsTaskPriority(128)
        assert task.getOsTaskPriority() == 128

    def test_set_os_task_schedule(self):
        """
        Test OsTaskSchedule.

        Implements: UTS_OS_MODEL_00006
        """
        root = EBModel.getInstance()
        task = OsTask(root, "Task")

        assert task.setOsTaskSchedule("FULL") == task
        assert task.getOsTaskSchedule() == "FULL"

        task.setOsTaskSchedule("NON")
        assert task.getOsTaskSchedule() == "NON"

    def test_set_os_task_type(self):
        """
        Test OsTaskType.

        Implements: UTS_OS_MODEL_00006
        """
        root = EBModel.getInstance()
        task = OsTask(root, "Task")

        assert task.setOsTaskType("BASIC") == task
        assert task.getOsTaskType() == "BASIC"

        task.setOsTaskType("EXTENDED")
        assert task.getOsTaskType() == "EXTENDED"

    def test_set_os_task_activation(self):
        """
        Test OsTaskActivation.

        Implements: UTS_OS_MODEL_00006
        """
        root = EBModel.getInstance()
        task = OsTask(root, "Task")

        assert task.setOsTaskActivation(1) == task
        assert task.getOsTaskActivation() == 1

    def test_set_os_stacksize(self):
        """
        Test OsStacksize.

        Implements: UTS_OS_MODEL_00006
        """
        root = EBModel.getInstance()
        task = OsTask(root, "Task")

        assert task.setOsStacksize(1024) == task
        assert task.getOsStacksize() == 1024

class TestOsApplicationExtended:

    def test_set_os_trusted(self):
        """
        Test OsTrusted flag.

        Implements: UTS_OS_MODEL_00008
        """
        root = EBModel.getInstance()
        app = OsApplication(root, "App")

        assert app.setOsTrusted(True) == app
        assert app.getOsTrusted() is True

        app.setOsTrusted(False)
        assert app.getOsTrusted() is False

    def test_set_os_trusted_function_name(self):
        """
        Test OsTrustedFunctionName.

        Implements: UTS_OS_MODEL_00008
        """
        root = EBModel.getInstance()
        app = OsApplication(root, "App")

        app.setOsTrustedFunctionName("TrustedFunc")
        assert app.getOsTrustedFunctionName() == "TrustedFunc"

    def test_set_os_application_core_assignment(self):
        """
        Test OsApplicationCoreAssignment.

        Implements: UTS_OS_MODEL_00008
        """
        root = EBModel.getInstance()
        app = OsApplication(root, "App")

        app.setOsApplicationCoreAssignment(0)
        assert app.getOsApplicationCoreAssignment() == 0

class TestOsResource:

    def test_initialization(self):
        """
        Test OsResource initialization.

        Implements: UTS_OS_MODEL_00009
        """
        root = EBModel.getInstance()
        resource = OsResource(root, "Resource")

        assert resource.getName() == "Resource"
        assert resource.getOsResourceProperty() is None

    def test_set_os_resource_property(self):
        """
        Test OsResourceProperty.

        Implements: UTS_OS_MODEL_00009
        """
        root = EBModel.getInstance()
        resource = OsResource(root, "Resource")

        assert resource.setOsResourceProperty("STANDARD") == resource
        assert resource.getOsResourceProperty() == "STANDARD"

        resource.setOsResourceProperty("LINKED")
        assert resource.getOsResourceProperty() == "LINKED"

    def test_set_os_linked_resource_ref(self):
        """
        Test OsLinkedResourceRef.

        Implements: UTS_OS_MODEL_00009
        """
        root = EBModel.getInstance()
        resource2 = OsResource(root, "Resource2")

        ref = EcucRefType("ASPath:/Os/Resource1")
        resource2.setOsLinkedResourceRef(ref)
        assert resource2.getOsLinkedResourceRef() == ref

class TestOsHooks:

    def test_initialization(self):
        """
        Test OsHooks initialization.

        Implements: UTS_OS_MODEL_00010
        """
        root = EBModel.getInstance()
        hooks = OsHooks(root, "OsHooks")

        assert hooks.getName() == "OsHooks"
        assert hooks.getOsStartupHook() is None
        assert hooks.getOsShutdownHook() is None
        assert hooks.getOsErrorHook() is None
        assert hooks.getOsPreTaskHook() is None
        assert hooks.getOsPostTaskHook() is None

    def test_set_os_startup_hook(self):
        """
        Test OsStartupHook.

        Implements: UTS_OS_MODEL_00010
        """
        root = EBModel.getInstance()
        hooks = OsHooks(root, "OsHooks")

        assert hooks.setOsStartupHook(True) == hooks
        assert hooks.getOsStartupHook() is True

    def test_set_os_shutdown_hook(self):
        """
        Test OsShutdownHook.

        Implements: UTS_OS_MODEL_00010
        """
        root = EBModel.getInstance()
        hooks = OsHooks(root, "OsHooks")

        assert hooks.setOsShutdownHook(True) == hooks
        assert hooks.getOsShutdownHook() is True

    def test_set_os_error_hook(self):
        """
        Test OsErrorHook.

        Implements: UTS_OS_MODEL_00010
        """
        root = EBModel.getInstance()
        hooks = OsHooks(root, "OsHooks")

        assert hooks.setOsErrorHook(True) == hooks
        assert hooks.getOsErrorHook() is True

    def test_hook_combinations(self):
        """
        Test OsHooks flag combinations.

        Implements: UTS_OS_MODEL_00010
        """
        root = EBModel.getInstance()
        hooks = OsHooks(root, "OsHooks")

        # All enabled
        hooks.setOsStartupHook(True).setOsShutdownHook(True).setOsErrorHook(True)
        hooks.setOsPreTaskHook(True).setOsPostTaskHook(True)
        assert hooks.getOsStartupHook() is True
        assert hooks.getOsShutdownHook() is True
        assert hooks.getOsErrorHook() is True
        assert hooks.getOsPreTaskHook() is True
        assert hooks.getOsPostTaskHook() is True

        # All disabled
        hooks.setOsStartupHook(False).setOsShutdownHook(False).setOsErrorHook(False)
        hooks.setOsPreTaskHook(False).setOsPostTaskHook(False)
        assert hooks.getOsStartupHook() is False
        assert hooks.getOsShutdownHook() is False
        assert hooks.getOsErrorHook() is False
        assert hooks.getOsPreTaskHook() is False
        assert hooks.getOsPostTaskHook() is False


class TestOsAppMode:

    def test_initialization(self):
        """
        Test OsAppMode initialization.

        Implements: UTS_OS_MODEL_00004
        """
        root = EBModel.getInstance()
        os = root.getOs()
        app_mode = OsAppMode(os, "AppMode1")

        assert app_mode.getName() == "AppMode1"
        assert app_mode.getParent() == os


class TestOsIsr:

    def test_initialization(self):
        """
        Test OsIsr initialization.

        Implements: UTS_OS_MODEL_00014
        """
        root = EBModel.getInstance()
        os = root.getOs()
        isr = OsIsr(os, "ISR1")

        assert isr.getName() == "ISR1"
        assert isr.getParent() == os
        assert isr.getOsIsrCategory() is None
        assert isr.getOsStacksize() is None

    def test_set_os_isr_category(self):
        """
        Test OsIsrCategory with different values.

        Implements: UTS_OS_MODEL_00015
        """
        root = EBModel.getInstance()
        os = root.getOs()
        isr = OsIsr(os, "ISR1")

        isr.setOsIsrCategory("CATEGORY_1")
        assert isr.getOsIsrCategory() == "CATEGORY_1"

        isr.setOsIsrCategory("CATEGORY_2")
        assert isr.getOsIsrCategory() == "CATEGORY_2"

    def test_set_os_stacksize_boundary_values(self):
        """
        Test OsStacksize with boundary values.

        Implements: UTS_OS_MODEL_00016
        """
        root = EBModel.getInstance()
        os = root.getOs()
        isr = OsIsr(os, "ISR1")

        # Test min value
        isr.setOsStacksize(0)
        assert isr.getOsStacksize() == 0

        # Test typical small stack
        isr.setOsStacksize(1024)
        assert isr.getOsStacksize() == 1024

        # Test typical medium stack
        isr.setOsStacksize(4096)
        assert isr.getOsStacksize() == 4096

        # Test max value
        isr.setOsStacksize(2000000000)
        assert isr.getOsStacksize() == 2000000000


class TestOsPeripheralArea:

    def test_initialization(self):
        """
        Test OsPeripheralArea initialization.

        Implements: UTS_OS_MODEL_00020
        """
        root = EBModel.getInstance()
        os = root.getOs()
        peripheral_area = OsPeripheralArea(os, "PeripheralArea1")

        assert peripheral_area.getName() == "PeripheralArea1"
        assert peripheral_area.getParent() == os
        assert peripheral_area.getOsPeripheralAreaStartAddress() is None
        assert peripheral_area.getOsPeripheralAreaEndAddress() is None
        assert peripheral_area.getOsPeripheralAreaId() is None

    def test_set_peripheral_area_addresses(self):
        """
        Test OsPeripheralArea address fields.

        Implements: UTS_OS_MODEL_00021
        """
        root = EBModel.getInstance()
        os = root.getOs()
        peripheral_area = OsPeripheralArea(os, "PeripheralArea1")

        # Test min values
        peripheral_area.setOsPeripheralAreaStartAddress(0)
        peripheral_area.setOsPeripheralAreaEndAddress(0)
        peripheral_area.setOsPeripheralAreaId(0)

        assert peripheral_area.getOsPeripheralAreaStartAddress() == 0
        assert peripheral_area.getOsPeripheralAreaEndAddress() == 0
        assert peripheral_area.getOsPeripheralAreaId() == 0

        # Test max values
        peripheral_area.setOsPeripheralAreaStartAddress(9223372036854775807)
        peripheral_area.setOsPeripheralAreaEndAddress(9223372036854775807)
        peripheral_area.setOsPeripheralAreaId(9223372036854775807)

        assert peripheral_area.getOsPeripheralAreaStartAddress() == 9223372036854775807
        assert peripheral_area.getOsPeripheralAreaEndAddress() == 9223372036854775807
        assert peripheral_area.getOsPeripheralAreaId() == 9223372036854775807


class TestOsScheduleTable:

    def test_initialization(self):
        """
        Test OsScheduleTable initialization.

        Implements: UTS_OS_MODEL_00024
        """
        root = EBModel.getInstance()
        os = root.getOs()
        schedule_table = OsScheduleTable(os, "ScheduleTable1")

        assert schedule_table.getName() == "ScheduleTable1"
        assert schedule_table.getParent() == os
        assert schedule_table.getOsScheduleTableDuration() is None
        assert schedule_table.getOsScheduleTableRepeating() is None
        assert schedule_table.getOsScheduleTableCounterRef() is None

    def test_set_duration_and_repeating(self):
        """
        Test OsScheduleTable duration and repeating fields.

        Implements: UTS_OS_MODEL_00025
        """
        root = EBModel.getInstance()
        os = root.getOs()
        schedule_table = OsScheduleTable(os, "ScheduleTable1")

        schedule_table.setOsScheduleTableDuration(100)
        schedule_table.setOsScheduleTableRepeating(True)

        assert schedule_table.getOsScheduleTableDuration() == 100
        assert schedule_table.getOsScheduleTableRepeating() is True

        schedule_table.setOsScheduleTableDuration(1000)
        schedule_table.setOsScheduleTableRepeating(False)

        assert schedule_table.getOsScheduleTableDuration() == 1000
        assert schedule_table.getOsScheduleTableRepeating() is False

    def test_set_counter_ref(self):
        """
        Test OsScheduleTableCounterRef field.

        Implements: UTS_OS_MODEL_00026
        """
        root = EBModel.getInstance()
        os = root.getOs()
        schedule_table = OsScheduleTable(os, "ScheduleTable1")

        counter_ref = EcucRefType("/Os/Counter1")
        schedule_table.setOsScheduleTableCounterRef(counter_ref)

        assert schedule_table.getOsScheduleTableCounterRef() == counter_ref


class TestOsRoot:

    def test_initialization(self):
        """
        Test Os root model initialization.

        Implements: UTS_OS_MODEL_00027
        """
        root = EBModel.getInstance()
        os = root.getOs()

        assert os is not None
        assert os.getOsTaskList() == []
        assert os.getOsIsrList() == []
        assert os.getOsAlarmList() == []

    def test_entity_list_methods(self):
        """
        Test Os root model entity list methods.

        Implements: UTS_OS_MODEL_00028
        """
        root = EBModel.getInstance()
        os = root.getOs()

        # Add entities
        task = OsTask(os, "Task1")
        isr = OsIsr(os, "ISR1")
        alarm = OsAlarm(os, "Alarm1")
        counter = OsCounter(os, "Counter1")
        app = OsApplication(os, "App1")
        resource = OsResource(os, "Resource1")
        event = OsEvent(os, "Event1")
        spinlock = OsSpinlock(os, "Spinlock1")
        peripheral_area = OsPeripheralArea(os, "PeripheralArea1")
        schedule_table = OsScheduleTable(os, "ScheduleTable1")

        os.addOsTask(task)
        os.addOsIsr(isr)
        os.addOsAlarm(alarm)
        os.addOsCounter(counter)
        os.addOsApplication(app)
        os.addOsResource(resource)
        os.addOsEvent(event)
        os.addOsSpinlock(spinlock)
        os.addOsPeripheralArea(peripheral_area)
        os.addOsScheduleTable(schedule_table)

        assert len(os.getOsTaskList()) == 1
        assert len(os.getOsIsrList()) == 1
        assert len(os.getOsAlarmList()) == 1
        assert len(os.getOsCounterList()) == 1
        assert len(os.getOsApplicationList()) == 1
        assert len(os.getOsResourceList()) == 1
        assert len(os.getOsEventList()) == 1
        assert len(os.getOsSpinlockList()) == 1
        assert len(os.getOsPeripheralAreaList()) == 1
        assert len(os.getOsScheduleTableList()) == 1

    def test_appmode_list_method(self):
        """
        Test Os root model getOsAppModeList method.

        Implements: UTS_OS_MODEL_00029
        """
        root = EBModel.getInstance()
        os = root.getOs()

        app_mode1 = OsAppMode(os, "AppMode1")
        app_mode2 = OsAppMode(os, "AppMode2")

        os.addOsAppMode(app_mode1)
        os.addOsAppMode(app_mode2)

        assert len(os.getOsAppModeList()) == 2
