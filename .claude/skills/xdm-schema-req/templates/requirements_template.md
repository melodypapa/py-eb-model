# Requirements Document Templates

Use these templates verbatim. Do not add extra sections, columns, or annotations.

---

## Document Header

```markdown
# Software Requirements: <Module Display Name> - Model Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | <Module Display Name> Model Layer Requirements |
| Document ID | SWR_<MODULE_ABBR>_MODELS_00001 |
| Version | 1.0 |
| Date | YYYY-MM-DD |
| Project | py-eb-model |
| Module | <Module Display Name> - Model Layer |

---

## Overview

The <Module Display Name> Model Layer provides Python classes representing AUTOSAR <module description> configuration entities extracted from EB Tresos XDM files.

**Implementation:** `src/eb_model/models/<stack>/<module_lower>_xdm.py`

---
```

---

## Entity Requirement (one per container)

```markdown
### SWR_<MODULE_ABBR>_MODELS_<NNNNN> - <Entity Name> Model

The system shall provide an `<EntityName>` model class for <brief description>.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| fieldName | type | Description with range | AUTOSAR/EB |

**Implementation:** `<module_lower>_xdm.py:<EntityName>`
**Status:** Implemented
**Last Validated:** YYYY-MM-DD

---
```

---

## Choice Container — Grouped Summary (Step 6a)

```markdown
### SWR_<MODULE_ABBR>_MODELS_<NNNNN> - <ChoiceName> Models

The system shall provide choice action model classes.

| Class | Purpose |
|-------|---------|
| ClassName1 | Description |
| ClassName2 | Description |

**Implementation:** `<module_lower>_xdm.py:ClassName1`, `<module_lower>_xdm.py:ClassName2`, etc.
**Status:** Implemented
**Last Validated:** YYYY-MM-DD
```

---

## Choice Container — Per-Variant Requirement (Step 6b)

```markdown
### SWR_<MODULE_ABBR>_MODELS_<NNNNN> - <ClassName1> Model

The system shall provide a `<ClassName1>` model class for <brief description>.

| Field | Type | Description | Origin |
|-------|------|-------------|--------|
| FieldName | type | Description | AUTOSAR/EB |

**Implementation:** `<module_lower>_xdm.py:<ClassName1>`
**Status:** Implemented
**Last Validated:** YYYY-MM-DD
```

---

## Root Module Requirement (Step 7 — always last)

```markdown
### SWR_<MODULE_ABBR>_MODELS_<NNNNN> - <ModuleName> Model (Root)

The system shall provide an `<ModuleName>` root model class containing all <module_name> entities.

**Methods:**
- `get<EntityName>List()` - Get all <entity_name_lower>
- ... (one per top-level entity)

**Implementation:** `<module_lower>_xdm.py:<ModuleName>`
**Status:** Implemented
**Last Validated:** YYYY-MM-DD
```

---

## Traceability Table (Step 8 — always at end)

```markdown
## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_<MODULE_ABBR>_MODELS_00001 | <module_lower>_xdm.py:Entity1 | UTS_<MODULE_ABBR>_MODEL_00001 |
| SWR_<MODULE_ABBR>_MODELS_00002 | <module_lower>_xdm.py:Entity2 | UTS_<MODULE_ABBR>_MODEL_00002 |
| ... | ... | ... |
```

Test case IDs follow the pattern `UTS_<MODULE_ABBR>_MODEL_<NNNNN>`.
