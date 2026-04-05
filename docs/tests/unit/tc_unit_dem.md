# DEM Module Unit Test Cases

This document contains all unit test cases for the DEM module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_DEM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DEM_00001 |
| Title | DEM Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the DEM parser correctly extracts XML namespace definitions from EB Tresos XDM files, validates the module name, extracts AUTOSAR/software version information, and properly initializes the parser. This test ensures the foundation for all subsequent DEM configuration parsing.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Test XDM file (valid Dem.xdm) is available at known location |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/Dem_valid.xdm` | Valid DEM XDM file for testing |
| Module Name | "Dem" | Expected root module name |
| AUTOSAR Version | "4.3.0" | Example AUTOSAR version |
| Software Version | "1.2.3" | Example software version |
| Namespace Prefix | "d" | Default namespace prefix |
| Namespace URI | "http://www.tresos.de/_projects/DataModel2/06/data.xsd" | Data namespace URI |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create DemXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with valid Dem.xdm file | File parses without errors |
| 3 | Verify namespace map is populated | nsmap contains namespace definitions |
| 4 | Verify module name validation | Module "Dem" is accepted, others raise ValueError |
| 5 | Extract AUTOSAR version | Returns correct AUTOSAR version string |
| 6 | Extract software version | Returns correct software version string |
| 7 | Attempt parsing non-DEM XDM file | Raises ValueError with descriptive message |

## Expected Results

- Namespace map contains at least 3 namespace definitions
- Module name "Dem" is validated successfully
- AUTOSAR version matches expected value from file
- Software version matches expected value from file
- Parsing non-DEM file raises ValueError with message "Invalid module name"
- Parsing completes within 2 seconds for 5MB file

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No temporary files created during test |
| 2 | Parser instance can be garbage collected |
| 3 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00001 | Parser Layer - XDM file parsing and validation | Covered |
| SWR_DEM_00012 | Non-Functional - Efficient processing of 10MB files | Covered |
| SWR_DEM_00020 | Non-Functional - Inherit from AbstractEbModelParser | Covered |

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

# Test Case: TC_UNIT_DEM_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DEM_00002 |
| Title | DEM Model - Module Initialization |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the DEM module initializes with correct name and parent reference, inheriting all Module properties properly.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Module Name | "Dem" | Expected module name |
| Parent Type | EcucParamConfContainerDef | Parent container type |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create EBModel instance | EBModel initialized successfully |
| 2 | Create EcucParamConfContainerDef parent | Parent container created |
| 3 | Instantiate Dem with parent | Dem instance created with correct name |
| 4 | Verify getName() returns "Dem" | Name is correct |
| 5 | Verify parent reference is correct | Parent points to correct container |

## Expected Results

- Dem instance is created successfully
- getName() returns "Dem"
- Parent reference points to the correct EcucParamConfContainerDef
- All inherited Module properties are accessible

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Dem object remains in memory for verification |
| 2 | EBModel contains updated module collection |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00001 | Module Initialization | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_dem-module.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_DEM_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DEM_00003 |
| Title | DEM Model - DemGeneral Initialization |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the DemGeneral container initializes correctly with proper parent-child relationship.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Dem instance is created |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Container Name | "DemGeneral" | Expected container name |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create DemGeneral with Dem parent | Container initialized successfully |
| 2 | Verify getName() returns "DemGeneral" | Name is correct |
| 3 | Verify parent reference is correct | Parent points to Dem instance |

## Expected Results

- DemGeneral instance created successfully
- Name is "DemGeneral"
- Parent reference points to Dem instance

## Post-conditions

| # | Description |
|---|-------------|
| 1 | DemGeneral object remains in memory for verification |
| 2 | Dem contains updated element collection |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00002 | DemGeneral Container | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_dem-module.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_DEM_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DEM_00004 |
| Title | DEM Model - DemDevErrorDetect Property |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify the DemDevErrorDetect property getter and setter work correctly for DemGeneral container.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | DemGeneral instance is created |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| DemDevErrorDetect Value | true | Boolean test value |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Set DemDevErrorDetect to True using setter | Property set successfully |
| 2 | Call getDemDevErrorDetect() | Returns True |
| 3 | Set DemDevErrorDetect to False using setter | Property set successfully |
| 4 | Call getDemDevErrorDetect() | Returns False |

## Expected Results

- Getter returns the value set by setter
- Boolean type is preserved correctly
- Property can be toggled between True and False

## Post-conditions

| # | Description |
|---|-------------|
| 1 | DemGeneral object remains in memory for verification |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00002 | DemDevErrorDetect Property | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_dem-module.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_DEM_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DEM_00005 |
| Title | DEM Model - DemEnabled Property |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify the DemEnabled property getter and setter work correctly for DemGeneral container.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | DemGeneral instance is created |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| DemEnabled Value | true | Boolean test value |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Set DemEnabled to True using setter | Property set successfully |
| 2 | Call getDemEnabled() | Returns True |
| 3 | Set DemEnabled to False using setter | Property set successfully |
| 4 | Call getDemEnabled() | Returns False |

## Expected Results

- Getter returns the value set by setter
- Boolean type is preserved correctly
- Property can be toggled between True and False

## Post-conditions

| # | Description |
|---|-------------|
| 1 | DemGeneral object remains in memory for verification |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00002 | DemEnabled Property | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_dem-module.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_DEM_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DEM_00006 |
| Title | DEM Model - Fluent Interface Pattern |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that setters return self for method chaining in the fluent interface pattern.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | DemGeneral instance is created |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Test Value | true | Boolean test value |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Call setDemDevErrorDetect(True) | Returns self |
| 2 | Verify return value is self reference | Same object reference |
| 3 | Chain setDemEnabled(True) | Chaining works |
| 4 | Verify all properties are set correctly | Both DemDevErrorDetect and DemEnabled are True |

## Expected Results

- All setter methods return self
- Method chaining works correctly
- Multiple properties can be set in one chained call
- Property values are correctly set after chaining

## Post-conditions

| # | Description |
|---|-------------|
| 1 | DemGeneral object remains in memory for verification |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00006 | Fluent Interface Pattern | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_dem-module.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_DEM_00007

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DEM_00007 |
| Title | DEM Parser - Parse DemGeneral Container |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the DEM parser correctly extracts DemGeneral container from XML including DemDevErrorDetect and DemEnabled properties.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment with DemGeneral container is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| DemDevErrorDetect Value | true | Parsed from XML |
| DemEnabled Value | true | Parsed from XML |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create parser with namespace map | Parser initialized |
| 2 | Parse XML element containing DemGeneral | Container parsed successfully |
| 3 | Check model DemDevErrorDetect value | Matches XML value |
| 4 | Check model DemEnabled value | Matches XML value |
| 5 | Verify container name is "DemGeneral" | Name is correct |

## Expected Results

- DemGeneral container is created from XML
- DemDevErrorDetect value correctly extracted
- DemEnabled value correctly extracted
- Container name is correctly set

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Parsed model remains in memory for verification |
| 2 | No XML parsing errors occurred |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00002 | DemGeneral Parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_dem-module.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_DEM_00008

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DEM_00008 |
| Title | DEM Reporter - Excel Worksheet Generation |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the DEM reporter correctly generates Excel worksheets for DemGeneral configuration with proper formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | DEM model objects are populated with test data |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Output File Path | "test_output/Dem_report.xlsx" | Generated Excel file path |
| Worksheets to Generate | DemGeneral | Expected worksheets |
| Column Headers | Name, DemDevErrorDetect, DemEnabled | Expected column structure |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create DemXdmXlsWriter instance | Writer initialized successfully |
| 2 | Generate DemGeneral worksheet | Worksheet created with all data |
| 3 | Verify column headers are correct | Headers match expected structure |
| 4 | Verify data is populated correctly | All values match model |
| 5 | Verify column auto-width formatting | Column widths sized to fit content |
| 6 | Verify numeric data centering | Numeric columns are center-aligned |

## Expected Results

- DemGeneral worksheet is created
- All data is populated correctly
- Column formatting is applied (auto-width, centering for numeric)
- Data types are correct (strings for text, booleans for flags)
- File is valid and can be opened in Excel

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file persists for review |
| 2 | No memory leaks in reporter |
| 3 | Model objects remain unchanged after export |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00003 | Reporter Layer - Excel worksheet generation | Covered |
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

# Test Case: TC_UNIT_DEM_00009

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DEM_00009 |
| Title | DEM CLI - Command-Line Interface |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the DEM CLI correctly parses command-line arguments, executes the parsing workflow, and handles various command options including verbose logging.

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
| Command | `dem-xdm-xlsx input.xdm output.xlsx` | Basic command execution |
| Input File | `data/test/Dem_test.xdm` | Test input file |
| Output File | `test_output/Dem_test.xlsx` | Test output file |
| Verbose Flag | `-v` or `--verbose` | Enable verbose logging |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute basic command: `dem-xdm-xlsx input.xdm output.xlsx` | Command completes successfully, Excel file generated |
| 2 | Verify output file exists | File created at specified path |
| 3 | Execute with verbose flag: `dem-xdm-xlsx -v input.xdm output.xlsx` | Command completes with verbose logging output |
| 4 | Verify verbose output contains progress messages | Logs show parsing and export progress |
| 5 | Execute with missing input file: `dem-xdm-xlsx missing.xdm output.xlsx` | Command exits with error, appropriate error message |
| 6 | Execute with invalid arguments: `dem-xdm-xlsx` | Help message displayed |

## Expected Results

- Basic command executes successfully
- Output Excel file is valid
- Verbose flag enables detailed logging
- Missing input file produces helpful error
- Invalid arguments display help message
- Exit codes are appropriate (0 for success, non-zero for error)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Generated Excel files persist for review |
| 2 | No orphaned processes remain |
| 3 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00004 | CLI Interface - Command-line argument parsing and execution | Covered |

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

# Test Case: TC_UNIT_DEM_00010

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DEM_00010 |
| Title | DEM Error Handling - Malformed XML |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the DEM parser correctly handles malformed XML files with missing tags, invalid nesting, or incorrect attribute types, providing appropriate error messages without crashing.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Malformed XDM test files are available |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Malformed File 1 | Missing closing tag | Verify missing tag handling |
| Malformed File 2 | Invalid attribute type (string for boolean) | Verify type validation |
| Malformed File 3 | Duplicate element names | Verify duplicate handling |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XDM file with missing closing tag | Parser raises XMLSyntaxError or ValueError |
| 2 | Verify error message is descriptive | Error message indicates missing tag |
| 3 | Parse XDM file with invalid attribute type | Parser raises ValueError with type mismatch message |
| 4 | Verify error message includes field name and expected type | Message is clear and actionable |
| 5 | Parse XDM file with duplicate element names | Parser raises ValueError or handles with warning |
| 6 | Verify error indicates duplicate element | Message identifies conflicting element |

## Expected Results

- Malformed XML is detected and reported
- Error messages are clear, descriptive, and actionable
- Parser does not crash on malformed input
- Error messages include context (file, line, element, expected vs actual)
- Type mismatches are caught with helpful messages
- Duplicate elements are detected

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No partial model objects created |
| 2 | System returns to clean state |
| 3 | Parser can be reused for subsequent operations |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DEM_00015 | Non-Functional - Malformed XML error handling | Covered |
| SWR_DEM_00016 | Non-Functional - Missing optional elements handling | Covered |

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