# Test Case: TC_INT_RTE_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_RTE_00003 |
| Title | RTE Module - Mixed Version Handling |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | Medium |

## Purpose/Objective

Verify that the RTE parser can handle switching between AR 3.x and AR 4.x versions within a single session, correctly adapting to each version's specific features and schemas.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Both AR 3.x and AR 4.x test files are available |
| 3 | Output directory is writable |
| 4 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| AR3 Input File | `data/test/Rte_ar3.xdm` | AR 3.x test file |
| AR4 Input File | `data/test/Rte_ar4.xdm` | AR 4.x test file |
| AR3 Output File | `test_output/Rte_ar3.xlsx` | AR 3.x output |
| AR4 Output File | `test_output/Rte_ar4.xlsx` | AR 4.x output |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse AR 3.x file | File parsed successfully, AR 3.x mode activated |
| 2 | Generate AR 3.x Excel output | Output file created with AR 3.x structure |
| 3 | Reset EBModel singleton | EBModel is clean, no AR 3.x artifacts |
| 4 | Parse AR 4.x file | File parsed successfully, AR 4.x mode activated |
| 5 | Generate AR 4.x Excel output | Output file created with AR 4.x structure |
| 6 | Verify no cross-version contamination | AR 3.x data not in AR 4.x output and vice versa |
| 7 | Verify AR 3.x specific features in AR 3.x output | Runnable entities, port structure correct |
| 8 | Verify AR 4.x specific features in AR 4.x output | Port interfaces, communication patterns correct |
| 9 | Parse AR 3.x file again | Parser correctly switches back to AR 3.x mode |
| 10 | Generate second AR 3.x output | Output matches first AR 3.x output |

## Expected Results

- Parser correctly switches between AR 3.x and AR 4.x modes
- Each version's specific features are handled correctly
- No cross-version contamination occurs
- Multiple version switches work correctly
- Outputs for same version are consistent

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Both output files persist for review |
| 2 | EBModel can be reset for next test |
| 3 | No version state pollution remains |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00005 | AR 3.x Version Support | Covered |
| SWR_RTE_00006 | AR 4.x Version Support | Covered |
| SWR_RTE_00011 | Non-Functional - AR 3.x specific handling | Covered |
| SWR_RTE_00012 | Non-Functional - AR 4.x specific handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Parser Documentation | ../../src/eb_model/parser/rte_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |