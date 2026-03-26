# TcpIp Module Software Requirements

## SWR_TCPIP_00001: TcpIp Module Parser

**Description**: The parser shall extract TcpIp (TCP/IP Stack) configuration from EB Tresos XDM files.

**Source Code**:
- Class: `TcpIpXdmParser`
- File: `src/eb_model/parser/tcpip_xdm_parser.py`

**Verification**: Unit tests

## SWR_TCPIP_00002: General Configuration Parsing

**Description**: The parser shall extract general TcpIp configuration parameters.

**Source Code**:
- Method: `TcpIpXdmParser.read_tcpip_general()`
- Class: `TcpIpGeneral`
- File: `src/eb_model/models/tcpip_xdm.py`

## SWR_TCPIP_00003: Controller Configuration Parsing

**Description**: The parser shall extract TCP/IP controller configurations including IPv4/IPv6 and offload settings.

**Source Code**:
- Method: `TcpIpXdmParser.read_tcpip_ctrls()`
- Class: `TcpIpCtrl`, `TcpIpIpV4Ctrl`, `TcpIpIpV6Ctrl`, `TcpIpOffloadChecksum`
- File: `src/eb_model/models/tcpip_xdm.py`

## SWR_TCPIP_00004: Local Address Configuration Parsing

**Description**: The parser shall extract local IP address configurations.

**Source Code**:
- Method: `TcpIpXdmParser.read_tcpip_local_addrs()`
- Class: `TcpIpLocalAddr`
- File: `src/eb_model/models/tcpip_xdm.py`

## SWR_TCPIP_00005: Excel Report Generation

**Description**: The reporter shall generate Excel output for TcpIp configuration.

**Source Code**:
- Class: `TcpIpXdmXlsWriter`
- File: `src/eb_model/reporter/excel_reporter/tcpip_xdm.py`

## SWR_TCPIP_00006: CLI Entry Point

**Description**: The CLI entry point shall provide XDM to Excel conversion for TcpIp.

**Source Code**:
- Module: `tcpip_xdm_2_xls_cli`
- File: `src/eb_model/cli/tcpip_xdm_2_xls_cli.py`