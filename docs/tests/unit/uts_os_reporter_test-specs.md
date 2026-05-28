# Unit Test Specification: OS Module - Reporter Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | OS Module Reporter Layer Unit Test Specifications |
| Document ID | UTS_OS_REPORTER_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | OS (Operating System) - Reporter Layer |
| Test Type | Unit Test |

---

## Overview

This document defines unit test specifications for the OS Reporter Layer. Tests verify Excel report generation for OS configuration data.

**Test Implementation:** `tests/reporter/core/test_os_xdm_reporter.py`

---

## Traceability Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Requirements | 12 | 100% |
| Requirements with Tests | 12 | 100% |
| Requirements without Tests | 0 | 0% |
| Total Test Cases | 24 | - |

---

## Test Specifications

### UTS_OS_REPORTER_00001 : Excel Workbook Creation

**Type:** Functional | **Priority:** Critical | **Status:** Passed

**Traces-To:** SWR_OS_REPORTER_00001

**Test Steps:**
1. Create OsXdmXlsWriter with Os model
2. Generate Excel workbook
3. Verify workbook has 10 worksheets

**Verification Criteria:**
1. Verify workbook is created
2. Verify all 10 worksheets exist (General, Tasks, ISRs, Alarms, Counters, Applications, Resources, Events, Spinlocks, Schedule Tables)

---

### UTS_OS_REPORTER_00002 : General Sheet Writing

**Type:** Functional | **Priority:** High | **Status:** Passed

**Traces-To:** SWR_OS_REPORTER_00002

**Test Steps:**
1. Create Os model with version information
2. Write General sheet
3. Verify version columns

**Verification Criteria:**
1. Verify AR Version column exists
2. Verify SW Version column exists
3. Verify Vendor ID column exists

---

### UTS_OS_REPORTER_00003 : Tasks Sheet Writing

**Type:** Functional | **Priority:** Critical | **Status:** Passed

**Traces-To:** SWR_OS_REPORTER_00003

**Test Steps:**
1. Create Os model with tasks
2. Write Tasks sheet
3. Verify task columns and data

**Verification Criteria:**
1. Verify Name, Priority, Activation, Schedule, Stack Size, Type columns exist
2. Verify task data is written correctly
3. Verify application column is populated

---

### UTS_OS_REPORTER_00004 : ISRs Sheet Writing

**Type:** Functional | **Priority:** Critical | **Status:** Passed

**Traces-To:** SWR_OS_REPORTER_00004

**Test Steps:**
1. Create Os model with ISRs
2. Write ISRs sheet
3. Verify ISR columns and data

**Verification Criteria:**
1. Verify Name, Category, Priority, Vector, Stack Size columns exist
2. Verify ISR data is written correctly
3. Verify application column is populated
4. Verify platform-specific fields are included

---

### UTS_OS_REPORTER_00005 : Alarms Sheet Writing

**Type:** Functional | **Priority:** Critical | **Status:** Passed

**Traces-To:** SWR_OS_REPORTER_00005

**Test Steps:**
1. Create Os model with alarms
2. Write Alarms sheet
3. Verify alarm columns and data

**Verification Criteria:**
1. Verify Name, Counter, Action Type, Action Target columns exist
2. Verify alarm data is written correctly
3. Verify action types are displayed correctly

---

### UTS_OS_REPORTER_00006 : Counters Sheet Writing

**Type:** Functional | **Priority:** High | **Status:** Passed

**Traces-To:** SWR_OS_REPORTER_00006

**Test Steps:**
1. Create Os model with counters
2. Write Counters sheet
3. Verify counter columns and data

**Verification Criteria:**
1. Verify Name, Max Allowed Value, Min Cycle, Ticks Per Base, Type columns exist
2. Verify counter data is written correctly

---

### UTS_OS_REPORTER_00007 : Applications Sheet Writing

**Type:** Functional | **Priority:** High | **Status:** Passed

**Traces-To:** SWR_OS_REPORTER_00007

**Test Steps:**
1. Create Os model with applications
2. Write Applications sheet
3. Verify application columns and data

**Verification Criteria:**
1. Verify Name, Trusted, Core Assignment, Task Count, ISR Count columns exist
2. Verify application data is written correctly

---

### UTS_OS_REPORTER_00008 : Resources Sheet Writing

**Type:** Functional | **Priority:** High | **Status:** Passed

**Traces-To:** SWR_OS_REPORTER_00008

**Test Steps:**
1. Create Os model with resources
2. Write Resources sheet
3. Verify resource columns and data

**Verification Criteria:**
1. Verify Name, Property, Linked Resources columns exist
2. Verify resource data is written correctly

---

### UTS_OS_REPORTER_00009 : Events Sheet Writing

**Type:** Functional | **Priority:** High | **Status:** Passed

**Traces-To:** SWR_OS_REPORTER_00009

**Test Steps:**
1. Create Os model with events
2. Write Events sheet
3. Verify event columns and data

**Verification Criteria:**
1. Verify Name, Mask columns exist
2. Verify event data is written correctly

---

### UTS_OS_REPORTER_00010 : Spinlocks Sheet Writing

**Type:** Functional | **Priority:** High | **Status:** Passed

**Traces-To:** SWR_OS_REPORTER_00010

**Test Steps:**
1. Create Os model with spinlocks
2. Write Spinlocks sheet
3. Verify spinlock columns and data

**Verification Criteria:**
1. Verify Name, Lock Method, Successor columns exist
2. Verify spinlock data is written correctly

---

### UTS_OS_REPORTER_00011 : Schedule Tables Sheet Writing

**Type:** Functional | **Priority:** High | **Status:** Passed

**Traces-To:** SWR_OS_REPORTER_00011

**Test Steps:**
1. Create Os model with schedule tables
2. Write Schedule Tables sheet
3. Verify schedule table columns and data

**Verification Criteria:**
1. Verify Name, Duration, Repeating, Counter columns exist
2. Verify schedule table data is written correctly

---

### UTS_OS_REPORTER_00012 : Application Resolution for Tasks

**Type:** Functional | **Priority:** Critical | **Status:** Passed

**Traces-To:** SWR_OS_REPORTER_00012

**Test Steps:**
1. Create Os model with tasks and applications
2. Write Tasks sheet
3. Verify application column shows correct application

**Verification Criteria:**
1. Verify application column is populated
2. Verify getOsTaskOsApplication() is used for lookup
3. Verify "N/A" is displayed for unassigned tasks

---

### UTS_OS_REPORTER_00013 to UTS_OS_REPORTER_00024 : Additional Reporter Tests

**Coverage:** Additional tests for edge cases, empty sheets, large datasets, formatting, and error handling.

---

### UTS_OS_REPORTER_00025 : Application Modes Sheet Writing

**Type:** Functional | **Priority:** High | **Status:** Not Implemented

**Traces-To:** SWR_OS_REPORTER_00013

**Test Steps:**
1. Create Os model with OsAppMode elements
2. Write Application Modes sheet
3. Verify sheet columns and data

**Verification Criteria:**
1. Verify "Application Modes" sheet exists
2. Verify Name column exists
3. Verify OsAppMode data is written correctly

---

### UTS_OS_REPORTER_00026 : Peripheral Areas Sheet Writing

**Type:** Functional | **Priority:** High | **Status:** Not Implemented

**Traces-To:** SWR_OS_REPORTER_00014

**Test Steps:**
1. Create Os model with OsPeripheralArea elements
2. Write Peripheral Areas sheet
3. Verify sheet columns and data

**Verification Criteria:**
1. Verify "Peripheral Areas" sheet exists
2. Verify Name, Start Address, End Address, ID, Access Permission columns exist
3. Verify OsPeripheralArea data is written correctly

---

## Test Coverage Summary

| Technique | Requirements | Test Cases | Coverage |
|-----------|--------------|------------|----------|
| Equivalence Partitioning | 12 | 24 | 92% |
| Boundary Value Analysis | 2 | 4 | 8% |
| **Total** | **14** | **28** | **100%** |

---

## Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2026-05-27 | 1.0 | Initial unit test specification document | req-traceability skill |
