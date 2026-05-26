# Software Requirements: EcuC Module - Model Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | EcuC Module Model Layer Requirements |
| Document ID | SWR_ECUC_MODELS_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | EcuC (ECU Configuration) - Model Layer |

---

## Overview

The EcuC Model Layer provides Python classes representing AUTOSAR ECU configuration entities.

**Implementation:** `src/eb_model/models/core/ecuc_xdm.py`

---

## Requirements

### SWR_ECUC_MODELS_00001 - EcuC Model (Root)

The system shall provide an `EcuC` root model class containing all ECU configuration entities.

**Methods:**
- `getEcucPartitionCollection()` - Get partition collection
- `setEcucPartitionCollection(collection)` - Set partition collection

**Implementation:** `ecuc_xdm.py:EcuC`
**Status:** Implemented

---

### SWR_ECUC_MODELS_00002 - EcucPartitionCollection Model

The system shall provide an `EcucPartitionCollection` model class for partition collection.

**Methods:**
- `getEcucPartitionList()` - Get all partitions
- `addEcucPartition(partition)` - Add partition

**Implementation:** `ecuc_xdm.py:EcucPartitionCollection`
**Status:** Implemented

---

### SWR_ECUC_MODELS_00003 - EcucPartition Model

The system shall provide an `EcucPartition` model class for ECU partition definitions.

| Field | Type | Description |
|-------|------|-------------|
| EcucPartitionDefaultBswPartition | bool | Default BSW partition flag |
| EcucPartitionRestart | str | Restart capability |
| EcucPartitionRef | EcucRefType | Partition reference |

**Methods:**
- `getEcucSwComponentInstanceList()` - Get SW component instances
- `addEcucSwComponentInstance(instance)` - Add SW component instance

**Implementation:** `ecuc_xdm.py:EcucPartition`
**Status:** Implemented

---

### SWR_ECUC_MODELS_00004 - EcucSwComponentInstance Model

The system shall provide an `EcucSwComponentInstance` model class for SW component assignments.

| Field | Type | Description |
|-------|------|-------------|
| EcucSwComponentInstanceTargetRef | EcucRefType | Target component reference |

**Implementation:** `ecuc_xdm.py:EcucSwComponentInstance`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_ECUC_MODELS_00001 | ecuc_xdm.py:EcuC | UTS_ECUC_MODEL_00001 |
| SWR_ECUC_MODELS_00002 | ecuc_xdm.py:EcucPartitionCollection | UTS_ECUC_MODEL_00002 |
| SWR_ECUC_MODELS_00003 | ecuc_xdm.py:EcucPartition | UTS_ECUC_MODEL_00003 |
| SWR_ECUC_MODELS_00004 | ecuc_xdm.py:EcucSwComponentInstance | UTS_ECUC_MODEL_00004 |
