# Software Requirements Specification: NvM Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | NvM Module Software Requirements Specification |
| Document ID | SWR_NVM_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | NvM (Non-Volatile Memory) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the NvM module of py-eb-model. The NvM module is responsible for extracting AUTOSAR Non-Volatile Memory configuration data from EB Tresos XDM (XML Data Model) files, enabling engineers to analyze data persistence configurations for preserving configuration data, adaptation values, and DTCs across power cycles.

### 1.2 Scope

The NvM module shall:

- Parse EB Tresos XDM files containing AUTOSAR NvM configuration
- Model NvM block descriptors with memory layer references
- Parse NvM common configuration with global settings
- Support EEPROM Abstraction (EA) and Flash EEPROM Emulation (FEE) layer references
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

The scope is limited to parsing XDM format files and does not include:
- Reference validation against actual AUTOSAR objects
- XDM file generation or modification
- Generic AUTOSAR XML file support (EB Tresos format only)

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture - a standardized automotive software architecture |
| NvM | Non-Volatile Memory manager - handles data persistence in automotive systems |
| EA | EEPROM Abstraction - abstraction layer for direct EEPROM access |
| FEE | Flash EEPROM Emulation - flash-based EEPROM emulation layer |
| XDM | XML Data Model - EB Tresos proprietary XML format for storing configuration |
| ASPath | AUTOSAR Path format for referencing configuration elements |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide and code style conventions
- [overview.md](overview.md) - System architecture and common patterns
- AUTOSAR NvM Specification - Industry standard for non-volatile memory management

---

## 2. General Description

### 2.1 Product Perspective

The NvM module is part of the three-layer py-eb-model parsing system:

```
┌─────────────────────────────────────────────────────────────┐
│                     CLI Layer                                │
│  nvm-xdm-xlsx command                                       │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Reporter Layer                              │
│  NvMXdmXlsWriter - Excel output                             │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   Model Layer                                │
│  NvM, NvMBlockDescriptor, NvMCommon, etc.                   │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Parser Layer                                │
│  NvMXdmParser - XDM file parsing with namespace handling    │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              EB Tresos NvM.xdm File                          │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Product Functions

The NvM module shall provide the following functions:

1. **Common Configuration Management**: Extract global NvM settings including CRC, queue sizes, and partition references
2. **Block Descriptor Management**: Extract NvM block configurations with memory layer references
3. **Memory Layer Reference Support**: Support both EA (EEPROM Abstraction) and FEE (Flash EEPROM Emulation) references
4. **Callback Configuration**: Parse callback function references for data validation and synchronization
5. **Partition Distribution Analysis**: Analyze block distribution across ECU partitions
6. **Excel Export**: Generate multi-sheet Excel reports

### 2.3 User Characteristics

Target users are:
- Automotive software engineers working with AUTOSAR memory configurations
- System integrators analyzing memory block distributions
- Technical reviewers validating data persistence configurations

Users are expected to be familiar with:
- AUTOSAR NvM concepts
- EB Tresos configuration tools
- Memory management in embedded systems

### 2.4 Constraints

- **Python Version**: Requires Python 3.9 or higher
- **File Format**: Only supports EB Tresos XDM format, not generic AUTOSAR XML
- **EA Reference Limitation**: Reporter raises NotImplementedError for EA references (only FEE fully supported)
- **Namespace Handling**: XDM files use extensive XML namespaces requiring special parsing

### 2.5 Dependencies

| Dependency | Purpose | Version |
|------------|---------|---------|
| openpyxl | Excel file generation | Required (runtime) |
| xml.etree.ElementTree | XML parsing | Python standard library |
| logging | Debug and error logging | Python standard library |

---

## 3. Functional Requirements

**SWR_NVM_00001 - Parser Layer**: The system shall parse EB Tresos XDM files containing NvM configuration.
- Extract XML namespace definitions from XDM files and store them in a namespace map for XPath queries
- Validate that the datamodel root element module name is "NvM" and raise a ValueError if it is not
- Extract AUTOSAR version and software version from the NvM configuration
- Inherit common XML parsing methods from AbstractEbModelParser base class

**SWR_NVM_00002 - Common Configuration**: The system shall parse and model NvM common configuration.
- Extract API configuration class and version information
- Extract CRC configuration including number of bytes
- Extract dataset selection bits for multi-block datasets
- Extract error detection and development error detection settings
- Extract job prioritization, queue sizes, and main function period
- Extract EcuC partition references for multi-partition systems
- Extract master EcuC partition reference

**SWR_NVM_00003 - Block Descriptor Management**: The system shall parse and model NvM block descriptors.
- Extract block identifier, block number, and base number
- Extract block length (size in bytes) and management type
- Extract job priority and resistance to software changes
- Extract ROM block and RAM block data addresses
- Extract CRC type and CRC usage settings
- Extract read/write all selection flags
- Extract EcuC partition reference for block

**SWR_NVM_00004 - Memory Layer References**: The system shall parse and model memory layer references.
- Parse NvMEaRef for EEPROM Abstraction layer block references
- Parse NvMFeeRef for Flash EEPROM Emulation layer block references
- Use choice field to determine correct reference type
- Raise ValueError for invalid choice values in target block reference

**SWR_NVM_00005 - Callback Configuration**: The system shall parse and model NvM callback configurations.
- Extract init block callback function reference
- Extract single block callback function reference
- Extract read RAM block from NvM callback
- Extract write RAM block to NvM callback
- Handle absence of optional callbacks gracefully

**SWR_NVM_00006 - Reporter Layer**: The system shall generate Excel (.xlsx) output with multiple worksheets.
- Create worksheets: General, BSW Distribution, Block List
- Apply auto-width column formatting to all worksheets
- Display key-value pairs for common settings in General sheet
- Display partition distribution with master indicator in BSW Distribution sheet
- Display block details with all attributes in Block List sheet
- Skip General and BSW Distribution sheets if NvMCommon is not present

**SWR_NVM_00007 - CLI Interface**: The system shall provide a command-line interface with the `nvm-xdm-xlsx` command.
- Accept INPUT (XDM file path) and OUTPUT (Excel file path) as positional arguments
- Support `--verbose` or `-v` flag to enable debug logging
- Display version information in help text
- Log errors to console (stderr) with appropriate formatting

---

## 4. Non-Functional Requirements

**SWR_NVM_00008**: The parser shall efficiently process XDM files of typical automotive configuration size (up to 10MB).

**SWR_NVM_00009**: The reporter shall generate Excel files with acceptable performance for projects containing up to 500 NvM blocks.

**SWR_NVM_00010**: The system shall handle malformed XML gracefully and report meaningful error messages.

**SWR_NVM_00011**: The system shall handle missing optional configuration elements without failing.

**SWR_NVM_00012**: The system shall validate required configuration elements and raise descriptive errors when missing.

**SWR_NVM_00013**: The parser shall inherit common XML parsing methods from AbstractEbModelParser base class.

**SWR_NVM_00014**: The model classes shall use a fluent interface pattern to enable method chaining.

**SWR_NVM_00015**: The code shall follow camelCase naming convention for methods and properties per AUTOSAR standards.

**SWR_NVM_00016**: The system shall use factory pattern for parser selection (EbParserFactory).

---

## 5. Appendix

### 5.1 Data Model Class Hierarchy

```
Module (abstract)
  └── NvM
      ├── NvMCommon (extends EcucParamConfContainerDef)
      │   └── NvMEcucPartitionRef (partition references)
      └── NvMBlockDescriptor (extends EcucParamConfContainerDef)
          ├── NvMTargetBlockReference (abstract)
          │   ├── NvMEaRef (EEPROM Abstraction)
          │   └── NvMFeeRef (Flash EEPROM Emulation)
          ├── NvMInitBlockCallback
          ├── NvMSingleBlockCallback
          ├── NvMReadRamBlockFromNvCallback
          └── NvMWriteRamBlockToNvCallback
```

### 5.2 Limitations

1. **XDM Format Only**: Only supports EB Tresos XDM format, not generic AUTOSAR XML files.

2. **EA Reference Not Supported**: The reporter raises NotImplementedError for NvMEaRef target block references. Only NvMFeeRef is fully supported in Excel export.

3. **Missing Configuration**: If NvMCommon is not present, General and BSW Distribution sheets are skipped.

4. **Hardcoded Values**: Some values in General sheet are hardcoded regardless of actual configuration.

5. **Optional Attributes**: Many block attributes are optional and may be None.

6. **Limited Test Coverage**: Edge cases for different memory layer references have limited testing.

7. **Thread Safety**: The parser is not thread-safe.

### 5.3 Future Enhancements

1. Add full support for EA (EEPROM Abstraction) references in Excel export.

2. Add reference validation to check ASPath references against actual objects.

3. Add CSV output format option.

4. Implement JSON output format.

5. Add configuration validation against AUTOSAR constraints.

### 5.4 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial requirements specification |

---

**Document End**