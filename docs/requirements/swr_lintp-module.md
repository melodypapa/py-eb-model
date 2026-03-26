# Software Requirements Specification: LinTp Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | LinTp Module Software Requirements Specification |
| Document ID | SWR_LINTP_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | LinTp (LIN Transport Protocol) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the LinTp module of py-eb-model. The LinTp module is responsible for extracting AUTOSAR LIN Transport Protocol configuration data from EB Tresos XDM files, enabling engineers to analyze transport layer configurations for segmented data transfer over LIN.

### 1.2 Scope

The LinTp module shall:

- Parse EB Tresos XDM files containing AUTOSAR LinTp configuration
- Model connection configurations
- Parse timing parameters
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture |
| LinTp | LIN Transport Protocol - ISO 15765-4 for LIN |
| XDM | XML Data Model - EB Tresos proprietary XML format |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide
- [overview.md](overview.md) - System architecture
- AUTOSAR LinTp Specification

---

## 2. General Description

### 2.1 Product Functions

1. **General Configuration**: Extract global LinTp settings
2. **Channel Configuration**: Parse Rx and Tx channel configurations
3. **Connection Configuration**: Parse connection settings
4. **Excel Export**: Generate Excel reports

### 2.2 Constraints

- Python 3.9+ required
- EB Tresos XDM format only

---

## 3. Functional Requirements

**SWR_LINTP_00001 - Parser Layer**: Parse LinTp XDM files.
- Validate module name is "LinTp"
- Extract AUTOSAR and software versions

**SWR_LINTP_00002 - Channel Configuration**: Parse LinTp channel configurations.
- Extract Rx and Tx channel settings
- Extract timing parameters

**SWR_LINTP_00003 - Connection Configuration**: Parse connection settings.
- Extract connection addressing
- Extract addressing format settings

**SWR_LINTP_00004 - Reporter Layer**: Generate Excel output.

**SWR_LINTP_00005 - CLI Interface**: Provide `lintp-xdm-xlsx` command.

---

## 4. Non-Functional Requirements

**SWR_LINTP_00006**: Process XDM files up to 10MB.

**SWR_LINTP_00007**: Use fluent interface pattern.

---

## 5. Appendix

### 5.1 Data Model

```
LinTp (Module)
  ├── LinTpGeneral
  ├── LinTpRxChannel
  ├── LinTpTxChannel
  └── LinTpConnection
```

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial specification |

---

**Document End**