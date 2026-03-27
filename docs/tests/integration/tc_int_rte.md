# RTE Module Integration Test Cases

This document contains all integration test cases for the RTE module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_INT_RTE_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_RTE_00001 |
| Title | RTE Module - End-to-End Parsing and Excel Export (AR 3.x) |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete end-to-end workflow of parsing an AR 3.x RTE XDM file, modeling all RTE entities (BSW components, SW components, event mappings), and exporting the configuration to a multi-sheet Excel file with proper formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Complete AR 3.x Rte.xdm file with all entity types is available |
| 3 | Output directory for Excel file is writable |
| 4 | No other instances of EBModel exist (singleton pattern) |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/Rte_ar3_complete.xdm` | AR 3.x RTE XDM with all entity types |
| Output File | `test_output/Rte_ar3_test.xlsx` | Generated Excel report |
| AUTOSAR Version | "3.2.1" | AUTOSAR 3.x version |
| Expected Worksheets | BswComponent, SwComponent, EventMapping | Expected worksheets |
| BSW Component Count | 5-10 | Number of BSW components |
| SW Component Count | 5-10 | Number of SW components |
| Event Mapping Count | 10-20 | Number of event mappings |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command: `rte-xdm-xlsx data/test/Rte_ar3_complete.xdm test_output/Rte_ar3_test.xlsx` | Command completes successfully |
| 2 | Verify Excel file exists | File created at output path |
| 3 | Open Excel file and verify worksheets | All expected worksheets present |
| 4 | Verify AUTOSAR version displayed | Version shown as AR 3.x |
| 5 | Verify BSW component worksheet | All BSW components extracted with AR 3.x structure |
| 6 | Verify SW component worksheet | All SW components extracted with AR 3.x structure |
| 7 | Verify event mapping worksheet | All event mappings extracted |
| 8 | Verify event-to-task mappings | Task references correctly populated |
| 9 | Verify runnable entities | Runnable entities displayed correctly |
| 10 | Verify port definitions | Port structure matches AR 3.x format |
| 11 | Verify column auto-width formatting | Columns sized to fit content |
| 12 | Verify numeric data centering | Numeric columns are center-aligned |
| 13 | Execute with --skip-bsw-component flag | BSW worksheet is skipped |
| 14 | Execute with --skip-sw-component flag | SW worksheet is skipped |
| 15 | Verify total execution time | Execution completes within 5 seconds for 10MB file |

## Expected Results

- Excel file generated successfully with no errors
- All expected worksheets present (or reduced when skip flags used)
- AUTOSAR version correctly identified as AR 3.x
- BSW component data includes AR 3.x specific structure
- SW component data includes AR 3.x specific structure
- Event mappings correctly link events to tasks
- Runnable entities are displayed correctly
- Port structure follows AR 3.x format
- Column formatting applied consistently
- Total execution time < 5 seconds for 10MB file
- Memory usage remains stable

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file persists for review |
| 2 | No memory leaks in parser/reporter |
| 3 | EBModel singleton can be reset for next test |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00001 | Parser Layer - XDM file parsing | Covered |
| SWR_RTE_00002 | BSW Component Instance Extraction | Covered |
| SWR_RTE_00003 | SW Component Instance Extraction | Covered |
| SWR_RTE_00004 | Event to Task Mapping | Covered |
| SWR_RTE_00005 | AR 3.x Version Support | Covered |
| SWR_RTE_00007 | Reporter Layer - Excel generation | Covered |
| SWR_RTE_00011 | Non-Functional - AR 3.x specific handling | Covered |
| SWR_RTE_00013 | Non-Functional - Excel performance | Covered |
| SWR_RTE_00014 | CLI Interface - Command execution | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| System Overview | ../requirements/overview.md |
| Parser Documentation | ../../src/eb_model/parser/rte_xdm_parser.py |
| Reporter Documentation | ../../src/eb_model/reporter/rte_xdm_xls_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_INT_RTE_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_RTE_00002 |
| Title | RTE Module - End-to-End Parsing and Excel Export (AR 4.x) |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete end-to-end workflow of parsing an AR 4.x RTE XDM file, modeling all RTE entities with AR 4.x specific features, and exporting the configuration to a multi-sheet Excel file.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Complete AR 4.x Rte.xdm file with all entity types is available |
| 3 | Output directory is writable |
| 4 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/Rte_ar4_complete.xdm` | AR 4.x RTE XDM with all entity types |
| Output File | `test_output/Rte_ar4_test.xlsx` | Generated Excel report |
| AUTOSAR Version | "4.3.0" | AUTOSAR 4.x version |
| Expected Worksheets | BswComponent, SwComponent, EventMapping | Expected worksheets |
| BSW Component Count | 5-10 | Number of BSW components |
| SW Component Count | 5-10 | Number of SW components |
| Event Mapping Count | 10-20 | Number of event mappings |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command with AR 4.x file | Command completes successfully |
| 2 | Verify Excel file generated | File created successfully |
| 3 | Verify AUTOSAR version displayed | Version shown as AR 4.x |
| 4 | Verify BSW component worksheet | All BSW components extracted with AR 4.x structure |
| 5 | Verify SW component worksheet | All SW components extracted with AR 4.x structure |
| 6 | Verify port interface definitions | Port interfaces follow AR 4.x format |
| 7 | Verify communication patterns | Communication patterns extracted correctly |
| 8 | Verify service needs | Service needs displayed correctly |
| 9 | Verify mode switch events | AR 4.x specific events extracted |
| 10 | Verify event-to-task mappings | Task references correctly populated |
| 11 | Verify column auto-width formatting | Columns sized to fit content |
| 12 | Verify total execution time | Execution completes within 5 seconds for 10MB file |

## Expected Results

- Excel file generated successfully with no errors
- AUTOSAR version correctly identified as AR 4.x
- BSW component data includes AR 4.x specific structure
- SW component data includes AR 4.x specific structure
- Port interface definitions follow AR 4.x format
- Communication patterns are extracted correctly
- Service needs are displayed correctly
- Mode switch events are extracted
- All event mappings are correct
- Performance meets requirements

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file with AR 4.x configuration persists for review |
| 2 | No memory leaks or resource exhaustion |
| 3 | EBModel can be reset for next test |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00001 | Parser Layer - XDM file parsing | Covered |
| SWR_RTE_00002 | BSW Component Instance Extraction | Covered |
| SWR_RTE_00003 | SW Component Instance Extraction | Covered |
| SWR_RTE_00004 | Event to Task Mapping | Covered |
| SWR_RTE_00006 | AR 4.x Version Support | Covered |
| SWR_RTE_00007 | Reporter Layer - Excel generation | Covered |
| SWR_RTE_00012 | Non-Functional - AR 4.x specific handling | Covered |
| SWR_RTE_00013 | Non-Functional - Excel performance | Covered |
| SWR_RTE_00014 | CLI Interface - Command execution | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Parser Documentation | ../../src/eb_model/parser/rte_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_INT_RTE_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_RTE_00003 |
| Title | RTE Module - Mixed Version Handling |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | Medium |

## Purpose/Objective

Verify that the RTE parser can handle switching between AR 3.x and AR 4.x versions within a single session, correctly adapting to each version's specific features and schemas.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Both AR 3.x and AR 4.x test files are available |
| 3 | Output directory is writable |
| 4 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| AR3 Input File | `data/test/Rte_ar3.xdm` | AR 3.x test file |
| AR4 Input File | `data/test/Rte_ar4.xdm` | AR 4.x test file |
| AR3 Output File | `test_output/Rte_ar3.xlsx` | AR 3.x output |
| AR4 Output File | `test_output/Rte_ar4.xlsx` | AR 4.x output |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse AR 3.x file | File parsed successfully, AR 3.x mode activated |
| 2 | Generate AR 3.x Excel output | Output file created with AR 3.x structure |
| 3 | Reset EBModel singleton | EBModel is clean, no AR 3.x artifacts |
| 4 | Parse AR 4.x file | File parsed successfully, AR 4.x mode activated |
| 5 | Generate AR 4.x Excel output | Output file created with AR 4.x structure |
| 6 | Verify no cross-version contamination | AR 3.x data not in AR 4.x output and vice versa |
| 7 | Verify AR 3.x specific features in AR 3.x output | Runnable entities, port structure correct |
| 8 | Verify AR 4.x specific features in AR 4.x output | Port interfaces, communication patterns correct |
| 9 | Parse AR 3.x file again | Parser correctly switches back to AR 3.x mode |
| 10 | Generate second AR 3.x output | Output matches first AR 3.x output |

## Expected Results

- Parser correctly switches between AR 3.x and AR 4.x modes
- Each version's specific features are handled correctly
- No cross-version contamination occurs
- Multiple version switches work correctly
- Outputs for same version are consistent

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Both output files persist for review |
| 2 | EBModel can be reset for next test |
| 3 | No version state pollution remains |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00005 | AR 3.x Version Support | Covered |
| SWR_RTE_00006 | AR 4.x Version Support | Covered |
| SWR_RTE_00011 | Non-Functional - AR 3.x specific handling | Covered |
| SWR_RTE_00012 | Non-Functional - AR 4.x specific handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Parser Documentation | ../../src/eb_model/parser/rte_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
