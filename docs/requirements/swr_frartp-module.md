# FrArTp Module Software Requirements

## SWR_FRARTP_00001: FrArTp Module Parser

**Description**: The parser shall extract FrArTp (FlexRay AR Transport Protocol) configuration from EB Tresos XDM files.

**Source Code**:
- Class: `FrArTpXdmParser`
- File: `src/eb_model/parser/frartp_xdm_parser.py`

**Verification**: Unit tests

## SWR_FRARTP_00002: General Configuration Parsing

**Description**: The parser shall extract general FrArTp configuration parameters.

**Source Code**:
- Method: `FrArTpXdmParser.read_frartp_general()`
- Class: `FrArTpGeneral`
- File: `src/eb_model/models/frartp_xdm.py`

## SWR_FRARTP_00003: Channel Configuration Parsing

**Description**: The parser shall extract FrArTp channel configurations.

**Source Code**:
- Method: `FrArTpXdmParser.read_frartp_channels()`
- Class: `FrArTpChannel`
- File: `src/eb_model/models/frartp_xdm.py`

## SWR_FRARTP_00004: Connection Configuration Parsing

**Description**: The parser shall extract FrArTp connection configurations.

**Source Code**:
- Method: `FrArTpXdmParser.read_frartp_connections()`
- Class: `FrArTpConnection`, `FrArTpRxSdu`, `FrArTpTxSdu`
- File: `src/eb_model/models/frartp_xdm.py`

## SWR_FRARTP_00005: PDU Configuration Parsing

**Description**: The parser shall extract FrArTp PDU configurations.

**Source Code**:
- Method: `FrArTpXdmParser.read_frartp_pdus()`
- Class: `FrArTpPdu`
- File: `src/eb_model/models/frartp_xdm.py`

## SWR_FRARTP_00006: Excel Report Generation

**Description**: The reporter shall generate Excel output for FrArTp configuration.

**Source Code**:
- Class: `FrArTpXdmXlsWriter`
- File: `src/eb_model/reporter/excel_reporter/frartp_xdm.py`

## SWR_FRARTP_00007: CLI Entry Point

**Description**: The CLI entry point shall provide XDM to Excel conversion for FrArTp.

**Source Code**:
- Module: `frartp_xdm_2_xls_cli`
- File: `src/eb_model/cli/frartp_xdm_2_xls_cli.py`