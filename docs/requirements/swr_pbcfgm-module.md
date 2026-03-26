# Software Requirements Specification: PbcfgM Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | PbcfgM Module Software Requirements Specification |
| Document ID | SWR_PBCFGM_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |
| Module | PbcfgM (Post-Build Configuration Manager) |

## Table of Contents

1. [Introduction](#1-introduction)
2. [General Description](#2-general-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Appendix](#5-appendix)

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the PbcfgM module of py-eb-model. The PbcfgM module is responsible for extracting AUTOSAR Post-Build Configuration Manager configuration data from EB Tresos XDM files, enabling engineers to analyze post-build configuration settings.

### 1.2 Scope

The PbcfgM module shall:

- Parse EB Tresos XDM files containing AUTOSAR PbcfgM configuration
- Model post-build configuration block settings
- Parse configuration selection mechanisms
- Export configuration data to Excel (.xlsx) format
- Provide command-line interface for extraction operations

### 1.3 Definitions

| Term | Definition |
|------|------------|
| AUTOSAR | AUTomotive Open System ARchitecture |
| PbcfgM | Post-Build Configuration Manager - manages variant configurations |
| Post-Build | Configuration after compilation/deployment |
| XDM | XML Data Model - EB Tresos proprietary XML format |

### 1.4 References

- [CLAUDE.md](../../CLAUDE.md) - Development guide
- [overview.md](overview.md) - System architecture
- AUTOSAR PbcfgM Specification

---

## 2. General Description

### 2.1 Product Functions

1. **General Configuration**: Extract global PbcfgM settings
2. **Block Configuration**: Parse configuration block definitions
3. **Excel Export**: Generate Excel reports

### 2.2 Constraints

- Python 3.9+ required
- EB Tresos XDM format only

---

## 3. Functional Requirements

**SWR_PBCFGM_00001 - Parser Layer**: Parse PbcfgM XDM files.
- Validate module name is "PbcfgM"
- Extract AUTOSAR and software versions

**SWR_PBCFGM_00002 - Block Configuration**: Parse configuration blocks.
- Extract configuration block definitions
- Extract block selection parameters
- Support multiple configuration blocks

**SWR_PBCFGM_00003 - Reporter Layer**: Generate Excel output.

**SWR_PBCFGM_00004 - CLI Interface**: Provide `pbcfgm-xdm-xlsx` command.

---

## 4. Non-Functional Requirements

**SWR_PBCFGM_00005**: Process XDM files up to 10MB.

**SWR_PBCFGM_00006**: Use fluent interface pattern.

---

## 5. Appendix

### 5.1 Data Model

```
PbcfgM (Module)
  ├── PbcfgMGeneral
  └── PbcfgMBlock
```

### 5.2 Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial specification |

---

**Document End**