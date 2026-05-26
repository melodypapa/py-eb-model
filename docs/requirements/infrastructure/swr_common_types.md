# Software Requirements: Infrastructure - Common Types

## Document Information

| Field | Value |
|-------|-------|
| Document Title | Common Types Infrastructure Requirements |
| Document ID | SWR_INFRA_COMMON_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | Infrastructure - Common Types |

---

## Overview

The Common Types module provides base classes and utility types used across all modules.

**Implementation:** `src/eb_model/models/core/abstract.py`

---

## Requirements

### SWR_INFRA_COMMON_00001 - EBModel Base Class

The system shall provide an `EBModel` base class for all model classes.

**Methods:**
- `getInstance()` - Get singleton instance
- `getName()` - Get model name
- `getParent()` - Get parent model

**Implementation:** `abstract.py:EBModel`
**Status:** Implemented

---

### SWR_INFRA_COMMON_00002 - EcucRefType

The system shall provide an `EcucRefType` class for AUTOSAR references.

| Field | Type | Description |
|-------|------|-------------|
| value | str | Reference value (ASPath format) |

**Methods:**
- `getValue()` - Get reference value
- `setValue(value)` - Set reference value

**Implementation:** `abstract.py:EcucRefType`
**Status:** Implemented

---

### SWR_INFRA_COMMON_00003 - AbstractEbModelParser

The system shall provide an `AbstractEbModelParser` base class for all parsers.

**Methods:**
- `parse(file_path)` - Parse XDM file
- `read_value(element, name)` - Read variable value
- `read_ref_value(element, name)` - Read reference value
- `find_ctr_tag(element, name)` - Find container tag
- `find_ctr_tag_list(element, name)` - Find container list

**Implementation:** `abstract.py:AbstractEbModelParser`
**Status:** Implemented

---

### SWR_INFRA_COMMON_00004 - Namespace Handling

The parser shall handle XDM namespaces correctly.

- Extract namespace definitions from XDM files
- Store namespace map for XPath queries
- Support `d:` namespace prefix for data elements

**Implementation:** `abstract.py:AbstractEbModelParser`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_INFRA_COMMON_00001 | abstract.py:EBModel | TC_UNIT_COMMON_00001 |
| SWR_INFRA_COMMON_00002 | abstract.py:EcucRefType | TC_UNIT_COMMON_00002 |
| SWR_INFRA_COMMON_00003 | abstract.py:AbstractEbModelParser | TC_UNIT_COMMON_00003 |
| SWR_INFRA_COMMON_00004 | abstract.py:AbstractEbModelParser | TC_UNIT_COMMON_00004 |
