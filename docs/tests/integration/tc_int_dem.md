# DEM Module Integration Test Cases

This document contains all integration test cases for the DEM module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_INT_DEM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_DEM_00001 |
| Title | DEM End-to-End Parser - Complete XDM File Parsing |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the DEM parser can parse a complete DEM XDM file with all containers, creating all model elements with correct values and establishing proper relationships.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid Dem.xdm file with complete configuration is available |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/Dem_complete.xdm` | Complete DEM XDM file |
| Expected Containers | DemGeneral, DemEventParameter, DemDtcClass, DemFaultMemoryConfig | All expected containers |
| Expected Properties | DemDevErrorDetect, DemEnabled, EventId, DtcClass, etc. | All expected properties |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create DemXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with complete Dem.xdm file | File parses without errors |
| 3 | Verify DemGeneral container is created | Container exists with correct name |
| 4 | Verify DemGeneral properties are correct | DevErrorDetect and Enabled match file |
| 5 | Verify DemEventParameter containers are created | All event parameters from file are present |
| 6 | Verify DemDtcClass containers are created | All DTC classes from file are present |
| 7 | Verify DemFaultMemoryConfig containers are created | All fault memory configs present |
| 8 | Verify parent-child relationships | All containers have correct parent references |
| 9 | Verify model element count | Total elements count matches file contents |
| 10 | Verify no parsing errors occurred | Parser completes without exceptions |

## Expected Results

- All expected containers are created from the XDM file
- All property values match the XDM file contents
- Parent-child relationships are correctly established
- No duplicate elements are created
- Model element count matches expected number of containers
- Parser completes successfully without errors

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Parsed DEM model remains in memory for verification |
| 2 | No partial or incomplete model objects exist |
| 3 | EBModel singleton contains updated DEM module |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00001 | Parser Layer - Complete XDM file parsing | Covered |
| SWR_DEM_00005 | End-to-End Parser Workflow | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_dem-module.md |
| Design Document | ../requirements/overview.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_INT_DEM_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_DEM_00002 |
| Title | DEM Reporter Integration - Excel Report Generation |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the DEM reporter can generate a complete Excel report from a parsed DEM model, including all worksheets with correct data and formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | Parsed DEM model is available |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input Model | Parsed DEM model from TC_INT_DEM_00001 | Complete DEM configuration |
| Output File Path | "test_output/Dem_integration_report.xlsx" | Generated Excel file path |
| Expected Worksheets | DemGeneral, DemEventParameter, DemDtcClass, DemFaultMemoryConfig | All expected worksheets |
| Expected Columns | Name, DemDevErrorDetect, DemEnabled, EventId, etc. | All expected column headers |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create DemXdmXlsWriter instance | Writer initialized successfully |
| 2 | Call write() with output path | Excel file generated successfully |
| 3 | Verify output file exists | File created at specified path |
| 4 | Verify file is valid Excel format | File can be opened with openpyxl |
| 5 | Verify DemGeneral worksheet exists | Worksheet is present |
| 6 | Verify DemGeneral data matches model | All values match parsed model |
| 7 | Verify DemEventParameter worksheet exists | Worksheet is present |
| 8 | Verify DemEventParameter data matches model | All values match parsed model |
| 9 | Verify DemDtcClass worksheet exists | Worksheet is present |
| 10 | Verify DemDtcClass data matches model | All values match parsed model |
| 11 | Verify all column headers are correct | Headers match expected structure |
| 12 | Verify formatting is applied | Auto-width and numeric centering applied |

## Expected Results

- Excel file is created at specified path
- File is valid and can be opened
- All expected worksheets are present
- All data values match the parsed model
- Column headers are correct for each worksheet
- Formatting is applied correctly
- No data corruption or missing values

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file persists for review |
| 2 | Parsed model remains unchanged |
| 3 | No memory leaks in reporter |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00003 | Reporter Layer - Excel report generation | Covered |
| SWR_DEM_00013 | Non-Functional - Excel generation performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_dem-module.md |
| Reporter Documentation | ../../src/eb_model/reporter/dem_xdm_xls_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_INT_DEM_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_DEM_00003 |
| Title | DEM CLI Integration - Command-Line Execution |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the DEM CLI command executes end-to-end, from command-line parsing through XDM parsing to Excel report generation.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI entry point is registered (dem-xdm-xlsx) |
| 3 | Test XDM file is available |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Command | `dem-xdm-xlsx input.xdm output.xlsx` | Basic CLI command |
| Input File | `data/test/Dem_complete.xdm` | Test input file |
| Output File | `test_output/Dem_cli_output.xlsx` | Test output file |
| Verbose Flag | `-v` or `--verbose` | Enable verbose logging |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command with valid input | Command completes successfully |
| 2 | Verify exit code is 0 | Exit code indicates success |
| 3 | Verify output file exists | File created at specified path |
| 4 | Verify output file is valid Excel | File can be opened and read |
| 5 | Verify all expected worksheets present | All DEM worksheets exist |
| 6 | Execute CLI command with verbose flag | Command completes with logging output |
| 7 | Verify verbose output includes progress | Parsing and export progress logged |
| 8 | Execute CLI with missing input file | Command exits with error |
| 9 | Verify error message is descriptive | Error message indicates missing file |
| 10 | Verify exit code is non-zero for error | Exit code indicates failure |

## Expected Results

- CLI command executes successfully for valid input
- Excel file is generated with correct contents
- Exit codes are appropriate (0 for success, non-zero for error)
- Verbose mode provides helpful progress information
- Error messages are clear and descriptive
- No orphaned processes remain

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Generated Excel file persists for review |
| 2 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00004 | CLI Interface - End-to-end command execution | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_dem-module.md |
| CLI Documentation | ../../src/eb_model/cli/dem_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_INT_DEM_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_DEM_00004 |
| Title | DEM Error Handling Integration - Malformed XDM File |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the DEM parser correctly handles malformed XDM files at the integration level, providing appropriate error messages without creating incomplete model objects.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Malformed XDM test files are available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Malformed File 1 | Missing closing tag | Verify missing tag handling |
| Malformed File 2 | Invalid attribute type | Verify type validation |
| Malformed File 3 | Missing required element | Verify required element validation |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt to parse file with missing closing tag | Parser raises XMLSyntaxError or ValueError |
| 2 | Verify error message is descriptive | Error message indicates the problem |
| 3 | Verify no incomplete model objects created | EBModel does not contain partial data |
| 4 | Attempt to parse file with invalid attribute type | Parser raises ValueError |
| 5 | Verify error includes field and expected type | Message is actionable |
| 6 | Verify model remains clean | No corrupted data in model |
| 7 | Attempt to parse file with missing required element | Parser raises ValueError or logs warning |
| 8 | Verify parser can be reused for valid file | Parser works correctly after error |

## Expected Results

- Malformed files are detected and rejected
- Error messages are clear and descriptive
- No incomplete or corrupted model objects are created
- Parser can recover and process valid files after errors
- Error messages include context about the problem

## Post-conditions

| # | Description |
|---|-------------|
| 1 | System returns to clean state |
| 2 | No partial model objects remain in memory |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00015 | Non-Functional - Malformed XML error handling | Covered |
| SWR_DEM_00017 | Non-Functional - Required element validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_dem-module.md |
| Parser Documentation | ../../src/eb_model/parser/dem_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

**Document End**