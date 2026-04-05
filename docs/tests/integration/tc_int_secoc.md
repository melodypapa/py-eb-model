# SECOC Module Integration Test Cases

This document contains all integration test cases for the SECOC module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_INT_SECOC_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_SECOC_00001 |
| Title | SECOC End-to-End Parser - Complete XDM File Parsing |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the SECOC parser can parse a complete SECOC XDM file with all containers, creating all model elements with correct values and establishing proper relationships.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid SecOC.xdm file with complete configuration is available |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/SecOC_complete.xdm` | Complete SECOC XDM file |
| Expected Containers | SecOCGeneral, SecOCGlobalConfig, SecOCChannelConfig | All expected containers |
| Expected Properties | DevErrorDetect, Enabled, KeyId, AuthTxDataLengthN | All expected properties |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create SecOCXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with complete SecOC.xdm file | File parses without errors |
| 3 | Verify SecOCGeneral container is created | Container exists with correct name |
| 4 | Verify SecOCGeneral properties are correct | DevErrorDetect and Enabled match file |
| 5 | Verify SecOCGlobalConfig container is created | Container exists with correct name |
| 6 | Verify SecOCGlobalConfig properties are correct | All properties match file |
| 7 | Verify SecOCChannelConfig containers are created | All channels from file are present |
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
| 1 | Parsed SECOC model remains in memory for verification |
| 2 | No partial or incomplete model objects exist |
| 3 | EBModel singleton contains updated SECOC module |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_SECOC_00001 | Parser Layer - Complete XDM file parsing | Covered |
| SWR_SECOC_00005 | End-to-End Parser Workflow | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_secoc-module.md |
| Design Document | ../requirements/overview.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_INT_SECOC_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_SECOC_00002 |
| Title | SECOC Reporter Integration - Excel Report Generation |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the SECOC reporter can generate a complete Excel report from a parsed SECOC model, including all worksheets with correct data and formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | Parsed SECOC model is available |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input Model | Parsed SECOC model from TC_INT_SECOC_00001 | Complete SECOC configuration |
| Output File Path | "test_output/SecOC_integration_report.xlsx" | Generated Excel file path |
| Expected Worksheets | SecOCGeneral, SecOCGlobalConfig, SecOCChannelConfig | All expected worksheets |
| Expected Columns | Name, DevErrorDetect, Enabled, KeyId, etc. | All expected column headers |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create SecOCXdmXlsWriter instance | Writer initialized successfully |
| 2 | Call write() with output path | Excel file generated successfully |
| 3 | Verify output file exists | File created at specified path |
| 4 | Verify file is valid Excel format | File can be opened with openpyxl |
| 5 | Verify SecOCGeneral worksheet exists | Worksheet is present |
| 6 | Verify SecOCGeneral data matches model | All values match parsed model |
| 7 | Verify SecOCGlobalConfig worksheet exists | Worksheet is present |
| 8 | Verify SecOCGlobalConfig data matches model | All values match parsed model |
| 9 | Verify SecOCChannelConfig worksheets exist | All channel worksheets present |
| 10 | Verify all column headers are correct | Headers match expected structure |
| 11 | Verify formatting is applied | Auto-width and numeric centering applied |

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
| SWR_SECOC_00003 | Reporter Layer - Excel report generation | Covered |
| SWR_SECOC_00013 | Non-Functional - Excel generation performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_secoc-module.md |
| Reporter Documentation | ../../src/eb_model/reporter/secoc_xdm_xls_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_INT_SECOC_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_SECOC_00003 |
| Title | SECOC CLI Integration - Command-Line Execution |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the SECOC CLI command executes end-to-end, from command-line parsing through XDM parsing to Excel report generation.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI entry point is registered (secoc-xdm-xlsx) |
| 3 | Test XDM file is available |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Command | `secoc-xdm-xlsx input.xdm output.xlsx` | Basic CLI command |
| Input File | `data/test/SecOC_complete.xdm` | Test input file |
| Output File | `test_output/SecOC_cli_output.xlsx` | Test output file |
| Verbose Flag | `-v` or `--verbose` | Enable verbose logging |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command with valid input | Command completes successfully |
| 2 | Verify exit code is 0 | Exit code indicates success |
| 3 | Verify output file exists | File created at specified path |
| 4 | Verify output file is valid Excel | File can be opened and read |
| 5 | Verify all expected worksheets present | All SECOC worksheets exist |
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
| SWR_SECOC_00004 | CLI Interface - End-to-end command execution | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_secoc-module.md |
| CLI Documentation | ../../src/eb_model/cli/secoc_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_INT_SECOC_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_SECOC_00004 |
| Title | SECOC Error Handling Integration - Malformed XDM File |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the SECOC parser correctly handles malformed XDM files at the integration level, providing appropriate error messages without creating incomplete model objects.

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
| SWR_SECOC_00015 | Non-Functional - Malformed XML error handling | Covered |
| SWR_SECOC_00017 | Non-Functional - Required element validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_secoc-module.md |
| Parser Documentation | ../../src/eb_model/parser/secoc_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

**Document End**