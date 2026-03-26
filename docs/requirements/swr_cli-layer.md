# Software Requirements Specification: CLI Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | CLI Layer Software Requirements Specification |
| Document ID | SWR_CLI_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | CLI Layer (Infrastructure) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the CLI Layer of py-eb-model. The CLI Layer provides command-line interface entry points for extracting and exporting XDM configuration data.

### 1.2 Scope

The CLI Layer shall:

- Provide CLI commands for each module type
- Parse command-line arguments
- Configure logging
- Handle errors gracefully
- Support verbose output mode

### 1.3 Definitions

| Term | Definition |
|------|------------|
| CLI | Command-Line Interface |
| XDM | XML Data Model - EB Tresos proprietary XML format |
| argparse | Python argument parsing library |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide
- [overview.md](overview.md) - System architecture

---

## 2. General Description

### 2.1 Product Functions

1. **Command Registration**: Register CLI entry points
2. **Argument Parsing**: Parse input/output arguments
3. **Logging Configuration**: Configure debug and error logging
4. **Error Handling**: Handle errors with user-friendly messages
5. **Help Display**: Show usage information

### 2.2 Constraints

- Python 3.9+ required
- argparse library (standard library)

---

## 3. Functional Requirements

**SWR_CLI_00001 - Command Registration**: Register CLI entry points.
- Register one command per module type
- Follow naming convention: `<module>-xdm-xlsx`
- Register PrefSystemImporter for preference import

**SWR_CLI_00002 - Argument Parsing**: Parse command-line arguments.
- Accept INPUT file path(s) as positional argument
- Accept OUTPUT file path as positional argument
- Support `-v/--verbose` flag for debug logging
- Support module-specific options

**SWR_CLI_00003 - Logging Configuration**: Configure logging output.
- Configure console logging for errors
- Configure file logging when verbose
- Use appropriate log format with timestamps

**SWR_CLI_00004 - Error Handling**: Handle errors gracefully.
- Display user-friendly error messages
- Exit with non-zero status on error
- Log detailed error information in verbose mode

**SWR_CLI_00005 - Help Display**: Show usage information.
- Display usage syntax
- Display available options
- Display version information

**SWR_CLI_00006 - Factory Integration**: Use parser factory for multiple inputs.
- Support multiple input files
- Automatically select parser based on file content
- Combine outputs into single workbook

---

## 4. Non-Functional Requirements

**SWR_CLI_00007**: Start up within 1 second.

**SWR_CLI_00008**: Display help within 1 second.

**SWR_CLI_00009**: Handle paths with spaces correctly.

---

## 5. Appendix

### 5.1 CLI Commands

| Command | Purpose |
|---------|---------|
| `os-xdm-xlsx` | Extract OS configuration |
| `rte-xdm-xlsx` | Extract RTE configuration |
| `nvm-xdm-xlsx` | Extract NvM configuration |
| `ecuc-xdm-xlsx` | Extract EcuC configuration |
| `bswm-xdm-xlsx` | Extract BswM configuration |
| `canif-xdm-xlsx` | Extract CanIf configuration |
| `cannm-xdm-xlsx` | Extract CanNm configuration |
| `cansm-xdm-xlsx` | Extract CanSm configuration |
| `cantp-xdm-xlsx` | Extract CanTp configuration |
| `linif-xdm-xlsx` | Extract LinIf configuration |
| `linsm-xdm-xlsx` | Extract LinSm configuration |
| `lintp-xdm-xlsx` | Extract LinTp configuration |
| `det-xdm-xlsx` | Extract Det configuration |
| `ecum-xdm-xlsx` | Extract EcuM configuration |
| `tm-xdm-xlsx` | Extract Tm configuration |
| `pbcfgm-xdm-xlsx` | Extract PbcfgM configuration |
| `PrefSystemImporter` | Import EB preference files |

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial specification |

---

**Document End**