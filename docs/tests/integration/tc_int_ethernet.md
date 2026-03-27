# Ethernet Stack Integration Test Cases

This document contains all integration test cases for the Ethernet Communication Stack modules (EthIf, EthSm, DoIP, SoAd, SomeIpTp, TcpIp, UdpNm) following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_INT_ETHERNET_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_ETHERNET_00001 |
| Title | Ethernet Stack - End-to-End Parsing and Excel Export |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete end-to-end workflow of parsing Ethernet stack XDM files and exporting to Excel.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Ethernet stack XDM files are available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse EthIf configuration | Configuration parsed successfully |
| 2 | Parse EthSm configuration | Configuration parsed successfully |
| 3 | Parse DoIP configuration | Configuration parsed successfully |
| 4 | Parse SoAd configuration | Configuration parsed successfully |
| 5 | Parse SomeIpTp configuration | Configuration parsed successfully |
| 6 | Parse TcpIp configuration | Configuration parsed successfully |
| 7 | Parse UdpNm configuration | Configuration parsed successfully |
| 8 | Generate Excel outputs | All files created successfully |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ETHIF_00001 | EthIf Module Parsing | Covered |
| SWR_ETHSM_00001 | EthSm Module Parsing | Covered |
| SWR_DOIP_00001 | DoIP Module Parsing | Covered |
| SWR_SOAD_00001 | SoAd Module Parsing | Covered |
| SWR_SOMEIPTP_00001 | SomeIpTp Module Parsing | Covered |
| SWR_TCPIP_00001 | TcpIp Module Parsing | Covered |
| SWR_UDPNM_00001 | UdpNm Module Parsing | Covered |

---

# Test Case: TC_INT_ETHERNET_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_ETHERNET_00002 |
| Title | Ethernet Stack - Multi-Controller Configuration |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the Ethernet stack parser can handle multi-controller configurations.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Multi-controller Ethernet configuration is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse multi-controller EthIf | All controllers extracted |
| 2 | Verify controller count | Count matches configuration |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ETHIF_00001 | EthIf Module Parsing | Covered |

---

# Test Case: TC_INT_ETHERNET_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_ETHERNET_00003 |
| Title | Ethernet Stack - Error Recovery |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the Ethernet stack modules handle error conditions gracefully.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Test files with error conditions are available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse invalid Ethernet file | Error reported clearly |
| 2 | Verify system recovery | Subsequent operations work |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ETHIF_00001 | EthIf Module Parsing | Covered |