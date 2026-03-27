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