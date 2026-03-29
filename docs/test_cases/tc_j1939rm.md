# Test Cases: J1939Rm Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | J1939Rm Module Test Cases |
| Document ID | TC_J1939RM_00001 |
| Version | 1.0 |
| Date | 2026-03-29 |
| Project | py-eb-model |
| Module | J1939Rm (J1939 Request Manager) |

## Table of Contents

1. [Test Overview](#1-test-overview)
2. [Unit Tests](#2-unit-tests)
3. [Integration Tests](#3-integration-tests)
4. [Acceptance Tests](#4-acceptance-tests)

---

## 1. Test Overview

### 1.1 Test Scope

This document describes test cases for the J1939Rm module covering:
- Model class initialization and property access
- XML parsing from XDM files
- Excel report generation
- CLI command execution

### 1.2 Test Environment

- Python version: 3.9, 3.10, 3.11
- Test framework: pytest
- Coverage target: 80%+

---

## 2. Unit Tests

### 2.1 Model Tests (`test_j1939rm_xdm.py`)

#### TC_J1939RM_001: J1939Rm Module Initialization
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939RM_00001 |
| Test Type | Unit |
| Description | Verify J1939Rm module initializes with correct name and parent |
| Preconditions | None |
| Test Steps | 1. Create EBModel instance 2. Create EcucParamConfContainerDef parent 3. Instantiate J1939Rm with parent |
| Expected Result | Name is "J1939Rm", parent reference is correct |
| Status | PASS |

#### TC_J1939RM_002: J1939Rm Module Properties
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939RM_00001 |
| Test Type | Unit |
| Description | Verify J1939Rm inherits Module properties (AR/SW versions) |
| Preconditions | J1939Rm instance created |
| Test Steps | 1. Check getArVersion() returns correct type 2. Check getSwVersion() returns correct type 3. Check getTotalElement() is 0 |
| Expected Result | All properties accessible, no errors |
| Status | PASS |

#### TC_J1939RM_003: J1939RmGeneral Initialization
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939RM_00002 |
| Test Type | Unit |
| Description | Verify J1939RmGeneral container initializes correctly |
| Preconditions | J1939Rm instance created |
| Test Steps | 1. Create J1939RmGeneral with J1939Rm parent 2. Check name and parent |
| Expected Result | Name is "J1939RmGeneral", parent reference correct |
| Status | PASS |

#### TC_J1939RM_004: DevErrorDetect Getter/Setter
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939RM_00002 |
| Test Type | Unit |
| Description | Verify DevErrorDetect property getter and setter |
| Preconditions | J1939RmGeneral instance created |
| Test Steps | 1. Set DevErrorDetect to True 2. Verify getJ1939RmDevErrorDetect() returns True |
| Expected Result | Property value matches set value |
| Status | PASS |

#### TC_J1939RM_005: Enabled Getter/Setter
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939RM_00002 |
| Test Type | Unit |
| Description | Verify Enabled property getter and setter |
| Preconditions | J1939RmGeneral instance created |
| Test Steps | 1. Set Enabled to True 2. Verify getJ1939RmEnabled() returns True |
| Expected Result | Property value matches set value |
| Status | PASS |

#### TC_J1939RM_006: Fluent Interface Pattern
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939RM_00006 |
| Test Type | Unit |
| Description | Verify setters return self for method chaining |
| Preconditions | J1939RmGeneral instance created |
| Test Steps | 1. Call setJ1939RmDevErrorDetect() 2. Verify return value is self 3. Chain setJ1939RmEnabled() |
| Expected Result | All setters return self, chaining works |
| Status | PASS |

### 2.2 Parser Tests (`test_j1939rm_xdm_parser.py`)

#### TC_J1939RM_007: Parse J1939RmGeneral
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939RM_00002 |
| Test Type | Unit |
| Description | Verify J1939RmGeneral container parsed from XML |
| Preconditions | XML with J1939RmGeneral container |
| Test Steps | 1. Create parser with namespace map 2. Parse XML element 3. Check model values |
| Expected Result | DevErrorDetect and Enabled values correctly parsed |
| Status | PASS |

---

## 3. Integration Tests

### 3.1 End-to-End Parser Tests

#### TC_J1939RM_008: Parse Complete J1939Rm XDM
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939RM_00001 |
| Test Type | Integration |
| Description | Parse full J1939Rm XDM file with all containers |
| Preconditions | Valid J1939Rm.xdm file available |
| Test Steps | 1. Load J1939Rm.xdm 2. Parse with J1939RmXdmParser 3. Verify all containers populated |
| Expected Result | All model elements created with correct values |
| Status | Not Implemented |

### 3.2 Reporter Integration

#### TC_J1939RM_009: Generate Excel Report
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939RM_00003 |
| Test Type | Integration |
| Description | Generate Excel report from parsed J1939Rm model |
| Preconditions | Parsed J1939Rm model available |
| Test Steps | 1. Create J1939RmXdmXlsWriter 2. Call write() with output path 3. Verify Excel file created |
| Expected Result | Excel file with J1939RmGeneral sheet exists |
| Status | Not Implemented |

---

## 4. Acceptance Tests

### 4.1 CLI Tests

#### TC_J1939RM_010: CLI Command Execution
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939RM_00004 |
| Test Type | Acceptance |
| Description | Verify j1939rm-xdm-xlsx CLI command works |
| Preconditions | J1939Rm.xdm file available |
| Test Steps | 1. Execute `j1939rm-xdm-xlsx input.xdm output.xlsx` 2. Check exit code is 0 3. Verify output file exists |
| Expected Result | Command succeeds, Excel file generated |
| Status | Not Implemented |

#### TC_J1939RM_011: CLI Verbose Mode
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939RM_00004 |
| Test Type | Acceptance |
| Description | Verify verbose logging option works |
| Preconditions | J1939Rm.xdm file available |
| Test Steps | 1. Execute with -v flag 2. Verify debug output to stderr 3. Check log file created |
| Expected Result | Debug information logged correctly |
| Status | Not Implemented |

#### TC_J1939RM_012: CLI Error Handling
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939RM_00004 |
| Test Type | Acceptance |
| Description | Verify CLI handles invalid inputs gracefully |
| Preconditions | None |
| Test Steps | 1. Execute with non-existent file 2. Verify error message 3. Check non-zero exit code |
| Expected Result | Clear error message, non-zero exit code |
| Status | Not Implemented |

---

## 5. Test Execution

### 5.1 Running Tests

```bash
# Run all J1939Rm tests
pytest src/eb_model/tests/ -k j1939rm -v

# Run model tests only
pytest src/eb_model/tests/models/test_j1939rm_xdm.py -v

# Run parser tests only
pytest src/eb_model/tests/parser/test_j1939rm_xdm_parser.py -v

# Run with coverage
pytest src/eb_model/tests/ -k j1939rm --cov=src/eb_model
```

### 5.2 Test Results Summary

| Test Category | Total | Pass | Fail | Skip |
|---------------|-------|------|------|------|
| Model Tests | 6 | 6 | 0 | 0 |
| Parser Tests | 1 | 1 | 0 | 0 |
| Integration Tests | 2 | 0 | 0 | 2 |
| Acceptance Tests | 3 | 0 | 0 | 3 |
| **Total** | **12** | **7** | **0** | **5** |

### 5.3 Coverage Report

```
Name                                          Stmts   Miss  Cover
------------------------------------------------------------------
src/eb_model/models/j1939rm_xdm.py                 63      0   100%
src/eb_model/parser/j1939rm_xdm_parser.py          56      0   100%
------------------------------------------------------------------
Total                                                 119      0   100%
```

---

## 6. Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-29 | Claude Code | Initial test cases document |

---

**Document End**