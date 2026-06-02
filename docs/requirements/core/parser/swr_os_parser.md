# Software Requirements: OS Module - Parser Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | OS Module Parser Layer Requirements |
| Document ID | SWR_OS_PARSER_00001 |
| Version | 1.0 |
| Date | 2026-05-31 |
| Project | py-eb-model |
| Module | OS (Operating System) - Parser Layer |

---

## Overview

The OS Parser Layer provides XDM file parsing for AUTOSAR OS configuration data.

**Implementation:** `src/eb_model/parser/core/os_xdm_parser.py`

---

## Requirements

### SWR_OS_PARSER_00001 - Module Validation

The parser shall validate that the XDM file contains OS module configuration.

- Extract module name from XDM datamodel root element
- Raise `ValueError` if module name is not "Os"
- Store namespace map for XPath queries

**Implementation:** `os_xdm_parser.py:OsXdmParser.parse`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00002 - Version Extraction

The parser shall extract version information from OS configuration.

- Extract ARVersion (ArMajorVersion, ArMinorVersion, ArPatchVersion)
- Extract SwVersion (SwMajorVersion, SwMinorVersion, SwPatchVersion)
- Extract VendorId

**Implementation:** `os_xdm_parser.py:read_version_info`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00003 - Task Parsing

The parser shall parse OsTask elements from XDM.

- Extract OsTaskActivation [1..1] (INTEGER, 1-255)
- Extract OsTaskPriority [1..1] (INTEGER, 0-2147483647)
- Extract OsTaskSchedule [1..1] (ENUMERATION: FULL/NON, default FULL)
- Extract OsStacksize [1..1] (INTEGER, 0-2000000000)
- Parse OsTaskAccessingApplication [1..*] (REFERENCE list)
- Parse OsTaskEventRef [1..*] (REFERENCE list)
- Parse OsTaskResourceRef [1..*] (REFERENCE list)
- Parse OsTaskAutostart [0..1] sub-container (see SWR_OS_PARSER_00016)
- Parse OsTaskTimingProtection [0..1] sub-container (see SWR_OS_PARSER_00017)

**Implementation:** `os_xdm_parser.py:read_os_tasks`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00004 - ISR Parsing

The parser shall parse OsIsr elements from XDM.

- Extract OsIsrCategory [1..1] (ENUMERATION: CATEGORY_1/CATEGORY_2)
- Parse OsIsrResourceRef [1..*] (REFERENCE list)
- Extract OsWindowsVector [1..1] (ENUMERATION: INTUSER00-INTUSER31/TIMER0-3/XCORE0-3)
- Parse OsIsrAccessingApplication [1..*] (REFERENCE list)
- Extract OsWindowsIrqLevel [1..1] (INTEGER, 0-31)
- Extract OsStacksize [1..1] (INTEGER, 0-2000000000)
- Parse OsIsrTimingProtection [0..1] sub-container (see SWR_OS_PARSER_00019)

**Implementation:** `os_xdm_parser.py:read_os_isrs`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00005 - Schedule Table Parsing

The parser shall parse OsScheduleTable elements from XDM.

- Extract OsScheduleTableDuration [1..1] (INTEGER)
- Extract OsScheduleTableRepeating [1..1] (BOOLEAN, default false)
- Parse OsSchTblAccessingApplication [1..*] (REFERENCE list)
- Extract OsScheduleTableCounterRef [1..1] (REFERENCE)
- Parse OsScheduleTableAutostart [0..1] sub-container (see SWR_OS_PARSER_00022)
- Parse OsScheduleTableExpiryPoint [1..*] sub-containers (see SWR_OS_PARSER_00023)
- Parse OsScheduleTableSync [0..1] sub-container (see SWR_OS_PARSER_00027)

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00006 - Counter Parsing

The parser shall parse OsCounter elements from XDM.

