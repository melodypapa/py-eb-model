# Software Requirements Specification: J1939Tp Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | J1939Tp Module Software Requirements Specification |
| Document ID | SWR_J1939TP_00001 |
| Version | 1.0 |
| Date | 2026-03-29 |
| Project | py-eb-model |
| Module | J1939Tp (J1939 Transport Protocol) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the J1939Tp module of py-eb-model.

### 1.2 Scope

The J1939Tp module shall:

- Parse EB Tresos XDM files containing AUTOSAR J1939Tp configuration
- Model J1939 transport protocol settings
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture |
| J1939Tp | J1939 Transport Protocol for SAE J1939 protocol |
| XDM | XML Data Model - EB Tresos proprietary XML format |
| SAE J1939 | Society of Automotive Engineers J1939 standard for vehicle networks |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide
- [overview.md](overview.md) - System architecture

---

## 2. General Description

### 2.1 Product Functions

1. **General Configuration**: Extract global J1939Tp settings
2. **Excel Export**: Generate Excel reports

### 2.2 Constraints

- Python 3.9+ required
- EB Tresos XDM format only

---

## 3. Functional Requirements

**SWR_J1939TP_00001 - Parser Layer**: Parse J1939Tp XDM files.

**SWR_J1939TP_00002 - General Configuration**: Parse J1939Tp general settings.

**SWR_J1939TP_00003 - Reporter Layer**: Generate Excel output.

**SWR_J1939TP_00004 - CLI Interface**: Provide `j1939tp-xdm-xlsx` command.

---

## 4. Non-Functional Requirements

**SWR_J1939TP_00005**: Process XDM files up to 10MB.

**SWR_J1939TP_00006**: Use fluent interface pattern.

---

## 5. Appendix

### 5.1 Data Model

```
J1939Tp (Module)
  └── J1939TpGeneral
```

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-29 | Claude Code | Initial specification |

---

**Document End**