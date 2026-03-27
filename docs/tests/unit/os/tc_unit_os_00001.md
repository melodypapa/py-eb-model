# Test Case: TC_UNIT_OS_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00001 |
| Title | OS Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts XML namespace definitions from EB Tresos XDM files, validates the module name, extracts AUTOSAR/software version information, and properly initializes the parser. This test ensures the foundation for all subsequent OS configuration parsing.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Test XDM file (valid Os.xdm) is available at known location |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/Os_valid.xdm` | Valid OS XDM file for testing |
| Module Name | "Os" | Expected root module name |
| AUTOSAR Version | "4.3.0" | Example AUTOSAR version |
| Software Version | "1.2.3" | Example software version |
| Namespace Prefix | "d" | Default namespace prefix |
| Namespace URI | "http://www.tresos.de/_projects/DataModel2/06/data.xsd" | Data namespace URI |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create OsXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with valid Os.xdm file | File parses without errors |
| 3 | Verify namespace map is populated | nsmap contains namespace definitions |
| 4 | Verify module name validation | Module "Os" is accepted, others raise ValueError |
| 5 | Extract AUTOSAR version | Returns correct AUTOSAR version string |
| 6 | Extract software version | Returns correct software version string |
| 7 | Attempt parsing non-OS XDM file | Raises ValueError with descriptive message |

## Expected Results

- Namespace map contains at least 3 namespace definitions
- Module name "Os" is validated successfully
- AUTOSAR version matches expected value from file
- Software version matches expected value from file
- Parsing non-OS file raises ValueError with message "Invalid module name"
- Parsing completes within 2 seconds for 5MB file

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No temporary files created during test |
| 2 | Parser instance can be garbage collected |
| 3 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00001 | Parser Layer - XDM file parsing and validation | Covered |
| SWR_OS_00012 | Non-Functional - Efficient processing of 10MB files | Covered |
| SWR_OS_00020 | Non-Functional - Inherit from AbstractEbModelParser | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Design Document | ../requirements/overview.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |