# OS Module Test Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement comprehensive unit tests for OS module (model, parser, reporter) to achieve >90% coverage

**Architecture:** Follow NvM test pattern - enhance MOCK_OS_XDM, add model tests for all classes, add parser tests for all methods, add reporter tests for all sheets

**Tech Stack:** Python, pytest, openpyxl, xml.etree.ElementTree

---

## File Structure

### Test Files (Create/Modify)
- **Modify:** `tests/mock_data.py` - Enhance MOCK_OS_XDM with comprehensive test data
- **Modify:** `tests/models/core/test_os_xdm.py` - Add 60 new model tests
- **Modify:** `tests/parser/core/test_os_xdm_parser.py` - Add 40 new parser tests
- **Modify:** `tests/reporter/excel_reporter/core/test_os_xdm.py` - Add 24 new reporter tests

### Implementation Files (Reference Only)
- `src/eb_model/models/core/os_xdm.py` - 38 OS model classes
- `src/eb_model/parser/core/os_xdm_parser.py` - OS XDM parser
- `src/eb_model/reporter/excel_reporter/core/os_xdm.py` - OS Excel reporter

---

## Task 1: Enhance MOCK_OS_XDM Test Data

**Files:**
- Modify: `tests/mock_data.py:8-250`

- [ ] **Step 1: Add comprehensive OsTask instances**

Add to MOCK_OS_XDM after existing Task2:

```xml
<d:ctr name="Task3">
  <d:var name="OsTaskPriority" type="INTEGER" value="1"/>
  <d:var name="OsTaskActivation" type="INTEGER" value="1"/>
  <d:var name="OsTaskSchedule" type="ENUMERATION" value="NON"/>
  <d:var name="OsStacksize" type="INTEGER" value="512"/>
  <d:var name="OsTaskType" type="ENUMERATION" value="BASIC"/>
  <d:var name="OsTaskAutostart" type="BOOLEAN" value="true"/>
</d:ctr>
<d:ctr name="TaskExtended">
  <d:var name="OsTaskPriority" type="INTEGER" value="10"/>
  <d:var name="OsTaskActivation" type="INTEGER" value="5"/>
  <d:var name="OsTaskSchedule" type="ENUMERATION" value="FULL"/>
  <d:var name="OsStacksize" type="INTEGER" value="4096"/>
  <d:var name="OsTaskType" type="ENUMERATION" value="EXTENDED"/>
  <d:var name="OsTaskAutostart" type="BOOLEAN" value="false"/>
</d:ctr>
```

- [ ] **Step 2: Add OsAlarm instances with all action types**

Add after existing Alarm1:

```xml
<d:ctr name="AlarmSetEvent">
  <d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Counter1"/>
  <d:chc name="OsAlarmAction" value="OsAlarmSetEvent">
    <d:ctr name="OsAlarmSetEvent">
      <d:ref name="OsAlarmSetEventTaskRef" type="REFERENCE" value="ASPath:/Os/Task1"/>
      <d:ref name="OsAlarmSetEventRef" type="REFERENCE" value="ASPath:/Os/Event1"/>
    </d:ctr>
  </d:chc>
</d:ctr>
<d:ctr name="AlarmIncrementCounter">
  <d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Counter2"/>
  <d:chc name="OsAlarmAction" value="OsAlarmIncrementCounter">
    <d:ctr name="OsAlarmIncrementCounter">
      <d:ref name="OsAlarmIncrementCounterRef" type="REFERENCE" value="ASPath:/Os/Counter1"/>
    </d:ctr>
  </d:chc>
</d:ctr>
<d:ctr name="AlarmCallback">
  <d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Counter1"/>
  <d:chc name="OsAlarmAction" value="OsAlarmCallback">
    <d:ctr name="OsAlarmCallback">
      <d:var name="OsAlarmCallbackName" type="FUNCTION-NAME" value="AlarmCallbackFunction"/>
    </d:ctr>
  </d:chc>
</d:ctr>
```

- [ ] **Step 3: Add OsApplication instances with trust configurations**

Add after OsAlarm section:

```xml
<d:lst name="OsApplication" type="MAP">
  <d:ctr name="AppTrusted">
    <d:var name="OsTrusted" type="BOOLEAN" value="true"/>
    <d:var name="OsTrustedFunction" type="BOOLEAN" value="true"/>
    <d:var name="OsRestartTask" type="BOOLEAN" value="true"/>
  </d:ctr>
  <d:ctr name="AppUntrusted">
    <d:var name="OsTrusted" type="BOOLEAN" value="false"/>
    <d:var name="OsTrustedFunction" type="BOOLEAN" value="false"/>
    <d:var name="OsRestartTask" type="BOOLEAN" value="false"/>
  </d:ctr>
  <d:ctr name="AppMixed">
    <d:var name="OsTrusted" type="BOOLEAN" value="false"/>
    <d:var name="OsTrustedFunction" type="BOOLEAN" value="true"/>
    <d:var name="OsRestartTask" type="BOOLEAN" value="true"/>
  </d:ctr>
</d:lst>
```

- [ ] **Step 4: Add OsEvent instances**

Add after OsApplication section:

```xml
<d:lst name="OsEvent" type="MAP">
  <d:ctr name="Event1">
    <d:var name="OsEventProperty" type="ENUMERATION" value="STANDARD"/>
  </d:ctr>
  <d:ctr name="Event2">
    <d:var name="OsEventProperty" type="ENUMERATION" value="STANDARD"/>
  </d:ctr>
</d:lst>
```

- [ ] **Step 5: Add OsResource instances**

Add after OsEvent section:

```xml
<d:lst name="OsResource" type="MAP">
  <d:ctr name="Resource1">
    <d:var name="OsResourceProperty" type="ENUMERATION" value="STANDARD"/>
    <d:lst name="OsResourceAccessingApplication" type="MAP">
      <d:ref type="REFERENCE" value="ASPath:/Os/AppTrusted"/>
    </d:lst>
  </d:ctr>
  <d:ctr name="ResourceLinked">
    <d:var name="OsResourceProperty" type="ENUMERATION" value="LINKED"/>
    <d:ref name="OsLinkedResourceRef" type="REFERENCE" value="ASPath:/Os/Resource1"/>
  </d:ctr>
</d:lst>
```

- [ ] **Step 6: Add OsSpinlock instances**

Add after OsResource section:

```xml
<d:lst name="OsSpinlock" type="MAP">
  <d:ctr name="Spinlock1">
    <d:var name="OsSpinlockLockMethod" type="ENUMERATION" value="LOCK_ALL"/>
    <d:var name="OsSpinlockPriority" type="INTEGER" value="1"/>
  </d:ctr>
</d:lst>
```

- [ ] **Step 7: Add OsHooks configuration**

Add after OsSpinlock section:

```xml
<d:ctr name="OsHooks">
  <d:var name="OsStartupHook" type="BOOLEAN" value="true"/>
  <d:var name="OsShutdownHook" type="BOOLEAN" value="true"/>
  <d:var name="OsErrorHook" type="BOOLEAN" value="true"/>
  <d:var name="OsPreTaskHook" type="BOOLEAN" value="false"/>
  <d:var name="OsPostTaskHook" type="BOOLEAN" value="false"/>
</d:ctr>
```

- [ ] **Step 8: Add OsOS configuration with microkernel**

Add after OsHooks section:

```xml
<d:ctr name="OsOS">
  <d:var name="OsStackMonitoring" type="BOOLEAN" value="true"/>
  <d:var name="OsUseGetServiceId" type="BOOLEAN" value="true"/>
  <d:var name="OsUseParameterAccess" type="BOOLEAN" value="true"/>
  <d:var name="OsScalabilityClass" type="ENUMERATION" value="SC1"/>
  <d:ctr name="OsMicrokernel">
    <d:var name="MkMemoryProtection" type="BOOLEAN" value="true"/>
    <d:lst name="MkMemoryRegion" type="MAP">
      <d:ctr name="Region1">
        <d:var name="MkMemoryRegionStart" type="INTEGER" value="0x1000"/>
        <d:var name="MkMemoryRegionSize" type="INTEGER" value="0x1000"/>
        <d:var name="MkMemoryRegionRead" type="BOOLEAN" value="true"/>
        <d:var name="MkMemoryRegionWrite" type="BOOLEAN" value="true"/>
      </d:ctr>
    </d:lst>
  </d:ctr>
</d:ctr>
```

- [ ] **Step 9: Run tests to verify MOCK_OS_XDM is valid**

Run: `source .venv/bin/activate && python -m pytest tests/parser/core/test_os_xdm_parser.py -v --tb=short -o addopts=""`

Expected: All existing tests pass

- [ ] **Step 10: Commit enhanced MOCK_OS_XDM**

```bash
git add tests/mock_data.py
git commit -m "test: enhance MOCK_OS_XDM with comprehensive test data"
```

---

## Task 2: Add OsAlarmAction Model Tests

**Files:**
- Modify: `tests/models/core/test_os_xdm.py`

- [ ] **Step 1: Write test for OsAlarmAction initialization**

Add to test_os_xdm.py after TestOsAlarm class:

```python
class TestOsAlarmAction:

    def test_initialization(self):
        root = EBModel.getInstance()
        action = OsAlarmAction(root, "TestAction")

        assert action.getName() == "TestAction"
        assert action.getParent() == root

    def test_set_os_alarm_action_name(self):
        root = EBModel.getInstance()
        action = OsAlarmAction(root, "TestAction")

        assert action.setOsAlarmActionName("ActionName") == action
        assert action.getOsAlarmActionName() == "ActionName"
```

- [ ] **Step 2: Run test to verify it passes**

Run: `source .venv/bin/activate && python -m pytest tests/models/core/test_os_xdm.py::TestOsAlarmAction -v --tb=short -o addopts=""`

Expected: 2 tests pass

- [ ] **Step 3: Commit OsAlarmAction tests**

```bash
git add tests/models/core/test_os_xdm.py
git commit -m "test: add OsAlarmAction model tests"
```

---

## Task 3: Add OsAlarmAutostart Model Tests

**Files:**
- Modify: `tests/models/core/test_os_xdm.py`

- [ ] **Step 1: Write test for OsAlarmAutostart with boundary values**

Add to test_os_xdm.py after TestOsAlarmAction class:

```python
class TestOsAlarmAutostart:

    def test_initialization(self):
        root = EBModel.getInstance()
        autostart = OsAlarmAutostart(root, "Autostart")

        assert autostart.getName() == "Autostart"
        assert autostart.getOsAlarmAutostartType() is None
        assert autostart.getOsAlarmAlarmTime() is None
        assert autostart.getOsAlarmCycleTime() is None

    def test_set_os_alarm_autostart_type(self):
        root = EBModel.getInstance()
        autostart = OsAlarmAutostart(root, "Autostart")

        assert autostart.setOsAlarmAutostartType("ABSOLUTE") == autostart
        assert autostart.getOsAlarmAutostartType() == "ABSOLUTE"

    def test_set_os_alarm_alarm_time_boundary_values(self):
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
        root = EBModel.getInstance()
        autostart = OsAlarmAutostart(root, "Autostart")

        assert autostart.setOsAlarmCycleTime(500) == autostart
        assert autostart.getOsAlarmCycleTime() == 500
```

- [ ] **Step 2: Run test to verify it passes**

Run: `source .venv/bin/activate && python -m pytest tests/models/core/test_os_xdm.py::TestOsAlarmAutostart -v --tb=short -o addopts=""`

Expected: 4 tests pass

- [ ] **Step 3: Commit OsAlarmAutostart tests**

```bash
git add tests/models/core/test_os_xdm.py
git commit -m "test: add OsAlarmAutostart model tests with boundary values"
```

---

## Task 4: Add OsCounter Model Tests

**Files:**
- Modify: `tests/models/core/test_os_xdm.py`

- [ ] **Step 1: Write test for OsCounter with boundary values**

Add to test_os_xdm.py after TestOsAlarmAutostart class:

```python
class TestOsCounter:

    def test_initialization(self):
        root = EBModel.getInstance()
        counter = OsCounter(root, "Counter")

        assert counter.getName() == "Counter"
        assert counter.getOsCounterMaxAllowedValue() is None
        assert counter.getOsCounterMinCycle() is None
        assert counter.getOsCounterTicksPerBase() is None
        assert counter.getOsCounterType() is None

    def test_set_os_counter_max_allowed_value_boundary(self):
        root = EBModel.getInstance()
        counter = OsCounter(root, "Counter")

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
        root = EBModel.getInstance()
        counter = OsCounter(root, "Counter")

        assert counter.setOsCounterType("SOFTWARE") == counter
        assert counter.getOsCounterType() == "SOFTWARE"

        counter.setOsCounterType("HARDWARE")
        assert counter.getOsCounterType() == "HARDWARE"

    def test_set_os_counter_min_cycle(self):
        root = EBModel.getInstance()
        counter = OsCounter(root, "Counter")

        assert counter.setOsCounterMinCycle(1) == counter
        assert counter.getOsCounterMinCycle() == 1

    def test_set_os_counter_ticks_per_base(self):
        root = EBModel.getInstance()
        counter = OsCounter(root, "Counter")

        assert counter.setOsCounterTicksPerBase(1000) == counter
        assert counter.getOsCounterTicksPerBase() == 1000
```

- [ ] **Step 2: Run test to verify it passes**

Run: `source .venv/bin/activate && python -m pytest tests/models/core/test_os_xdm.py::TestOsCounter -v --tb=short -o addopts=""`

Expected: 5 tests pass

- [ ] **Step 3: Commit OsCounter tests**

```bash
git add tests/models/core/test_os_xdm.py
git commit -m "test: add OsCounter model tests with boundary values"
```

---

## Task 5: Add OsTask Model Tests

**Files:**
- Modify: `tests/models/core/test_os_xdm.py`

- [ ] **Step 1: Write test for OsTask with priority and scheduling**

Add to test_os_xdm.py after TestOsCounter class:

```python
class TestOsTaskExtended:

    def test_set_os_task_priority_boundary(self):
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
        root = EBModel.getInstance()
        task = OsTask(root, "Task")

        assert task.setOsTaskSchedule("FULL") == task
        assert task.getOsTaskSchedule() == "FULL"

        task.setOsTaskSchedule("NON")
        assert task.getOsTaskSchedule() == "NON"

    def test_set_os_task_type(self):
        root = EBModel.getInstance()
        task = OsTask(root, "Task")

        assert task.setOsTaskType("BASIC") == task
        assert task.getOsTaskType() == "BASIC"

        task.setOsTaskType("EXTENDED")
        assert task.getOsTaskType() == "EXTENDED"

    def test_set_os_task_activation(self):
        root = EBModel.getInstance()
        task = OsTask(root, "Task")

        assert task.setOsTaskActivation(1) == task
        assert task.getOsTaskActivation() == 1

    def test_set_os_stacksize(self):
        root = EBModel.getInstance()
        task = OsTask(root, "Task")

        assert task.setOsStacksize(1024) == task
        assert task.getOsStacksize() == 1024
```

- [ ] **Step 2: Run test to verify it passes**

Run: `source .venv/bin/activate && python -m pytest tests/models/core/test_os_xdm.py::TestOsTaskExtended -v --tb=short -o addopts=""`

Expected: 5 tests pass

- [ ] **Step 3: Commit OsTask tests**

```bash
git add tests/models/core/test_os_xdm.py
git commit -m "test: add OsTask model tests with priority and scheduling"
```

---

## Task 6: Add OsApplication Model Tests

**Files:**
- Modify: `tests/models/core/test_os_xdm.py`

- [ ] **Step 1: Write test for OsApplication with trust configuration**

Add to test_os_xdm.py after TestOsTaskExtended class:

```python
class TestOsApplicationExtended:

    def test_set_os_trusted(self):
        root = EBModel.getInstance()
        app = OsApplication(root, "App")

        assert app.setOsTrusted(True) == app
        assert app.getOsTrusted() is True

        app.setOsTrusted(False)
        assert app.getOsTrusted() is False

    def test_set_os_trusted_function(self):
        root = EBModel.getInstance()
        app = OsApplication(root, "App")

        assert app.setOsTrustedFunction(True) == app
        assert app.getOsTrustedFunction() is True

    def test_set_os_restart_task(self):
        root = EBModel.getInstance()
        app = OsApplication(root, "App")

        assert app.setOsRestartTask(True) == app
        assert app.getOsRestartTask() is True

    def test_trust_combinations(self):
        root = EBModel.getInstance()
        app = OsApplication(root, "App")

        # All trusted
        app.setOsTrusted(True).setOsTrustedFunction(True).setOsRestartTask(True)
        assert app.getOsTrusted() is True
        assert app.getOsTrustedFunction() is True
        assert app.getOsRestartTask() is True

        # None trusted
        app.setOsTrusted(False).setOsTrustedFunction(False).setOsRestartTask(False)
        assert app.getOsTrusted() is False
        assert app.getOsTrustedFunction() is False
        assert app.getOsRestartTask() is False
```

- [ ] **Step 2: Run test to verify it passes**

Run: `source .venv/bin/activate && python -m pytest tests/models/core/test_os_xdm.py::TestOsApplicationExtended -v --tb=short -o addopts=""`

Expected: 4 tests pass

- [ ] **Step 3: Commit OsApplication tests**

```bash
git add tests/models/core/test_os_xdm.py
git commit -m "test: add OsApplication model tests with trust configuration"
```

---

## Task 7: Add OsResource Model Tests

**Files:**
- Modify: `tests/models/core/test_os_xdm.py`

- [ ] **Step 1: Write test for OsResource with access control**

Add to test_os_xdm.py after TestOsApplicationExtended class:

```python
class TestOsResource:

    def test_initialization(self):
        root = EBModel.getInstance()
        resource = OsResource(root, "Resource")

        assert resource.getName() == "Resource"
        assert resource.getOsResourceProperty() is None

    def test_set_os_resource_property(self):
        root = EBModel.getInstance()
        resource = OsResource(root, "Resource")

        assert resource.setOsResourceProperty("STANDARD") == resource
        assert resource.getOsResourceProperty() == "STANDARD"

        resource.setOsResourceProperty("LINKED")
        assert resource.getOsResourceProperty() == "LINKED"

    def test_set_os_linked_resource_ref(self):
        root = EBModel.getInstance()
        resource1 = OsResource(root, "Resource1")
        resource2 = OsResource(root, "Resource2")

        ref = EcucRefType(resource2, "ASPath:/Os/Resource1")
        resource2.setOsLinkedResourceRef(ref)
        assert resource2.getOsLinkedResourceRef() == ref
```

- [ ] **Step 2: Run test to verify it passes**

Run: `source .venv/bin/activate && python -m pytest tests/models/core/test_os_xdm.py::TestOsResource -v --tb=short -o addopts=""`

Expected: 3 tests pass

- [ ] **Step 3: Commit OsResource tests**

```bash
git add tests/models/core/test_os_xdm.py
git commit -m "test: add OsResource model tests with access control"
```

---

## Task 8: Add OsHooks Model Tests

**Files:**
- Modify: `tests/models/core/test_os_xdm.py`

- [ ] **Step 1: Write test for OsHooks with hook configuration**

Add to test_os_xdm.py after TestOsResource class:

```python
class TestOsHooks:

    def test_initialization(self):
        root = EBModel.getInstance()
        hooks = OsHooks(root, "OsHooks")

        assert hooks.getName() == "OsHooks"
        assert hooks.getOsStartupHook() is None
        assert hooks.getOsShutdownHook() is None
        assert hooks.getOsErrorHook() is None
        assert hooks.getOsPreTaskHook() is None
        assert hooks.getOsPostTaskHook() is None

    def test_set_os_startup_hook(self):
        root = EBModel.getInstance()
        hooks = OsHooks(root, "OsHooks")

        assert hooks.setOsStartupHook(True) == hooks
        assert hooks.getOsStartupHook() is True

    def test_set_os_shutdown_hook(self):
        root = EBModel.getInstance()
        hooks = OsHooks(root, "OsHooks")

        assert hooks.setOsShutdownHook(True) == hooks
        assert hooks.getOsShutdownHook() is True

    def test_set_os_error_hook(self):
        root = EBModel.getInstance()
        hooks = OsHooks(root, "OsHooks")

        assert hooks.setOsErrorHook(True) == hooks
        assert hooks.getOsErrorHook() is True

    def test_hook_combinations(self):
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
```

- [ ] **Step 2: Run test to verify it passes**

Run: `source .venv/bin/activate && python -m pytest tests/models/core/test_os_xdm.py::TestOsHooks -v --tb=short -o addopts=""`

Expected: 5 tests pass

- [ ] **Step 3: Commit OsHooks tests**

```bash
git add tests/models/core/test_os_xdm.py
git commit -m "test: add OsHooks model tests with hook configuration"
```

---

## Task 9: Run Model Coverage Analysis

**Files:**
- None (analysis only)

- [ ] **Step 1: Run coverage for OS model tests**

Run: `source .venv/bin/activate && python -m pytest tests/models/core/test_os_xdm.py --cov=eb_model.models.core.os_xdm --cov-report=term-missing -o addopts=""`

Expected: Coverage >85%

- [ ] **Step 2: Identify remaining coverage gaps**

Review output and list uncovered lines.

- [ ] **Step 3: Document coverage status**

Create a note of current coverage percentage and remaining gaps.

---

## Task 10: Add Parser Tests for OsAlarm Actions

**Files:**
- Modify: `tests/parser/core/test_os_xdm_parser.py`

- [ ] **Step 1: Write test for parsing OsAlarm with different action types**

Add to test_os_xdm_parser.py:

```python
    def test_parse_alarm_set_event_action(self):
        """
        Test parsing OsAlarm with OsAlarmSetEvent action.

        Implements: UTS_OS_PARSER_00003
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:chc type="AR-ELEMENT" value="MODULE-CONFIGURATION" name="Os"/>
            <d:ctr name="Os">
                <d:lst name="OsAlarm" type="MAP">
                    <d:ctr name="AlarmSetEvent">
                        <d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Counter1"/>
                        <d:chc name="OsAlarmAction" value="OsAlarmSetEvent">
                            <d:ctr name="OsAlarmSetEvent">
                                <d:ref name="OsAlarmSetEventTaskRef" type="REFERENCE" value="ASPath:/Os/Task1"/>
                                <d:ref name="OsAlarmSetEventRef" type="REFERENCE" value="ASPath:/Os/Event1"/>
                            </d:ctr>
                        </d:chc>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        EBModel._EBModel__instance = None
        doc = EBModel.getInstance()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }
        parser.parse(element, doc)

        alarms = doc.getOs().getOsAlarmList()
        assert len(alarms) == 1
        alarm = alarms[0]
        assert alarm.getName() == "AlarmSetEvent"
        action = alarm.getOsAlarmAction()
        assert isinstance(action, OsAlarmSetEvent)

    def test_parse_alarm_callback_action(self):
        """
        Test parsing OsAlarm with OsAlarmCallback action.

        Implements: UTS_OS_PARSER_00003
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:chc type="AR-ELEMENT" value="MODULE-CONFIGURATION" name="Os"/>
            <d:ctr name="Os">
                <d:lst name="OsAlarm" type="MAP">
                    <d:ctr name="AlarmCallback">
                        <d:ref name="OsAlarmCounterRef" type="REFERENCE" value="ASPath:/Os/Counter1"/>
                        <d:chc name="OsAlarmAction" value="OsAlarmCallback">
                            <d:ctr name="OsAlarmCallback">
                                <d:var name="OsAlarmCallbackName" type="FUNCTION-NAME" value="CallbackFunc"/>
                            </d:ctr>
                        </d:chc>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        EBModel._EBModel__instance = None
        doc = EBModel.getInstance()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }
        parser.parse(element, doc)

        alarms = doc.getOs().getOsAlarmList()
        assert len(alarms) == 1
        alarm = alarms[0]
        action = alarm.getOsAlarmAction()
        assert isinstance(action, OsAlarmCallback)
        assert action.getOsAlarmCallbackName() == "CallbackFunc"
```

- [ ] **Step 2: Run test to verify it passes**

Run: `source .venv/bin/activate && python -m pytest tests/parser/core/test_os_xdm_parser.py::TestOsXdmParser::test_parse_alarm_set_event_action tests/parser/core/test_os_xdm_parser.py::TestOsXdmParser::test_parse_alarm_callback_action -v --tb=short -o addopts=""`

Expected: 2 tests pass

- [ ] **Step 3: Commit parser tests**

```bash
git add tests/parser/core/test_os_xdm_parser.py
git commit -m "test: add OsAlarm action parser tests"
```

---

## Task 11: Add Parser Tests for OsApplication

**Files:**
- Modify: `tests/parser/core/test_os_xdm_parser.py`

- [ ] **Step 1: Write test for parsing OsApplication with trust configuration**

Add to test_os_xdm_parser.py:

```python
    def test_parse_os_application_trusted(self):
        """
        Test parsing OsApplication with trust configuration.

        Implements: UTS_OS_PARSER_00006
        """
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:chc type="AR-ELEMENT" value="MODULE-CONFIGURATION" name="Os"/>
            <d:ctr name="Os">
                <d:lst name="OsApplication" type="MAP">
                    <d:ctr name="AppTrusted">
                        <d:var name="OsTrusted" type="BOOLEAN" value="true"/>
                        <d:var name="OsTrustedFunction" type="BOOLEAN" value="true"/>
                        <d:var name="OsRestartTask" type="BOOLEAN" value="true"/>
                    </d:ctr>
                    <d:ctr name="AppUntrusted">
                        <d:var name="OsTrusted" type="BOOLEAN" value="false"/>
                        <d:var name="OsTrustedFunction" type="BOOLEAN" value="false"/>
                        <d:var name="OsRestartTask" type="BOOLEAN" value="false"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        EBModel._EBModel__instance = None
        doc = EBModel.getInstance()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }
        parser.parse(element, doc)

        apps = doc.getOs().getOsApplicationList()
        assert len(apps) == 2

        trusted_app = apps[0]
        assert trusted_app.getName() == "AppTrusted"
        assert trusted_app.getOsTrusted() is True
        assert trusted_app.getOsTrustedFunction() is True
        assert trusted_app.getOsRestartTask() is True

        untrusted_app = apps[1]
        assert untrusted_app.getName() == "AppUntrusted"
        assert untrusted_app.getOsTrusted() is False
        assert untrusted_app.getOsTrustedFunction() is False
        assert untrusted_app.getOsRestartTask() is False
```

- [ ] **Step 2: Run test to verify it passes**

Run: `source .venv/bin/activate && python -m pytest tests/parser/core/test_os_xdm_parser.py::TestOsXdmParser::test_parse_os_application_trusted -v --tb=short -o addopts=""`

Expected: 1 test passes

- [ ] **Step 3: Commit parser tests**

```bash
git add tests/parser/core/test_os_xdm_parser.py
git commit -m "test: add OsApplication parser tests with trust configuration"
```

---

## Task 12: Run Full Test Suite and Coverage Analysis

**Files:**
- None (analysis only)

- [ ] **Step 1: Run full OS test suite**

Run: `source .venv/bin/activate && python -m pytest tests/models/core/test_os_xdm.py tests/parser/core/test_os_xdm_parser.py tests/reporter/excel_reporter/core/test_os_xdm.py --cov=eb_model.models.core.os_xdm --cov=eb_model.parser.core.os_xdm_parser --cov=eb_model.reporter.excel_reporter.core.os_xdm --cov-report=term-missing -o addopts=""`

Expected: All tests pass, coverage >85% for all components

- [ ] **Step 2: Document final coverage results**

Record final coverage percentages:
- Model: ____%
- Parser: ____%
- Reporter: ____%

- [ ] **Step 3: Create summary of remaining gaps**

List any uncovered lines or features that need additional tests.

---

## Task 13: Final Commit and Documentation

**Files:**
- None (git operations only)

- [ ] **Step 1: Push all commits to remote**

```bash
git push origin main
```

- [ ] **Step 2: Update test specification document**

Add implementation status to `docs/tests/unit/uts_os_test-specs.md`:
- Mark implemented test cases
- Update coverage results
- Add notes on any deviations

- [ ] **Step 3: Commit documentation updates**

```bash
git add docs/tests/unit/uts_os_test-specs.md
git commit -m "docs: update OS test specification with implementation status"
git push origin main
```

---

## Success Criteria

1. **Coverage Targets Met:**
   - Model: >90%
   - Parser: >90%
   - Reporter: >90%

2. **All Tests Pass:**
   - No failing tests
   - No skipped tests without justification

3. **Documentation Complete:**
   - All test cases documented inline
   - Coverage report generated
   - Implementation status updated

4. **Code Quality:**
   - Follows existing test patterns
   - DRY principles applied
   - Clear test names and documentation

---

## Notes

- This plan implements a subset of the full test specification (Tasks 1-13 cover the most critical tests)
- Additional tests can be added incrementally following the same pattern
- Focus on achieving >90% coverage first, then add edge case tests
- Use MOCK_OS_XDM for all parser tests to ensure consistency
