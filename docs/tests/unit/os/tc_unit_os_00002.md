# Test Case: TC_UNIT_OS_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00002 |
| Title | OS Model - Task Attribute Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts all task attributes from XDM configuration containers, creates OsTask model objects, and establishes proper parent-child relationships. This test ensures task data is accurately modeled and accessible.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsTask containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Task Name | "Task1" | Example task identifier |
| Task Priority | 5 | Task priority value |
| Task Activation | 1 | Number of activations |
| Schedule Type | "FULL" | Preemptive/Non-preemptive scheduling |
| Stack Size | 1024 | Stack size in bytes |
| Autostart | true | Task auto-start flag |
| Application Reference | "App1" | Application mapping reference |
| Task Attributes List | All 15+ task attributes | Verify complete attribute extraction |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsTask container | OsTask object created successfully |
| 2 | Verify task name extraction | getName() returns "Task1" |
| 3 | Verify task priority extraction | getPriority() returns 5 |
| 4 | Verify task activation extraction | getActivation() returns 1 |
| 5 | Verify schedule type extraction | getScheduleType() returns "FULL" |
| 6 | Verify stack size extraction | getStackSize() returns 1024 |
| 7 | Verify autostart flag extraction | isAutostart() returns true |
| 8 | Verify application reference extraction | getApplication() returns "App1" |
| 9 | Verify parent-child relationship | Task's parent is OS module |
| 10 | Verify O(1) lookup performance | Task retrieval by name is constant time |

## Expected Results

- All task attributes are extracted correctly
- Task object is properly registered with parent module
- Parent-child relationship is established
- Task lookup by name is O(1) using dictionary
- Task full name includes parent hierarchy

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsTask objects remain in memory for verification |
| 2 | EBModel contains updated task collection |
| 3 | No orphaned task objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00002 | Task Management - Task attribute extraction and modeling | Covered |
| SWR_OS_00014 | Non-Functional - O(1) lookup performance using dictionary | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |