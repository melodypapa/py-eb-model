# Software Requirements: CAN Stack - Model Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | CAN Stack Model Layer Requirements |
| Document ID | SWR_CAN_MODELS_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | CAN Stack - Model Layer |

---

## Overview

The CAN Stack Model Layer provides Python classes representing AUTOSAR CAN communication configuration entities.

**Implementation:** `src/eb_model/models/can_stack/`

---

## Requirements

### SWR_CANIF_MODELS_00001 - CanIf Model (Root)

The system shall provide a `CanIf` root model class containing all CanIf entities.

**Methods:**
- `getCanIfGeneral()` - Get general configuration
- `getCanIfCtrlCfgList()` - Get controller configurations
- `getCanIfTrcvCfgList()` - Get transceiver configurations
- `getCanIfRxPduCfgList()` - Get Rx PDU configurations
- `getCanIfTxPduCfgList()` - Get Tx PDU configurations

**Implementation:** `can_stack/canif_xdm.py:CanIf`
**Status:** Implemented

---

### SWR_CANIF_MODELS_00002 - CanIfGeneral Model

The system shall provide a `CanIfGeneral` model class for global CanIf settings.

| Field | Type | Description |
|-------|------|-------------|
| CanIfDevErrorDetect | bool | Development error detection |
| CanIfNumOfCanHardwareUnits | int | Number of CAN hardware units |
| CanIfMaxCtrl | int | Maximum controllers |
| CanIfMaxTxPdu | int | Maximum Tx PDUs |
| CanIfMaxRxPdu | int | Maximum Rx PDUs |

**Implementation:** `can_stack/canif_xdm.py:CanIfGeneral`
**Status:** Implemented

---

### SWR_CANIF_MODELS_00003 - CanIfCtrlCfg Model

The system shall provide a `CanIfCtrlCfg` model class for CAN controller configuration.

| Field | Type | Description |
|-------|------|-------------|
| CanIfCtrlId | int | Controller ID |
| CanIfCtrlWakeupSupport | bool | Wakeup support |
| CanIfCtrlCanCtrlRef | EcucRefType | CAN controller reference |

**Implementation:** `can_stack/canif_xdm.py:CanIfCtrlCfg`
**Status:** Implemented

---

### SWR_CANNM_MODELS_00001 - CanNm Model (Root)

The system shall provide a `CanNm` root model class containing all CanNm entities.

**Methods:**
- `getCanNmChannelList()` - Get channel configurations

**Implementation:** `can_stack/cannm_xdm.py:CanNm`
**Status:** Implemented

---

### SWR_CANNM_MODELS_00002 - CanNmChannel Model

The system shall provide a `CanNmChannel` model class for NM channel configuration.

| Field | Type | Description |
|-------|------|-------------|
| CanNmNmTimeoutTime | int | NM timeout |
| CanNmWaitBusSleepTime | int | Wait bus sleep time |
| CanNmRemoteSleepIndTime | int | Remote sleep indication time |
| CanNmMsgCycleTime | int | Message cycle time |
| CanNmMsgReducedTime | int | Reduced message time |
| CanNmImmediateRestartTime | int | Immediate restart time |

**Implementation:** `can_stack/cannm_xdm.py:CanNmChannel`
**Status:** Implemented

---

### SWR_CANSM_MODELS_00001 - CanSm Model (Root)

The system shall provide a `CanSm` root model class containing all CanSm entities.

**Methods:**
- `getCanSmNetworkList()` - Get network configurations

**Implementation:** `can_stack/cansm_xdm.py:CanSm`
**Status:** Implemented

---

### SWR_CANSM_MODELS_00002 - CanSmNetwork Model

The system shall provide a `CanSmNetwork` model class for CAN network configuration.

| Field | Type | Description |
|-------|------|-------------|
| CanSmNetworkId | int | Network ID |
| CanSmControllerRef | EcucRefType | Controller reference |
| CanSmTransceiverRef | EcucRefType | Transceiver reference |

**Implementation:** `can_stack/cansm_xdm.py:CanSmNetwork`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_CANIF_MODELS_00001 | canif_xdm.py:CanIf | UTS_CANIF_MODEL_00001 |
| SWR_CANIF_MODELS_00002 | canif_xdm.py:CanIfGeneral | UTS_CANIF_MODEL_00002 |
| SWR_CANIF_MODELS_00003 | canif_xdm.py:CanIfCtrlCfg | UTS_CANIF_MODEL_00003 |
| SWR_CANNM_MODELS_00001 | cannm_xdm.py:CanNm | UTS_CANNM_MODEL_00001 |
| SWR_CANNM_MODELS_00002 | cannm_xdm.py:CanNmChannel | UTS_CANNM_MODEL_00002 |
| SWR_CANSM_MODELS_00001 | cansm_xdm.py:CanSm | UTS_CANSM_MODEL_00001 |
| SWR_CANSM_MODELS_00002 | cansm_xdm.py:CanSmNetwork | UTS_CANSM_MODEL_00002 |