- Extract OsCounterMaxAllowedValue [1..1] (INTEGER, 1-4294967295)
- Extract OsCounterMinCycle [1..1] (INTEGER)
- Extract OsCounterTicksPerBase [1..1] (INTEGER, 1-4294967295)
- Extract OsCounterType [1..1] (ENUMERATION: HARDWARE/SOFTWARE)
- Extract OsCounterWindowsTimer [1..1] (ENUMERATION: TIMER0-3/TSIM_00-11)
- Parse OsCounterAccessingApplication [1..*] (REFERENCE list)
- Extract OsWindowsIrqLevel [1..1] (INTEGER, 1-32)
- Parse OsTimeConstant [1..*] sub-containers (see SWR_OS_PARSER_00020)
- Parse OsDriver [0..1] sub-container (see SWR_OS_PARSER_00021)

**Implementation:** `os_xdm_parser.py:read_os_counters`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00007 - Application Parsing

The parser shall parse OsApplication elements from XDM.

- Extract OsTrusted [1..1] (BOOLEAN, default false)
- Extract OsTrustedApplicationWithProtection [1..1] (BOOLEAN, default false)
- Extract OsTrustedApplicationDelayTimingViolationCall [1..1] (BOOLEAN, default false)
- Extract OsApplicationCoreRef [1..1] (REFERENCE)
- Parse OsAppTaskRef [1..*] (REFERENCE list)
- Parse OsAppIsrRef [1..*] (REFERENCE list)
- Parse OsAppAlarmRef [1..*] (REFERENCE list)
- Parse OsAppCounterRef [1..*] (REFERENCE list)
- Parse OsAppResourceRef [1..*] (REFERENCE list)
- Parse OsAppScheduleTableRef [1..*] (REFERENCE list)
- Parse OsApplicationHooks [1..1] sub-container (see SWR_OS_PARSER_00014)
- Parse OsApplicationTrustedFunction [1..*] sub-containers (see SWR_OS_PARSER_00015)

**Implementation:** `os_xdm_parser.py:read_os_applications`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00008 - Alarm Parsing

The parser shall parse OsAlarm elements from XDM.

- Parse OsAlarmAccessingApplication [1..*] (REFERENCE list)
- Extract OsAlarmCounterRef [1..1] (REFERENCE)
- Parse OsAlarmAction [1..1] choice container (see SWR_OS_PARSER_00009)
- Parse OsAlarmAutostart [0..1] sub-container (see SWR_OS_PARSER_00010)

**Implementation:** `os_xdm_parser.py:read_os_alarms`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00009 - Alarm Action Parsing

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
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00010 - Alarm Autostart Parsing

The parser shall parse OsAlarmAutostart sub-container from XDM.

- Extract OsAlarmAlarmTime [1..1] (INTEGER, 1-4294967295)
- Extract OsAlarmAutostartType [1..1] (ENUMERATION: ABSOLUTE/RELATIVE, default RELATIVE)
- Extract OsAlarmCycleTime [1..1] (INTEGER, 0-4294967295)
- Parse OsAlarmAppModeRef [1..*] (REFERENCE list)

**Implementation:** `os_xdm_parser.py:read_os_alarms`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00011 - Resource Parsing

The parser shall parse OsResource elements from XDM.

- Extract OsResourceProperty [1..1] (ENUMERATION: INTERNAL/LINKED/STANDARD, default STANDARD)
- Parse OsResourceAccessingApplication [1..*] (REFERENCE list)

**Implementation:** `os_xdm_parser.py:read_os_resources`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00012 - Event Parsing

The parser shall parse OsEvent elements from XDM.

- Parse OsEvent name identifier

**Implementation:** `os_xdm_parser.py:read_os_events`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00013 - Spinlock Parsing

The parser shall parse OsSpinlock elements from XDM.

- Extract OsSpinlockLockMethod [1..1] (ENUMERATION: LOCK_NOTHING/LOCK_ALL_INTERRUPTS/LOCK_CAT2_INTERRUPTS/LOCK_WITH_RES_SCHEDULER, default LOCK_NOTHING)
- Extract OsSpinlockSuccessor [1..1] (REFERENCE)
- Parse OsSpinlockAccessingApplication [1..*] (REFERENCE list)

**Implementation:** `os_xdm_parser.py:read_os_spinlocks`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00014 - Application Hooks Parsing

The parser shall parse OsApplicationHooks sub-container from XDM.

- Extract OsAppErrorHook [1..1] (BOOLEAN, default false)
- Extract OsAppShutdownHook [1..1] (BOOLEAN, default false)
- Extract OsAppStartupHook [1..1] (BOOLEAN, default false)

**Implementation:** `os_xdm_parser.py:read_os_applications`
**Status:** Not Implemented
**Last Validated:** N/A

---

### SWR_OS_PARSER_00015 - Application Trusted Function Parsing

The parser shall parse OsApplicationTrustedFunction sub-containers from XDM.

- Extract OsTrustedFunctionName [1..1] (FUNCTION-NAME)

**Implementation:** `os_xdm_parser.py:read_os_applications`
**Status:** Not Implemented
**Last Validated:** N/A

---

### SWR_OS_PARSER_00016 - Task Autostart Parsing

The parser shall parse OsTaskAutostart sub-container from XDM.

- Parse OsTaskAppModeRef [1..*] (REFERENCE list)

**Implementation:** `os_xdm_parser.py:read_os_tasks`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00017 - Task Timing Protection Parsing

The parser shall parse OsTaskTimingProtection sub-container from XDM.

- Parse OsTaskResourceLock [1..*] sub-containers (see SWR_OS_PARSER_00018)

**Implementation:** `os_xdm_parser.py:read_os_tasks`
**Status:** Not Implemented
**Last Validated:** N/A

---

### SWR_OS_PARSER_00018 - Task Resource Lock Parsing

The parser shall parse OsTaskResourceLock sub-containers from XDM.

- Extract OsTaskResourceLockBudget [1..1] (FLOAT, 0.0-86400.0)
- Extract OsTaskResourceLockResourceRef [1..1] (REFERENCE)

**Implementation:** `os_xdm_parser.py:read_os_tasks`
**Status:** Not Implemented
**Last Validated:** N/A

---

### SWR_OS_PARSER_00019 - ISR Timing Protection Parsing

The parser shall parse OsIsrTimingProtection sub-container from XDM.

- Parse OsIsrResourceLock [1..*] sub-containers (see SWR_OS_PARSER_00020_new)

**Implementation:** `os_xdm_parser.py:read_os_isrs`
**Status:** Not Implemented
**Last Validated:** N/A

---

### SWR_OS_PARSER_00028 - ISR Resource Lock Parsing

The parser shall parse OsIsrResourceLock sub-containers from XDM.

- Extract OsIsrResourceLockBudget [1..1] (FLOAT, 0.0-86400.0)
- Extract OsIsrResourceLockResourceRef [1..1] (REFERENCE)

**Implementation:** `os_xdm_parser.py:read_os_isrs`
**Status:** Not Implemented
**Last Validated:** N/A

---

### SWR_OS_PARSER_00020 - Time Constant Parsing

The parser shall parse OsTimeConstant sub-containers from XDM.

- Extract OsTimeValue [1..1] (FLOAT, 0.0-86400.0)
- Extract OsConstName [1..1] (STRING)

**Implementation:** `os_xdm_parser.py:read_os_counters`
**Status:** Not Implemented
**Last Validated:** N/A

---

### SWR_OS_PARSER_00021 - Counter Driver Parsing

The parser shall parse OsDriver sub-container from XDM.

- Parse OsHwIncrementer [0..1] sub-container (see SWR_OS_PARSER_00022_new)

**Implementation:** `os_xdm_parser.py:read_os_counters`
**Status:** Not Implemented
**Last Validated:** N/A

---

### SWR_OS_PARSER_00029 - Hardware Incrementer Parsing

The parser shall parse OsHwIncrementer sub-container from XDM.

- Extract OsHwModule [1..1] (ENUMERATION)
- Extract OsIncrementerIrqLevel [1..1] (INTEGER, 1)

**Implementation:** `os_xdm_parser.py:read_os_counters`
**Status:** Not Implemented
**Last Validated:** N/A

---

### SWR_OS_PARSER_00022 - Schedule Table Autostart Parsing

The parser shall parse OsScheduleTableAutostart sub-container from XDM.

- Extract OsScheduleTableAutostartType [1..1] (ENUMERATION: ABSOLUTE/RELATIVE/SYNCHRON, default RELATIVE)
- Parse OsScheduleTableAppModeRef [1..*] (REFERENCE list)
- Extract OsScheduleTableStartValue [1..1] (INTEGER, 0-4294967295)

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00023 - Schedule Table Expiry Point Parsing

The parser shall parse OsScheduleTableExpiryPoint sub-containers from XDM.

- Extract OsScheduleTblExpPointOffset [1..1] (INTEGER)
- Parse OsScheduleTableEventSetting [1..*] sub-containers (see SWR_OS_PARSER_00024)
- Parse OsScheduleTableTaskActivation [1..*] sub-containers (see SWR_OS_PARSER_00025)
- Parse OsScheduleTblAdjustableExpPoint [0..1] sub-container (see SWR_OS_PARSER_00026)

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00024 - Schedule Table Event Setting Parsing

The parser shall parse OsScheduleTableEventSetting sub-containers from XDM.

- Extract OsScheduleTableSetEventRef [1..1] (REFERENCE)
- Extract OsScheduleTableSetEventTaskRef [1..1] (REFERENCE)

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00025 - Schedule Table Task Activation Parsing

The parser shall parse OsScheduleTableTaskActivation sub-containers from XDM.

- Extract OsScheduleTableActivateTaskRef [1..1] (REFERENCE)

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00026 - Adjustable Expiry Point Parsing

The parser shall parse OsScheduleTblAdjustableExpPoint sub-container from XDM.

- Extract OsScheduleTableMaxLengthen [1..1] (INTEGER, 0-4294967295)
- Extract OsScheduleTableMaxShorten [1..1] (INTEGER, 0-4294967295)

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00027 - Schedule Table Sync Parsing

The parser shall parse OsScheduleTableSync sub-container from XDM.

- Extract OsScheduleTblSyncStrategy [1..1] (ENUMERATION: EXPLICIT/IMPLICIT/NONE, default NONE)

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00030 - Hooks Parsing

The parser shall parse OsHooks elements from XDM.

- Extract hook enable flags: OsStartupHook, OsShutdownHook, OsErrorHook, OsPreTaskHook, OsPostTaskHook

**Implementation:** `os_xdm_parser.py:read_os_hooks`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00031 - OS Configuration Parsing

The parser shall parse OsOS configuration elements from XDM.

- Extract OsScalabilityClass, OsUseOsApplication, OsUseGetServiceId
- Extract OsNumberOfCores, OsUseParameterAccess

**Implementation:** `os_xdm_parser.py:read_os_os`
**Status:** Implemented
**Last Validated:** 2026-05-31

---

### SWR_OS_PARSER_00032 - Application Mode Parsing

The parser shall parse OsAppMode elements from XDM.

- Extract OsAppMode name
- Add OsAppMode to Os model

**Implementation:** `os_xdm_parser.py:read_os_appmodes`
**Status:** Not Implemented
**Last Validated:** N/A

---

### SWR_OS_PARSER_00033 - Peripheral Area Parsing

The parser shall parse OsPeripheralArea elements from XDM.

- Extract OsPeripheralAreaStartAddress [1..1] (INTEGER, 0-9223372036854775807)
- Extract OsPeripheralAreaEndAddress [1..1] (INTEGER, 0-9223372036854775807)
- Extract OsPeripheralAreaId [1..1] (INTEGER, 0-9223372036854775807)
- Parse OsPeripheralAreaAccessingApplication [1..1] (REFERENCE)

