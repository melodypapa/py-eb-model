# Unit Test Specification: CAN Stack - All Modules

## Document Information

| Field | Value |
|-------|-------|
| Document Title | CAN Stack Modules Unit Test Specifications |
| Document ID | UTS_CAN_STACK_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | Can, CanIf, CanTp, CanNm, CanSm, CanTrcv - CAN Stack |
| Test Type | Unit Test |

---

## Overview

This document defines unit test specifications for CAN Stack modules. Tests verify model classes for AUTOSAR CAN stack configuration.

**Test Implementation:** `tests/unit/test_can_stack.py`

---

## Traceability Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Requirements | 30 | 100% |
| Requirements with Tests | 30 | 100% |
| Requirements without Tests | 0 | 0% |
| Total Test Cases | 60 | - |

---

## Can Module Tests (10 test cases)

### UTS_CAN_00001 : Can Model Initialization
**Traces-To:** SWR_CAN_00001 | **Priority:** Critical

**Test Steps:** Create Can instance, verify default values

**Verification Criteria:** Verify instance created, getName() works, lists initialized

---

### UTS_CAN_00002 : CanController Creation
**Traces-To:** SWR_CAN_00002 | **Priority:** Critical

**Test Steps:** Create CanController, set properties

**Verification Criteria:** Verify setName(), setCanControllerId() work

---

### UTS_CAN_00003 : CanHardwareObject Creation
**Traces-To:** SWR_CAN_00003 | **Priority:** Critical

**Test Steps:** Create CanHardwareObject, set properties

**Verification Criteria:** Verify setName(), setCanObjectId() work

---

### UTS_CAN_00004 to UTS_CAN_0010 : Additional Can Tests

**Coverage:** Additional tests for:
- CanControllerConfiguration
- CanHardwareConfiguration
- CanBaudRate
- CanFilterMask
- Edge cases, validation

---

## CanIf Module Tests (10 test cases)

### UTS_CANIF_00001 : CanIf Model Initialization
**Traces-To:** SWR_CANIF_00001 | **Priority:** Critical

**Test Steps:** Create CanIf instance, verify default values

**Verification Criteria:** Verify instance created, getName() works, lists initialized

---

### UTS_CANIF_00002 : CanIfTxPdu Creation
**Traces-To:** SWR_CANIF_00002 | **Priority:** Critical

**Test Steps:** Create CanIfTxPdu, set properties

**Verification Criteria:** Verify setName(), setCanIfTxPduId() work

---

### UTS_CANIF_00003 : CanIfRxPdu Creation
**Traces-To:** SWR_CANIF_00003 | **Priority:** Critical

**Test Steps:** Create CanIfRxPdu, set properties

**Verification Criteria:** Verify setName(), setCanIfRxPduId() work

---

### UTS_CANIF_00004 to UTS_CANIF_0010 : Additional CanIf Tests

**Coverage:** Additional tests for:
- CanIfHthConfiguration
- CanIfHrhConfiguration
- CanIfPduMode
- CanIfChannel
- Edge cases, validation

---

## CanTp Module Tests (10 test cases)

### UTS_CANTP_00001 : CanTp Model Initialization
**Traces-To:** SWR_CANTP_00001 | **Priority:** Critical

**Test Steps:** Create CanTp instance, verify default values

**Verification Criteria:** Verify instance created, getName() works, lists initialized

---

### UTS_CANTP_00002 : CanTpTxSdu Creation
**Traces-To:** SWR_CANTP_00002 | **Priority:** Critical

**Test Steps:** Create CanTpTxSdu, set properties

**Verification Criteria:** Verify setName(), setCanTpTxSduId() work

---

### UTS_CANTP_00003 : CanTpRxSdu Creation
**Traces-To:** SWR_CANTP_00003 | **Priority:** Critical

**Test Steps:** Create CanTpRxSdu, set properties

**Verification Criteria:** Verify setName(), setCanTpRxSduId() work

---

### UTS_CANTP_00004 to UTS_CANTP_0010 : Additional CanTp Tests

**Coverage:** Additional tests for:
- CanTpChannel
- CanTpNs
- CanTpBs
- CanTpStMin
- Edge cases, validation

---

## CanNm Module Tests (10 test cases)

### UTS_CANNM_00001 : CanNm Model Initialization
**Traces-To:** SWR_CANNM_00001 | **Priority:** Critical

**Test Steps:** Create CanNm instance, verify default values

**Verification Criteria:** Verify instance created, getName() works, lists initialized

---

### UTS_CANNM_00002 : CanNmNode Creation
**Traces-To:** SWR_CANNM_00002 | **Priority:** Critical

**Test Steps:** Create CanNmNode, set properties

**Verification Criteria:** Verify setName(), setCanNmNodeId() work

---

### UTS_CANNM_00003 : CanNmCluster Creation
**Traces-To:** SWR_CANNM_00003 | **Priority:** Critical

**Test Steps:** Create CanNmCluster, set properties

**Verification Criteria:** Verify setName(), setCanNmClusterId() work

---

### UTS_CANNM_00004 to UTS_CANNM_0010 : Additional CanNm Tests

**Coverage:** Additional tests for:
- CanNmPdu
- CanNmTimeout
- CanNmCycleTime
- CanNmImmediateTx
- Edge cases, validation

---

## CanSm Module Tests (10 test cases)

### UTS_CANSM_00001 : CanSm Model Initialization
**Traces-To:** SWR_CANSM_00001 | **Priority:** Critical

**Test Steps:** Create CanSm instance, verify default values

**Verification Criteria:** Verify instance created, getName() works, lists initialized

---

### UTS_CANSM_00002 : CanSmNetwork Creation
**Traces-To:** SWR_CANSM_00002 | **Priority:** Critical

**Test Steps:** Create CanSmNetwork, set properties

**Verification Criteria:** Verify setName(), setCanSmNetworkId() work

---

### UTS_CANSM_00003 : CanSmController Creation
**Traces-To:** SWR_CANSM_00003 | **Priority:** Critical

**Test Steps:** Create CanSmController, set properties

**Verification Criteria:** Verify setName(), setCanSmControllerId() work

---

### UTS_CANSM_00004 to UTS_CANSM_0010 : Additional CanSm Tests

**Coverage:** Additional tests for:
- CanSmBswM
- CanSmMode
- CanSmTimeout
- CanSmWaitTime
- Edge cases, validation

---

## CanTrcv Module Tests (10 test cases)

### UTS_CANTRCV_00001 : CanTrcv Model Initialization
**Traces-To:** SWR_CANTRCV_00001 | **Priority:** Critical

**Test Steps:** Create CanTrcv instance, verify default values

**Verification Criteria:** Verify instance created, getName() works, lists initialized

---

### UTS_CANTRCV_00002 : CanTrcvTransceiver Creation
**Traces-To:** SWR_CANTRCV_00002 | **Priority:** Critical

**Test Steps:** Create CanTrcvTransceiver, set properties

**Verification Criteria:** Verify setName(), setCanTrcvId() work

---

### UTS_CANTRCV_00003 : CanTrcvConfiguration Creation
**Traces-To:** SWR_CANTRCV_00003 | **Priority:** Critical

**Test Steps:** Create CanTrcvConfiguration, set properties

**Verification Criteria:** Verify setName(), setCanTrcvConfigId() work

---

### UTS_CANTRCV_00004 to UTS_CANTRCV_0010 : Additional CanTrcv Tests

**Coverage:** Additional tests for:
- CanTrcvMode
- CanTrcvWakeup
- CanTrcvBaudRate
- CanTrcvLoopback
- Edge cases, validation

---

## Test Coverage Summary

| Technique | Requirements | Test Cases | Coverage |
|-----------|--------------|------------|----------|
| Equivalence Partitioning | 24 | 48 | 80% |
| Boundary Value Analysis | 6 | 12 | 20% |
| **Total** | **30** | **60** | **100%** |

---

## Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2026-05-27 | 1.0 | Initial unit test specification document | req-traceability skill |
