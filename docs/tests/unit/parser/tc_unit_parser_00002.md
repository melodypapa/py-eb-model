# Test Case: TC_UNIT_PARSER_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_PARSER_00002 |
| Title | Abstract Parser - Value Reading Methods |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the AbstractEbModelParser's read_value() and read_optional_value() methods correctly extract values from XML elements, handling different data types and optional elements.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML file with various value types is available |
| 3 | AbstractEbModelParser subclass is instantiated |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| BOOLEAN Value | "true" | Boolean data type |
| INTEGER Value | "42" | Integer data type |
| FLOAT Value | "3.14159" | Float data type |
| STRING Value | "Test String" | String data type |
| ENUMERATION Value | "SCHEDULE_FULL" | Enumeration data type |
| Optional Value Present | Value is present | Test read_optional_value() with present value |
| Optional Value Missing | Element missing ENABLE="false" | Test read_optional_value() with missing value |
| ENABLE Attribute | "true" | Element is enabled |
| DISABLE Attribute | "false" | Element is disabled |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Read BOOLEAN value using read_value() | Returns boolean "true" |
| 2 | Read INTEGER value using read_value() | Returns integer 42 |
| 3 | Read FLOAT value using read_value() | Returns float 3.14159 |
| 4 | Read STRING value using read_value() | Returns string "Test String" |
| 5 | Read ENUMERATION value using read_value() | Returns "SCHEDULE_FULL" |
| 6 | Read optional value with ENABLE="true" | Returns value |
| 7 | Read optional value with ENABLE="false" | Returns None or empty string |
| 8 | Read optional value with missing element | Returns None or empty string |
| 9 | Read required value that is missing | Raises appropriate error |
| 10 | Verify type conversion for numeric values | Numeric values are converted correctly |

## Expected Results

- All data types are read correctly
- Boolean values are properly converted
- Numeric values maintain precision
- String values are returned as-is
- Enumeration values are returned as strings
- Optional values with ENABLE="false" return None
- Missing optional values return None
- Missing required values raise errors
- Type conversion is accurate

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Read values are available to calling code |
| 2 | Parser state is unchanged after reading |
| 3 | No side effects on XML element tree |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00002 | Abstract Parser - Value reading methods | Covered |
| SWR_PARSER_00007 | Non-Functional - Type handling for values | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Parser Documentation | ../../src/eb_model/parser/abstract_eb_model_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |