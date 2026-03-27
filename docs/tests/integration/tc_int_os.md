# OS Module Integration Test Cases

This document contains all integration test cases for the OS module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_INT_OS_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_OS_00001 |
| Title | OS Module - End-to-End Parsing and Excel Export |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete end-to-end workflow of parsing an OS XDM file, modeling all OS entities (tasks, ISRs, schedule tables, counters, applications, alarms, resources), and exporting the configuration to a multi-sheet Excel file with proper formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Complete Os.xdm file with all entity types is available |
| 3 | Output directory for Excel file is writable |
| 4 | No other instances of EBModel exist (singleton pattern) |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/Os_complete.xdm` | XDM with all OS entity types |
| Output File | `test_output/Os_test.xlsx` | Generated Excel report |
| Expected Worksheets | OsTask, OsIsr, OsScheduleTable, OsCounter, OsAlarm, OsResource, OsApplication | List of expected sheets |
| Task Count | 10-20 | Expected number of tasks |
| ISR Count | 5-10 | Expected number of ISRs |
| Schedule Table Count | 3-5 | Expected number of schedule tables |
| Counter Count | 2-5 | Expected number of counters |
| Alarm Count | 5-10 | Expected number of alarms |
| Resource Count | 3-5 | Expected number of resources |
| Application Count | 2-4 | Expected number of applications |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command: `os-xdm-xlsx data/test/Os_complete.xdm test_output/Os_test.xlsx` | Command completes successfully |
| 2 | Verify Excel file exists | File created at output path |
| 3 | Open Excel file and verify worksheets | All expected worksheets present |
| 4 | Verify OsTask worksheet contains all tasks | Task count matches input, all columns populated |
| 5 | Verify OsIsr worksheet contains all ISRs | ISR count matches input, hardware attributes populated |
| 6 | Verify OsScheduleTable worksheet | Tables and expiry points correctly extracted |
| 7 | Verify OsCounter worksheet | Counter configurations correctly extracted |
| 8 | Verify OsAlarm worksheet | Alarm configurations correctly extracted |
| 9 | Verify OsResource worksheet | Resource configurations correctly extracted |
| 10 | Verify OsApplication worksheet | Applications correctly extracted with mappings |
| 11 | Verify column auto-width formatting | Columns sized to fit content |
| 12 | Verify numeric data centering | Numeric columns are center-aligned |
| 13 | Verify task-to-application mappings | Application references correctly populated |
| 14 | Verify ISR-to-application mappings | Application references correctly populated |
| 15 | Verify schedule table counter references | Counter references correctly resolved |
| 16 | Execute with --skip-os-task flag | OsTask worksheet is skipped |
| 17 | Execute with --skip-os-isr flag | OsIsr worksheet is skipped |
| 18 | Verify total execution time | Execution completes within 5 seconds for 10MB file |

## Expected Results

- Excel file generated successfully with no errors
- All 7 expected worksheets present (or reduced when skip flags used)
- Task data includes: name, priority, activation, schedule type, stack size, autostart
- ISR data includes: category, priority, vector, stack size, hardware attributes
- Schedule table data includes: duration, repeating, counter reference, expiry points
- Counter data includes: max allowed value, min cycle, ticks per base, counter type
- Alarm data includes: name, action, target, cycle, counter reference
- Resource data includes: name, property, scheduler access, service access
- Application data includes: name, description, ID, mapped tasks, mapped ISRs
- Application mappings correctly established (bidirectional)
- Column formatting applied consistently
- Total execution time < 5 seconds for 10MB file
- Memory usage remains stable (no leaks)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file persists for review |
| 2 | No memory leaks in parser/reporter |
| 3 | EBModel singleton can be reset for next test |
| 4 | No orphaned XML elements remain in memory |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00001 | Parser Layer - XDM file parsing | Covered |
| SWR_OS_00002 | Task Management - Task extraction and modeling | Covered |
| SWR_OS_00003 | ISR Management - ISR extraction and modeling | Covered |
| SWR_OS_00004 | Schedule Tables - Schedule table extraction | Covered |
| SWR_OS_00005 | Counters - Counter extraction | Covered |
| SWR_OS_00006 | Applications - Application mapping | Covered |
| SWR_OS_00007 | Alarms - Alarm extraction | Covered |
| SWR_OS_00008 | Resources - Resource extraction | Covered |
| SWR_OS_00010 | Reporter Layer - Excel generation | Covered |
| SWR_OS_00011 | CLI Interface - Command execution | Covered |
| SWR_OS_00013 | Non-Functional - Excel performance | Covered |
| SWR_OS_00014 | Non-Functional - O(1) lookup performance | Covered |
| SWR_OS_00019 | Non-Functional - Memory efficiency | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| System Overview | ../requirements/overview.md |
| Parser Documentation | ../../src/eb_model/parser/os_xdm_parser.py |
| Reporter Documentation | ../../src/eb_model/reporter/os_xdm_xls_writer.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_INT_OS_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_OS_00002 |
| Title | OS Module - Complex Configuration Handling |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the OS parser can handle complex configurations including multiple applications, cross-application mappings, complex schedule tables with many expiry points, and intricate resource access patterns.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Complex Os.xdm file with advanced features is available |
| 3 | Output directory is writable |
| 4 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/Os_complex.xdm` | XDM with complex configuration |
| Application Count | 5-10 | Multiple applications for mapping |
| Tasks per Application | 3-8 | Tasks distributed across applications |
| ISRs per Application | 2-5 | ISRs distributed across applications |
| Schedule Table Expiry Points | 10-20 per table | Complex schedule tables |
| Shared Resources | 3-5 | Resources accessed by multiple tasks |
| Hardware Platforms | Mixed (TriCore, ARM) | Verify hardware-specific handling |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command with complex XDM file | Command completes successfully |
| 2 | Verify Excel file generated with all worksheets | File created successfully |
| 3 | Verify application count | All applications extracted correctly |
| 4 | Verify task-to-application mapping | Each task maps to correct application |
| 5 | Verify ISR-to-application mapping | Each ISR maps to correct application |
| 6 | Verify application lookup returns correct tasks | getTasks() returns correct task list for each application |
| 7 | Verify application lookup returns correct ISRs | getIsrs() returns correct ISR list for each application |
| 8 | Verify schedule table expiry point count | All expiry points extracted |
| 9 | Verify expiry points sorted by offset | Expiry points in correct order |
| 10 | Verify expiry point actions | All action types correctly parsed |
| 11 | Verify shared resource references | Resources correctly referenced by multiple tasks |
| 12 | Verify TriCore-specific ISR attributes | TriCore ISRs have correct hardware attributes |
| 13 | Verify ARM-specific ISR attributes | ARM ISRs have correct hardware attributes |
| 14 | Verify counter references in schedule tables | All counter references resolved correctly |
| 15 | Verify counter references in alarms | All counter references resolved correctly |
| 16 | Verify bidirectional mappings | Application can lookup tasks, tasks can lookup application |

## Expected Results

- Complex configuration is parsed completely and correctly
- All application mappings are established bidirectionally
- Complex schedule tables with many expiry points are handled
- Shared resource references are correctly maintained
- Hardware-specific attributes are correctly parsed for each platform
- All cross-references are resolved
- Performance remains acceptable for complex configurations
- No data loss or corruption in complex scenarios

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file with complex configuration persists for review |
| 2 | No memory leaks or resource exhaustion |
| 3 | EBModel can be reset for next test |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00002 | Task Management - Task extraction and modeling | Covered |
| SWR_OS_00003 | ISR Management - ISR extraction and hardware-specific handling | Covered |
| SWR_OS_00004 | Schedule Tables - Schedule table extraction | Covered |
| SWR_OS_00006 | Applications - Application mapping | Covered |
| SWR_OS_00008 | Resources - Resource extraction | Covered |
| SWR_OS_00014 | Non-Functional - O(1) lookup performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Parser Documentation | ../../src/eb_model/parser/os_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_INT_OS_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_OS_00003 |
| Title | OS Module - Error Recovery and Reporting |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the OS module gracefully handles error conditions including missing files, invalid configurations, and corrupted data, providing clear error messages and recovering when possible.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Test files with various error conditions are available |
| 3 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Missing File | Non-existent file path | Verify file not found handling |
| Empty File | Empty .xdm file | Verify empty file handling |
| Invalid Module | XDM file with wrong module name | Verify module validation |
| Corrupted XML | XML with structural errors | Verify XML error handling |
| Invalid References | References to non-existent entities | Verify reference error handling |
| Large File | 50MB+ XDM file | Verify performance and stability |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute with non-existent file | Command exits with error code, file not found message |
| 2 | Verify error message includes file path | Message is specific and helpful |
| 3 | Execute with empty file | Command exits with error, indicates empty/invalid file |
| 4 | Execute with invalid module name (non-OS) | Command exits with error, indicates wrong module |
| 5 | Verify error message shows expected vs actual module | Message is clear about validation failure |
| 6 | Execute with corrupted XML | Command exits with error, indicates XML parsing failure |
| 7 | Verify error message includes line/position | Message helps locate error |
| 8 | Execute with invalid counter reference | Parser logs warning or exits with error |
| 9 | Verify error message indicates unresolved reference | Message identifies what couldn't be resolved |
| 10 | Execute with large file (50MB) | Command completes successfully or reports size limit |
| 11 | Verify memory usage during large file processing | Memory usage remains stable, no leaks |
| 12 | Verify system can recover after error | Subsequent valid operations work correctly |
| 13 | Test error with --verbose flag | Detailed error information in verbose mode |
| 14 | Verify verbose error includes stack trace | Debug information available when requested |

## Expected Results

- Missing files produce clear error messages with file paths
- Empty or invalid files are detected and reported
- Module validation catches wrong module types
- Corrupted XML produces helpful error messages with location
- Invalid references are detected and reported
- Large files are handled within performance limits
- System recovers gracefully after errors
- Verbose mode provides additional debugging information
- Error codes are appropriate (non-zero for failures)
- No partial or corrupted output files created on error

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No corrupted output files from failed operations |
| 2 | System returns to clean state |
| 3 | EBModel singleton can be reset for next test |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00015 | Non-Functional - Malformed XML error handling | Covered |
| SWR_OS_00016 | Non-Functional - Missing optional elements handling | Covered |
| SWR_OS_00017 | Non-Functional - Required element validation | Covered |
| SWR_OS_00018 | Non-Functional - Path validation | Covered |
| SWR_OS_00019 | Non-Functional - Memory efficiency | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Parser Documentation | ../../src/eb_model/parser/os_xdm_parser.py |
| CLI Documentation | ../../src/eb_model/cli/os_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |