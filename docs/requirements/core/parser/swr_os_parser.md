# Software Requirements: Os - Parser Layer

## Document Information

| Item | Value |
|------|-------|
| Module | Os |
| Stack | core |
| Abbreviation | OS |
| Generated From | Os.xdm |
| Generation Date | 2026-06-04 |

## Overview

This document defines the parser layer requirements for the AUTOSAR OS module. These requirements specify how XDM configuration files are parsed to extract OS configuration entities.

## Requirements

### SWR_OS_PARSER_00001 - Module Validation

The parser shall validate the OS module configuration structure.

- Verify module name is "Os"
- Verify module type is "MODULE-DEF"
- Raise `ValueError` if module validation fails

**Implementation:** `os_xdm_parser.py:parse`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00002 - Version Extraction

The parser shall extract version information from OS configuration.

- Extract ARVersion (ArMajorVersion, ArMinorVersion, ArPatchVersion)
- Extract SwVersion (SwMajorVersion, SwMinorVersion, SwPatchVersion)
- Extract VendorId

**Implementation:** `os_xdm_parser.py:read_version_info`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00003 - Alarm Parsing

The parser shall parse OsAlarm elements from XDM.

- Parse OsAlarmAccessingApplication [1..*] (REFERENCE list) — via `read_ref_value_list()`
- Extract OsAlarmCounterRef [1..1] (REFERENCE) — via `read_ref_value()`
- Parse OsAlarmAction [1..1] choice container (see SWR_OS_PARSER_00004)
- Parse OsAlarmAutostart [0..1] sub-container (see SWR_OS_PARSER_00005)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_alarms`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00004 - Alarm Action Parsing

The parser shall parse OsAlarmAction choice element from XDM.

- Parse OsAlarmActivateTask variant:
  - Extract OsAlarmActivateTaskRef [1..1] (REFERENCE)
- Parse OsAlarmCallback variant:
  - Extract OsAlarmCallbackName [1..1] (FUNCTION-NAME)
- Parse OsAlarmIncrementCounter variant:
  - Extract OsAlarmIncrementCounterRef [1..1] (REFERENCE)
- Parse OsAlarmSetEvent variant:
  - Extract OsAlarmSetEventRef [1..1] (REFERENCE)
  - Extract OsAlarmSetEventTaskRef [1..1] (REFERENCE)
- Raise `ValueError` if alarm action is missing or unsupported

**Implementation:** `os_xdm_parser.py:read_os_alarms`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00005 - Alarm Autostart Parsing

The parser shall parse OsAlarmAutostart sub-container from XDM.

- Extract OsAlarmAlarmTime [1..1] (INTEGER, 1-4294967295)
- Extract OsAlarmAutostartType [1..1] (ENUMERATION: ABSOLUTE/RELATIVE, default RELATIVE)
- Extract OsAlarmCycleTime [1..1] (INTEGER, 0-4294967295)
- Parse OsAlarmAppModeRef [1..*] (REFERENCE list)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_alarms`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00006 - Application Mode Parsing

The parser shall parse OsAppMode elements from XDM.

- Extract OsAppModeName [1..1] (STRING)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_app_modes`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00007 - Application Parsing

The parser shall parse OsApplication elements from XDM.

- Parse OsAppResourceRef [1..*] (REFERENCE list) — via `read_ref_value_list()`
- Extract OsTrustedApplicationWithProtection [1..1] (BOOLEAN, default false)
- Extract OsTrustedApplicationDelayTimingViolationCall [1..1] (BOOLEAN, default false)
- Extract OsTrusted [1..1] (BOOLEAN, default false)
- Extract OsApplicationCoreRef [1..1] (REFERENCE)
- Parse OsAppTaskRef [1..*] (REFERENCE list)
- Parse OsAppIsrRef [1..*] (REFERENCE list)
- Parse OsAppAlarmRef [1..*] (REFERENCE list)
- Parse OsAppCounterRef [1..*] (REFERENCE list)
- Parse OsAppScheduleTableRef [1..*] (REFERENCE list)
- Parse OsApplicationHooks [1..1] sub-container (see SWR_OS_PARSER_00008)
- Parse OsApplicationTrustedFunction [1..*] sub-containers (see SWR_OS_PARSER_00009)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_applications`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00008 - Application Hooks Parsing

The parser shall parse OsApplicationHooks sub-container from XDM.

- Extract OsAppStartupHook [0..1] (STRING)
- Extract OsAppShutdownHook [0..1] (STRING)
- Extract OsAppErrorHook [0..1] (STRING)

**Implementation:** `os_xdm_parser.py:read_os_applications`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00009 - Application Trusted Function Parsing

The parser shall parse OsApplicationTrustedFunction sub-containers from XDM.

- Extract OsTrustedFunctionName [1..1] (STRING)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_applications`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00010 - Counter Parsing

The parser shall parse OsCounter elements from XDM.

- Extract OsCounterMaxAllowedValue [1..1] (INTEGER, 1-4294967295)
- Extract OsCounterMinCycle [1..1] (INTEGER)
- Extract OsCounterTicksPerBase [1..1] (INTEGER, 1-4294967295)
- Extract OsCounterType [1..1] (ENUMERATION: HARDWARE/SOFTWARE)
- Extract OsCounterWindowsTimer [1..1] (ENUMERATION: TIMER0-3/TSIM_00-11)
- Parse OsCounterAccessingApplication [1..*] (REFERENCE list)
- Extract OsWindowsIrqLevel [1..1] (INTEGER, 1-32)
- Parse OsTimeConstant [1..*] sub-containers (see SWR_OS_PARSER_00011)
- Parse OsDriver [0..1] sub-container (see SWR_OS_PARSER_00012)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_counters`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00011 - Time Constant Parsing

The parser shall parse OsTimeConstant sub-containers from XDM.

- Extract OsTimeValue [1..1] (FLOAT, 0.0-86400.0)
- Extract OsConstName [1..1] (STRING)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_counters`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00012 - Counter Driver Parsing

The parser shall parse OsDriver sub-container from XDM.

- Parse OsHwIncrementer [1..*] sub-containers (see SWR_OS_PARSER_00013)

**Implementation:** `os_xdm_parser.py:read_os_counters`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00013 - Hardware Incrementer Parsing

The parser shall parse OsHwIncrementer sub-containers from XDM.

- Extract OsHwIncrementerSystemTime [1..1] (INTEGER)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_counters`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00014 - Event Parsing

The parser shall parse OsEvent elements from XDM.

- Extract OsEventName [1..1] (STRING)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_events`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00015 - Spinlock Parsing

The parser shall parse OsSpinlock elements from XDM.

- Parse OsSpinlockAccessingApplication [1..*] (REFERENCE list)
- Extract OsSpinlockSuccessor [1..1] (REFERENCE)
- Extract OsSpinlockLockMethod [1..1] (ENUMERATION)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_spinlocks`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00016 - ISR Parsing

The parser shall parse OsIsr elements from XDM.

- Extract OsIsrCategory [1..1] (ENUMERATION)
- Parse OsIsrResourceRef [1..*] (REFERENCE list)
- Extract OsWindowsVector [1..1] (ENUMERATION)
- Parse OsIsrAccessingApplication [1..*] (REFERENCE list)
- Extract OsWindowsIrqLevel [1..1] (INTEGER, 1-32)
- Extract OsStacksize [1..1] (INTEGER)
- Parse OsIsrTimingProtection [0..1] sub-container (see SWR_OS_PARSER_00017)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_isrs`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00017 - ISR Timing Protection Parsing

The parser shall parse OsIsrTimingProtection sub-container from XDM.

- Parse OsIsrResourceLock [1..*] sub-containers (see SWR_OS_PARSER_00018)

**Implementation:** `os_xdm_parser.py:read_os_isrs`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00018 - ISR Resource Lock Parsing

The parser shall parse OsIsrResourceLock sub-containers from XDM.

- Extract OsIsrResourceLockBudget [1..1] (FLOAT, 0.0-86400.0)
- Extract OsIsrResourceLockResourceRef [1..1] (REFERENCE)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_isrs`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00019 - Task Parsing

The parser shall parse OsTask elements from XDM.

- Extract OsTaskActivation [1..1] (INTEGER, 1-255)
- Extract OsTaskPriority [1..1] (INTEGER, 0-2147483647)
- Extract OsTaskSchedule [1..1] (ENUMERATION: FULL/NON, default FULL)
- Extract OsStacksize [1..1] (INTEGER, 0-2000000000)
- Parse OsTaskAccessingApplication [1..*] (REFERENCE list)
- Parse OsTaskEventRef [1..*] (REFERENCE list)
- Parse OsTaskResourceRef [1..*] (REFERENCE list)
- Parse OsTaskAutostart [0..1] sub-container (see SWR_OS_PARSER_00020)
- Parse OsTaskTimingProtection [0..1] sub-container (see SWR_OS_PARSER_00021)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_tasks`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00020 - Task Autostart Parsing

The parser shall parse OsTaskAutostart sub-container from XDM.

- Parse OsTaskAppModeRef [1..*] (REFERENCE list)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_tasks`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00021 - Task Timing Protection Parsing

The parser shall parse OsTaskTimingProtection sub-container from XDM.

- Parse OsTaskResourceLock [1..*] sub-containers (see SWR_OS_PARSER_00022)

**Implementation:** `os_xdm_parser.py:read_os_tasks`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00022 - Task Resource Lock Parsing

The parser shall parse OsTaskResourceLock sub-containers from XDM.

- Extract OsTaskResourceLockBudget [1..1] (FLOAT, 0.0-86400.0)
- Extract OsTaskResourceLockResourceRef [1..1] (REFERENCE)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_tasks`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00023 - Peripheral Area Parsing

The parser shall parse OsPeripheralArea elements from XDM.

- Extract OsPeripheralAreaEndAddress [1..1] (INTEGER, 0-9223372036854775807)
- Extract OsPeripheralAreaId [1..1] (INTEGER, 0-9223372036854775807)
- Extract OsPeripheralAreaStartAddress [1..1] (INTEGER, 0-9223372036854775807)
- Extract OsPeripheralAreaAccessingApplication [1..1] (REFERENCE)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_peripheral_areas`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00024 - Resource Parsing

The parser shall parse OsResource elements from XDM.

- Extract OsResourceProperty [1..1] (ENUMERATION)
- Parse OsResourceAccessingApplication [1..*] (REFERENCE list)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_resources`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00025 - Schedule Table Parsing

The parser shall parse OsScheduleTable elements from XDM.

- Extract OsScheduleTableDuration [1..1] (INTEGER)
- Extract OsScheduleTableRepeating [1..1] (BOOLEAN)
- Parse OsSchTblAccessingApplication [1..*] (REFERENCE list)
- Extract OsScheduleTableCounterRef [1..1] (REFERENCE)
- Parse OsScheduleTableAutostart [0..1] sub-container (see SWR_OS_PARSER_00026)
- Parse OsScheduleTableExpiryPoint [1..*] sub-containers (see SWR_OS_PARSER_00027)
- Parse OsScheduleTableSync [0..1] sub-container (see SWR_OS_PARSER_00028)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00026 - Schedule Table Autostart Parsing

The parser shall parse OsScheduleTableAutostart sub-container from XDM.

- Extract OsScheduleTableAutostartType [1..1] (ENUMERATION: ABSOLUTE/RELATIVE/SYNCHRON, default RELATIVE)
- Parse OsScheduleTableAppModeRef [1..*] (REFERENCE list)
- Extract OsScheduleTableStartValue [1..1] (INTEGER, 0-4294967295)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00027 - Schedule Table Expiry Point Parsing

The parser shall parse OsScheduleTableExpiryPoint sub-containers from XDM.

- Extract OsScheduleTblExpPointOffset [1..1] (INTEGER)
- Parse OsScheduleTableEventSetting [1..*] sub-containers (see SWR_OS_PARSER_00029)
- Parse OsScheduleTableTaskActivation [1..*] sub-containers (see SWR_OS_PARSER_00030)
- Parse OsScheduleTblAdjustableExpPoint [0..1] sub-container (see SWR_OS_PARSER_00031)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00028 - Schedule Table Sync Parsing

The parser shall parse OsScheduleTableSync sub-container from XDM.

- Extract OsScheduleTableSyncStrategy [1..1] (ENUMERATION)
- Parse OsScheduleTableExplicitSync [0..1] sub-container
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00029 - Schedule Table Event Setting Parsing

The parser shall parse OsScheduleTableEventSetting sub-containers from XDM.

- Extract OsScheduleTableSetEventRef [1..1] (REFERENCE)
- Extract OsScheduleTableSetEventTaskRef [1..1] (REFERENCE)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00030 - Schedule Table Task Activation Parsing

The parser shall parse OsScheduleTableTaskActivation sub-containers from XDM.

- Extract OsScheduleTableActivateTaskRef [1..1] (REFERENCE)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00031 - Adjustable Expiry Point Parsing

The parser shall parse OsScheduleTblAdjustableExpPoint sub-container from XDM.

- Extract OsScheduleTableExpPointAdjustmentAllowed [1..1] (BOOLEAN)
- Extract OsScheduleTableExpPointAdjustmentMaxAllowed [1..1] (INTEGER)
- Raise `ValueError` if required field is missing

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

### SWR_OS_PARSER_00032 - OS Configuration Parsing

The parser shall parse the complete OS module configuration.

- Parse OsAlarm list — via `read_os_alarms()`
- Parse OsAppMode list — via `read_os_app_modes()`
- Parse OsApplication list — via `read_os_applications()`
- Parse OsCounter list — via `read_os_counters()`
- Parse OsEvent list — via `read_os_events()`
- Parse OsSpinlock list — via `read_os_spinlocks()`
- Parse OsIsr list — via `read_os_isrs()`
- Parse OsTask list — via `read_os_tasks()`
- Parse OsPeripheralArea list — via `read_os_peripheral_areas()`
- Parse OsResource list — via `read_os_resources()`
- Parse OsScheduleTable list — via `read_os_schedule_tables()`
- Return Os model instance with all parsed entities

**Implementation:** `os_xdm_parser.py:parse`
**Status:** Implemented
**Last Validated:** 2026-06-04

---

## Implementation Notes

| Requirement ID | Implementation |
| --- | --- |
| SWR_OS_PARSER_00001 | os_xdm_parser.py:parse |
| SWR_OS_PARSER_00002 | os_xdm_parser.py:read_version_info |
| SWR_OS_PARSER_00003 | os_xdm_parser.py:read_os_alarms |
| SWR_OS_PARSER_00004 | os_xdm_parser.py:read_os_alarms |
| SWR_OS_PARSER_00005 | os_xdm_parser.py:read_os_alarms |
| SWR_OS_PARSER_00006 | os_xdm_parser.py:read_os_app_modes |
| SWR_OS_PARSER_00007 | os_xdm_parser.py:read_os_applications |
| SWR_OS_PARSER_00008 | os_xdm_parser.py:read_os_applications |
| SWR_OS_PARSER_00009 | os_xdm_parser.py:read_os_applications |
| SWR_OS_PARSER_00010 | os_xdm_parser.py:read_os_counters |
| SWR_OS_PARSER_00011 | os_xdm_parser.py:read_os_counters |
| SWR_OS_PARSER_00012 | os_xdm_parser.py:read_os_counters |
| SWR_OS_PARSER_00013 | os_xdm_parser.py:read_os_counters |
| SWR_OS_PARSER_00014 | os_xdm_parser.py:read_os_events |
| SWR_OS_PARSER_00015 | os_xdm_parser.py:read_os_spinlocks |
| SWR_OS_PARSER_00016 | os_xdm_parser.py:read_os_isrs |
| SWR_OS_PARSER_00017 | os_xdm_parser.py:read_os_isrs |
| SWR_OS_PARSER_00018 | os_xdm_parser.py:read_os_isrs |
| SWR_OS_PARSER_00019 | os_xdm_parser.py:read_os_tasks |
| SWR_OS_PARSER_00020 | os_xdm_parser.py:read_os_tasks |
| SWR_OS_PARSER_00021 | os_xdm_parser.py:read_os_tasks |
| SWR_OS_PARSER_00022 | os_xdm_parser.py:read_os_tasks |
| SWR_OS_PARSER_00023 | os_xdm_parser.py:read_os_peripheral_areas |
| SWR_OS_PARSER_00024 | os_xdm_parser.py:read_os_resources |
| SWR_OS_PARSER_00025 | os_xdm_parser.py:read_os_schedule_tables |
| SWR_OS_PARSER_00026 | os_xdm_parser.py:read_os_schedule_tables |
| SWR_OS_PARSER_00027 | os_xdm_parser.py:read_os_schedule_tables |
| SWR_OS_PARSER_00028 | os_xdm_parser.py:read_os_schedule_tables |
| SWR_OS_PARSER_00029 | os_xdm_parser.py:read_os_schedule_tables |
| SWR_OS_PARSER_00030 | os_xdm_parser.py:read_os_schedule_tables |
| SWR_OS_PARSER_00031 | os_xdm_parser.py:read_os_schedule_tables |
| SWR_OS_PARSER_00032 | os_xdm_parser.py:parse |