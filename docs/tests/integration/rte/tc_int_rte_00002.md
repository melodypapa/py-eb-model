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