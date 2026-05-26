# Software Requirements: OS Module - Reporter Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | OS Module Reporter Layer Requirements |
| Document ID | SWR_OS_REPORTER_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | OS (Operating System) - Reporter Layer |

---

## Overview

The OS Reporter Layer provides Excel export functionality for AUTOSAR OS configuration data.

**Implementation:** `src/eb_model/reporter/excel_reporter/core/os_xdm.py`

---

## Requirements

### SWR_OS_REPORTER_00001 - Excel Workbook Creation

The reporter shall create an Excel workbook with multiple worksheets for OS configuration.

**Worksheets:**
1. General - Version information
2. Tasks - Task configuration
3. ISRs - ISR configuration
4. Alarms - Alarm configuration
5. Counters - Counter configuration
6. Applications - Application configuration
7. Resources - Resource configuration
8. Events - Event configuration
9. Spinlocks - Spinlock configuration
10. Schedule Tables - Schedule table configuration

**Implementation:** `os_xdm.py:OsXdmXlsWriter`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_REPORTER_00002 - General Sheet

The reporter shall write version information to the General worksheet.

**Columns:**
- AR Version (Major.Minor.Patch)
- SW Version (Major.Minor.Patch)
- Vendor ID

**Implementation:** `os_xdm.py:write_general`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_REPORTER_00003 - Tasks Sheet

The reporter shall write task configuration to the Tasks worksheet.

**Columns:**
- Name
- Priority
- Activation
- Schedule
- Stack Size
- Type
- Autostart
- Application (resolved from task-to-application mapping)

**Implementation:** `os_xdm.py:write_tasks`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_REPORTER_00004 - ISRs Sheet

The reporter shall write ISR configuration to the ISRs worksheet.

**Columns:**
- Name
- Category
- Priority
- Vector
- Stack Size
- Application (resolved from ISR-to-application mapping)
- Platform-specific fields (TriCore/ARM)

**Implementation:** `os_xdm.py:write_isrs`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_REPORTER_00005 - Alarms Sheet

The reporter shall write alarm configuration to the Alarms worksheet.

**Columns:**
- Name
- Counter
- Action Type
- Action Target (task/event/counter/callback)
- Autostart
- Application

**Implementation:** `os_xdm.py:write_alarms`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_REPORTER_00006 - Counters Sheet

The reporter shall write counter configuration to the Counters worksheet.

**Columns:**
- Name
- Max Allowed Value
- Min Cycle
- Ticks Per Base
- Type
- Seconds Per Tick

**Implementation:** `os_xdm.py:write_counters`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_REPORTER_00007 - Applications Sheet

The reporter shall write application configuration to the Applications worksheet.

**Columns:**
- Name
- Trusted
- Core Assignment
- Task Count
- ISR Count
- Alarm Count
- Resource Count

**Implementation:** `os_xdm.py:write_applications`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_REPORTER_00008 - Resources Sheet

The reporter shall write resource configuration to the Resources worksheet.

**Columns:**
- Name
- Property
- Linked Resources
- Accessing Applications

**Implementation:** `os_xdm.py:write_resources`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_REPORTER_00009 - Events Sheet

The reporter shall write event configuration to the Events worksheet.

**Columns:**
- Name
- Mask

**Implementation:** `os_xdm.py:write_events`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_REPORTER_00010 - Spinlocks Sheet

The reporter shall write spinlock configuration to the Spinlocks worksheet.

**Columns:**
- Name
- Lock Method
- Successor

**Implementation:** `os_xdm.py:write_spinlocks`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_REPORTER_00011 - Schedule Tables Sheet

The reporter shall write schedule table configuration to the Schedule Tables worksheet.

**Columns:**
- Name
- Duration
- Repeating
- Counter
- Expiry Points (count)

**Implementation:** `os_xdm.py:write_schedule_tables`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

### SWR_OS_REPORTER_00012 - Application Resolution

The reporter shall resolve task and ISR application assignments.

- Use O(1) lookup via `getOsTaskOsApplication()` and `getOsIsrOsApplication()`
- Display "N/A" if task/ISR is not assigned to any application

**Implementation:** `os_xdm.py:write_tasks`, `os_xdm.py:write_isrs`
**Status:** Implemented
**Last Validated:** 2026-05-26

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_OS_REPORTER_00001 | os_xdm.py:OsXdmXlsWriter | TC_UNIT_OS_RPT_00001 |
| SWR_OS_REPORTER_00002 | os_xdm.py:write_general | TC_UNIT_OS_RPT_00002 |
| SWR_OS_REPORTER_00003 | os_xdm.py:write_tasks | TC_UNIT_OS_RPT_00003 |
| SWR_OS_REPORTER_00004 | os_xdm.py:write_isrs | TC_UNIT_OS_RPT_00004 |
| SWR_OS_REPORTER_00005 | os_xdm.py:write_alarms | TC_UNIT_OS_RPT_00005 |
| SWR_OS_REPORTER_00006 | os_xdm.py:write_counters | TC_UNIT_OS_RPT_00006 |
| SWR_OS_REPORTER_00007 | os_xdm.py:write_applications | TC_UNIT_OS_RPT_00007 |
| SWR_OS_REPORTER_00008 | os_xdm.py:write_resources | TC_UNIT_OS_RPT_00008 |
| SWR_OS_REPORTER_00009 | os_xdm.py:write_events | TC_UNIT_OS_RPT_00009 |
| SWR_OS_REPORTER_00010 | os_xdm.py:write_spinlocks | TC_UNIT_OS_RPT_00010 |
| SWR_OS_REPORTER_00011 | os_xdm.py:write_schedule_tables | TC_UNIT_OS_RPT_00011 |
| SWR_OS_REPORTER_00012 | os_xdm.py:write_tasks | TC_UNIT_OS_RPT_00012 |
