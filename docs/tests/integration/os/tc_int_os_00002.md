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