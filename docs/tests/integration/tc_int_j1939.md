# J1939 Module Integration Test Cases

This document contains all integration test cases for the J1939 modules (J1939Dcm, J1939Nm, J1939Rm, J1939Tp) following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_INT_J1939_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_J1939_00001 |
| Title | J1939Dcm End-to-End Parser - Complete XDM File Parsing |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the J1939Dcm parser can parse a complete J1939Dcm XDM file with all containers, creating all model elements with correct values and establishing proper relationships.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid J1939Dcm.xdm file with complete configuration is available |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/J1939Dcm_complete.xdm` | Complete J1939Dcm XDM file |
| Expected Containers | J1939DcmGeneral, J1939DcmRxPduCm, J1939DcmTxPduCm | All expected containers |
| Expected Properties | J1939DcmDevErrorDetect, J1939DcmEnabled, PduId, Address, etc. | All expected properties |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create J1939DcmXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with complete J1939Dcm.xdm file | File parses without errors |
| 3 | Verify J1939DcmGeneral container is created | Container exists with correct name |
| 4 | Verify J1939DcmGeneral properties are correct | DevErrorDetect and Enabled match file |
| 5 | Verify J1939DcmRxPduCm containers are created | All RX PDUs from file are present |
| 6 | Verify J1939DcmTxPduCm containers are created | All TX PDUs from file are present |
| 7 | Verify parent-child relationships | All containers have correct parent references |
| 8 | Verify model element count | Total elements count matches file contents |
| 9 | Verify no parsing errors occurred | Parser completes without exceptions |

## Expected Results

- All expected containers are created from the XDM file
- All property values match the XDM file contents
- Parent-child relationships are correctly established
- No duplicate elements are created
- Model element count matches expected number of containers
- Parser completes successfully without errors

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Parsed J1939Dcm model remains in memory for verification |
| 2 | No partial or incomplete model objects exist |
| 3 | EBModel singleton contains updated J1939Dcm module |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939DCM_00001 | Parser Layer - Complete XDM file parsing | Covered |
| SWR_J1939DCM_00005 | End-to-End Parser Workflow | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |
| Design Document | ../requirements/overview.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_INT_J1939_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_J1939_00002 |
| Title | J1939Nm End-to-End Parser - Complete XDM File Parsing |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the J1939Nm parser can parse a complete J1939Nm XDM file with all containers, creating all model elements with correct values.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid J1939Nm.xdm file with complete configuration is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/J1939Nm_complete.xdm` | Complete J1939Nm XDM file |
| Expected Containers | J1939NmGeneral, J1939NmNode | All expected containers |
| Expected Properties | J1939NmDevErrorDetect, J1939NmEnabled, NodeAddress | All expected properties |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create J1939NmXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with complete J1939Nm.xdm file | File parses without errors |
| 3 | Verify J1939NmGeneral container is created | Container exists with correct name |
| 4 | Verify J1939NmGeneral properties are correct | Properties match file |
| 5 | Verify J1939NmNode containers are created | All nodes from file are present |
| 6 | Verify parent-child relationships | All containers have correct parent references |

## Expected Results

- All expected containers are created from the XDM file
- All property values match the XDM file contents
- Parent-child relationships are correctly established

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Parsed J1939Nm model remains in memory for verification |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939NM_00001 | Parser Layer - Complete XDM file parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_INT_J1939_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_J1939_00003 |
| Title | J1939Rm End-to-End Parser - Complete XDM File Parsing |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the J1939Rm parser can parse a complete J1939Rm XDM file with all containers, creating all model elements with correct values.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid J1939Rm.xdm file with complete configuration is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/J1939Rm_complete.xdm` | Complete J1939Rm XDM file |
| Expected Containers | J1939RmGeneral, J1939RmRequestRx, J1939RmRequestTx | All expected containers |
| Expected Properties | J1939RmDevErrorDetect, J1939RmEnabled, Pgn, etc. | All expected properties |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create J1939RmXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with complete J1939Rm.xdm file | File parses without errors |
| 3 | Verify J1939RmGeneral container is created | Container exists with correct name |
| 4 | Verify J1939RmGeneral properties are correct | Properties match file |
| 5 | Verify J1939RmRequestRx containers are created | All RX requests from file are present |
| 6 | Verify J1939RmRequestTx containers are created | All TX requests from file are present |

## Expected Results

- All expected containers are created from the XDM file
- All property values match the XDM file contents

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Parsed J1939Rm model remains in memory for verification |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939RM_00001 | Parser Layer - Complete XDM file parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_INT_J1939_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_J1939_00004 |
| Title | J1939Tp End-to-End Parser - Complete XDM File Parsing |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the J1939Tp parser can parse a complete J1939Tp XDM file with all containers, creating all model elements with correct values.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Valid J1939Tp.xdm file with complete configuration is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/J1939Tp_complete.xdm` | Complete J1939Tp XDM file |
| Expected Containers | J1939TpGeneral, J1939TpRx, J1939TpTx | All expected containers |
| Expected Properties | J1939TpDevErrorDetect, J1939TpEnabled, Pgn, etc. | All expected properties |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create J1939TpXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with complete J1939Tp.xdm file | File parses without errors |
| 3 | Verify J1939TpGeneral container is created | Container exists with correct name |
| 4 | Verify J1939TpGeneral properties are correct | Properties match file |
| 5 | Verify J1939TpRx containers are created | All RX TP from file are present |
| 6 | Verify J1939TpTx containers are created | All TX TP from file are present |

## Expected Results

- All expected containers are created from the XDM file
- All property values match the XDM file contents

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Parsed J1939Tp model remains in memory for verification |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939TP_00001 | Parser Layer - Complete XDM file parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_INT_J1939_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_J1939_00005 |
| Title | J1939 Reporter Integration - Excel Report Generation |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the J1939 reporters can generate complete Excel reports from parsed J1939 models, including all worksheets with correct data and formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | Parsed J1939 models are available |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input Models | Parsed J1939Dcm, J1939Nm, J1939Rm, J1939Tp models | Complete J1939 configurations |
| Output File Paths | J1939Dcm_integration_report.xlsx, etc. | Generated Excel file paths |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create J1939DcmXdmXlsWriter instance | Writer initialized successfully |
| 2 | Call write() with output path | Excel file generated successfully |
| 3 | Verify J1939Dcm report is valid | File can be opened and read |
| 4 | Create J1939NmXdmXlsWriter instance | Writer initialized successfully |
| 5 | Call write() with output path | Excel file generated successfully |
| 6 | Verify J1939Nm report is valid | File can be opened and read |
| 7 | Create J1939RmXdmXlsWriter instance | Writer initialized successfully |
| 8 | Call write() with output path | Excel file generated successfully |
| 9 | Verify J1939Rm report is valid | File can be opened and read |
| 10 | Create J1939TpXdmXlsWriter instance | Writer initialized successfully |
| 11 | Call write() with output path | Excel file generated successfully |
| 12 | Verify J1939Tp report is valid | File can be opened and read |

## Expected Results

- All Excel files are created successfully
- All files are valid and can be opened
- All expected worksheets are present in each file
- All data values match the parsed models
- Formatting is applied correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel files persist for review |
| 2 | Parsed models remain unchanged |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939DCM_00003 | Reporter Layer - J1939Dcm Excel report generation | Covered |
| SWR_J1939NM_00003 | Reporter Layer - J1939Nm Excel report generation | Covered |
| SWR_J1939RM_00003 | Reporter Layer - J1939Rm Excel report generation | Covered |
| SWR_J1939TP_00003 | Reporter Layer - J1939Tp Excel report generation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_INT_J1939_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_J1939_00006 |
| Title | J1939 CLI Integration - Command-Line Execution |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the J1939 CLI commands execute end-to-end, from command-line parsing through XDM parsing to Excel report generation.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI entry points are registered |
| 3 | Test XDM files are available |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Commands | j1939dcm-xdm-xlsx, j1939nm-xdm-xlsx, j1939rm-xdm-xlsx, j1939tp-xdm-xlsx | All J1939 CLI commands |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute j1939dcm-xdm-xlsx command | Command completes successfully |
| 2 | Verify exit code is 0 | Exit code indicates success |
| 3 | Verify output file exists | File created at specified path |
| 4 | Execute j1939nm-xdm-xlsx command | Command completes successfully |
| 5 | Verify exit code is 0 | Exit code indicates success |
| 6 | Verify output file exists | File created at specified path |
| 7 | Execute j1939rm-xdm-xlsx command | Command completes successfully |
| 8 | Verify exit code is 0 | Exit code indicates success |
| 9 | Verify output file exists | File created at specified path |
| 10 | Execute j1939tp-xdm-xlsx command | Command completes successfully |
| 11 | Verify exit code is 0 | Exit code indicates success |
| 12 | Verify output file exists | File created at specified path |

## Expected Results

- All CLI commands execute successfully
- Excel files are generated with correct contents
- Exit codes are appropriate (0 for success)
- No orphaned processes remain

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Generated Excel files persist for review |
| 2 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939DCM_00004 | CLI Interface - J1939Dcm command execution | Covered |
| SWR_J1939NM_00004 | CLI Interface - J1939Nm command execution | Covered |
| SWR_J1939RM_00004 | CLI Interface - J1939Rm command execution | Covered |
| SWR_J1939TP_00004 | CLI Interface - J1939Tp command execution | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

**Document End**