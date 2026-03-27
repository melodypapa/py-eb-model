# Test Case: TC_INT_PARSER_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_PARSER_00001 |
| Title | Parser Layer - Multi-Module Parsing |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that the parser layer can handle multiple XDM files in sequence, correctly instantiating different parsers and maintaining clean state between parsing operations.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XDM files for multiple modules are available |
| 3 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| OS XDM File | `data/test/Os.xdm` | OS module file |
| RTE XDM File | `data/test/Rte.xdm` | RTE module file |
| NVM XDM File | `data/test/NvM.xdm` | NVM module file |
| CanIf XDM File | `data/test/CanIf.xdm` | CanIf module file |
| Total Files | 4+ | Multiple files for testing |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse OS XDM file | OsXdmParser instantiated, OS model created |
| 2 | Verify OS model populated | OS entities present in model |
| 3 | Parse RTE XDM file | RteXdmParser instantiated, RTE model created |
| 4 | Verify RTE model populated | RTE entities present in model |
| 5 | Verify OS model still present | OS entities not overwritten |
| 6 | Parse NVM XDM file | NvMXdmParser instantiated, NVM model created |
| 7 | Verify NVM model populated | NVM entities present in model |
| 8 | Verify all models present | OS, RTE, NVM entities all present |
| 9 | Reset EBModel singleton | Model is clean |
| 10 | Parse CanIf XDM file | CanIfXdmParser instantiated, CanIf model created |

## Expected Results

- Each module is parsed with correct parser
- All models are populated correctly
- Models don't interfere with each other
- EBModel singleton maintains state correctly
- Reset functionality works
- Multiple parsing operations work in sequence

## Post-conditions

| # | Description |
|---|-------------|
| 1 | EBModel contains all parsed modules |
| 2 | Parser layer is stable |
| 3 | No memory leaks from multiple parses |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00001 | Abstract Parser - XML parsing and namespace handling | Covered |
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