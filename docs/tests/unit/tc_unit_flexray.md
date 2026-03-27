# FlexRay Stack Unit Test Cases

This document contains all unit test cases for the FlexRay Communication Stack modules (FrIf, FrNm, FrSm, FrTp, FrArTp) following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_FRIF_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_FRIF_00001 |
| Title | FrIf Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the FrIf parser correctly validates the module name and extracts FlexRay interface configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid FrIf.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid FrIf.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "FrIf" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_FRIF_00001 | FrIf Module Parsing | Covered |

---

# Test Case: TC_UNIT_FRNM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_FRNM_00001 |
| Title | FrNm Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the FrNm parser correctly validates the module name and extracts network management configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid FrNm.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid FrNm.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "FrNm" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_FRNM_00001 | FrNm Module Parsing | Covered |

---

# Test Case: TC_UNIT_FRSM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_FRSM_00001 |
| Title | FrSm Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the FrSm parser correctly validates the module name and extracts state manager configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid FrSm.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid FrSm.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "FrSm" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_FRSM_00001 | FrSm Module Parsing | Covered |

---

# Test Case: TC_UNIT_FRTP_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_FRTP_00001 |
| Title | FrTp Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the FrTp parser correctly validates the module name and extracts transport protocol configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid FrTp.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid FrTp.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "FrTp" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_FRTP_00001 | FrTp Module Parsing | Covered |

---

# Test Case: TC_UNIT_FRARTP_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_FRARTP_00001 |
| Title | FrArTp Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the FrArTp parser correctly validates the module name and extracts AUTOSAR transport protocol configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid FrArTp.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid FrArTp.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "FrArTp" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_FRARTP_00001 | FrArTp Module Parsing | Covered |

---

# Test Case: TC_UNIT_FRIF_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_FRIF_00002 |
| Title | FrIf Reporter - Excel Worksheet Generation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the FrIf reporter correctly generates Excel worksheets.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | FrIf model objects are populated |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Generate Excel output | File created successfully |
| 2 | Verify worksheet content | All data populated correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_FRIF_00002 | FrIf Excel Generation | Covered |