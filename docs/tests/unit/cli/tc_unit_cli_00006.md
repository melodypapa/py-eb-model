# Test Case: TC_UNIT_CLI_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CLI_00006 |
| Title | CLI Layer - Exit Code Handling |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CLI layer returns appropriate exit codes for different execution outcomes (success, errors, warnings).

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI commands are available |
| 3 | Test scenarios for various outcomes |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Success Scenario | Valid input and output | Test success exit code |
| Error Scenario | Missing input file | Test error exit code |
| Warning Scenario | Recoverable issue | Test warning exit code |
| Help Scenario | -h flag | Test help exit code |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute command with valid input and output | Command completes successfully |
| 2 | Verify exit code is 0 | Exit code indicates success |
| 3 | Execute command with missing input file | Command fails with error |
| 4 | Verify exit code is non-zero | Exit code indicates failure |
| 5 | Execute command with -h flag | Help is displayed |
| 6 | Verify exit code is 0 | Exit code indicates success (help) |
| 7 | Execute command that generates warnings | Command completes with warnings |
| 8 | Verify exit code handling | Exit code reflects warnings if applicable |
| 9 | Verify exit code consistency | Same scenarios give same exit codes |
| 10 | Test exit codes across all commands | Consistent exit code behavior |

## Expected Results

- Exit code 0 for success scenarios
- Non-zero exit code for error scenarios
- Exit code 0 for help display
- Exit codes are consistent across commands
- Exit codes reflect actual execution outcomes

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Exit codes can be checked by shell scripts |
| 2 | No side effects from exit code checking |
| 3 | System remains stable |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
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