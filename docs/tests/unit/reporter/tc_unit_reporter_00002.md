# Test Case: TC_UNIT_REPORTER_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00002 |
| Title | Excel Reporter - Worksheet Management |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly creates, configures, and manages worksheets within a workbook.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | Workbook is created and available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Worksheet Name 1 | "OsTask" | First worksheet name |
| Worksheet Name 2 | "OsIsr" | Second worksheet name |
| Worksheet Name 3 | "OsScheduleTable" | Third worksheet name |
| Column Headers | List of header names | Worksheet column structure |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create worksheet with name "OsTask" | Worksheet created successfully |
| 2 | Verify worksheet name | Name matches "OsTask" |
| 3 | Create second worksheet with name "OsIsr" | Second worksheet created |
| 4 | Verify multiple worksheets | Both worksheets exist in workbook |
| 5 | Attempt to create worksheet with duplicate name | Worksheet renamed or error raised |
| 6 | Set active worksheet | Specified worksheet becomes active |
| 7 | Verify active worksheet | Correct worksheet is active |
| 8 | Delete worksheet | Worksheet removed from workbook |
| 9 | Verify worksheet removed | Worksheet no longer in workbook |
| 10 | Clear all worksheets | Workbook becomes empty |

## Expected Results

- Worksheets are created with correct names
- Multiple worksheets are managed correctly
- Duplicate names are handled appropriately
- Active worksheet can be set
- Worksheets can be deleted
- Workbook state remains consistent

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Workbook contains expected worksheets |
| 2 | Worksheet operations are reversible |
| 3 | No orphaned worksheets remain |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00002 | Excel Reporter - Worksheet management | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/abstract_xls_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |