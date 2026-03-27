# Test Case: TC_INT_CROSS_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_CROSS_00004 |
| Title | Cross-Module - Multi-Module Excel Export |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify that multiple modules can be parsed and exported to a single Excel workbook with all module data in separate worksheets.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XDM files for multiple modules are available |
| 3 | EBModel singleton is clean |
| 4 | Output directory is writable |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| OS XDM File | `data/test/Os.xdm` | OS module |
| RTE XDM File | `data/test/Rte.xdm` | RTE module |
| NVM XDM File | `data/test/NvM.xdm` | NVM module |
| EcuC XDM File | `data/test/EcuC.xdm` | EcuC module |
| Output File | `test_output/Multi_module.xlsx` | Combined workbook |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse OS XDM file | OS model populated |
| 2 | Parse RTE XDM file | RTE model populated |
| 3 | Parse NVM XDM file | NVM model populated |
| 4 | Parse EcuC XDM file | EcuC model populated |
| 5 | Generate combined Excel workbook | Single file with all module worksheets |
| 6 | Verify OS worksheets | OsTask, OsIsr, etc. present |
| 7 | Verify RTE worksheets | BswComponent, SwComponent present |
| 8 | Verify NVM worksheets | NvM module worksheets present |
| 9 | Verify EcuC worksheets | EcuC module worksheets present |
| 10 | Verify worksheet naming | No naming conflicts between modules |

## Expected Results

- All modules parse successfully
- Single Excel file contains all module data
- All expected worksheets are present
- Worksheet names don't conflict
- Data is correctly separated by module
- File is valid Excel format

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Combined output file persists for review |
| 2 | EBModel contains all module data |
| 3 | No data corruption between modules |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00009 | EbParserFactory - Parser type determination | Covered |
| SWR_REPORTER_00002 | Excel Reporter - Worksheet management | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Requirement Document | ../requirements/swr_reporter-layer.md |
| System Overview | ../requirements/overview.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |