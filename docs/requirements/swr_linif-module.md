# Software Requirements Specification: LinIf Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | LinIf Module Software Requirements Specification |
| Document ID | SWR_LINIF_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | LinIf (LIN Interface) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the LinIf module of py-eb-model. The LinIf module is responsible for extracting AUTOSAR LIN Interface configuration data from EB Tresos XDM files, enabling engineers to analyze LIN communication configurations for local interconnect network in automotive systems.

### 1.2 Scope

The LinIf module shall:

- Parse EB Tresos XDM files containing AUTOSAR LinIf configuration
- Model LIN controller and channel configurations
- Parse schedule table configurations
- Support frame configurations for Rx and Tx
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture |
| LinIf | LIN Interface - abstraction layer for LIN communication |
| LIN | Local Interconnect Network - automotive serial protocol |
| Schedule Table | Configuration defining frame transmission order |
| XDM | XML Data Model - EB Tresos proprietary XML format |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide
- [overview.md](overview.md) - System architecture
- AUTOSAR LinIf Specification (LIN 2.x)

---

## 2. General Description

### 2.1 Product Perspective

The LinIf module is part of the three-layer py-eb-model parsing system for LIN communication in automotive body electronics.

### 2.2 Product Functions

1. **General Configuration**: Extract global LinIf settings
2. **Channel Configuration**: Parse LIN channel configurations
3. **Schedule Table Configuration**: Parse schedule definitions
4. **Frame Configuration**: Parse LIN frame configurations
5. **Excel Export**: Generate multi-sheet Excel reports

### 2.3 Constraints

- Python 3.9+ required
- EB Tresos XDM format only

---

## 3. Functional Requirements

**SWR_LINIF_00001 - Parser Layer**: The system shall parse EB Tresos XDM files containing LinIf configuration.
- Validate module name is "LinIf"
- Extract AUTOSAR and software versions

**SWR_LINIF_00002 - Channel Configuration**: Parse LIN channel configurations.
- Extract channel ID and controller references
- Extract baud rate and protocol settings
- Support multiple channel configurations

**SWR_LINIF_00003 - Schedule Table Configuration**: Parse schedule tables.
- Extract schedule definitions and frame entries
- Extract timing parameters for schedule slots
- Support multiple schedule configurations

**SWR_LINIF_00004 - Frame Configuration**: Parse LIN frame configurations.
- Extract frame ID, length, and checksum type
- Extract signal mapping references
- Support unconditional and event-triggered frames

**SWR_LINIF_00005 - Reporter Layer**: Generate Excel output.

**SWR_LINIF_00006 - CLI Interface**: Provide `linif-xdm-xlsx` command.

---

## 4. Non-Functional Requirements

**SWR_LINIF_00007**: Process XDM files up to 10MB.

**SWR_LINIF_00008**: Handle projects with up to 100 frames.

**SWR_LINIF_00009**: Use fluent interface pattern.

---

## 5. Appendix

### 5.1 Data Model

```
LinIf (Module)
  ├── LinIfGeneral
  ├── LinIfChannel
  ├── LinIfSchedule
  └── LinIfFrame
```

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial specification |

---

**Document End**