# CAN Stack Unit Test Cases

This document contains all unit test cases for the CAN Communication Stack modules (CanIf, CanNm, CanSm, CanTp) following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_CANIF_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CANIF_00001 |
| Title | CanIf Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CanIf parser correctly validates the module name and extracts configuration from XDM files.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid CanIf.xdm file is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Module Name | "CanIf" | Expected module name |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid CanIf.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "CanIf" is accepted |
| 3 | Parse non-CanIf file | Raises ValueError |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CANIF_00001 | CanIf Module Parsing | Covered |

---

# Test Case: TC_UNIT_CANIF_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CANIF_00002 |
| Title | CanIf Model - General Configuration Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CanIf parser correctly extracts CanIfGeneral configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CanIfGeneral configuration is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Dev Error Detect | true | Development error detection |
| Number of CAN HW Units | 2 | Hardware unit count |
| Max Controllers | 2 | Maximum controllers |
| Max Tx PDUs | 64 | Maximum transmit PDUs |
| Max Rx PDUs | 64 | Maximum receive PDUs |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse CanIfGeneral configuration | Object created successfully |
| 2 | Verify dev error detect | Value extracted correctly |
| 3 | Verify HW unit count | Value extracted correctly |
| 4 | Verify max controllers | Value extracted correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CANIF_00002 | CanIf General Configuration | Covered |

---

# Test Case: TC_UNIT_CANIF_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CANIF_00003 |
| Title | CanIf Model - Controller Configuration Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CanIf parser correctly extracts CanIfCtrlCfg configurations.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Controller configuration is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Controller ID | 0 | Controller identifier |
| Wakeup Support | true | Wakeup support flag |
| CAN Controller Ref | Reference to CanCtrl | Controller reference |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse CanIfCtrlCfg configuration | Object created successfully |
| 2 | Verify controller ID | Value extracted correctly |
| 3 | Verify wakeup support | Value extracted correctly |
| 4 | Verify controller reference | Reference extracted correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CANIF_00003 | CanIf Controller Configuration | Covered |

---

# Test Case: TC_UNIT_CANNM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CANNM_00001 |
| Title | CanNm Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CanNm parser correctly validates the module name and extracts network management configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid CanNm.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid CanNm.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "CanNm" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CANNM_00001 | CanNm Module Parsing | Covered |

---

# Test Case: TC_UNIT_CANSM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CANSM_00001 |
| Title | CanSm Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CanSm parser correctly validates the module name and extracts state manager configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid CanSm.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid CanSm.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "CanSm" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CANSM_00001 | CanSm Module Parsing | Covered |

---

# Test Case: TC_UNIT_CANTP_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CANTP_00001 |
| Title | CanTp Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CanTp parser correctly validates the module name and extracts transport protocol configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid CanTp.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid CanTp.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "CanTp" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CANTP_00001 | CanTp Module Parsing | Covered |

---

# Test Case: TC_UNIT_CANIF_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CANIF_00004 |
| Title | CanIf Reporter - Excel Worksheet Generation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CanIf reporter correctly generates Excel worksheets for CanIf configurations.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CanIf model objects are populated |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Generate Excel output | File created successfully |
| 2 | Verify worksheet content | All data populated correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CANIF_00004 | CanIf Excel Generation | Covered |

---

# Test Case: TC_UNIT_CANNM_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CANNM_00002 |
| Title | CanNm Model - Node Configuration Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CanNm parser correctly extracts node configurations.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CanNm node configuration is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse CanNm node configuration | Object created successfully |
| 2 | Verify node ID | Value extracted correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CANNM_00002 | CanNm Node Configuration | Covered |