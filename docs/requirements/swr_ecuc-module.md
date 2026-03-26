# Software Requirements Specification: EcuC Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | EcuC Module Software Requirements Specification |
| Document ID | SWR_ECUC_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | EcuC (ECU Configuration) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the EcuC module of py-eb-model. The EcuC module is responsible for extracting AUTOSAR ECU Configuration data from EB Tresos XDM (XML Data Model) files, enabling engineers to analyze ECU partitioning for memory protection, isolation, and multi-core support.

### 1.2 Scope

The EcuC module shall:

- Parse EB Tresos XDM files containing AUTOSAR EcuC configuration
- Model ECU partition definitions with their properties
- Parse software component instance references within partitions
- Support partition restart capability analysis
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
| EcuC | ECU Configuration - defines partitioning of ECU software |
| Partition | Memory isolation boundary separating software components and BSW modules |
| BSW | Basic Software - low-level software modules (drivers, services) |
| SWC | Software Component - application-level software component |
| XDM | XML Data Model - EB Tresos proprietary XML format for storing configuration |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide and code style conventions
- [overview.md](overview.md) - System architecture and common patterns
- AUTOSAR EcuC Specification - Industry standard for ECU configuration

---

## 2. General Description

### 2.1 Product Perspective

The EcuC module is part of the three-layer py-eb-model parsing system:

```
┌─────────────────────────────────────────────────────────────┐
│                     CLI Layer                                │
│  ecuc-xdm-xlsx command                                      │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Reporter Layer                              │
│  EcucXdmXlsWriter - Excel output                            │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   Model Layer                                │
│  EcuC, EcucPartitionCollection, EcucPartition, etc.         │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Parser Layer                                │
│  EcucXdmParser - XDM file parsing with namespace handling   │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              EB Tresos EcuC.xdm File                         │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Product Functions

The EcuC module shall provide the following functions:

1. **Partition Collection Management**: Extract partition collection container and all partition definitions
2. **Partition Configuration**: Extract partition attributes including restart capability and BSW partition flags
3. **Software Component Assignment**: Parse software component instance references within partitions
4. **Partition Analysis**: Support analysis of BSW vs application partitions
5. **Excel Export**: Generate multi-sheet Excel reports

### 2.3 User Characteristics

Target users are:
- Automotive software engineers working with AUTOSAR configurations
- System integrators analyzing partition distributions
- Technical reviewers validating memory isolation configurations

Users are expected to be familiar with:
- AUTOSAR partitioning concepts
- EB Tresos configuration tools
- Memory protection in embedded systems

### 2.4 Constraints

- **Python Version**: Requires Python 3.9 or higher
- **File Format**: Only supports EB Tresos XDM format, not generic AUTOSAR XML
- **Missing Attributes**: Some attributes (EcucPartitionId, EcucPartitionCoreRef) are not parsed
- **Namespace Handling**: XDM files use extensive XML namespaces requiring special parsing

### 2.5 Dependencies

| Dependency | Purpose | Version |
|------------|---------|---------|
| openpyxl | Excel file generation | Required (runtime) |
| xml.etree.ElementTree | XML parsing | Python standard library |
| logging | Debug and error logging | Python standard library |

---

## 3. Functional Requirements

**SWR_ECUC_00001 - Parser Layer**: The system shall parse EB Tresos XDM files containing EcuC configuration.
- Extract XML namespace definitions from XDM files and store them in a namespace map for XPath queries
- Validate that the datamodel root element module name is "EcuC" and raise a ValueError if it is not
- Extract AUTOSAR version and software version from the EcuC configuration
- Inherit common XML parsing methods from AbstractEbModelParser base class

**SWR_ECUC_00002 - Partition Collection**: The system shall parse and model ECU partition collection.
- Parse the EcucPartitionCollection container
- Extract all EcucPartition definitions within the collection
- Handle absence of partition collection gracefully

**SWR_ECUC_00003 - Partition Configuration**: The system shall parse and model ECU partition definitions.
- Extract partition name and default BSW partition flag
- Extract partition restart capability setting
- Extract partition reference (self-reference to partition definition)
- Support partition-to-core mappings for multi-core systems

**SWR_ECUC_00004 - Software Component Instance References**: The system shall parse software component assignments.
- Parse software component instance references within each partition
- Extract target references for each software component instance
- Support linking software components to their hosting partitions
- Handle empty TARGET references gracefully

**SWR_ECUC_00005 - Reporter Layer**: The system shall generate Excel (.xlsx) output with multiple worksheets.
- Create worksheets: EcucPartition, SoftwareComponent
- Apply auto-width column formatting to all worksheets
- Display partition definitions with restart capability in EcucPartition sheet
- Display software component assignments with partition name in SoftwareComponent sheet
- Handle None target references without runtime error

**SWR_ECUC_00006 - CLI Interface**: The system shall provide a command-line interface with the `ecuc-xdm-xlsx` command.
- Accept INPUT (XDM file path) and OUTPUT (Excel file path) as positional arguments
- Support `--verbose` or `-v` flag to enable debug logging
- Display version information in help text
- Log errors to console (stderr) with appropriate formatting

---

## 4. Non-Functional Requirements

**SWR_ECUC_00007**: The parser shall efficiently process XDM files of typical automotive configuration size (up to 10MB).

**SWR_ECUC_00008**: The reporter shall generate Excel files with acceptable performance for projects containing up to 100 partitions.

**SWR_ECUC_00009**: The system shall handle malformed XML gracefully and report meaningful error messages.

**SWR_ECUC_00010**: The system shall handle missing optional configuration elements without failing.

**SWR_ECUC_00011**: The parser shall inherit common XML parsing methods from AbstractEbModelParser base class.

**SWR_ECUC_00012**: The model classes shall use a fluent interface pattern to enable method chaining.

**SWR_ECUC_00013**: The code shall follow camelCase naming convention for methods and properties per AUTOSAR standards.

**SWR_ECUC_00014**: The system shall use factory pattern for parser selection (EbParserFactory).

---

## 5. Appendix

### 5.1 Data Model Class Hierarchy

```
Module (abstract)
  └── EcuC
      └── EcucPartitionCollection (extends EcucParamConfContainerDef)
          └── EcucPartition (extends EcucParamConfContainerDef)
              └── EcucPartitionSoftwareComponentInstanceRef
```

### 5.2 Limitations

1. **XDM Format Only**: Only supports EB Tresos XDM format, not generic AUTOSAR XML files.

2. **Missing Partition ID**: The EcucPartitionId attribute is defined but not parsed from XDM.

3. **Limited Attributes**: Several attributes are defined but not parsed:
   - EcucPartitionRef (commented out in parser)
   - EcucPartitionBswModuleDistinguishedPartitions
   - EcucPartitionCoreRef

4. **Empty Target References**: Reporter may fail on empty TARGET references.

5. **No Test Coverage**: No dedicated test files exist for EcuC parser.

6. **Thread Safety**: The parser is not thread-safe.

### 5.3 Future Enhancements

1. Add parsing for EcucPartitionId attribute.

2. Add parsing for core reference attributes for multi-core systems.

3. Add reference validation to check ASPath references.

4. Add dedicated test coverage for EcuC parser.

5. Add partition-to-OS-application mapping analysis.

### 5.4 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial requirements specification |

---

**Document End**