# Software Requirements Specification: OS Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | OS Module Software Requirements Specification |
| Document ID | SWR_OS_00001 |
| Version | 1.0 |
| Date | 2026-03-23 |
| Project | py-eb-model |
| Module | OS (Operating System) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the OS module of py-eb-model. The OS module is responsible for extracting AUTOSAR Operating System configuration data from EB Tresos XDM (XML Data Model) files and transforming it into structured Python objects and Excel reports.

### 1.2 Scope

The OS module shall:

- Parse EB Tresos XDM files containing AUTOSAR OS configuration
- Model OS entities including tasks, ISRs, schedule tables, counters, applications, alarms, resources, and memory protection
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
| EB Tresos | Elektronikbit automotive configuration tool for AUTOSAR projects |
| XDM | XML Data Model - EB Tresos proprietary XML format for storing configuration |
| ASPath | AUTOSAR Path format for referencing configuration elements (`ASPath:/path/to/element`) |
| ISR | Interrupt Service Routine - handler for hardware interrupts |
| OS Application | Logical grouping of OS objects for memory protection and isolation |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide and code style conventions
- [overview.md](overview.md) - System architecture and common patterns
- AUTOSAR OS Specification - Industry standard for automotive operating systems

---

## 2. General Description

### 2.1 Product Perspective

The OS module is part of the three-layer py-eb-model parsing system:

```
┌─────────────────────────────────────────────────────────────┐
│                     CLI Layer                                │
│  os-xdm-xlsx command                                         │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Reporter Layer                              │
│  OsXdmXlsWriter - Excel output                              │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   Model Layer                                │
│  Os, OsTask, OsIsr, OsScheduleTable, OsCounter, etc.       │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Parser Layer                                │
│  OsXdmParser - XDM file parsing with namespace handling     │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              EB Tresos Os.xdm File                           │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Product Functions

The OS module shall provide the following functions:

1. **Task Management**: Extract task definitions with priorities, stacks, and scheduling
2. **ISR Management**: Extract interrupt service routines with hardware-specific attributes
3. **Schedule Table Management**: Extract cyclic scheduling configurations
4. **Counter Management**: Extract time measurement counters
5. **Application Management**: Extract OS application boundaries and mappings
6. **Alarm Management**: Extract time-based alarm configurations
7. **Resource Management**: Extract resource definitions and access patterns
8. **Memory Protection**: Extract EB Safety OS memory region configurations
9. **Excel Export**: Generate multi-sheet Excel reports

### 2.3 User Characteristics

Target users are:
- Automotive software engineers working with AUTOSAR configurations
- System integrators validating OS configurations
- Technical reviewers analyzing system scheduling and resource allocation

Users are expected to be familiar with:
- AUTOSAR OS concepts
- EB Tresos configuration tools
- Basic command-line interface usage

### 2.4 Constraints

- **Python Version**: Requires Python 3.9 or higher
- **File Format**: Only supports EB Tresos XDM format, not generic AUTOSAR XML
- **Namespace Handling**: XDM files use extensive XML namespaces requiring special parsing
- **Reference Validation**: ASPath references are extracted but not validated

### 2.5 Dependencies

| Dependency | Purpose | Version |
|------------|---------|---------|
| openpyxl | Excel file generation | Required (runtime) |
| xml.etree.ElementTree | XML parsing | Python standard library |
| logging | Debug and error logging | Python standard library |

---

## 3. Functional Requirements

**SWR_OS_00001 - Parser Layer**: The system shall parse EB Tresos XDM files containing OS configuration.
- Extract XML namespace definitions from XDM files and store them in a namespace map for XPath queries
- Validate that the datamodel root element module name is "Os" and raise a ValueError if it is not
- Extract AUTOSAR version and software version from the OS configuration
- Inherit common XML parsing methods from AbstractEbModelParser base class

**SWR_OS_00002 - Task Management**: The system shall parse and model OS task definitions.
- Extract name, priority, activation count, schedule type (FULL/NON), and stack size
- Extract task type (BASIC/EXTENDED) for memory planning
- Parse task autostart configuration with application mode references
- Parse task resource references for resource locking analysis
- Provide an `IsPreemptable()` method that returns true if the schedule type is FULL
- Map tasks to their parent OS applications for O(1) lookup

**SWR_OS_00003 - ISR Management**: The system shall parse and model Interrupt Service Routines (ISRs).
- Extract category (CATEGORY_1 or CATEGORY_2), priority, vector, and stack size
- Extract Infineon AURIX TriCore-specific attributes (TricoreIrqLevel, TricoreVector)
- Extract ARM core-specific attributes (ARMIrqLevel, ARMVector)
- Parse EB Safety OS memory region references
- Extract ISR period when defined
- Map ISRs to their parent OS applications for O(1) lookup

**SWR_OS_00004 - Schedule Tables**: The system shall parse and model schedule tables for cyclic scheduling.
- Extract duration, repeating behavior, and counter references
- Parse expiry points with offset values
- Parse task activation configurations and event settings at expiry points
- Parse adjustable expiry points with max lengthen and max shorten values
- Support time unit specifications (NANOSECONDS or TICKS) and validate against allowed values
- Sort expiry points by offset when generating reports

**SWR_OS_00005 - Counters**: The system shall parse and model time measurement counters.
- Extract max allowed value, min cycle, ticks per base, and counter type (HARDWARE/SOFTWARE)
- Extract seconds per tick configuration when present
- Parse driver references and time constant references when present

**SWR_OS_00006 - Applications**: The system shall parse and model OS applications for memory protection and isolation.
- Extract trusted status and core assignment
- Parse application-to-partition references for multi-core systems
- Parse references to tasks, ISRs, resources, alarms, counters, and schedule tables
- Maintain lookup mappings for task-to-application and ISR-to-application relationships

**SWR_OS_00007 - Alarms**: The system shall parse and model time-based alarms.
- Parse counter references and alarm accessing application references
- Parse alarm action configurations including:
  - ActivateTask: Reference to task to activate
  - IncrementCounter: Reference to counter to increment
  - SetEvent: Reference to event and task
  - Callback: Callback function name
- Raise a ValueError if an alarm action is not specified or unsupported

**SWR_OS_00008 - Resources**: The system shall parse and model resources for exclusive access management.
- Extract properties (STANDARD or INTERNAL)
- Parse resource accessing application references
- Extract importer information attributes
- Support calculated service access references (including `@CALC(SvcAs,...)` syntax)

**SWR_OS_00009 - Memory Protection**: The system shall parse and model EB Safety OS memory protection configuration.
- Parse microkernel memory protection configuration when present
- Parse memory region definitions with access flags for InitThread, IdleThread, OsThread, ErrorHook, ProtHook, ShutdownHook, Shutdown, Kernel access, and Initialize per-core settings
- Parse memory region initialization and global scope flags
- Handle absence of memory protection configuration gracefully

**SWR_OS_00010 - Reporter Layer**: The system shall generate Excel (.xlsx) output with multiple worksheets.
- Create worksheets: OsTask, OsApplications, OsIsr, OsScheduleTable, OsCounter, OsScheduleTableExpiryPoint, MkMemoryRegion (if present)
- Apply auto-width column formatting to all worksheets
- Center-align numeric data
- Wrap text for cells containing multiple values (2-10 items)
- Display summary text for lists exceeding 10 items
- Support skipping the OsTask worksheet via configuration option

**SWR_OS_00011 - CLI Interface**: The system shall provide a command-line interface with the `os-xdm-xlsx` command.
- Accept INPUT (XDM file path) and OUTPUT (Excel file path) as positional arguments
- Support `--verbose` or `-v` flag to enable debug logging to `os_xdm_2_xls.log` in output directory
- Support `--skip-os-task` flag to skip OsTask worksheet generation
- Display version information in help text
- Log errors to console (stderr) with appropriate formatting

---

## 4. Non-Functional Requirements

**SWR_OS_00012**: The parser shall efficiently process XDM files of typical automotive configuration size (up to 10MB).

**SWR_OS_00013**: The reporter shall generate Excel files with acceptable performance for projects containing up to 1000 tasks/ISRs.

**SWR_OS_00014**: The parser shall use dictionary-based mappings for O(1) lookup of task-to-application and ISR-to-application relationships.

**SWR_OS_00015**: The system shall handle malformed XML gracefully and report meaningful error messages.

**SWR_OS_00016**: The system shall handle missing optional configuration elements without failing.

**SWR_OS_00017**: The system shall validate required configuration elements and raise descriptive errors when missing.

**SWR_OS_00018**: The system shall validate input file paths to prevent path traversal attacks.

**SWR_OS_00019**: The system shall handle XML parsing safely to prevent XML injection attacks.

**SWR_OS_00020**: The parser shall inherit common XML parsing methods from AbstractEbModelParser base class.

**NREQ-OS-4.10**: The model classes shall use a fluent interface pattern to enable method chaining.

**NREQ-OS-4.11**: The code shall follow camelCase naming convention for methods and properties per AUTOSAR standards.

**NREQ-OS-4.12**: The system shall use factory pattern for parser selection (EbParserFactory).

---

## 5. Appendix

### 5.1 Data Model Class Hierarchy

```
Module (abstract)
  └── Os
      ├── OsTask (extends EcucObject)
      ├── OsIsr (extends EcucObject)
      ├── OsAlarm (extends EcucParamConfContainerDef)
      │   ├── OsAlarmActivateTask (extends OsAlarmAction)
      │   ├── OsAlarmIncrementCounter (extends OsAlarmAction)
      │   ├── OsAlarmSetEvent (extends OsAlarmAction)
      │   └── OsAlarmCallback (extends OsAlarmAction)
      ├── OsScheduleTable (extends EcucParamConfContainerDef)
      │   └── OsScheduleTableExpiryPoint
      │       ├── OsScheduleTableTaskActivation
      │       ├── OsScheduleTableEventSetting
      │       └── OsScheduleTblAdjustableExpPoint
      ├── OsCounter (extends EcucParamConfContainerDef)
      ├── OsApplication (extends EcucParamConfContainerDef)
      ├── OsResource (extends EcucParamConfContainerDef)
      └── OsMicrokernel (extends EcucParamConfContainerDef)
          └── MkMemoryProtection
              └── MkMemoryRegion (extends EcucObject)
```

### 5.2 Limitations

1. **XDM Format Only**: Only supports EB Tresos XDM format, not generic AUTOSAR XML files.

2. **Reference Validation**: ASPath references are extracted but not validated against actual targets.

3. **Vendor-Specific Attributes**: TriCore and ARM attributes are read independently; which set is populated depends on the target hardware.

4. **Calculated References**: Resource references using `@CALC(SvcAs,...)` syntax are stored but not evaluated.

5. **Test Coverage**: Alarms, schedule tables, and microkernel features have limited test coverage.

6. **Thread Safety**: The parser is not thread-safe.

### 5.3 Future Enhancements

1. Add reference validation to check ASPath references against actual objects.

2. Extend support to generic AUTOSAR XML files.

3. Add CSV output format option.

4. Implement JSON output format.

5. Add configuration validation against AUTOSAR constraints.

6. Enhance test coverage for all OS entities.

### 5.4 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-23 | Claude Code | Initial requirements specification |

---

**Document End**