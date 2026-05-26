# Software Requirements: OS Module - Parser Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | OS Module Parser Layer Requirements |
| Document ID | SWR_OS_PARSER_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
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
**Last Validated:** 2026-05-26

---

### SWR_OS_PARSER_00002 - Version Extraction

The parser shall extract version information from OS configuration.

- Extract ARVersion (ArMajorVersion, ArMinorVersion, ArPatchVersion)
- Extract SwVersion (SwMajorVersion, SwMinorVersion, SwPatchVersion)
- Extract VendorId

**Implementation:** `os_xdm_parser.py:read_version_info`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_PARSER_00003 - Task Parsing

The parser shall parse OsTask elements from XDM.

- Extract required fields: OsTaskPriority, OsTaskActivation, OsTaskSchedule, OsStacksize, OsTaskType
- Extract optional fields: OsTaskAutostart, OsMeasureMaxRuntime, OsTaskUseHwFp
- Parse OsTaskResourceRef list
- Parse OsTaskEventRef list

**Implementation:** `os_xdm_parser.py:read_os_tasks`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_PARSER_00004 - ISR Parsing

The parser shall parse OsIsr elements from XDM.

- Extract required fields: OsIsrCategory, OsIsrPriority
- Extract platform-specific fields: OsIsrTricoreIrqLevel, OsIsrTricoreVector, OsIsrARMIrqLevel
- Parse OsIsrMemoryRegionRefs list

**Implementation:** `os_xdm_parser.py:read_os_isrs`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_PARSER_00005 - Schedule Table Parsing

The parser shall parse OsScheduleTable elements from XDM.

- Extract OsScheduleTableDuration, OsScheduleTableRepeating, OsScheduleTableCounterRef
- Parse OsScheduleTableAutostart configuration
- Parse OsScheduleTblExpiryPoint elements with offsets and actions

**Implementation:** `os_xdm_parser.py:read_os_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_PARSER_00006 - Counter Parsing

The parser shall parse OsCounter elements from XDM.

- Extract OsCounterMaxAllowedValue, OsCounterMinCycle, OsCounterTicksPerBase, OsCounterType
- Extract optional fields: OsCounterSecondsPerTick, OsHwModule

**Implementation:** `os_xdm_parser.py:read_os_counters`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_PARSER_00007 - Application Parsing

The parser shall parse OsApplication elements from XDM.

- Extract OsTrusted, OsApplicationCoreAssignment
- Parse reference lists: OsAppTaskRef, OsAppIsrRef, OsAppAlarmRef, OsAppCounterRef, OsAppResourceRef
- Create task-to-application and ISR-to-application mappings

**Implementation:** `os_xdm_parser.py:read_os_applications`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_PARSER_00008 - Alarm Parsing

The parser shall parse OsAlarm elements from XDM.

- Extract OsAlarmCounterRef
- Parse OsAlarmAction choice element:
  - OsAlarmActivateTask
  - OsAlarmSetEvent
  - OsAlarmIncrementCounter
  - OsAlarmCallback
- Parse OsAlarmAutostart configuration
- Raise `ValueError` if alarm action is missing or unsupported

**Implementation:** `os_xdm_parser.py:read_os_alarms`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_PARSER_00009 - Resource Parsing

The parser shall parse OsResource elements from XDM.

- Extract OsResourceProperty
- Parse OsResourceAccessingApplicationRefs list
- Parse OsResourceLinkedResourceRefs list

**Implementation:** `os_xdm_parser.py:read_os_resources`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_PARSER_00010 - Event Parsing

The parser shall parse OsEvent elements from XDM.

- Extract OsEventMask value

**Implementation:** `os_xdm_parser.py:read_os_events`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_PARSER_00011 - Spinlock Parsing

The parser shall parse OsSpinlock elements from XDM.

- Extract OsSpinlockLockMethod
- Extract OsSpinlockSuccessor

**Implementation:** `os_xdm_parser.py:read_os_spinlocks`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_PARSER_00012 - Hooks Parsing

The parser shall parse OsHooks elements from XDM.

- Extract hook enable flags: OsStartupHook, OsShutdownHook, OsErrorHook, OsPreTaskHook, OsPostTaskHook

**Implementation:** `os_xdm_parser.py:read_os_hooks`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_PARSER_00013 - OS Configuration Parsing

The parser shall parse OsOS configuration elements from XDM.

- Extract OsScalabilityClass, OsUseOsApplication, OsUseGetServiceId
- Extract OsNumberOfCores, OsUseParameterAccess

**Implementation:** `os_xdm_parser.py:read_os_os`
**Status:** Implemented
**Last Validated:** 2026-05-26

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
| SWR_OS_PARSER_00009 | os_xdm_parser.py:read_os_resources | TC_UNIT_OS_00009 |
| SWR_OS_PARSER_00010 | os_xdm_parser.py:read_os_events | TC_UNIT_OS_00010 |
| SWR_OS_PARSER_00011 | os_xdm_parser.py:read_os_spinlocks | TC_UNIT_OS_00011 |
| SWR_OS_PARSER_00012 | os_xdm_parser.py:read_os_hooks | TC_UNIT_OS_00012 |
| SWR_OS_PARSER_00013 | os_xdm_parser.py:read_os_os | TC_UNIT_OS_00013 |