**Implementation:** `os_xdm_parser.py:read_os_peripheral_areas`
**Status:** Partially Implemented (missing OsPeripheralAreaId)
**Last Validated:** 2026-05-31

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_OS_PARSER_00001 | os_xdm_parser.py:parse | TC_UNIT_OS_00001 |
| SWR_OS_PARSER_00002 | os_xdm_parser.py:read_version_info | TC_UNIT_OS_00002 |
| SWR_OS_PARSER_00003 | os_xdm_parser.py:read_os_tasks | TC_UNIT_OS_00003 |
| SWR_OS_PARSER_00004 | os_xdm_parser.py:read_os_isrs | TC_UNIT_OS_00004 |
| SWR_OS_PARSER_00005 | os_xdm_parser.py:read_os_schedule_tables | TC_UNIT_OS_00005 |
| SWR_OS_PARSER_00006 | os_xdm_parser.py:read_os_counters | TC_UNIT_OS_00006 |
| SWR_OS_PARSER_00007 | os_xdm_parser.py:read_os_applications | TC_UNIT_OS_00007 |
| SWR_OS_PARSER_00008 | os_xdm_parser.py:read_os_alarms | TC_UNIT_OS_00008 |
| SWR_OS_PARSER_00009 | os_xdm_parser.py:read_os_alarms | TC_UNIT_OS_00009 |
| SWR_OS_PARSER_00010 | os_xdm_parser.py:read_os_alarms | TC_UNIT_OS_00010 |
| SWR_OS_PARSER_00011 | os_xdm_parser.py:read_os_resources | TC_UNIT_OS_00011 |
| SWR_OS_PARSER_00012 | os_xdm_parser.py:read_os_events | TC_UNIT_OS_00012 |
| SWR_OS_PARSER_00013 | os_xdm_parser.py:read_os_spinlocks | TC_UNIT_OS_00013 |
| SWR_OS_PARSER_00014 | os_xdm_parser.py:read_os_applications | TC_UNIT_OS_00014 |
| SWR_OS_PARSER_00015 | os_xdm_parser.py:read_os_applications | TC_UNIT_OS_00015 |
| SWR_OS_PARSER_00016 | os_xdm_parser.py:read_os_tasks | TC_UNIT_OS_00016 |
| SWR_OS_PARSER_00017 | os_xdm_parser.py:read_os_tasks | TC_UNIT_OS_00017 |
| SWR_OS_PARSER_00018 | os_xdm_parser.py:read_os_tasks | TC_UNIT_OS_00018 |
| SWR_OS_PARSER_00019 | os_xdm_parser.py:read_os_isrs | TC_UNIT_OS_00019 |
| SWR_OS_PARSER_00020 | os_xdm_parser.py:read_os_counters | TC_UNIT_OS_00020 |
| SWR_OS_PARSER_00021 | os_xdm_parser.py:read_os_counters | TC_UNIT_OS_00021 |
| SWR_OS_PARSER_00022 | os_xdm_parser.py:read_os_schedule_tables | TC_UNIT_OS_00022 |
| SWR_OS_PARSER_00023 | os_xdm_parser.py:read_os_schedule_tables | TC_UNIT_OS_00023 |
| SWR_OS_PARSER_00024 | os_xdm_parser.py:read_os_schedule_tables | TC_UNIT_OS_00024 |
| SWR_OS_PARSER_00025 | os_xdm_parser.py:read_os_schedule_tables | TC_UNIT_OS_00025 |
| SWR_OS_PARSER_00026 | os_xdm_parser.py:read_os_schedule_tables | TC_UNIT_OS_00026 |
| SWR_OS_PARSER_00027 | os_xdm_parser.py:read_os_schedule_tables | TC_UNIT_OS_00027 |
| SWR_OS_PARSER_00028 | os_xdm_parser.py:read_os_isrs | TC_UNIT_OS_00028 |
| SWR_OS_PARSER_00029 | os_xdm_parser.py:read_os_counters | TC_UNIT_OS_00029 |
| SWR_OS_PARSER_00030 | os_xdm_parser.py:read_os_hooks | TC_UNIT_OS_00030 |
| SWR_OS_PARSER_00031 | os_xdm_parser.py:read_os_os | TC_UNIT_OS_00031 |
| SWR_OS_PARSER_00032 | os_xdm_parser.py:read_os_appmodes | TC_UNIT_OS_00032 |
| SWR_OS_PARSER_00033 | os_xdm_parser.py:read_os_peripheral_areas | TC_UNIT_OS_00033 |
