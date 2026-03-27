# Test Case: TC_UNIT_PARSER_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_PARSER_00003 |
| Title | Abstract Parser - Reference Reading Methods |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the AbstractEbModelParser's read_ref_value() and read_ref_raw_value() methods correctly extract AUTOSAR path references from XML elements, handling both direct references and calculated references.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML file with various reference types is available |
| 3 | AbstractEbModelParser subclass is instantiated |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Direct Reference | "ASPath:/Os/Task1" | Simple ASPath reference |
| Nested Reference | "ASPath:/EcuC/Partition1/Task2" | Nested ASPath reference |
| Calculated Reference | "@CALC(SvcAs:/Os/Task1)" | Calculated reference |
| Complex Calculated Reference | "@CALC(SvcAs:/Os/Counter1) + 100" | Calculated reference with expression |
| Missing Reference | Element missing | Test missing reference handling |
| Invalid Reference | "NotASPath:/Invalid" | Test invalid reference format |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Read direct reference using read_ref_value() | Returns "ASPath:/Os/Task1" |
| 2 | Read nested reference using read_ref_value() | Returns "ASPath:/EcuC/Partition1/Task2" |
| 3 | Read calculated reference using read_ref_raw_value() | Returns "@CALC(SvcAs:/Os/Task1)" |
| 4 | Extract ASPath from calculated reference | Returns "/Os/Task1" |
| 5 | Read complex calculated reference | Returns full calculated expression |
| 6 | Read missing reference using read_ref_value() | Returns None or empty string |
| 7 | Read invalid reference format | Handles gracefully or raises error |
| 8 | Verify reference format validation | Valid ASPath format is recognized |
| 9 | Verify calculated reference detection | Calculated references are identified |
| 10 | Test reference path extraction | Path component extracted correctly |

## Expected Results

- Direct references are read correctly
- Calculated references are identified and processed
- ASPath format is validated
- Path extraction works for calculated references
- Missing references return None
- Invalid references are handled appropriately
- Reference format is preserved
- Calculated expressions are not evaluated (returned as-is)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Read references are available to calling code |
| 2 | Parser state is unchanged after reading |
| 3 | No side effects on XML element tree |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00003 | Abstract Parser - Reference reading methods | Covered |
| SWR_PARSER_00008 | Non-Functional - ASPath reference handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Parser Documentation | ../../src/eb_model/parser/abstract_eb_model_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |