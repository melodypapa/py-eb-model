# EthSM Module Software Requirements

## SWR_ETHSM_00001: EthSM Module Parser

**Description**: The parser shall extract EthSM (Ethernet State Manager) configuration from EB Tresos XDM files.

**Source Code**:
- Class: `EthSMXdmParser`
- File: `src/eb_model/parser/ethsm_xdm_parser.py`

**Verification**: Unit tests

## SWR_ETHSM_00002: General Configuration Parsing

**Description**: The parser shall extract general EthSM configuration parameters.

**Source Code**:
- Method: `EthSMXdmParser.read_ethsm_general()`
- Class: `EthSMGeneral`
- File: `src/eb_model/models/ethsm_xdm.py`

## SWR_ETHSM_00003: Network Configuration Parsing

**Description**: The parser shall extract Ethernet network configurations including controller and ComM references.

**Source Code**:
- Method: `EthSMXdmParser.read_ethsm_networks()`
- Class: `EthSMNetwork`, `EthSMDemEventParameterRefs`
- File: `src/eb_model/models/ethsm_xdm.py`

## SWR_ETHSM_00004: Excel Report Generation

**Description**: The reporter shall generate Excel output for EthSM configuration.

**Source Code**:
- Class: `EthSMXdmXlsWriter`
- File: `src/eb_model/reporter/excel_reporter/ethsm_xdm.py`

## SWR_ETHSM_00005: CLI Entry Point

**Description**: The CLI entry point shall provide XDM to Excel conversion for EthSM.

**Source Code**:
- Module: `ethsm_xdm_2_xls_cli`
- File: `src/eb_model/cli/ethsm_xdm_2_xls_cli.py`