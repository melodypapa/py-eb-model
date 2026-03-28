# Reporter Module Unit Test Cases

This document contains all unit test cases for the Reporter module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_REPORTER_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00001 |
| Title | Excel Reporter - Initialization |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly initializes, creates new workbooks, and prepares the workbook structure for worksheet generation.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create ExcelReporter instance | Reporter initialized successfully |
| 2 | Verify workbook is created | Workbook object exists |
| 3 | Verify workbook has initial worksheet | Default worksheet exists |
| 4 | Verify logger is initialized | Logger object exists |

## Expected Results

- Reporter initializes successfully
- Workbook object is created
- Logger is properly configured
- No errors during initialization

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Reporter instance is ready for use |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00001 | Excel Reporter - Workbook creation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00002 |
| Title | Excel Reporter - Cell Writing |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly writes cells with various values.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Cell Value | "Test Data" | Test cell content |
| Row Number | 1 | Test row position |
| Column Number | 1 | Test column position |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Write cell with value | Cell value is set correctly |
| 2 | Write cell with None value | Cell value is None |
| 3 | Write cell with empty string | Cell value is empty string |

## Expected Results

- Cell values are written correctly
- None and empty values are handled

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Cell values are correctly written |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00003 | Excel Reporter - Cell formatting | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00003 |
| Title | Excel Reporter - Cell Formatting with Number Format |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly applies number formatting to cells.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Cell Value | 123.456 | Test numeric value |
| Number Format | "0.00" | Test number formatting |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Write cell with number format | Cell value and number format are set |

## Expected Results

- Cell value is set correctly
- Number format is applied

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Number formatting is applied |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00003 | Excel Reporter - Cell formatting | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00004 |
| Title | Excel Reporter - Title Row Writing |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly writes title rows with center alignment.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Title Row | ["Column A", "Column B", "Column C"] | Test title row data |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Write title row | All column values are written |
| 2 | Verify center alignment | All cells have center alignment |

## Expected Results

- Title row values are written correctly
- All cells have center alignment

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Title row is correctly formatted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00003 | Excel Reporter - Cell formatting | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00005 |
| Title | Excel Reporter - Boolean Formatting |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly formats boolean values for output.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Boolean True | True | Test True value |
| Boolean False | False | Test False value |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Format boolean True | Returns "Y" |
| 2 | Format boolean False | Returns "" |

## Expected Results

- True values are formatted as "Y"
- False values are formatted as ""

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Boolean values are formatted correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00004 | Excel Reporter - Data formatting | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00006 |
| Title | Excel Reporter - Boolean Cell Writing |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly writes boolean cells with formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Boolean True | True | Test True value |
| Boolean False | False | Test False value |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Write bool cell with True | Cell value is "Y" and center-aligned |
| 2 | Write bool cell with False | Cell value is "" and center-aligned |

## Expected Results

- True values are formatted as "Y" with center alignment
- False values are formatted as "" with center alignment

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Boolean cell formatting is correct |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00004 | Excel Reporter - Data formatting | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00007

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00007 |
| Title | Excel Reporter - Auto-Width Formatting |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly calculates and applies column widths based on content.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Short Content | "Short" | Test short content |
| Medium Content | "Medium Length" | Test medium content |
| Long Content | "This is a very long string that should cause the column to expand" | Test long content |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Write short content to column A | Column A width adjusts to short content |
| 2 | Write medium content to column B | Column B width adjusts to medium content |
| 3 | Write long content to column C | Column C width adjusts to long content |
| 4 | Apply auto-width to worksheet | All columns sized appropriately |

## Expected Results

- Column widths accommodate longest content
- All columns are sized appropriately

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Column widths are visible in Excel |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00004 | Excel Reporter - Auto-width formatting | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00008

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00008 |
| Title | Excel Reporter - Auto-Width with Customized Widths |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly applies customized column widths.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Customized Width | 50 | Test customized column width |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Write data to column A | Column A width adjusts to content |
| 2 | Apply auto-width with customized dict | Column A uses customized width |

## Expected Results

- Customized widths are respected
- Other columns use auto-width

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Column widths are correctly set |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00004 | Excel Reporter - Auto-width formatting | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00009

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00009 |
| Title | Excel Reporter - Auto-Width with Zero Customized Width |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter handles zero width customization.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Zero Width | 0 | Test zero width customization |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Write data to column A | Column A has content |
| 2 | Apply auto-width with zero width | Column A uses auto-width (not zero) |

## Expected Results

- Zero width is not applied
- Auto-width is used instead

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Column width is set correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00004 | Excel Reporter - Auto-width formatting | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00010

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00010 |
| Title | Excel Reporter - Auto-Width with Positive Customized Width |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly applies positive customized column widths.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Positive Width | 50 | Test positive customized width |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Write data to column A | Column A has content |
| 2 | Apply auto-width with positive customized width | Column A uses customized width |

## Expected Results

- Positive customized width is applied
- Column width matches specified value

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Column width is correctly set |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00004 | Excel Reporter - Auto-width formatting | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00011

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00011 |
| Title | Excel Reporter - Workbook Save |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter correctly saves workbooks to file.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Cell Data | "Test Content" | Test data to write |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Write data to workbook | Data is written to cells |
| 2 | Save workbook to file | File is created at specified path |
| 3 | Verify file exists | File exists at output path |
| 4 | Verify file size | File size is greater than 0 |
| 5 | Load saved workbook | Workbook can be opened for reading |
| 6 | Verify saved data | Data matches what was written |

## Expected Results

- Workbook is saved successfully
- File exists at specified path
- File has non-zero size
- File can be opened by openpyxl
- Saved data is intact

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Workbook file exists at output path |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00002 | Excel Reporter - Excel output | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00012

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00012 |
| Title | Excel Reporter - Save to Invalid Path |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Excel reporter handles invalid file paths appropriately.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Invalid Path | "/nonexistent/directory/test.xlsx" | Test invalid path |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt to save to invalid directory | Raises OSError |

## Expected Results

- Error conditions are detected
- OSError is raised

## Post-conditions

| # | Description |
|---|-------------|
| 1 | System is stable after error |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00009 | Reporter Layer - Error handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00013

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00013 |
| Title | Excel Reporter - Workbook Can Be Loaded After Save |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that saved workbooks can be loaded and data is intact.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Various Data Types | String, Number, Boolean, None | Test various data types |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Write various data types to cells | Data is written |
| 2 | Save workbook | File is created |
| 3 | Load saved workbook | Workbook can be opened |
| 4 | Verify all data | All data matches what was written |

## Expected Results

- Workbook can be loaded after save
- All data types are preserved
- None values are preserved

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Workbook file is valid Excel format |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00002 | Excel Reporter - Excel output | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/abstract.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00014

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00014 |
| Title | Os Excel Reporter - File Creation |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Os Excel reporter correctly creates Excel files with expected sheets.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create OsXdmXlsWriter instance | Writer initialized |
| 2 | Call write() method | Excel file created |
| 3 | Verify file exists | File exists at output path |
| 4 | Verify expected sheets | Sheets "OsApplications" and "OsIsr" exist |

## Expected Results

- Excel file is created successfully
- Expected sheets are present

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file exists at output path |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00002 | Excel Reporter - Excel output | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/os_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00015

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00015 |
| Title | Com Excel Reporter - File Creation with Data
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Com Excel reporter correctly creates Excel files with ComGeneral data.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| EnableUserSupport | True | ComGeneral configuration |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create ComXdmXlsWriter instance | Writer initialized |
| 2 | Create EBModel with ComGeneral | Model created with data |
| 3 | Call write() method | Excel file created |
| 4 | Verify ComGeneral sheet exists | Sheet "ComGeneral" exists |
| 5 | Verify data in sheet | Data is written correctly |

## Expected Results

