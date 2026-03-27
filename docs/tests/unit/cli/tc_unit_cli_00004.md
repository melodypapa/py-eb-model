# Test Case: TC_UNIT_CLI_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CLI_00004 |
| Title | CLI Layer - Logging Configuration |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CLI layer correctly configures logging based on command-line options, including verbose mode and different log levels.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI commands are available |
| 3 | Logging module is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Verbose Flag | `-v` or `--verbose` | Enable verbose logging |
| Default Log Level | WARNING | Default logging level |
| Verbose Log Level | INFO or DEBUG | Verbose logging level |
| Log Output | Console | Logging destination |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute command without verbose flag | Logging at default level (WARNING) |
| 2 | Verify log output | Only WARNING and ERROR messages shown |
| 3 | Execute command with verbose flag | Logging at verbose level (INFO or DEBUG) |
| 4 | Verify verbose log output | INFO/DEBUG messages shown |
| 5 | Verify log format | Log messages include timestamp, level, message |
| 6 | Execute command with valid input | Progress messages in verbose mode |
| 7 | Verify error logging | Errors logged at ERROR level |
| 8 | Verify warning logging | Warnings logged at WARNING level |
| 9 | Test multiple verbose flags | Logging level doesn't change with multiple flags |
| 10 | Verify logging doesn't interfere with output | Log messages separate from normal output |

## Expected Results

- Default logging level is WARNING
- Verbose flag enables INFO/DEBUG logging
- Log format includes timestamp, level, message
- Progress messages shown in verbose mode
- Errors logged at ERROR level
- Warnings logged at WARNING level
- Logging doesn't interfere with normal output

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Logging configuration resets between commands |
| 2 | No log files remain after command |
| 3 | CLI state is unchanged |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CLI_00004 | CLI Layer - Logging configuration | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_cli-layer.md |
| CLI Documentation | ../../src/eb_model/cli/os_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |