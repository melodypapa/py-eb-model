# Test Case: TC_UNIT_OS_00012

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00012 |
| Title | OS Error Handling - Malformed XML |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly handles malformed XML files with missing tags, invalid nesting, or incorrect attribute types, providing appropriate error messages without crashing.

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
| Malformed File 2 | Invalid attribute type (string for number) | Verify type validation |
| Malformed File 3 | Invalid enum value | Verify enum validation |
| Malformed File 4 | Duplicate element names | Verify duplicate handling |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XDM file with missing closing tag | Parser raises XMLSyntaxError or ValueError |
| 2 | Verify error message is descriptive | Error message indicates missing tag |
| 3 | Parse XDM file with invalid attribute type (priority="abc") | Parser raises ValueError with type mismatch message |
| 4 | Verify error message includes field name and expected type | Message is clear and actionable |
| 5 | Parse XDM file with invalid enum value (scheduleType="INVALID") | Parser raises ValueError with valid enum options |
| 6 | Verify error message includes valid options | User can see acceptable values |
| 7 | Parse XDM file with duplicate task names | Parser raises ValueError or handles with warning |
| 8 | Verify error indicates duplicate element | Message identifies conflicting element |

## Expected Results

- Malformed XML is detected and reported
- Error messages are clear, descriptive, and actionable
- Parser does not crash on malformed input
- Error messages include context (file, line, element, expected vs actual)
- Type mismatches are caught with helpful messages
- Invalid enum values show valid options
- Duplicate elements are detected

## Post-conditions

| # | Description |
|---|-------------|
| 1 | No partial model objects created |
| 2 | System returns to clean state |
| 3 | Parser can be reused for subsequent operations |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00015 | Non-Functional - Malformed XML error handling | Covered |
| SWR_OS_00016 | Non-Functional - Missing optional elements handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Parser Documentation | ../../src/eb_model/parser/os_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |