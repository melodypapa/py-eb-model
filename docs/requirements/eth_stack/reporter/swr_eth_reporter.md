# Software Requirements: ETH Stack - Reporter Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | ETH Stack Reporter Layer Requirements |
| Document ID | SWR_ETH_REPORTER_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | ETH Stack - Reporter Layer |

---

## Overview

The ETH Stack Reporter Layer provides Excel export functionality for AUTOSAR Ethernet communication modules.

**Implementation:** `src/eb_model/reporter/excel_reporter/eth_stack/`

---

## Requirements

### SWR_ETHIF_REPORTER_00001 - EthIf Excel Workbook

The reporter shall create an Excel workbook for EthIf configuration.

**Implementation:** `eth_stack/ethif_xdm.py:EthIfXdmXlsWriter`
**Status:** Implemented

---

### SWR_TCPIP_REPORTER_00001 - TcpIp Excel Workbook

The reporter shall create an Excel workbook for TcpIp configuration.

**Implementation:** `eth_stack/tcpip_xdm.py:TcpIpXdmXlsWriter`
**Status:** Implemented

---

### SWR_SOAD_REPORTER_00001 - SoAd Excel Workbook

The reporter shall create an Excel workbook for SoAd configuration.

**Implementation:** `eth_stack/soad_xdm.py:SoAdXdmXlsWriter`
**Status:** Implemented

---

### SWR_DOIP_REPORTER_00001 - DoIP Excel Workbook

The reporter shall create an Excel workbook for DoIP configuration.

**Implementation:** `eth_stack/doip_xdm.py:DoIPXdmXlsWriter`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_ETHIF_REPORTER_00001 | ethif_xdm.py:EthIfXdmXlsWriter | TC_UNIT_ETHIF_RPT_00001 |
| SWR_TCPIP_REPORTER_00001 | tcpip_xdm.py:TcpIpXdmXlsWriter | TC_UNIT_TCPIP_RPT_00001 |
| SWR_SOAD_REPORTER_00001 | soad_xdm.py:SoAdXdmXlsWriter | TC_UNIT_SOAD_RPT_00001 |
| SWR_DOIP_REPORTER_00001 | doip_xdm.py:DoIPXdmXlsWriter | TC_UNIT_DOIP_RPT_00001 |
