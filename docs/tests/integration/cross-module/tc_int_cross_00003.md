# Test Case: TC_INT_CROSS_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_CROSS_00003 |
| Title | Cross-Module - Ethernet Stack End-to-End |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete Ethernet stack integration, ensuring that EthIf, EthSm, DoIP, SoAd, SomeIpTp, TcpIp, and UdpNm modules work together correctly with proper socket and routing coordination.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Ethernet stack XDM files are available |
| 3 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| EthIf XDM File | `data/test/EthIf.xdm` | Ethernet Interface configuration |
| EthSm XDM File | `data/test/EthSm.xdm` | Ethernet State Manager |
| DoIP XDM File | `data/test/DoIp.xdm` | Diagnostics over IP |
| SoAd XDM File | `data/test/SoAd.xdm` | Socket Adapter |
| SomeIpTp XDM File | `data/test/SomeIpTp.xdm` | SOME/IP Transport |
| TcpIp XDM File | `data/test/TcpIp.xdm` | TCP/IP Stack |
| UdpNm XDM File | `data/test/UdpNm.xdm` | UDP Network Management |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse EthIf XDM file | EthIf model populated with controllers |
| 2 | Parse EthSm XDM file | EthSm model populated with networks |
| 3 | Parse DoIP XDM file | DoIp model populated with channels |
| 4 | Parse SoAd XDM file | SoAd model populated with socket connections |
| 5 | Parse SomeIpTp XDM file | SomeIpTp model populated with channels |
| 6 | Parse TcpIp XDM file | TcpIp model populated with controllers |
| 7 | Parse UdpNm XDM file | UdpNm model populated with channels |
| 8 | Verify controller references | EthSm references EthIf controllers |
| 9 | Verify socket and routing coordination | Connections route correctly through stack |
| 10 | Generate combined Ethernet stack report | All modules in one workbook |

## Expected Results

- All Ethernet stack modules parse successfully
- Cross-module references are resolved correctly
- Socket and routing coordination works
- Combined reports include all stack data
- No conflicting data between modules

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Combined Ethernet stack output persists for review |
| 2 | EBModel contains all Ethernet stack data |
| 3 | No reference resolution errors |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ETHIF_00001-00009 | EthIf module requirements | Covered |
| SWR_ETHSM_00001-00005 | EthSm module requirements | Covered |
| SWR_DOIP_00001-00006 | DoIP module requirements | Covered |
| SWR_SOAD_00001-00007 | SoAd module requirements | Covered |
| SWR_SOMEIPTP_00001-00007 | SomeIpTp module requirements | Covered |
| SWR_TCPIP_00001-00006 | TcpIp module requirements | Covered |
| SWR_UDPNM_00001-00005 | UdpNm module requirements | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_ethif-module.md |
| Requirement Document | ../requirements/swr_ethsm-module.md |
| Requirement Document | ../requirements/swr_doip-module.md |
| Requirement Document | ../requirements/swr_soad-module.md |
| Requirement Document | ../requirements/swr_someiptp-module.md |
| Requirement Document | ../requirements/swr_tcpip-module.md |
| Requirement Document | ../requirements/swr_udpnm-module.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |