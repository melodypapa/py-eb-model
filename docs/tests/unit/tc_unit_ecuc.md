# EcuC Module Unit Test Cases

This document contains all unit test cases for the EcuC (ECU Configuration) module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_ECUC_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ECUC_00001 |
| Title | EcuC Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EcuC parser correctly extracts XML namespace definitions from EB Tresos XDM files, validates the module name, extracts AUTOSAR/software version information, and properly initializes the parser.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Test XDM file (valid EcuC.xdm) is available at known location |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/EcuC_valid.xdm` | Valid EcuC XDM file for testing |
| Module Name | "EcuC" | Expected root module name |
| AUTOSAR Version | "4.3.0" | Example AUTOSAR version |
| Software Version | "1.2.3" | Example software version |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create EcucXdmParser instance | Parser initialized successfully |
| 2 | Call parse() with valid EcuC.xdm file | File parses without errors |
| 3 | Verify namespace map is populated | nsmap contains namespace definitions |
| 4 | Verify module name validation | Module "EcuC" is accepted, others raise ValueError |
| 5 | Extract AUTOSAR version | Returns correct AUTOSAR version string |
| 6 | Extract software version | Returns correct software version string |
| 7 | Attempt parsing non-EcuC XDM file | Raises ValueError with descriptive message |

## Expected Results

- Namespace map contains at least 3 namespace definitions
- Module name "EcuC" is validated successfully
- AUTOSAR version matches expected value from file
- Software version matches expected value from file
- Parsing non-EcuC file raises ValueError

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No temporary files created during test |
| 2 | Parser instance can be garbage collected |
| 3 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUC_00001 | Parser Layer - XDM file parsing and validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_ecuc-module.md |
| Parser Documentation | ../../src/eb_model/parser/ecuc_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_ECUC_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ECUC_00002 |
| Title | EcuC Model - Partition Collection Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EcuC parser correctly extracts EcucPartitionCollection from XDM containers, creating the container for partition configurations.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing EcucPartitionCollection container is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Collection Name | "EcucPartitionCollection" | Collection identifier |
| Partition Count | 2-5 | Number of partitions in collection |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with EcucPartitionCollection container | EcucPartitionCollection object created successfully |
| 2 | Verify collection is set on EcuC module | getEcucPartitionCollection() returns valid object |
| 3 | Verify partition list exists | getEcucPartitions() returns list |
| 4 | Verify parent-child relationship | Collection's parent is EcuC module |

## Expected Results

- EcucPartitionCollection is created correctly
- Collection is properly attached to EcuC module
- Partition list is initialized (empty or populated)
- Parent-child relationship is established

## Post-conditions

| # | Description |
|---|-------------|
| 1 | EcucPartitionCollection object remains in memory |
| 2 | EBModel contains updated EcuC configuration |
| 3 | No orphaned collection objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUC_00003 | Partition Collection Parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_ecuc-module.md |
| Model Documentation | ../../src/eb_model/models/ecuc_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_ECUC_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ECUC_00003 |
| Title | EcuC Model - Partition Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EcuC parser correctly extracts EcucPartition configurations from XDM containers, including partition attributes like default BSW partition and restart capability.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing EcucPartition containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Partition Name | "Partition_0" | Partition identifier |
| Default BSW Partition | true | Default BSW partition flag |
| Partition Can Be Restarted | true | Restart capability flag |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with EcucPartition container | EcucPartition object created successfully |
| 2 | Verify partition name extraction | getName() returns "Partition_0" |
| 3 | Verify default BSW partition extraction | getEcucDefaultBswPartition() returns true |
| 4 | Verify partition can be restarted extraction | getEcucPartitionCanBeRestarted() returns true |
| 5 | Verify SW component instance reference list | getEcucPartitionSoftwareComponentInstanceRefs() returns list |
| 6 | Verify parent-child relationship | Partition's parent is EcucPartitionCollection |

## Expected Results

- EcucPartition is created with correct name
- Default BSW partition flag is extracted correctly
- Restart capability flag is extracted correctly
- SW component instance reference list is initialized
- Parent-child relationship is established

## Post-conditions

| # | Description |
|---|-------------|
| 1 | EcucPartition objects remain in memory |
| 2 | EcucPartitionCollection contains partition |
| 3 | No orphaned partition objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUC_00002 | Partition Configuration Parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_ecuc-module.md |
| Model Documentation | ../../src/eb_model/models/ecuc_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_ECUC_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ECUC_00004 |
| Title | EcuC Model - Software Component Instance Reference |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EcuC parser correctly extracts EcucPartitionSoftwareComponentInstanceRef configurations, linking partitions to software component instances.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing SW component instance references is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Instance Type | "ApplicationSwComponentType" | Component type |
| Target Reference | "ASPath:/Application/App_Swc" | Target component reference |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with EcucPartitionSoftwareComponentInstanceRef | EcucPartitionSoftwareComponentInstanceRef object created |
| 2 | Verify instance type extraction | Name matches component type |
| 3 | Verify target reference extraction | getEcucPartitionSoftwareComponentInstanceTargetRef() returns valid reference |
| 4 | Verify reference short name | getShortName() returns component short name |
| 5 | Verify parent-child relationship | Reference parent is EcucPartition |

## Expected Results

- SW component instance reference is created correctly
- Target reference is extracted and valid
- Reference short name is accessible
- Parent-child relationship is established

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Reference objects remain in memory |
| 2 | EcucPartition contains reference |
| 3 | No orphaned reference objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUC_00002 | Partition Configuration Parsing - SW Component References | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_ecuc-module.md |
| Model Documentation | ../../src/eb_model/models/ecuc_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_ECUC_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ECUC_00005 |
| Title | EcuC Reporter - Excel Worksheet Generation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EcuC reporter correctly generates Excel worksheets for all EcuC entity types with proper formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | EcuC model objects are populated with test data |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Output File Path | "test_output/EcuC_report.xlsx" | Generated Excel file path |
| Partition Count | 3-5 | Number of partitions for testing |
| SW Component References | 5-10 per partition | Component references per partition |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create EcuC XLS writer instance | Writer initialized successfully |
| 2 | Generate partition worksheet | Partition worksheet created with all data |
| 3 | Verify partition names displayed | All partition names shown |
| 4 | Verify BSW partition flags | Default BSW flags displayed correctly |
| 5 | Verify restart flags | Restart capability shown |
| 6 | Verify SW component references | Component references displayed |
| 7 | Verify column auto-width formatting | Columns sized to fit content |

## Expected Results

- Expected worksheets are created
- All partition data is populated correctly
- SW component references are displayed
- Column formatting is applied
- File is valid and can be opened in Excel

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file persists for review |
| 2 | No memory leaks in reporter |
| 3 | Model objects remain unchanged after export |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUC_00004 | Reporter Layer - Excel worksheet generation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_ecuc-module.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/ecuc_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_ECUC_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ECUC_00006 |
| Title | EcuC CLI - Command-Line Interface |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EcuC CLI correctly parses command-line arguments, executes the parsing workflow, and handles various command options.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI entry point is registered (ecuc-xdm-xlsx) |
| 3 | Test XDM file is available |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Command | `ecuc-xdm-xlsx input.xdm output.xlsx` | Basic command execution |
| Input File | `data/test/EcuC_test.xdm` | Test input file |
| Output File | `test_output/EcuC_test.xlsx` | Test output file |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute basic command | Command completes successfully, Excel file generated |
| 2 | Verify output file exists | File created at specified path |
| 3 | Execute with missing input file | Command exits with error, appropriate error message |
| 4 | Execute with invalid arguments | Help message displayed |
| 5 | Verify help message includes usage and options | Help is complete and accurate |

## Expected Results

- Basic command executes successfully
- Output Excel file is valid
- Missing input file produces helpful error
- Invalid arguments display help message
- Exit codes are appropriate

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Generated Excel files persist for review |
| 2 | No orphaned processes remain |
| 3 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUC_00005 | CLI Interface - Command-line argument parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_ecuc-module.md |
| CLI Documentation | ../../src/eb_model/cli/ecuc_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_ECUC_00007

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ECUC_00007 |
| Title | EcuC Error Handling - Invalid Module |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EcuC parser correctly validates module name and handles invalid configurations.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Test files with various error conditions are available |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Invalid Module File | XDM file with wrong module name | Verify module validation |
| Missing Partition Collection | XDM without EcucPartitionCollection | Verify optional handling |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XDM file with wrong module name | Parser raises ValueError |
| 2 | Verify error message indicates wrong module | Message is clear and helpful |
| 3 | Parse XDM file without partition collection | Parser handles gracefully (optional element) |

## Expected Results

- Invalid module name is detected and reported
- Error messages are clear and actionable
- Optional missing elements don't cause errors

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No partial model objects created |
| 2 | System returns to clean state |
| 3 | Parser can be reused |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUC_00001 | Parser Layer - Module validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_ecuc-module.md |
| Parser Documentation | ../../src/eb_model/parser/ecuc_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_ECUC_00008

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_ECUC_00008 |
| Title | EcuC Model - Optional Value Handling |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | Medium |

## Purpose/Objective

Verify that the EcuC parser correctly handles optional values in partition configurations.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment with partition missing optional values is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Partition Name | "Partition_Minimal" | Partition with minimal config |
| Default BSW Partition | Not set | Optional value not present |
| SW Component References | Empty list | No references configured |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse partition with missing optional values | Partition created successfully |
| 2 | Verify optional values are null | getEcucDefaultBswPartition() returns None |
| 3 | Verify SW component reference list is empty | getEcucPartitionSoftwareComponentInstanceRefs() returns empty list |
| 4 | Verify partition is usable | Partition object is valid |

## Expected Results

- Optional values don't cause parsing errors
- Missing optional values return None or empty list
- Partition object is valid and usable

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Partition object created successfully |
| 2 | No errors logged for missing optional values |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_ECUC_00002 | Partition Configuration Parsing - Optional values | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_ecuc-module.md |
| Model Documentation | ../../src/eb_model/models/ecuc_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |