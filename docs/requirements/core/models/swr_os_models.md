# Software Requirements: Os Module - Model Layer

## Document Information

| Field          | Value                               |
| -------------- | ----------------------------------- |
| Document Title | Os Module Model Layer Requirements  |
| Document ID    | SWR_OS_MODELS_00001                 |
| Version        | 1.0                                 |
| Date           | 2026-05-31                          |
| Project        | py-eb-model                         |
| Module         | Os (Operating System) - Model Layer |

---

## Overview

The Os Model Layer provides Python classes representing AUTOSAR OS configuration entities extracted from EB Tresos XDM files.

**Implementation:** `src/eb_model/models/core/os_xdm.py`

---

## Requirements

### SWR_OS_MODELS_00001 - OsAlarm Model

The system shall provide an `OsAlarm` model class for alarm configuration.

| Field                                | Type              | Description                         | Origin  |
| ------------------------------------ | ----------------- | ----------------------------------- | ------- |
| OsAlarmAccessingApplication [1..*]   | List[EcucRefType] | List of application references      | AUTOSAR |
| OsAlarmCounterRef [1..1]            | EcucRefType       | Associated counter reference        | AUTOSAR |
| OsAlarmAction                        | OsAlarmAction     | Alarm action choice                 | AUTOSAR |
| OsAlarmAutostart [0..1]              | OsAlarmAutostart  | Automatic alarm start configuration | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarm`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00013 - OsAlarmAction Models

The system shall provide choice action model classes.

| Class                   | Purpose                           |
| ----------------------- | --------------------------------- |
| OsAlarmActivateTask     | Activate task on alarm expiry     |
| OsAlarmCallback         | Callback function on alarm expiry |
| OsAlarmIncrementCounter | Increment counter on alarm expiry |
| OsAlarmSetEvent         | Set event on alarm expiry         |

**Implementation:** `os_xdm.py:OsAlarmActivateTask`, `os_xdm.py:OsAlarmCallback`, `os_xdm.py:OsAlarmIncrementCounter`, `os_xdm.py:OsAlarmSetEvent`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00014 - OsAlarmActivateTask Model

The system shall provide an `OsAlarmActivateTask` model class for task activation alarm action.

| Field                         | Type        | Description               | Origin  |
| ----------------------------- | ----------- | ------------------------- | ------- |
| OsAlarmActivateTaskRef [1..1] | EcucRefType | Task activation reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarmActivateTask`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00015 - OsAlarmCallback Model

The system shall provide an `OsAlarmCallback` model class for callback alarm action.

| Field                | Type | Description            | Origin  |
| -------------------- | ---- | ---------------------- | ------- |
| OsAlarmCallbackName  | str  | Callback function name | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarmCallback`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00016 - OsAlarmIncrementCounter Model

The system shall provide an `OsAlarmIncrementCounter` model class for counter increment alarm action.

| Field                           | Type        | Description                 | Origin  |
| ------------------------------- | ----------- | --------------------------- | ------- |
| OsAlarmIncrementCounterRef [1..1] | EcucRefType | Counter increment reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarmIncrementCounter`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00017 - OsAlarmSetEvent Model

The system shall provide an `OsAlarmSetEvent` model class for event setting alarm action.

| Field                        | Type        | Description              | Origin  |
| ---------------------------- | ----------- | ------------------------ | ------- |
| OsAlarmSetEventRef [1..1]    | EcucRefType | Event reference          | AUTOSAR |
| OsAlarmSetEventTaskRef [1..1] | EcucRefType | Task reference for event | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarmSetEvent`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00018 - OsAlarmAutostart Model

The system shall provide an `OsAlarmAutostart` model class for automatic alarm start configuration.

| Field                         | Type                 | Description                                          | Origin  |
| ----------------------------- | -------------------- | ---------------------------------------------------- | ------- |
| OsAlarmAlarmTime [1..1]       | int                  | Alarm expiry tick value (1-4294967295)               | AUTOSAR |
| OsAlarmAutostartType [1..1]   | OsAlarmAutostartType | Autostart type (ABSOLUTE/RELATIVE, default RELATIVE) | AUTOSAR |
| OsAlarmCycleTime [1..1]       | int                  | Cycle time in ticks (0-4294967295)                   | AUTOSAR |
| OsAlarmAppModeRef [1..*]      | List[EcucRefType]    | List of application mode references                  | AUTOSAR |

**Implementation:** `os_xdm.py:OsAlarmAutostart`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00002 - OsAppMode Model

The system shall provide an `OsAppMode` model class for application mode configuration.

**Implementation:** `os_xdm.py:OsAppMode`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00003 - OsApplication Model

The system shall provide an `OsApplication` model class for OS application boundaries.

| Field                                                   | Type                               | Description                                              | Origin  |
| ------------------------------------------------------- | ---------------------------------- | -------------------------------------------------------- | ------- |
| OsAppResourceRef [1..*]                                 | List[EcucRefType]                  | List of resource references                              | EB      |
| OsTrustedApplicationWithProtection [1..1]               | bool                               | Trusted application with protection flag (default false) | AUTOSAR |
| OsTrustedApplicationDelayTimingViolationCall [1..1]     | bool                               | Delay timing violation call flag (default false)         | AUTOSAR |
| OsTrusted [1..1]                                        | bool                               | Trusted application flag (default false)                 | AUTOSAR |
| OsApplicationCoreRef [1..1]                             | EcucRefType                        | Core reference                                           | AUTOSAR |
| OsAppAlarmRef [1..*]                                    | List[EcucRefType]                  | List of alarm references                                 | AUTOSAR |
| OsAppCounterRef [1..*]                                  | List[EcucRefType]                  | List of counter references                               | AUTOSAR |
| OsAppIsrRef [1..*]                                      | List[EcucRefType]                  | List of ISR references                                   | AUTOSAR |
| OsAppScheduleTableRef [1..*]                            | List[EcucRefType]                  | List of schedule table references                        | AUTOSAR |
| OsAppTaskRef [1..*]                                     | List[EcucRefType]                  | List of task references                                  | AUTOSAR |
| OsApplicationHooks [1..1]                               | OsApplicationHooks                 | Application hook configuration                           | AUTOSAR |
| OsApplicationTrustedFunction [1..*]                     | List[OsApplicationTrustedFunction] | Trusted function definitions                             | AUTOSAR |

**Implementation:** `os_xdm.py:OsApplication`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00019 - OsApplicationHooks Model

The system shall provide an `OsApplicationHooks` model class for application hook configuration.

| Field                     | Type | Description                                | Origin  |
| ------------------------- | ---- | ------------------------------------------ | ------- |
| OsAppErrorHook [1..1]     | bool | Application error hook (default false)     | AUTOSAR |
| OsAppShutdownHook [1..1]  | bool | Application shutdown hook (default false)  | AUTOSAR |
| OsAppStartupHook [1..1]   | bool | Application startup hook (default false)   | AUTOSAR |

**Implementation:** `os_xdm.py:OsApplicationHooks`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00020 - OsApplicationTrustedFunction Model

The system shall provide an `OsApplicationTrustedFunction` model class for trusted function definitions.

| Field                      | Type | Description             | Origin  |
| -------------------------- | ---- | ----------------------- | ------- |
| OsTrustedFunctionName [1..1] | str  | Trusted function identifier | AUTOSAR |

**Implementation:** `os_xdm.py:OsApplicationTrustedFunction`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00004 - OsCounter Model

The system shall provide an `OsCounter` model class for time measurement counters.

| Field                                  | Type                 | Description                                                                           | Origin  |
| -------------------------------------- | -------------------- | ------------------------------------------------------------------------------------- | ------- |
| OsCounterMaxAllowedValue [1..1]        | int                  | Maximum allowed value (1-4294967295)                                                  | AUTOSAR |
| OsCounterMinCycle [1..1]               | int                  | Minimum cycle ticks                                                                   | AUTOSAR |
| OsCounterTicksPerBase [1..1]           | int                  | Ticks per base unit (1-4294967295)                                                    | AUTOSAR |
| OsCounterType [1..1]                   | OsCounterType        | Counter type (HARDWARE/SOFTWARE)                                                      | AUTOSAR |
| OsCounterWindowsTimer [1..1]           | OsCounterWindowsTimer | Windows timer selection (TIMER0/TIMER1/TIMER2/TIMER3/TSIM_00/TSIM_01/TSIM_10/TSIM_11) | EB      |
| OsCounterAccessingApplication [1..*]   | List[EcucRefType]    | List of application references                                                        | AUTOSAR |
| OsWindowsIrqLevel [1..1]               | int                  | Interrupt request level (1-32)                                                        | EB      |
| OsTimeConstant [1..*]                  | List[OsTimeConstant] | Named time constants                                                                  | AUTOSAR |
| OsDriver [0..1]                        | OsDriver             | Counter driver configuration                                                          | AUTOSAR |

**Implementation:** `os_xdm.py:OsCounter`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00021 - OsTimeConstant Model

The system shall provide an `OsTimeConstant` model class for named time constants.

| Field               | Type  | Description                    | Origin  |
| ------------------- | ----- | ------------------------------ | ------- |
| OsTimeValue [1..1]  | float | Time constant value (0.0-86400.0) | AUTOSAR |
| OsConstName [1..1]  | str   | Constant access name           | EB      |

**Implementation:** `os_xdm.py:OsTimeConstant`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00022 - OsDriver Model

The system shall provide an `OsDriver` model class for counter driver configuration.

| Field                     | Type             | Description                       | Origin |
| ------------------------- | ---------------- | --------------------------------- | ------ |
| OsHwIncrementer [0..1]    | OsHwIncrementer  | Hardware incrementer configuration | EB     |

**Implementation:** `os_xdm.py:OsDriver`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00023 - OsHwIncrementer Model

The system shall provide an `OsHwIncrementer` model class for hardware counter incrementer configuration.

| Field                      | Type                          | Description                | Origin |
| -------------------------- | ----------------------------- | -------------------------- | ------ |
| OsHwModule [1..1]          | OsHwIncrementerOsHwModule     | Hardware module selection  | EB     |
| OsIncrementerIrqLevel [1..1] | int                         | Incrementer IRQ level (1)  | EB     |

**Implementation:** `os_xdm.py:OsHwIncrementer`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00005 - OsEvent Model

The system shall provide an `OsEvent` model class for event masks.

**Implementation:** `os_xdm.py:OsEvent`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00006 - OsSpinlock Model

The system shall provide an `OsSpinlock` model class for multi-core synchronization.

| Field                                   | Type                | Description                                                                                                        | Origin  |
| --------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------ | ------- |
| OsSpinlockAccessingApplication [1..*]   | List[EcucRefType]   | List of application references                                                                                     | AUTOSAR |
| OsSpinlockSuccessor [1..1]              | EcucRefType         | Next spinlock reference                                                                                            | AUTOSAR |
| OsSpinlockLockMethod [1..1]             | OsSpinlockLockMethod | Lock method (LOCK_NOTHING/LOCK_ALL_INTERRUPTS/LOCK_CAT2_INTERRUPTS/LOCK_WITH_RES_SCHEDULER, default LOCK_NOTHING) | AUTOSAR |

**Implementation:** `os_xdm.py:OsSpinlock`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00007 - OsIsr Model

The system shall provide an `OsIsr` model class for Interrupt Service Routines.

| Field                              | Type                  | Description                                               | Origin  |
| ---------------------------------- | --------------------- | --------------------------------------------------------- | ------- |
| OsIsrCategory [1..1]               | OsIsrCategory         | ISR category (CATEGORY_1/CATEGORY_2)                      | AUTOSAR |
| OsIsrResourceRef [1..*]            | List[EcucRefType]     | List of resource references                               | AUTOSAR |
| OsWindowsVector [1..1]             | OsIsrOsWindowsVector  | Interrupt vector selection                                | EB      |
| OsIsrAccessingApplication [1..*]   | List[EcucRefType]     | List of application references                            | EB      |
| OsWindowsIrqLevel [1..1]           | int                   | Interrupt request level (0-31)                            | EB      |
| OsStacksize [1..1]                 | int                   | Stack size in bytes (0-2000000000)                        | EB      |
| OsIsrTimingProtection [0..1]       | OsIsrTimingProtection | ISR timing protection                                     | AUTOSAR |

**Implementation:** `os_xdm.py:OsIsr`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00024 - OsIsrTimingProtection Model

The system shall provide an `OsIsrTimingProtection` model class for ISR timing protection configuration.

| Field                       | Type                    | Description               | Origin  |
| --------------------------- | ----------------------- | ------------------------- | ------- |
| OsIsrResourceLock [1..*]    | List[OsIsrResourceLock] | ISR resource lock budgets | AUTOSAR |

**Implementation:** `os_xdm.py:OsIsrTimingProtection`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00025 - OsIsrResourceLock Model

The system shall provide an `OsIsrResourceLock` model class for ISR resource lock timing budgets.

| Field                              | Type        | Description                            | Origin  |
| ---------------------------------- | ----------- | -------------------------------------- | ------- |
| OsIsrResourceLockBudget [1..1]     | float       | Resource lock duration (0.0-86400.0)   | AUTOSAR |
| OsIsrResourceLockResourceRef [1..1] | EcucRefType | Locked resource reference              | AUTOSAR |

**Implementation:** `os_xdm.py:OsIsrResourceLock`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00008 - OsTask Model

The system shall provide an `OsTask` model class for OS task configuration.

| Field                             | Type               | Description                                           | Origin  |
| --------------------------------- | ------------------ | ----------------------------------------------------- | ------- |
| OsTaskActivation [1..1]           | int                | Maximum activations (1-255)                           | AUTOSAR |
| OsTaskPriority [1..1]            | int                | Relative task priority (0-2147483647)                 | AUTOSAR |
| OsTaskAccessingApplication [1..*] | List[EcucRefType]  | List of application references                        | AUTOSAR |
| OsTaskEventRef [1..*]            | List[EcucRefType]  | List of event references                              | AUTOSAR |
| OsTaskResourceRef [1..*]         | List[EcucRefType]  | List of resource references                           | AUTOSAR |
| OsStacksize [1..1]               | int                | Stack size in bytes (0-2000000000)                    | EB      |
| OsTaskSchedule [1..1]            | OsTaskSchedule     | Schedule type (FULL/NON, default FULL)               | AUTOSAR |
| OsTaskAutostart [0..1]           | OsTaskAutostart    | Automatic task start configuration                    | AUTOSAR |
| OsTaskTimingProtection [0..1]    | OsTaskTimingProtection | Task timing protection                            | AUTOSAR |

**Implementation:** `os_xdm.py:OsTask`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00026 - OsTaskAutostart Model

The system shall provide an `OsTaskAutostart` model class for automatic task start configuration.

| Field                     | Type              | Description                          | Origin  |
| ------------------------- | ----------------- | ------------------------------------ | ------- |
| OsTaskAppModeRef [1..*]   | List[EcucRefType] | List of application mode references  | AUTOSAR |

**Implementation:** `os_xdm.py:OsTaskAutostart`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00027 - OsTaskTimingProtection Model

The system shall provide an `OsTaskTimingProtection` model class for task timing protection configuration.

| Field                      | Type                     | Description                | Origin  |
| -------------------------- | ------------------------ | -------------------------- | ------- |
| OsTaskResourceLock [1..*]  | List[OsTaskResourceLock] | Task resource lock budgets | AUTOSAR |

**Implementation:** `os_xdm.py:OsTaskTimingProtection`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00028 - OsTaskResourceLock Model

The system shall provide an `OsTaskResourceLock` model class for task resource lock timing budgets.

| Field                               | Type        | Description                          | Origin  |
| ----------------------------------- | ----------- | ------------------------------------ | ------- |
| OsTaskResourceLockBudget [1..1]     | float       | Resource lock duration (0.0-86400.0) | AUTOSAR |
| OsTaskResourceLockResourceRef [1..1] | EcucRefType | Locked resource reference            | AUTOSAR |

**Implementation:** `os_xdm.py:OsTaskResourceLock`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00009 - OsPeripheralArea Model

The system shall provide an `OsPeripheralArea` model class for peripheral memory area configuration.

| Field                                     | Type        | Description                             | Origin  |
| ----------------------------------------- | ----------- | --------------------------------------- | ------- |
| OsPeripheralAreaEndAddress [1..1]         | int         | End address (0-9223372036854775807)     | AUTOSAR |
| OsPeripheralAreaId [1..1]                 | int         | Peripheral area identifier (0-9223372036854775807) | AUTOSAR |
| OsPeripheralAreaStartAddress [1..1]       | int         | Start address (0-9223372036854775807)   | AUTOSAR |
| OsPeripheralAreaAccessingApplication [1..1] | EcucRefType | Application reference                 | AUTOSAR |

**Implementation:** `os_xdm.py:OsPeripheralArea`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00010 - OsResource Model

The system shall provide an `OsResource` model class for resource management.

| Field                                   | Type                | Description                                                       | Origin  |
| --------------------------------------- | ------------------- | ----------------------------------------------------------------- | ------- |
| OsResourceProperty [1..1]               | OsResourceProperty  | Resource property (INTERNAL/LINKED/STANDARD, default STANDARD)    | AUTOSAR |
| OsResourceAccessingApplication [1..*]   | List[EcucRefType]   | List of application references                                    | AUTOSAR |

**Implementation:** `os_xdm.py:OsResource`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00011 - OsScheduleTable Model

The system shall provide an `OsScheduleTable` model class for cyclic scheduling.

| Field                                    | Type                       | Description                                        | Origin  |
| ---------------------------------------- | -------------------------- | -------------------------------------------------- | ------- |
| OsScheduleTableDuration [1..1]           | int                        | Table duration in ticks                            | AUTOSAR |
| OsScheduleTableRepeating [1..1]          | bool                       | Periodic table flag (default false)                | AUTOSAR |
| OsSchTblAccessingApplication [1..*]      | List[EcucRefType]          | List of application references                     | AUTOSAR |
| OsScheduleTableCounterRef [1..1]         | EcucRefType                | Associated counter reference                       | AUTOSAR |
| OsScheduleTableAutostart [0..1]          | OsScheduleTableAutostart   | Automatic schedule table start                     | AUTOSAR |
| OsScheduleTableExpiryPoint [1..*]        | List[OsScheduleTableExpiryPoint] | Schedule table expiry points              | AUTOSAR |
| OsScheduleTableSync [0..1]               | OsScheduleTableSync        | Schedule table synchronization                     | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTable`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00029 - OsScheduleTableAutostart Model

The system shall provide an `OsScheduleTableAutostart` model class for automatic schedule table start configuration.

| Field                                    | Type                         | Description                                                     | Origin  |
| ---------------------------------------- | ---------------------------- | --------------------------------------------------------------- | ------- |
| OsScheduleTableAutostartType [1..1]      | OsScheduleTableAutostartType | Autostart type (ABSOLUTE/RELATIVE/SYNCHRON, default RELATIVE)   | AUTOSAR |
| OsScheduleTableAppModeRef [1..*]         | List[EcucRefType]            | List of application mode references                             | AUTOSAR |
| OsScheduleTableStartValue [1..1]         | int                          | Start value in ticks (0-4294967295)                             | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTableAutostart`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00030 - OsScheduleTableExpiryPoint Model

The system shall provide an `OsScheduleTableExpiryPoint` model class for schedule table expiry point configuration.

| Field                                  | Type                             | Description                  | Origin  |
| -------------------------------------- | -------------------------------- | ---------------------------- | ------- |
| OsScheduleTblExpPointOffset [1..1]     | int                              | Expiry point offset in ticks | AUTOSAR |
| OsScheduleTableEventSetting [1..*]     | List[OsScheduleTableEventSetting] | Event setting actions       | AUTOSAR |
| OsScheduleTableTaskActivation [1..*]   | List[OsScheduleTableTaskActivation] | Task activation actions  | AUTOSAR |
| OsScheduleTblAdjustableExpPoint [0..1] | OsScheduleTblAdjustableExpPoint | Adjustable expiry point      | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTableExpiryPoint`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00031 - OsScheduleTableEventSetting Model

