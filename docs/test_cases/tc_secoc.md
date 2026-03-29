# Test Cases: SecOC Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | SecOC Module Test Cases |
| Document ID | TC_SECOC_00001 |
| Version | 1.0 |
| Date | 2026-03-29 |
| Project | py-eb-model |
| Module | SecOC (Secure On-Board Communication) |

## Table of Contents

1. [Test Overview](#1-test-overview)
2. [Unit Tests](#2-unit-tests)
3. [Integration Tests](#3-integration-tests)
4. [Acceptance Tests](#4-acceptance-tests)

---

## 1. Test Overview

### 1.1 Test Scope

This document describes test cases for the SecOC module covering:
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

### 2.1 Model Tests (`test_secoc_xdm.py`)

#### TC_SECOC_001: SecOC Module Initialization
| Field | Value |
|-------|-------|
| Requirement | SWR_SECOC_00001 |
| Test Type | Unit |
| Description | Verify SecOC module initializes with correct name and parent |
| Preconditions | None |
| Test Steps | 1. Create EBModel instance 2. Create EcucParamConfContainerDef parent 3. Instantiate SecOC with parent |
| Expected Result | Name is "SecOC", parent reference is correct |
| Status | PASS |

#### TC_SECOC_002: SecOC Module Properties
| Field | Value |
|-------|-------|
| Requirement | SWR_SECOC_00001 |
| Test Type | Unit |
| Description | Verify SecOC inherits Module properties (AR/SW versions) |
| Preconditions | SecOC instance created |
| Test Steps | 1. Check getArVersion() returns correct type 2. Check getSwVersion() returns correct type 3. Check getTotalElement() is 0 |
| Expected Result | All properties accessible, no errors |
| Status | PASS |

#### TC_SECOC_003: SecOCGeneral Initialization
| Field | Value |
|-------|-------|
| Requirement | SWR_SECOC_00002 |
| Test Type | Unit |
| Description | Verify SecOCGeneral container initializes correctly |
| Preconditions | SecOC instance created |
| Test Steps | 1. Create SecOCGeneral with SecOC parent 2. Check name and parent |
| Expected Result | Name is "SecOCGeneral", parent reference correct |
| Status | PASS |

#### TC_SECOC_004: DevErrorDetect Getter/Setter
| Field | Value |
|-------|-------|
| Requirement | SWR_SECOC_00002 |
| Test Type | Unit |
| Description | Verify DevErrorDetect property getter and setter |
| Preconditions | SecOCGeneral instance created |
| Test Steps | 1. Set DevErrorDetect to True 2. Verify getSecocDevErrorDetect() returns True |
| Expected Result | Property value matches set value |
| Status | PASS |

#### TC_SECOC_005: Enabled Getter/Setter
| Field | Value |
|-------|-------|
| Requirement | SWR_SECOC_00002 |
| Test Type | Unit |
| Description | Verify Enabled property getter and setter |
| Preconditions | SecOCGeneral instance created |
| Test Steps | 1. Set Enabled to True 2. Verify getSecocEnabled() returns True |
| Expected Result | Property value matches set value |
| Status | PASS |

#### TC_SECOC_006: Fluent Interface Pattern
| Field | Value |
|-------|-------|
| Requirement | SWR_SECOC_00006 |
| Test Type | Unit |
| Description | Verify setters return self for method chaining |
| Preconditions | SecOCGeneral instance created |
| Test Steps | 1. Call setSecocDevErrorDetect() 2. Verify return value is self 3. Chain setSecocEnabled() |
| Expected Result | All setters return self, chaining works |
| Status | PASS |

### 2.2 Parser Tests (`test_secoc_xdm_parser.py`)

#### TC_SECOC_007: Parse SecOCGeneral
| Field | Value |
|-------|-------|
| Requirement | SWR_SECOC_00002 |
| Test Type | Unit |
| Description | Verify SecOCGeneral container parsed from XML |
| Preconditions | XML with SecOCGeneral container |
| Test Steps | 1. Create parser with namespace map 2. Parse XML element 3. Check model values |
| Expected Result | DevErrorDetect and Enabled values correctly parsed |
| Status | PASS |

---

## 3. Integration Tests

### 3.1 End-to-End Parser Tests

#### TC_SECOC_008: Parse Complete SecOC XDM
| Field | Value |
|-------|-------|
| Requirement | SWR_SECOC_00001 |
| Test Type | Integration |
| Description | Parse full SecOC XDM file with all containers |
| Preconditions | Valid SecOC.xdm file available |
| Test Steps | 1. Load SecOC.xdm 2. Parse with SecOCXdmParser 3. Verify all containers populated |
| Expected Result | All model elements created with correct values |
| Status | Not Implemented |

### 3.2 Reporter Integration

#### TC_SECOC_009: Generate Excel Report
| Field | Value |
|-------|-------|
| Requirement | SWR_SECOC_00003 |
| Test Type | Integration |
| Description | Generate Excel report from parsed SecOC model |
| Preconditions | Parsed SecOC model available |
| Test Steps | 1. Create SecOCXdmXlsWriter 2. Call write() with output path 3. Verify Excel file created |
| Expected Result | Excel file with SecOCGeneral sheet exists |
| Status | Not Implemented |

---

## 4. Acceptance Tests

### 4.1 CLI Tests

#### TC_SECOC_010: CLI Command Execution
| Field | Value |
|-------|-------|
| Requirement | SWR_SECOC_00004 |
| Test Type | Acceptance |
| Description | Verify secoc-xdm-xlsx CLI command works |
| Preconditions | SecOC.xdm file available |
| Test Steps | 1. Execute `secoc-xdm-xlsx input.xdm output.xlsx` 2. Check exit code is 0 3. Verify output file exists |
| Expected Result | Command succeeds, Excel file generated |
| Status | Not Implemented |

#### TC_SECOC_011: CLI Verbose Mode
| Field | Value |
|-------|-------|
| Requirement | SWR_SECOC_00004 |
| Test Type | Acceptance |
| Description | Verify verbose logging option works |
| Preconditions | SecOC.xdm file available |
| Test Steps | 1. Execute with -v flag 2. Verify debug output to stderr 3. Check log file created |
| Expected Result | Debug information logged correctly |
| Status | Not Implemented |

#### TC_SECOC_012: CLI Error Handling
| Field | Value |
|-------|-------|
| Requirement | SWR_SECOC_00004 |
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
# Run all SecOC tests
pytest src/eb_model/tests/ -k secoc -v

# Run model tests only
pytest src/eb_model/tests/models/test_secoc_xdm.py -v

# Run parser tests only
pytest src/eb_model/tests/parser/test_secoc_xdm_parser.py -v

# Run with coverage
pytest src/eb_model/tests/ -k secoc --cov=src/eb_model
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
src/eb_model/models/secoc_xdm.py                 46      0   100%
src/eb_model/parser/secoc_xdm_parser.py          56      0   100%
------------------------------------------------------------------
Total                                             102      0   100%
```

---

## 6. Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-29 | Claude Code | Initial test cases document |

---

**Document End**