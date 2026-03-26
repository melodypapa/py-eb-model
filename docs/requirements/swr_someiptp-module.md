# SomeIpTp Module Software Requirements

## SWR_SOMEIPTP_00001: SomeIpTp Module Parser

**Description**: The parser shall extract SomeIpTp (SOME/IP Transport Protocol) configuration from EB Tresos XDM files.

**Source Code**:
- Class: `SomeIpTpXdmParser`
- File: `src/eb_model/parser/someiptp_xdm_parser.py`

**Verification**: Unit tests

## SWR_SOMEIPTP_00002: General Configuration Parsing

**Description**: The parser shall extract general SomeIpTp configuration parameters.

**Source Code**:
- Method: `SomeIpTpXdmParser.read_someiptp_general()`
- Class: `SomeIpTpGeneral`
- File: `src/eb_model/models/someiptp_xdm.py`

## SWR_SOMEIPTP_00003: Channel Configuration Parsing

**Description**: The parser shall extract SomeIpTp channel configurations.

**Source Code**:
- Method: `SomeIpTpXdmParser.read_someiptp_channels()`
- Class: `SomeIpTpChannel`
- File: `src/eb_model/models/someiptp_xdm.py`

## SWR_SOMEIPTP_00004: RxNSdu Configuration Parsing

**Description**: The parser shall extract SomeIpTp receive NSDU configurations.

**Source Code**:
- Method: `SomeIpTpXdmParser.read_someiptp_rx_nsdus()`
- Class: `SomeIpTpRxNSdu`, `SomeIpTpRxNPdu`
- File: `src/eb_model/models/someiptp_xdm.py`

## SWR_SOMEIPTP_00005: TxNSdu Configuration Parsing

**Description**: The parser shall extract SomeIpTp transmit NSDU configurations.

**Source Code**:
- Method: `SomeIpTpXdmParser.read_someiptp_tx_nsdus()`
- Class: `SomeIpTpTxNSdu`, `SomeIpTpTxNPdu`
- File: `src/eb_model/models/someiptp_xdm.py`

## SWR_SOMEIPTP_00006: Excel Report Generation

**Description**: The reporter shall generate Excel output for SomeIpTp configuration.

**Source Code**:
- Class: `SomeIpTpXdmXlsWriter`
- File: `src/eb_model/reporter/excel_reporter/someiptp_xdm.py`

## SWR_SOMEIPTP_00007: CLI Entry Point

**Description**: The CLI entry point shall provide XDM to Excel conversion for SomeIpTp.

**Source Code**:
- Module: `someiptp_xdm_2_xls_cli`
- File: `src/eb_model/cli/someiptp_xdm_2_xls_cli.py`