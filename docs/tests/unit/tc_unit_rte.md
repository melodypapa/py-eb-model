# RTE Module Unit Test Cases

This document contains all unit test cases for the RTE module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_RTE_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00001 |
| Title | RTE Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly extracts XML namespace definitions from EB Tresos XDM files, validates the module name, extracts AUTOSAR version information, and detects AUTOSAR version (AR 3.x vs AR 4.x) for appropriate handling.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Test XDM files (Rte.xdm for AR 3.x and AR 4.x) are available |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File AR3 | `data/test/Rte_ar3.xdm` | RTE XDM file for AUTOSAR 3.x |
| Input File AR4 | `data/test/Rte_ar4.xdm` | RTE XDM file for AUTOSAR 4.x |
| Module Name | "Rte" | Expected root module name |
| AUTOSAR Version AR3 | "3.2.1" | Example AUTOSAR 3.x version |
| AUTOSAR Version AR4 | "4.3.0" | Example AUTOSAR 4.x version |
| Namespace Prefix | "d" | Default namespace prefix |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create RteXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with AR 3.x file | File parses without errors |
| 3 | Verify namespace map is populated | nsmap contains namespace definitions |
| 4 | Verify module name validation | Module "Rte" is accepted |
| 5 | Extract AUTOSAR version for AR 3.x file | Returns correct AUTOSAR 3.x version string |
| 6 | Detect AUTOSAR version from AR 3.x file | AR version detected as 3.x |
| 7 | Parse AR 4.x file | File parses without errors |
| 8 | Extract AUTOSAR version for AR 4.x file | Returns correct AUTOSAR 4.x version string |
| 9 | Detect AUTOSAR version from AR 4.x file | AR version detected as 4.x |
| 10 | Attempt parsing non-RTE XDM file | Raises ValueError with descriptive message |

## Expected Results

- Namespace map contains at least 3 namespace definitions
- Module name "Rte" is validated successfully
- AUTOSAR version is extracted correctly for both 3.x and 4.x
- AR version detection works correctly (3.x vs 4.x)
- Parsing non-RTE file raises ValueError
- AR 3.x specific handling is triggered for 3.x files
- AR 4.x specific handling is triggered for 4.x files

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No temporary files created during test |
| 2 | Parser instance can be garbage collected |
| 3 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00001 | Parser Layer - XDM file parsing and validation | Covered |
| SWR_RTE_00008 | Non-Functional - Efficient processing of 10MB files | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Design Document | ../requirements/overview.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_RTE_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00002 |
| Title | RTE Model - BSW Component Instance Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly extracts Basic Software (BSW) component instance configurations from XDM containers, creating BswComponentInstance model objects with all relevant attributes.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing BSW component instance containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| BSW Component Name | "BswComponent1" | Example BSW component identifier |
| BSW Component Type | "CanIf" | BSW component type |
| BSW Component Version | "1.2.3" | Component version |
| BSW Component Instance | "CanIf_1" | Specific instance name |
| Init Function | "CanIf_Init" | Initialization function name |
| Provider Port Count | 3 | Number of provider ports |
| Requester Port Count | 2 | Number of requester ports |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with BSW component instance container | BswComponentInstance object created successfully |
| 2 | Verify component name extraction | getName() returns "BswComponent1" |
| 3 | Verify component type extraction | getType() returns "CanIf" |
| 4 | Verify component version extraction | getVersion() returns "1.2.3" |
| 5 | Verify instance name extraction | getInstanceName() returns "CanIf_1" |
| 6 | Verify init function extraction | getInitFunction() returns "CanIf_Init" |
| 7 | Verify provider port count extraction | getProviderPortCount() returns 3 |
| 8 | Verify requester port count extraction | getRequesterPortCount() returns 2 |
| 9 | Verify parent-child relationship | Component's parent is RTE module |
| 10 | Verify O(1) lookup performance | Component retrieval by name is constant time |

## Expected Results

- All BSW component attributes are extracted correctly
- Component object is properly registered with parent module
- Parent-child relationship is established
- Component lookup by name is O(1) using dictionary
- Component full name includes parent hierarchy

## Post-conditions

