# Software Requirements Specification: Tm Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | Tm Module Software Requirements Specification |
| Document ID | SWR_TM_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | Tm (Timing) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the Tm module of py-eb-model. The Tm module is responsible for extracting AUTOSAR Timing configuration data from EB Tresos XDM files, enabling engineers to analyze timing constraints and schedules.

### 1.2 Scope

The Tm module shall:

- Parse EB Tresos XDM files containing AUTOSAR Tm configuration
- Model timing constraint configurations
- Parse timing protection settings
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture |
| Tm | Timing - timing constraints and protection |
| Timing Constraint | Execution time limits for tasks/ISRs |
| XDM | XML Data Model - EB Tresos proprietary XML format |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide
- [overview.md](overview.md) - System architecture
- AUTOSAR Tm Specification

---

## 2. General Description

### 2.1 Product Functions

1. **General Configuration**: Extract global Tm settings
2. **Timing Constraint Configuration**: Parse timing constraints
3. **Excel Export**: Generate Excel reports

### 2.2 Constraints

- Python 3.9+ required
- EB Tresos XDM format only

---

## 3. Functional Requirements

**SWR_TM_00001 - Parser Layer**: Parse Tm XDM files.
- Validate module name is "Tm"
- Extract AUTOSAR and software versions

**SWR_TM_00002 - Timing Constraint Configuration**: Parse timing settings.
- Extract timing constraint definitions
- Extract execution budget settings
- Extract inter-arrival timing parameters

**SWR_TM_00003 - Reporter Layer**: Generate Excel output.

**SWR_TM_00004 - CLI Interface**: Provide `tm-xdm-xlsx` command.

---

## 4. Non-Functional Requirements

**SWR_TM_00005**: Process XDM files up to 10MB.

**SWR_TM_00006**: Use fluent interface pattern.

---

## 5. Appendix

### 5.1 Data Model

```
Tm (Module)
  └── TmGeneral
```

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial specification |

---

**Document End**