The system shall provide an `OsScheduleTableEventSetting` model class for schedule table event setting actions.

| Field                                | Type        | Description              | Origin  |
| ------------------------------------ | ----------- | ------------------------ | ------- |
| OsScheduleTableSetEventRef [1..1]    | EcucRefType | Event reference          | AUTOSAR |
| OsScheduleTableSetEventTaskRef [1..1] | EcucRefType | Task reference for event | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTableEventSetting`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00032 - OsScheduleTableTaskActivation Model

The system shall provide an `OsScheduleTableTaskActivation` model class for schedule table task activation actions.

| Field                                 | Type        | Description             | Origin  |
| ------------------------------------- | ----------- | ----------------------- | ------- |
| OsScheduleTableActivateTaskRef [1..1] | EcucRefType | Task activation reference | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTableTaskActivation`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00033 - OsScheduleTblAdjustableExpPoint Model

The system shall provide an `OsScheduleTblAdjustableExpPoint` model class for adjustable expiry point configuration.

| Field                             | Type | Description                            | Origin  |
| --------------------------------- | ---- | -------------------------------------- | ------- |
| OsScheduleTableMaxLengthen [1..1] | int  | Maximum lengthen adjustment (0-4294967295) | AUTOSAR |
| OsScheduleTableMaxShorten [1..1]  | int  | Maximum shorten adjustment (0-4294967295)  | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTblAdjustableExpPoint`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_MODELS_00034 - OsScheduleTableSync Model

The system shall provide an `OsScheduleTableSync` model class for schedule table synchronization.

| Field                                 | Type                                        | Description                                                        | Origin  |
| ------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------ | ------- |
| OsScheduleTblSyncStrategy [1..1]      | OsScheduleTableSyncOsScheduleTblSyncStrategy | Synchronization strategy (EXPLICIT/IMPLICIT/NONE, default NONE) | AUTOSAR |

**Implementation:** `os_xdm.py:OsScheduleTableSync`
**Status:** Implemented
**Last Validated:** 2026-05-31

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
**Last Validated:** 2026-05-31

---

## Traceability

| Requirement ID       | Implementation                                                                                                 | Test Cases         |
| -------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------ |
| SWR_OS_MODELS_00001  | os_xdm.py:OsAlarm                                                                                              | UTS_OS_MODEL_00001 |
| SWR_OS_MODELS_00002  | os_xdm.py:OsAppMode                                                                                            | UTS_OS_MODEL_00002 |
| SWR_OS_MODELS_00003  | os_xdm.py:OsApplication                                                                                        | UTS_OS_MODEL_00003 |
| SWR_OS_MODELS_00004  | os_xdm.py:OsCounter                                                                                            | UTS_OS_MODEL_00004 |
| SWR_OS_MODELS_00005  | os_xdm.py:OsEvent                                                                                              | UTS_OS_MODEL_00005 |
| SWR_OS_MODELS_00006  | os_xdm.py:OsSpinlock                                                                                           | UTS_OS_MODEL_00006 |
| SWR_OS_MODELS_00007  | os_xdm.py:OsIsr                                                                                                | UTS_OS_MODEL_00007 |
| SWR_OS_MODELS_00008  | os_xdm.py:OsTask                                                                                               | UTS_OS_MODEL_00008 |
| SWR_OS_MODELS_00009  | os_xdm.py:OsPeripheralArea                                                                                     | UTS_OS_MODEL_00009 |
| SWR_OS_MODELS_00010  | os_xdm.py:OsResource                                                                                           | UTS_OS_MODEL_00010 |
| SWR_OS_MODELS_00011  | os_xdm.py:OsScheduleTable                                                                                      | UTS_OS_MODEL_00011 |
| SWR_OS_MODELS_00012  | os_xdm.py:Os                                                                                                   | UTS_OS_MODEL_00012 |
| SWR_OS_MODELS_00013  | os_xdm.py:OsAlarmActivateTask, os_xdm.py:OsAlarmCallback, os_xdm.py:OsAlarmIncrementCounter, os_xdm.py:OsAlarmSetEvent | UTS_OS_MODEL_00013 |
| SWR_OS_MODELS_00014  | os_xdm.py:OsAlarmActivateTask                                                                                  | UTS_OS_MODEL_00014 |
| SWR_OS_MODELS_00015  | os_xdm.py:OsAlarmCallback                                                                                      | UTS_OS_MODEL_00015 |
| SWR_OS_MODELS_00016  | os_xdm.py:OsAlarmIncrementCounter                                                                              | UTS_OS_MODEL_00016 |
| SWR_OS_MODELS_00017  | os_xdm.py:OsAlarmSetEvent                                                                                      | UTS_OS_MODEL_00017 |
| SWR_OS_MODELS_00018  | os_xdm.py:OsAlarmAutostart                                                                                     | UTS_OS_MODEL_00018 |
| SWR_OS_MODELS_00019  | os_xdm.py:OsApplicationHooks                                                                                   | UTS_OS_MODEL_00019 |
| SWR_OS_MODELS_00020  | os_xdm.py:OsApplicationTrustedFunction                                                                         | UTS_OS_MODEL_00020 |
| SWR_OS_MODELS_00021  | os_xdm.py:OsTimeConstant                                                                                       | UTS_OS_MODEL_00021 |
| SWR_OS_MODELS_00022  | os_xdm.py:OsDriver                                                                                             | UTS_OS_MODEL_00022 |
| SWR_OS_MODELS_00023  | os_xdm.py:OsHwIncrementer                                                                                      | UTS_OS_MODEL_00023 |
| SWR_OS_MODELS_00024  | os_xdm.py:OsIsrTimingProtection                                                                                | UTS_OS_MODEL_00024 |
| SWR_OS_MODELS_00025  | os_xdm.py:OsIsrResourceLock                                                                                    | UTS_OS_MODEL_00025 |
| SWR_OS_MODELS_00026  | os_xdm.py:OsTaskAutostart                                                                                      | UTS_OS_MODEL_00026 |
| SWR_OS_MODELS_00027  | os_xdm.py:OsTaskTimingProtection                                                                               | UTS_OS_MODEL_00027 |
| SWR_OS_MODELS_00028  | os_xdm.py:OsTaskResourceLock                                                                                   | UTS_OS_MODEL_00028 |
| SWR_OS_MODELS_00029  | os_xdm.py:OsScheduleTableAutostart                                                                             | UTS_OS_MODEL_00029 |
| SWR_OS_MODELS_00030  | os_xdm.py:OsScheduleTableExpiryPoint                                                                           | UTS_OS_MODEL_00030 |
| SWR_OS_MODELS_00031  | os_xdm.py:OsScheduleTableEventSetting                                                                          | UTS_OS_MODEL_00031 |
| SWR_OS_MODELS_00032  | os_xdm.py:OsScheduleTableTaskActivation                                                                        | UTS_OS_MODEL_00032 |
| SWR_OS_MODELS_00033  | os_xdm.py:OsScheduleTblAdjustableExpPoint                                                                      | UTS_OS_MODEL_00033 |
| SWR_OS_MODELS_00034  | os_xdm.py:OsScheduleTableSync                                                                                  | UTS_OS_MODEL_00034 |
