# Test Case: TC_UNIT_OS_00013

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00013 |
| Title | OS Error Handling - Required Element Validation |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly validates required elements and references, detecting missing mandatory attributes and invalid path references.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XDM test files with missing required elements are available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Missing Required Attribute | Task without name | Verify required attribute validation |
| Invalid Counter Reference | Schedule table referencing non-existent counter | Verify reference validation |
| Invalid Application Reference | Task referencing non-existent application | Verify reference validation |
| Invalid Path Reference | Malformed ASPath reference | Verify path validation |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XDM file with task missing name attribute | Parser raises ValueError indicating missing required attribute |
| 2 | Verify error message includes element name and attribute | Message identifies exactly what's missing |
| 3 | Parse XDM file with schedule table referencing invalid counter | Parser raises ValueError or logs warning |
| 4 | Verify error message indicates unresolved reference | Message includes reference target |
| 5 | Parse XDM file with task referencing non-existent application | Parser raises ValueError or logs warning |
| 6 | Verify error handling allows optional application reference | Application reference is optional, no error if missing |
| 7 | Parse XDM file with malformed ASPath reference | Parser raises ValueError with path format details |
| 8 | Verify path validation accepts valid ASPath format | Valid paths like "ASPath:/Os/Task1" are accepted |

## Expected Results

- Missing required attributes are detected and reported
- Error messages clearly indicate what's missing and where
- Invalid references are detected with helpful messages
- Optional elements don't cause errors when missing
- Path references are validated for correct format
- Parser gracefully handles missing references (error or warning based on severity)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No partial model objects created for invalid entities |
| 2 | System returns to clean state |
| 3 | Parser can be reused for subsequent operations |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00017 | Non-Functional - Required element validation | Covered |
| SWR_OS_00018 | Non-Functional - Path validation | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Parser Documentation | ../../src/eb_model/parser/os_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |