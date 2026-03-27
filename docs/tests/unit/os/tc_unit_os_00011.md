# Test Case: TC_UNIT_OS_00011

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00011 |
| Title | OS CLI - Command-Line Interface |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS CLI correctly parses command-line arguments, executes the parsing workflow, and handles various command options including verbose logging and worksheet filtering.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI entry point is registered (os-xdm-xlsx) |
| 3 | Test XDM file is available |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Command | `os-xdm-xlsx input.xdm output.xlsx` | Basic command execution |
| Input File | `data/test/Os_test.xdm` | Test input file |
| Output File | `test_output/Os_test.xlsx` | Test output file |
| Verbose Flag | `-v` or `--verbose` | Enable verbose logging |
| Skip Task Flag | `--skip-os-task` | Skip OsTask worksheet |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute basic command: `os-xdm-xlsx input.xdm output.xlsx` | Command completes successfully, Excel file generated |
| 2 | Verify output file exists | File created at specified path |
| 3 | Execute with verbose flag: `os-xdm-xlsx -v input.xdm output.xlsx` | Command completes with verbose logging output |
| 4 | Verify verbose output contains progress messages | Logs show parsing and export progress |
| 5 | Execute with skip flag: `os-xdm-xlsx --skip-os-task input.xdm output.xlsx` | Command completes, OsTask worksheet skipped |
| 6 | Verify output file missing OsTask worksheet | OsTask worksheet not present |
| 7 | Execute with missing input file: `os-xdm-xlsx missing.xdm output.xlsx` | Command exits with error, appropriate error message |
| 8 | Execute with invalid arguments: `os-xdm-xlsx` | Help message displayed |
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
| SWR_OS_00011 | CLI Interface - Command-line argument parsing and execution | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| CLI Documentation | ../../src/eb_model/cli/os_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |