# Test Case Registry

## Document Information

| Field | Value |
|-------|-------|
| Document Title | py-eb-model Test Case Registry |
| Document ID | TC_REGISTRY_00001 |
| Version | 1.0 |
| Date | 2026-03-27 |
| Project | py-eb-model |

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Test Cases | 230 |
| Unit Test Cases | 177 |
| Integration Test Cases | 53 |
| Modules Covered | 36 |
| Requirements Covered | ~315 |

## Coverage by Module

| Module | Unit Tests | Integration Tests | Total | Requirements |
|--------|------------|-------------------|-------|--------------|
| OS | 13 | 3 | 16 | 20 |
| RTE | 10 | 3 | 13 | 15 |
| NVM | 10 | 3 | 13 | 16 |
| EcuC | 8 | 3 | 11 | 14 |
| BswM | 7 | 3 | 10 | 14 |
| CanIf | 6 | - | 6 | 16 |
| CanNm | 4 | - | 4 | 10 |
| CanSm | 4 | - | 4 | 8 |
| CanTp | 4 | - | 4 | 9 |
| LinIf | 4 | - | 4 | 9 |
| LinSm | 3 | - | 3 | 6 |
| LinTp | 3 | - | 3 | 7 |
| FrIf | 3 | - | 3 | 6 |
| FrNm | 3 | - | 3 | 5 |
| FrSm | 3 | - | 3 | 5 |
| FrTp | 3 | - | 3 | 7 |
| FrArTp | 3 | - | 3 | 7 |
| EthIf | 5 | - | 5 | 9 |
| EthSm | 3 | - | 3 | 5 |
| DoIP | 4 | - | 4 | 6 |
| SoAd | 4 | - | 4 | 7 |
| SomeIpTp | 4 | - | 4 | 7 |
| TcpIp | 3 | - | 3 | 6 |
| UdpNm | 3 | - | 3 | 5 |
| Det | 3 | - | 3 | 7 |
| EcuM | 3 | - | 3 | 9 |
| Tm | 1 | - | 1 | 6 |
| PbcfgM | 1 | - | 1 | 6 |
| Crypto Stack | 10 | 4 | 14 | 16 |
| Diagnostics Stack | 14 | 4 | 18 | 16 |
| J1939 Stack | 14 | 6 | 20 | 16 |
| Parser | 8 | 1 | 9 | 10 |
| Reporter | 6 | 1 | 7 | 9 |
| CLI | 6 | 1 | 7 | 9 |
| CAN Stack | - | 5 | 5 | N/A |
| LIN Stack | - | 4 | 4 | N/A |
| FlexRay Stack | - | 5 | 5 | N/A |
| Ethernet Stack | - | 6 | 6 | N/A |
| System Modules | - | 3 | 3 | N/A |
| Cross-Module | - | 5 | 5 | N/A |

## Test Case Traceability Matrix

### OS Module Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_OS_00001 | OS Parser - XDM File Parsing and Validation | Unit | SWR_OS_00001, SWR_OS_00012 |
| TC_UNIT_OS_00002 | OS Model - Task Attribute Extraction | Unit | SWR_OS_00002, SWR_OS_00014 |
| TC_UNIT_OS_00003 | OS Model - ISR Attribute Extraction | Unit | SWR_OS_00003 |
| TC_UNIT_OS_00004 | OS Model - Schedule Table Parsing | Unit | SWR_OS_00004 |
| TC_UNIT_OS_00005 | OS Model - Counter Configuration Parsing | Unit | SWR_OS_00005 |
| TC_UNIT_OS_00006 | OS Model - Application Mapping | Unit | SWR_OS_00006 |
| TC_UNIT_OS_00007 | OS Model - Alarm Action Parsing | Unit | SWR_OS_00007 |
| TC_UNIT_OS_00008 | OS Model - Resource Configuration Parsing | Unit | SWR_OS_00008 |
| TC_UNIT_OS_00009 | OS Model - Memory Protection Parsing | Unit | SWR_OS_00009 |
| TC_UNIT_OS_00010 | OS Reporter - Excel Worksheet Generation | Unit | SWR_OS_00010, SWR_OS_00013 |
| TC_UNIT_OS_00011 | OS CLI - Command-Line Interface | Unit | SWR_OS_00011 |
| TC_UNIT_OS_00012 | OS Error Handling - Malformed XML | Unit | SWR_OS_00015, SWR_OS_00016 |
| TC_UNIT_OS_00013 | OS Error Handling - Required Element Validation | Unit | SWR_OS_00017, SWR_OS_00018 |
| TC_INT_OS_00001 | OS Module - End-to-End Parsing and Excel Export | Integration | SWR_OS_00001-00011, SWR_OS_00013-00014 |
| TC_INT_OS_00002 | OS Module - Complex Configuration Handling | Integration | SWR_OS_00002-00009 |
| TC_INT_OS_00003 | OS Module - Error Recovery and Reporting | Integration | SWR_OS_00015-00020 |

### RTE Module Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_RTE_00001 | RTE Parser - XDM File Parsing and Validation | Unit | SWR_RTE_00001, SWR_RTE_00008 |
| TC_UNIT_RTE_00002 | RTE Model - BSW Component Instance Extraction | Unit | SWR_RTE_00002, SWR_RTE_00009 |
| TC_UNIT_RTE_00003 | RTE Model - SW Component Instance Extraction | Unit | SWR_RTE_00003, SWR_RTE_00010 |
| TC_UNIT_RTE_00004 | RTE Model - Event to Task Mapping | Unit | SWR_RTE_00004 |
| TC_UNIT_RTE_00005 | RTE Model - AR 3.x Version Support | Unit | SWR_RTE_00005, SWR_RTE_00011 |
| TC_UNIT_RTE_00006 | RTE Model - AR 4.x Version Support | Unit | SWR_RTE_00006, SWR_RTE_00012 |
| TC_UNIT_RTE_00007 | RTE Reporter - Excel Worksheet Generation | Unit | SWR_RTE_00007, SWR_RTE_00013 |
| TC_UNIT_RTE_00008 | RTE CLI - Command-Line Interface | Unit | SWR_RTE_00014 |
| TC_UNIT_RTE_00009 | RTE Error Handling - Malformed XML | Unit | SWR_RTE_00015 |
| TC_UNIT_RTE_00010 | RTE Error Handling - Missing Required Elements | Unit | SWR_RTE_00015 |
| TC_INT_RTE_00001 | RTE Module - End-to-End Parsing and Excel Export (AR 3.x) | Integration | SWR_RTE_00001-00007, SWR_RTE_00011, SWR_RTE_00013 |
| TC_INT_RTE_00002 | RTE Module - End-to-End Parsing and Excel Export (AR 4.x) | Integration | SWR_RTE_00001-00007, SWR_RTE_00012, SWR_RTE_00013 |
| TC_INT_RTE_00003 | RTE Module - Mixed Version Handling | Integration | SWR_RTE_00005-00006, SWR_RTE_00011-00012 |

### NVM Module Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_NVM_00001 | NVM Parser - XDM File Parsing and Validation | Unit | SWR_NVM_00001, SWR_NVM_00016 |
| TC_UNIT_NVM_00002 | NVM Model - Block Descriptor Extraction | Unit | SWR_NVM_00002 |
| TC_UNIT_NVM_00003 | NVM Model - EA/FEE Reference Extraction | Unit | SWR_NVM_00003, SWR_NVM_00004 |
| TC_UNIT_NVM_00004 | NVM Model - CRC Configuration Parsing | Unit | SWR_NVM_00005 |
| TC_UNIT_NVM_00005 | NVM Model - Callback Function Extraction | Unit | SWR_NVM_00006 |
| TC_UNIT_NVM_00006 | NVM Model - Partition Distribution Parsing | Unit | SWR_NVM_00007 |
| TC_UNIT_NVM_00007 | NVM Reporter - Excel Worksheet Generation | Unit | SWR_NVM_00008, SWR_NVM_00015 |
| TC_UNIT_NVM_00008 | NVM CLI - Command-Line Interface | Unit | SWR_NVM_00009 |
| TC_UNIT_NVM_00009 | NVM Error Handling - Invalid CRC Configuration | Unit | SWR_NVM_00010 |
| TC_UNIT_NVM_00010 | NVM Error Handling - Missing Block Descriptors | Unit | SWR_NVM_00010 |
| TC_INT_NVM_00001 | NVM Module - End-to-End Parsing and Excel Export | Integration | SWR_NVM_00001-00008, SWR_NVM_00015 |
| TC_INT_NVM_00002 | NVM Module - Multi-Partition Configuration | Integration | SWR_NVM_00002-00007 |
| TC_INT_NVM_00003 | NVM Module - Error Recovery and Reporting | Integration | SWR_NVM_00010-00014 |

### EcuC Module Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_ECUC_00001 | EcuC Parser - XDM File Parsing and Validation | Unit | SWR_ECUC_00001, SWR_ECUC_00014 |
| TC_UNIT_ECUC_00002 | EcuC Model - Partition Definition Extraction | Unit | SWR_ECUC_00002 |
| TC_UNIT_ECUC_00003 | EcuC Model - Software Component Instance References | Unit | SWR_ECUC_00003 |
| TC_UNIT_ECUC_00004 | EcuC Model - Restart Capability Parsing | Unit | SWR_ECUC_00004 |
| TC_UNIT_ECUC_00005 | EcuC Reporter - Excel Worksheet Generation | Unit | SWR_ECUC_00005, SWR_ECUC_00013 |
| TC_UNIT_ECUC_00006 | EcuC CLI - Command-Line Interface | Unit | SWR_ECUC_00006 |
| TC_UNIT_ECUC_00007 | EcuC Error Handling - Invalid Partition Configuration | Unit | SWR_ECUC_00010 |
| TC_UNIT_ECUC_00008 | EcuC Error Handling - Missing Required Elements | Unit | SWR_ECUC_00010 |
| TC_INT_ECUC_00001 | EcuC Module - End-to-End Parsing and Excel Export | Integration | SWR_ECUC_00001-00006, SWR_ECUC_00013 |
| TC_INT_ECUC_00002 | EcuC Module - Multi-Partition Configuration | Integration | SWR_ECUC_00002-00004 |
| TC_INT_ECUC_00003 | EcuC Module - Error Recovery and Reporting | Integration | SWR_ECUC_00010-00012 |

### BswM Module Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_BSWM_00001 | BswM Parser - XDM File Parsing and Validation | Unit | SWR_BSWM_00001, SWR_BSWM_00014 |
| TC_UNIT_BSWM_00002 | BswM Model - Mode Declaration Extraction | Unit | SWR_BSWM_00002 |
| TC_UNIT_BSWM_00003 | BswM Model - Arbitration Rule Parsing | Unit | SWR_BSWM_00003 |
| TC_UNIT_BSWM_00004 | BswM Model - Action List Extraction | Unit | SWR_BSWM_00004 |
| TC_UNIT_BSWM_00005 | BswM Model - Mode Request Processing | Unit | SWR_BSWM_00005 |
| TC_UNIT_BSWM_00006 | BswM Reporter - Excel Worksheet Generation | Unit | SWR_BSWM_00006, SWR_BSWM_00013 |
| TC_UNIT_BSWM_00007 | BswM CLI - Command-Line Interface | Unit | SWR_BSWM_00007 |
| TC_INT_BSWM_00001 | BswM Module - End-to-End Parsing and Excel Export | Integration | SWR_BSWM_00001-00007, SWR_BSWM_00013 |
| TC_INT_BSWM_00002 | BswM Module - Complex Mode Machine | Integration | SWR_BSWM_00002-00005 |
| TC_INT_BSWM_00003 | BswM Module - Error Recovery and Reporting | Integration | SWR_BSWM_00010-00012 |

### CAN Stack Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_CANIF_00001 | CanIf Parser - XDM File Parsing and Validation | Unit | SWR_CANIF_00001, SWR_CANIF_00016 |
| TC_UNIT_CANIF_00002 | CanIf Model - Controller Configuration Extraction | Unit | SWR_CANIF_00002 |
| TC_UNIT_CANIF_00003 | CanIf Model - Rx/Tx PDU Configuration | Unit | SWR_CANIF_00003, SWR_CANIF_00004 |
| TC_UNIT_CANIF_00004 | CanIf Model - HRH/HTH Configuration | Unit | SWR_CANIF_00005, SWR_CANIF_00006 |
| TC_UNIT_CANIF_00005 | CanIf Reporter - Excel Worksheet Generation | Unit | SWR_CANIF_00007, SWR_CANIF_00015 |
| TC_UNIT_CANIF_00006 | CanIf CLI - Command-Line Interface | Unit | SWR_CANIF_00008 |
| TC_UNIT_CANNM_00001 | CanNm Parser - XDM File Parsing and Validation | Unit | SWR_CANNM_00001, SWR_CANNM_00010 |
| TC_UNIT_CANNM_00002 | CanNm Model - Channel Timing Configuration | Unit | SWR_CANNM_00002 |
| TC_UNIT_CANNM_00003 | CanNm Model - NM PDU Configuration | Unit | SWR_CANNM_00003 |
| TC_UNIT_CANNM_00004 | CanNm CLI - Command-Line Interface | Unit | SWR_CANNM_00004 |
| TC_UNIT_CANSM_00001 | CanSm Parser - XDM File Parsing and Validation | Unit | SWR_CANSM_00001, SWR_CANSM_00008 |
| TC_UNIT_CANSM_00002 | CanSm Model - State Machine Configuration | Unit | SWR_CANSM_00002 |
| TC_UNIT_CANSM_00003 | CanSm Model - Mode Request Processing | Unit | SWR_CANSM_00003 |
| TC_UNIT_CANSM_00004 | CanSm CLI - Command-Line Interface | Unit | SWR_CANSM_00004 |
| TC_UNIT_CANTP_00001 | CanTp Parser - XDM File Parsing and Validation | Unit | SWR_CANTP_00001, SWR_CANTP_00009 |
| TC_UNIT_CANTP_00002 | CanTp Model - Rx/Tx Channel Configuration | Unit | SWR_CANTP_00002, SWR_CANTP_00003 |
| TC_UNIT_CANTP_00003 | CanTp Model - Timing Parameters (N_Bs, N_Cs, N_Ar, N_Br) | Unit | SWR_CANTP_00004 |
| TC_UNIT_CANTP_00004 | CanTp CLI - Command-Line Interface | Unit | SWR_CANTP_00005 |
| TC_INT_CAN_00001 | CAN Stack - End-to-End Integration Test | Integration | All CAN SWR requirements |
| TC_INT_CAN_00002 | CAN Stack - Multi-Channel Configuration | Integration | SWR_CANIF_00002, SWR_CANNM_00002, SWR_CANSM_00002 |
| TC_INT_CAN_00003 | CAN Stack - Network State Machine Coordination | Integration | SWR_CANNM_00004, SWR_CANSM_00002 |
| TC_INT_CAN_00004 | CAN Stack - PDU Routing Across Layers | Integration | SWR_CANIF_00003-00006, SWR_CANTP_00002-00003 |
| TC_INT_CAN_00005 | CAN Stack - Error Recovery and Reporting | Integration | SWR_CANIF_00016, SWR_CANNM_00010, SWR_CANSM_00008, SWR_CANTP_00009 |

### LIN Stack Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_LINIF_00001 | LinIf Parser - XDM File Parsing and Validation | Unit | SWR_LINIF_00001, SWR_LINIF_00009 |
| TC_UNIT_LINIF_00002 | LinIf Model - Channel Configuration Extraction | Unit | SWR_LINIF_00002 |
| TC_UNIT_LINIF_00003 | LinIf Model - Frame and Signal Mapping | Unit | SWR_LINIF_00003, SWR_LINIF_00004 |
| TC_UNIT_LINIF_00004 | LinIf CLI - Command-Line Interface | Unit | SWR_LINIF_00005 |
| TC_UNIT_LINSM_00001 | LinSm Parser - XDM File Parsing and Validation | Unit | SWR_LINSM_00001, SWR_LINSM_00006 |
| TC_UNIT_LINSM_00002 | LinSm Model - State Machine Configuration | Unit | SWR_LINSM_00002 |
| TC_UNIT_LINSM_00003 | LinSm CLI - Command-Line Interface | Unit | SWR_LINSM_00003 |
| TC_UNIT_LINTP_00001 | LinTp Parser - XDM File Parsing and Validation | Unit | SWR_LINTP_00001, SWR_LINTP_00007 |
| TC_UNIT_LINTP_00002 | LinTp Model - Rx/Tx Channel Configuration | Unit | SWR_LINTP_00002, SWR_LINTP_00003 |
| TC_UNIT_LINTP_00003 | LinTp CLI - Command-Line Interface | Unit | SWR_LINTP_00004 |
| TC_INT_LIN_00001 | LIN Stack - End-to-End Integration Test | Integration | All LIN SWR requirements |
| TC_INT_LIN_00002 | LIN Stack - Multi-Channel Schedule Handling | Integration | SWR_LINIF_00002, SWR_LINSM_00002 |
| TC_INT_LIN_00003 | LIN Stack - PDU Routing and Transport | Integration | SWR_LINIF_00003-00004, SWR_LINTP_00002-00003 |
| TC_INT_LIN_00004 | LIN Stack - Error Recovery and Reporting | Integration | SWR_LINIF_00009, SWR_LINSM_00006, SWR_LINTP_00007 |

### FlexRay Stack Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_FRIF_00001 | FrIf Parser - XDM File Parsing and Validation | Unit | SWR_FRIF_00001, SWR_FRIF_00006 |
| TC_UNIT_FRIF_00002 | FrIf Model - Controller Configuration Extraction | Unit | SWR_FRIF_00002 |
| TC_UNIT_FRIF_00003 | FrIf CLI - Command-Line Interface | Unit | SWR_FRIF_00003 |
| TC_UNIT_FRNM_00001 | FrNm Parser - XDM File Parsing and Validation | Unit | SWR_FRNM_00001, SWR_FRNM_00005 |
| TC_UNIT_FRNM_00002 | FrNm Model - Channel Configuration | Unit | SWR_FRNM_00002 |
| TC_UNIT_FRNM_00003 | FrNm CLI - Command-Line Interface | Unit | SWR_FRNM_00003 |
| TC_UNIT_FRSM_00001 | FrSm Parser - XDM File Parsing and Validation | Unit | SWR_FRSM_00001, SWR_FRSM_00005 |
| TC_UNIT_FRSM_00002 | FrSm Model - Cluster Configuration | Unit | SWR_FRSM_00002 |
| TC_UNIT_FRSM_00003 | FrSm CLI - Command-Line Interface | Unit | SWR_FRSM_00003 |
| TC_UNIT_FRTP_00001 | FrTp Parser - XDM File Parsing and Validation | Unit | SWR_FRTP_00001, SWR_FRTP_00007 |
| TC_UNIT_FRTP_00002 | FrTp Model - Connection Configuration | Unit | SWR_FRTP_00002 |
| TC_UNIT_FRTP_00003 | FrTp CLI - Command-Line Interface | Unit | SWR_FRTP_00003 |
| TC_UNIT_FRARTP_00001 | FrArTp Parser - XDM File Parsing and Validation | Unit | SWR_FRARTP_00001, SWR_FRARTP_00007 |
| TC_UNIT_FRARTP_00002 | FrArTp Model - PDU Configuration | Unit | SWR_FRARTP_00002 |
| TC_UNIT_FRARTP_00003 | FrArTp CLI - Command-Line Interface | Unit | SWR_FRARTP_00003 |
| TC_INT_FLEXRAY_00001 | FlexRay Stack - End-to-End Integration Test | Integration | All FlexRay SWR requirements |
| TC_INT_FLEXRAY_00002 | FlexRay Stack - Multi-Cluster Configuration | Integration | SWR_FRIF_00002, SWR_FRSM_00002 |
| TC_INT_FLEXRAY_00003 | FlexRay Stack - PDU Routing Across Protocols | Integration | SWR_FRNM_00002, SWR_FRTP_00002, SWR_FRARTP_00002 |
| TC_INT_FLEXRAY_00004 | FlexRay Stack - Startup and Shutdown Sequences | Integration | SWR_FRSM_00003, SWR_FRSM_00004 |
| TC_INT_FLEXRAY_00005 | FlexRay Stack - Error Recovery and Reporting | Integration | SWR_FRIF_00006, SWR_FRNM_00005, SWR_FRSM_00005, SWR_FRTP_00007, SWR_FRARTP_00007 |

### Ethernet Stack Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_ETHIF_00001 | EthIf Parser - XDM File Parsing and Validation | Unit | SWR_ETHIF_00001, SWR_ETHIF_00009 |
| TC_UNIT_ETHIF_00002 | EthIf Model - Controller Configuration Extraction | Unit | SWR_ETHIF_00002 |
| TC_UNIT_ETHIF_00003 | EthIf Model - Physical Controller and Switch Configuration | Unit | SWR_ETHIF_00003, SWR_ETHIF_00004 |
| TC_UNIT_ETHIF_00004 | EthIf Model - Rx/Tx Indication Handling | Unit | SWR_ETHIF_00005 |
| TC_UNIT_ETHIF_00005 | EthIf CLI - Command-Line Interface | Unit | SWR_ETHIF_00006 |
| TC_UNIT_ETHSM_00001 | EthSm Parser - XDM File Parsing and Validation | Unit | SWR_ETHSM_00001, SWR_ETHSM_00005 |
| TC_UNIT_ETHSM_00002 | EthSm Model - Network Configuration | Unit | SWR_ETHSM_00002 |
| TC_UNIT_ETHSM_00003 | EthSm CLI - Command-Line Interface | Unit | SWR_ETHSM_00003 |
| TC_UNIT_DOIP_00001 | DoIP Parser - XDM File Parsing and Validation | Unit | SWR_DOIP_00001, SWR_DOIP_00006 |
| TC_UNIT_DOIP_00002 | DoIp Model - Channel Configuration | Unit | SWR_DOIP_00002 |
| TC_UNIT_DOIP_00003 | DoIP Model - Vehicle Announcement Handling | Unit | SWR_DOIP_00003 |
| TC_UNIT_DOIP_00004 | DoIP CLI - Command-Line Interface | Unit | SWR_DOIP_00004 |
| TC_UNIT_SOAD_00001 | SoAd Parser - XDM File Parsing and Validation | Unit | SWR_SOAD_00001, SWR_SOAD_00007 |
| TC_UNIT_SOAD_00002 | SoAd Model - Socket Connection Configuration | Unit | SWR_SOAD_00002 |
| TC_UNIT_SOAD_00003 | SoAd Model - PDU Route and Routing Group | Unit | SWR_SOAD_00003, SWR_SOAD_00004 |
| TC_UNIT_SOAD_00004 | SoAd CLI - Command-Line Interface | Unit | SWR_SOAD_00005 |
| TC_UNIT_SOMEIPTP_00001 | SomeIpTp Parser - XDM File Parsing and Validation | Unit | SWR_SOMEIPTP_00001, SWR_SOMEIPTP_00007 |
| TC_UNIT_SOMEIPTP_00002 | SomeIpTp Model - Channel Configuration | Unit | SWR_SOMEIPTP_00002 |
| TC_UNIT_SOMEIPTP_00003 | SomeIpTp Model - RxNSdu/TxNSdu Configuration | Unit | SWR_SOMEIPTP_00003, SWR_SOMEIPTP_00004 |
| TC_UNIT_SOMEIPTP_00004 | SomeIpTp CLI - Command-Line Interface | Unit | SWR_SOMEIPTP_00005 |
| TC_UNIT_TCPIP_00001 | TcpIp Parser - XDM File Parsing and Validation | Unit | SWR_TCPIP_00001, SWR_TCPIP_00006 |
| TC_UNIT_TCPIP_00002 | TcpIp Model - Controller Configuration | Unit | SWR_TCPIP_00002 |
| TC_UNIT_TCPIP_00003 | TcpIp CLI - Command-Line Interface | Unit | SWR_TCPIP_00003 |
| TC_UNIT_UDPNM_00001 | UdpNm Parser - XDM File Parsing and Validation | Unit | SWR_UDPNM_00001, SWR_UDPNM_00005 |
| TC_UNIT_UDPNM_00002 | UdpNm Model - Channel Configuration | Unit | SWR_UDPNM_00002 |
| TC_UNIT_UDPNM_00003 | UdpNm CLI - Command-Line Interface | Unit | SWR_UDPNM_00003 |
| TC_INT_ETHERNET_00001 | Ethernet Stack - End-to-End Integration Test | Integration | All Ethernet SWR requirements |
| TC_INT_ETHERNET_00002 | Ethernet Stack - Multi-Controller Configuration | Integration | SWR_ETHIF_00002, SWR_TCPIP_00002 |
| TC_INT_ETHERNET_00003 | Ethernet Stack - Socket and Routing Coordination | Integration | SWR_SOAD_00002-00004, SWR_SOMEIPTP_00002-00004 |
| TC_INT_ETHERNET_00004 | Ethernet Stack - DoIP Discovery and Communication | Integration | SWR_DOIP_00002-00003, SWR_ETHSM_00002 |
| TC_INT_ETHERNET_00005 | Ethernet Stack - Network State Management | Integration | SWR_ETHSM_00002, SWR_UDPNM_00002 |
| TC_INT_ETHERNET_00006 | Ethernet Stack - Error Recovery and Reporting | Integration | SWR_ETHIF_00009, SWR_ETHSM_00005, SWR_DOIP_00006, SWR_SOAD_00007, SWR_SOMEIPTP_00007, SWR_TCPIP_00006, SWR_UDPNM_00005 |

### System Modules Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_DET_00001 | Det Parser - XDM File Parsing and Validation | Unit | SWR_DET_00001, SWR_DET_00007 |
| TC_UNIT_DET_00002 | Det Model - Error Detection Configuration | Unit | SWR_DET_00002 |
| TC_UNIT_DET_00003 | Det Model - Error Hook Configuration | Unit | SWR_DET_00003 |
| TC_UNIT_DET_00004 | Det CLI - Command-Line Interface | Unit | SWR_DET_00004 |
| TC_UNIT_ECUM_00001 | EcuM Parser - XDM File Parsing and Validation | Unit | SWR_ECUM_00001, SWR_ECUM_00009 |
| TC_UNIT_ECUM_00002 | EcuM Model - State Machine Configuration | Unit | SWR_ECUM_00002 |
| TC_UNIT_ECUM_00003 | EcuM Model - Wakeup Source Configuration | Unit | SWR_ECUM_00003 |
| TC_UNIT_ECUM_00004 | EcuM Model - Startup and Shutdown Sequences | Unit | SWR_ECUM_00004, SWR_ECUM_00005 |
| TC_UNIT_ECUM_00005 | EcuM CLI - Command-Line Interface | Unit | SWR_ECUM_00006 |
| TC_UNIT_TM_00001 | Tm Parser - XDM File Parsing and Validation | Unit | SWR_TM_00001, SWR_TM_00006 |
| TC_UNIT_TM_00002 | Tm Model - Timing Constraint Configuration | Unit | SWR_TM_00002 |
| TC_UNIT_TM_00003 | Tm Model - Execution Budget Configuration | Unit | SWR_TM_00003 |
| TC_UNIT_TM_00004 | Tm CLI - Command-Line Interface | Unit | SWR_TM_00004 |
| TC_UNIT_PBCFGM_00001 | PbcfgM Parser - XDM File Parsing and Validation | Unit | SWR_PBCFGM_00001, SWR_PBCFGM_00006 |
| TC_UNIT_PBCFGM_00002 | PbcfgM Model - Configuration Block Parsing | Unit | SWR_PBCFGM_00002 |
| TC_UNIT_PBCFGM_00003 | PbcfgM CLI - Command-Line Interface | Unit | SWR_PBCFGM_00003 |
| TC_INT_DET_00001 | Det Module - End-to-End Integration Test | Integration | SWR_DET_00001-00007 |
| TC_INT_ECUM_00001 | EcuM Module - End-to-End Integration Test | Integration | SWR_ECUM_00001-00009 |
| TC_INT_TM_00001 | Tm Module - End-to-End Integration Test | Integration | SWR_TM_00001-00006 |
| TC_INT_PBCFGM_00001 | PbcfgM Module - End-to-End Integration Test | Integration | SWR_PBCFGM_00001-00006 |

### Crypto Stack Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_SECOC_00001 | SECOC Parser - XDM File Parsing and Validation | Unit | SWR_SECOC_00001, SWR_SECOC_00012, SWR_SECOC_00020 |
| TC_UNIT_SECOC_00002 | SECOC Model - Module Initialization | Unit | SWR_SECOC_00001 |
| TC_UNIT_SECOC_00003 | SECOC Model - SecOCGeneral Initialization | Unit | SWR_SECOC_00002 |
| TC_UNIT_SECOC_00004 | SECOC Model - DevErrorDetect Property | Unit | SWR_SECOC_00002 |
| TC_UNIT_SECOC_00005 | SECOC Model - Enabled Property | Unit | SWR_SECOC_00002 |
| TC_UNIT_SECOC_00006 | SECOC Model - Fluent Interface Pattern | Unit | SWR_SECOC_00006 |
| TC_UNIT_SECOC_00007 | SECOC Parser - Parse SecOCGeneral Container | Unit | SWR_SECOC_00002 |
| TC_UNIT_SECOC_00008 | SECOC Reporter - Excel Worksheet Generation | Unit | SWR_SECOC_00003, SWR_SECOC_00013 |
| TC_UNIT_SECOC_00009 | SECOC CLI - Command-Line Interface | Unit | SWR_SECOC_00004 |
| TC_UNIT_SECOC_00010 | SECOC Error Handling - Malformed XML | Unit | SWR_SECOC_00015, SWR_SECOC_00016 |
| TC_INT_SECOC_00001 | SECOC End-to-End Parser - Complete XDM File Parsing | Integration | SWR_SECOC_00001, SWR_SECOC_00005 |
| TC_INT_SECOC_00002 | SECOC Reporter Integration - Excel Report Generation | Integration | SWR_SECOC_00003, SWR_SECOC_00013 |
| TC_INT_SECOC_00003 | SECOC CLI Integration - Command-Line Execution | Integration | SWR_SECOC_00004 |
| TC_INT_SECOC_00004 | SECOC Error Handling Integration - Malformed XDM File | Integration | SWR_SECOC_00015, SWR_SECOC_00017 |
| TC_UNIT_CRYIF_00001 | CryIf Parser - XDM File Parsing and Validation | Unit | SWR_CRYIF_00001, SWR_CRYIF_00006 |
| TC_UNIT_CRYIF_00002 | CryIf Model - Primitive Configuration | Unit | SWR_CRYIF_00002 |
| TC_UNIT_CRYIF_00003 | CryIf Model - CSM References | Unit | SWR_CRYIF_00003 |
| TC_UNIT_CRYIF_00004 | CryIf Model - Key Management | Unit | SWR_CRYIF_00004 |
| TC_UNIT_CRYIF_00005 | CryIf CLI - Command-Line Interface | Unit | SWR_CRYIF_00005 |
| TC_INT_CRYPTO_00001 | Crypto Stack - End-to-End Integration Test | Integration | All Crypto SWR requirements |

### Diagnostics Stack Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_DEM_00001 | DEM Parser - XDM File Parsing and Validation | Unit | SWR_DEM_00001, SWR_DEM_00012, SWR_DEM_00020 |
| TC_UNIT_DEM_00002 | DEM Model - Module Initialization | Unit | SWR_DEM_00001 |
| TC_UNIT_DEM_00003 | DEM Model - DemGeneral Initialization | Unit | SWR_DEM_00002 |
| TC_UNIT_DEM_00004 | DEM Model - DemDevErrorDetect Property | Unit | SWR_DEM_00002 |
| TC_UNIT_DEM_00005 | DEM Model - DemEnabled Property | Unit | SWR_DEM_00002 |
| TC_UNIT_DEM_00006 | DEM Model - Fluent Interface Pattern | Unit | SWR_DEM_00006 |
| TC_UNIT_DEM_00007 | DEM Parser - Parse DemGeneral Container | Unit | SWR_DEM_00002 |
| TC_UNIT_DEM_00008 | DEM Reporter - Excel Worksheet Generation | Unit | SWR_DEM_00003, SWR_DEM_00013 |
| TC_UNIT_DEM_00009 | DEM CLI - Command-Line Interface | Unit | SWR_DEM_00004 |
| TC_UNIT_DEM_00010 | DEM Error Handling - Malformed XML | Unit | SWR_DEM_00015, SWR_DEM_00016 |
| TC_INT_DEM_00001 | DEM End-to-End Parser - Complete XDM File Parsing | Integration | SWR_DEM_00001, SWR_DEM_00005 |
| TC_INT_DEM_00002 | DEM Reporter Integration - Excel Report Generation | Integration | SWR_DEM_00003, SWR_DEM_00013 |
| TC_INT_DEM_00003 | DEM CLI Integration - Command-Line Execution | Integration | SWR_DEM_00004 |
| TC_INT_DEM_00004 | DEM Error Handling Integration - Malformed XDM File | Integration | SWR_DEM_00015, SWR_DEM_00017 |
| TC_UNIT_DCM_00001 | Dcm Parser - XDM File Parsing and Validation | Unit | SWR_DCM_00001, SWR_DCM_00010 |
| TC_UNIT_DCM_00002 | Dcm Model - DSID Configuration | Unit | SWR_DCM_00002 |
| TC_UNIT_DCM_00003 | Dcm Model - DID Configuration | Unit | SWR_DCM_00003 |
| TC_UNIT_DCM_00004 | Dcm CLI - Command-Line Interface | Unit | SWR_DCM_00004 |
| TC_UNIT_FIM_00001 | Fim Parser - XDM File Parsing and Validation | Unit | SWR_FIM_00001, SWR_FIM_00008 |
| TC_UNIT_FIM_00002 | Fim Model - Function Identifier Configuration | Unit | SWR_FIM_00002 |
| TC_UNIT_FIM_00003 | Fim Model - Inhibit Configuration | Unit | SWR_FIM_00003 |
| TC_UNIT_FIM_00004 | Fim CLI - Command-Line Interface | Unit | SWR_FIM_00004 |
| TC_UNIT_DLT_00001 | Dlt Parser - XDM File Parsing and Validation | Unit | SWR_DLT_00001, SWR_DLT_00006 |
| TC_UNIT_DLT_00002 | Dlt Model - Log Configuration | Unit | SWR_DLT_00002 |
| TC_UNIT_DLT_00003 | Dlt Model - Trace Configuration | Unit | SWR_DLT_00003 |
| TC_UNIT_DLT_00004 | Dlt CLI - Command-Line Interface | Unit | SWR_DLT_00004 |
| TC_INT_DIAG_00001 | Diagnostics Stack - End-to-End Integration Test | Integration | All Diagnostics SWR requirements |

