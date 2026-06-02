# Software Requirements: Infrastructure - Parser Methods

## Document Information

| Field | Value |
|-------|-------|
| Document Title | Parser Methods Infrastructure Requirements |
| Document ID | SWR_INFRA_PARSER_00001 |
| Version | 1.0 |
| Date | 2026-06-02 |
| Project | py-eb-model |
| Module | Infrastructure - Parser Methods |

---

## Overview

The Parser Methods module provides XML parsing utilities for reading values, references, and containers from XDM files.

**Implementation:** `src/eb_model/parser/core/eb_parser.py`

---

## Requirements

### SWR_INFRA_PARSER_00001 - Mandatory Value Reading

The parser shall provide a method to read mandatory values from XML elements.

**Method:** `read_value(parent, name) -> str`

| Parameter | Type | Description |
|-----------|------|-------------|
| parent | ET.Element | Parent XML element |
| name | str | Variable name to read |
| **Returns** | str | Converted value |
| **Raises** | KeyError | If variable does not exist |

**Behavior:**
- Search for `<d:var name="{name}">` element
- Raise `KeyError` if not found
- Convert value using `_convert_value()` (handles BOOLEAN, INTEGER, FLOAT, STRING)

**Use Case:** Fields with multiplicity [1..1] (mandatory)

**Implementation:** `eb_parser.py:read_value`
**Status:** Implemented

---

### SWR_INFRA_PARSER_00002 - Optional Value Reading

The parser shall provide a method to read optional values with default fallback and ENABLE attribute support.

**Method:** `read_optional_value(parent, name, default_value=None) -> str`

| Parameter | Type | Description |
|-----------|------|-------------|
| parent | ET.Element | Parent XML element |
| name | str | Variable name to read |
| default_value | Any | Default value if not found (default: None) |
| **Returns** | Any | Converted value or default_value |

**Behavior:**
- Search for `<d:var name="{name}">` element
- Return `default_value` if not found
- Return `default_value` if no `value` attribute exists
- Check `ENABLE` attribute; return `default_value` if `ENABLE="false"`
- Convert value using `_convert_value()`

**Use Case:** Fields with multiplicity [0..1] (optional)

**Implementation:** `eb_parser.py:read_optional_value`
**Status:** Implemented

---

### SWR_INFRA_PARSER_00003 - Mandatory Choice Value Reading

The parser shall provide a method to read mandatory choice values from XML elements.

**Method:** `read_choice_value(parent, name) -> str`

| Parameter | Type | Description |
|-----------|------|-------------|
| parent | ET.Element | Parent XML element |
| name | str | Choice name to read |
| **Returns** | str | Choice value |
| **Raises** | KeyError | If choice does not exist or has no value |

**Behavior:**
- Search for `<d:chc name="{name}">` element
- Return the `value` attribute
- Raise exception if not found or no value attribute

**Use Case:** Choice fields with multiplicity [1..1] (mandatory)

**Implementation:** `eb_parser.py:read_choice_value`
**Status:** Implemented

---

### SWR_INFRA_PARSER_00004 - Optional Choice Value Reading

The parser shall provide a method to read optional choice values with default fallback.

**Method:** `read_optional_choice_value(parent, name, default_value=None) -> str`

| Parameter | Type | Description |
|-----------|------|-------------|
| parent | ET.Element | Parent XML element |
| name | str | Choice name to read |
| default_value | Any | Default value if not found (default: None) |
| **Returns** | Any | Choice value or default_value |

**Behavior:**
- Search for `<d:chc name="{name}">` element
- Return `default_value` if not found
- Return `value` attribute or `default_value` if not present

**Use Case:** Choice fields with multiplicity [0..1] (optional)

**Implementation:** `eb_parser.py:read_optional_choice_value`
**Status:** Implemented

---

### SWR_INFRA_PARSER_00005 - Mandatory Reference Reading

The parser shall provide a method to read mandatory reference values in ASPath format.

**Method:** `read_ref_value(parent, name) -> EcucRefType`

| Parameter | Type | Description |
|-----------|------|-------------|
| parent | ET.Element | Parent XML element |
| name | str | Reference name to read |
| **Returns** | EcucRefType | Reference object with short name |
| **Raises** | KeyError | If reference does not exist |

**Behavior:**
- Search for `<d:ref name="{name}">` element
- Raise `KeyError` if not found
- Parse ASPath format and extract short name
- Return `EcucRefType` object

**Use Case:** Reference fields with multiplicity [1..1] (mandatory)

**Implementation:** `eb_parser.py:read_ref_value`
**Status:** Implemented

---

### SWR_INFRA_PARSER_00006 - Optional Reference Reading

The parser shall provide a method to read optional reference values with ENABLE attribute support.

**Method:** `read_optional_ref_value(parent, name) -> EcucRefType`

| Parameter | Type | Description |
|-----------|------|-------------|
| parent | ET.Element | Parent XML element |
| name | str | Reference name to read |
| **Returns** | EcucRefType \| None | Reference object or None |

**Behavior:**
- Search for `<d:ref name="{name}">` element
- Return `None` if not found
- Return `None` if no `value` attribute exists
- Check `ENABLE` attribute; return `None` if `ENABLE="false"`
- Parse ASPath format and return `EcucRefType` object

**Use Case:** Reference fields with multiplicity [0..1] (optional)

**Implementation:** `eb_parser.py:read_optional_ref_value`
**Status:** Implemented

---

### SWR_INFRA_PARSER_00007 - Reference List Reading

The parser shall provide a method to read a list of reference values.

**Method:** `read_ref_value_list(parent, name) -> List[EcucRefType]`

| Parameter | Type | Description |
|-----------|------|-------------|
| parent | ET.Element | Parent XML element |
| name | str | Reference list name |
| **Returns** | List[EcucRefType] | List of reference objects |

**Behavior:**
- Search for `<d:lst name="{name}">` element
- Iterate over all `<d:ref>` children
- Skip references without `value` attribute (log warning)
- Parse ASPath format and build `EcucRefType` list

**Use Case:** Reference fields with multiplicity [0..*] or [1..*] (multiple)

**Implementation:** `eb_parser.py:read_ref_value_list`
**Status:** Implemented

---

### SWR_INFRA_PARSER_00008 - Container Tag Finding (Single)

The parser shall provide a method to find a single container tag with ENABLE attribute support.

**Method:** `find_ctr_tag(parent, name) -> ET.Element`

| Parameter | Type | Description |
|-----------|------|-------------|
| parent | ET.Element | Parent XML element |
| name | str | Container name |
| **Returns** | ET.Element \| None | Container element or None |

**Behavior:**
- Search for `<d:ctr name="{name}">` element
- Return `None` if not found
- Check `ENABLE` attribute; return `None` if `ENABLE="false"`
- Return the container element

**Use Case:** Container fields with multiplicity [0..1] (optional)

**Implementation:** `eb_parser.py:find_ctr_tag`
**Status:** Implemented

---

### SWR_INFRA_PARSER_00009 - Container Tag Finding (Multiple)

The parser shall provide a method to find all container tags with a given name.

**Method:** `find_ctr_tag_list(parent, name) -> List[ET.Element]`

| Parameter | Type | Description |
|-----------|------|-------------|
| parent | ET.Element | Parent XML element |
| name | str | Container list name |
| **Returns** | List[ET.Element] | List of container elements |

**Behavior:**
- Search for `<d:lst name="{name}">` element
- Return all `<d:ctr>` children as a list

**Use Case:** Container fields with multiplicity [0..*] or [1..*] (multiple)

**Implementation:** `eb_parser.py:find_ctr_tag_list`
**Status:** Implemented

---

## Method Selection Guide

| Multiplicity | ENABLE Attribute | Method |
|--------------|------------------|--------|
| [1..1] | N/A | `read_value` |
| [0..1] | May exist | `read_optional_value` |
| [1..1] (Choice) | N/A | `read_choice_value` |
| [0..1] (Choice) | May exist | `read_optional_choice_value` |
| [1..1] (Reference) | N/A | `read_ref_value` |
| [0..1] (Reference) | May exist | `read_optional_ref_value` |
| [0..*] or [1..*] (Reference) | N/A | `read_ref_value_list` |
| [0..1] (Container) | May exist | `find_ctr_tag` |
| [0..*] or [1..*] (Container) | N/A | `find_ctr_tag_list` |

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_INFRA_PARSER_00001 | eb_parser.py:read_value | TC_UNIT_PARSER_00001 |
| SWR_INFRA_PARSER_00002 | eb_parser.py:read_optional_value | TC_UNIT_PARSER_00002 |
| SWR_INFRA_PARSER_00003 | eb_parser.py:read_choice_value | TC_UNIT_PARSER_00003 |
| SWR_INFRA_PARSER_00004 | eb_parser.py:read_optional_choice_value | TC_UNIT_PARSER_00004 |
| SWR_INFRA_PARSER_00005 | eb_parser.py:read_ref_value | TC_UNIT_PARSER_00005 |
| SWR_INFRA_PARSER_00006 | eb_parser.py:read_optional_ref_value | TC_UNIT_PARSER_00006 |
| SWR_INFRA_PARSER_00007 | eb_parser.py:read_ref_value_list | TC_UNIT_PARSER_00007 |
| SWR_INFRA_PARSER_00008 | eb_parser.py:find_ctr_tag | TC_UNIT_PARSER_00008 |
| SWR_INFRA_PARSER_00009 | eb_parser.py:find_ctr_tag_list | TC_UNIT_PARSER_00009 |
