# Software Requirements Specification: CanNm Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | CanNm Module Software Requirements Specification |
| Document ID | SWR_CANNM_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | CanNm (CAN Network Management) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the CanNm module of py-eb-model. The CanNm module is responsible for extracting AUTOSAR CAN Network Management configuration data from EB Tresos XDM files, enabling engineers to analyze network management parameters for coordinated sleep/wake operations in automotive CAN networks.

### 1.2 Scope

The CanNm module shall:

- Parse EB Tresos XDM files containing AUTOSAR CanNm configuration
- Model channel configurations with timing parameters
- Parse network management PDU configurations
- Support partial network and coordination cluster configurations
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture |
| CanNm | CAN Network Management - OSEK/VDX NM for CAN |
| NM | Network Management - coordinated sleep/wake behavior |
| PDU | Protocol Data Unit |
| XDM | XML Data Model - EB Tresos proprietary XML format |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide
- [overview.md](overview.md) - System architecture
- AUTOSAR CanNm Specification

---

## 2. General Description

### 2.1 Product Perspective

The CanNm module is part of the three-layer py-eb-model parsing system:

```
CLI Layer (canif-xdm-xlsx) → Reporter Layer → Model Layer (CanNm, CanNmChannel, etc.) → Parser Layer → XDM Files
```

### 2.2 Product Functions

1. **General Configuration**: Extract global NM settings
2. **Channel Configuration**: Parse NM channel configurations with timing parameters
3. **PDU Configuration**: Parse NM PDU configurations
4. **Partial Network Support**: Parse partial network configurations
5. **Coordination Cluster Support**: Parse NM cluster coordination settings
6. **Excel Export**: Generate multi-sheet Excel reports

### 2.3 Constraints

- Python 3.9+ required
- EB Tresos XDM format only

---

## 3. Functional Requirements

**SWR_CANNM_00001 - Parser Layer**: The system shall parse EB Tresos XDM files containing CanNm configuration.
- Validate module name is "CanNm"
- Extract AUTOSAR and software versions
- Inherit from AbstractEbModelParser

**SWR_CANNM_00002 - Channel Configuration**: The system shall parse and model CanNm channel configurations.
- Extract channel timing parameters (timeout, wait, sleep times)
- Extract NM message cycle times
- Extract immediate message settings
- Extract NM coordinator and node settings
- Support multiple channel configurations

**SWR_CANNM_00003 - PDU Configuration**: The system shall parse and model NM PDU configurations.
- Extract PDU ID and position
- Extract user data configuration
- Extract transmit and receive capabilities

**SWR_CANNM_00004 - Partial Network Configuration**: The system shall parse partial network settings.
- Extract partial network cluster configurations
- Extract coordinated sleep/wake parameters

**SWR_CANNM_00005 - Reporter Layer**: Generate Excel output with NM configurations.

**SWR_CANNM_00006 - CLI Interface**: Provide `cannm-xdm-xlsx` command.

---

## 4. Non-Functional Requirements

**SWR_CANNM_00007**: Process XDM files up to 10MB efficiently.

**SWR_CANNM_00008**: Handle projects with up to 50 NM channels.

**SWR_CANNM_00009**: Use fluent interface pattern.

**SWR_CANNM_00010**: Follow camelCase naming convention.

---

## 5. Appendix

### 5.1 Data Model

```
CanNm (Module)
  ├── CanNmGeneral
  ├── CanNmChannelCfg
  │   ├── CanNmRxPdu
  │   └── CanNmTxPdu
  └── CanNmCluster
```

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial specification |

---

**Document End**