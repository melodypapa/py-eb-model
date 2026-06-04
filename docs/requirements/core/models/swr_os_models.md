# Software Requirements: Os - Model Layer

## Document Information

| Item | Value |
|------|-------|
| Module | Os |
| Stack | core |
| Abbreviation | OS |
| Generated From | Os.xdm |
| Generation Date | 2026-06-04 |

## Overview

This document defines the model layer requirements for the AUTOSAR OS module. These requirements specify the data model classes that represent OS configuration entities extracted from XDM files.

## Requirements

### SWR_OS_MODELS_00001 - OsAlarm Model

The system shall provide an `OsAlarm` model class for alarm configuration.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsAlarmAccessingApplication | [1..*] | List[EcucRefType] | Application access references | AUTOSAR |
| OsAlarmCounterRef | [1..1] | EcucRefType | Associated counter reference | AUTOSAR |
| OsAlarmAction | [1..1] | OsAlarmAction | Alarm action choice | AUTOSAR |
| OsAlarmAutostart | [0..1] | OsAlarmAutostart | Automatic alarm start | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarm`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00002 - OsAlarmAction Models

The system shall provide choice action model classes for alarm expiry behavior.

| Class | Purpose |
| --- | --- |
| OsAlarmActivateTask | Activate task on alarm expiry |
| OsAlarmCallback | Callback function on alarm expiry |
| OsAlarmIncrementCounter | Increment counter on alarm expiry |
| OsAlarmSetEvent | Set event on alarm expiry |

**Implementation:** `os_xdm.py:OsAlarmActivateTask`, `os_xdm.py:OsAlarmCallback`, `os_xdm.py:OsAlarmIncrementCounter`, `os_xdm.py:OsAlarmSetEvent`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00003 - OsAlarmActivateTask Model

The system shall provide an `OsAlarmActivateTask` model class for task activation action.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsAlarmActivateTaskRef | [1..1] | EcucRefType | Task to activate reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarmActivateTask`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00004 - OsAlarmCallback Model

The system shall provide an `OsAlarmCallback` model class for callback action.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsAlarmCallbackName | [1..1] | str | Callback function name | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarmCallback`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00005 - OsAlarmIncrementCounter Model

The system shall provide an `OsAlarmIncrementCounter` model class for counter increment action.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsAlarmIncrementCounterRef | [1..1] | EcucRefType | Counter to increment reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarmIncrementCounter`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00006 - OsAlarmSetEvent Model

The system shall provide an `OsAlarmSetEvent` model class for event setting action.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsAlarmSetEventRef | [1..1] | EcucRefType | Event to set reference | AUTOSAR |
| OsAlarmSetEventTaskRef | [1..1] | EcucRefType | Task for event reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarmSetEvent`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00007 - OsAlarmAutostart Model

The system shall provide an `OsAlarmAutostart` model class for automatic alarm start configuration.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsAlarmAlarmTime | [1..1] | int | First expiry time in ticks (1-4294967295) | AUTOSAR |
| OsAlarmAutostartType | [1..1] | OsAlarmAutostartType | Autostart type (ABSOLUTE/RELATIVE, default RELATIVE) | AUTOSAR |
| OsAlarmCycleTime | [1..1] | int | Cycle time in ticks (0-4294967295) | AUTOSAR |
| OsAlarmAppModeRef | [1..*] | List[EcucRefType] | Application mode references | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarmAutostart`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00008 - OsAppMode Model

The system shall provide an `OsAppMode` model class for application mode configuration.

**Note:** This entity has no configuration fields.

**Implementation:** `os_xdm.py:OsAppMode`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00009 - OsApplication Model

The system shall provide an `OsApplication` model class for OS application boundaries.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsAppResourceRef | [1..*] | List[EcucRefType] | Resource references | EB |
| OsTrustedApplicationWithProtection | [1..1] | bool | Trusted with protection flag (default false) | AUTOSAR |
| OsTrustedApplicationDelayTimingViolationCall | [1..1] | bool | Delay timing violation flag (default false) | AUTOSAR |
| OsTrusted | [1..1] | bool | Trusted application flag (default false) | AUTOSAR |
| OsApplicationCoreRef | [1..1] | EcucRefType | Core reference | AUTOSAR |
| OsAppAlarmRef | [1..*] | List[EcucRefType] | Alarm references | AUTOSAR |
| OsAppCounterRef | [1..*] | List[EcucRefType] | Counter references | AUTOSAR |
| OsAppIsrRef | [1..*] | List[EcucRefType] | ISR references | AUTOSAR |
| OsAppScheduleTableRef | [1..*] | List[EcucRefType] | Schedule table references | AUTOSAR |
| OsAppTaskRef | [1..*] | List[EcucRefType] | Task references | AUTOSAR |
| OsApplicationHooks | [1..1] | OsApplicationHooks | Hook configuration | AUTOSAR |
| OsApplicationTrustedFunction | [1..*] | List[OsApplicationTrustedFunction] | Trusted function definitions | AUTOSAR |

**Implementation:** `os_xdm.py:OsApplication`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00010 - OsApplicationHooks Model

The system shall provide an `OsApplicationHooks` model class for application hook configuration.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsAppStartupHook | [0..1] | str | Startup hook function name | AUTOSAR |
| OsAppShutdownHook | [0..1] | str | Shutdown hook function name | AUTOSAR |
| OsAppErrorHook | [0..1] | str | Error hook function name | AUTOSAR |

**Implementation:** `os_xdm.py:OsApplicationHooks`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00011 - OsApplicationTrustedFunction Model

The system shall provide an `OsApplicationTrustedFunction` model class for trusted function definition.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsTrustedFunctionName | [1..1] | str | Trusted function name | AUTOSAR |

**Implementation:** `os_xdm.py:OsApplicationTrustedFunction`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00012 - OsCounter Model

The system shall provide an `OsCounter` model class for time measurement counters.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsCounterMaxAllowedValue | [1..1] | int | Maximum counter value (1-4294967295) | AUTOSAR |
| OsCounterMinCycle | [1..1] | int | Minimum cycle ticks | AUTOSAR |
| OsCounterTicksPerBase | [1..1] | int | Ticks per base unit (1-4294967295) | AUTOSAR |
| OsCounterType | [1..1] | OsCounterType | Counter type (HARDWARE/SOFTWARE) | AUTOSAR |
| OsCounterWindowsTimer | [1..1] | OsCounterWindowsTimer | Windows timer (TIMER0-3/TSIM_00-11) | EB |
| OsCounterAccessingApplication | [1..*] | List[EcucRefType] | Application access references | AUTOSAR |
| OsWindowsIrqLevel | [1..1] | int | IRQ level (1-32) | EB |
| OsTimeConstant | [1..*] | List[OsTimeConstant] | Time constants | AUTOSAR |
| OsDriver | [0..1] | OsDriver | Counter driver configuration | AUTOSAR |

**Implementation:** `os_xdm.py:OsCounter`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00013 - OsTimeConstant Model

The system shall provide an `OsTimeConstant` model class for named time constants.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsTimeValue | [1..1] | float | Time constant value (0.0-86400.0) | AUTOSAR |
| OsConstName | [1..1] | str | Constant access name | EB |

**Implementation:** `os_xdm.py:OsTimeConstant`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00014 - OsDriver Model

The system shall provide an `OsDriver` model class for counter driver configuration.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsHwIncrementer | [1..*] | List[OsHwIncrementer] | Hardware incrementers | EB |

**Implementation:** `os_xdm.py:OsDriver`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00015 - OsHwIncrementer Model

The system shall provide an `OsHwIncrementer` model class for hardware incrementer configuration.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsHwIncrementerSystemTime | [1..1] | int | System time value | EB |

**Implementation:** `os_xdm.py:OsHwIncrementer`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00016 - OsEvent Model

The system shall provide an `OsEvent` model class for event configuration.

**Note:** This entity has no configuration fields.

**Implementation:** `os_xdm.py:OsEvent`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00017 - OsSpinlock Model

The system shall provide an `OsSpinlock` model class for spinlock synchronization.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsSpinlockAccessingApplication | [1..*] | List[EcucRefType] | Application access references | AUTOSAR |
| OsSpinlockSuccessor | [1..1] | EcucRefType | Successor spinlock reference | AUTOSAR |
| OsSpinlockLockMethod | [1..1] | OsSpinlockLockMethod | Lock method type | AUTOSAR |

**Implementation:** `os_xdm.py:OsSpinlock`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00018 - OsIsr Model

The system shall provide an `OsIsr` model class for interrupt service routine configuration.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsIsrCategory | [1..1] | OsIsrCategory | ISR category type | AUTOSAR |
| OsIsrResourceRef | [1..*] | List[EcucRefType] | Resource references | AUTOSAR |
| OsWindowsVector | [1..1] | OsIsrOsWindowsVector | Windows vector | EB |
| OsIsrAccessingApplication | [1..*] | List[EcucRefType] | Application access references | EB |
| OsWindowsIrqLevel | [1..1] | int | IRQ level (1-32) | EB |
| OsStacksize | [1..1] | int | Stack size in bytes | EB |
| OsIsrTimingProtection | [0..1] | OsIsrTimingProtection | Timing protection configuration | AUTOSAR |

**Implementation:** `os_xdm.py:OsIsr`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00019 - OsIsrTimingProtection Model

The system shall provide an `OsIsrTimingProtection` model class for ISR timing protection.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsIsrResourceLock | [1..*] | List[OsIsrResourceLock] | Resource lock budgets | AUTOSAR |

**Implementation:** `os_xdm.py:OsIsrTimingProtection`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00020 - OsIsrResourceLock Model

The system shall provide an `OsIsrResourceLock` model class for ISR resource lock timing.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsIsrResourceLockBudget | [1..1] | float | Lock duration budget (0.0-86400.0) | AUTOSAR |
| OsIsrResourceLockResourceRef | [1..1] | EcucRefType | Locked resource reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsIsrResourceLock`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00021 - OsTask Model

The system shall provide an `OsTask` model class for OS task configuration.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsTaskActivation | [1..1] | int | Maximum activations (1-255) | AUTOSAR |
| OsTaskPriority | [1..1] | int | Task priority (0-2147483647) | AUTOSAR |
| OsTaskAccessingApplication | [1..*] | List[EcucRefType] | Application access references | AUTOSAR |
| OsTaskEventRef | [1..*] | List[EcucRefType] | Event references | AUTOSAR |
| OsTaskResourceRef | [1..*] | List[EcucRefType] | Resource references | AUTOSAR |
| OsStacksize | [1..1] | int | Stack size in bytes (0-2000000000) | EB |
| OsTaskSchedule | [1..1] | OsTaskSchedule | Schedule type (FULL/NON, default FULL) | AUTOSAR |
| OsTaskAutostart | [0..1] | OsTaskAutostart | Automatic task start | AUTOSAR |
| OsTaskTimingProtection | [0..1] | OsTaskTimingProtection | Timing protection configuration | AUTOSAR |

**Implementation:** `os_xdm.py:OsTask`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00022 - OsTaskAutostart Model

The system shall provide an `OsTaskAutostart` model class for automatic task start configuration.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsTaskAppModeRef | [1..*] | List[EcucRefType] | Application mode references | AUTOSAR |

**Implementation:** `os_xdm.py:OsTaskAutostart`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00023 - OsTaskTimingProtection Model

The system shall provide an `OsTaskTimingProtection` model class for task timing protection.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsTaskResourceLock | [1..*] | List[OsTaskResourceLock] | Resource lock budgets | AUTOSAR |

**Implementation:** `os_xdm.py:OsTaskTimingProtection`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00024 - OsTaskResourceLock Model

The system shall provide an `OsTaskResourceLock` model class for task resource lock timing.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsTaskResourceLockBudget | [1..1] | float | Lock duration budget (0.0-86400.0) | AUTOSAR |
| OsTaskResourceLockResourceRef | [1..1] | EcucRefType | Locked resource reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsTaskResourceLock`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00025 - OsPeripheralArea Model

