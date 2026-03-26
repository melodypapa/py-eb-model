# FrIf Module Software Requirements

## SWR_FRIF_00001: FrIf Module Parser

**Description**: The parser shall extract FrIf (FlexRay Interface) configuration from EB Tresos XDM files.

**Source Code**:
- Class: `FrIfXdmParser`
- File: `src/eb_model/parser/frif_xdm_parser.py`

**Verification**: Unit tests in `test_frif_xdm_parser.py`

## SWR_FRIF_00002: General Configuration Parsing

**Description**: The parser shall extract general FrIf configuration parameters.

**Source Code**:
- Method: `FrIfXdmParser.read_frif_general()`
- Class: `FrIfGeneral`
- File: `src/eb_model/models/frif_xdm.py`

**Verification**: Unit tests in `test_frif_xdm_parser.py`

## SWR_FRIF_00003: Controller Configuration Parsing

**Description**: The parser shall extract FlexRay controller configurations including MTU.

**Source Code**:
- Method: `FrIfXdmParser.read_frif_controllers()`
- Class: `FrIfController`
- File: `src/eb_model/models/frif_xdm.py`

**Verification**: Unit tests in `test_frif_xdm_parser.py`

## SWR_FRIF_00004: Cluster Configuration Parsing

**Description**: The parser shall extract FlexRay cluster configurations.

**Source Code**:
- Method: `FrIfXdmParser.read_frif_clusters()`
- Class: `FrIfCluster`
- File: `src/eb_model/models/frif_xdm.py`

## SWR_FRIF_00005: Excel Report Generation

**Description**: The reporter shall generate Excel output for FrIf configuration.

**Source Code**:
- Class: `FrIfXdmXlsWriter`
- File: `src/eb_model/reporter/excel_reporter/frif_xdm.py`

## SWR_FRIF_00006: CLI Entry Point

**Description**: The CLI entry point shall provide XDM to Excel conversion for FrIf.

**Source Code**:
- Module: `frif_xdm_2_xls_cli`
- File: `src/eb_model/cli/frif_xdm_2_xls_cli.py`