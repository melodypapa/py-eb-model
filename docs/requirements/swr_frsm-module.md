# FrSM Module Software Requirements

## SWR_FRSM_00001: FrSM Module Parser

**Description**: The parser shall extract FrSM (FlexRay State Manager) configuration from EB Tresos XDM files.

**Source Code**:
- Class: `FrSMXdmParser`
- File: `src/eb_model/parser/frsm_xdm_parser.py`

**Verification**: Unit tests

## SWR_FRSM_00002: General Configuration Parsing

**Description**: The parser shall extract general FrSM configuration parameters.

**Source Code**:
- Method: `FrSMXdmParser.read_frsm_general()`
- Class: `FrSMGeneral`
- File: `src/eb_model/models/frsm_xdm.py`

## SWR_FRSM_00003: Cluster Configuration Parsing

**Description**: The parser shall extract FrSM cluster configurations including timing and startup parameters.

**Source Code**:
- Method: `FrSMXdmParser.read_frsm_clusters()`
- Class: `FrSMCluster`, `FrSMClusterDemEventParameterRefs`
- File: `src/eb_model/models/frsm_xdm.py`

## SWR_FRSM_00004: Excel Report Generation

**Description**: The reporter shall generate Excel output for FrSM configuration.

**Source Code**:
- Class: `FrSMXdmXlsWriter`
- File: `src/eb_model/reporter/excel_reporter/frsm_xdm.py`

## SWR_FRSM_00005: CLI Entry Point

**Description**: The CLI entry point shall provide XDM to Excel conversion for FrSM.

**Source Code**:
- Module: `frsm_xdm_2_xls_cli`
- File: `src/eb_model/cli/frsm_xdm_2_xls_cli.py`