The system shall provide an `OsPeripheralArea` model class for peripheral memory area configuration.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsPeripheralAreaEndAddress | [1..1] | int | End address (0-9223372036854775807) | AUTOSAR |
| OsPeripheralAreaId | [1..1] | int | Peripheral area identifier (0-9223372036854775807) | AUTOSAR |
| OsPeripheralAreaStartAddress | [1..1] | int | Start address (0-9223372036854775807) | AUTOSAR |
| OsPeripheralAreaAccessingApplication | [1..1] | EcucRefType | Application access reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsPeripheralArea`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00026 - OsResource Model

The system shall provide an `OsResource` model class for resource management.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsResourceProperty | [1..1] | OsResourceProperty | Resource property type | AUTOSAR |
| OsResourceAccessingApplication | [1..*] | List[EcucRefType] | Application access references | AUTOSAR |

**Implementation:** `os_xdm.py:OsResource`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00027 - OsScheduleTable Model

The system shall provide an `OsScheduleTable` model class for schedule table configuration.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsScheduleTableDuration | [1..1] | int | Table duration in ticks | AUTOSAR |
| OsScheduleTableRepeating | [1..1] | bool | Repeating table flag | AUTOSAR |
| OsSchTblAccessingApplication | [1..*] | List[EcucRefType] | Application access references | AUTOSAR |
| OsScheduleTableCounterRef | [1..1] | EcucRefType | Counter reference | AUTOSAR |
| OsScheduleTableAutostart | [0..1] | OsScheduleTableAutostart | Automatic table start | AUTOSAR |
| OsScheduleTableExpiryPoint | [1..*] | List[OsScheduleTableExpiryPoint] | Expiry points | AUTOSAR |
| OsScheduleTableSync | [0..1] | OsScheduleTableSync | Synchronization configuration | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTable`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00028 - OsScheduleTableAutostart Model

The system shall provide an `OsScheduleTableAutostart` model class for automatic schedule table start.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsScheduleTableAutostartType | [1..1] | OsScheduleTableAutostartType | Autostart type (ABSOLUTE/RELATIVE/SYNCHRON, default RELATIVE) | AUTOSAR |
| OsScheduleTableAppModeRef | [1..*] | List[EcucRefType] | Application mode references | AUTOSAR |
| OsScheduleTableStartValue | [1..1] | int | Start value in ticks (0-4294967295) | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTableAutostart`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00029 - OsScheduleTableExpiryPoint Model

The system shall provide an `OsScheduleTableExpiryPoint` model class for schedule table expiry points.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsScheduleTblExpPointOffset | [1..1] | int | Expiry point offset in ticks | AUTOSAR |
| OsScheduleTableEventSetting | [1..*] | List[OsScheduleTableEventSetting] | Event setting actions | AUTOSAR |
| OsScheduleTableTaskActivation | [1..*] | List[OsScheduleTableTaskActivation] | Task activation actions | AUTOSAR |
| OsScheduleTblAdjustableExpPoint | [0..1] | OsScheduleTblAdjustableExpPoint | Adjustable expiry point | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTableExpiryPoint`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00030 - OsScheduleTableEventSetting Model

The system shall provide an `OsScheduleTableEventSetting` model class for event setting actions.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsScheduleTableSetEventRef | [1..1] | EcucRefType | Event reference | AUTOSAR |
| OsScheduleTableSetEventTaskRef | [1..1] | EcucRefType | Task reference for event | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTableEventSetting`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00031 - OsScheduleTableTaskActivation Model

The system shall provide an `OsScheduleTableTaskActivation` model class for task activation actions.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsScheduleTableActivateTaskRef | [1..1] | EcucRefType | Task to activate reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTableTaskActivation`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00032 - OsScheduleTblAdjustableExpPoint Model

The system shall provide an `OsScheduleTblAdjustableExpPoint` model class for adjustable expiry points.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsScheduleTableExpPointAdjustmentAllowed | [1..1] | bool | Adjustment allowed flag | AUTOSAR |
| OsScheduleTableExpPointAdjustmentMaxAllowed | [1..1] | int | Maximum adjustment value | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTblAdjustableExpPoint`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00033 - OsScheduleTableSync Model

The system shall provide an `OsScheduleTableSync` model class for schedule table synchronization.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| OsScheduleTableSyncStrategy | [1..1] | OsScheduleTableSyncStrategy | Synchronization strategy | AUTOSAR |
| OsScheduleTableExplicitSync | [0..1] | OsScheduleTableExplicitSync | Explicit sync configuration | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTableSync`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_MODELS_00034 - Os Model (Root)

The system shall provide an `Os` root model class for OS module configuration.

**Methods:**

- `getOsAlarmList()` — Returns list of OsAlarm entities
- `getOsAppModeList()` — Returns list of OsAppMode entities
- `getOsApplicationList()` — Returns list of OsApplication entities
- `getOsCounterList()` — Returns list of OsCounter entities
- `getOsEventList()` — Returns list of OsEvent entities
- `getOsSpinlockList()` — Returns list of OsSpinlock entities
- `getOsIsrList()` — Returns list of OsIsr entities
- `getOsTaskList()` — Returns list of OsTask entities
- `getOsPeripheralAreaList()` — Returns list of OsPeripheralArea entities
- `getOsResourceList()` — Returns list of OsResource entities
- `getOsScheduleTableList()` — Returns list of OsScheduleTable entities

**Implementation:** `os_xdm.py:Os`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

## Implementation Notes

| Requirement ID | Implementation |
| --- | --- |
| SWR_OS_MODELS_00001 | os_xdm.py:OsAlarm |
| SWR_OS_MODELS_00002 | os_xdm.py:OsAlarmActivateTask, os_xdm.py:OsAlarmCallback, os_xdm.py:OsAlarmIncrementCounter, os_xdm.py:OsAlarmSetEvent |
| SWR_OS_MODELS_00003 | os_xdm.py:OsAlarmActivateTask |
| SWR_OS_MODELS_00004 | os_xdm.py:OsAlarmCallback |
| SWR_OS_MODELS_00005 | os_xdm.py:OsAlarmIncrementCounter |
| SWR_OS_MODELS_00006 | os_xdm.py:OsAlarmSetEvent |
| SWR_OS_MODELS_00007 | os_xdm.py:OsAlarmAutostart |
| SWR_OS_MODELS_00008 | os_xdm.py:OsAppMode |
| SWR_OS_MODELS_00009 | os_xdm.py:OsApplication |
| SWR_OS_MODELS_00010 | os_xdm.py:OsApplicationHooks |
| SWR_OS_MODELS_00011 | os_xdm.py:OsApplicationTrustedFunction |
| SWR_OS_MODELS_00012 | os_xdm.py:OsCounter |
| SWR_OS_MODELS_00013 | os_xdm.py:OsTimeConstant |
| SWR_OS_MODELS_00014 | os_xdm.py:OsDriver |
| SWR_OS_MODELS_00015 | os_xdm.py:OsHwIncrementer |
| SWR_OS_MODELS_00016 | os_xdm.py:OsEvent |
| SWR_OS_MODELS_00017 | os_xdm.py:OsSpinlock |
| SWR_OS_MODELS_00018 | os_xdm.py:OsIsr |
| SWR_OS_MODELS_00019 | os_xdm.py:OsIsrTimingProtection |
| SWR_OS_MODELS_00020 | os_xdm.py:OsIsrResourceLock |
| SWR_OS_MODELS_00021 | os_xdm.py:OsTask |
| SWR_OS_MODELS_00022 | os_xdm.py:OsTaskAutostart |
| SWR_OS_MODELS_00023 | os_xdm.py:OsTaskTimingProtection |
| SWR_OS_MODELS_00024 | os_xdm.py:OsTaskResourceLock |
| SWR_OS_MODELS_00025 | os_xdm.py:OsPeripheralArea |
| SWR_OS_MODELS_00026 | os_xdm.py:OsResource |
| SWR_OS_MODELS_00027 | os_xdm.py:OsScheduleTable |
| SWR_OS_MODELS_00028 | os_xdm.py:OsScheduleTableAutostart |
| SWR_OS_MODELS_00029 | os_xdm.py:OsScheduleTableExpiryPoint |
| SWR_OS_MODELS_00030 | os_xdm.py:OsScheduleTableEventSetting |
| SWR_OS_MODELS_00031 | os_xdm.py:OsScheduleTableTaskActivation |
| SWR_OS_MODELS_00032 | os_xdm.py:OsScheduleTblAdjustableExpPoint |
| SWR_OS_MODELS_00033 | os_xdm.py:OsScheduleTableSync |
| SWR_OS_MODELS_00034 | os_xdm.py:Os |