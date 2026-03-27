# Test Case: TC_UNIT_PARSER_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_PARSER_00006 |
| Title | EbParserFactory - Parser Type Determination |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EbParserFactory correctly determines the parser type from XDM file's MODULE-CONFIGURATION tag and instantiates the appropriate parser class.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XDM files for various modules are available |
| 3 | EbParserFactory is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| OS XDM File | MODULE-CONFIGURATION choice="Os" | Test OS parser selection |
| RTE XDM File | MODULE-CONFIGURATION choice="Rte" | Test RTE parser selection |
| NVM XDM File | MODULE-CONFIGURATION choice="NvM" | Test NvM parser selection |
| CanIf XDM File | MODULE-CONFIGURATION choice="CanIf" | Test CanIf parser selection |
| Invalid Module | MODULE-CONFIGURATION choice="InvalidModule" | Test error handling |
| Missing Choice | No MODULE-CONFIGURATION choice | Test error handling |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Call EbParserFactory.create() with OS XDM file | Returns OsXdmParser instance |
| 2 | Call EbParserFactory.create() with RTE XDM file | Returns RteXdmParser instance |
| 3 | Call EbParserFactory.create() with NVM XDM file | Returns NvMXdmParser instance |
| 4 | Call EbParserFactory.create() with CanIf XDM file | Returns CanIfXdmParser instance |
| 5 | Call with invalid module choice | Raises ValueError with appropriate message |
| 6 | Call with missing choice | Raises ValueError with appropriate message |
| 7 | Verify parser type is correct | Returned parser is instance of expected class |
| 8 | Verify parser is initialized | Parser can be used for parsing |
| 9 | Test all registered module parsers | All 32 modules can be instantiated |
| 10 | Verify factory pattern usage | Factory returns proper parser for each type |

## Expected Results

- Correct parser is instantiated for each module type
- Invalid module choices raise ValueError
- Missing choices raise ValueError
- Returned parsers are properly initialized
- All registered modules work through factory
- Factory pattern is implemented correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Parsers can be used for parsing |
| 2 | Factory state is unchanged |
| 3 | No side effects from factory calls |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00009 | EbParserFactory - Parser type determination | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Factory Documentation | ../../src/eb_model/parser/eb_parser_factory.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |