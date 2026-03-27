# Reporter Module Unit Test Cases

This document contains all unit test cases for the Reporter module following ISO/IEC/IEEE 29119-3 standard.

---

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
---

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
---

# Test Case: TC_UNIT_REPORTER_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00003 |
| Title | Excel Reporter - Cell Formatting |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly applies formatting to cells, including font, alignment, colors, and borders.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | Worksheet is created and available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Header Font | Bold, size 12 | Header cell font |
| Data Font | Normal, size 11 | Data cell font |
| Alignment Options | Left, Center, Right | Cell alignment options |
| Background Color | Light gray for headers | Header background color |
| Border Style | Thin black borders | Cell border style |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Write header cell with bold font | Cell has bold font |
| 2 | Write data cell with normal font | Cell has normal font |
| 3 | Apply left alignment to cell | Cell content left-aligned |
| 4 | Apply center alignment to cell | Cell content center-aligned |
| 5 | Apply right alignment to cell | Cell content right-aligned |
| 6 | Set header background color | Cell has light gray background |
| 7 | Apply thin black borders | Cell has borders on all sides |
| 8 | Apply number format to numeric cell | Cell formatted as number |
| 9 | Apply date format to date cell | Cell formatted as date |
| 10 | Verify formatting persists after save | Formatting visible in saved Excel file |

## Expected Results

- Font styles are applied correctly
- Alignment options work as expected
- Colors are applied correctly
- Borders are displayed properly
- Number and date formats work correctly
- Formatting persists after save

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Cell formatting is visible in Excel |
| 2 | Formatting doesn't affect cell values |
| 3 | No side effects from formatting operations |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00003 | Excel Reporter - Cell formatting | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/abstract_xls_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_REPORTER_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00004 |
| Title | Excel Reporter - Auto-Width Formatting |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly calculates and applies column widths based on content, ensuring all data is visible and columns are appropriately sized.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | Worksheet is created and populated with data |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Short Content | "ABC" | Test short content |
| Medium Content | "Medium Length Text" | Test medium content |
| Long Content | "This is a very long string that should cause the column to expand" | Test long content |
| Minimum Width | 10 | Minimum column width in characters |
| Maximum Width | 50 | Maximum column width in characters |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Write short content to column | Column width adjusts to short content |
| 2 | Write medium content to column | Column width adjusts to medium content |
| 3 | Write long content to column | Column width adjusts to long content |
| 4 | Verify column width calculation | Width accommodates longest content |
| 5 | Apply minimum width constraint | Column width not less than minimum |
| 6 | Apply maximum width constraint | Column width not exceed maximum |
| 7 | Test multi-column width calculation | All columns sized appropriately |
| 8 | Test width calculation with headers | Headers included in width calculation |
| 9 | Apply auto-width to worksheet | All columns sized automatically |
| 10 | Verify width persists after save | Column widths visible in saved Excel file |

## Expected Results

- Column widths accommodate longest content
- Minimum width constraints are respected
- Maximum width constraints are respected
- All columns are sized appropriately
- Headers are included in width calculation
- Widths persist after save

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Column widths are visible in Excel |
| 2 | All content is visible without manual adjustment |
| 3 | No columns are excessively wide or narrow |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00004 | Excel Reporter - Auto-width formatting | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/abstract_xls_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_REPORTER_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00005 |
| Title | Reporter Layer - Markdown Output |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | Medium |

## Purpose/Objective

Verify that the reporter layer correctly generates Markdown formatted output for OS application data.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | OS application model objects are available |
| 3 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Output File Path | "test_output/OsApp_report.md" | Markdown output file |
| Application Name | "App1" | Application identifier |
| Application Description | "Safety Application" | Application description |
| Mapped Tasks | List of task names | Tasks mapped to application |
| Mapped ISRs | List of ISR names | ISRs mapped to application |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create OsApplicationMarkdownWriter instance | Writer initialized successfully |
| 2 | Generate Markdown output for application | Markdown file created |
| 3 | Verify output file exists | File created at specified path |
| 4 | Verify Markdown structure | File has valid Markdown format |
| 5 | Verify application header | Application name in heading |
| 6 | Verify application description | Description formatted correctly |
| 7 | Verify task list | Tasks listed with correct formatting |
| 8 | Verify ISR list | ISRs listed with correct formatting |
| 9 | Verify table formatting | Tables use correct Markdown syntax |
| 10 | Verify file can be rendered | Markdown renders correctly in viewer |

## Expected Results

- Markdown file is created successfully
- File has valid Markdown structure
- Application data is formatted correctly
- Tables use correct Markdown syntax
- File renders correctly in Markdown viewers
- All application information is included

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Markdown file exists at output path |
| 2 | File can be opened and read |
| 3 | No side effects from generation |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00005 | Reporter Layer - Markdown output | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/os_application_markdown_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_REPORTER_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00006 |
| Title | Reporter Layer - Error Handling |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the reporter layer handles errors consistently, providing clear error messages and preventing system crashes during report generation.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Test data with various error conditions is available |
| 3 | Reporter classes are available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Invalid Model Object | None or malformed object | Test error handling |
| Non-Writable Directory | Directory without write permission | Test permission error |
| Disk Full Condition | Simulated disk full scenario | Test disk error |
| Corrupted Workbook | Partially written workbook | Test recovery |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt to write report with None model | Raises ValueError or TypeError |
| 2 | Verify error message is descriptive | Message indicates what's missing |
| 3 | Attempt to write to non-writable directory | Raises PermissionError or IOError |
| 4 | Verify error message includes path | Message identifies the directory |
| 5 | Attempt to save with disk full simulation | Raises IOError with disk full message |
| 6 | Verify error message indicates disk full | Message is clear about the issue |
| 7 | Attempt to write corrupted workbook | Handles gracefully or raises error |
| 8 | Verify error handling for corrupted data | Error message indicates corruption |
| 9 | Test recovery after error | System remains stable |
| 10 | Verify no partial files from errors | No incomplete output files created |

## Expected Results

- All error conditions are detected
- Error messages are clear and actionable
- Errors include context (path, object, issue)
- No system crashes occur
- Errors are raised with appropriate exception types
- Error handling is consistent across reporter types
- No partial files are created

## Post-conditions

| # | Description |
|---|-------------|
| 1 | System is stable after errors |
| 2 | Reporter can be reused for valid operations |
| 3 | No corrupted state from errors |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00009 | Reporter Layer - Error handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/abstract_xls_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
