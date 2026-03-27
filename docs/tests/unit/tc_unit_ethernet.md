# Ethernet Stack Unit Test Cases

This document contains all unit test cases for the Ethernet Communication Stack modules (EthIf, EthSm, DoIP, SoAd, SomeIpTp, TcpIp, UdpNm) following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_ETHIF_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ETHIF_00001 |
| Title | EthIf Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EthIf parser correctly validates the module name and extracts Ethernet interface configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid EthIf.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid EthIf.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "EthIf" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ETHIF_00001 | EthIf Module Parsing | Covered |

---

# Test Case: TC_UNIT_ETHSM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ETHSM_00001 |
| Title | EthSm Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EthSm parser correctly validates the module name and extracts state manager configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid EthSm.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid EthSm.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "EthSm" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ETHSM_00001 | EthSm Module Parsing | Covered |

---

# Test Case: TC_UNIT_DOIP_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_DOIP_00001 |
| Title | DoIP Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the DoIP parser correctly validates the module name and extracts Diagnostics over IP configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid DoIP.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid DoIP.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "DoIP" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_DOIP_00001 | DoIP Module Parsing | Covered |

---

# Test Case: TC_UNIT_SOAD_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_SOAD_00001 |
| Title | SoAd Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the SoAd parser correctly validates the module name and extracts socket adapter configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid SoAd.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid SoAd.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "SoAd" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_SOAD_00001 | SoAd Module Parsing | Covered |

---

# Test Case: TC_UNIT_SOMEIPTP_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_SOMEIPTP_00001 |
| Title | SomeIpTp Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the SomeIpTp parser correctly validates the module name and extracts SOME/IP transport protocol configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid SomeIpTp.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid SomeIpTp.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "SomeIpTp" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_SOMEIPTP_00001 | SomeIpTp Module Parsing | Covered |

---

# Test Case: TC_UNIT_TCPIP_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_TCPIP_00001 |
| Title | TcpIp Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the TcpIp parser correctly validates the module name and extracts TCP/IP stack configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid TcpIp.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid TcpIp.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "TcpIp" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_TCPIP_00001 | TcpIp Module Parsing | Covered |

---

# Test Case: TC_UNIT_UDPNM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_UDPNM_00001 |
| Title | UdpNm Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the UdpNm parser correctly validates the module name and extracts UDP network management configuration.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid UdpNm.xdm file is available |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse valid UdpNm.xdm file | File parses successfully |
| 2 | Verify module name validation | Module "UdpNm" is accepted |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_UDPNM_00001 | UdpNm Module Parsing | Covered |

---

# Test Case: TC_UNIT_ETHIF_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ETHIF_00002 |
| Title | EthIf Reporter - Excel Worksheet Generation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EthIf reporter correctly generates Excel worksheets.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | EthIf model objects are populated |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Generate Excel output | File created successfully |
| 2 | Verify worksheet content | All data populated correctly |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ETHIF_00002 | EthIf Excel Generation | Covered |