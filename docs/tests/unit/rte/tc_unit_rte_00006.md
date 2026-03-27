# Test Case: TC_UNIT_RTE_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00006 |
| Title | RTE Model - AR 4.x Version Support |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly handles AUTOSAR 4.x version specific elements and attributes, including 4.x specific data structures, port interfaces, and communication patterns.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | AUTOSAR 4.x XDM file is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| AUTOSAR Version | "4.3.0" | AUTOSAR 4.x version identifier |
| AR4 Specific Element | "ModeSwitchEvent" | 4.x specific event type |
| AR4 Specific Attribute | "ServiceNeeds" | 4.x specific attribute |
| XML Namespace | AUTOSAR 4.x namespace | 4.x specific XML namespace |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse AUTOSAR 4.x XDM file | File parses successfully with AR 4.x handling |
| 2 | Verify version detection | AR version detected as 4.x |
| 3 | Extract AR 4.x specific elements | Elements parsed correctly |
| 4 | Extract AR 4.x specific attributes | Attributes parsed correctly |
| 5 | Validate AR 4.x XML namespace | Namespace recognized as AUTOSAR 4.x |
| 6 | Verify BSW component structure for AR 4.x | Structure matches AR 4.x schema |
| 7 | Verify SW component structure for AR 4.x | Structure matches AR 4.x schema |
| 8 | Verify port interface definitions for AR 4.x | Port interfaces follow AR 4.x format |
| 9 | Handle AR 4.x specific communication patterns | Communication patterns extracted correctly |
| 10 | Validate AR 4.x specific features | All 4.x specific features work correctly |

## Expected Results

- AUTOSAR 4.x version is detected correctly
- AR 4.x specific elements and attributes are handled
- XML namespace is recognized correctly
- BSW and SW component structures match AR 4.x schema
- Port interface definitions follow AR 4.x format
- Communication patterns are extracted correctly
- No AR 3.x specific features are expected or required
- Parser adapts to AR 4.x differences from AR 3.x

## Post-conditions

| # | Description |
|---|-------------|
| 1 | RTE model objects for AR 4.x remain in memory |
| 2 | EBModel contains AR 4.x specific data |
| 3 | Parser can be reused for AR 3.x files |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00006 | AR 4.x Version Support | Covered |
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