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