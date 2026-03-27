# CLI Module Unit Test Cases

This document contains all unit test cases for the CLI module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_CLI_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CLI_00001 |
| Title | CLI Layer - Command Registration |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CLI layer correctly registers all module-specific commands and makes them available through the command-line interface.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI entry points are registered in setup.py |
| 3 | Command modules are available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Registered Commands | List of all CLI commands | Verify all commands registered |
| Command Names | os-xdm-xlsx, rte-xdm-xlsx, nvm-xdm-xlsx, etc. | Verify command names |
| Command Modules | Corresponding CLI modules | Verify module mapping |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Query CLI for registered commands | Returns list of all commands |
| 2 | Verify OS command is registered | "os-xdm-xlsx" is in command list |
| 3 | Verify RTE command is registered | "rte-xdm-xlsx" is in command list |
| 4 | Verify NVM command is registered | "nvm-xdm-xlsx" is in command list |
| 5 | Verify all 32 module commands are registered | All expected commands present |
| 6 | Verify command to module mapping | Each command maps to correct module |
| 7 | Execute command with --help option | Help message displayed |
| 8 | Verify help includes command description | Description is accurate |
| 9 | Attempt to execute unregistered command | Error message or command not found |
| 10 | Verify command discovery | Commands are discoverable via CLI |

## Expected Results

- All 32 module commands are registered
- Command names are correct
- Command to module mapping is correct
- Help messages are available for all commands
- Unregistered commands are handled appropriately
- Commands are discoverable via CLI

## Post-conditions

| # | Description |
|---|-------------|
| 1 | All commands remain registered |
| 2 | CLI state is unchanged |
| 3 | No side effects from command queries |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CLI_00001 | CLI Layer - Command registration | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_cli-layer.md |
| CLI Documentation | ../../setup.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_CLI_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CLI_00002 |
| Title | CLI Layer - Argument Parsing |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CLI layer correctly parses command-line arguments, including positional arguments, optional flags, and switches.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI commands are available |
| 3 | Test arguments are available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Positional Argument 1 | Input file path | Required input argument |
| Positional Argument 2 | Output file path | Required output argument |
| Optional Flag 1 | `-v` or `--verbose` | Verbose logging flag |
| Optional Flag 2 | `--skip-os-task` | Skip worksheet flag |
| Optional Flag 3 | `--skip-os-isr` | Skip worksheet flag |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse command with both positional arguments | Arguments parsed correctly |
| 2 | Verify input file argument | Input file path extracted correctly |
| 3 | Verify output file argument | Output file path extracted correctly |
| 4 | Parse command with verbose flag | Verbose flag recognized |
| 5 | Verify verbose flag value | Flag value is True |
| 6 | Parse command with skip flags | Skip flags recognized |
| 7 | Verify skip flag values | Flag values are True |
| 8 | Parse command with missing required argument | Error message indicates missing argument |
| 9 | Parse command with invalid flag | Error message indicates invalid flag |
| 10 | Verify argument type validation | File paths validated as strings |

## Expected Results

- Positional arguments are parsed correctly
- Optional flags are recognized and parsed
- Flag values are correct (True when present)
- Missing required arguments generate errors
- Invalid flags generate errors
- Argument types are validated correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Parsed arguments are available to command logic |
| 2 | No side effects from argument parsing |
| 3 | Parser can be reused for subsequent arguments |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CLI_00002 | CLI Layer - Argument parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_cli-layer.md |
| CLI Documentation | ../../src/eb_model/cli/os_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_CLI_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CLI_00003 |
| Title | CLI Layer - Help Display |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CLI layer correctly displays help messages, including usage information, available options, and command descriptions.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI commands are available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Help Option | `-h` or `--help` | Help flag |
| Command Name | os-xdm-xlsx | Test command |
| Expected Content | Usage, options, description | Help message components |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute command with -h option | Help message displayed |
| 2 | Execute command with --help option | Help message displayed |
| 3 | Verify usage line | Usage line shows correct syntax |
| 4 | Verify command description | Description is accurate and helpful |
| 5 | Verify positional arguments | Input and output arguments documented |
| 6 | Verify optional flags | All optional flags documented |
| 7 | Verify flag descriptions | Flag descriptions are clear |
| 8 | Verify exit code after help | Exit code is 0 (success) |
| 9 | Verify help format | Format is readable and consistent |
| 10 | Test help for all commands | All commands have help messages |

## Expected Results

- Help message is displayed for -h and --help
- Usage line is correct
- Command description is accurate
- Positional arguments are documented
- Optional flags are documented
- Flag descriptions are clear
- Exit code is 0 after help
- Help format is readable
- All commands have help messages

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No output files created (help only) |
| 2 | No side effects from help display |
| 3 | CLI state is unchanged |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CLI_00003 | CLI Layer - Help display | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_cli-layer.md |
| CLI Documentation | ../../src/eb_model/cli/os_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

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
---

# Test Case: TC_UNIT_CLI_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_CLI_00005 |
| Title | CLI Layer - Error Messages |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the CLI layer displays clear, actionable error messages for various error conditions.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI commands are available |
| 3 | Test scenarios for various errors |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Missing Input File | Non-existent file path | Test file not found error |
| Invalid Arguments | Wrong number of arguments | Test argument error |
| File Permission Error | File without read permission | Test permission error |
| Invalid File Format | Wrong file format | Test format error |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute command with missing input file | Error message displayed |
| 2 | Verify error message includes file path | Message identifies missing file |
| 3 | Execute command with invalid arguments | Error message displayed |
| 4 | Verify error message shows expected arguments | Message indicates what's expected |
| 5 | Execute command with file permission error | Error message displayed |
| 6 | Verify error message includes permission issue | Message indicates permission problem |
| 7 | Execute command with invalid file format | Error message displayed |
| 8 | Verify error message indicates format issue | Message is specific about format |
| 9 | Verify error message clarity | Message is understandable to user |
| 10 | Verify exit code for errors | Exit code is non-zero for errors |

## Expected Results

- Error messages are displayed for all error conditions
- Error messages include relevant context (file path, expected format, etc.)
- Error messages are clear and actionable
- Exit codes are non-zero for errors
- Error messages are consistent across commands

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No partial output files from errors |
| 2 | CLI state is clean after errors |
| 3 | System remains stable

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CLI_00005 | CLI Layer - Error messages | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_cli-layer.md |
| CLI Documentation | ../../src/eb_model/cli/os_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

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
