# NVM Module Unit Test Cases

This document contains all unit test cases for the NVM (Non-volatile Memory) module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_NVM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_NVM_00001 |
| Title | NVM Parser - XDM File Parsing and Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the NVM parser correctly extracts XML namespace definitions from EB Tresos XDM files, validates the module name, extracts AUTOSAR/software version information, and properly initializes the parser.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Test XDM file (valid NvM.xdm) is available at known location |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/NvM_valid.xdm` | Valid NVM XDM file for testing |
| Module Name | "NvM" | Expected root module name |
| AUTOSAR Version | "4.3.0" | Example AUTOSAR version |
| Software Version | "1.2.3" | Example software version |
| Namespace Prefix | "d" | Default namespace prefix |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create NvMXdmParser instance | Parser initialized successfully |
| 2 | Call parse() with valid NvM.xdm file | File parses without errors |
| 3 | Verify namespace map is populated | nsmap contains namespace definitions |
| 4 | Verify module name validation | Module "NvM" is accepted, others raise ValueError |
| 5 | Extract AUTOSAR version | Returns correct AUTOSAR version string |
| 6 | Extract software version | Returns correct software version string |
| 7 | Attempt parsing non-NVM XDM file | Raises ValueError with descriptive message |

## Expected Results

- Namespace map contains at least 3 namespace definitions
- Module name "NvM" is validated successfully
- AUTOSAR version matches expected value from file
- Software version matches expected value from file
- Parsing non-NVM file raises ValueError with message indicating invalid module

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No temporary files created during test |
| 2 | Parser instance can be garbage collected |
| 3 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_NVM_00001 | Parser Layer - XDM file parsing and validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_nvm-module.md |
| Parser Documentation | ../../src/eb_model/parser/nvm_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_NVM_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_NVM_00002 |
| Title | NVM Model - Common Configuration Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the NVM parser correctly extracts NvMCommon configuration from XDM containers, including API config class, job queues, polling mode, and other common settings.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing NvMCommon container is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| API Config Class | "NVMAPICONFIGCLASS_1" | API configuration class |
| Compiled Config ID | 42 | Configuration identifier |
| CRC Num of Bytes | 4 | CRC byte count |
| Dev Error Detect | true | Development error detection flag |
| Polling Mode | false | Polling mode flag |
| Job Prioritization | true | Job prioritization flag |
| Main Function Period | 0.01 | Main function period in seconds |
| Size Standard Job Queue | 10 | Standard job queue size |
| Size Immediate Job Queue | 5 | Immediate job queue size |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with NvMCommon container | NvMCommon object created successfully |
| 2 | Verify API config class extraction | getNvMApiConfigClass() returns correct value |
| 3 | Verify compiled config ID extraction | getNvMCompiledConfigId() returns 42 |
| 4 | Verify CRC num of bytes extraction | getNvMCrcNumOfBytes() returns 4 |
| 5 | Verify dev error detect extraction | getNvMDevErrorDetect() returns true |
| 6 | Verify polling mode extraction | getNvMPollingMode() returns false |
| 7 | Verify job prioritization extraction | getNvMJobPrioritization() returns true |
| 8 | Verify main function period extraction | getNvMMainFunctionPeriod() returns 0.01 |
| 9 | Verify standard job queue size extraction | getNvMSizeStandardJobQueue() returns 10 |
| 10 | Verify immediate job queue size extraction | getNvMSizeImmediateJobQueue() returns 5 |

## Expected Results

- All NvMCommon attributes are extracted correctly
- Boolean values are parsed correctly
- Numeric values are parsed with correct types
- Optional values are handled gracefully when not present
- Parent-child relationship is established

## Post-conditions

| # | Description |
|---|-------------|
| 1 | NvMCommon object remains in memory for verification |
| 2 | EBModel contains updated NvMCommon configuration |
| 3 | No orphaned configuration objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_NVM_00002 | NvM Common Configuration Parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_nvm-module.md |
| Model Documentation | ../../src/eb_model/models/nvm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_NVM_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_NVM_00003 |
| Title | NVM Model - Block Descriptor Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the NVM parser correctly extracts NvMBlockDescriptor configurations from XDM containers, including block management type, CRC settings, job priority, and data addresses.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing NvMBlockDescriptor containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Block Name | "NvMBlock_UserData" | Block descriptor identifier |
| Block Management Type | "NVM_BLOCK_MGMT" | Block management type |
| NVRAM Block Identifier | 1 | Block identifier |
| NV Block Length | 256 | Block length in bytes |
| NV Block Num | 1 | Number of NV blocks |
| ROM Block Num | 0 | Number of ROM blocks |
| Block Job Priority | 50 | Job priority |
| Block Use CRC | true | CRC usage flag |
| Block CRC Type | "NVM_CRC16" | CRC type |
| Select Block For Read All | true | ReadAll selection flag |
| Select Block For Write All | true | WriteAll selection flag |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with NvMBlockDescriptor container | NvMBlockDescriptor object created successfully |
| 2 | Verify block name extraction | getName() returns "NvMBlock_UserData" |
| 3 | Verify block management type extraction | getNvMBlockManagementType() returns "NVM_BLOCK_MGMT" |
| 4 | Verify NVRAM block identifier extraction | getNvMNvramBlockIdentifier() returns 1 |
| 5 | Verify NV block length extraction | getNvMNvBlockLength() returns 256 |
| 6 | Verify NV block num extraction | getNvMNvBlockNum() returns 1 |
| 7 | Verify ROM block num extraction | getNvMRomBlockNum() returns 0 |
| 8 | Verify block job priority extraction | getNvMBlockJobPriority() returns 50 |
| 9 | Verify block use CRC extraction | getNvMBlockUseCrc() returns true |
| 10 | Verify block CRC type extraction | getNvMBlockCrcType() returns "NVM_CRC16" |

## Expected Results

- All NvMBlockDescriptor attributes are extracted correctly
- Block management type is validated
- CRC settings are correctly parsed
- Job priority is extracted with correct value
- ReadAll/WriteAll flags are correctly parsed
- Parent-child relationship is established

## Post-conditions

| # | Description |
|---|-------------|
| 1 | NvMBlockDescriptor objects remain in memory for verification |
| 2 | EBModel contains updated block descriptor collection |
| 3 | No orphaned block descriptor objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_NVM_00003 | NvM Block Descriptor Parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_nvm-module.md |
| Model Documentation | ../../src/eb_model/models/nvm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_NVM_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_NVM_00004 |
| Title | NVM Model - Target Block Reference (EA/FEE) |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the NVM parser correctly extracts target block references (NvMEaRef and NvMFeeRef) from XDM containers, establishing the link between NVM blocks and underlying memory abstraction modules.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing NvMEaRef/NvMFeeRef containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| EA Block Reference | "EaBlock_UserData" | EA block reference target |
| FEE Block Reference | "FeeBlock_UserData" | FEE block reference target |
| Reference Type | "NvMEaRef" or "NvMFeeRef" | Reference type identifier |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with NvMEaRef container | NvMEaRef object created successfully |
| 2 | Verify EA block name extraction | getNvMNameOfEaBlock() returns correct reference |
| 3 | Verify reference type | Object is instance of NvMEaRef |
| 4 | Parse XML fragment with NvMFeeRef container | NvMFeeRef object created successfully |
| 5 | Verify FEE block name extraction | getNvMNameOfFeeBlock() returns correct reference |
| 6 | Verify reference type | Object is instance of NvMFeeRef |
| 7 | Verify parent-child relationship | Reference parent is NvMBlockDescriptor |
| 8 | Handle invalid reference type | Parser raises ValueError for unknown types |

## Expected Results

- NvMEaRef is created correctly with EA block reference
- NvMFeeRef is created correctly with FEE block reference
- Reference type is correctly identified from choice element
- Invalid reference types are rejected with error
- Parent-child relationships are established

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Target block reference objects remain in memory |
| 2 | NvMBlockDescriptor has valid target block reference |
| 3 | No orphaned reference objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_NVM_00003 | NvM Block Descriptor Parsing - Target Block Reference | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_nvm-module.md |
| Model Documentation | ../../src/eb_model/models/nvm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_NVM_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_NVM_00005 |
| Title | NVM Model - Callback Configuration Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the NVM parser correctly extracts callback configurations (NvMInitBlockCallback and NvMSingleBlockCallback) from XDM containers.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing callback containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Init Block Callback Function | "NvM_InitBlock_UserData" | Init callback function name |
| Single Block Callback Function | "NvM_SingleBlockCallback_UserData" | Single block callback function name |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with NvMInitBlockCallback container | NvMInitBlockCallback object created successfully |
| 2 | Verify init callback function extraction | getNvMInitBlockCallbackFnc() returns correct function name |
| 3 | Parse XML fragment with NvMSingleBlockCallback container | NvMSingleBlockCallback object created successfully |
| 4 | Verify single block callback function extraction | getNvMSingleBlockCallbackFnc() returns correct function name |
| 5 | Verify optional callback handling | Missing callbacks don't cause errors |
| 6 | Verify parent-child relationship | Callback parent is NvMBlockDescriptor |

## Expected Results

- Init block callback is extracted correctly
- Single block callback is extracted correctly
- Optional callbacks are handled gracefully when not present
- Parent-child relationships are established

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Callback objects remain in memory for verification |
| 2 | NvMBlockDescriptor has valid callback references |
| 3 | No orphaned callback objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_NVM_00003 | NvM Block Descriptor Parsing - Callback Configuration | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_nvm-module.md |
| Model Documentation | ../../src/eb_model/models/nvm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_NVM_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_NVM_00006 |
| Title | NVM Model - Partition Reference Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | Medium |

## Purpose/Objective

Verify that the NVM parser correctly extracts ECU partition references from XDM containers, including master partition and block-level partition assignments.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing partition references is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Master ECUc Partition Ref | "ASPath:/EcuC/EcuCPartition_0" | Master partition reference |
| ECUc Partition Ref List | Multiple partition references | Partition assignment list |
| Block Partition Ref | "ASPath:/EcuC/EcuCPartition_1" | Block-level partition reference |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with partition references | Partition references extracted correctly |
| 2 | Verify master partition reference extraction | getNvMMasterEcucPartitionRef() returns correct reference |
| 3 | Verify partition reference list extraction | getNvMEcucPartitionRefList() returns correct list |
| 4 | Verify block partition reference extraction | getNvMBlockEcucPartitionRef() returns correct reference |
| 5 | Handle missing optional references | Optional references don't cause errors |

## Expected Results

- Master partition reference is extracted correctly
- Partition reference list is populated
- Block-level partition references are extracted
- Optional references are handled gracefully

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Partition reference objects remain in memory |
| 2 | EBModel contains partition configuration |
| 3 | No orphaned reference objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_NVM_00002 | NvM Common Configuration Parsing - Partition References | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_nvm-module.md |
| Model Documentation | ../../src/eb_model/models/nvm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_NVM_00007

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_NVM_00007 |
| Title | NVM Reporter - Excel Worksheet Generation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the NVM reporter correctly generates Excel worksheets for all NVM entity types (NvMCommon, NvMBlockDescriptor) with proper formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Openpyxl library is available |
| 3 | NVM model objects are populated with test data |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Output File Path | "test_output/NvM_report.xlsx" | Generated Excel file path |
| Worksheets to Generate | NvMCommon, NvMBlockDescriptor | Expected worksheets |
| Block Descriptor Count | 10-20 | Number of block descriptors for testing |
| Column Headers | Name, Block Management Type, Block Length, etc. | Expected column structure |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create NvM XLS writer instance | Writer initialized successfully |
| 2 | Generate NvMCommon worksheet | NvMCommon worksheet created with all data |
| 3 | Generate NvMBlockDescriptor worksheet | NvMBlockDescriptor worksheet created with all data |
| 4 | Verify column auto-width formatting | Column widths sized to fit content |
| 5 | Verify numeric data centering | Numeric columns are center-aligned |
| 6 | Verify block descriptor data | All block attributes displayed correctly |
| 7 | Verify callback function names displayed | Callback functions shown in worksheet |
| 8 | Verify target block references displayed | EA/FEE references shown correctly |

## Expected Results

- All expected worksheets are created
- All data is populated correctly
- Column formatting is applied (auto-width, centering for numeric)
- Data types are correct (strings for text, numbers for numeric values)
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
| SWR_NVM_00004 | Reporter Layer - Excel worksheet generation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_nvm-module.md |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/nvm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_NVM_00008

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_NVM_00008 |
| Title | NVM CLI - Command-Line Interface |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the NVM CLI correctly parses command-line arguments, executes the parsing workflow, and handles various command options.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CLI entry point is registered (nvm-xdm-xlsx) |
| 3 | Test XDM file is available |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Command | `nvm-xdm-xlsx input.xdm output.xlsx` | Basic command execution |
| Input File | `data/test/NvM_test.xdm` | Test input file |
| Output File | `test_output/NvM_test.xlsx` | Test output file |
| Verbose Flag | `-v` or `--verbose` | Enable verbose logging |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute basic command | Command completes successfully, Excel file generated |
| 2 | Verify output file exists | File created at specified path |
| 3 | Execute with verbose flag | Command completes with verbose logging output |
| 4 | Execute with missing input file | Command exits with error, appropriate error message |
| 5 | Execute with invalid arguments | Help message displayed |
| 6 | Verify help message includes usage and options | Help is complete and accurate |

## Expected Results

- Basic command executes successfully
- Output Excel file is valid
- Verbose flag enables detailed logging
- Missing input file produces helpful error
- Invalid arguments display help message
- Exit codes are appropriate (0 for success, non-zero for error)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Generated Excel files persist for review |
| 2 | No orphaned processes remain |
| 3 | System returns to pre-test state |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_NVM_00005 | CLI Interface - Command-line argument parsing and execution | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_nvm-module.md |
| CLI Documentation | ../../src/eb_model/cli/nvm_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_NVM_00009

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_NVM_00009 |
| Title | NVM Error Handling - Malformed XML |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the NVM parser correctly handles malformed XML files with missing tags, invalid nesting, or incorrect attribute types, providing appropriate error messages without crashing.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Malformed XDM test files are available |
| 3 | No other parsing operations are in progress |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Malformed File 1 | Missing closing tag | Verify missing tag handling |
| Malformed File 2 | Invalid attribute type | Verify type validation |
| Malformed File 3 | Invalid enum value | Verify enum validation |
| Malformed File 4 | Invalid block reference type | Verify reference type validation |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XDM file with missing closing tag | Parser raises XMLSyntaxError or ValueError |
| 2 | Verify error message is descriptive | Error message indicates missing tag |
| 3 | Parse XDM file with invalid attribute type | Parser raises ValueError with type mismatch message |
| 4 | Parse XDM file with invalid enum value | Parser raises ValueError with valid enum options |
| 5 | Parse XDM file with invalid block reference type | Parser raises ValueError with descriptive message |

## Expected Results

- Malformed XML is detected and reported
- Error messages are clear, descriptive, and actionable
- Parser does not crash on malformed input
- Invalid block reference types are rejected

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No partial model objects created |
| 2 | System returns to clean state |
| 3 | Parser can be reused for subsequent operations |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_NVM_00006 | Non-Functional - Malformed XML error handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_nvm-module.md |
| Parser Documentation | ../../src/eb_model/parser/nvm_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_UNIT_NVM_00010

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_NVM_00010 |
| Title | NVM Model - O(1) Lookup Performance |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | Medium |

## Purpose/Objective

Verify that NVM block descriptor lookup operations achieve O(1) performance using dictionary-based storage.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Large NVM XDM file with many block descriptors is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Block Descriptor Count | 100+ | Large number of blocks for performance testing |
| Lookup Iterations | 1000 | Number of lookup operations to perform |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse large NVM XDM file | All block descriptors parsed correctly |
| 2 | Perform multiple lookups by name | Lookup time is constant regardless of position |
| 3 | Verify lookup performance | Average lookup time < 1ms |
| 4 | Compare first vs last block lookup time | Times are approximately equal |

## Expected Results

- Block descriptor lookup is O(1) using dictionary
- Lookup performance does not degrade with file size
- Average lookup time meets performance requirements

## Post-conditions

| # | Description |
|---|-------------|
| 1 | EBModel contains all block descriptors |
| 2 | No memory leaks detected |
| 3 | Parser can be reused |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_NVM_00007 | Non-Functional - O(1) lookup performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_nvm-module.md |
| Model Documentation | ../../src/eb_model/models/nvm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |