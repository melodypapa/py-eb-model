# DoIP Module Software Requirements

## SWR_DOIP_00001: DoIP Module Parser

**Description**: The parser shall extract DoIP (Diagnostics over IP) configuration from EB Tresos XDM files.

**Source Code**:
- Class: `DoIPXdmParser`
- File: `src/eb_model/parser/doip_xdm_parser.py`

**Verification**: Unit tests

## SWR_DOIP_00002: General Configuration Parsing

**Description**: The parser shall extract general DoIP configuration parameters.

**Source Code**:
- Method: `DoIPXdmParser.read_doip_general()`
- Class: `DoIPGeneral`
- File: `src/eb_model/models/doip_xdm.py`

## SWR_DOIP_00003: Channel Configuration Parsing

**Description**: The parser shall extract DoIP channel configurations.

**Source Code**:
- Method: `DoIPXdmParser.read_doip_channels()`
- Method: `DoIPXdmParser.read_doip_custom_channels()`
- Class: `DoIPChannel`, `DoIPPduRRxPdu`, `DoIPPduRTxPdu`
- File: `src/eb_model/models/doip_xdm.py`

## SWR_DOIP_00004: Connection Configuration Parsing

**Description**: The parser shall extract DoIP connection configurations including TCP/UDP and vehicle announcement.

**Source Code**:
- Method: `DoIPXdmParser.read_doip_connections()`
- Class: `DoIPConnections`, `DoIPTcpConnection`, `DoIPUdpConnection`, `DoIPUdpVehicleAnnouncement`
- File: `src/eb_model/models/doip_xdm.py`

## SWR_DOIP_00005: Excel Report Generation

**Description**: The reporter shall generate Excel output for DoIP configuration.

**Source Code**:
- Class: `DoIPXdmXlsWriter`
- File: `src/eb_model/reporter/excel_reporter/doip_xdm.py`

## SWR_DOIP_00006: CLI Entry Point

**Description**: The CLI entry point shall provide XDM to Excel conversion for DoIP.

**Source Code**:
- Module: `doip_xdm_2_xls_cli`
- File: `src/eb_model/cli/doip_xdm_2_xls_cli.py`