# Test Case: TC_UNIT_REPORTER_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00001 |
| Title | Excel Reporter - Workbook Creation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly creates new workbooks, initializes the workbook structure, and prepares it for worksheet generation.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | Model objects are available for reporting |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Output File Path | "test_output/test_workbook.xlsx" | Output workbook file |
| Workbook Title | "Test Report" | Workbook metadata title |
| Author | "Test Architect" | Workbook metadata author |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create reporter instance | Reporter initialized successfully |
| 2 | Create new workbook | Workbook object created |
| 3 | Verify workbook is empty | No worksheets present initially |
| 4 | Set workbook title | Title metadata set correctly |
| 5 | Set workbook author | Author metadata set correctly |
| 6 | Verify workbook properties | Properties are set as expected |
| 7 | Attempt to create workbook in non-existent directory | Creates directory or raises error |
| 8 | Attempt to create workbook with invalid path | Raises appropriate error |
| 9 | Verify workbook can be saved | File created at specified path |
| 10 | Verify saved file is valid Excel file | File can be opened in Excel |

## Expected Results

- Workbook is created successfully
- Workbook is initially empty
- Metadata properties are set correctly
- Directory creation works or appropriate error raised
- Invalid paths are handled with errors
- Saved file is valid Excel format

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Workbook file exists at output path |
| 2 | Workbook can be opened for reading |
| 3 | No memory leaks in reporter |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00001 | Excel Reporter - Workbook creation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/abstract_xls_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |