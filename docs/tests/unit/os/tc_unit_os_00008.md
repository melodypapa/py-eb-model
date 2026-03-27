# Test Case: TC_UNIT_OS_00008

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00008 |
| Title | OS Model - Resource Configuration Parsing |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts resource configurations from XDM containers, including resource properties and service access references.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsResource containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Resource Name | "Resource1" | Example resource identifier |
| Resource Property | "STANDARD" | Resource property (Standard, Link, etc.) |
| Scheduler Access | "FULL" | Scheduler access level |
| Service Access Reference | "Service1" | Service that uses this resource |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsResource container | OsResource object created successfully |
| 2 | Verify resource name extraction | getName() returns "Resource1" |
| 3 | Verify resource property extraction | getResourceProperty() returns "STANDARD" |
| 4 | Verify scheduler access extraction | getSchedulerAccess() returns "FULL" |
| 5 | Verify service access reference extraction | getServiceAccess() returns "Service1" |
| 6 | Validate resource property | Property is one of valid types (Standard, Link) |
| 7 | Validate scheduler access | Access level is valid (Full, Non) |
| 8 | Verify parent-child relationship | Resource's parent is OS module |

## Expected Results

- All resource attributes are extracted correctly
- Resource property is validated against supported types
- Scheduler access is validated
- Service access reference is correctly resolved
- Resource is properly registered with parent module

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsResource objects remain in memory for verification |
| 2 | EBModel contains updated resource collection |
| 3 | No orphaned resource objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00008 | Resources - Resource configuration and service access parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |