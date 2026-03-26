# Software Requirements Specification: BswM Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | BswM Module Software Requirements Specification |
| Document ID | SWR_BSWM_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | BswM (Basic Software Mode Manager) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the BswM module of py-eb-model. The BswM module is responsible for extracting AUTOSAR Basic Software Mode Manager configuration data from EB Tresos XDM (XML Data Model) files, enabling engineers to analyze mode management and coordination across basic software modules.

### 1.2 Scope

The BswM module shall:

- Parse EB Tresos XDM files containing AUTOSAR BswM configuration
- Model mode declaration groups and mode declarations
- Parse mode arbitration rules and action lists
- Support mode request processing analysis
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

**⚠️ Current Status**: This module is a stub implementation. Most requirements are not yet implemented.

The scope is limited to parsing XDM format files and does not include:
- Reference validation against actual AUTOSAR objects
- XDM file generation or modification
- Generic AUTOSAR XML file support (EB Tresos format only)

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture - a standardized automotive software architecture |
| BswM | Basic Software Mode Manager - manages mode switches across BSW modules |
| Mode | A distinct state of operation (e.g., NORMAL, SLEEP, DIAGNOSTIC) |
| Mode Arbitration | Decision logic for mode transitions |
| Action List | List of actions executed on mode switch |
| XDM | XML Data Model - EB Tresos proprietary XML format for storing configuration |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide and code style conventions
- [overview.md](overview.md) - System architecture and common patterns
- AUTOSAR BswM Specification - Industry standard for mode management

---

## 2. General Description

### 2.1 Product Perspective

The BswM module is part of the three-layer py-eb-model parsing system:

