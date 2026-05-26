# Software Requirements: RTE Module - Model Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | RTE Module Model Layer Requirements |
| Document ID | SWR_RTE_MODELS_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | RTE (Runtime Environment) - Model Layer |

---

## Overview

The RTE Model Layer provides Python classes representing AUTOSAR RTE configuration entities.

**Implementation:** `src/eb_model/models/core/rte_xdm.py`

---

## Requirements

### SWR_RTE_MODELS_00001 - Rte Model (Root)

The system shall provide an `Rte` root model class containing all RTE entities.

**Methods:**
- `getRteBswModuleInstanceList()` - Get all BSW module instances
- `getRteSwComponentInstanceList()` - Get all SW component instances
- `addRteBswModuleInstance(instance)` - Add BSW module instance
- `addRteSwComponentInstance(instance)` - Add SW component instance

**Implementation:** `rte_xdm.py:Rte`
**Status:** Implemented

---

### SWR_RTE_MODELS_00002 - RteBswModuleInstance Model

The system shall provide an `RteBswModuleInstance` model class for BSW module instances.

| Field | Type | Description |
|-------|------|-------------|
| RteBswImplementationRef | EcucRefType | BSW implementation reference |
| RteBswEventToTaskMapping | List | Event-to-task mappings |

**Methods:**
- `getMappedEvents()` - Get event mappings grouped by task

**Implementation:** `rte_xdm.py:RteBswModuleInstance`
**Status:** Implemented

---

### SWR_RTE_MODELS_00003 - RteSwComponentInstance Model

The system shall provide an `RteSwComponentInstance` model class for SW component instances.

| Field | Type | Description |
|-------|------|-------------|
| RteSwComponentInstanceRef | EcucRefType | SW component instance reference |
| RteEventToTaskMapping | List | Event-to-task mappings |

**Methods:**
- `getMappedEvents()` - Get event mappings grouped by task

**Implementation:** `rte_xdm.py:RteSwComponentInstance`
**Status:** Implemented

---

### SWR_RTE_MODELS_00004 - RteEventToTaskMappingV3 Model

The system shall provide an `RteEventToTaskMappingV3` model class for AUTOSAR 3.x event mappings.

| Field | Type | Description |
|-------|------|-------------|
| RteEventRef | EcucRefType | Single event reference |
| RteMappedToTaskRef | EcucRefType | Task reference |
| RteActivationOffset | float | Activation offset |
| RtePositionInTask | int | Position in task |

**Methods:**
- `getRteEventRef()` - Returns single event reference
- `getRteEventRefs()` - Returns list with single reference

**Implementation:** `rte_xdm.py:RteEventToTaskMappingV3`
**Status:** Implemented

---

### SWR_RTE_MODELS_00005 - RteEventToTaskMappingV4 Model

The system shall provide an `RteEventToTaskMappingV4` model class for AUTOSAR 4.x event mappings.

| Field | Type | Description |
|-------|------|-------------|
| RteEventRefs | List[EcucRefType] | Multiple event references |
| RteMappedToTaskRef | EcucRefType | Task reference |
| RteActivationOffset | float | Activation offset |
| RtePositionInTask | int | Position in task |

**Methods:**
- `getRteEventRef()` - Returns single reference or raises ValueError
- `getRteEventRefs()` - Returns list of all event references

**Implementation:** `rte_xdm.py:RteEventToTaskMappingV4`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_RTE_MODELS_00001 | rte_xdm.py:Rte | UTS_RTE_MODEL_00001 |
| SWR_RTE_MODELS_00002 | rte_xdm.py:RteBswModuleInstance | UTS_RTE_MODEL_00002 |
| SWR_RTE_MODELS_00003 | rte_xdm.py:RteSwComponentInstance | UTS_RTE_MODEL_00003 |
| SWR_RTE_MODELS_00004 | rte_xdm.py:RteEventToTaskMappingV3 | UTS_RTE_MODEL_00004 |
| SWR_RTE_MODELS_00005 | rte_xdm.py:RteEventToTaskMappingV4 | UTS_RTE_MODEL_00005 |
