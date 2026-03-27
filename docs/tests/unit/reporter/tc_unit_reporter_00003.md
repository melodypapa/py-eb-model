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