### J1939 Stack Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_J1939_00001 | J1939Dcm Parser - XDM File Parsing and Validation | Unit | SWR_J1939DCM_00001 |
| TC_UNIT_J1939_00002 | J1939Dcm Model - Module Initialization | Unit | SWR_J1939DCM_00001 |
| TC_UNIT_J1939_00003 | J1939Dcm Model - J1939DcmGeneral Container | Unit | SWR_J1939DCM_00002, SWR_J1939DCM_00006 |
| TC_UNIT_J1939_00004 | J1939Dcm Parser - Parse J1939DcmGeneral Container | Unit | SWR_J1939DCM_00002 |
| TC_UNIT_J1939_00005 | J1939Nm Parser - XDM File Parsing and Validation | Unit | SWR_J1939NM_00001 |
| TC_UNIT_J1939_00006 | J1939Nm Model - Module Initialization and General Container | Unit | SWR_J1939NM_00001, SWR_J1939NM_00002 |
| TC_UNIT_J1939_00007 | J1939Rm Parser - XDM File Parsing and Validation | Unit | SWR_J1939RM_00001 |
| TC_UNIT_J1939_00008 | J1939Rm Model - Module Initialization and General Container | Unit | SWR_J1939RM_00001, SWR_J1939RM_00002 |
| TC_UNIT_J1939_00009 | J1939Tp Parser - XDM File Parsing and Validation | Unit | SWR_J1939TP_00001 |
| TC_UNIT_J1939_00010 | J1939Tp Model - Module Initialization and General Container | Unit | SWR_J1939TP_00001, SWR_J1939TP_00002 |
| TC_UNIT_J1939_00011 | J1939 CLI - Command-Line Interface | Unit | SWR_J1939DCM_00004, SWR_J1939NM_00004, SWR_J1939RM_00004, SWR_J1939TP_00004 |
| TC_INT_J1939_00001 | J1939Dcm End-to-End Parser - Complete XDM File Parsing | Integration | SWR_J1939DCM_00001, SWR_J1939DCM_00005 |
| TC_INT_J1939_00002 | J1939Nm End-to-End Parser - Complete XDM File Parsing | Integration | SWR_J1939NM_00001 |
| TC_INT_J1939_00003 | J1939Rm End-to-End Parser - Complete XDM File Parsing | Integration | SWR_J1939RM_00001 |
| TC_INT_J1939_00004 | J1939Tp End-to-End Parser - Complete XDM File Parsing | Integration | SWR_J1939TP_00001 |
| TC_INT_J1939_00005 | J1939 Reporter Integration - Excel Report Generation | Integration | SWR_J1939DCM_00003, SWR_J1939NM_00003, SWR_J1939RM_00003, SWR_J1939TP_00003 |
| TC_INT_J1939_00006 | J1939 CLI Integration - Command-Line Execution | Integration | SWR_J1939DCM_00004, SWR_J1939NM_00004, SWR_J1939RM_00004, SWR_J1939TP_00004 |

### Infrastructure Layers Tests

| Test Case ID | Title | Type | Requirements |
|--------------|-------|------|--------------|
| TC_UNIT_PARSER_00001 | Abstract Parser - XML Parsing and Namespace Handling | Unit | SWR_PARSER_00001, SWR_PARSER_00006 |
| TC_UNIT_PARSER_00002 | Abstract Parser - Value Reading Methods | Unit | SWR_PARSER_00002, SWR_PARSER_00007 |
| TC_UNIT_PARSER_00003 | Abstract Parser - Reference Reading Methods | Unit | SWR_PARSER_00003, SWR_PARSER_00008 |
| TC_UNIT_PARSER_00004 | Abstract Parser - Container Tag Finding | Unit | SWR_PARSER_00004 |
| TC_UNIT_PARSER_00005 | Abstract Parser - ENABLE Attribute Handling | Unit | SWR_PARSER_00005 |
| TC_UNIT_PARSER_00006 | EbParserFactory - Parser Type Determination | Unit | SWR_PARSER_00009 |
| TC_UNIT_PARSER_00007 | EbParserFactory - Module Registration | Unit | SWR_PARSER_00009 |
| TC_UNIT_PARSER_00008 | Parser Layer - Error Handling | Unit | SWR_PARSER_00010 |
| TC_UNIT_REPORTER_00001 | Excel Reporter - Workbook Creation | Unit | SWR_REPORTER_00001 |
| TC_UNIT_REPORTER_00002 | Excel Reporter - Worksheet Management | Unit | SWR_REPORTER_00002 |
| TC_UNIT_REPORTER_00003 | Excel Reporter - Cell Formatting | Unit | SWR_REPORTER_00003 |
| TC_UNIT_REPORTER_00004 | Excel Reporter - Auto-Width Formatting | Unit | SWR_REPORTER_00004 |
| TC_UNIT_REPORTER_00005 | Reporter Layer - Markdown Output | Unit | SWR_REPORTER_00005 |
| TC_UNIT_REPORTER_00006 | Reporter Layer - Error Handling | Unit | SWR_REPORTER_00009 |
| TC_UNIT_CLI_00001 | CLI Layer - Command Registration | Unit | SWR_CLI_00001 |
| TC_UNIT_CLI_00002 | CLI Layer - Argument Parsing | Unit | SWR_CLI_00002 |
| TC_UNIT_CLI_00003 | CLI Layer - Help Display | Unit | SWR_CLI_00003 |
| TC_UNIT_CLI_00004 | CLI Layer - Logging Configuration | Unit | SWR_CLI_00004 |
| TC_UNIT_CLI_00005 | CLI Layer - Error Messages | Unit | SWR_CLI_00005 |
| TC_UNIT_CLI_00006 | CLI Layer - Exit Code Handling | Unit | SWR_CLI_00006 |
| TC_INT_PARSER_00001 | Parser Layer - Multi-Module Parsing | Integration | SWR_PARSER_00001-00009 |
| TC_INT_REPORTER_00001 | Reporter Layer - Multi-Format Output | Integration | SWR_REPORTER_00001-00008 |
| TC_INT_CLI_00001 | CLI Layer - End-to-End Command Execution | Integration | SWR_CLI_00001-00009 |
| TC_INT_CROSS_00001 | Cross-Module - OS and RTE Integration | Integration | SWR_OS_00001-00011, SWR_RTE_00001-00007 |
| TC_INT_CROSS_00002 | Cross-Module - CAN Stack End-to-End | Integration | All CAN SWR requirements |
| TC_INT_CROSS_00003 | Cross-Module - Ethernet Stack End-to-End | Integration | All Ethernet SWR requirements |
| TC_INT_CROSS_00004 | Cross-Module - Multi-Module Excel Export | Integration | All module parser/reporter requirements |
| TC_INT_CROSS_00005 | Cross-Module - Full System Workflow | Integration | All SWR requirements |

## Reverse Traceability (Requirements to Tests)

### SWR_OS Requirements

| Requirement ID | Description | Test Cases |
|----------------|-------------|------------|
| SWR_OS_00001 | Parser Layer - XDM file parsing and validation | TC_UNIT_OS_00001, TC_INT_OS_00001 |
| SWR_OS_00002 | Task Management - Task extraction and modeling | TC_UNIT_OS_00002, TC_INT_OS_00001-00002 |
| SWR_OS_00003 | ISR Management - ISR extraction and modeling | TC_UNIT_OS_00003, TC_INT_OS_00001-00002 |
| SWR_OS_00004 | Schedule Tables - Schedule table extraction | TC_UNIT_OS_00004, TC_INT_OS_00001-00002 |
| SWR_OS_00005 | Counters - Counter extraction | TC_UNIT_OS_00005, TC_INT_OS_00001-00002 |
| SWR_OS_00006 | Applications - Application mapping | TC_UNIT_OS_00006, TC_INT_OS_00001-00002 |
| SWR_OS_00007 | Alarms - Alarm extraction | TC_UNIT_OS_00007, TC_INT_OS_00001-00002 |
| SWR_OS_00008 | Resources - Resource extraction | TC_UNIT_OS_00008, TC_INT_OS_00001-00002 |
| SWR_OS_00009 | Memory Protection - Memory protection extraction | TC_UNIT_OS_00009, TC_INT_OS_00002 |
| SWR_OS_00010 | Reporter Layer - Excel generation | TC_UNIT_OS_00010, TC_INT_OS_00001 |
| SWR_OS_00011 | CLI Interface - Command execution | TC_UNIT_OS_00011, TC_INT_OS_00001 |
| SWR_OS_00012 | Non-Functional - Efficient processing of 10MB files | TC_UNIT_OS_00001 |
| SWR_OS_00013 | Non-Functional - Excel performance | TC_UNIT_OS_00010, TC_INT_OS_00001 |
| SWR_OS_00014 | Non-Functional - O(1) lookup performance | TC_UNIT_OS_00002, TC_INT_OS_00001 |
| SWR_OS_00015 | Non-Functional - Malformed XML handling | TC_UNIT_OS_00012, TC_INT_OS_00003 |
| SWR_OS_00016 | Non-Functional - Missing optional elements | TC_UNIT_OS_00012, TC_INT_OS_00003 |
| SWR_OS_00017 | Non-Functional - Required element validation | TC_UNIT_OS_00013, TC_INT_OS_00003 |
| SWR_OS_00018 | Non-Functional - Path validation | TC_UNIT_OS_00013, TC_INT_OS_00003 |
| SWR_OS_00019 | Non-Functional - Memory efficiency | TC_INT_OS_00001 |
| SWR_OS_00020 | Non-Functional - Inherit from AbstractEbModelParser | TC_UNIT_OS_00001 |

### SWR_RTE Requirements

| Requirement ID | Description | Test Cases |
|----------------|-------------|------------|
| SWR_RTE_00001 | Parser Layer - XDM file parsing and validation | TC_UNIT_RTE_00001, TC_INT_RTE_00001-00003 |
| SWR_RTE_00002 | BSW Component Instance Extraction | TC_UNIT_RTE_00002, TC_INT_RTE_00001-00003 |
| SWR_RTE_00003 | SW Component Instance Extraction | TC_UNIT_RTE_00003, TC_INT_RTE_00001-00003 |
| SWR_RTE_00004 | Event to Task Mapping | TC_UNIT_RTE_00004, TC_INT_RTE_00001-00003 |
| SWR_RTE_00005 | AR 3.x Version Support | TC_UNIT_RTE_00005, TC_INT_RTE_00001 |
| SWR_RTE_00006 | AR 4.x Version Support | TC_UNIT_RTE_00006, TC_INT_RTE_00002 |
| SWR_RTE_00007 | Reporter Layer - Excel generation | TC_UNIT_RTE_00007, TC_INT_RTE_00001-00002 |
| SWR_RTE_00008 | Non-Functional - Efficient processing of 10MB files | TC_UNIT_RTE_00001 |
| SWR_RTE_00009 | Non-Functional - O(1) lookup performance | TC_UNIT_RTE_00002-00003, TC_INT_RTE_00001-00002 |
| SWR_RTE_00010 | Non-Functional - AR 3.x specific handling | TC_UNIT_RTE_00005, TC_INT_RTE_00001 |
| SWR_RTE_00011 | Non-Functional - AR 3.x validation | TC_UNIT_RTE_00005, TC_INT_RTE_00001 |
| SWR_RTE_00012 | Non-Functional - AR 4.x validation | TC_UNIT_RTE_00006, TC_INT_RTE_00002 |
| SWR_RTE_00013 | Non-Functional - Excel performance | TC_UNIT_RTE_00007, TC_INT_RTE_00001-00002 |
| SWR_RTE_00014 | CLI Interface - Command execution | TC_UNIT_RTE_00008, TC_INT_RTE_00001-00002 |
| SWR_RTE_00015 | Non-Functional - Error handling | TC_UNIT_RTE_00009-00010, TC_INT_RTE_00003 |

