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