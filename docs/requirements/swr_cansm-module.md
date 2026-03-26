# Software Requirements Specification: CanSm Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | CanSm Module Software Requirements Specification |
| Document ID | SWR_CANSM_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | CanSm (CAN State Manager) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the CanSm module of py-eb-model. The CanSm module is responsible for extracting AUTOSAR CAN State Manager configuration data from EB Tresos XDM files, enabling engineers to analyze CAN controller state machine configurations for startup, shutdown, and sleep transitions.

### 1.2 Scope

The CanSm module shall:

- Parse EB Tresos XDM files containing AUTOSAR CanSm configuration
- Model CAN network configurations
- Parse state machine transition parameters
- Support controller mode request configurations
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture |
| CanSm | CAN State Manager - manages CAN controller states |
| State Machine | State transition logic for controller modes |
| XDM | XML Data Model - EB Tresos proprietary XML format |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide
- [overview.md](overview.md) - System architecture
- AUTOSAR CanSm Specification

---

## 2. General Description

### 2.1 Product Perspective

The CanSm module is part of the three-layer py-eb-model parsing system for managing CAN controller state transitions in automotive networks.

### 2.2 Product Functions

1. **General Configuration**: Extract global CanSm settings
2. **Network Configuration**: Parse CAN network configurations
3. **State Machine Configuration**: Parse state transition parameters
4. **Mode Request Configuration**: Parse controller mode request settings
5. **Excel Export**: Generate multi-sheet Excel reports

### 2.3 Constraints

- Python 3.9+ required
- EB Tresos XDM format only

---

## 3. Functional Requirements

**SWR_CANSM_00001 - Parser Layer**: The system shall parse EB Tresos XDM files containing CanSm configuration.
- Validate module name is "CanSm"
- Extract AUTOSAR and software versions

**SWR_CANSM_00002 - Network Configuration**: The system shall parse and model CanSm network configurations.
- Extract network ID and controller references
- Extract state transition timing parameters
- Support multiple network configurations

**SWR_CANSM_00003 - State Machine Parameters**: Extract state transition settings.
- Extract wakeup source validation settings
- Extract bus-off recovery parameters
- Extract transceiver control settings

**SWR_CANSM_00004 - Reporter Layer**: Generate Excel output.

**SWR_CANSM_00005 - CLI Interface**: Provide `cansm-xdm-xlsx` command.

---

## 4. Non-Functional Requirements

**SWR_CANSM_00006**: Process XDM files up to 10MB.

**SWR_CANSM_00007**: Handle projects with up to 20 networks.

**SWR_CANSM_00008**: Use fluent interface pattern.

---

## 5. Appendix

### 5.1 Data Model

```
CanSm (Module)
  ├── CanSmGeneral
  └── CanSmNetwork
```

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial specification |

---

**Document End**