### SWR_SECOC Requirements

| Requirement ID | Description | Test Cases |
|----------------|-------------|------------|
| SWR_SECOC_00001 | Parser Layer - XDM file parsing and validation | TC_UNIT_SECOC_00001, TC_INT_SECOC_00001 |
| SWR_SECOC_00002 | SecOCGeneral Container | TC_UNIT_SECOC_00003-00004-00005-00006-00007 |
| SWR_SECOC_00003 | Reporter Layer - Excel generation | TC_UNIT_SECOC_00008, TC_INT_SECOC_00002 |
| SWR_SECOC_00004 | CLI Interface - Command execution | TC_UNIT_SECOC_00009, TC_INT_SECOC_00003 |
| SWR_SECOC_00005 | End-to-End Parser Workflow | TC_INT_SECOC_00001 |
| SWR_SECOC_00006 | Fluent Interface Pattern | TC_UNIT_SECOC_00006 |
| SWR_SECOC_00012 | Non-Functional - Efficient processing of 10MB files | TC_UNIT_SECOC_00001 |
| SWR_SECOC_00013 | Non-Functional - Excel performance | TC_UNIT_SECOC_00008, TC_INT_SECOC_00002 |
| SWR_SECOC_00015 | Non-Functional - Malformed XML error handling | TC_UNIT_SECOC_00010, TC_INT_SECOC_00004 |
| SWR_SECOC_00016 | Non-Functional - Missing optional elements handling | TC_UNIT_SECOC_00010 |
| SWR_SECOC_00017 | Non-Functional - Required element validation | TC_INT_SECOC_00004 |
| SWR_SECOC_00020 | Non-Functional - Inherit from AbstractEbModelParser | TC_UNIT_SECOC_00001 |

### SWR_DEM Requirements

| Requirement ID | Description | Test Cases |
|----------------|-------------|------------|
| SWR_DEM_00001 | Parser Layer - XDM file parsing and validation | TC_UNIT_DEM_00001, TC_INT_DEM_00001 |
| SWR_DEM_00002 | DemGeneral Container | TC_UNIT_DEM_00003-00004-00005-00006-00007 |
| SWR_DEM_00003 | Reporter Layer - Excel generation | TC_UNIT_DEM_00008, TC_INT_DEM_00002 |
| SWR_DEM_00004 | CLI Interface - Command execution | TC_UNIT_DEM_00009, TC_INT_DEM_00003 |
| SWR_DEM_00005 | End-to-End Parser Workflow | TC_INT_DEM_00001 |
| SWR_DEM_00006 | Fluent Interface Pattern | TC_UNIT_DEM_00006 |
| SWR_DEM_00012 | Non-Functional - Efficient processing of 10MB files | TC_UNIT_DEM_00001 |
| SWR_DEM_00013 | Non-Functional - Excel performance | TC_UNIT_DEM_00008, TC_INT_DEM_00002 |
| SWR_DEM_00015 | Non-Functional - Malformed XML error handling | TC_UNIT_DEM_00010, TC_INT_DEM_00004 |
| SWR_DEM_00016 | Non-Functional - Missing optional elements handling | TC_UNIT_DEM_00010 |
| SWR_DEM_00017 | Non-Functional - Required element validation | TC_INT_DEM_00004 |
| SWR_DEM_00020 | Non-Functional - Inherit from AbstractEbModelParser | TC_UNIT_DEM_00001 |

### SWR_J1939 Requirements

| Requirement ID | Description | Test Cases |
|----------------|-------------|------------|
| SWR_J1939DCM_00001 | J1939Dcm Parser Layer - XDM file parsing and validation | TC_UNIT_J1939_00001, TC_INT_J1939_00001 |
| SWR_J1939DCM_00002 | J1939DcmGeneral Container | TC_UNIT_J1939_00003-00004 |
| SWR_J1939DCM_00003 | J1939Dcm Reporter Layer - Excel generation | TC_INT_J1939_00005 |
| SWR_J1939DCM_00004 | J1939Dcm CLI Interface - Command execution | TC_UNIT_J1939_00011, TC_INT_J1939_00006 |
| SWR_J1939DCM_00005 | J1939Dcm End-to-End Parser Workflow | TC_INT_J1939_00001 |
| SWR_J1939DCM_00006 | J1939Dcm Fluent Interface Pattern | TC_UNIT_J1939_00003 |
| SWR_J1939NM_00001 | J1939Nm Parser Layer - XDM file parsing and validation | TC_UNIT_J1939_00005, TC_INT_J1939_00002 |
| SWR_J1939NM_00002 | J1939NmGeneral Container | TC_UNIT_J1939_00006 |
| SWR_J1939NM_00003 | J1939Nm Reporter Layer - Excel generation | TC_INT_J1939_00005 |
| SWR_J1939NM_00004 | J1939Nm CLI Interface - Command execution | TC_UNIT_J1939_00011, TC_INT_J1939_00006 |
| SWR_J1939RM_00001 | J1939Rm Parser Layer - XDM file parsing and validation | TC_UNIT_J1939_00007, TC_INT_J1939_00003 |
| SWR_J1939RM_00002 | J1939RmGeneral Container | TC_UNIT_J1939_00008 |
| SWR_J1939RM_00003 | J1939Rm Reporter Layer - Excel generation | TC_INT_J1939_00005 |
| SWR_J1939RM_00004 | J1939Rm CLI Interface - Command execution | TC_UNIT_J1939_00011, TC_INT_J1939_00006 |
| SWR_J1939TP_00001 | J1939Tp Parser Layer - XDM file parsing and validation | TC_UNIT_J1939_00009, TC_INT_J1939_00004 |
| SWR_J1939TP_00002 | J1939TpGeneral Container | TC_UNIT_J1939_00010 |
| SWR_J1939TP_00003 | J1939Tp Reporter Layer - Excel generation | TC_INT_J1939_00005 |
| SWR_J1939TP_00004 | J1939Tp CLI Interface - Command execution | TC_UNIT_J1939_00011, TC_INT_J1939_00006 |

## Document Control

| Field | Value |
|-------|-------|
| Document Title | py-eb-model Test Case Registry |
| Document ID | TC_REGISTRY_00001 |
| Version | 1.0 |
| Date | 2026-03-27 |
| Standard | ISO/IEC/IEEE 29119-3:2013 |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.1 | 2026-04-04 | Test Architect | Added SECOC, DEM, and J1939 stack modules; converted from docs/test_cases/ to ISO 29119-3 format |
| 1.0 | 2026-03-27 | Test Architect | Initial registry creation |