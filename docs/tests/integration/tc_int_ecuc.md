# EcuC Module Integration Test Cases

This document contains all integration test cases for the EcuC (ECU Configuration) module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_INT_ECUC_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_ECUC_00001 |
| Title | EcuC Module - End-to-End Parsing and Excel Export |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete end-to-end workflow of parsing an EcuC XDM file, modeling all EcuC entities (partitions, partition collections, SW component references), and exporting the configuration to Excel.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Complete EcuC.xdm file with all entity types is available |
| 3 | Output directory for Excel file is writable |
| 4 | No other instances of EBModel exist |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/EcuC_complete.xdm` | EcuC XDM with all entity types |
| Output File | `test_output/EcuC_test.xlsx` | Generated Excel report |
| Partition Count | 3-5 | Expected number of partitions |
| SW Component References | 10-20 total | Total SW component references |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command | Command completes successfully |
| 2 | Verify Excel file exists | File created at output path |
| 3 | Verify partition worksheet | All partitions displayed |
| 4 | Verify partition names | All partition names correct |
| 5 | Verify BSW partition flags | Default BSW flags correct |
| 6 | Verify restart capability flags | Restart flags correct |
| 7 | Verify SW component references | All references displayed |
| 8 | Verify column formatting | Columns sized correctly |
| 9 | Verify execution time | Completes within 3 seconds |

## Expected Results

- Excel file generated successfully
- All partitions extracted and displayed
- SW component references correctly linked
- Column formatting applied
- Performance meets requirements

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file persists for review |
| 2 | No memory leaks |
| 3 | EBModel can be reset |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUC_00001 | Parser Layer - XDM file parsing | Covered |
| SWR_ECUC_00002 | Partition Configuration Parsing | Covered |
| SWR_ECUC_00003 | Partition Collection Parsing | Covered |
| SWR_ECUC_00004 | Reporter Layer - Excel generation | Covered |
| SWR_ECUC_00005 | CLI Interface - Command execution | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_ecuc-module.md |
| Parser Documentation | ../../src/eb_model/parser/ecuc_xdm_parser.py |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/ecuc_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_INT_ECUC_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_ECUC_00002 |
| Title | EcuC Module - Multi-Core Partition Configuration |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the EcuC parser can handle multi-core configurations with multiple partitions assigned to different cores.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Multi-core EcuC.xdm file is available |
| 3 | Output directory is writable |
| 4 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/EcuC_multicore.xdm` | Multi-core EcuC XDM |
| Partition Count | 4+ | Multiple partitions |
| Core Count | 2+ | Multiple cores |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command with multi-core file | Command completes successfully |
| 2 | Verify all partitions extracted | Partition count matches |
| 3 | Verify BSW partition assignment | One partition marked as default BSW |
| 4 | Verify SW component distribution | Components distributed across partitions |
| 5 | Verify partition references | References correctly resolved |

## Expected Results

- Multi-core configuration is parsed correctly
- Partitions are assigned correctly
- BSW partition is identified
- SW component distribution is correct

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file with multi-core config persists |
| 2 | No memory leaks |
| 3 | EBModel can be reset |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUC_00002 | Partition Configuration Parsing | Covered |
| SWR_ECUC_00003 | Partition Collection Parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_ecuc-module.md |
| Parser Documentation | ../../src/eb_model/parser/ecuc_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_INT_ECUC_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_ECUC_00003 |
| Title | EcuC Module - Error Recovery |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the EcuC module gracefully handles error conditions and provides clear error messages.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Test files with error conditions are available |
| 3 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Missing File | Non-existent file path | Verify file not found handling |
| Invalid Module | XDM with wrong module name | Verify module validation |
| Empty File | Empty .xdm file | Verify empty file handling |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute with non-existent file | Command exits with error, file not found message |
| 2 | Execute with invalid module name | Command exits with error, indicates wrong module |
| 3 | Execute with empty file | Command exits with error |
| 4 | Verify system recovers | Subsequent valid operations work |

## Expected Results

- Missing files produce clear error messages
- Invalid module names are detected
- System recovers after errors
- Error codes are appropriate

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No corrupted output files |
| 2 | System returns to clean state |
| 3 | EBModel can be reset |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUC_00001 | Parser Layer - Module validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_ecuc-module.md |
| CLI Documentation | ../../src/eb_model/cli/ecuc_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |