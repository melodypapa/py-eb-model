# Software Requirements: Os Module - Model Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | Os Module Model Layer Requirements |
| Document ID | SWR_OS_MODELS_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | Os (Operating System) - Model Layer |

---

## Overview

The Os Model Layer provides Python classes representing AUTOSAR OS configuration entities extracted from EB Tresos XDM files.

**Implementation:** `src/eb_model/models/core/os_xdm.py`

---

## Requirements

### SWR_OS_MODELS_00001 - OsAlarm Model

The system shall provide an `OsAlarm` model class for alarm configuration.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsAlarmAccessingApplication | List[EcucRefType] | List of application references | AUTOSAR |
| OsAlarmCounterRef | EcucRefType | Associated counter reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarm`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00002 - OsAppMode Model

The system shall provide an `OsAppMode` model class for application mode configuration.

**Implementation:** `os_xdm.py:OsAppMode`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00003 - OsApplication Model

The system shall provide an `OsApplication` model class for OS application boundaries.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsAppResourceRef | List[EcucRefType] | List of resource references | EB |
| OsTrustedApplicationWithProtection | bool | Trusted application with protection flag | AUTOSAR |
| OsTrustedApplicationDelayTimingViolationCall | bool | Delay timing violation call flag | AUTOSAR |
| OsTrusted | bool | Trusted application flag | AUTOSAR |
| OsApplicationCoreRef | EcucRefType | Core reference | AUTOSAR |
| OsAppAlarmRef | List[EcucRefType] | List of alarm references | AUTOSAR |
| OsAppCounterRef | List[EcucRefType] | List of counter references | AUTOSAR |
| OsAppIsrRef | List[EcucRefType] | List of ISR references | AUTOSAR |
| OsAppScheduleTableRef | List[EcucRefType] | List of schedule table references | AUTOSAR |
| OsAppTaskRef | List[EcucRefType] | List of task references | AUTOSAR |

**Implementation:** `os_xdm.py:OsApplication`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00004 - OsCounter Model

The system shall provide an `OsCounter` model class for time measurement counters.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsCounterMaxAllowedValue | int | Maximum allowed value (1-4294967295) | AUTOSAR |
| OsCounterMinCycle | int | Minimum cycle ticks | AUTOSAR |
| OsCounterTicksPerBase | int | Ticks per base unit (1-4294967295) | AUTOSAR |
| OsCounterType | OsCounterType | Counter type (HARDWARE/SOFTWARE) | AUTOSAR |
| OsCounterWindowsTimer | OsCounterWindowsTimer | Windows timer selection (TIMER0/TIMER1/TIMER2/TIMER3/TSIM_00/TSIM_01/TSIM_10/TSIM_11) | EB |
| OsCounterAccessingApplication | List[EcucRefType] | List of application references | AUTOSAR |
| OsWindowsIrqLevel | int | Interrupt request level (1-32) | EB |

**Implementation:** `os_xdm.py:OsCounter`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00005 - OsEvent Model

The system shall provide an `OsEvent` model class for event masks.

**Implementation:** `os_xdm.py:OsEvent`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00006 - OsSpinlock Model

The system shall provide an `OsSpinlock` model class for multi-core synchronization.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsSpinlockAccessingApplication | List[EcucRefType] | List of application references | AUTOSAR |
| OsSpinlockSuccessor | EcucRefType | Next spinlock reference | AUTOSAR |
| OsSpinlockLockMethod | OsSpinlockLockMethod | Lock method (LOCK_NOTHING/LOCK_ALL_INTERRUPTS/LOCK_CAT2_INTERRUPTS/LOCK_WITH_RES_SCHEDULER) | AUTOSAR |

**Implementation:** `os_xdm.py:OsSpinlock`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00007 - OsIsr Model

The system shall provide an `OsIsr` model class for Interrupt Service Routines.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsIsrCategory | OsIsrCategory | ISR category (CATEGORY_1/CATEGORY_2) | AUTOSAR |
| OsIsrResourceRef | List[EcucRefType] | List of resource references | AUTOSAR |
| OsWindowsVector | OsIsrOsWindowsVector | Interrupt vector selection | EB |
| OsIsrAccessingApplication | List[EcucRefType] | List of application references | EB |
| OsWindowsIrqLevel | int | Interrupt request level (0-31) | EB |
| OsStacksize | int | Stack size in bytes (0-2000000000) | EB |

**Implementation:** `os_xdm.py:OsIsr`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00008 - OsTask Model

The system shall provide an `OsTask` model class for OS task configuration.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsTaskActivation | int | Maximum activations (1-255) | AUTOSAR |
| OsTaskPriority | int | Relative task priority (0-2147483647) | AUTOSAR |
| OsTaskAccessingApplication | List[EcucRefType] | List of application references | AUTOSAR |
| OsTaskEventRef | List[EcucRefType] | List of event references | AUTOSAR |
| OsTaskResourceRef | List[EcucRefType] | List of resource references | AUTOSAR |
| OsStacksize | int | Stack size in bytes (0-2000000000) | EB |
| OsTaskSchedule | OsTaskSchedule | Schedule type (FULL/NON) | AUTOSAR |

**Implementation:** `os_xdm.py:OsTask`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00009 - OsPeripheralArea Model

The system shall provide an `OsPeripheralArea` model class for peripheral memory area configuration.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsPeripheralAreaEndAddress | int | End address (0-9223372036854775807) | AUTOSAR |
| OsPeripheralAreaId | int | Peripheral area identifier (0-9223372036854775807) | AUTOSAR |
| OsPeripheralAreaStartAddress | int | Start address (0-9223372036854775807) | AUTOSAR |
| OsPeripheralAreaAccessingApplication | EcucRefType | Application reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsPeripheralArea`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00010 - OsResource Model

The system shall provide an `OsResource` model class for resource management.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsResourceProperty | OsResourceProperty | Resource property (INTERNAL/LINKED/STANDARD) | AUTOSAR |
| OsResourceAccessingApplication | List[EcucRefType] | List of application references | AUTOSAR |

**Implementation:** `os_xdm.py:OsResource`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00011 - OsScheduleTable Model

The system shall provide an `OsScheduleTable` model class for cyclic scheduling.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| OsScheduleTableDuration | int | Table duration in ticks | AUTOSAR |
| OsScheduleTableRepeating | bool | Periodic table flag | AUTOSAR |
| OsSchTblAccessingApplication | List[EcucRefType] | List of application references | AUTOSAR |
| OsScheduleTableCounterRef | EcucRefType | Associated counter reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTable`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

### SWR_OS_MODELS_00012 - Os Model (Root)

The system shall provide an `Os` root model class containing all os entities.

**Methods:**
- `getOsAlarmList()` - Get all osalarm
- `getOsAppModeList()` - Get all osappmode
- `getOsApplicationList()` - Get all osapplication
- `getOsCounterList()` - Get all oscounter
- `getOsEventList()` - Get all osevent
- `getOsSpinlockList()` - Get all osspinlock
- `getOsIsrList()` - Get all osisr
- `getOsTaskList()` - Get all ostask
- `getOsPeripheralAreaList()` - Get all osperipheralarea
- `getOsResourceList()` - Get all osresource
- `getOsScheduleTableList()` - Get all osscheduletable

**Implementation:** `os_xdm.py:Os`
**Status:** Implemented
**Last Validated:** 2026-05-27

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_OS_MODELS_00001 | os_xdm.py:OsAlarm | UTS_OS_MODEL_00001 |
| SWR_OS_MODELS_00002 | os_xdm.py:OsAppMode | UTS_OS_MODEL_00002 |
| SWR_OS_MODELS_00003 | os_xdm.py:OsApplication | UTS_OS_MODEL_00003 |
| SWR_OS_MODELS_00004 | os_xdm.py:OsCounter | UTS_OS_MODEL_00004 |
| SWR_OS_MODELS_00005 | os_xdm.py:OsEvent | UTS_OS_MODEL_00005 |
| SWR_OS_MODELS_00006 | os_xdm.py:OsSpinlock | UTS_OS_MODEL_00006 |
| SWR_OS_MODELS_00007 | os_xdm.py:OsIsr | UTS_OS_MODEL_00007 |
| SWR_OS_MODELS_00008 | os_xdm.py:OsTask | UTS_OS_MODEL_00008 |
| SWR_OS_MODELS_00009 | os_xdm.py:OsPeripheralArea | UTS_OS_MODEL_00009 |
| SWR_OS_MODELS_00010 | os_xdm.py:OsResource | UTS_OS_MODEL_00010 |
| SWR_OS_MODELS_00011 | os_xdm.py:OsScheduleTable | UTS_OS_MODEL_00011 |
| SWR_OS_MODELS_00012 | os_xdm.py:Os | UTS_OS_MODEL_00012 |
