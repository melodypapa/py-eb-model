# Software Requirements Specification: RTE Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | RTE Module Software Requirements Specification |
| Document ID | SWR_RTE_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | RTE (Runtime Environment) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the RTE module of py-eb-model. The RTE module is responsible for extracting AUTOSAR Runtime Environment configuration data from EB Tresos XDM (XML Data Model) files, enabling engineers to analyze how runnable entities are mapped to OS tasks and trace event-to-task mappings.

### 1.2 Scope

The RTE module shall:

- Parse EB Tresos XDM files containing AUTOSAR RTE configuration
- Model BSW module instances and software component instances with their event-to-task mappings
- Support both AUTOSAR 3.x and 4.x event reference formats
- Export event-to-task mapping data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

The scope is limited to parsing XDM format files and does not include:
- Reference validation against actual AUTOSAR objects
- XDM file generation or modification
- Generic AUTOSAR XML file support (EB Tresos format only)

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture - a standardized automotive software architecture |
| RTE | Runtime Environment - middleware layer enabling communication between software components |
| BSW | Basic Software - low-level software modules (drivers, services) |
| SWC | Software Component - application-level software component |
| XDM | XML Data Model - EB Tresos proprietary XML format for storing configuration |
| ASPath | AUTOSAR Path format for referencing configuration elements (`ASPath:/path/to/element`) |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide and code style conventions
- [overview.md](overview.md) - System architecture and common patterns
- AUTOSAR RTE Specification - Industry standard for automotive runtime environment

---

## 2. General Description

### 2.1 Product Perspective

The RTE module is part of the three-layer py-eb-model parsing system:

```
┌─────────────────────────────────────────────────────────────┐
│                     CLI Layer                                │
│  rte-xdm-xlsx command                                       │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Reporter Layer                              │
│  RteXdmXlsWriter, RteRunnableEntityXlsWriter                │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   Model Layer                                │
│  Rte, RteBswModuleInstance, RteSwComponentInstance, etc.    │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Parser Layer                                │
│  RteXdmParser - XDM file parsing with namespace handling    │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              EB Tresos Rte.xdm File                          │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Product Functions

The RTE module shall provide the following functions:

1. **BSW Module Instance Management**: Extract BSW module instance definitions with implementation references and event-to-task mappings
2. **Software Component Instance Management**: Extract SW component instance definitions with component references and event-to-task mappings
3. **Event-to-Task Mapping**: Parse and model how events are mapped to OS tasks with timing information
4. **AUTOSAR Version Support**: Support both AUTOSAR 3.x (single event reference) and 4.x (multiple event references) formats
5. **Excel Export**: Generate multi-sheet Excel reports with event mapping information

### 2.3 User Characteristics

Target users are:
- Automotive software engineers working with AUTOSAR configurations
- System integrators analyzing RTE event-to-task mappings
- Technical reviewers validating scheduling and timing configurations

Users are expected to be familiar with:
- AUTOSAR RTE concepts
- EB Tresos configuration tools
- Basic command-line interface usage

### 2.4 Constraints

- **Python Version**: Requires Python 3.9 or higher
- **File Format**: Only supports EB Tresos XDM format, not generic AUTOSAR XML
- **OS Dependency**: Runnable entity export requires both Rte.xdm and Os.xdm to be parsed
- **Namespace Handling**: XDM files use extensive XML namespaces requiring special parsing

### 2.5 Dependencies

| Dependency | Purpose | Version |
|------------|---------|---------|
| openpyxl | Excel file generation | Required (runtime) |
| xml.etree.ElementTree | XML parsing | Python standard library |
| logging | Debug and error logging | Python standard library |
| OS Module | Required for resolving task references in runnable entity export | py-eb-model |

---

## 3. Functional Requirements

**SWR_RTE_00001 - Parser Layer**: The system shall parse EB Tresos XDM files containing RTE configuration.
- Extract XML namespace definitions from XDM files and store them in a namespace map for XPath queries
- Validate that the datamodel root element module name is "Rte" and raise a ValueError if it is not
- Extract AUTOSAR version and software version from the RTE configuration
- Inherit common XML parsing methods from AbstractEbModelParser base class

**SWR_RTE_00002 - BSW Module Instance Management**: The system shall parse and model BSW module instances.
- Extract BSW module instance definitions with implementation references
- Extract OS application mappings for BSW instances
- Parse BSW event-to-task mappings including activation offset, period, and position in task
- Parse server queue length for client-server communication
- Support both AUTOSAR 3.x (single event ref) and 4.x (multiple event refs) formats

**SWR_RTE_00003 - Software Component Instance Management**: The system shall parse and model software component instances.
- Extract software component instance definitions with component instance references
- Extract OS application mappings for component instances
- Parse event-to-task mappings including activation offset, period, and position in task
- Parse server queue length for client-server communication
- Support both AUTOSAR 3.x (single event ref) and 4.x (multiple event refs) formats

**SWR_RTE_00004 - Event Reference Handling**: The system shall handle AUTOSAR version-specific event reference formats.
- Use RteEventToTaskMappingV3 for AUTOSAR 3.x (major version < 4) with single event reference
- Use RteEventToTaskMappingV4 for AUTOSAR 4.x (major version >= 4) with multiple event references
- Provide getRteEventRef() method that returns single reference or raises ValueError for multiple events
- Provide getRteEventRefs() method that returns list of all event references

**SWR_RTE_00005 - Event-to-Task Mapping Analysis**: The system shall provide analysis capabilities for event mappings.
- Group event-to-task mappings by target OS task name via getMappedEvents() method
- Sort mappings by position in task for execution order analysis
- Distinguish between BSW module events and software component events
- Support events with no task mapping (events not mapped to any task)

**SWR_RTE_00006 - Reporter Layer**: The system shall generate Excel (.xlsx) output with multiple worksheets.
- Create worksheets: OsTask, OsIsr (when OS data is available), Event Mapping (for runnable entity export)
- Apply auto-width column formatting to all worksheets
- Display event name, instance, position, and offset information
- Support grouping by OS task name

**SWR_RTE_00007 - CLI Interface**: The system shall provide a command-line interface with the `rte-xdm-xlsx` command.
- Accept INPUT (XDM file paths) and OUTPUT (Excel file path) as positional arguments
- Support multiple input files (Rte.xdm, Os.xdm, etc.) processed by factory pattern
- Support `-r` flag for runnable entities export mode
- Support `--verbose` or `-v` flag to enable debug logging
- Display version information in help text

---

## 4. Non-Functional Requirements

**SWR_RTE_00008**: The parser shall efficiently process XDM files of typical automotive configuration size (up to 10MB).

**SWR_RTE_00009**: The reporter shall generate Excel files with acceptable performance for projects containing up to 500 event-to-task mappings.

**SWR_RTE_00010**: The system shall handle malformed XML gracefully and report meaningful error messages.

**SWR_RTE_00011**: The system shall handle missing optional configuration elements without failing.

**SWR_RTE_00012**: The parser shall inherit common XML parsing methods from AbstractEbModelParser base class.

**SWR_RTE_00013**: The model classes shall use a fluent interface pattern to enable method chaining.

**SWR_RTE_00014**: The code shall follow camelCase naming convention for methods and properties per AUTOSAR standards.

**SWR_RTE_00015**: The system shall use factory pattern for parser selection (EbParserFactory).

---

## 5. Appendix

### 5.1 Data Model Class Hierarchy

```
Module (abstract)
  └── Rte
      ├── RteBswModuleInstance (extends AbstractRteInstance)
      │   ├── RteBswEventToTaskMapping (extends AbstractEventToTaskMapping)
      │   │   ├── RteBswEventToTaskMappingV3 (AR 3.x - single event ref)
      │   │   └── RteBswEventToTaskMappingV4 (AR 4.x - multiple event refs)
      │   └── RteEventToIsrMapping
      └── RteSwComponentInstance (extends AbstractRteInstance)
          ├── RteEventToTaskMapping (extends AbstractEventToTaskMapping)
          │   ├── RteEventToTaskMappingV3 (AR 3.x - single event ref)
          │   └── RteEventToTaskMappingV4 (AR 4.x - multiple event refs)
          └── RteEventToIsrMapping
```

### 5.2 Limitations

1. **XDM Format Only**: Only supports EB Tresos XDM format, not generic AUTOSAR XML files.

2. **OS Dependency**: Runnable entity export requires both Rte.xdm and Os.xdm to be parsed.

3. **Reference Validation**: ASPath references are extracted but not validated against actual targets.

4. **AR 4.0 Multiple Events**: Calling getRteEventRef() on a mapping with multiple events raises ValueError.

5. **Limited Test Coverage**: No dedicated test files for RTE parser exist in the current codebase.

6. **Unmapped Events**: Events with no task mapping are excluded from getMappedEvents() output.

7. **Thread Safety**: The parser is not thread-safe.

### 5.3 Future Enhancements

1. Add reference validation to check ASPath references against actual objects.

2. Add dedicated test coverage for RTE parser.

3. Implement JSON output format.

4. Add support for ISR mappings analysis.

### 5.4 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial requirements specification |

---

**Document End**