| # | Description |
|---|-------------|
| 1 | BswComponentInstance objects remain in memory for verification |
| 2 | EBModel contains updated BSW component collection |
| 3 | No orphaned component objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00002 | BSW Component Instance Extraction | Covered |
| SWR_RTE_00009 | Non-Functional - O(1) lookup performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_RTE_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00003 |
| Title | RTE Model - SW Component Instance Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly extracts Software (SW) component instance configurations from XDM containers, creating SwComponentInstance model objects with all relevant attributes.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing SW component instance containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| SW Component Name | "SwComponent1" | Example SW component identifier |
| SW Component Type | "ApplicationComponent" | SW component type |
| SW Component Version | "2.0.0" | Component version |
| SW Component Instance | "App_Swc_1" | Specific instance name |
| Runnable Entity Count | 5 | Number of runnable entities |
| Port Count | 4 | Number of ports |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with SW component instance container | SwComponentInstance object created successfully |
| 2 | Verify component name extraction | getName() returns "SwComponent1" |
| 3 | Verify component type extraction | getType() returns "ApplicationComponent" |
| 4 | Verify component version extraction | getVersion() returns "2.0.0" |
| 5 | Verify instance name extraction | getInstanceName() returns "App_Swc_1" |
| 6 | Verify runnable entity count extraction | getRunnableEntityCount() returns 5 |
| 7 | Verify port count extraction | getPortCount() returns 4 |
| 8 | Verify parent-child relationship | Component's parent is RTE module |
| 9 | Verify O(1) lookup performance | Component retrieval by name is constant time |

## Expected Results

- All SW component attributes are extracted correctly
- Component object is properly registered with parent module
- Parent-child relationship is established
- Component lookup by name is O(1) using dictionary
- Component full name includes parent hierarchy

## Post-conditions

| # | Description |
|---|-------------|
| 1 | SwComponentInstance objects remain in memory for verification |
| 2 | EBModel contains updated SW component collection |
| 3 | No orphaned component objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00003 | SW Component Instance Extraction | Covered |
| SWR_RTE_00010 | Non-Functional - O(1) lookup performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_RTE_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00004 |
| Title | RTE Model - Event to Task Mapping |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly extracts event-to-task mapping configurations from XDM containers, establishing relationships between RTE events and OS tasks.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing event-to-task mapping containers is available |
| 3 | EBModel singleton is initialized with OS module |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Event Name | "Event1" | Example event identifier |
| Event Type | "DataReceivedEvent" | RTE event type |
| Mapped Task | "Task1" | OS task that handles this event |
| Event Priority | 5 | Event priority |
| Event Mask | 0xFF | Event mask value |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with event-to-task mapping container | EventMapping object created successfully |
| 2 | Verify event name extraction | getName() returns "Event1" |
| 3 | Verify event type extraction | getType() returns "DataReceivedEvent" |
| 4 | Verify mapped task extraction | getMappedTask() returns "Task1" |
| 5 | Verify event priority extraction | getPriority() returns 5 |
| 6 | Verify event mask extraction | getMask() returns 0xFF |
| 7 | Verify bidirectional relationship | Task's getEvents() includes this event |
| 8 | Validate task reference exists | Referenced task is found in OS module |
| 9 | Handle unmapped events | Events without task reference don't cause error |
| 10 | Verify parent-child relationship | Event's parent is RTE module |

## Expected Results

- All event attributes are extracted correctly
- Task reference is correctly resolved when present
- Bidirectional relationship is established between event and task
- Events without task references are handled gracefully
- Parent-child relationship is established
- Event lookup is efficient

## Post-conditions

| # | Description |
|---|-------------|
| 1 | EventMapping objects remain in memory for verification |
| 2 | EBModel contains updated event mapping collection |
| 3 | No orphaned event objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00004 | Event to Task Mapping | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_RTE_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00005 |
| Title | RTE Model - AR 3.x Version Support |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly handles AUTOSAR 3.x version specific elements and attributes, including 3.x specific data structures and XML schemas.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | AUTOSAR 3.x XDM file is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| AUTOSAR Version | "3.2.1" | AUTOSAR 3.x version identifier |
| AR3 Specific Element | "DataReceivedEvent" | 3.x specific event type |
| AR3 Specific Attribute | "RunnableEntity" | 3.x specific attribute |
| XML Namespace | AUTOSAR 3.x namespace | 3.x specific XML namespace |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse AUTOSAR 3.x XDM file | File parses successfully with AR 3.x handling |
| 2 | Verify version detection | AR version detected as 3.x |
| 3 | Extract AR 3.x specific elements | Elements parsed correctly |
| 4 | Extract AR 3.x specific attributes | Attributes parsed correctly |
| 5 | Validate AR 3.x XML namespace | Namespace recognized as AUTOSAR 3.x |
| 6 | Verify BSW component structure for AR 3.x | Structure matches AR 3.x schema |
| 7 | Verify SW component structure for AR 3.x | Structure matches AR 3.x schema |
| 8 | Verify port definitions for AR 3.x | Port structure matches AR 3.x format |
| 9 | Handle AR 3.x specific runnable entities | Runnable entities extracted correctly |
| 10 | Validate AR 3.x specific features | All 3.x specific features work correctly |

## Expected Results

- AUTOSAR 3.x version is detected correctly
- AR 3.x specific elements and attributes are handled
- XML namespace is recognized correctly
- BSW and SW component structures match AR 3.x schema
- Port definitions follow AR 3.x format
- Runnable entities are extracted correctly
- No AR 4.x specific features are expected or required
- Parser adapts to AR 3.x differences from AR 4.x

## Post-conditions

| # | Description |
|---|-------------|
| 1 | RTE model objects for AR 3.x remain in memory |
| 2 | EBModel contains AR 3.x specific data |
| 3 | Parser can be reused for AR 4.x files |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00005 | AR 3.x Version Support | Covered |
| SWR_RTE_00011 | Non-Functional - AR 3.x specific handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Parser Documentation | ../../src/eb_model/parser/rte_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_RTE_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00006 |
| Title | RTE Model - AR 4.x Version Support |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly handles AUTOSAR 4.x version specific elements and attributes, including 4.x specific data structures, port interfaces, and communication patterns.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | AUTOSAR 4.x XDM file is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| AUTOSAR Version | "4.3.0" | AUTOSAR 4.x version identifier |
| AR4 Specific Element | "ModeSwitchEvent" | 4.x specific event type |
| AR4 Specific Attribute | "ServiceNeeds" | 4.x specific attribute |
| XML Namespace | AUTOSAR 4.x namespace | 4.x specific XML namespace |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse AUTOSAR 4.x XDM file | File parses successfully with AR 4.x handling |
| 2 | Verify version detection | AR version detected as 4.x |
| 3 | Extract AR 4.x specific elements | Elements parsed correctly |
| 4 | Extract AR 4.x specific attributes | Attributes parsed correctly |
| 5 | Validate AR 4.x XML namespace | Namespace recognized as AUTOSAR 4.x |
| 6 | Verify BSW component structure for AR 4.x | Structure matches AR 4.x schema |
| 7 | Verify SW component structure for AR 4.x | Structure matches AR 4.x schema |
| 8 | Verify port interface definitions for AR 4.x | Port interfaces follow AR 4.x format |
| 9 | Handle AR 4.x specific communication patterns | Communication patterns extracted correctly |
| 10 | Validate AR 4.x specific features | All 4.x specific features work correctly |

## Expected Results

- AUTOSAR 4.x version is detected correctly
- AR 4.x specific elements and attributes are handled
- XML namespace is recognized correctly
- BSW and SW component structures match AR 4.x schema
- Port interface definitions follow AR 4.x format
- Communication patterns are extracted correctly
- No AR 3.x specific features are expected or required
- Parser adapts to AR 4.x differences from AR 3.x

## Post-conditions

| # | Description |
|---|-------------|
| 1 | RTE model objects for AR 4.x remain in memory |
| 2 | EBModel contains AR 4.x specific data |
| 3 | Parser can be reused for AR 3.x files |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00006 | AR 4.x Version Support | Covered |
| SWR_RTE_00012 | Non-Functional - AR 4.x specific handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Parser Documentation | ../../src/eb_model/parser/rte_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

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
---

# Test Case: TC_UNIT_RTE_00008

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00008 |
| Title | RTE CLI - Command-Line Interface |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE CLI correctly parses command-line arguments, executes the parsing workflow, and handles various command options including verbose logging and worksheet filtering.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI entry point is registered (rte-xdm-xlsx) |
| 3 | Test XDM file is available |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Command | `rte-xdm-xlsx input.xdm output.xlsx` | Basic command execution |
| Input File | `data/test/Rte_test.xdm` | Test input file |
| Output File | `test_output/Rte_test.xlsx` | Test output file |
| Verbose Flag | `-v` or `--verbose` | Enable verbose logging |
| Skip BSW Flag | `--skip-bsw-component` | Skip BSW component worksheet |
| Skip SW Flag | `--skip-sw-component` | Skip SW component worksheet |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute basic command: `rte-xdm-xlsx input.xdm output.xlsx` | Command completes successfully, Excel file generated |
| 2 | Verify output file exists | File created at specified path |
| 3 | Execute with verbose flag: `rte-xdm-xlsx -v input.xdm output.xlsx` | Command completes with verbose logging output |
| 4 | Verify verbose output contains progress messages | Logs show parsing and export progress |
| 5 | Execute with skip flag: `rte-xdm-xlsx --skip-bsw-component input.xdm output.xlsx` | Command completes, BSW worksheet skipped |
| 6 | Verify output file missing BSW worksheet | BSW worksheet not present |
| 7 | Execute with missing input file: `rte-xdm-xlsx missing.xdm output.xlsx` | Command exits with error, appropriate error message |
| 8 | Execute with invalid arguments: `rte-xdm-xlsx` | Help message displayed |
| 9 | Verify help message includes usage and options | Help is complete and accurate |
| 10 | Execute with all worksheets skipped | Error message that at least one worksheet must be generated |

## Expected Results

- Basic command executes successfully
- Output Excel file is valid
- Verbose flag enables detailed logging
- Skip flags correctly filter worksheets
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
| SWR_RTE_00014 | CLI Interface - Command-line argument parsing and execution | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| CLI Documentation | ../../src/eb_model/cli/rte_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_RTE_00009

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00009 |
| Title | RTE Error Handling - Malformed XML |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly handles malformed XML files with missing tags, invalid nesting, or incorrect attribute types, providing appropriate error messages without crashing.

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
| Malformed File 2 | Invalid attribute type (string for number) | Verify type validation |
| Malformed File 3 | Invalid enum value | Verify enum validation |
| Malformed File 4 | Duplicate component names | Verify duplicate handling |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XDM file with missing closing tag | Parser raises XMLSyntaxError or ValueError |
| 2 | Verify error message is descriptive | Error message indicates missing tag |
| 3 | Parse XDM file with invalid attribute type (portCount="abc") | Parser raises ValueError with type mismatch message |
| 4 | Verify error message includes field name and expected type | Message is clear and actionable |
| 5 | Parse XDM file with invalid enum value (eventType="INVALID") | Parser raises ValueError with valid enum options |
| 6 | Verify error message includes valid options | User can see acceptable values |
| 7 | Parse XDM file with duplicate component names | Parser raises ValueError or handles with warning |
| 8 | Verify error indicates duplicate element | Message identifies conflicting element |

## Expected Results

- Malformed XML is detected and reported
- Error messages are clear, descriptive, and actionable
- Parser does not crash on malformed input
- Error messages include context (file, line, element, expected vs actual)
- Type mismatches are caught with helpful messages
- Invalid enum values show valid options
- Duplicate components are detected

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No partial model objects created |
| 2 | System returns to clean state |
| 3 | Parser can be reused for subsequent operations |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00015 | Non-Functional - Malformed XML error handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Parser Documentation | ../../src/eb_model/parser/rte_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_RTE_00010

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00010 |
| Title | RTE Error Handling - Missing Required Elements |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly validates required elements and references, detecting missing mandatory attributes and invalid task references.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XDM test files with missing required elements are available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Missing Required Attribute | BSW component without name | Verify required attribute validation |
| Invalid Task Reference | Event mapping referencing non-existent task | Verify reference validation |
| Invalid Component Reference | Port referencing non-existent component | Verify reference validation |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XDM file with component missing name attribute | Parser raises ValueError indicating missing required attribute |
| 2 | Verify error message includes element name and attribute | Message identifies exactly what's missing |
| 3 | Parse XDM file with event mapping referencing invalid task | Parser raises ValueError or logs warning |
| 4 | Verify error message indicates unresolved reference | Message includes reference target |
| 5 | Parse XDM file with port referencing non-existent component | Parser raises ValueError or logs warning |
| 6 | Verify error handling allows optional references | Optional references don't cause errors when missing |
| 7 | Validate task reference resolves correctly | Valid task references are resolved |

## Expected Results

- Missing required attributes are detected and reported
- Error messages clearly indicate what's missing and where
- Invalid references are detected with helpful messages
- Optional elements don't cause errors when missing
- Valid references are correctly resolved

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No partial model objects created for invalid entities |
| 2 | System returns to clean state |
| 3 | Parser can be reused for subsequent operations |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00015 | Non-Functional - Error handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Parser Documentation | ../../src/eb_model/parser/rte_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
