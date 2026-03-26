# Software Requirements Specification: CanIf Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | CanIf Module Software Requirements Specification |
| Document ID | SWR_CANIF_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | CanIf (CAN Interface) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the CanIf module of py-eb-model. The CanIf module is responsible for extracting AUTOSAR CAN Interface configuration data from EB Tresos XDM (XML Data Model) files, enabling engineers to analyze CAN communication configurations including controllers, transceivers, and PDU routing.

### 1.2 Scope

The CanIf module shall:

- Parse EB Tresos XDM files containing AUTOSAR CanIf configuration
- Model CAN controller and transceiver configurations
- Parse Rx/Tx PDU configurations with CAN ID mappings
- Support HRH (Hardware Receive Handle) and HTH (Hardware Transmit Handle) configurations
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture - a standardized automotive software architecture |
| CanIf | CAN Interface - abstraction layer for CAN communication |
| PDU | Protocol Data Unit - data packet in communication |
| HRH | Hardware Receive Handle - receive configuration identifier |
| HTH | Hardware Transmit Handle - transmit configuration identifier |
| XDM | XML Data Model - EB Tresos proprietary XML format for storing configuration |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide and code style conventions
- [overview.md](overview.md) - System architecture and common patterns
- AUTOSAR CanIf Specification - Industry standard for CAN interface

---

## 2. General Description

### 2.1 Product Perspective

The CanIf module is part of the three-layer py-eb-model parsing system:

```
┌─────────────────────────────────────────────────────────────┐
│                     CLI Layer                                │
│  canif-xdm-xlsx command                                     │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Reporter Layer                              │
│  CanIfXdmXlsWriter - Excel output                           │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   Model Layer                                │
│  CanIf, CanIfGeneral, CanIfCtrlCfg, etc.                    │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Parser Layer                                │
│  CanIfXdmParser - XDM file parsing with namespace handling  │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              EB Tresos CanIf.xdm File                        │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Product Functions

The CanIf module shall provide the following functions:

1. **General Configuration**: Extract public and private configuration settings
2. **Controller Configuration**: Parse CAN controller configurations with wakeup support
3. **Transceiver Configuration**: Parse CAN transceiver configurations
4. **Buffer Configuration**: Parse buffer configurations for transmission
5. **HRH/HTH Configuration**: Parse hardware handle configurations
6. **PDU Configuration**: Parse Rx and Tx PDU configurations with CAN ID mappings
7. **Excel Export**: Generate multi-sheet Excel reports

### 2.3 User Characteristics

Target users are:
- Automotive software engineers working with CAN communication
- System integrators analyzing PDU routing configurations
- Technical reviewers validating CAN ID assignments

### 2.4 Constraints

- **Python Version**: Requires Python 3.9 or higher
- **File Format**: Only supports EB Tresos XDM format
- **Namespace Handling**: XDM files use extensive XML namespaces

### 2.5 Dependencies

| Dependency | Purpose | Version |
|------------|---------|---------|
| openpyxl | Excel file generation | Required (runtime) |
| xml.etree.ElementTree | XML parsing | Python standard library |

---

## 3. Functional Requirements

**SWR_CANIF_00001 - Parser Layer**: The system shall parse EB Tresos XDM files containing CanIf configuration.
- Validate that the datamodel root element module name is "CanIf"
- Extract AUTOSAR version and software version
- Inherit common XML parsing methods from AbstractEbModelParser

**SWR_CANIF_00002 - General Configuration**: The system shall parse and model CanIf general configuration.
- Extract error detection settings (CanIfDevErrorDetect)
- Extract number of CAN hardware units
- Extract maximum controller, Tx PDU, and Rx PDU counts
- Extract TTCAN support flag

**SWR_CANIF_00003 - Controller Configuration**: The system shall parse and model CAN controller configurations.
- Extract controller ID and wakeup support flag
- Extract CAN controller reference for hardware mapping
- Support multiple controller configurations

**SWR_CANIF_00004 - Transceiver Configuration**: The system shall parse and model CAN transceiver configurations.
- Extract transceiver ID and wakeup support flag
- Extract CAN transceiver reference for hardware mapping
- Support multiple transceiver configurations

**SWR_CANIF_00005 - Buffer Configuration**: The system shall parse and model buffer configurations.
- Extract buffer size
- Extract HTH reference for transmit buffer
- Support multiple buffer configurations

**SWR_CANIF_00006 - HRH Configuration**: The system shall parse and model hardware receive handle configurations.
- Extract software filter flag
- Extract CAN controller ID reference
- Support multiple HRH configurations

**SWR_CANIF_00007 - HTH Configuration**: The system shall parse and model hardware transmit handle configurations.
- Extract CAN controller ID reference
- Support multiple HTH configurations

**SWR_CANIF_00008 - Rx PDU Configuration**: The system shall parse and model receive PDU configurations.
- Extract CAN ID and CAN ID type
- Extract DLC and PDU ID
- Extract HRH reference and upper layer reference
- Support multiple Rx PDU configurations

**SWR_CANIF_00009 - Tx PDU Configuration**: The system shall parse and model transmit PDU configurations.
- Extract CAN ID, CAN ID type, and DLC
- Extract PDU ID and PDU type
- Extract buffer reference, HTH reference, and upper layer reference
- Support multiple Tx PDU configurations

**SWR_CANIF_00010 - Reporter Layer**: The system shall generate Excel (.xlsx) output with multiple worksheets.
- Create worksheets for controllers, transceivers, buffers, HRH, HTH, Rx PDUs, Tx PDUs
- Apply auto-width column formatting

**SWR_CANIF_00011 - CLI Interface**: The system shall provide a command-line interface with the `canif-xdm-xlsx` command.
- Accept INPUT and OUTPUT as positional arguments
- Support verbose logging flag

---

## 4. Non-Functional Requirements

**SWR_CANIF_00012**: The parser shall efficiently process XDM files up to 10MB.

**SWR_CANIF_00013**: The reporter shall generate Excel files for projects with up to 1000 PDUs.

**SWR_CANIF_00014**: The system shall handle malformed XML gracefully.

**SWR_CANIF_00015**: The model classes shall use fluent interface pattern.

**SWR_CANIF_00016**: The code shall follow camelCase naming convention.

---

## 5. Appendix

### 5.1 Data Model Class Hierarchy

```
Module (abstract)
  └── CanIf
      ├── CanIfGeneral
      ├── CanIfCtrlCfg
      ├── CanIfTrcvCfg
      ├── CanIfDispatchCfg
      ├── CanIfBufferCfg
      ├── CanIfHrhCfg
      ├── CanIfHthCfg
      ├── CanIfRxPduCfg
      └── CanIfTxPduCfg
```

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial requirements specification |

---

**Document End**