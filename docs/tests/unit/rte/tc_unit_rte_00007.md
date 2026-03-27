# Test Case: TC_UNIT_RTE_00007

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00007 |
| Title | RTE Reporter - Excel Worksheet Generation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE reporter correctly generates Excel worksheets for all RTE entity types (BSW components, SW components, event mappings) with proper formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | RTE model objects are populated with test data |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Output File Path | "test_output/Rte_report.xlsx" | Generated Excel file path |
| Worksheets to Generate | BswComponent, SwComponent, EventMapping | Expected worksheets |
| BSW Component Count | 5-10 | Number of BSW components |
| SW Component Count | 5-10 | Number of SW components |
| Event Mapping Count | 10-20 | Number of event mappings |
| Column Headers | Name, Type, Version, Instance, etc. | Expected column structure |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create RteXdmXlsWriter instance | Writer initialized successfully |
| 2 | Generate BswComponent worksheet | BswComponent worksheet created with all data |
| 3 | Generate SwComponent worksheet | SwComponent worksheet created with all data |
| 4 | Generate EventMapping worksheet | EventMapping worksheet created with all data |
| 5 | Verify column auto-width formatting | Column widths sized to fit content |
| 6 | Verify numeric data centering | Numeric columns are center-aligned |
| 7 | Verify AR version information | AR version displayed correctly |
| 8 | Verify BSW component port counts | Port counts displayed correctly |
| 9 | Verify SW component runnable entity counts | Runnable entity counts displayed correctly |
| 10 | Verify event task references | Task references displayed correctly |

## Expected Results

- All expected worksheets are created
- All data is populated correctly
- Column formatting is applied (auto-width, centering for numeric)
- Data types are correct (strings for text, numbers for numeric values)
- File is valid and can be opened in Excel
- Performance meets requirements (< 5 seconds for typical file)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file persists for review |
| 2 | No memory leaks in reporter |
| 3 | Model objects remain unchanged after export |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00007 | Reporter Layer - Excel worksheet generation and formatting | Covered |
| SWR_RTE_00013 | Non-Functional - Excel generation performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Reporter Documentation | ../../src/eb_model/reporter/rte_xdm_xls_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |