# BswM Module Integration Test Cases

This document contains all integration test cases for the BswM (Basic Software Mode Manager) module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_INT_BSWM_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_BSWM_00001 |
| Title | BswM Module - End-to-End Parsing and Excel Export |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete end-to-end workflow of parsing a BswM XDM file, modeling all BswM entities, and exporting to Excel.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Complete BswM.xdm file is available |
| 3 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Input File | `data/test/BswM_complete.xdm` | Complete BswM XDM |
| Mode Declaration Count | 5-15 | Expected mode declarations |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command | Command completes successfully |
| 2 | Verify Excel file exists | File created successfully |
| 3 | Verify mode declarations extracted | All declarations displayed |
| 4 | Verify mode conditions linked | Conditions correctly linked |
| 5 | Verify column formatting | Formatting applied correctly |

## Expected Results

- Excel file generated successfully
- All mode declarations extracted
- Mode conditions linked correctly
- Performance meets requirements

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_BSWM_00001 | Parser Layer - XDM file parsing | Covered |
| SWR_BSWM_00003 | Mode Declaration Parsing | Covered |
| SWR_BSWM_00004 | Reporter Layer - Excel generation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_bswm-module.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_INT_BSWM_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_BSWM_00002 |
| Title | BswM Module - Complex Mode Configuration |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the BswM parser can handle complex mode configurations with multiple conditions.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Complex BswM.xdm file is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Mode Declarations | 20+ | Large number of modes |
| Conditions per Declaration | 3-5 | Multiple conditions |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute CLI command with complex file | Command completes successfully |
| 2 | Verify all mode declarations extracted | Count matches |
| 3 | Verify conditions per declaration | All conditions linked |

## Expected Results

- Complex configuration parsed correctly
- All conditions extracted
- Performance acceptable

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_BSWM_00003 | Mode Declaration Parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_bswm-module.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |

---

# Test Case: TC_INT_BSWM_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_BSWM_00003 |
| Title | BswM Module - Error Recovery |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the BswM module handles error conditions gracefully.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Test files with error conditions are available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Missing File | Non-existent file | File not found handling |
| Invalid Module | Wrong module name | Module validation |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute with missing file | Command exits with error |
| 2 | Execute with invalid module | Command exits with error |
| 3 | Verify system recovers | Subsequent valid operations work |

## Expected Results

- Clear error messages
- System recovers after errors
- Error codes are appropriate

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_BSWM_00001 | Parser Layer - Module validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_bswm-module.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |