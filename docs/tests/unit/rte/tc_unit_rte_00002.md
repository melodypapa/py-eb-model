# Test Case: TC_UNIT_RTE_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00002 |
| Title | RTE Model - BSW Component Instance Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly extracts Basic Software (BSW) component instance configurations from XDM containers, creating BswComponentInstance model objects with all relevant attributes.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing BSW component instance containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| BSW Component Name | "BswComponent1" | Example BSW component identifier |
| BSW Component Type | "CanIf" | BSW component type |
| BSW Component Version | "1.2.3" | Component version |
| BSW Component Instance | "CanIf_1" | Specific instance name |
| Init Function | "CanIf_Init" | Initialization function name |
| Provider Port Count | 3 | Number of provider ports |
| Requester Port Count | 2 | Number of requester ports |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with BSW component instance container | BswComponentInstance object created successfully |
| 2 | Verify component name extraction | getName() returns "BswComponent1" |
| 3 | Verify component type extraction | getType() returns "CanIf" |
| 4 | Verify component version extraction | getVersion() returns "1.2.3" |
| 5 | Verify instance name extraction | getInstanceName() returns "CanIf_1" |
| 6 | Verify init function extraction | getInitFunction() returns "CanIf_Init" |
| 7 | Verify provider port count extraction | getProviderPortCount() returns 3 |
| 8 | Verify requester port count extraction | getRequesterPortCount() returns 2 |
| 9 | Verify parent-child relationship | Component's parent is RTE module |
| 10 | Verify O(1) lookup performance | Component retrieval by name is constant time |

## Expected Results

- All BSW component attributes are extracted correctly
- Component object is properly registered with parent module
- Parent-child relationship is established
- Component lookup by name is O(1) using dictionary
- Component full name includes parent hierarchy

## Post-conditions

| # | Description |
|---|-------------|
| 1 | BswComponentInstance objects remain in memory for verification |
| 2 | EBModel contains updated BSW component collection |
| 3 | No orphaned component objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00002 | BSW Component Instance Extraction | Covered |
| SWR_RTE_00009 | Non-Functional - O(1) lookup performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |