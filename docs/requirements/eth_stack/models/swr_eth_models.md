# Software Requirements: ETH Stack - Model Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | ETH Stack Model Layer Requirements |
| Document ID | SWR_ETH_MODELS_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | ETH Stack - Model Layer |

---

## Overview

The ETH Stack Model Layer provides Python classes representing AUTOSAR Ethernet communication configuration entities.

**Implementation:** `src/eb_model/models/eth_stack/`

---

## Requirements

### SWR_ETHIF_MODELS_00001 - EthIf Model (Root)

The system shall provide an `EthIf` root model class containing all EthIf entities.

**Methods:**
- `getEthIfGeneral()` - Get general configuration
- `getEthIfCtrlCfgList()` - Get controller configurations

**Implementation:** `eth_stack/ethif_xdm.py:EthIf`
**Status:** Implemented

---

### SWR_TCPIP_MODELS_00001 - TcpIp Model (Root)

The system shall provide a `TcpIp` root model class containing all TcpIp entities.

**Methods:**
- `getTcpIpGeneral()` - Get general configuration
- `getTcpIpCtrlList()` - Get controller configurations

**Implementation:** `eth_stack/tcpip_xdm.py:TcpIp`
**Status:** Implemented

---

### SWR_SOAD_MODELS_00001 - SoAd Model (Root)

The system shall provide a `SoAd` root model class containing all SoAd entities.

**Methods:**
- `getSoAdGeneral()` - Get general configuration
- `getSoAdRoutingGroupList()` - Get routing group configurations

**Implementation:** `eth_stack/soad_xdm.py:SoAd`
**Status:** Implemented

---

### SWR_DOIP_MODELS_00001 - DoIP Model (Root)

The system shall provide a `DoIP` root model class containing all DoIP entities.

**Methods:**
- `getDoIpGeneral()` - Get general configuration

**Implementation:** `eth_stack/doip_xdm.py:DoIP`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_ETHIF_MODELS_00001 | ethif_xdm.py:EthIf | UTS_ETHIF_MODEL_00001 |
| SWR_TCPIP_MODELS_00001 | tcpip_xdm.py:TcpIp | UTS_TCPIP_MODEL_00001 |
| SWR_SOAD_MODELS_00001 | soad_xdm.py:SoAd | UTS_SOAD_MODEL_00001 |
| SWR_DOIP_MODELS_00001 | doip_xdm.py:DoIP | UTS_DOIP_MODEL_00001 |
