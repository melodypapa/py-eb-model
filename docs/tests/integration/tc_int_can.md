# CAN Stack Integration Test Cases

This document contains all integration test cases for the CAN Communication Stack modules (CanIf, CanNm, CanSm, CanTp) following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_INT_CAN_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_CAN_00001 |
| Title | CAN Stack - End-to-End Parsing and Excel Export |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete end-to-end workflow of parsing CAN stack XDM files and exporting to Excel.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CAN stack XDM files are available |
| 3 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| CanIf File | `data/test/CanIf.xdm` | CanIf configuration |
| CanNm File | `data/test/CanNm.xdm` | CanNm configuration |
| CanSm File | `data/test/CanSm.xdm` | CanSm configuration |
| CanTp File | `data/test/CanTp.xdm` | CanTp configuration |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse CanIf configuration | Configuration parsed successfully |
| 2 | Parse CanNm configuration | Configuration parsed successfully |
| 3 | Parse CanSm configuration | Configuration parsed successfully |
| 4 | Parse CanTp configuration | Configuration parsed successfully |
| 5 | Generate Excel outputs | All files created successfully |

## Expected Results

- All CAN stack modules parsed correctly
- Excel files generated for each module
- Performance meets requirements

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CANIF_00001 | CanIf Module Parsing | Covered |
| SWR_CANNM_00001 | CanNm Module Parsing | Covered |
| SWR_CANSM_00001 | CanSm Module Parsing | Covered |
| SWR_CANTP_00001 | CanTp Module Parsing | Covered |

---

# Test Case: TC_INT_CAN_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_CAN_00002 |
| Title | CAN Stack - Multi-Channel Configuration |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the CAN stack parser can handle multi-channel configurations.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Multi-channel CAN configuration is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse multi-channel CanIf | All channels extracted |
| 2 | Verify channel count | Count matches configuration |
| 3 | Verify controller assignments | Controllers assigned correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CANIF_00003 | CanIf Controller Configuration | Covered |

---

# Test Case: TC_INT_CAN_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_CAN_00003 |
| Title | CAN Stack - Error Recovery |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the CAN stack modules handle error conditions gracefully.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Test files with error conditions are available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse invalid CAN file | Error reported clearly |
| 2 | Parse missing file | Error reported clearly |
| 3 | Verify system recovery | Subsequent operations work |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CANIF_00001 | CanIf Module Parsing | Covered |