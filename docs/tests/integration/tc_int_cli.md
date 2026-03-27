# CLI Module Integration Test Cases

This document contains all integration test cases for the CLI module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_INT_CLI_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_CLI_00001 |
| Title | CLI Layer - End-to-End Command Execution |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete CLI workflow from command invocation through parsing, modeling, and report generation, including all error handling and logging.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid XDM test file is available |
| 3 | Output directory is writable |
| 4 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/Os_complete.xdm` | Test input file |
| Output File | `test_output/Os_cli_test.xlsx` | Test output file |
| Command Options | `-v --skip-os-task` | Optional command flags |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command: `os-xdm-xlsx -v data/test/Os_complete.xdm test_output/Os_cli_test.xlsx` | Command executes successfully |
| 2 | Verify verbose output | Progress messages displayed |
| 3 | Verify parsing completion | Parsing logged as complete |
| 4 | Verify model population | Model entities logged |
| 5 | Verify report generation | Export logged as complete |
| 6 | Check output file exists | Excel file created |
| 7 | Verify output file content | Expected worksheets present |
| 8 | Execute with skip flags: `os-xdm-xlsx --skip-os-task data/test/Os_complete.xdm test_output/Os_cli_skip.xlsx` | Command executes successfully |
| 9 | Verify skipped worksheet | OsTask worksheet not present |
| 10 | Verify exit code | Exit code is 0 for success |

## Expected Results

- Complete CLI workflow executes successfully
- Verbose logging shows all steps
- Output file is valid and correct
- Skip flags work as expected
- Exit codes are appropriate
- Error handling works for invalid inputs

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Output files persist for review |
| 2 | No orphaned processes |
| 3 | System returns to clean state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CLI_00001 | CLI Layer - Command registration | Covered |
| SWR_CLI_00002 | CLI Layer - Argument parsing | Covered |
| SWR_CLI_00003 | CLI Layer - Help display | Covered |
| SWR_CLI_00004 | CLI Layer - Logging configuration | Covered |
| SWR_CLI_00005 | CLI Layer - Error messages | Covered |
| SWR_CLI_00006 | CLI Layer - Exit code handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_cli-layer.md |
| CLI Documentation | ../../src/eb_model/cli/os_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
