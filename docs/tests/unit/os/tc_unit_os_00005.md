# Test Case: TC_UNIT_OS_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00005 |
| Title | OS Model - Counter Configuration Parsing |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts counter configurations from XDM containers, including counter limits, cycle times, and driver references.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsCounter containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Counter Name | "Counter1" | Example counter identifier |
| Max Allowed Value | 65535 | Maximum counter value |
| Min Cycle | 1 | Minimum cycle in ticks |
| Ticks Per Base | 1000 | Ticks per base counter |
| Counter Type | "SOFTWARE" | Counter type (Software/Hardware) |
| Driver Reference | "GptChannel1" | Hardware driver reference |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsCounter container | OsCounter object created successfully |
| 2 | Verify counter name extraction | getName() returns "Counter1" |
| 3 | Verify max allowed value extraction | getMaxAllowedValue() returns 65535 |
| 4 | Verify min cycle extraction | getMinCycle() returns 1 |
| 5 | Verify ticks per base extraction | getTicksPerBase() returns 1000 |
| 6 | Verify counter type extraction | getCounterType() returns "SOFTWARE" |
| 7 | Verify driver reference extraction | getDriver() returns "GptChannel1" |
| 8 | Verify parent-child relationship | Counter's parent is OS module |
| 9 | Handle software counter (no driver) | Driver reference is null for software counters |
| 10 | Handle hardware counter | Driver reference is populated for hardware counters |

## Expected Results

- All counter attributes are extracted correctly
- Software counters have null driver reference
- Hardware counters have valid driver reference
- Counter limits are correctly validated
- Counter is properly registered with parent module

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsCounter objects remain in memory for verification |
| 2 | EBModel contains updated counter collection |
| 3 | No orphaned counter objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00005 | Counters - Counter configuration parsing including driver references | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |