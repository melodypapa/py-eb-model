# NVM Module Integration Test Cases

This document contains all integration test cases for the NVM (Non-volatile Memory) module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_INT_NVM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_NVM_00001 |
| Title | NVM Module - End-to-End Parsing and Excel Export |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete end-to-end workflow of parsing an NVM XDM file, modeling all NVM entities (NvMCommon, NvMBlockDescriptors, callbacks, target references), and exporting the configuration to a multi-sheet Excel file with proper formatting.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed and accessible |
| 2 | Complete NvM.xdm file with all entity types is available |
| 3 | Output directory for Excel file is writable |
| 4 | No other instances of EBModel exist (singleton pattern) |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/NvM_complete.xdm` | NVM XDM with all entity types |
| Output File | `test_output/NvM_test.xlsx` | Generated Excel report |
| Expected Worksheets | NvMCommon, NvMBlockDescriptor | List of expected sheets |
| Block Descriptor Count | 20-50 | Expected number of block descriptors |
| EA References | 5-10 | Expected EA block references |
| FEE References | 5-10 | Expected FEE block references |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command: `nvm-xdm-xlsx data/test/NvM_complete.xdm test_output/NvM_test.xlsx` | Command completes successfully |
| 2 | Verify Excel file exists | File created at output path |
| 3 | Open Excel file and verify worksheets | All expected worksheets present |
| 4 | Verify NvMCommon worksheet | Common configuration displayed correctly |
| 5 | Verify NvMBlockDescriptor worksheet | All block descriptors extracted |
| 6 | Verify block descriptor count | Count matches input file |
| 7 | Verify CRC settings | Block CRC types displayed correctly |
| 8 | Verify callback function names | Init and single block callbacks shown |
| 9 | Verify target block references | EA/FEE references displayed correctly |
| 10 | Verify partition references | Partition assignments shown |
| 11 | Verify column auto-width formatting | Columns sized to fit content |
| 12 | Verify numeric data centering | Numeric columns are center-aligned |
| 13 | Verify total execution time | Execution completes within 5 seconds for 10MB file |

## Expected Results

- Excel file generated successfully with no errors
- All expected worksheets present
- Common configuration includes API config class, job queues, polling mode
- Block descriptor data includes all management types and CRC settings
- Callback functions are displayed correctly
- Target block references show EA/FEE block names
- Column formatting applied consistently
- Total execution time < 5 seconds for typical file
- Memory usage remains stable (no leaks)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file persists for review |
| 2 | No memory leaks in parser/reporter |
| 3 | EBModel singleton can be reset for next test |
| 4 | No orphaned XML elements remain in memory |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_NVM_00001 | Parser Layer - XDM file parsing | Covered |
| SWR_NVM_00002 | NvM Common Configuration Parsing | Covered |
| SWR_NVM_00003 | NvM Block Descriptor Parsing | Covered |
| SWR_NVM_00004 | Reporter Layer - Excel generation | Covered |
| SWR_NVM_00005 | CLI Interface - Command execution | Covered |
| SWR_NVM_00007 | Non-Functional - O(1) lookup performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_nvm-module.md |
| Parser Documentation | ../../src/eb_model/parser/nvm_xdm_parser.py |
| Reporter Documentation | ../../src/eb_model/reporter/excel_reporter/nvm_xdm.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_INT_NVM_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_NVM_00002 |
| Title | NVM Module - Complex Block Configuration Handling |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the NVM parser can handle complex configurations including multiple block types, mixed EA/FEE references, various management types, and intricate callback configurations.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Complex NvM.xdm file with advanced features is available |
| 3 | Output directory is writable |
| 4 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/NvM_complex.xdm` | XDM with complex configuration |
| Block Descriptor Count | 50+ | Large number of block descriptors |
| Management Types | Mixed (NVM_BLOCK_MGMT, NVM_DATASET, NVM_QUEUE) | Various management types |
| Reference Types | Mixed EA and FEE | Both reference types in same file |
| Callback Configurations | Various init and single block callbacks | Complex callback setup |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command with complex XDM file | Command completes successfully |
| 2 | Verify Excel file generated with all worksheets | File created successfully |
| 3 | Verify block descriptor count | All blocks extracted correctly |
| 4 | Verify mixed management types | All types parsed correctly |
| 5 | Verify EA references | EA blocks referenced correctly |
| 6 | Verify FEE references | FEE blocks referenced correctly |
| 7 | Verify callback configurations | All callbacks extracted |
| 8 | Verify partition assignments | Partitions correctly assigned |
| 9 | Verify CRC type variations | Different CRC types handled |
| 10 | Verify job priority variations | Priorities extracted correctly |

## Expected Results

- Complex configuration is parsed completely and correctly
- All block management types are handled
- EA and FEE references are correctly distinguished
- All callbacks are extracted
- Performance remains acceptable for complex configurations
- No data loss or corruption in complex scenarios

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Excel file with complex configuration persists for review |
| 2 | No memory leaks or resource exhaustion |
| 3 | EBModel can be reset for next test |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_NVM_00002 | NvM Common Configuration Parsing | Covered |
| SWR_NVM_00003 | NvM Block Descriptor Parsing | Covered |
| SWR_NVM_00007 | Non-Functional - O(1) lookup performance | Covered |

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

# Test Case: TC_INT_NVM_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_NVM_00003 |
| Title | NVM Module - Error Recovery and Reporting |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the NVM module gracefully handles error conditions including missing files, invalid configurations, and corrupted data, providing clear error messages and recovering when possible.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Test files with various error conditions are available |
| 3 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Missing File | Non-existent file path | Verify file not found handling |
| Empty File | Empty .xdm file | Verify empty file handling |
| Invalid Module | XDM file with wrong module name | Verify module validation |
| Invalid Block Reference | Unknown block reference type | Verify reference type validation |
| Large File | 50MB+ XDM file | Verify performance and stability |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute with non-existent file | Command exits with error, file not found message |
| 2 | Verify error message includes file path | Message is specific and helpful |
| 3 | Execute with empty file | Command exits with error, indicates empty/invalid file |
| 4 | Execute with invalid module name (non-NvM) | Command exits with error, indicates wrong module |
| 5 | Execute with invalid block reference type | Command exits with error, indicates unknown reference type |
| 6 | Execute with large file (50MB) | Command completes or reports size limit |
| 7 | Verify memory usage during large file processing | Memory usage remains stable, no leaks |
| 8 | Verify system can recover after error | Subsequent valid operations work correctly |

## Expected Results

- Missing files produce clear error messages with file paths
- Empty or invalid files are detected and reported
- Module validation catches wrong module types
- Invalid block reference types are reported with helpful messages
- Large files are handled within performance limits
- System recovers gracefully after errors
- Error codes are appropriate (non-zero for failures)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No corrupted output files from failed operations |
| 2 | System returns to clean state |
| 3 | EBModel singleton can be reset for next test |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_NVM_00006 | Non-Functional - Error handling | Covered |
| SWR_NVM_00007 | Non-Functional - O(1) lookup performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_nvm-module.md |
| Parser Documentation | ../../src/eb_model/parser/nvm_xdm_parser.py |
| CLI Documentation | ../../src/eb_model/cli/nvm_xdm_2_xls_cli.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |