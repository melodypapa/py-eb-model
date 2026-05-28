# Unit Test Specification: OS Module - Model Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | OS Module Model Layer Unit Test Specifications |
| Document ID | UTS_OS_MODELS_00001 |
| Version | 1.1 |
| Date | 2026-05-28 |
| Project | py-eb-model |
| Module | OS (Operating System) - Model Layer |
| Test Type | Unit Test |

---

## Overview

This document defines unit test specifications for the OS Model Layer requirements. Tests verify individual model classes and their methods in isolation.

**Test Implementation:** `tests/models/core/test_os_xdm.py`

---

## Traceability Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Requirements | 12 | 100% |
| Requirements with Tests | 12 | 100% |
| Requirements without Tests | 0 | 0% |
| Total Test Cases | 36 | - |

---

## Coverage Matrix

| Requirement ID | Test Case IDs | Coverage Status | Last Verified |
|----------------|---------------|-----------------|---------------|
| SWR_OS_MODELS_00001 | UTS_OS_MODEL_00001, UTS_OS_MODEL_00002, UTS_OS_MODEL_00003 | ✅ Covered | 2026-05-28 |
| SWR_OS_MODELS_00002 | UTS_OS_MODEL_00004 | ✅ Covered | 2026-05-28 |
| SWR_OS_MODELS_00003 | UTS_OS_MODEL_00005, UTS_OS_MODEL_00006, UTS_OS_MODEL_00007 | ✅ Covered | 2026-05-28 |
| SWR_OS_MODELS_00004 | UTS_OS_MODEL_00008, UTS_OS_MODEL_00009, UTS_OS_MODEL_00010 | ✅ Covered | 2026-05-28 |
| SWR_OS_MODELS_00005 | UTS_OS_MODEL_00011 | ✅ Covered | 2026-05-28 |
| SWR_OS_MODELS_00006 | UTS_OS_MODEL_00012, UTS_OS_MODEL_00013 | ✅ Covered | 2026-05-28 |
| SWR_OS_MODELS_00007 | UTS_OS_MODEL_00014, UTS_OS_MODEL_00015, UTS_OS_MODEL_00016 | ✅ Covered | 2026-05-28 |
| SWR_OS_MODELS_00008 | UTS_OS_MODEL_00017, UTS_OS_MODEL_00018, UTS_OS_MODEL_00019 | ✅ Covered | 2026-05-28 |
| SWR_OS_MODELS_00009 | UTS_OS_MODEL_00020, UTS_OS_MODEL_00021 | ✅ Covered | 2026-05-28 |
| SWR_OS_MODELS_00010 | UTS_OS_MODEL_00022, UTS_OS_MODEL_00023 | ✅ Covered | 2026-05-28 |
| SWR_OS_MODELS_00011 | UTS_OS_MODEL_00024, UTS_OS_MODEL_00025, UTS_OS_MODEL_00026 | ✅ Covered | 2026-05-28 |
| SWR_OS_MODELS_00012 | UTS_OS_MODEL_00027, UTS_OS_MODEL_00028, UTS_OS_MODEL_00029 | ✅ Covered | 2026-05-28 |

---

## Test Specifications

### UTS_OS_MODEL_00001 : OsAlarm Model Initialization

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00001
**Test Implementation:** test_os_xdm.py:test_osalarm_initialization
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsAlarm class is imported from eb_model.models.core.os_xdm

**Test Steps:**
1. **Given:** No OsAlarm instance exists
2. **When:** Create OsAlarm with name "Alarm1"
3. **Then:** OsAlarm instance is created with default values

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| name | "Alarm1" | Alarm name |

**Expected Results:**
- OsAlarm instance is not None
- getName() returns "Alarm1"
- OsAlarmAccessingApplication is empty list
- OsAlarmCounterRef is None

**Verification Criteria:**
1. Verify OsAlarm instance is created successfully
2. Verify name is set correctly
3. Verify default field values

**Rationale:**
Verify basic OsAlarm model initialization with minimal parameters.

---

### UTS_OS_MODEL_00002 : OsAlarm Accessing Application References

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00001
**Test Implementation:** test_os_xdm.py:test_osalarm_accessing_application
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsAlarm instance exists

**Test Steps:**
1. **Given:** OsAlarm with empty accessing application list
2. **When:** Add multiple application references
3. **Then:** Application references are stored correctly

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| ref1 | EcucRefType("/Os/App1") | First application reference |
| ref2 | EcucRefType("/Os/App2") | Second application reference |

**Expected Results:**
- getOsAlarmAccessingApplicationRefList() returns list with 2 references
- References are in correct order

**Verification Criteria:**
1. Verify application references are added correctly
2. Verify list contains all added references
3. Verify getOsAlarmAccessingApplicationRefList() returns correct count

**Rationale:**
Verify OsAlarmAccessingApplication field stores multiple references.

---

### UTS_OS_MODEL_00003 : OsAlarm Counter Reference

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00001
**Test Implementation:** test_os_xdm.py:test_osalarm_counter_ref
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsAlarm instance exists

**Test Steps:**
1. **Given:** OsAlarm with no counter reference
2. **When:** Set counter reference
3. **Then:** Counter reference is stored correctly

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| counterRef | EcucRefType("/Os/Counter1") | Counter reference |

**Expected Results:**
- getOsAlarmCounterRef() returns correct reference
- Reference points to correct counter

**Verification Criteria:**
1. Verify counter reference is set correctly
2. Verify getOsAlarmCounterRef() returns expected value

**Rationale:**
Verify OsAlarmCounterRef field stores counter reference.

---

### UTS_OS_MODEL_00004 : OsAppMode Model Initialization

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00002
**Test Implementation:** test_os_xdm.py:test_osappmode_initialization
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsAppMode class is imported from eb_model.models.core.os_xdm

**Test Steps:**
1. **Given:** No OsAppMode instance exists
2. **When:** Create OsAppMode with name "AppMode1"
3. **Then:** OsAppMode instance is created with default values

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| name | "AppMode1" | Application mode name |

**Expected Results:**
- OsAppMode instance is not None
- getName() returns "AppMode1"

**Verification Criteria:**
1. Verify OsAppMode instance is created successfully
2. Verify name is set correctly

**Rationale:**
Verify basic OsAppMode model initialization.

---

### UTS_OS_MODEL_00005 : OsApplication Model Initialization

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00003
**Test Implementation:** test_os_xdm.py:test_osapplication_initialization
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsApplication class is imported from eb_model.models.core.os_xdm

**Test Steps:**
1. **Given:** No OsApplication instance exists
2. **When:** Create OsApplication with name "App1"
3. **Then:** OsApplication instance is created with default values

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| name | "App1" | Application name |

**Expected Results:**
- OsApplication instance is not None
- getName() returns "App1"
- OsTrusted is False
- All reference lists are empty

**Verification Criteria:**
1. Verify OsApplication instance is created successfully
2. Verify name is set correctly
3. Verify default field values

**Rationale:**
Verify basic OsApplication model initialization.

---

### UTS_OS_MODEL_00006 : OsApplication Trusted Flags

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00003
**Test Implementation:** test_os_xdm.py:test_osapplication_trusted_flags
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Decision Table Testing

**Preconditions:**
1. OsApplication instance exists

**Test Steps:**
1. **Given:** OsApplication with default trusted flags
2. **When:** Set trusted flag combinations
3. **Then:** Trusted flags are stored correctly

**Test Data:**
| OsTrusted | OsTrustedApplicationWithProtection | OsTrustedApplicationDelayTimingViolationCall |
|-----------|-------------------------------------|---------------------------------------------|
| True | False | False |
| True | True | False |
| True | True | True |
| False | False | False |

**Expected Results:**
- All flag combinations are accepted
- Flags are stored correctly

**Verification Criteria:**
1. Verify OsTrusted flag is set correctly
2. Verify OsTrustedApplicationWithProtection flag is set correctly
3. Verify OsTrustedApplicationDelayTimingViolationCall flag is set correctly

**Rationale:**
Verify OsApplication trusted flag combinations.

---

### UTS_OS_MODEL_00007 : OsApplication Reference Lists

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00003
**Test Implementation:** test_os_xdm.py:test_osapplication_reference_lists
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsApplication instance exists

**Test Steps:**
1. **Given:** OsApplication with empty reference lists
2. **When:** Add references to all lists
3. **Then:** References are stored correctly

**Test Data:**
| List Type | Reference |
|-----------|-----------|
| OsAppTaskRef | EcucRefType("/Os/Task1") |
| OsAppIsrRef | EcucRefType("/Os/ISR1") |
| OsAppCounterRef | EcucRefType("/Os/Counter1") |
| OsAppAlarmRef | EcucRefType("/Os/Alarm1") |
| OsAppScheduleTableRef | EcucRefType("/Os/ScheduleTable1") |
| OsAppResourceRef | EcucRefType("/Os/Resource1") |

**Expected Results:**
- All reference lists contain added references
- Each list maintains correct count

**Verification Criteria:**
1. Verify OsAppTaskRef list contains added reference
2. Verify OsAppIsrRef list contains added reference
3. Verify OsAppCounterRef list contains added reference
4. Verify OsAppAlarmRef list contains added reference
5. Verify OsAppScheduleTableRef list contains added reference
6. Verify OsAppResourceRef list contains added reference

**Rationale:**
Verify OsApplication reference list fields.

---

### UTS_OS_MODEL_00008 : OsCounter Model Initialization

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00004
**Test Implementation:** test_os_xdm.py:test_oscounter_initialization
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsCounter class is imported from eb_model.models.core.os_xdm

**Test Steps:**
1. **Given:** No OsCounter instance exists
2. **When:** Create OsCounter with name "Counter1"
3. **Then:** OsCounter instance is created with default values

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| name | "Counter1" | Counter name |

**Expected Results:**
- OsCounter instance is not None
- getName() returns "Counter1"
- OsCounterMaxAllowedValue is None
- OsCounterMinCycle is None
- OsCounterTicksPerBase is None

**Verification Criteria:**
1. Verify OsCounter instance is created successfully
2. Verify name is set correctly
3. Verify default field values

**Rationale:**
Verify basic OsCounter model initialization.

---

### UTS_OS_MODEL_00009 : OsCounter Boundary Values

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00004
**Test Implementation:** test_os_xdm.py:test_oscounter_boundary_values
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Boundary Value Analysis

**Preconditions:**
1. OsCounter instance exists

**Test Steps:**
1. **Given:** OsCounter with default values
2. **When:** Set boundary values for MaxAllowedValue and TicksPerBase
3. **Then:** Values are stored correctly

**Test Data:**
| Field | Min Value | Max Value |
|-------|-----------|-----------|
| OsCounterMaxAllowedValue | 1 | 4294967295 |
| OsCounterTicksPerBase | 1 | 4294967295 |
| OsWindowsIrqLevel | 1 | 32 |

**Expected Results:**
- All boundary values are accepted
- Values are stored correctly

**Verification Criteria:**
1. Verify OsCounterMaxAllowedValue accepts min (1) and max (4294967295)
2. Verify OsCounterTicksPerBase accepts min (1) and max (4294967295)
3. Verify OsWindowsIrqLevel accepts min (1) and max (32)

**Rationale:**
Test boundary values for OsCounter fields.

---

### UTS_OS_MODEL_00010 : OsCounter Type Enumeration

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00004
**Test Implementation:** test_os_xdm.py:test_oscounter_type
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsCounter instance exists

**Test Steps:**
1. **Given:** OsCounter with no type
2. **When:** Set OsCounterType to HARDWARE and SOFTWARE
3. **Then:** Type is stored correctly

**Test Data:**
| OsCounterType | Description |
|---------------|-------------|
| HARDWARE | Hardware counter |
| SOFTWARE | Software counter |

**Expected Results:**
- Both types are accepted
- getOsCounterType() returns correct value

**Verification Criteria:**
1. Verify HARDWARE type is set correctly
2. Verify SOFTWARE type is set correctly

**Rationale:**
Verify OsCounterType enumeration field.

---

### UTS_OS_MODEL_00011 : OsEvent Model Initialization

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00005
**Test Implementation:** test_os_xdm.py:test_osevent_initialization
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsEvent class is imported from eb_model.models.core.os_xdm

**Test Steps:**
1. **Given:** No OsEvent instance exists
2. **When:** Create OsEvent with name "Event1"
3. **Then:** OsEvent instance is created with default values

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| name | "Event1" | Event name |

**Expected Results:**
- OsEvent instance is not None
- getName() returns "Event1"

**Verification Criteria:**
1. Verify OsEvent instance is created successfully
2. Verify name is set correctly

**Rationale:**
Verify basic OsEvent model initialization.

---

### UTS_OS_MODEL_00012 : OsSpinlock Model Initialization

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00006
**Test Implementation:** test_os_xdm.py:test_ospinlock_initialization
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsSpinlock class is imported from eb_model.models.core.os_xdm

**Test Steps:**
1. **Given:** No OsSpinlock instance exists
2. **When:** Create OsSpinlock with name "Spinlock1"
3. **Then:** OsSpinlock instance is created with default values

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| name | "Spinlock1" | Spinlock name |

**Expected Results:**
- OsSpinlock instance is not None
- getName() returns "Spinlock1"
- OsSpinlockLockMethod is None
- OsSpinlockSuccessor is None

**Verification Criteria:**
1. Verify OsSpinlock instance is created successfully
2. Verify name is set correctly
3. Verify default field values

**Rationale:**
Verify basic OsSpinlock model initialization.

---

### UTS_OS_MODEL_00013 : OsSpinlock Lock Method

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00006
**Test Implementation:** test_os_xdm.py:test_ospinlock_lock_method
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsSpinlock instance exists

**Test Steps:**
1. **Given:** OsSpinlock with no lock method
2. **When:** Set different lock methods
3. **Then:** Lock method is stored correctly

**Test Data:**
| OsSpinlockLockMethod | Description |
|---------------------|-------------|
| LOCK_NOTHING | No locking |
| LOCK_ALL_INTERRUPTS | Lock all interrupts |
| LOCK_CAT2_INTERRUPTS | Lock category 2 interrupts |
| LOCK_WITH_RES_SCHEDULER | Lock with resource scheduler |

**Expected Results:**
- All lock methods are accepted
- getOsSpinlockLockMethod() returns correct value

**Verification Criteria:**
1. Verify LOCK_NOTHING is set correctly
2. Verify LOCK_ALL_INTERRUPTS is set correctly
3. Verify LOCK_CAT2_INTERRUPTS is set correctly
4. Verify LOCK_WITH_RES_SCHEDULER is set correctly

**Rationale:**
Verify OsSpinlockLockMethod enumeration field.

---

### UTS_OS_MODEL_00014 : OsIsr Model Initialization

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00007
**Test Implementation:** test_os_xdm.py:test_osisr_initialization
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsIsr class is imported from eb_model.models.core.os_xdm

**Test Steps:**
1. **Given:** No OsIsr instance exists
2. **When:** Create OsIsr with name "ISR1"
3. **Then:** OsIsr instance is created with default values

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| name | "ISR1" | ISR name |

**Expected Results:**
- OsIsr instance is not None
- getName() returns "ISR1"
- OsIsrCategory is None
- OsStacksize is None

**Verification Criteria:**
1. Verify OsIsr instance is created successfully
2. Verify name is set correctly
3. Verify default field values

**Rationale:**
Verify basic OsIsr model initialization.

---

### UTS_OS_MODEL_00015 : OsIsr Category

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00007
**Test Implementation:** test_os_xdm.py:test_osisr_category
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsIsr instance exists

**Test Steps:**
1. **Given:** OsIsr with no category
2. **When:** Set OsIsrCategory to CATEGORY_1 and CATEGORY_2
3. **Then:** Category is stored correctly

**Test Data:**
| OsIsrCategory | Description |
|---------------|-------------|
| CATEGORY_1 | Category 1 ISR |
| CATEGORY_2 | Category 2 ISR |

**Expected Results:**
- Both categories are accepted
- getOsIsrCategory() returns correct value

**Verification Criteria:**
1. Verify CATEGORY_1 is set correctly
2. Verify CATEGORY_2 is set correctly

**Rationale:**
Verify OsIsrCategory enumeration field.

---

### UTS_OS_MODEL_00016 : OsIsr Stack Size

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00007
**Test Implementation:** test_os_xdm.py:test_osisr_stacksize
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Boundary Value Analysis

**Preconditions:**
1. OsIsr instance exists

**Test Steps:**
1. **Given:** OsIsr with no stack size
2. **When:** Set OsStacksize to boundary values
3. **Then:** Stack size is stored correctly

**Test Data:**
| OsStacksize | Description |
|-------------|-------------|
| 0 | Minimum value |
| 1024 | Typical small stack |
| 4096 | Typical medium stack |
| 2000000000 | Maximum value |

**Expected Results:**
- All values are accepted
- getOsStacksize() returns correct value

**Verification Criteria:**
1. Verify stack size 0 is accepted
2. Verify stack size 1024 is accepted
3. Verify stack size 4096 is accepted
4. Verify stack size 2000000000 is accepted

**Rationale:**
Verify OsStacksize field with boundary values.

---

### UTS_OS_MODEL_00017 : OsTask Model Initialization

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00008
**Test Implementation:** test_os_xdm.py:test_ostask_initialization
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsTask class is imported from eb_model.models.core.os_xdm

**Test Steps:**
1. **Given:** No OsTask instance exists
2. **When:** Create OsTask with name "Task1"
3. **Then:** OsTask instance is created with default values

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| name | "Task1" | Task name |

**Expected Results:**
- OsTask instance is not None
- getName() returns "Task1"
- OsTaskActivation is None
- OsTaskPriority is None
- OsTaskSchedule is None

**Verification Criteria:**
1. Verify OsTask instance is created successfully
2. Verify name is set correctly
3. Verify default field values

**Rationale:**
Verify basic OsTask model initialization.

---

### UTS_OS_MODEL_00018 : OsTask Boundary Values

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00008
**Test Implementation:** test_os_xdm.py:test_ostask_boundary_values
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Boundary Value Analysis

**Preconditions:**
1. OsTask instance exists

**Test Steps:**
1. **Given:** OsTask with default values
2. **When:** Set boundary values for Activation and Priority
3. **Then:** Values are stored correctly

**Test Data:**
| Field | Min Value | Max Value |
|-------|-----------|-----------|
| OsTaskActivation | 1 | 255 |
| OsTaskPriority | 0 | 2147483647 |
| OsStacksize | 0 | 2000000000 |

**Expected Results:**
- All boundary values are accepted
- Values are stored correctly

**Verification Criteria:**
1. Verify OsTaskActivation accepts min (1) and max (255)
2. Verify OsTaskPriority accepts min (0) and max (2147483647)
3. Verify OsStacksize accepts min (0) and max (2000000000)

**Rationale:**
Test boundary values for OsTask fields.

---

### UTS_OS_MODEL_00019 : OsTask Schedule Type

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00008
**Test Implementation:** test_os_xdm.py:test_ostask_schedule_type
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsTask instance exists

**Test Steps:**
1. **Given:** OsTask with no schedule type
2. **When:** Set OsTaskSchedule to FULL and NON
3. **Then:** Schedule type is stored correctly

**Test Data:**
| OsTaskSchedule | Description |
|----------------|-------------|
| FULL | Fully preemptable task |
| NON | Non-preemptable task |

**Expected Results:**
- Both schedule types are accepted
- IsPreemptable() returns expected value

**Verification Criteria:**
1. Verify FULL schedule type is set correctly
2. Verify NON schedule type is set correctly
3. Verify IsPreemptable() returns True for FULL
4. Verify IsPreemptable() returns False for NON

**Rationale:**
Verify OsTaskSchedule enumeration field and behavior.

---

### UTS_OS_MODEL_00020 : OsPeripheralArea Model Initialization

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00009
**Test Implementation:** test_os_xdm.py:test_osperipheralarea_initialization
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsPeripheralArea class is imported from eb_model.models.core.os_xdm

**Test Steps:**
1. **Given:** No OsPeripheralArea instance exists
2. **When:** Create OsPeripheralArea with name "PeripheralArea1"
3. **Then:** OsPeripheralArea instance is created with default values

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| name | "PeripheralArea1" | Peripheral area name |

**Expected Results:**
- OsPeripheralArea instance is not None
- getName() returns "PeripheralArea1"
- All address fields are None

**Verification Criteria:**
1. Verify OsPeripheralArea instance is created successfully
2. Verify name is set correctly
3. Verify default field values

**Rationale:**
Verify basic OsPeripheralArea model initialization.

---

### UTS_OS_MODEL_00021 : OsPeripheralArea Address Fields

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00009
**Test Implementation:** test_os_xdm.py:test_osperipheralarea_addresses
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Boundary Value Analysis

**Preconditions:**
1. OsPeripheralArea instance exists

**Test Steps:**
1. **Given:** OsPeripheralArea with no addresses
2. **When:** Set start, end addresses and ID
3. **Then:** Values are stored correctly

**Test Data:**
| Field | Min Value | Max Value |
|-------|-----------|-----------|
| OsPeripheralAreaStartAddress | 0 | 9223372036854775807 |
| OsPeripheralAreaEndAddress | 0 | 9223372036854775807 |
| OsPeripheralAreaId | 0 | 9223372036854775807 |

**Expected Results:**
- All values are accepted
- Values are stored correctly

**Verification Criteria:**
1. Verify start address is set correctly
2. Verify end address is set correctly
3. Verify ID is set correctly

**Rationale:**
Verify OsPeripheralArea address fields.

---

### UTS_OS_MODEL_00022 : OsResource Model Initialization

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00010
**Test Implementation:** test_os_xdm.py:test_osresource_initialization
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsResource class is imported from eb_model.models.core.os_xdm

**Test Steps:**
1. **Given:** No OsResource instance exists
2. **When:** Create OsResource with name "Resource1"
3. **Then:** OsResource instance is created with default values

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| name | "Resource1" | Resource name |

**Expected Results:**
- OsResource instance is not None
- getName() returns "Resource1"
- OsResourceProperty is None
- OsResourceAccessingApplication is empty list

**Verification Criteria:**
1. Verify OsResource instance is created successfully
2. Verify name is set correctly
3. Verify default field values

**Rationale:**
Verify basic OsResource model initialization.

---

### UTS_OS_MODEL_00023 : OsResource Property Types

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00010
**Test Implementation:** test_os_xdm.py:test_osresource_property
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsResource instance exists

**Test Steps:**
1. **Given:** OsResource with no property
2. **When:** Set OsResourceProperty to different types
3. **Then:** Property is stored correctly

**Test Data:**
| OsResourceProperty | Description |
|-------------------|-------------|
| INTERNAL | Internal resource |
| LINKED | Linked resource |
| STANDARD | Standard resource |

**Expected Results:**
- All property types are accepted
- getOsResourceProperty() returns correct value

**Verification Criteria:**
1. Verify INTERNAL is set correctly
2. Verify LINKED is set correctly
3. Verify STANDARD is set correctly

**Rationale:**
Verify OsResourceProperty enumeration field.

---

### UTS_OS_MODEL_00024 : OsScheduleTable Model Initialization

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00011
**Test Implementation:** test_os_xdm.py:test_osscheduletable_initialization
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsScheduleTable class is imported from eb_model.models.core.os_xdm

**Test Steps:**
1. **Given:** No OsScheduleTable instance exists
2. **When:** Create OsScheduleTable with name "ScheduleTable1"
3. **Then:** OsScheduleTable instance is created with default values

**Test Data:**
| Input Field | Value | Description |
|-------------|-------|-------------|
| name | "ScheduleTable1" | Schedule table name |

**Expected Results:**
- OsScheduleTable instance is not None
- getName() returns "ScheduleTable1"
- OsScheduleTableDuration is None
- OsScheduleTableRepeating is None
- OsScheduleTableCounterRef is None

**Verification Criteria:**
1. Verify OsScheduleTable instance is created successfully
2. Verify name is set correctly
3. Verify default field values

**Rationale:**
Verify basic OsScheduleTable model initialization.

---

### UTS_OS_MODEL_00025 : OsScheduleTable Duration and Repeating

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00011
**Test Implementation:** test_os_xdm.py:test_osscheduletable_duration
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsScheduleTable instance exists

**Test Steps:**
1. **Given:** OsScheduleTable with no duration
2. **When:** Set duration and repeating flag
3. **Then:** Values are stored correctly

**Test Data:**
| OsScheduleTableDuration | OsScheduleTableRepeating |
|-------------------------|--------------------------|
| 100 | True |
| 1000 | False |
| 10000 | True |

**Expected Results:**
- Duration is stored correctly
- Repeating flag is stored correctly

**Verification Criteria:**
1. Verify OsScheduleTableDuration is set correctly
2. Verify OsScheduleTableRepeating is set correctly

**Rationale:**
Verify OsScheduleTable duration and repeating fields.

---

### UTS_OS_MODEL_00026 : OsScheduleTable Counter Reference

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00011
**Test Implementation:** test_os_xdm.py:test_osscheduletable_counter_ref
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. OsScheduleTable instance exists

**Test Steps:**
1. **Given:** OsScheduleTable with no counter reference
2. **When:** Set counter reference
3. **Then:** Counter reference is stored correctly

**Test Data:**
| OsScheduleTableCounterRef | Description |
|---------------------------|-------------|
| EcucRefType("/Os/Counter1") | Counter reference |

**Expected Results:**
- Counter reference is stored correctly
- getOsScheduleTableCounterRef() returns correct value

**Verification Criteria:**
1. Verify counter reference is set correctly
2. Verify getOsScheduleTableCounterRef() returns expected value

**Rationale:**
Verify OsScheduleTableCounterRef field.

---

### UTS_OS_MODEL_00027 : Os Model Initialization

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00012
**Test Implementation:** test_os_xdm.py:test_os_initialization
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. Os class is imported from eb_model.models.core.os_xdm

**Test Steps:**
1. **Given:** No Os instance exists
2. **When:** Create Os instance
3. **Then:** Os instance is created with empty entity lists

**Expected Results:**
- Os instance is not None
- All entity lists are empty

**Verification Criteria:**
1. Verify Os instance is created successfully
2. Verify all entity lists are empty

**Rationale:**
Verify basic Os root model initialization.

---

### UTS_OS_MODEL_00028 : Os Entity List Methods

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00012
**Test Implementation:** test_os_xdm.py:test_os_entity_lists
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. Os instance exists

**Test Steps:**
1. **Given:** Os with empty entity lists
2. **When:** Add entities to all lists
3. **Then:** Entities are stored and retrieved correctly

**Test Data:**
| Method | Entity Type |
|--------|-------------|
| addOsTask | OsTask |
| addOsIsr | OsIsr |
| addOsAlarm | OsAlarm |
| addOsCounter | OsCounter |
| addOsApplication | OsApplication |
| addOsResource | OsResource |
| addOsEvent | OsEvent |
| addOsSpinlock | OsSpinlock |
| addOsPeripheralArea | OsPeripheralArea |
| addOsScheduleTable | OsScheduleTable |

**Expected Results:**
- All entities are added successfully
- All get*List() methods return correct count

**Verification Criteria:**
1. Verify getOsTaskList() returns added tasks
2. Verify getOsIsrList() returns added ISRs
3. Verify getOsAlarmList() returns added alarms
4. Verify getOsCounterList() returns added counters
5. Verify getOsApplicationList() returns added applications
6. Verify getOsResourceList() returns added resources
7. Verify getOsEventList() returns added events
8. Verify getOsSpinlockList() returns added spinlocks
9. Verify getOsPeripheralAreaList() returns added peripheral areas
10. Verify getOsScheduleTableList() returns added schedule tables

**Rationale:**
Verify Os root model entity list methods.

---

### UTS_OS_MODEL_00029 : Os AppMode List Method

**Type:** Functional
**Priority:** High
**Status:** Passed

**Traces-To:** SWR_OS_MODELS_00012
**Test Implementation:** test_os_xdm.py:test_os_appmode_list
**Last Validated:** 2026-05-28
**Last Changed:** 2026-05-28

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. Os instance exists

**Test Steps:**
1. **Given:** Os with empty AppMode list
2. **When:** Add OsAppMode entities
3. **Then:** AppMode entities are stored and retrieved correctly

**Test Data:**
| Entity | Name |
|--------|------|
| OsAppMode | "AppMode1" |
| OsAppMode | "AppMode2" |

**Expected Results:**
- getOsAppModeList() returns correct count
- AppMode entities are stored correctly

**Verification Criteria:**
1. Verify getOsAppModeList() returns added app modes
2. Verify correct count is returned

**Rationale:**
Verify Os root model getOsAppModeList() method.

---

## Test Summary

| Test ID | Test Name | Priority | Status | Traces-To |
|---------|-----------|----------|--------|-----------|
| UTS_OS_MODEL_00001 | OsAlarm Model Initialization | Critical | Passed | SWR_OS_MODELS_00001 |
| UTS_OS_MODEL_00002 | OsAlarm Accessing Application References | High | Passed | SWR_OS_MODELS_00001 |
| UTS_OS_MODEL_00003 | OsAlarm Counter Reference | High | Passed | SWR_OS_MODELS_00001 |
| UTS_OS_MODEL_00004 | OsAppMode Model Initialization | Critical | Passed | SWR_OS_MODELS_00002 |
| UTS_OS_MODEL_00005 | OsApplication Model Initialization | Critical | Passed | SWR_OS_MODELS_00003 |
| UTS_OS_MODEL_00006 | OsApplication Trusted Flags | High | Passed | SWR_OS_MODELS_00003 |
| UTS_OS_MODEL_00007 | OsApplication Reference Lists | High | Passed | SWR_OS_MODELS_00003 |
| UTS_OS_MODEL_00008 | OsCounter Model Initialization | Critical | Passed | SWR_OS_MODELS_00004 |
| UTS_OS_MODEL_00009 | OsCounter Boundary Values | High | Passed | SWR_OS_MODELS_00004 |
| UTS_OS_MODEL_00010 | OsCounter Type Enumeration | High | Passed | SWR_OS_MODELS_00004 |
| UTS_OS_MODEL_00011 | OsEvent Model Initialization | Critical | Passed | SWR_OS_MODELS_00005 |
| UTS_OS_MODEL_00012 | OsSpinlock Model Initialization | Critical | Passed | SWR_OS_MODELS_00006 |
| UTS_OS_MODEL_00013 | OsSpinlock Lock Method | High | Passed | SWR_OS_MODELS_00006 |
| UTS_OS_MODEL_00014 | OsIsr Model Initialization | Critical | Passed | SWR_OS_MODELS_00007 |
| UTS_OS_MODEL_00015 | OsIsr Category | High | Passed | SWR_OS_MODELS_00007 |
| UTS_OS_MODEL_00016 | OsIsr Stack Size | High | Passed | SWR_OS_MODELS_00007 |
| UTS_OS_MODEL_00017 | OsTask Model Initialization | Critical | Passed | SWR_OS_MODELS_00008 |
| UTS_OS_MODEL_00018 | OsTask Boundary Values | High | Passed | SWR_OS_MODELS_00008 |
| UTS_OS_MODEL_00019 | OsTask Schedule Type | High | Passed | SWR_OS_MODELS_00008 |
| UTS_OS_MODEL_00020 | OsPeripheralArea Model Initialization | Critical | Passed | SWR_OS_MODELS_00009 |
| UTS_OS_MODEL_00021 | OsPeripheralArea Address Fields | High | Passed | SWR_OS_MODELS_00009 |
| UTS_OS_MODEL_00022 | OsResource Model Initialization | Critical | Passed | SWR_OS_MODELS_00010 |
| UTS_OS_MODEL_00023 | OsResource Property Types | High | Passed | SWR_OS_MODELS_00010 |
| UTS_OS_MODEL_00024 | OsScheduleTable Model Initialization | Critical | Passed | SWR_OS_MODELS_00011 |
| UTS_OS_MODEL_00025 | OsScheduleTable Duration and Repeating | High | Passed | SWR_OS_MODELS_00011 |
| UTS_OS_MODEL_00026 | OsScheduleTable Counter Reference | High | Passed | SWR_OS_MODELS_00011 |
| UTS_OS_MODEL_00027 | Os Model Initialization | Critical | Passed | SWR_OS_MODELS_00012 |
| UTS_OS_MODEL_00028 | Os Entity List Methods | Critical | Passed | SWR_OS_MODELS_00012 |
| UTS_OS_MODEL_00029 | Os AppMode List Method | High | Passed | SWR_OS_MODELS_00012 |
