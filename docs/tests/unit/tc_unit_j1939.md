# J1939 Module Unit Test Cases

This document contains all unit test cases for the J1939 modules (J1939Dcm, J1939Nm, J1939Rm, J1939Tp) following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_J1939_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_J1939_00001 |
| Title | J1939Dcm Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the J1939Dcm parser correctly extracts XML namespace definitions from EB Tresos XDM files, validates the module name, extracts AUTOSAR/software version information, and properly initializes the parser.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Test XDM file (valid J1939Dcm.xdm) is available at known location |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/J1939Dcm_valid.xdm` | Valid J1939Dcm XDM file for testing |
| Module Name | "J1939Dcm" | Expected root module name |
| AUTOSAR Version | "4.3.0" | Example AUTOSAR version |
| Software Version | "1.2.3" | Example software version |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create J1939DcmXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with valid J1939Dcm.xdm file | File parses without errors |
| 3 | Verify namespace map is populated | nsmap contains namespace definitions |
| 4 | Verify module name validation | Module "J1939Dcm" is accepted, others raise ValueError |
| 5 | Extract AUTOSAR version | Returns correct AUTOSAR version string |
| 6 | Extract software version | Returns correct software version string |

## Expected Results

- Namespace map contains namespace definitions
- Module name "J1939Dcm" is validated successfully
- AUTOSAR version matches expected value from file
- Software version matches expected value from file

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No temporary files created during test |
| 2 | Parser instance can be garbage collected |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939DCM_00001 | Parser Layer - XDM file parsing and validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_J1939_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_J1939_00002 |
| Title | J1939Dcm Model - Module Initialization |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the J1939Dcm module initializes with correct name and parent reference, inheriting all Module properties properly.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Module Name | "J1939Dcm" | Expected module name |
| Parent Type | EcucParamConfContainerDef | Parent container type |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create EBModel instance | EBModel initialized successfully |
| 2 | Create EcucParamConfContainerDef parent | Parent container created |
| 3 | Instantiate J1939Dcm with parent | J1939Dcm instance created with correct name |
| 4 | Verify getName() returns "J1939Dcm" | Name is correct |
| 5 | Verify parent reference is correct | Parent points to correct container |

## Expected Results

- J1939Dcm instance is created successfully
- getName() returns "J1939Dcm"
- Parent reference points to the correct EcucParamConfContainerDef

## Post-conditions

| # | Description |
|---|-------------|
| 1 | J1939Dcm object remains in memory for verification |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939DCM_00001 | Module Initialization | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_J1939_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_J1939_00003 |
| Title | J1939Dcm Model - J1939DcmGeneral Container |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the J1939DcmGeneral container initializes correctly and handles DevErrorDetect and Enabled properties.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | J1939Dcm instance is created |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Container Name | "J1939DcmGeneral" | Expected container name |
| DevErrorDetect Value | true | Boolean test value |
| Enabled Value | true | Boolean test value |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create J1939DcmGeneral with J1939Dcm parent | Container initialized successfully |
| 2 | Verify getName() returns "J1939DcmGeneral" | Name is correct |
| 3 | Set J1939DcmDevErrorDetect to True | Property set successfully |
| 4 | Call getJ1939DcmDevErrorDetect() | Returns True |
| 5 | Set J1939DcmEnabled to True | Property set successfully |
| 6 | Call getJ1939DcmEnabled() | Returns True |
| 7 | Verify fluent interface chaining | Setters return self |

## Expected Results

- J1939DcmGeneral instance created successfully
- Name is "J1939DcmGeneral"
- Parent reference points to J1939Dcm instance
- Property getters return correct values
- Fluent interface pattern works correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | J1939DcmGeneral object remains in memory for verification |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939DCM_00002 | J1939DcmGeneral Container | Covered |
| SWR_J1939DCM_00006 | Fluent Interface Pattern | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_J1939_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_J1939_00004 |
| Title | J1939Dcm Parser - Parse J1939DcmGeneral Container |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the J1939Dcm parser correctly extracts J1939DcmGeneral container from XML.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment with J1939DcmGeneral container is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| J1939DcmDevErrorDetect Value | true | Parsed from XML |
| J1939DcmEnabled Value | true | Parsed from XML |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create parser with namespace map | Parser initialized |
| 2 | Parse XML element containing J1939DcmGeneral | Container parsed successfully |
| 3 | Check model J1939DcmDevErrorDetect value | Matches XML value |
| 4 | Check model J1939DcmEnabled value | Matches XML value |
| 5 | Verify container name is "J1939DcmGeneral" | Name is correct |

## Expected Results

- J1939DcmGeneral container is created from XML
- J1939DcmDevErrorDetect value correctly extracted
- J1939DcmEnabled value correctly extracted
- Container name is correctly set

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Parsed model remains in memory for verification |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939DCM_00002 | J1939DcmGeneral Parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_J1939_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_J1939_00005 |
| Title | J1939Nm Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the J1939Nm parser correctly extracts XML namespace definitions from EB Tresos XDM files and validates the module name.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Test XDM file (valid J1939Nm.xdm) is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/J1939Nm_valid.xdm` | Valid J1939Nm XDM file for testing |
| Module Name | "J1939Nm" | Expected root module name |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create J1939NmXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with valid J1939Nm.xdm file | File parses without errors |
| 3 | Verify module name validation | Module "J1939Nm" is accepted |

## Expected Results

- Module name "J1939Nm" is validated successfully
- Parsing completes without errors

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No temporary files created during test |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939NM_00001 | Parser Layer - XDM file parsing and validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_J1939_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_J1939_00006 |
| Title | J1939Nm Model - Module Initialization and General Container |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the J1939Nm module initializes with correct name and parent reference, and that J1939NmGeneral container handles properties correctly.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Module Name | "J1939Nm" | Expected module name |
| Container Name | "J1939NmGeneral" | Expected container name |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create EBModel instance | EBModel initialized successfully |
| 2 | Create EcucParamConfContainerDef parent | Parent container created |
| 3 | Instantiate J1939Nm with parent | J1939Nm instance created |
| 4 | Verify getName() returns "J1939Nm" | Name is correct |
| 5 | Create J1939NmGeneral with J1939Nm parent | Container initialized successfully |
| 6 | Set J1939NmDevErrorDetect to True | Property set successfully |
| 7 | Call getJ1939NmDevErrorDetect() | Returns True |
| 8 | Set J1939NmEnabled to True | Property set successfully |
| 9 | Call getJ1939NmEnabled() | Returns True |

## Expected Results

- J1939Nm instance is created successfully
- J1939NmGeneral instance created successfully
- Property getters return correct values

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Objects remain in memory for verification |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939NM_00001 | Module Initialization | Covered |
| SWR_J1939NM_00002 | J1939NmGeneral Container | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_J1939_00007

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_J1939_00007 |
| Title | J1939Rm Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the J1939Rm parser correctly extracts XML namespace definitions from EB Tresos XDM files and validates the module name.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Test XDM file (valid J1939Rm.xdm) is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/J1939Rm_valid.xdm` | Valid J1939Rm XDM file for testing |
| Module Name | "J1939Rm" | Expected root module name |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create J1939RmXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with valid J1939Rm.xdm file | File parses without errors |
| 3 | Verify module name validation | Module "J1939Rm" is accepted |

## Expected Results

- Module name "J1939Rm" is validated successfully
- Parsing completes without errors

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No temporary files created during test |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939RM_00001 | Parser Layer - XDM file parsing and validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_J1939_00008

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_J1939_00008 |
| Title | J1939Rm Model - Module Initialization and General Container |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the J1939Rm module initializes with correct name and parent reference, and that J1939RmGeneral container handles properties correctly.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Module Name | "J1939Rm" | Expected module name |
| Container Name | "J1939RmGeneral" | Expected container name |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create EBModel instance | EBModel initialized successfully |
| 2 | Create EcucParamConfContainerDef parent | Parent container created |
| 3 | Instantiate J1939Rm with parent | J1939Rm instance created |
| 4 | Verify getName() returns "J1939Rm" | Name is correct |
| 5 | Create J1939RmGeneral with J1939Rm parent | Container initialized successfully |
| 6 | Set J1939RmDevErrorDetect to True | Property set successfully |
| 7 | Call getJ1939RmDevErrorDetect() | Returns True |
| 8 | Set J1939RmEnabled to True | Property set successfully |
| 9 | Call getJ1939RmEnabled() | Returns True |

## Expected Results

- J1939Rm instance is created successfully
- J1939RmGeneral instance created successfully
- Property getters return correct values

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Objects remain in memory for verification |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939RM_00001 | Module Initialization | Covered |
| SWR_J1939RM_00002 | J1939RmGeneral Container | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_J1939_00009

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_J1939_00009 |
| Title | J1939Tp Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the J1939Tp parser correctly extracts XML namespace definitions from EB Tresos XDM files and validates the module name.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Test XDM file (valid J1939Tp.xdm) is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/J1939Tp_valid.xdm` | Valid J1939Tp XDM file for testing |
| Module Name | "J1939Tp" | Expected root module name |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create J1939TpXdmParser instance | Parser initialized successfully |
| 2 | Call parse_xdm() with valid J1939Tp.xdm file | File parses without errors |
| 3 | Verify module name validation | Module "J1939Tp" is accepted |

## Expected Results

- Module name "J1939Tp" is validated successfully
- Parsing completes without errors

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No temporary files created during test |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939TP_00001 | Parser Layer - XDM file parsing and validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_J1939_00010

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_J1939_00010 |
| Title | J1939Tp Model - Module Initialization and General Container |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the J1939Tp module initializes with correct name and parent reference, and that J1939TpGeneral container handles properties correctly.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Module Name | "J1939Tp" | Expected module name |
| Container Name | "J1939TpGeneral" | Expected container name |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create EBModel instance | EBModel initialized successfully |
| 2 | Create EcucParamConfContainerDef parent | Parent container created |
| 3 | Instantiate J1939Tp with parent | J1939Tp instance created |
| 4 | Verify getName() returns "J1939Tp" | Name is correct |
| 5 | Create J1939TpGeneral with J1939Tp parent | Container initialized successfully |
| 6 | Set J1939TpDevErrorDetect to True | Property set successfully |
| 7 | Call getJ1939TpDevErrorDetect() | Returns True |
| 8 | Set J1939TpEnabled to True | Property set successfully |
| 9 | Call getJ1939TpEnabled() | Returns True |

## Expected Results

- J1939Tp instance is created successfully
- J1939TpGeneral instance created successfully
- Property getters return correct values

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Objects remain in memory for verification |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939TP_00001 | Module Initialization | Covered |
| SWR_J1939TP_00002 | J1939TpGeneral Container | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_j1939-modules.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-04-04 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_J1939_00011

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_J1939_00011 |
| Title | J1939 CLI - Command-Line Interface |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the J1939 CLI commands correctly parse command-line arguments and execute the parsing workflow.

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
| Commands | j1939dcm-xdm-xlsx, j1939nm-xdm-xlsx, j1939rm-xdm-xlsx, j1939tp-xdm-xlsx | CLI commands |
| Verbose Flag | `-v` or `--verbose` | Enable verbose logging |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute j1939dcm-xdm-xlsx command | Command completes successfully |
| 2 | Verify output file exists | File created at specified path |
| 3 | Execute with verbose flag | Command completes with verbose logging output |
| 4 | Execute j1939nm-xdm-xlsx command | Command completes successfully |
| 5 | Execute j1939rm-xdm-xlsx command | Command completes successfully |
| 6 | Execute j1939tp-xdm-xlsx command | Command completes successfully |

## Expected Results

- All CLI commands execute successfully
- Output Excel files are valid
- Verbose flag enables detailed logging
- Exit codes are appropriate (0 for success, non-zero for error)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Generated Excel files persist for review |
| 2 | No orphaned processes remain |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_J1939DCM_00004 | CLI Interface - J1939Dcm command | Covered |
| SWR_J1939NM_00004 | CLI Interface - J1939Nm command | Covered |
| SWR_J1939RM_00004 | CLI Interface - J1939Rm command | Covered |
| SWR_J1939TP_00004 | CLI Interface - J1939Tp command | Covered |

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