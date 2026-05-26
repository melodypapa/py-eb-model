# Software Requirements: J1939 Stack - Model Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | J1939 Stack Model Layer Requirements |
| Document ID | SWR_J1939_MODELS_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | J1939 Stack - Model Layer |

---

## Overview

The J1939 Stack Model Layer provides Python classes for J1939 communication modules.

**Implementation:** `src/eb_model/models/j1939_stack/`

---

## Requirements

### SWR_J1939DCM_MODELS_00001 - J1939Dcm Model

The system shall provide a `J1939Dcm` root model class for J1939 Diagnostic Communication Manager.

**Implementation:** `j1939_stack/j1939dcm_xdm.py:J1939Dcm`
**Status:** Implemented

---

### SWR_J1939NM_MODELS_00001 - J1939Nm Model

The system shall provide a `J1939Nm` root model class for J1939 Network Management.

**Implementation:** `j1939_stack/j1939nm_xdm.py:J1939Nm`
**Status:** Implemented

---

### SWR_J1939RM_MODELS_00001 - J1939Rm Model

The system shall provide a `J1939Rm` root model class for J1939 Resource Manager.

**Implementation:** `j1939_stack/j1939rm_xdm.py:J1939Rm`
**Status:** Implemented

---

### SWR_J1939TP_MODELS_00001 - J1939Tp Model

The system shall provide a `J1939Tp` root model class for J1939 Transport Protocol.

**Implementation:** `j1939_stack/j1939tp_xdm.py:J1939Tp`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_J1939DCM_MODELS_00001 | j1939dcm_xdm.py:J1939Dcm | UTS_J1939DCM_MODEL_00001 |
| SWR_J1939NM_MODELS_00001 | j1939nm_xdm.py:J1939Nm | UTS_J1939NM_MODEL_00001 |
| SWR_J1939RM_MODELS_00001 | j1939rm_xdm.py:J1939Rm | UTS_J1939RM_MODEL_00001 |
| SWR_J1939TP_MODELS_00001 | j1939tp_xdm.py:J1939Tp | UTS_J1939TP_MODEL_00001 |
