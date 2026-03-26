# Software Requirements Specification: LinSm Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | LinSm Module Software Requirements Specification |
| Document ID | SWR_LINSM_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | LinSm (LIN State Manager) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the LinSm module of py-eb-model. The LinSm module is responsible for extracting AUTOSAR LIN State Manager configuration data from EB Tresos XDM files, enabling engineers to analyze LIN network state machine configurations.

### 1.2 Scope

The LinSm module shall:

- Parse EB Tresos XDM files containing AUTOSAR LinSm configuration
- Model LIN network configurations
- Parse state machine transition parameters
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture |
| LinSm | LIN State Manager - manages LIN network states |
| LIN | Local Interconnect Network |
| XDM | XML Data Model - EB Tresos proprietary XML format |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide
- [overview.md](overview.md) - System architecture
- AUTOSAR LinSm Specification

---

## 2. General Description

### 2.1 Product Functions

1. **General Configuration**: Extract global LinSm settings
2. **Network Configuration**: Parse LIN network configurations
3. **State Machine Configuration**: Parse state transition parameters
4. **Excel Export**: Generate Excel reports

### 2.2 Constraints

- Python 3.9+ required
- EB Tresos XDM format only

---

## 3. Functional Requirements

**SWR_LINSM_00001 - Parser Layer**: Parse LinIf XDM files.
- Validate module name is "LinSm"
- Extract AUTOSAR and software versions

**SWR_LINSM_00002 - Network Configuration**: Parse LIN network configurations.
- Extract network ID and channel references
- Extract state transition parameters

**SWR_LINSM_00003 - Reporter Layer**: Generate Excel output.

**SWR_LINSM_00004 - CLI Interface**: Provide `linsm-xdm-xlsx` command.

---

## 4. Non-Functional Requirements

**SWR_LINSM_00005**: Process XDM files up to 10MB.

**SWR_LINSM_00006**: Use fluent interface pattern.

---

## 5. Appendix

### 5.1 Data Model

```
LinSm (Module)
  ├── LinSmGeneral
  └── LinSmNetwork
```

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial specification |

---

**Document End**