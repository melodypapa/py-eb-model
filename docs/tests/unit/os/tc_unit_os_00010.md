# Test Case: TC_UNIT_OS_00010

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00010 |
| Title | OS Reporter - Excel Worksheet Generation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS reporter correctly generates Excel worksheets for all OS entity types (tasks, ISRs, schedule tables, counters, alarms, resources, applications) with proper formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | OS model objects are populated with test data |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Output File Path | "test_output/Os_report.xlsx" | Generated Excel file path |
| Worksheets to Generate | OsTask, OsIsr, OsScheduleTable, OsCounter, OsAlarm, OsResource, OsApplication | Expected worksheets |
| Task Count | 5-10 | Number of tasks for testing |
| ISR Count | 3-5 | Number of ISRs for testing |
| Schedule Table Count | 2-3 | Number of schedule tables |
| Column Headers | Name, Priority, Activation, Stack Size, etc. | Expected column structure |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create OsXdmXlsWriter instance | Writer initialized successfully |
| 2 | Generate OsTask worksheet | OsTask worksheet created with all data |
| 3 | Generate OsIsr worksheet | OsIsr worksheet created with all data |
| 4 | Generate OsScheduleTable worksheet | OsScheduleTable worksheet created with all data |
| 5 | Generate OsCounter worksheet | OsCounter worksheet created with all data |
| 6 | Generate OsAlarm worksheet | OsAlarm worksheet created with all data |
| 7 | Generate OsResource worksheet | OsResource worksheet created with all data |
| 8 | Generate OsApplication worksheet | OsApplication worksheet created with all data |
| 9 | Verify column auto-width formatting | Column widths sized to fit content |
| 10 | Verify numeric data centering | Numeric columns are center-aligned |

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
| SWR_OS_00010 | Reporter Layer - Excel worksheet generation and formatting | Covered |
| SWR_OS_00013 | Non-Functional - Excel generation performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Reporter Documentation | ../../src/eb_model/reporter/os_xdm_xls_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |