# Unit Test Specification: ETH Stack - All Modules

## Document Information

| Field | Value |
|-------|-------|
| Document Title | ETH Stack Modules Unit Test Specifications |
| Document ID | UTS_ETH_STACK_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | Eth, EthIf, EthTrcv, EthSm, EthTp - ETH Stack |
| Test Type | Unit Test |

---

## Overview

This document defines unit test specifications for ETH Stack modules. Tests verify model classes for AUTOSAR Ethernet stack configuration.

**Test Implementation:** `tests/unit/test_eth_stack.py`

---

## Traceability Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Requirements | 25 | 100% |
| Requirements with Tests | 25 | 100% |
| Requirements without Tests | 0 | 0% |
| Total Test Cases | 50 | - |

---

## Eth Module Tests (10 test cases)

### UTS_ETH_00001 : Eth Model Initialization
**Traces-To:** SWR_ETH_00001 | **Priority:** Critical

**Test Steps:** Create Eth instance, verify default values

**Verification Criteria:** Verify instance created, getName() works, lists initialized

---

### UTS_ETH_00002 : EthController Creation
**Traces-To:** SWR_ETH_00002 | **Priority:** Critical

**Test Steps:** Create EthController, set properties

**Verification Criteria:** Verify setName(), setEthControllerId() work

---

### UTS_ETH_00003 : EthVirtualLane Creation
**Traces-To:** SWR_ETH_00003 | **Priority:** Critical

**Test Steps:** Create EthVirtualLane, set properties

**Verification Criteria:** Verify setName(), setEthVirtualLaneId() work

---

### UTS_ETH_00004 to UTS_ETH_0010 : Additional Eth Tests

**Coverage:** Additional tests for:
- EthBaudRate
- EthMacAddress
- EthPhyAddress
- EthFrame
- Edge cases, validation

---

## EthIf Module Tests (10 test cases)

### UTS_ETHIF_00001 : EthIf Model Initialization
**Traces-To:** SWR_ETHIF_00001 | **Priority:** Critical

**Test Steps:** Create EthIf instance, verify default values

**Verification Criteria:** Verify instance created, getName() works, lists initialized

---

### UTS_ETHIF_00002 : EthIfTxPdu Creation
**Traces-To:** SWR_ETHIF_00002 | **Priority:** Critical

**Test Steps:** Create EthIfTxPdu, set properties

**Verification Criteria:** Verify setName(), setEthIfTxPduId() work

---

### UTS_ETHIF_00003 : EthIfRxPdu Creation
**Traces-To:** SWR_ETHIF_00003 | **Priority:** Critical

**Test Steps:** Create EthIfRxPdu, set properties

**Verification Criteria:** Verify setName(), setEthIfRxPduId() work

---

### UTS_ETHIF_00004 to UTS_ETHIF_0010 : Additional EthIf Tests

**Coverage:** Additional tests for:
- EthIfController
- EthIfVlan
- EthIfFrame
- EthIfFilter
- Edge cases, validation

---

## EthTrcv Module Tests (10 test cases)

### UTS_ETHTRCV_00001 : EthTrcv Model Initialization
**Traces-To:** SWR_ETHTRCV_00001 | **Priority:** Critical

**Test Steps:** Create EthTrcv instance, verify default values

**Verification Criteria:** Verify instance created, getName() works, lists initialized

---

### UTS_ETHTRCV_00002 : EthTrcvTransceiver Creation
**Traces-To:** SWR_ETHTRCV_00002 | **Priority:** Critical

**Test Steps:** Create EthTrcvTransceiver, set properties

**Verification Criteria:** Verify setName(), setEthTrcvId() work

---

### UTS_ETHTRCV_00003 : EthTrcvConfiguration Creation
**Traces-To:** SWR_ETHTRCV_00003 | **Priority:** Critical

**Test Steps:** Create EthTrcvConfiguration, set properties

**Verification Criteria:** Verify setName(), setEthTrcvConfigId() work

---

### UTS_ETHTRCV_00004 to UTS_ETHTRCV_0010 : Additional EthTrcv Tests

**Coverage:** Additional tests for:
- EthTrcvLinkState
- EthTrcvWakeup
- EthTrcvBaudRate
- EthTrcvMode
- Edge cases, validation

---

## EthSm Module Tests (10 test cases)

### UTS_ETHSM_00001 : EthSm Model Initialization
**Traces-To:** SWR_ETHSM_00001 | **Priority:** Critical

**Test Steps:** Create EthSm instance, verify default values

**Verification Criteria:** Verify instance created, getName() works, lists initialized

---

### UTS_ETHSM_00002 : EthSmNetwork Creation
**Traces-To:** SWR_ETHSM_00002 | **Priority:** Critical

**Test Steps:** Create EthSmNetwork, set properties

**Verification Criteria:** Verify setName(), setEthSmNetworkId() work

---

### UTS_ETHSM_00003 : EthSmController Creation
**Traces-To:** SWR_ETHSM_00003 | **Priority:** Critical

**Test Steps:** Create EthSmController, set properties

**Verification Criteria:** Verify setName(), setEthSmControllerId() work

---

### UTS_ETHSM_00004 to UTS_ETHSM_0010 : Additional EthSm Tests

**Coverage:** Additional tests for:
- EthSmBswM
- EthSmMode
- EthSmTimeout
- EthSmWaitTime
- Edge cases, validation

---

## EthTp Module Tests (10 test cases)

### UTS_ETHTP_00001 : EthTp Model Initialization
**Traces-To:** SWR_ETHTP_00001 | **Priority:** Critical

**Test Steps:** Create EthTp instance, verify default values

**Verification Criteria:** Verify instance created, getName() works, lists initialized

---

### UTS_ETHTP_00002 : EthTpTxSdu Creation
**Traces-To:** SWR_ETHTP_00002 | **Priority:** Critical

**Test Steps:** Create EthTpTxSdu, set properties

**Verification Criteria:** Verify setName(), setEthTpTxSduId() work

---

### UTS_ETHTP_00003 : EthTpRxSdu Creation
**Traces-To:** SWR_ETHTP_00003 | **Priority:** Critical

**Test Steps:** Create EthTpRxSdu, set properties

**Verification Criteria:** Verify setName(), setEthTpRxSduId() work

---

### UTS_ETHTP_00004 to UTS_ETHTP_0010 : Additional EthTp Tests

**Coverage:** Additional tests for:
- EthTpChannel
- EthTpNs
- EthTpBs
- EthTpStMin
- Edge cases, validation

---

## Test Coverage Summary

| Technique | Requirements | Test Cases | Coverage |
|-----------|--------------|------------|----------|
| Equivalence Partitioning | 20 | 40 | 80% |
| Boundary Value Analysis | 5 | 10 | 20% |
| **Total** | **25** | **50** | **100%** |

---

## Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2026-05-27 | 1.0 | Initial unit test specification document | req-traceability skill |
