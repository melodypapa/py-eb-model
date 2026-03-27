# FlexRay Stack Integration Test Cases

This document contains all integration test cases for the FlexRay Communication Stack modules (FrIf, FrNm, FrSm, FrTp, FrArTp) following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_INT_FLEXRAY_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_FLEXRAY_00001 |
| Title | FlexRay Stack - End-to-End Parsing and Excel Export |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete end-to-end workflow of parsing FlexRay stack XDM files and exporting to Excel.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | FlexRay stack XDM files are available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse FrIf configuration | Configuration parsed successfully |
| 2 | Parse FrNm configuration | Configuration parsed successfully |
| 3 | Parse FrSm configuration | Configuration parsed successfully |
| 4 | Parse FrTp configuration | Configuration parsed successfully |
| 5 | Parse FrArTp configuration | Configuration parsed successfully |
| 6 | Generate Excel outputs | All files created successfully |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_FRIF_00001 | FrIf Module Parsing | Covered |
| SWR_FRNM_00001 | FrNm Module Parsing | Covered |
| SWR_FRSM_00001 | FrSm Module Parsing | Covered |
| SWR_FRTP_00001 | FrTp Module Parsing | Covered |
| SWR_FRARTP_00001 | FrArTp Module Parsing | Covered |

---

# Test Case: TC_INT_FLEXRAY_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_FLEXRAY_00002 |
| Title | FlexRay Stack - Error Recovery |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the FlexRay stack modules handle error conditions gracefully.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Test files with error conditions are available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse invalid FlexRay file | Error reported clearly |
| 2 | Verify system recovery | Subsequent operations work |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_FRIF_00001 | FrIf Module Parsing | Covered |