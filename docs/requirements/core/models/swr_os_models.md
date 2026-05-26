# Software Requirements: OS Module - Model Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | OS Module Model Layer Requirements |
| Document ID | SWR_OS_MODELS_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | OS (Operating System) - Model Layer |

---

## Overview

The OS Model Layer provides Python classes representing AUTOSAR OS configuration entities extracted from EB Tresos XDM files.

**Implementation:** `src/eb_model/models/core/os_xdm.py`

---

## Requirements

### SWR_OS_MODELS_00001 - OsTask Model

The system shall provide an `OsTask` model class for OS task configuration.

| Field | Type | Description |
|-------|------|-------------|
| OsTaskPriority | int | Task priority (0-255) |
| OsTaskActivation | int | Maximum activations |
| OsTaskSchedule | str | Schedule type (FULL/NON) |
| OsStacksize | int | Stack size in bytes |
| OsTaskType | str | Task type (BASIC/EXTENDED) |
| OsTaskAutostart | bool | Autostart flag |

**Methods:**
- `IsPreemptable()` - Returns True if OsTaskSchedule is FULL
- `setOsTaskPriority(value)` - Set task priority
- `setOsTaskSchedule(value)` - Set schedule type
- `setOsTaskType(value)` - Set task type

**Implementation:** `os_xdm.py:OsTask`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_MODELS_00002 - OsIsr Model

The system shall provide an `OsIsr` model class for Interrupt Service Routines.

| Field | Type | Description |
|-------|------|-------------|
| OsIsrCategory | str | ISR category (CATEGORY_1/CATEGORY_2) |
| OsIsrPriority | int | ISR priority |
| OsIsrVector | int | Interrupt vector |
| OsIsrStackSize | int | Stack size |
| OsIsrTricoreIrqLevel | int | TriCore IRQ level (optional) |
| OsIsrTricoreVector | int | TriCore vector (optional) |

**Implementation:** `os_xdm.py:OsIsr`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_MODELS_00003 - OsCounter Model

The system shall provide an `OsCounter` model class for time measurement counters.

| Field | Type | Description |
|-------|------|-------------|
| OsCounterMaxAllowedValue | int | Maximum counter value |
| OsCounterMinCycle | int | Minimum cycle time |
| OsCounterTicksPerBase | int | Ticks per base unit |
| OsCounterType | str | Counter type (HARDWARE/SOFTWARE) |

**Implementation:** `os_xdm.py:OsCounter`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_MODELS_00004 - OsAlarm Model

The system shall provide an `OsAlarm` model class for time-based alarms.

| Field | Type | Description |
|-------|------|-------------|
| OsAlarmCounterRef | EcucRefType | Reference to counter |
| OsAlarmAction | OsAlarmAction | Alarm action (ActivateTask/SetEvent/IncrementCounter/Callback) |
| OsAlarmAutostart | OsAlarmAutostart | Autostart configuration |

**Implementation:** `os_xdm.py:OsAlarm`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_MODELS_00005 - OsAlarmAction Models

The system shall provide alarm action model classes.

| Class | Purpose |
|-------|---------|
| OsAlarmActivateTask | Activate a task when alarm triggers |
| OsAlarmSetEvent | Set an event when alarm triggers |
| OsAlarmIncrementCounter | Increment a counter when alarm triggers |
| OsAlarmCallback | Execute callback function when alarm triggers |

**Implementation:** `os_xdm.py:OsAlarmActivateTask`, `os_xdm.py:OsAlarmSetEvent`, etc.
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_MODELS_00006 - OsApplication Model

The system shall provide an `OsApplication` model class for OS application boundaries.

| Field | Type | Description |
|-------|------|-------------|
| OsTrusted | bool | Trusted application flag |
| OsApplicationCoreAssignment | int | Core assignment |
| OsAppTaskRefs | List[EcucRefType] | Task references |
| OsAppIsrRefs | List[EcucRefType] | ISR references |
| OsAppAlarmRefs | List[EcucRefType] | Alarm references |

**Implementation:** `os_xdm.py:OsApplication`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_MODELS_00007 - OsResource Model

The system shall provide an `OsResource` model class for resource management.

| Field | Type | Description |
|-------|------|-------------|
| OsResourceProperty | str | Property type (STANDARD/LINKED) |
| OsResourceLinkedResourceRefs | List[EcucRefType] | Linked resource references |

**Implementation:** `os_xdm.py:OsResource`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_MODELS_00008 - OsHooks Model

The system shall provide an `OsHooks` model class for OS hook configuration.

| Field | Type | Description |
|-------|------|-------------|
| OsStartupHook | bool | Startup hook enabled |
| OsShutdownHook | bool | Shutdown hook enabled |
| OsErrorHook | bool | Error hook enabled |
| OsPreTaskHook | bool | Pre-task hook enabled |
| OsPostTaskHook | bool | Post-task hook enabled |

**Implementation:** `os_xdm.py:OsHooks`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_MODELS_00009 - OsScheduleTable Model

The system shall provide an `OsScheduleTable` model class for cyclic scheduling.

| Field | Type | Description |
|-------|------|-------------|
| OsScheduleTableDuration | int | Table duration |
| OsScheduleTableRepeating | bool | Repeating flag |
| OsScheduleTableCounterRef | EcucRefType | Counter reference |
| OsScheduleTableAutostart | OsScheduleTableAutostart | Autostart configuration |

**Implementation:** `os_xdm.py:OsScheduleTable`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_MODELS_00010 - OsEvent Model

The system shall provide an `OsEvent` model class for event masks.

| Field | Type | Description |
|-------|------|-------------|
| OsEventMask | int | Event mask value |

**Implementation:** `os_xdm.py:OsEvent`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_MODELS_00011 - OsSpinlock Model

The system shall provide an `OsSpinlock` model class for multi-core synchronization.

| Field | Type | Description |
|-------|------|-------------|
| OsSpinlockLockMethod | str | Lock method |
| OsSpinlockSuccessor | str | Successor spinlock |

**Implementation:** `os_xdm.py:OsSpinlock`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_MODELS_00012 - Os Model (Root)

The system shall provide an `Os` root model class containing all OS entities.

**Methods:**
- `getOsTaskList()` - Get all tasks
- `getOsIsrList()` - Get all ISRs
- `getOsAlarmList()` - Get all alarms
- `getOsCounterList()` - Get all counters
- `getOsApplicationList()` - Get all applications
- `getOsResourceList()` - Get all resources
- `getOsEventList()` - Get all events
- `getOsSpinlockList()` - Get all spinlocks
- `getOsScheduleTableList()` - Get all schedule tables
- `getOsTaskOsApplication(taskName)` - Get application for task (O(1) lookup)
- `getOsIsrOsApplication(isrName)` - Get application for ISR (O(1) lookup)

**Implementation:** `os_xdm.py:Os`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_OS_MODELS_00001 | os_xdm.py:OsTask | UTS_OS_MODEL_00001 |
| SWR_OS_MODELS_00002 | os_xdm.py:OsIsr | UTS_OS_MODEL_00002 |
| SWR_OS_MODELS_00003 | os_xdm.py:OsCounter | UTS_OS_MODEL_00005 |
| SWR_OS_MODELS_00004 | os_xdm.py:OsAlarm | UTS_OS_MODEL_00003 |
| SWR_OS_MODELS_00005 | os_xdm.py:OsAlarmAction | UTS_OS_MODEL_00001 |
| SWR_OS_MODELS_00006 | os_xdm.py:OsApplication | UTS_OS_MODEL_00008 |
| SWR_OS_MODELS_00007 | os_xdm.py:OsResource | UTS_OS_MODEL_00009 |
| SWR_OS_MODELS_00008 | os_xdm.py:OsHooks | UTS_OS_MODEL_00010 |
| SWR_OS_MODELS_00009 | os_xdm.py:OsScheduleTable | UTS_OS_MODEL_00004 |
| SWR_OS_MODELS_00010 | os_xdm.py:OsEvent | UTS_OS_MODEL_00007 |
| SWR_OS_MODELS_00011 | os_xdm.py:OsSpinlock | UTS_OS_MODEL_00006 |
| SWR_OS_MODELS_00012 | os_xdm.py:Os | UTS_OS_MODEL_00000 |
