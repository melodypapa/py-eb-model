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