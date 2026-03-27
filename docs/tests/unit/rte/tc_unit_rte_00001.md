# Test Case: TC_UNIT_RTE_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00001 |
| Title | RTE Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly extracts XML namespace definitions from EB Tresos XDM files, validates the module name, extracts AUTOSAR version information, and detects AUTOSAR version (AR 3.x vs AR 4.x) for appropriate handling.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Test XDM files (Rte.xdm for AR 3.x and AR 4.x) are available |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File AR3 | `data/test/Rte_ar3.xdm` | RTE XDM file for AUTOSAR 3.x |
| Input File AR4 | `data/test/Rte_ar4.xdm` | RTE XDM file for AUTOSAR 4.x |
| Module Name | "Rte" | Expected root module name |
| AUTOSAR Version AR3 | "3.2.1" | Example AUTOSAR 3.x version |
| AUTOSAR Version AR4 | "4.3.0" | Example AUTOSAR 4.x version |
| Namespace Prefix | "d" | Default namespace prefix |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create RteXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with AR 3.x file | File parses without errors |
| 3 | Verify namespace map is populated | nsmap contains namespace definitions |
| 4 | Verify module name validation | Module "Rte" is accepted |
| 5 | Extract AUTOSAR version for AR 3.x file | Returns correct AUTOSAR 3.x version string |
| 6 | Detect AUTOSAR version from AR 3.x file | AR version detected as 3.x |
| 7 | Parse AR 4.x file | File parses without errors |
| 8 | Extract AUTOSAR version for AR 4.x file | Returns correct AUTOSAR 4.x version string |
| 9 | Detect AUTOSAR version from AR 4.x file | AR version detected as 4.x |
| 10 | Attempt parsing non-RTE XDM file | Raises ValueError with descriptive message |

## Expected Results

- Namespace map contains at least 3 namespace definitions
- Module name "Rte" is validated successfully
- AUTOSAR version is extracted correctly for both 3.x and 4.x
- AR version detection works correctly (3.x vs 4.x)
- Parsing non-RTE file raises ValueError
- AR 3.x specific handling is triggered for 3.x files
- AR 4.x specific handling is triggered for 4.x files

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No temporary files created during test |
| 2 | Parser instance can be garbage collected |
| 3 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00001 | Parser Layer - XDM file parsing and validation | Covered |
| SWR_RTE_00008 | Non-Functional - Efficient processing of 10MB files | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Design Document | ../requirements/overview.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |