# Software Requirements Specification: CanTp Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | CanTp Module Software Requirements Specification |
| Document ID | SWR_CANTP_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | CanTp (CAN Transport Protocol) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the CanTp module of py-eb-model. The CanTp module is responsible for extracting AUTOSAR CAN Transport Protocol configuration data from EB Tresos XDM files, enabling engineers to analyze transport layer configurations for segmented data transfer over CAN.

### 1.2 Scope

The CanTp module shall:

- Parse EB Tresos XDM files containing AUTOSAR CanTp configuration
- Model connection configurations
- Parse timing parameters (N_Bs, N_Cs, N_Ar, N_Br)
- Support Rx and Tx channel configurations
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture |
| CanTp | CAN Transport Protocol - ISO 15765-4 for CAN |
| N-SDU | Network Service Data Unit |
| N_AI | Network Address Information |
| XDM | XML Data Model - EB Tresos proprietary XML format |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide
- [overview.md](overview.md) - System architecture
- AUTOSAR CanTp Specification (ISO 15765)

---

## 2. General Description

### 2.1 Product Perspective

The CanTp module is part of the three-layer py-eb-model parsing system for transport protocol handling in automotive diagnostics and communication.

### 2.2 Product Functions

1. **General Configuration**: Extract global CanTp settings
2. **Channel Configuration**: Parse Rx and Tx channel configurations
3. **Connection Configuration**: Parse connection settings with addressing
4. **Timing Configuration**: Parse protocol timing parameters
5. **Excel Export**: Generate multi-sheet Excel reports

### 2.3 Constraints

- Python 3.9+ required
- EB Tresos XDM format only

---

## 3. Functional Requirements

**SWR_CANTP_00001 - Parser Layer**: The system shall parse EB Tresos XDM files containing CanTp configuration.
- Validate module name is "CanTp"
- Extract AUTOSAR and software versions

**SWR_CANTP_00002 - Channel Configuration**: The system shall parse and model CanTp channel configurations.
- Extract Rx channel configurations
- Extract Tx channel configurations
- Extract channel timing parameters

**SWR_CANTP_00003 - Connection Configuration**: Parse connection settings.
- Extract connection addressing information
- Extract addressing format settings
- Support functional and physical addressing

**SWR_CANTP_00004 - Timing Configuration**: Parse protocol timers.
- Extract N_Bs, N_Cs, N_Ar, N_Br timing parameters
- Extract STmin and BS parameters

**SWR_CANTP_00005 - Reporter Layer**: Generate Excel output.

**SWR_CANTP_00006 - CLI Interface**: Provide `cantp-xdm-xlsx` command.

---

## 4. Non-Functional Requirements

**SWR_CANTP_00007**: Process XDM files up to 10MB.

**SWR_CANTP_00008**: Handle projects with up to 100 connections.

**SWR_CANTP_00009**: Use fluent interface pattern.

---

## 5. Appendix

### 5.1 Data Model

```
CanTp (Module)
  ├── CanTpGeneral
  ├── CanTpRxChannel
  ├── CanTpTxChannel
  └── CanTpConnection
```

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial specification |

---

**Document End**