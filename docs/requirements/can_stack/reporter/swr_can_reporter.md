# Software Requirements: CAN Stack - Reporter Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | CAN Stack Reporter Layer Requirements |
| Document ID | SWR_CAN_REPORTER_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | CAN Stack - Reporter Layer |

---

## Overview

The CAN Stack Reporter Layer provides Excel export functionality for AUTOSAR CAN communication modules.

**Implementation:** `src/eb_model/reporter/excel_reporter/can_stack/`

---

## Requirements

### SWR_CANIF_REPORTER_00001 - CanIf Excel Workbook

The reporter shall create an Excel workbook with multiple worksheets for CanIf configuration.

**Worksheets:**
1. General - Version and settings
2. Controllers - Controller configurations
3. Transceivers - Transceiver configurations
4. RxPdu - Rx PDU configurations
5. TxPdu - Tx PDU configurations

**Implementation:** `can_stack/canif_xdm.py:CanIfXdmXlsWriter`
**Status:** Implemented

---

### SWR_CANNM_REPORTER_00001 - CanNm Excel Workbook

The reporter shall create an Excel workbook for CanNm configuration.

**Worksheets:**
1. General - Version and settings
2. Channels - Channel configurations with timing parameters

**Implementation:** `can_stack/cannm_xdm.py:CanNmXdmXlsWriter`
**Status:** Implemented

---

### SWR_CANSM_REPORTER_00001 - CanSm Excel Workbook

The reporter shall create an Excel workbook for CanSm configuration.

**Worksheets:**
1. General - Version and settings
2. Networks - Network configurations

**Implementation:** `can_stack/cansm_xdm.py:CanSmXdmXlsWriter`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_CANIF_REPORTER_00001 | canif_xdm.py:CanIfXdmXlsWriter | TC_UNIT_CANIF_RPT_00001 |
| SWR_CANNM_REPORTER_00001 | cannm_xdm.py:CanNmXdmXlsWriter | TC_UNIT_CANNM_RPT_00001 |
| SWR_CANSM_REPORTER_00001 | cansm_xdm.py:CanSmXdmXlsWriter | TC_UNIT_CANSM_RPT_00001 |
