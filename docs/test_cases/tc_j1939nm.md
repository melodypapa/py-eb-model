# Test Cases: J1939Nm Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | J1939Nm Module Test Cases |
| Document ID | TC_J1939NM_00001 |
| Version | 1.0 |
| Date | 2026-03-29 |
| Project | py-eb-model |
| Module | J1939Nm (J1939 Network Manager) |

## Table of Contents

1. [Test Overview](#1-test-overview)
2. [Unit Tests](#2-unit-tests)
3. [Integration Tests](#3-integration-tests)
4. [Acceptance Tests](#4-acceptance-tests)

---

## 1. Test Overview

### 1.1 Test Scope

This document describes test cases for the J1939Nm module covering:
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

### 2.1 Model Tests (`test_j1939nm_xdm.py`)

#### TC_J1939NM_001: J1939Nm Module Initialization
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939NM_00001 |
| Test Type | Unit |
| Description | Verify J1939Nm module initializes with correct name and parent |
| Preconditions | None |
| Test Steps | 1. Create EBModel instance 2. Create EcucParamConfContainerDef parent 3. Instantiate J1939Nm with parent |
| Expected Result | Name is "J1939Nm", parent reference is correct |
| Status | PASS |

#### TC_J1939NM_002: J1939Nm Module Properties
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939NM_00001 |
| Test Type | Unit |
| Description | Verify J1939Nm inherits Module properties (AR/SW versions) |
| Preconditions | J1939Nm instance created |
| Test Steps | 1. Check getArVersion() returns correct type 2. Check getSwVersion() returns correct type 3. Check getTotalElement() is 0 |
| Expected Result | All properties accessible, no errors |
| Status | PASS |

#### TC_J1939NM_003: J1939NmGeneral Initialization
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939NM_00002 |
| Test Type | Unit |
| Description | Verify J1939NmGeneral container initializes correctly |
| Preconditions | J1939Nm instance created |
| Test Steps | 1. Create J1939NmGeneral with J1939Nm parent 2. Check name and parent |
| Expected Result | Name is "J1939NmGeneral", parent reference correct |
| Status | PASS |

#### TC_J1939NM_004: DevErrorDetect Getter/Setter
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939NM_00002 |
| Test Type | Unit |
| Description | Verify DevErrorDetect property getter and setter |
| Preconditions | J1939NmGeneral instance created |
| Test Steps | 1. Set DevErrorDetect to True 2. Verify getJ1939NmDevErrorDetect() returns True |
| Expected Result | Property value matches set value |
| Status | PASS |

#### TC_J1939NM_005: Enabled Getter/Setter
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939NM_00002 |
| Test Type | Unit |
| Description | Verify Enabled property getter and setter |
| Preconditions | J1939NmGeneral instance created |
| Test Steps | 1. Set Enabled to True 2. Verify getJ1939NmEnabled() returns True |
| Expected Result | Property value matches set value |
| Status | PASS |

#### TC_J1939NM_006: Fluent Interface Pattern
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939NM_00006 |
| Test Type | Unit |
| Description | Verify setters return self for method chaining |
| Preconditions | J1939NmGeneral instance created |
| Test Steps | 1. Call setJ1939NmDevErrorDetect() 2. Verify return value is self 3. Chain setJ1939NmEnabled() |
| Expected Result | All setters return self, chaining works |
| Status | PASS |

### 2.2 Parser Tests (`test_j1939nm_xdm_parser.py`)

#### TC_J1939NM_007: Parse J1939NmGeneral
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939NM_00002 |
| Test Type | Unit |
| Description | Verify J1939NmGeneral container parsed from XML |
| Preconditions | XML with J1939NmGeneral container |
| Test Steps | 1. Create parser with namespace map 2. Parse XML element 3. Check model values |
| Expected Result | DevErrorDetect and Enabled values correctly parsed |
| Status | PASS |

---

## 3. Integration Tests

### 3.1 End-to-End Parser Tests

#### TC_J1939NM_008: Parse Complete J1939Nm XDM
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939NM_00001 |
| Test Type | Integration |
| Description | Parse full J1939Nm XDM file with all containers |
| Preconditions | Valid J1939Nm.xdm file available |
| Test Steps | 1. Load J1939Nm.xdm 2. Parse with J1939NmXdmParser 3. Verify all containers populated |
| Expected Result | All model elements created with correct values |
| Status | Not Implemented |

### 3.2 Reporter Integration

#### TC_J1939NM_009: Generate Excel Report
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939NM_00003 |
| Test Type | Integration |
| Description | Generate Excel report from parsed J1939Nm model |
| Preconditions | Parsed J1939Nm model available |
| Test Steps | 1. Create J1939NmXdmXlsWriter 2. Call write() with output path 3. Verify Excel file created |
| Expected Result | Excel file with J1939NmGeneral sheet exists |
| Status | Not Implemented |

---

## 4. Acceptance Tests

### 4.1 CLI Tests

#### TC_J1939NM_010: CLI Command Execution
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939NM_00004 |
| Test Type | Acceptance |
| Description | Verify j1939nm-xdm-xlsx CLI command works |
| Preconditions | J1939Nm.xdm file available |
| Test Steps | 1. Execute `j1939nm-xdm-xlsx input.xdm output.xlsx` 2. Check exit code is 0 3. Verify output file exists |
| Expected Result | Command succeeds, Excel file generated |
| Status | Not Implemented |

#### TC_J1939NM_011: CLI Verbose Mode
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939NM_00004 |
| Test Type | Acceptance |
| Description | Verify verbose logging option works |
| Preconditions | J1939Nm.xdm file available |
| Test Steps | 1. Execute with -v flag 2. Verify debug output to stderr 3. Check log file created |
| Expected Result | Debug information logged correctly |
| Status | Not Implemented |

#### TC_J1939NM_012: CLI Error Handling
| Field | Value |
|-------|-------|
| Requirement | SWR_J1939NM_00004 |
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
# Run all J1939Nm tests
pytest src/eb_model/tests/ -k j1939nm -v

# Run model tests only
pytest src/eb_model/tests/models/test_j1939nm_xdm.py -v

# Run parser tests only
pytest src/eb_model/tests/parser/test_j1939nm_xdm_parser.py -v

# Run with coverage
pytest src/eb_model/tests/ -k j1939nm --cov=src/eb_model
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
src/eb_model/models/j1939nm_xdm.py                 63      0   100%
src/eb_model/parser/j1939nm_xdm_parser.py          56      0   100%
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