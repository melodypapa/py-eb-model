# UdpNm Module Software Requirements

## SWR_UDPNM_00001: UdpNm Module Parser

**Description**: The parser shall extract UdpNm (UDP Network Management) configuration from EB Tresos XDM files.

**Source Code**:
- Class: `UdpNmXdmParser`
- File: `src/eb_model/parser/udpnm_xdm_parser.py`

**Verification**: Unit tests

## SWR_UDPNM_00002: General Configuration Parsing

**Description**: The parser shall extract general UdpNm configuration parameters.

**Source Code**:
- Method: `UdpNmXdmParser.read_udpnm_general()`
- Class: `UdpNmGeneral`
- File: `src/eb_model/models/udpnm_xdm.py`

## SWR_UDPNM_00003: Channel Configuration Parsing

**Description**: The parser shall extract UdpNm channel configurations including RX/TX PDU settings.

**Source Code**:
- Method: `UdpNmXdmParser.read_udpnm_channels()`
- Class: `UdpNmChannel`, `UdpNmChannelIdentifiers`, `UdpNmRxPdu`, `UdpNmTxPdu`
- File: `src/eb_model/models/udpnm_xdm.py`

## SWR_UDPNM_00004: Excel Report Generation

**Description**: The reporter shall generate Excel output for UdpNm configuration.

**Source Code**:
- Class: `UdpNmXdmXlsWriter`
- File: `src/eb_model/reporter/excel_reporter/udpnm_xdm.py`

## SWR_UDPNM_00005: CLI Entry Point

**Description**: The CLI entry point shall provide XDM to Excel conversion for UdpNm.

**Source Code**:
- Module: `udpnm_xdm_2_xls_cli`
- File: `src/eb_model/cli/udpnm_xdm_2_xls_cli.py`