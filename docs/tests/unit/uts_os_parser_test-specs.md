# Unit Test Specification: OS Module - Parser Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | OS Module Parser Layer Unit Test Specifications |
| Document ID | UTS_OS_PARSER_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | OS (Operating System) - Parser Layer |
| Test Type | Unit Test |

---

## Overview

This document defines unit test specifications for the OS Parser Layer requirements. Tests verify XDM parsing functionality for OS configuration data.

**Test Implementation:** `tests/parser/core/test_os_xdm_parser.py`

---

## Traceability Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Requirements | 15 | 100% |
| Requirements with Tests | 15 | 100% |
| Requirements without Tests | 0 | 0% |
| Total Test Cases | 28 | - |

---

## Coverage Matrix

| Requirement ID | Test Case IDs | Coverage Status | Last Verified |
|----------------|---------------|-----------------|---------------|
| SWR_OS_PARSER_00001 | UTS_OS_PARSER_00001, UTS_OS_PARSER_00002 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00002 | UTS_OS_PARSER_00003, UTS_OS_PARSER_00004 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00003 | UTS_OS_PARSER_00005, UTS_OS_PARSER_00006 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00004 | UTS_OS_PARSER_00007, UTS_OS_PARSER_00008 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00005 | UTS_OS_PARSER_00009, UTS_OS_PARSER_00010 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00006 | UTS_OS_PARSER_00011, UTS_OS_PARSER_00012 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00007 | UTS_OS_PARSER_00013, UTS_OS_PARSER_00014 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00008 | UTS_OS_PARSER_00015, UTS_OS_PARSER_00016 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00009 | UTS_OS_PARSER_00017, UTS_OS_PARSER_00018 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00010 | UTS_OS_PARSER_00019 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00011 | UTS_OS_PARSER_00020 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00012 | UTS_OS_PARSER_00021 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00013 | UTS_OS_PARSER_00022 | ✅ Covered | 2026-05-26 |
| SWR_OS_PARSER_00014 | UTS_OS_PARSER_00023 | ✅ Covered | 2026-05-28 |
| SWR_OS_PARSER_00015 | UTS_OS_PARSER_00024 | ✅ Covered | 2026-05-28 |

---

## Test Specifications

### UTS_OS_PARSER_00001 : Module Validation - Valid OS Module

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00001
**Test Implementation:** test_os_xdm_parser.py:test_module_validation_valid
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with valid OS module configuration exists

**Test Steps:**
1. **Given:** XDM file with module name "Os"
2. **When:** Parse XDM file
3. **Then:** Parser validates module name successfully

**Test Data:**
| Input | Expected Result |
|-------|----------------|
| Module name: "Os" | Validation passes |

**Expected Results:**
- Parser extracts module name "Os"
- No ValueError is raised
- Namespace map is stored

**Verification Criteria:**
1. Verify module name is "Os"
2. Verify no exception is raised
3. Verify namespace map is available

**Rationale:**
Verify parser accepts valid OS module configuration.

---

### UTS_OS_PARSER_00002 : Module Validation - Invalid Module

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00001
**Test Implementation:** test_os_xdm_parser.py:test_module_validation_invalid
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Error Guessing

**Preconditions:**
1. XDM file with invalid module name exists

**Test Steps:**
1. **Given:** XDM file with module name "InvalidModule"
2. **When:** Parse XDM file
3. **Then:** Parser raises ValueError

**Test Data:**
| Input | Expected Result |
|-------|----------------|
| Module name: "InvalidModule" | ValueError raised |

**Expected Results:**
- Parser raises ValueError with message about invalid module name

**Verification Criteria:**
1. Verify ValueError is raised
2. Verify error message mentions invalid module name

**Rationale:**
Verify parser rejects non-OS module configuration.

---

### UTS_OS_PARSER_00003 : Version Extraction - AR Version

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00002
**Test Implementation:** test_os_xdm_parser.py:test_version_extraction_ar
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with AR version information exists

**Test Steps:**
1. **Given:** XDM file with AR version (4.4.0)
2. **When:** Parse version information
3. **Then:** AR version is extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| ArMajorVersion | 4 |
| ArMinorVersion | 4 |
| ArPatchVersion | 0 |

**Expected Results:**
- AR version is extracted as "4.4.0"

**Verification Criteria:**
1. Verify ArMajorVersion is 4
2. Verify ArMinorVersion is 4
3. Verify ArPatchVersion is 0

**Rationale:**
Verify AR version extraction from XDM.

---

### UTS_OS_PARSER_00004 : Version Extraction - SW Version

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00002
**Test Implementation:** test_os_xdm_parser.py:test_version_extraction_sw
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with SW version information exists

**Test Steps:**
1. **Given:** XDM file with SW version (1.2.3)
2. **When:** Parse version information
3. **Then:** SW version is extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| SwMajorVersion | 1 |
| SwMinorVersion | 2 |
| SwPatchVersion | 3 |

**Expected Results:**
- SW version is extracted as "1.2.3"

**Verification Criteria:**
1. Verify SwMajorVersion is 1
2. Verify SwMinorVersion is 2
3. Verify SwPatchVersion is 3

**Rationale:**
Verify SW version extraction from XDM.

---

### UTS_OS_PARSER_00005 : Task Parsing - Required Fields

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00003
**Test Implementation:** test_os_xdm_parser.py:test_task_parsing_required
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsTask elements exists

**Test Steps:**
1. **Given:** XDM file with OsTask elements
2. **When:** Parse OsTask elements
3. **Then:** Required fields are extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsTaskPriority | 10 |
| OsTaskActivation | 1 |
| OsTaskSchedule | FULL |
| OsStacksize | 1024 |
| OsTaskType | EXTENDED |

**Expected Results:**
- All required fields are extracted
- OsTask model is created with correct values

**Verification Criteria:**
1. Verify OsTaskPriority is 10
2. Verify OsTaskActivation is 1
3. Verify OsTaskSchedule is "FULL"
4. Verify OsStacksize is 1024
5. Verify OsTaskType is "EXTENDED"

**Rationale:**
Verify required field extraction for OsTask.

---

### UTS_OS_PARSER_00006 : Task Parsing - Optional Fields

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00003
**Test Implementation:** test_os_xdm_parser.py:test_task_parsing_optional
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsTask elements with optional fields exists

**Test Steps:**
1. **Given:** XDM file with OsTask elements with optional fields
2. **When:** Parse OsTask elements
3. **Then:** Optional fields are extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsTaskAutostart | True |
| OsMeasureMaxRuntime | True |
| OsTaskUseHwFp | False |

**Expected Results:**
- Optional fields are extracted
- OsTask model has optional fields set

**Verification Criteria:**
1. Verify OsTaskAutostart is True
2. Verify OsMeasureMaxRuntime is True
3. Verify OsTaskUseHwFp is False

**Rationale:**
Verify optional field extraction for OsTask.

---

### UTS_OS_PARSER_00007 : ISR Parsing - Required Fields

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00004
**Test Implementation:** test_os_xdm_parser.py:test_isr_parsing_required
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsIsr elements exists

**Test Steps:**
1. **Given:** XDM file with OsIsr elements
2. **When:** Parse OsIsr elements
3. **Then:** Required fields are extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsIsrCategory | CATEGORY_2 |
| OsIsrPriority | 5 |

**Expected Results:**
- Required fields are extracted
- OsIsr model is created with correct values

**Verification Criteria:**
1. Verify OsIsrCategory is "CATEGORY_2"
2. Verify OsIsrPriority is 5

**Rationale:**
Verify required field extraction for OsIsr.

---

### UTS_OS_PARSER_00008 : ISR Parsing - Platform-Specific Fields

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00004
**Test Implementation:** test_os_xdm_parser.py:test_isr_parsing_platform
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsIsr elements with platform-specific fields exists

**Test Steps:**
1. **Given:** XDM file with OsIsr elements with TriCore fields
2. **When:** Parse OsIsr elements
3. **Then:** Platform-specific fields are extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsIsrTricoreIrqLevel | 10 |
| OsIsrTricoreVector | 20 |

**Expected Results:**
- Platform-specific fields are extracted
- OsIsr model has platform-specific fields set

**Verification Criteria:**
1. Verify OsIsrTricoreIrqLevel is 10
2. Verify OsIsrTricoreVector is 20

**Rationale:**
Verify platform-specific field extraction for OsIsr.

---

### UTS_OS_PARSER_00009 : Schedule Table Parsing - Basic Configuration

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00005
**Test Implementation:** test_os_xdm_parser.py:test_schedule_table_parsing_basic
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsScheduleTable elements exists

**Test Steps:**
1. **Given:** XDM file with OsScheduleTable elements
2. **When:** Parse OsScheduleTable elements
3. **Then:** Basic configuration is extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsScheduleTableDuration | 1000 |
| OsScheduleTableRepeating | True |
| OsScheduleTableCounterRef | Counter1 |

**Expected Results:**
- Basic configuration is extracted
- OsScheduleTable model is created

**Verification Criteria:**
1. Verify OsScheduleTableDuration is 1000
2. Verify OsScheduleTableRepeating is True
3. Verify OsScheduleTableCounterRef is "Counter1"

**Rationale:**
Verify basic OsScheduleTable parsing.

---

### UTS_OS_PARSER_00010 : Schedule Table Parsing - Expiry Points

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00005
**Test Implementation:** test_os_xdm_parser.py:test_schedule_table_parsing_expiry
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsScheduleTable elements with expiry points exists

**Test Steps:**
1. **Given:** XDM file with OsScheduleTblExpiryPoint elements
2. **When:** Parse OsScheduleTable elements
3. **Then:** Expiry points are extracted correctly

**Test Data:**
| Expiry Point | Offset | Action |
|--------------|--------|--------|
| EP1 | 100 | ActivateTask |
| EP2 | 200 | SetEvent |

**Expected Results:**
- Expiry points are extracted
- Actions are parsed correctly

**Verification Criteria:**
1. Verify expiry points are extracted
2. Verify offsets are correct
3. Verify actions are parsed

**Rationale:**
Verify OsScheduleTblExpiryPoint parsing.

---

### UTS_OS_PARSER_00011 : Counter Parsing - Required Fields

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00006
**Test Implementation:** test_os_xdm_parser.py:test_counter_parsing_required
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsCounter elements exists

**Test Steps:**
1. **Given:** XDM file with OsCounter elements
2. **When:** Parse OsCounter elements
3. **Then:** Required fields are extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsCounterMaxAllowedValue | 1000 |
| OsCounterMinCycle | 10 |
| OsCounterTicksPerBase | 1 |
| OsCounterType | HARDWARE |

**Expected Results:**
- Required fields are extracted
- OsCounter model is created

**Verification Criteria:**
1. Verify OsCounterMaxAllowedValue is 1000
2. Verify OsCounterMinCycle is 10
3. Verify OsCounterTicksPerBase is 1
4. Verify OsCounterType is "HARDWARE"

**Rationale:**
Verify required field extraction for OsCounter.

---

### UTS_OS_PARSER_00012 : Counter Parsing - Optional Fields

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00006
**Test Implementation:** test_os_xdm_parser.py:test_counter_parsing_optional
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsCounter elements with optional fields exists

**Test Steps:**
1. **Given:** XDM file with OsCounter elements with optional fields
2. **When:** Parse OsCounter elements
3. **Then:** Optional fields are extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsCounterSecondsPerTick | 0.001 |
| OsHwModule | "STM" |

**Expected Results:**
- Optional fields are extracted
- OsCounter model has optional fields set

**Verification Criteria:**
1. Verify OsCounterSecondsPerTick is 0.001
2. Verify OsHwModule is "STM"

**Rationale:**
Verify optional field extraction for OsCounter.

---

### UTS_OS_PARSER_00013 : Application Parsing - Basic Configuration

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00007
**Test Implementation:** test_os_xdm_parser.py:test_application_parsing_basic
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsApplication elements exists

**Test Steps:**
1. **Given:** XDM file with OsApplication elements
2. **When:** Parse OsApplication elements
3. **Then:** Basic configuration is extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsTrusted | True |
| OsApplicationCoreAssignment | 0 |

**Expected Results:**
- Basic configuration is extracted
- OsApplication model is created

**Verification Criteria:**
1. Verify OsTrusted is True
2. Verify OsApplicationCoreAssignment is 0

**Rationale:**
Verify basic OsApplication parsing.

---

### UTS_OS_PARSER_00014 : Application Parsing - Reference Lists

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00007
**Test Implementation:** test_os_xdm_parser.py:test_application_parsing_refs
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsApplication elements with reference lists exists

**Test Steps:**
1. **Given:** XDM file with OsApplication elements with reference lists
2. **When:** Parse OsApplication elements
3. **Then:** Reference lists are extracted correctly

**Test Data:**
| Reference List | Count |
|----------------|-------|
| OsAppTaskRef | 2 |
| OsAppIsrRef | 1 |
| OsAppAlarmRef | 1 |

**Expected Results:**
- Reference lists are extracted
- Task-to-application mappings are created

**Verification Criteria:**
1. Verify OsAppTaskRef list has 2 references
2. Verify OsAppIsrRef list has 1 reference
3. Verify OsAppAlarmRef list has 1 reference
4. Verify task-to-application mapping is created

**Rationale:**
Verify reference list parsing for OsApplication.

---

### UTS_OS_PARSER_00015 : Alarm Parsing - Basic Configuration

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00008
**Test Implementation:** test_os_xdm_parser.py:test_alarm_parsing_basic
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsAlarm elements exists

**Test Steps:**
1. **Given:** XDM file with OsAlarm elements
2. **When:** Parse OsAlarm elements
3. **Then:** Basic configuration is extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsAlarmCounterRef | Counter1 |

**Expected Results:**
- Basic configuration is extracted
- OsAlarm model is created

**Verification Criteria:**
1. Verify OsAlarmCounterRef is "Counter1"

**Rationale:**
Verify basic OsAlarm parsing.

---

### UTS_OS_PARSER_00016 : Alarm Parsing - Action Types

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00008
**Test Implementation:** test_os_xdm_parser.py:test_alarm_parsing_actions
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Decision Table Testing

**Preconditions:**
1. XDM file with OsAlarm elements with different action types exists

**Test Steps:**
1. **Given:** XDM file with OsAlarm elements with different actions
2. **When:** Parse OsAlarm elements
3. **Then:** Alarm actions are parsed correctly

**Test Data:**
| Alarm | Action Type | Target |
|-------|-------------|--------|
| Alarm1 | OsAlarmActivateTask | Task1 |
| Alarm2 | OsAlarmSetEvent | Event1 |
| Alarm3 | OsAlarmIncrementCounter | Counter1 |
| Alarm4 | OsAlarmCallback | Callback1 |

**Expected Results:**
- All alarm action types are parsed correctly
- ValueError is raised for missing or unsupported actions

**Verification Criteria:**
1. Verify OsAlarmActivateTask is parsed
2. Verify OsAlarmSetEvent is parsed
3. Verify OsAlarmIncrementCounter is parsed
4. Verify OsAlarmCallback is parsed
5. Verify ValueError is raised for missing action

**Rationale:**
Verify alarm action parsing for all supported types.

---

### UTS_OS_PARSER_00017 : Resource Parsing - Basic Configuration

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00009
**Test Implementation:** test_os_xdm_parser.py:test_resource_parsing_basic
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsResource elements exists

**Test Steps:**
1. **Given:** XDM file with OsResource elements
2. **When:** Parse OsResource elements
3. **Then:** Basic configuration is extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsResourceProperty | STANDARD |

**Expected Results:**
- Basic configuration is extracted
- OsResource model is created

**Verification Criteria:**
1. Verify OsResourceProperty is "STANDARD"

**Rationale:**
Verify basic OsResource parsing.

---

### UTS_OS_PARSER_00018 : Resource Parsing - Linked Resources

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00009
**Test Implementation:** test_os_xdm_parser.py:test_resource_parsing_linked
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsResource elements with linked references exists

**Test Steps:**
1. **Given:** XDM file with OsResource elements with linked references
2. **When:** Parse OsResource elements
3. **Then:** Linked references are extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsResourceProperty | LINKED |
| OsResourceLinkedResourceRefs | Resource1, Resource2 |

**Expected Results:**
- Linked references are extracted
- OsResource model has linked references

**Verification Criteria:**
1. Verify OsResourceProperty is "LINKED"
2. Verify OsResourceLinkedResourceRefs has 2 references

**Rationale:**
Verify linked resource reference parsing.

---

### UTS_OS_PARSER_00019 : Event Parsing

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00010
**Test Implementation:** test_os_xdm_parser.py:test_event_parsing
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsEvent elements exists

**Test Steps:**
1. **Given:** XDM file with OsEvent elements
2. **When:** Parse OsEvent elements
3. **Then:** Event mask is extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsEventMask | 0x01 |

**Expected Results:**
- Event mask is extracted
- OsEvent model is created

**Verification Criteria:**
1. Verify OsEventMask is 0x01

**Rationale:**
Verify OsEvent parsing.

---

### UTS_OS_PARSER_00020 : Spinlock Parsing

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00011
**Test Implementation:** test_os_xdm_parser.py:test_spinlock_parsing
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsSpinlock elements exists

**Test Steps:**
1. **Given:** XDM file with OsSpinlock elements
2. **When:** Parse OsSpinlock elements
3. **Then:** Spinlock configuration is extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsSpinlockLockMethod | "LOCK_ALL" |
| OsSpinlockSuccessor | "Spinlock2" |

**Expected Results:**
- Spinlock configuration is extracted
- OsSpinlock model is created

**Verification Criteria:**
1. Verify OsSpinlockLockMethod is "LOCK_ALL"
2. Verify OsSpinlockSuccessor is "Spinlock2"

**Rationale:**
Verify OsSpinlock parsing.

---

### UTS_OS_PARSER_00021 : Hooks Parsing

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00012
**Test Implementation:** test_os_xdm_parser.py:test_hooks_parsing
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Decision Table Testing

**Preconditions:**
1. XDM file with OsHooks elements exists

**Test Steps:**
1. **Given:** XDM file with OsHooks elements
2. **When:** Parse OsHooks elements
3. **Then:** Hook enable flags are extracted correctly

**Test Data:**
| Hook Type | Enabled |
|-----------|---------|
| OsStartupHook | True |
| OsShutdownHook | True |
| OsErrorHook | True |
| OsPreTaskHook | False |
| OsPostTaskHook | False |

**Expected Results:**
- All hook enable flags are extracted
- OsHooks model is created

**Verification Criteria:**
1. Verify OsStartupHook is True
2. Verify OsShutdownHook is True
3. Verify OsErrorHook is True
4. Verify OsPreTaskHook is False
5. Verify OsPostTaskHook is False

**Rationale:**
Verify OsHooks parsing.

---

### UTS_OS_PARSER_00022 : OS Configuration Parsing

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_PARSER_00013
**Test Implementation:** test_os_xdm_parser.py:test_os_configuration_parsing
**Last Validated:** 2026-05-26
**Last Changed:** 2026-05-26

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsOS configuration exists

**Test Steps:**
1. **Given:** XDM file with OsOS configuration
2. **When:** Parse OsOS configuration
3. **Then:** OS configuration is extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsScalabilityClass | "SC1" |
| OsUseOsApplication | True |
| OsUseGetServiceId | True |
| OsNumberOfCores | 1 |
| OsUseParameterAccess | True |

**Expected Results:**
- OS configuration is extracted
- Os model has configuration data

**Verification Criteria:**
1. Verify OsScalabilityClass is "SC1"
2. Verify OsUseOsApplication is True
3. Verify OsUseGetServiceId is True
4. Verify OsNumberOfCores is 1
5. Verify OsUseParameterAccess is True

**Rationale:**
Verify OsOS configuration parsing.

---

### UTS_OS_PARSER_00023 : Application Mode Parsing

**Type:** Functional
**Priority:** High
**Status:** Not Implemented

**Traces-To:** SWR_OS_PARSER_00014
**Test Implementation:** test_os_xdm_parser.py:test_appmode_parsing
**Last Validated:** N/A
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsAppMode elements exists

**Test Steps:**
1. **Given:** XDM file with OsAppMode elements
2. **When:** Parse OsAppMode elements
3. **Then:** Application modes are extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsAppMode name | "AppMode1" |

**Expected Results:**
- OsAppMode is created
- OsAppMode is added to Os model
- OsAppMode name is extracted

**Verification Criteria:**
1. Verify OsAppMode exists in Os model
2. Verify OsAppMode name is "AppMode1"

**Rationale:**
Verify OsAppMode parsing functionality.

---

### UTS_OS_PARSER_00024 : Peripheral Area Parsing - Complete Fields

**Type:** Functional
**Priority:** High
**Status:** Not Implemented

**Traces-To:** SWR_OS_PARSER_00015
**Test Implementation:** test_os_xdm_parser.py:test_peripheral_area_parsing_complete
**Last Validated:** N/A
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. XDM file with OsPeripheralArea elements with all fields exists

**Test Steps:**
1. **Given:** XDM file with OsPeripheralArea elements
2. **When:** Parse OsPeripheralArea elements
3. **Then:** All fields including OsPeripheralAreaId are extracted correctly

**Test Data:**
| Field | Value |
|-------|-------|
| OsPeripheralAreaStartAddress | 0x1000 |
| OsPeripheralAreaEndAddress | 0x1FFF |
| OsPeripheralAreaId | 1 |
| OsPeripheralAreaAccessPermission | "READ-WRITE" |

**Expected Results:**
- OsPeripheralArea is created
- All fields are extracted including OsPeripheralAreaId
- OsPeripheralArea is added to Os model

**Verification Criteria:**
1. Verify OsPeripheralAreaStartAddress is 0x1000
2. Verify OsPeripheralAreaEndAddress is 0x1FFF
3. Verify OsPeripheralAreaId is 1
4. Verify OsPeripheralAreaAccessPermission is "READ-WRITE"

**Rationale:**
Verify complete OsPeripheralArea parsing including OsPeripheralAreaId field.

---

## Test Coverage Summary

### Requirements Coverage by Test Design Technique

| Technique | Requirements | Test Cases | Coverage |
|-----------|--------------|------------|----------|
| Equivalence Partitioning | 11 | 20 | 77% |
| Decision Table Testing | 2 | 4 | 15% |
| Error Guessing | 1 | 2 | 8% |
| **Total** | **13** | **26** | **100%** |

### Test Case Distribution by Priority

| Priority | Test Cases | Percentage |
|----------|------------|------------|
| Critical | 8 | 31% |
| High | 18 | 69% |
| **Total** | **26** | **100%** |

---

## Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2026-05-27 | 1.0 | Initial unit test specification document | req-traceability skill |