- Excel file is created successfully
- File has correct sheets
- Data is written correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file exists at output path |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00002 | Excel Reporter - Excel output | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/com_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00016

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00016 |
| Title | ComM Excel Reporter - File Creation |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the ComM Excel reporter correctly creates Excel files with ComM channel data.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Channel Name | "ComMChannel_1" | ComM channel name |
| Channel ID | 1 | ComM channel ID |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create ComMXdmXlsWriter instance | Writer initialized |
| 2 | Create EBModel with ComM channel | Model created with data |
| 3 | Call write() method | Excel file created |
| 4 | Verify data in sheet | Data is written correctly |

## Expected Results

- Excel file is created successfully
- Data is written correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file exists at output path |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00002 | Excel Reporter - Excel output | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/comm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00017

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00017 |
| Title | Crc Excel Reporter - File Creation |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Crc Excel reporter correctly creates Excel files with CrcConfig data.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| CRC ID | 1 | CRC configuration ID |
| CRC Type | "CRC_16" | CRC configuration type |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create CrcXdmXlsWriter instance | Writer initialized |
| 2 | Create EBModel with CrcConfig | Model created with data |
| 3 | Call write() method | Excel file created |
| 4 | Verify data in sheet | Data is written correctly |

## Expected Results

- Excel file is created successfully
- Data is written correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file exists at output path |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00002 | Excel Reporter - Excel output | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/crc_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00018

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00018 |
| Title | IpduM Excel Reporter - File Creation |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the IpduM Excel reporter correctly creates Excel files with IpduMDynPdu data.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| PDU ID | 1 | IpduM dynamic PDU ID |
| PDU Length | 8 | IpduM dynamic PDU length |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create IpduMXdmXlsWriter instance | Writer initialized |
| 2 | Create EBModel with IpduMDynPdu | Model created with data |
| 3 | Call write() method | Excel file created |
| 4 | Verify data in sheet | Data is written correctly |

## Expected Results

- Excel file is created successfully
- Data is written correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file exists at output path |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00002 | Excel Reporter - Excel output | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/ipdum_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00019

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00019 |
| Title | LdCom Excel Reporter - File Creation |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the LdCom Excel reporter correctly creates Excel files.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create LdComXdmXlsWriter instance | Writer initialized |
| 2 | Create EBModel with LdCom | Model created |
| 3 | Call write() method | Excel file created |
| 4 | Verify file exists | File exists at output path |

## Expected Results

- Excel file is created successfully
- File can be opened in Excel

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file exists at output path |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00002 | Excel Reporter - Excel output | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/ldcom_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00020

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00020 |
| Title | Nm Excel Reporter - File Creation |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the Nm Excel reporter correctly creates Excel files with NmChannel data.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Channel Name | "NmChannel_1" | Nm channel name |
| Channel ID | 1 | Nm channel ID |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create NmXdmXlsWriter instance | Writer initialized |
| 2 | Create EBModel with NmChannel | Model created with data |
| 3 | Call write() method | Excel file created |
| 4 | Verify data in sheet | Data is written correctly |

## Expected Results

- Excel file is created successfully
- Data is written correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file exists at output path |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00002 | Excel Reporter - Excel output | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/nm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_REPORTER_00021

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_REPORTER_00021 |
| Title | PduR Excel Reporter - File Creation |
| Version | 1.0 |
| Date | 2026-03-28 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the PduR Excel reporter correctly creates Excel files with PduRRoutingTableEntry data.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Entry ID | 1 | Routing table entry ID |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create PduRXdmXlsWriter instance | Writer initialized |
| 2 | Create EBModel with PduRRoutingTableEntry | Model created with data |
| 3 | Call write() method | Excel file created |
| 4 | Verify data in sheet | Data is written correctly |

## Expected Results

- Excel file is created successfully
- Data is written correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file exists at output path |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_REPORTER_00002 | Excel Reporter - Excel output | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/pdur_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-28 | Test Architect | Initial test case |

---

**Document End**