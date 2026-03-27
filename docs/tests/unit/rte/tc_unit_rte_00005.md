# Test Case: TC_UNIT_RTE_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00005 |
| Title | RTE Model - AR 3.x Version Support |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly handles AUTOSAR 3.x version specific elements and attributes, including 3.x specific data structures and XML schemas.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | AUTOSAR 3.x XDM file is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| AUTOSAR Version | "3.2.1" | AUTOSAR 3.x version identifier |
| AR3 Specific Element | "DataReceivedEvent" | 3.x specific event type |
| AR3 Specific Attribute | "RunnableEntity" | 3.x specific attribute |
| XML Namespace | AUTOSAR 3.x namespace | 3.x specific XML namespace |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse AUTOSAR 3.x XDM file | File parses successfully with AR 3.x handling |
| 2 | Verify version detection | AR version detected as 3.x |
| 3 | Extract AR 3.x specific elements | Elements parsed correctly |
| 4 | Extract AR 3.x specific attributes | Attributes parsed correctly |
| 5 | Validate AR 3.x XML namespace | Namespace recognized as AUTOSAR 3.x |
| 6 | Verify BSW component structure for AR 3.x | Structure matches AR 3.x schema |
| 7 | Verify SW component structure for AR 3.x | Structure matches AR 3.x schema |
| 8 | Verify port definitions for AR 3.x | Port structure matches AR 3.x format |
| 9 | Handle AR 3.x specific runnable entities | Runnable entities extracted correctly |
| 10 | Validate AR 3.x specific features | All 3.x specific features work correctly |

## Expected Results

- AUTOSAR 3.x version is detected correctly
- AR 3.x specific elements and attributes are handled
- XML namespace is recognized correctly
- BSW and SW component structures match AR 3.x schema
- Port definitions follow AR 3.x format
- Runnable entities are extracted correctly
- No AR 4.x specific features are expected or required
- Parser adapts to AR 3.x differences from AR 4.x

## Post-conditions

| # | Description |
|---|-------------|
| 1 | RTE model objects for AR 3.x remain in memory |
| 2 | EBModel contains AR 3.x specific data |
| 3 | Parser can be reused for AR 4.x files |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00005 | AR 3.x Version Support | Covered |
| SWR_RTE_00011 | Non-Functional - AR 3.x specific handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Parser Documentation | ../../src/eb_model/parser/rte_xdm_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |