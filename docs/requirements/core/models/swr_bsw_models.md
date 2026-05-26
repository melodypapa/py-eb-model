# Software Requirements: BSW Modules - Model Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | BSW Modules Model Layer Requirements |
| Document ID | SWR_BSW_MODELS_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | BSW Modules - Model Layer |

---

## Overview

The BSW Modules Model Layer provides Python classes for Basic Software modules.

**Implementation:** `src/eb_model/models/core/`

---

## Requirements

### SWR_BSWM_MODELS_00001 - BswM Model

The system shall provide a `BswM` root model class for BSW Mode Manager.

**Implementation:** `core/bswm_xdm.py:BswM`
**Status:** Implemented

---

### SWR_DET_MODELS_00001 - Det Model

The system shall provide a `Det` root model class for Default Error Tracer.

**Implementation:** `core/det_xdm.py:Det`
**Status:** Implemented

---

### SWR_ECUM_MODELS_00001 - EcuM Model

The system shall provide an `EcuM` root model class for ECU State Manager.

**Implementation:** `core/ecum_xdm.py:EcuM`
**Status:** Implemented

---

### SWR_PBCFGM_MODELS_00001 - PbcfgM Model

The system shall provide a `PbcfgM` root model class for Post-Build Configuration Manager.

**Implementation:** `core/pbcfgm_xdm.py:PbcfgM`
**Status:** Implemented

---

### SWR_TM_MODELS_00001 - Tm Model

The system shall provide a `Tm` root model class for Timer Module.

**Implementation:** `core/tm_xdm.py:Tm`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_BSWM_MODELS_00001 | bswm_xdm.py:BswM | UTS_BSWM_MODEL_00001 |
| SWR_DET_MODELS_00001 | det_xdm.py:Det | UTS_DET_MODEL_00001 |
| SWR_ECUM_MODELS_00001 | ecum_xdm.py:EcuM | UTS_ECUM_MODEL_00001 |
| SWR_PBCFGM_MODELS_00001 | pbcfgm_xdm.py:PbcfgM | UTS_PBCFGM_MODEL_00001 |
| SWR_TM_MODELS_00001 | tm_xdm.py:Tm | UTS_TM_MODEL_00001 |
