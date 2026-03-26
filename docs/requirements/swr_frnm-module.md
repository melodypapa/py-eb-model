# FrNm Module Software Requirements

## SWR_FRNM_00001: FrNm Module Parser

**Description**: The parser shall extract FrNm (FlexRay Network Management) configuration from EB Tresos XDM files.

**Source Code**:
- Class: `FrNmXdmParser`
- File: `src/eb_model/parser/frnm_xdm_parser.py`

**Verification**: Unit tests

## SWR_FRNM_00002: General Configuration Parsing

**Description**: The parser shall extract general FrNm configuration parameters.

**Source Code**:
- Method: `FrNmXdmParser.read_frnm_general()`
- Class: `FrNmGeneral`
- File: `src/eb_model/models/frnm_xdm.py`

## SWR_FRNM_00003: Channel Configuration Parsing

**Description**: The parser shall extract FrNm channel configurations including RX/TX PDU settings.

**Source Code**:
- Method: `FrNmXdmParser.read_frnm_channels()`
- Class: `FrNmChannel`, `FrNmChannelIdentifiers`, `FrNmRxPdu`, `FrNmTxPdu`
- File: `src/eb_model/models/frnm_xdm.py`

## SWR_FRNM_00004: Excel Report Generation

**Description**: The reporter shall generate Excel output for FrNm configuration.

**Source Code**:
- Class: `FrNmXdmXlsWriter`
- File: `src/eb_model/reporter/excel_reporter/frnm_xdm.py`

## SWR_FRNM_00005: CLI Entry Point

**Description**: The CLI entry point shall provide XDM to Excel conversion for FrNm.

**Source Code**:
- Module: `frnm_xdm_2_xls_cli`
- File: `src/eb_model/cli/frnm_xdm_2_xls_cli.py`