# Software Requirements Specification: EcuM Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | EcuM Module Software Requirements Specification |
| Document ID | SWR_ECUM_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | EcuM (ECU State Manager) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the EcuM module of py-eb-model. The EcuM module is responsible for extracting AUTOSAR ECU State Manager configuration data from EB Tresos XDM files, enabling engineers to analyze ECU startup, shutdown, and sleep state configurations.

### 1.2 Scope

The EcuM module shall:

- Parse EB Tresos XDM files containing AUTOSAR EcuM configuration
- Model ECU state machine configurations
- Parse wakeup source configurations
- Parse startup and shutdown configurations
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture |
| EcuM | ECU State Manager - manages ECU lifecycle states |
| Wakeup Source | Event that triggers ECU wakeup |
| XDM | XML Data Model - EB Tresos proprietary XML format |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide
- [overview.md](overview.md) - System architecture
- AUTOSAR EcuM Specification

---

## 2. General Description

### 2.1 Product Functions

1. **General Configuration**: Extract global EcuM settings
2. **State Configuration**: Parse ECU state machine configurations
3. **Wakeup Configuration**: Parse wakeup source configurations
4. **Startup/Shutdown Configuration**: Parse lifecycle configurations
5. **Excel Export**: Generate Excel reports

### 2.2 Constraints

- Python 3.9+ required
- EB Tresos XDM format only

---

## 3. Functional Requirements

**SWR_ECUM_00001 - Parser Layer**: Parse EcuM XDM files.
- Validate module name is "EcuM"
- Extract AUTOSAR and software versions

**SWR_ECUM_00002 - State Configuration**: Parse ECU state configurations.
- Extract state machine definitions
- Extract state transition conditions

**SWR_ECUM_00003 - Wakeup Configuration**: Parse wakeup source settings.
- Extract wakeup source IDs
- Extract wakeup validation settings
- Support multiple wakeup sources

**SWR_ECUM_00004 - Startup/Shutdown Configuration**: Parse lifecycle settings.
- Extract startup option configurations
- Extract shutdown target configurations
- Extract sleep mode configurations

**SWR_ECUM_00005 - Reporter Layer**: Generate Excel output.

**SWR_ECUM_00006 - CLI Interface**: Provide `ecum-xdm-xlsx` command.

---

## 4. Non-Functional Requirements

**SWR_ECUM_00007**: Process XDM files up to 10MB.

**SWR_ECUM_00008**: Handle projects with up to 20 wakeup sources.

**SWR_ECUM_00009**: Use fluent interface pattern.

---

## 5. Appendix

### 5.1 Data Model

```
EcuM (Module)
  ├── EcuMGeneral
  ├── EcuMState
  ├── EcuMWakeupSource
  └── EcuMSleepMode
```

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial specification |

---

**Document End**