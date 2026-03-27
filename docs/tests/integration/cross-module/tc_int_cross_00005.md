# Test Case: TC_INT_CROSS_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_CROSS_00005 |
| Title | Cross-Module - Full System Workflow |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete system workflow from parsing multiple XDM files through modeling all modules to generating comprehensive reports, including error handling and performance validation.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XDM files for representative modules are available |
| 3 | EBModel singleton is clean |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Core Modules | OS, RTE, NVM, EcuC, BswM | Representative core modules |
| Communication Modules | CanIf, LinIf, EthIf | Representative communication modules |
| System Modules | Det, EcuM, Tm | Representative system modules |
| Total Files | 8-10 | Number of files to parse |
| Output File | `test_output/Full_system.xlsx` | Complete system report |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse all core module files | Core models populated |
| 2 | Parse all communication module files | Communication models populated |
| 3 | Parse all system module files | System models populated |
| 4 | Verify no cross-module conflicts | Each module data is independent |
| 5 | Verify cross-module references | References resolved where appropriate |
| 6 | Generate full system Excel workbook | All module data in single file |
| 7 | Verify all module worksheets | All expected worksheets present |
| 8 | Verify data integrity | No data loss or corruption |
| 9 | Measure total execution time | Performance within acceptable limits |
| 10 | Verify memory usage | No memory leaks or excessive usage |

## Expected Results

- All modules parse successfully
- No cross-module conflicts
- Cross-module references resolved correctly
- Full system report generated
- All data integrity maintained
- Performance acceptable (< 30 seconds)
- Memory usage stable

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Full system output persists for review |
| 2 | EBModel contains all module data |
| 3 | System stable for subsequent operations |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00001-00010 | All parser layer requirements | Covered |
| SWR_REPORTER_00001-00009 | All reporter layer requirements | Covered |
| SWR_CLI_00001-00009 | All CLI layer requirements | Covered |
| All module requirements | Complete system test | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Requirement Document | ../requirements/swr_reporter-layer.md |
| Requirement Document | ../requirements/swr_cli-layer.md |
| System Overview | ../requirements/overview.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |