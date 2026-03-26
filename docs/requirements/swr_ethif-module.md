# EthIf Module Software Requirements

## SWR_ETHIF_00001: EthIf Module Parser

**Description**: The parser shall extract EthIf (Ethernet Interface) configuration from EB Tresos XDM files.

**Source Code**:
- Class: `EthIfXdmParser`
- File: `src/eb_model/parser/ethif_xdm_parser.py`

**Verification**: Unit tests in `test_ethif_xdm_parser.py`

## SWR_ETHIF_00002: General Configuration Parsing

**Description**: The parser shall extract general EthIf configuration parameters.

**Source Code**:
- Method: `EthIfXdmParser.read_ethif_general()`
- Class: `EthIfGeneral`
- File: `src/eb_model/models/ethif_xdm.py`

**Verification**: Unit tests in `test_ethif_xdm_parser.py`

## SWR_ETHIF_00003: Controller Configuration Parsing

**Description**: The parser shall extract Ethernet controller configurations including MTU, max buffers, and transceiver references.

**Source Code**:
- Method: `EthIfXdmParser.read_ethif_controllers()`
- Class: `EthIfController`
- File: `src/eb_model/models/ethif_xdm.py`

**Verification**: Unit tests in `test_ethif_xdm_parser.py`

## SWR_ETHIF_00004: Physical Controller Configuration Parsing

**Description**: The parser shall extract physical controller configurations.

**Source Code**:
- Method: `EthIfXdmParser.read_ethif_phys_controllers()`
- Class: `EthIfPhysController`
- File: `src/eb_model/models/ethif_xdm.py`

## SWR_ETHIF_00005: Switch Configuration Parsing

**Description**: The parser shall extract Ethernet switch configurations.

**Source Code**:
- Method: `EthIfXdmParser.read_ethif_switches()`
- Class: `EthIfSwitch`
- File: `src/eb_model/models/ethif_xdm.py`

## SWR_ETHIF_00006: Transceiver Configuration Parsing

**Description**: The parser shall extract Ethernet transceiver configurations.

**Source Code**:
- Method: `EthIfXdmParser.read_ethif_transceivers()`
- Class: `EthIfTransceiver`
- File: `src/eb_model/models/ethif_xdm.py`

## SWR_ETHIF_00007: RX/TX Indication Configuration Parsing

**Description**: The parser shall extract RX and TX indication FIFO configurations.

**Source Code**:
- Method: `EthIfXdmParser.read_ethif_rx_indication_configs()`
- Method: `EthIfXdmParser.read_ethif_tx_confirmation_configs()`
- Class: `EthIfRxIndicationConfig`, `EthIfTxConfirmationConfig`
- File: `src/eb_model/models/ethif_xdm.py`

## SWR_ETHIF_00008: Excel Report Generation

**Description**: The reporter shall generate Excel output for EthIf configuration.

**Source Code**:
- Class: `EthIfXdmXlsWriter`
- File: `src/eb_model/reporter/excel_reporter/ethif_xdm.py`

## SWR_ETHIF_00009: CLI Entry Point

**Description**: The CLI entry point shall provide XDM to Excel conversion for EthIf.

**Source Code**:
- Module: `ethif_xdm_2_xls_cli`
- File: `src/eb_model/cli/ethif_xdm_2_xls_cli.py`