```
┌─────────────────────────────────────────────────────────────┐
│                     CLI Layer                                │
│  bswm-xdm-xlsx command                                      │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Reporter Layer                              │
│  BswMXdmXlsWriter - Excel output                            │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   Model Layer                                │
│  BswM, BswMModeDeclarationGroup, etc.                       │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Parser Layer                                │
│  BswMXdmParser - XDM file parsing with namespace handling   │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              EB Tresos BswM.xdm File                         │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Product Functions

The BswM module shall provide the following functions:

1. **Mode Declaration Management**: Parse mode declaration groups and mode declarations
2. **Mode Arbitration**: Parse mode arbitration rules and conditions
3. **Action List Management**: Parse mode switch action lists
4. **Mode Request Processing**: Parse mode request sources and targets
5. **Version Information**: Extract AUTOSAR and software version
6. **Excel Export**: Generate multi-sheet Excel reports

### 2.3 User Characteristics

Target users are:
- Automotive software engineers working with AUTOSAR mode management
- System integrators analyzing mode switching behavior
- Technical reviewers validating mode dependencies

Users are expected to be familiar with:
- AUTOSAR BswM concepts
- EB Tresos configuration tools
- Mode management in embedded systems

### 2.4 Constraints

- **Python Version**: Requires Python 3.9 or higher
- **File Format**: Only supports EB Tresos XDM format, not generic AUTOSAR XML
- **Namespace Handling**: XDM files use extensive XML namespaces requiring special parsing
- **Current Status**: Module is a stub implementation

### 2.5 Dependencies

| Dependency | Purpose | Version |
|------------|---------|---------|
| openpyxl | Excel file generation | Required (runtime) |
| xml.etree.ElementTree | XML parsing | Python standard library |
| logging | Debug and error logging | Python standard library |

---

## 3. Functional Requirements

**SWR_BSWM_00001 - Parser Layer**: The system shall parse EB Tresos XDM files containing BswM configuration.
- Extract XML namespace definitions from XDM files and store them in a namespace map for XPath queries
- Validate that the datamodel root element module name is "BswM" and raise a ValueError if it is not
- Extract AUTOSAR version and software version from the BswM configuration
- Inherit common XML parsing methods from AbstractEbModelParser base class

**SWR_BSWM_00002 - Mode Declaration Management**: The system shall parse and model mode declarations.
- Parse mode declaration group definitions
- Parse mode declaration instances within groups
- Parse mode request sources and targets
- Parse mode switching conditions

**SWR_BSWM_00003 - Mode Arbitration**: The system shall parse and model mode arbitration rules.
- Parse mode arbitration rule definitions
- Parse mode dependencies between rules
- Parse mode transition constraints
- Parse condition evaluation logic

**SWR_BSWM_00004 - Action List Management**: The system shall parse and model mode switch action lists.
- Parse mode switch action list definitions
- Parse initialization action lists
- Parse mode indication callback configurations
- Parse action execution order

**SWR_BSWM_00005 - Reporter Layer**: The system shall generate Excel (.xlsx) output with multiple worksheets.
- Create worksheets for mode declarations, arbitration rules, and action lists
- Apply auto-width column formatting to all worksheets
- Display mode declaration groups with their mode values
- Display arbitration rules with conditions and actions

**SWR_BSWM_00006 - CLI Interface**: The system shall provide a command-line interface with the `bswm-xdm-xlsx` command.
- Accept INPUT (XDM file path) and OUTPUT (Excel file path) as positional arguments
- Support `--verbose` or `-v` flag to enable debug logging
- Display version information in help text
- Log errors to console (stderr) with appropriate formatting

---

## 4. Non-Functional Requirements

**SWR_BSWM_00007**: The parser shall efficiently process XDM files of typical automotive configuration size (up to 10MB).

**SWR_BSWM_00008**: The reporter shall generate Excel files with acceptable performance for projects containing up to 100 mode rules.

**SWR_BSWM_00009**: The system shall handle malformed XML gracefully and report meaningful error messages.

**SWR_BSWM_00010**: The system shall handle missing optional configuration elements without failing.

**SWR_BSWM_00011**: The parser shall inherit common XML parsing methods from AbstractEbModelParser base class.

**SWR_BSWM_00012**: The model classes shall use a fluent interface pattern to enable method chaining.

**SWR_BSWM_00013**: The code shall follow camelCase naming convention for methods and properties per AUTOSAR standards.

**SWR_BSWM_00014**: The system shall use factory pattern for parser selection (EbParserFactory).

---

## 5. Appendix

### 5.1 Data Model Class Hierarchy

```
Module (abstract)
  └── BswM
      ├── BswMConfiguration (extends EcucParamConfContainerDef)
      ├── BswMModeDeclarationGroup (extends EcucParamConfContainerDef)
      │   └── BswMModeDeclaration
      ├── BswMModeRequestSource (extends EcucParamConfContainerDef)
      ├── BswMModeRequestPoint (extends EcucParamConfContainerDef)
      ├── BswMModeArbitration (extends EcucParamConfContainerDef)
      │   └── BswMModeArbitrationRule
      └── BswMSwitchActionList (extends EcucParamConfContainerDef)
```

### 5.2 Current Implementation Status

**⚠️ WARNING**: This module is currently a stub implementation.

| Component | Status | Notes |
|-----------|--------|-------|
| Parser | Stub | Validates file type only, no data extraction |
| Model | Minimal | Contains only logger, no BswM-specific attributes |
| Reporter | Incorrect | Exports OS data instead of BswM data |
| CLI | Missing | No entry point registered in setup.py |
| Tests | Missing | No test coverage |

### 5.3 Limitations

1. **No BswM Parsing**: Parser does not extract any BswM configuration.

2. **Incorrect Reporter**: Reporter exports OS data instead of BswM data.

3. **No CLI Entry**: No `bswm-xdm-xlsx` command available.

4. **No Test Coverage**: No test files exist.

5. **Placeholder Status**: Module is a placeholder for future implementation.

### 5.4 Future Enhancements

1. Implement BswM data model classes.

2. Implement BswM-specific parser logic.

3. Replace reporter with BswM-specific implementation.

4. Add CLI entry point registration.

5. Add comprehensive test coverage.

### 5.5 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial requirements specification |

---

**Document End**