# BswM Module Unit Test Cases

This document contains all unit test cases for the BswM (Basic Software Mode Manager) module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_BSWM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_BSWM_00001 |
| Title | BswM Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the BswM parser correctly extracts XML namespace definitions from EB Tresos XDM files, validates the module name, and extracts version information.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Test XDM file (valid BswM.xdm) is available |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/BswM_valid.xdm` | Valid BswM XDM file |
| Module Name | "BswM" | Expected root module name |
| AUTOSAR Version | "4.3.0" | Example AUTOSAR version |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create BswMXdmParser instance | Parser initialized successfully |
| 2 | Call parse() with valid BswM.xdm file | File parses without errors |
| 3 | Verify module name validation | Module "BswM" is accepted |
| 4 | Attempt parsing non-BswM XDM file | Raises ValueError |

## Expected Results

- Module name "BswM" is validated successfully
- Parsing non-BswM file raises ValueError
- Version information is extracted correctly

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_BSWM_00001 | Parser Layer - XDM file parsing and validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_bswm-module.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_BSWM_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_BSWM_00002 |
| Title | BswM Model - General Configuration Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the BswM parser correctly extracts BswMGeneral configuration from XDM containers.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing BswMGeneral container is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Dev Error Detect | true | Development error detection flag |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with BswMGeneral container | BswMGeneral object created |
| 2 | Verify dev error detect extraction | getBswMDevErrorDetect() returns true |
| 3 | Verify parent-child relationship | General's parent is BswM module |

## Expected Results

- BswMGeneral is created correctly
- Dev error detect flag is extracted
- Parent-child relationship is established

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_BSWM_00002 | General Configuration Parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Model Documentation | ../../src/eb_model/models/bswm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_BSWM_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_BSWM_00003 |
| Title | BswM Model - Mode Declaration Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the BswM parser correctly extracts BswMModeDeclaration configurations from XDM containers.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing BswMModeDeclaration containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Mode Declaration Name | "BswM_Mode_Application" | Mode declaration identifier |
| Available For Scheduler | true | Scheduler availability flag |
| Mode Type | "ApplicationMode" | Mode type identifier |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with BswMModeDeclaration | BswMModeDeclaration object created |
| 2 | Verify mode declaration name extraction | getName() returns correct value |
| 3 | Verify available for scheduler extraction | getBswMAvailableForScheduler() returns true |
| 4 | Verify mode type extraction | getBswMModeType() returns correct value |
| 5 | Verify mode condition list initialized | getBswMModeConditionList() returns list |

## Expected Results

- Mode declaration is created correctly
- All attributes are extracted
- Mode condition list is initialized

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_BSWM_00003 | Mode Declaration Parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Model Documentation | ../../src/eb_model/models/bswm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_BSWM_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_BSWM_00004 |
| Title | BswM Model - Mode Condition Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the BswM parser correctly extracts BswMModeCondition configurations from XDM containers.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing BswMModeCondition containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Condition Source Ref | "ASPath:/Rte/ModeCondition" | Mode condition source reference |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with BswMModeCondition | BswMModeCondition object created |
| 2 | Verify condition source reference extraction | getBswMModeConditionSourceRef() returns reference |
| 3 | Verify parent-child relationship | Condition's parent is BswMModeDeclaration |

## Expected Results

- Mode condition is created correctly
- Source reference is extracted
- Parent-child relationship is established

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_BSWM_00003 | Mode Declaration Parsing - Conditions | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Model Documentation | ../../src/eb_model/models/bswm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_BSWM_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_BSWM_00005 |
| Title | BswM Reporter - Excel Worksheet Generation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the BswM reporter correctly generates Excel worksheets for all BswM entity types.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | BswM model objects are populated with test data |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Output File Path | "test_output/BswM_report.xlsx" | Generated Excel file path |
| Mode Declaration Count | 5-10 | Number of mode declarations |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create BswM XLS writer instance | Writer initialized successfully |
| 2 | Generate mode declaration worksheet | Worksheet created with all data |
| 3 | Verify column formatting | Columns sized correctly |

## Expected Results

- Expected worksheets are created
- All mode declaration data is populated
- Column formatting is applied

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_BSWM_00004 | Reporter Layer - Excel generation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/bswm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_BSWM_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_BSWM_00006 |
| Title | BswM CLI - Command-Line Interface |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the BswM CLI correctly parses command-line arguments and executes the parsing workflow.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI entry point is registered (bswm-xdm-xlsx) |
| 3 | Test XDM file is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Command | `bswm-xdm-xlsx input.xdm output.xlsx` | Basic command execution |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute basic command | Command completes successfully |
| 2 | Verify output file exists | File created at specified path |
| 3 | Execute with missing input file | Command exits with error |

## Expected Results

- Basic command executes successfully
- Output Excel file is valid
- Error handling works correctly

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_BSWM_00005 | CLI Interface - Command-line parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| CLI Documentation | ../../src/eb_model/cli/bswm_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_BSWM_00007

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_BSWM_00007 |
| Title | BswM Model - Mode Declaration Sorting |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | Medium |

## Purpose/Objective

Verify that mode declarations and conditions are sorted correctly by name.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Multiple mode declarations with different names are available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Mode Declarations | Multiple with names: "B", "A", "C" | Test sorting |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Add multiple mode declarations | All added successfully |
| 2 | Retrieve mode declaration list | List is sorted by name |
| 3 | Verify order | "A", "B", "C" order |

## Expected Results

- Mode declarations are returned in sorted order
- Sorting is consistent

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_BSWM_00003 | Mode Declaration Parsing - Sorting | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Model Documentation | ../../src/eb_model/models/bswm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |