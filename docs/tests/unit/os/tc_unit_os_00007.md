# Test Case: TC_UNIT_OS_00007

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00007 |
| Title | OS Model - Alarm Action Parsing |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts alarm configurations from XDM containers, including alarm attributes and action definitions with their targets.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsAlarm containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Alarm Name | "Alarm1" | Example alarm identifier |
| Alarm Action | "ACTIVATE_TASK" | Action type (ActivateTask, SetEvent, Callback, etc.) |
| Action Target | "Task1" | Target task/event for action |
| Cycle | 100 | Alarm cycle time in ticks |
| Counter Reference | "Counter1" | Associated counter reference |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsAlarm container | OsAlarm object created successfully |
| 2 | Verify alarm name extraction | getName() returns "Alarm1" |
| 3 | Verify alarm action extraction | getAction() returns "ACTIVATE_TASK" |
| 4 | Verify action target extraction | getActionTarget() returns "Task1" |
| 5 | Verify cycle extraction | getCycle() returns 100 |
| 6 | Verify counter reference extraction | getCounter() returns "Counter1" |
| 7 | Validate action type | Action is one of valid types (ActivateTask, SetEvent, Callback, IncrementCounter) |
| 8 | Validate target reference | Target reference resolves to valid object |
| 9 | Verify parent-child relationship | Alarm's parent is OS module |

## Expected Results

- All alarm attributes are extracted correctly
- Action type is validated against supported types
- Target reference is correctly resolved
- Counter reference is correctly resolved
- Alarm is properly registered with parent module

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsAlarm objects remain in memory for verification |
| 2 | EBModel contains updated alarm collection |
| 3 | No orphaned alarm objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00007 | Alarms - Alarm configuration and action parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |