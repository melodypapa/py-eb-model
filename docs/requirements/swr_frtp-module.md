# FrTp Module Software Requirements

## SWR_FRTP_00001: FrTp Module Parser

**Description**: The parser shall extract FrTp (FlexRay Transport Protocol) configuration from EB Tresos XDM files.

**Source Code**:
- Class: `FrTpXdmParser`
- File: `src/eb_model/parser/frtp_xdm_parser.py`

**Verification**: Unit tests

## SWR_FRTP_00002: General Configuration Parsing

**Description**: The parser shall extract general FrTp configuration parameters.

**Source Code**:
- Method: `FrTpXdmParser.read_frtp_general()`
- Class: `FrTpGeneral`
- File: `src/eb_model/models/frtp_xdm.py`

## SWR_FRTP_00003: Connection Configuration Parsing

**Description**: The parser shall extract FrTp connection configurations.

**Source Code**:
- Method: `FrTpXdmParser.read_frtp_connections()`
- Class: `FrTpConnection`, `FrTpConnectionControl`
- File: `src/eb_model/models/frtp_xdm.py`

## SWR_FRTP_00004: RxSdu/TxSdu Configuration Parsing

**Description**: The parser shall extract FrTp receive/transmit SDU configurations.

**Source Code**:
- Method: `FrTpXdmParser.read_frtp_rx_sdu()`
- Method: `FrTpXdmParser.read_frtp_tx_sdu()`
- Class: `FrTpRxSdu`, `FrTpTxSdu`
- File: `src/eb_model/models/frtp_xdm.py`

## SWR_FRTP_00005: Connection Limit Configuration Parsing

**Description**: The parser shall extract FrTp connection limit configuration.

**Source Code**:
- Method: `FrTpXdmParser.read_frtp_connection_limit_config()`
- Class: `FrTpConnectionLimitConfig`
- File: `src/eb_model/models/frtp_xdm.py`

## SWR_FRTP_00006: Excel Report Generation

**Description**: The reporter shall generate Excel output for FrTp configuration.

**Source Code**:
- Class: `FrTpXdmXlsWriter`
- File: `src/eb_model/reporter/excel_reporter/frtp_xdm.py`

## SWR_FRTP_00007: CLI Entry Point

**Description**: The CLI entry point shall provide XDM to Excel conversion for FrTp.

**Source Code**:
- Module: `frtp_xdm_2_xls_cli`
- File: `src/eb_model/cli/frtp_xdm_2_xls_cli.py`