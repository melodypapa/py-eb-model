# Agent 3: Os Module XDM Model Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement all missing classes and attributes for Os module (10 missing classes, many missing attributes) to achieve complete XDM container coverage.

**Architecture:** Follow existing patterns in py-eb-model - extend model classes in `_xdm.py` files, update parsers in `_xdm_parser.py` files, add tests for verification.

**Tech Stack:** Python 3.9+, pytest, xml.etree.ElementTree

---

## File Structure

### New Files to Create
- `src/eb_model/tests/models/test_os_xdm.py` - Os model class tests (if not exists)

### Files to Modify
- `src/eb_model/models/os_xdm.py` - Add 10 missing classes, missing attributes
- `src/eb_model/parser/os_xdm_parser.py` - Add parser methods for new containers and attributes
- `src/eb_model/tests/parser/test_os_xdm_parser.py` - Add tests for new parser methods

---

## Task 1: Create or Update Os Model Test File

**Files:**
- Create or Modify: `src/eb_model/tests/models/test_os_xdm.py`

- [ ] **Step 1: Check if test file exists**

Run: `ls src/eb_model/tests/models/test_os_xdm.py`

If file doesn't exist, create it with structure. If exists, update it.

- [ ] **Step 2: Write test file structure**

```python
"""
Os Model Tests - Tests for OS module model classes.
"""
import pytest
from ...models.os_xdm import Os, OsTask, OsApplication, OsAlarm
from ...models.eb_doc import EBModel


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
        assert app.getOsTrusted() is None
```

- [ ] **Step 3: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/models/test_os_xdm.py -v`
Expected: PASS

- [ ] **Step 4: Commit**

```bash
git add src/eb_model/tests/models/test_os_xdm.py
git commit -m "test: add/update Os model test file structure"
```

---

## Task 2: Add Os Missing Classes

**Files:**
- Modify: `src/eb_model/models/os_xdm.py`

- [ ] **Step 1: Add CommonPublishedInformation class**

```python
class CommonPublishedInformation(EcucParamConfContainerDef):
    """
    Common published information containing AUTOSAR version information.

    Implements: SWR_OS_00010 (Version information)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.arMajorVersion: int = None
        self.arMinorVersion: int = None
        self.arPatchVersion: int = None
        self.swMajorVersion: int = None
        self.swMinorVersion: int = None
        self.swPatchVersion: int = None

    def getArMajorVersion(self) -> int:
        return self.arMajorVersion

    def setArMajorVersion(self, value: int):
        if value is not None:
            self.arMajorVersion = value
        return self

    def getArMinorVersion(self) -> int:
        return self.arMinorVersion

    def setArMinorVersion(self, value: int):
        if value is not None:
            self.arMinorVersion = value
        return self

    def getArPatchVersion(self) -> int:
        return self.arPatchVersion

    def setArPatchVersion(self, value: int):
        if value is not None:
            self.arPatchVersion = value
        return self

    def getSwMajorVersion(self) -> int:
        return self.swMajorVersion

    def setSwMajorVersion(self, value: int):
        if value is not None:
            self.swMajorVersion = value
        return self

    def getSwMinorVersion(self) -> int:
        return self.swMinorVersion

    def setSwMinorVersion(self, value: int):
        if value is not None:
            self.swMinorVersion = value
        return self

    def getSwPatchVersion(self) -> int:
        return self.swPatchVersion

    def setSwPatchVersion(self, value: int):
        if value is not None:
            self.swPatchVersion = value
        return self
```

- [ ] **Step 2: Add PublishedInformation class**

```python
class PublishedInformation(EcucParamConfContainerDef):
    """
    Module-specific published information.

    Implements: SWR_OS_00011 (Module metadata)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.vendorId: str = None
        self.arReleaseMajorVersion: str = None
        self.arReleaseMinorVersion: str = None
        self.arReleasePatchVersion: str = None
        self.swMajorVersion: str = None
        self.swMinorVersion: str = None
        self.swPatchVersion: str = None

    def getVendorId(self) -> str:
        return self.vendorId

    def setVendorId(self, value: str):
        if value is not None:
            self.vendorId = value
        return self

    def getArReleaseMajorVersion(self) -> str:
        return self.arReleaseMajorVersion

    def setArReleaseMajorVersion(self, value: str):
        if value is not None:
            self.arReleaseMajorVersion = value
        return self

    def getArReleaseMinorVersion(self) -> str:
        return self.arReleaseMinorVersion

    def setArReleaseMinorVersion(self, value: str):
        if value is not None:
            self.arReleaseMinorVersion = value
        return self

    def getArReleasePatchVersion(self) -> str:
        return self.arReleasePatchVersion

    def setArReleasePatchVersion(self, value: str):
        if value is not None:
            self.arReleasePatchVersion = value
        return self

    def getSwMajorVersion(self) -> str:
        return self.swMajorVersion

    def setSwMajorVersion(self, value: str):
        if value is not None:
            self.swMajorVersion = value
        return self

    def getSwMinorVersion(self) -> str:
        return self.swMinorVersion

    def setSwMinorVersion(self, value: str):
        if value is not None:
            self.swMinorVersion = value
        return self

    def getSwPatchVersion(self) -> str:
        return self.swPatchVersion

    def setSwPatchVersion(self, value: str):
        if value is not None:
            self.swPatchVersion = value
        return self
```

- [ ] **Step 3: Add OsHwIncrementer class**

```python
class OsHwIncrementer(EcucParamConfContainerDef):
    """
    Hardware incrementer configuration.

    Implements: SWR_OS_00012 (Hardware incrementer)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osHwIncrementerBase: int = None
        self.osHwIncrementerMax: int = None

    def getOsHwIncrementerBase(self) -> int:
        return self.osHwIncrementerBase

    def setOsHwIncrementerBase(self, value: int):
        if value is not None:
            self.osHwIncrementerBase = value
        return self

    def getOsHwIncrementerMax(self) -> int:
        return self.osHwIncrementerMax

    def setOsHwIncrementerMax(self, value: int):
        if value is not None:
            self.osHwIncrementerMax = value
        return self
```

- [ ] **Step 4: Add OsEvent class**

```python
class OsEvent(EcucParamConfContainerDef):
    """
    Event synchronization primitive.

    Implements: SWR_OS_00013 (Event synchronization)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osEventMask: int = None
        self.osEventAutostart: OsTaskAutostart = None

    def getOsEventMask(self) -> int:
        return self.osEventMask

    def setOsEventMask(self, value: int):
        if value is not None:
            self.osEventMask = value
        return self

    def getOsEventAutostart(self) -> OsTaskAutostart:
        return self.osEventAutostart

    def setOsEventAutostart(self, value: OsTaskAutostart):
        if value is not None:
            self.osEventAutostart = value
        return self
```

- [ ] **Step 5: Add OsSpinlock class**

```python
class OsSpinlock(EcucParamConfContainerDef):
    """
    Spinlock synchronization primitive.

    Implements: SWR_OS_00014 (Spinlock synchronization)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osSpinlockType: str = None
        self.osSpinlockSpinCount: int = None

    def getOsSpinlockType(self) -> str:
        return self.osSpinlockType

    def setOsSpinlockType(self, value: str):
        if value is not None:
            self.osSpinlockType = value
        return self

    def getOsSpinlockSpinCount(self) -> int:
        return self.osSpinlockSpinCount

    def setOsSpinlockSpinCount(self, value: int):
        if value is not None:
            self.osSpinlockSpinCount = value
        return self
```

- [ ] **Step 6: Add OsPeripheralArea class**

```python
class OsPeripheralArea(EcucParamConfContainerDef):
    """
    Peripheral memory area configuration.

    Implements: SWR_OS_00015 (Peripheral area)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osPeripheralAreaStartAddress: int = None
        self.osPeripheralAreaEndAddress: int = None
        self.osPeripheralAreaAccessPermission: str = None

    def getOsPeripheralAreaStartAddress(self) -> int:
        return self.osPeripheralAreaStartAddress

    def setOsPeripheralAreaStartAddress(self, value: int):
        if value is not None:
            self.osPeripheralAreaStartAddress = value
        return self

    def getOsPeripheralAreaEndAddress(self) -> int:
        return self.osPeripheralAreaEndAddress

    def setOsPeripheralAreaEndAddress(self, value: int):
        if value is not None:
            self.osPeripheralAreaEndAddress = value
        return self

    def getOsPeripheralAreaAccessPermission(self) -> str:
        return self.osPeripheralAreaAccessPermission

    def setOsPeripheralAreaAccessPermission(self, value: str):
        if value is not None:
            self.osPeripheralAreaAccessPermission = value
        return self
```

- [ ] **Step 7: Add OsOS class**

```python
class OsOS(EcucParamConfContainerDef):
    """
    OS-level configuration.

    Implements: SWR_OS_00016 (OS configuration)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osOSCoreAssignment: int = None
        self.osOsStackMonitoring: bool = None
        self.osOsUseGetServiceId: bool = None
        self.osOsUseParameterAccess: bool = None
        self.osOsUseServiceId: bool = None

    def getOsOSCoreAssignment(self) -> int:
        return self.osOSCoreAssignment

    def setOsOSCoreAssignment(self, value: int):
        if value is not None:
            self.osOSCoreAssignment = value
        return self

    def getOsOsStackMonitoring(self) -> bool:
        return self.osOsStackMonitoring

    def setOsOsStackMonitoring(self, value: bool):
        if value is not None:
            self.osOsStackMonitoring = value
        return self

    def getOsOsUseGetServiceId(self) -> bool:
        return self.osOsUseGetServiceId

    def setOsOsUseGetServiceId(self, value: bool):
        if value is not None:
            self.osOsUseGetServiceId = value
        return self

    def getOsOsUseParameterAccess(self) -> bool:
        return self.osOsUseParameterAccess

    def setOsOsUseParameterAccess(self, value: bool):
        if value is not None:
            self.osOsUseParameterAccess = value
        return self

    def getOsOsUseServiceId(self) -> bool:
        return self.osOsUseServiceId

    def setOsOsUseServiceId(self, value: bool):
        if value is not None:
            self.osOsUseServiceId = value
        return self
```

- [ ] **Step 8: Add OsHooks class**

```python
class OsHooks(EcucParamConfContainerDef):
    """
    OS hook configuration.

    Implements: SWR_OS_00017 (Hook configuration)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osErrorHook: bool = None
        self.osShutdownHook: bool = None
        self.osStartupHook: bool = None
        self.osPreTaskHook: bool = None
        self.osPostTaskHook: bool = None
        self.osProtectionHook: bool = None

    def getOsErrorHook(self) -> bool:
        return self.osErrorHook

    def setOsErrorHook(self, value: bool):
        if value is not None:
            self.osErrorHook = value
        return self

    def getOsShutdownHook(self) -> bool:
        return self.osShutdownHook

    def setOsShutdownHook(self, value: bool):
        if value is not None:
            self.osShutdownHook = value
        return self

    def getOsStartupHook(self) -> bool:
        return self.osStartupHook

    def setOsStartupHook(self, value: bool):
        if value is not None:
            self.osStartupHook = value
        return self

    def getOsPreTaskHook(self) -> bool:
        return self.osPreTaskHook

    def setOsPreTaskHook(self, value: bool):
        if value is not None:
            self.osPreTaskHook = value
        return self

    def getOsPostTaskHook(self) -> bool:
        return self.osPostTaskHook

    def setOsPostTaskHook(self, value: bool):
        if value is not None:
            self.osPostTaskHook = value
        return self

    def getOsProtectionHook(self) -> bool:
        return self.osProtectionHook

    def setOsProtectionHook(self, value: bool):
        if value is not None:
            self.osProtectionHook = value
        return self
```

- [ ] **Step 9: Add OsCoreConfig class**

```python
class OsCoreConfig(EcucParamConfContainerDef):
    """
    Multi-core configuration.

    Implements: SWR_OS_00018 (Core configuration)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osCoreId: int = None
        self.osCoreMainFunction: str = None
        self.osCoreStackStartAddress: int = None
        self.osCoreStackSize: int = None

    def getOsCoreId(self) -> int:
        return self.osCoreId

    def setOsCoreId(self, value: int):
        if value is not None:
            self.osCoreId = value
        return self

    def getOsCoreMainFunction(self) -> str:
        return self.osCoreMainFunction

    def setOsCoreMainFunction(self, value: str):
        if value is not None:
            self.osCoreMainFunction = value
        return self

    def getOsCoreStackStartAddress(self) -> int:
        return self.osCoreStackStartAddress

    def setOsCoreStackStartAddress(self, value: int):
        if value is not None:
            self.osCoreStackStartAddress = value
        return self

    def getOsCoreStackSize(self) -> int:
        return self.osCoreStackSize

    def setOsCoreStackSize(self, value: int):
        if value is not None:
            self.osCoreStackSize = value
        return self
```

- [ ] **Step 10: Add OsAutosarCustomization class**

```python
class OsAutosarCustomization(EcucParamConfContainerDef):
    """
    AUTOSAR-specific customizations.

    Implements: SWR_OS_00019 (AUTOSAR customization)
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.osScalableClass: str = None
        self.osApplicationType: str = None

    def getOsScalableClass(self) -> str:
        return self.osScalableClass

    def setOsScalableClass(self, value: str):
        if value is not None:
            self.osScalableClass = value
        return self

    def getOsApplicationType(self) -> str:
        return self.osApplicationType

    def setOsApplicationType(self, value: str):
        if value is not None:
            self.osApplicationType = value
        return self
```

- [ ] **Step 11: Add missing attributes to OsAlarm class**

Add these attributes to `OsAlarm.__init__`:

```python
self.osAlarmCallbackName: str = None
```

Add these getter/setter methods after existing methods:

```python
def getOsAlarmCallbackName(self) -> str:
    return self.osAlarmCallbackName

def setOsAlarmCallbackName(self, value: str):
    if value is not None:
        self.osAlarmCallbackName = value
    return self
```

- [ ] **Step 12: Add missing attributes to OsApplication class**

Add these attributes to `OsApplication.__init__`:

```python
self.osAppErrorHookStack: int = None
self.osAppShutdownHookStack: int = None
self.osAppStartupHookStack: int = None
self.osTrustedFunctionName: str = None
```

Add these getter/setter methods after existing methods:

```python
def getOsAppErrorHookStack(self) -> int:
    return self.osAppErrorHookStack

def setOsAppErrorHookStack(self, value: int):
    if value is not None:
        self.osAppErrorHookStack = value
    return self

def getOsAppShutdownHookStack(self) -> int:
    return self.osAppShutdownHookStack

def setOsAppShutdownHookStack(self, value: int):
    if value is not None:
        self.osAppShutdownHookStack = value
    return self

def getOsAppStartupHookStack(self) -> int:
    return self.osAppStartupHookStack

def setOsAppStartupHookStack(self, value: int):
    if value is not None:
        self.osAppStartupHookStack = value
    return self

def getOsTrustedFunctionName(self) -> str:
    return self.osTrustedFunctionName

def setOsTrustedFunctionName(self, value: str):
    if value is not None:
        self.osTrustedFunctionName = value
    return self
```

- [ ] **Step 13: Add missing attributes to OsTask class**

Add these attributes to `OsTask.__init__`:

```python
self.osMeasureMaxRuntime: bool = None
self.osTaskUseHwFp: bool = None
self.osTaskCallScheduler: str = None
self.osTaskType: str = None
self.osTaskAppModeRef: EcucRefType = None
```

Add these getter/setter methods after existing methods:

```python
def getOsMeasureMaxRuntime(self) -> bool:
    return self.osMeasureMaxRuntime

def setOsMeasureMaxRuntime(self, value: bool):
    if value is not None:
        self.osMeasureMaxRuntime = value
    return self

def getOsTaskUseHwFp(self) -> bool:
    return self.osTaskUseHwFp

def setOsTaskUseHwFp(self, value: bool):
    if value is not None:
        self.osTaskUseHwFp = value
    return self

def getOsTaskCallScheduler(self) -> str:
    return self.osTaskCallScheduler

def setOsTaskCallScheduler(self, value: str):
    if value is not None:
        self.osTaskCallScheduler = value
    return self

def getOsTaskType(self) -> str:
    return self.osTaskType

def setOsTaskType(self, value: str):
    if value is not None:
        self.osTaskType = value
    return self

def getOsTaskAppModeRef(self) -> EcucRefType:
    return self.osTaskAppModeRef

def setOsTaskAppModeRef(self, value: EcucRefType):
    if value is not None:
        self.osTaskAppModeRef = value
    return self
```

- [ ] **Step 14: Add missing attributes to OsCounter class**

Add these attributes to `OsCounter.__init__`:

```python
self.osCounterWindowsTimer: str = None
self.osWindowsIrqLevel: int = None
self.osConstName: str = None
self.osHwModule: str = None
```

Add these getter/setter methods after existing methods:

```python
def getOsCounterWindowsTimer(self) -> str:
    return self.osCounterWindowsTimer

def setOsCounterWindowsTimer(self, value: str):
    if value is not None:
        self.osCounterWindowsTimer = value
    return self

def getOsWindowsIrqLevel(self) -> int:
    return self.osWindowsIrqLevel

def setOsWindowsIrqLevel(self, value: int):
    if value is not None:
        self.osWindowsIrqLevel = value
    return self

def getOsConstName(self) -> str:
    return self.osConstName

def setOsConstName(self, value: str):
    if value is not None:
        self.osConstName = value
    return self

def getOsHwModule(self) -> str:
    return self.osHwModule

def setOsHwModule(self, value: str):
    if value is not None:
        self.osHwModule = value
    return self
```

- [ ] **Step 15: Add new containers to Os module class**

Add to `Os.__init__`:

```python
self.commonPublishedInformation: CommonPublishedInformation = None
self.publishedInformation: PublishedInformation = None
self.osHwIncrementer: OsHwIncrementer = None
self.osEvents: List[OsEvent] = []
self.osSpinlocks: List[OsSpinlock] = []
self.osPeripheralAreas: List[OsPeripheralArea] = []
self.osOS: OsOS = None
self.osHooks: OsHooks = None
self.osCoreConfigs: List[OsCoreConfig] = []
self.osAutosarCustomization: OsAutosarCustomization = None
```

Add these getter/setter methods to `Os` class:

```python
def getCommonPublishedInformation(self) -> CommonPublishedInformation:
    return self.commonPublishedInformation

def setCommonPublishedInformation(self, value: CommonPublishedInformation):
    if value is not None:
        self.commonPublishedInformation = value
    return self

def getPublishedInformation(self) -> PublishedInformation:
    return self.publishedInformation

def setPublishedInformation(self, value: PublishedInformation):
    if value is not None:
        self.publishedInformation = value
    return self

def getOsHwIncrementer(self) -> OsHwIncrementer:
    return self.osHwIncrementer

def setOsHwIncrementer(self, value: OsHwIncrementer):
    if value is not None:
        self.osHwIncrementer = value
    return self

def getOsEventList(self) -> List[OsEvent]:
    return list(sorted(filter(lambda a: isinstance(a, OsEvent), self.elements.values()), key=lambda o: o.name))

def addOsEvent(self, value: OsEvent):
    self.addElement(value)
    self.osEvents.append(value)
    return self

def getOsSpinlockList(self) -> List[OsSpinlock]:
    return list(sorted(filter(lambda a: isinstance(a, OsSpinlock), self.elements.values()), key=lambda o: o.name))

def addOsSpinlock(self, value: OsSpinlock):
    self.addElement(value)
    self.osSpinlocks.append(value)
    return self

def getOsPeripheralAreaList(self) -> List[OsPeripheralArea]:
    return list(sorted(filter(lambda a: isinstance(a, OsPeripheralArea), self.elements.values()), key=lambda o: o.name))

def addOsPeripheralArea(self, value: OsPeripheralArea):
    self.addElement(value)
    self.osPeripheralAreas.append(value)
    return self

def getOsOS(self) -> OsOS:
    return self.osOS

def setOsOS(self, value: OsOS):
    if value is not None:
        self.osOS = value
    return self

def getOsHooks(self) -> OsHooks:
    return self.osHooks

def setOsHooks(self, value: OsHooks):
    if value is not None:
        self.osHooks = value
    return self

def getOsCoreConfigList(self) -> List[OsCoreConfig]:
    return list(sorted(filter(lambda a: isinstance(a, OsCoreConfig), self.elements.values()), key=lambda o: o.name))

def addOsCoreConfig(self, value: OsCoreConfig):
    self.addElement(value)
    self.osCoreConfigs.append(value)
    return self

def getOsAutosarCustomization(self) -> OsAutosarCustomization:
    return self.osAutosarCustomization

def setOsAutosarCustomization(self, value: OsAutosarCustomization):
    if value is not None:
        self.osAutosarCustomization = value
    return self
```

- [ ] **Step 16: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/models/test_os_xdm.py -v`
Expected: PASS

- [ ] **Step 17: Commit**

```bash
git add src/eb_model/models/os_xdm.py src/eb_model/tests/models/test_os_xdm.py
git commit -m "feat(os): add 10 missing classes and many missing attributes

Add CommonPublishedInformation, PublishedInformation, OsHwIncrementer,
OsEvent, OsSpinlock, OsPeripheralArea, OsOS, OsHooks, OsCoreConfig,
OsAutosarCustomization classes. Add missing attributes to OsAlarm,
OsApplication, OsTask, OsCounter classes."
```

---

## Task 3: Update Os Parser for New Containers and Attributes

**Files:**
- Modify: `src/eb_model/parser/os_xdm_parser.py`

- [ ] **Step 1: Add import for new classes**

Update the imports to include all new classes.

- [ ] **Step 2: Add parser method for CommonPublishedInformation**

```python
def read_common_published_information(self, element: ET.Element, os: Os):
    """Parse CommonPublishedInformation container from XDM."""
    ctr_tag = self.find_ctr_tag(element, "CommonPublishedInformation")
    if ctr_tag is not None:
        pub_info = CommonPublishedInformation(os, ctr_tag.attrib["name"])
        pub_info.setArMajorVersion(self.read_value(ctr_tag, "ArMajorVersion"))
        pub_info.setArMinorVersion(self.read_value(ctr_tag, "ArMinorVersion"))
        pub_info.setArPatchVersion(self.read_value(ctr_tag, "ArPatchVersion"))
        pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
        pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
        pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
        os.setCommonPublishedInformation(pub_info)
        self.logger.debug("Read CommonPublishedInformation")
```

- [ ] **Step 3: Add parser method for PublishedInformation**

```python
def read_published_information(self, element: ET.Element, os: Os):
    """Parse PublishedInformation container from XDM."""
    ctr_tag = self.find_ctr_tag(element, "PublishedInformation")
    if ctr_tag is not None:
        pub_info = PublishedInformation(os, ctr_tag.attrib["name"])
        pub_info.setVendorId(self.read_value(ctr_tag, "VendorId"))
        pub_info.setArReleaseMajorVersion(self.read_value(ctr_tag, "ArReleaseMajorVersion"))
        pub_info.setArReleaseMinorVersion(self.read_value(ctr_tag, "ArReleaseMinorVersion"))
        pub_info.setArReleasePatchVersion(self.read_value(ctr_tag, "ArReleasePatchVersion"))
        pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
        pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
        pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
        os.setPublishedInformation(pub_info)
        self.logger.debug("Read PublishedInformation")
```

- [ ] **Step 4: Add parser methods for remaining new containers**

Add parser methods for OsHwIncrementer, OsEvent, OsSpinlock, OsPeripheralArea, OsOS, OsHooks, OsCoreConfig, OsAutosarCustomization following the same pattern.

- [ ] **Step 5: Update existing parser methods to read missing attributes**

Update `read_os_alarms`, `read_os_applications`, `read_os_tasks`, `read_os_counters` methods to read the new attributes added in Task 2.

- [ ] **Step 6: Update parse method to call new parser methods**

Add calls to all new parser methods in the `parse` method.

- [ ] **Step 7: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/parser/test_os_xdm_parser.py -v`
Expected: PASS

- [ ] **Step 8: Commit**

```bash
git add src/eb_model/parser/os_xdm_parser.py
git commit -m "feat(os): update parser for 10 new containers and missing attributes

Add parser methods for all new containers. Update existing parser methods
to read missing attributes from OsAlarm, OsApplication, OsTask, OsCounter."
```

---

## Task 4: Add Os Parser Tests for New Functionality

**Files:**
- Modify: `src/eb_model/tests/parser/test_os_xdm_parser.py`

- [ ] **Step 1: Add tests for new container parsers**

Add tests for CommonPublishedInformation, PublishedInformation, OsHwIncrementer, OsEvent, and other new containers following the same pattern as Tm and Det tests.

- [ ] **Step 2: Update existing tests to include new attributes**

Update `test_read_os_task`, `test_read_os_application`, `test_read_os_alarm`, `test_read_os_counter` tests to include assertions for new attributes.

- [ ] **Step 3: Run tests to verify they pass**

Run: `pytest src/eb_model/tests/parser/test_os_xdm_parser.py -v`
Expected: PASS

- [ ] **Step 4: Commit**

```bash
git add src/eb_model/tests/parser/test_os_xdm_parser.py
git commit -m "test(os): add tests for new container parsers and missing attributes"
```

---

## Task 5: Run Linting and Final Verification

**Files:**
- All modified files

- [ ] **Step 1: Run flake8 on modified files**

Run: `flake8 src/eb_model/models/os_xdm.py src/eb_model/parser/os_xdm_parser.py src/eb_model/tests/models/test_os_xdm.py src/eb_model/tests/parser/test_os_xdm_parser.py --max-line-length=150 --ignore=F401,W293,F403`

Expected: No errors

- [ ] **Step 2: Run all tests**

Run: `pytest src/eb_model/tests/models/test_os_xdm.py src/eb_model/tests/parser/test_os_xdm_parser.py -v`

Expected: All PASS

- [ ] **Step 3: Verify against analysis report checklist**

Manually verify:
- Os: 10 missing classes implemented
- OsAlarm: 1 missing attribute implemented
- OsApplication: 4 missing attributes implemented
- OsTask: 5 missing attributes implemented
- OsCounter: 4 missing attributes implemented

- [ ] **Step 4: Create completion summary**

Create file: `docs/superpowers/completion/2026-03-29-agent3-os-completion.md`

```markdown
# Agent 3: Os Module Completion Summary

**Date:** 2026-03-29
**Agent:** 3
**Module:** Os

## Work Completed

### Os Module
- Added CommonPublishedInformation class
- Added PublishedInformation class
- Added OsHwIncrementer class
- Added OsEvent class
- Added OsSpinlock class
- Added OsPeripheralArea class
- Added OsOS class
- Added OsHooks class
- Added OsCoreConfig class
- Added OsAutosarCustomization class
- Added missing attributes to existing classes:
  - OsAlarm: 1 attribute
  - OsApplication: 4 attributes
  - OsTask: 5 attributes
  - OsCounter: 4 attributes
- Updated OsXdmParser with parser methods for all new containers and attributes
- Created or updated test file `src/eb_model/tests/models/test_os_xdm.py`
- Added parser tests for new functionality

## Files Modified
- `src/eb_model/models/os_xdm.py`
- `src/eb_model/parser/os_xdm_parser.py`
- `src/eb_model/tests/models/test_os_xdm.py` (created/updated)
- `src/eb_model/tests/parser/test_os_xdm_parser.py` (updated)

## Test Results
All tests passing:
- Os model tests: PASS
- Os parser tests: PASS

## Coverage Summary
- Os: 10/10 missing classes implemented (100%)
- OsAlarm attributes: 1/1 missing attributes implemented (100%)
- OsApplication attributes: 4/4 missing attributes implemented (100%)
- OsTask attributes: 5/5 missing attributes implemented (100%)
- OsCounter attributes: 4/4 missing attributes implemented (100%)

## Notes
- All code follows established patterns from py-eb-model
- All classes have proper docstrings with SWR references
- Linting passed with no errors
- Ready for integration verification
```

- [ ] **Step 5: Commit completion summary**

```bash
git add docs/superpowers/completion/2026-03-29-agent3-os-completion.md
git commit -m "docs: add Agent 3 (Os) completion summary"
```

---

## Summary

This plan implements complete coverage for Os module:

**Os Module:**
- 10 missing classes added (CommonPublishedInformation, PublishedInformation, OsHwIncrementer, OsEvent, OsSpinlock, OsPeripheralArea, OsOS, OsHooks, OsCoreConfig, OsAutosarCustomization)
- 14 missing attributes added to existing classes (1 to OsAlarm, 4 to OsApplication, 5 to OsTask, 4 to OsCounter)

All work follows existing patterns in py-eb-model with proper docstrings, tests, and linting compliance.