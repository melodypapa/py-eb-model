# Test Case: TC_UNIT_RTE_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00003 |
| Title | RTE Model - SW Component Instance Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly extracts Software (SW) component instance configurations from XDM containers, creating SwComponentInstance model objects with all relevant attributes.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing SW component instance containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| SW Component Name | "SwComponent1" | Example SW component identifier |
| SW Component Type | "ApplicationComponent" | SW component type |
| SW Component Version | "2.0.0" | Component version |
| SW Component Instance | "App_Swc_1" | Specific instance name |
| Runnable Entity Count | 5 | Number of runnable entities |
| Port Count | 4 | Number of ports |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with SW component instance container | SwComponentInstance object created successfully |
| 2 | Verify component name extraction | getName() returns "SwComponent1" |
| 3 | Verify component type extraction | getType() returns "ApplicationComponent" |
| 4 | Verify component version extraction | getVersion() returns "2.0.0" |
| 5 | Verify instance name extraction | getInstanceName() returns "App_Swc_1" |
| 6 | Verify runnable entity count extraction | getRunnableEntityCount() returns 5 |
| 7 | Verify port count extraction | getPortCount() returns 4 |
| 8 | Verify parent-child relationship | Component's parent is RTE module |
| 9 | Verify O(1) lookup performance | Component retrieval by name is constant time |

## Expected Results

- All SW component attributes are extracted correctly
- Component object is properly registered with parent module
- Parent-child relationship is established
- Component lookup by name is O(1) using dictionary
- Component full name includes parent hierarchy

## Post-conditions

| # | Description |
|---|-------------|
| 1 | SwComponentInstance objects remain in memory for verification |
| 2 | EBModel contains updated SW component collection |
| 3 | No orphaned component objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00003 | SW Component Instance Extraction | Covered |
| SWR_RTE_00010 | Non-Functional - O(1) lookup performance | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |