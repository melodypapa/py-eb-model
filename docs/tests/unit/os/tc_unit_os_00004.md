# Test Case: TC_UNIT_OS_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00004 |
| Title | OS Model - Schedule Table Parsing |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts schedule table configurations from XDM containers, including table attributes and expiry points with their actions.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsScheduleTable containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Schedule Table Name | "Schedule1" | Example schedule table identifier |
| Duration | 100 | Schedule table duration in ticks |
| Repeating | true | Table repeats cyclically |
| Counter Reference | "Counter1" | Associated counter reference |
| Expiry Point Offset | 0 | First expiry point offset |
| Expiry Point Action | "ACTIVATE_TASK" | Action type (ActivateTask, SetEvent, etc.) |
| Action Target | "Task1" | Target task/event for action |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsScheduleTable container | OsScheduleTable object created successfully |
| 2 | Verify schedule table name extraction | getName() returns "Schedule1" |
| 3 | Verify duration extraction | getDuration() returns 100 |
| 4 | Verify repeating flag extraction | isRepeating() returns true |
| 5 | Verify counter reference extraction | getCounter() returns "Counter1" |
| 6 | Verify expiry point extraction | Expiry points list is populated |
| 7 | Verify expiry point offset | First expiry point offset is 0 |
| 8 | Verify expiry point action | Action type is "ACTIVATE_TASK" |
| 9 | Verify expiry point target | Target is "Task1" |
| 10 | Verify expiry point sorting | Expiry points are sorted by offset |

## Expected Results

- Schedule table attributes are extracted correctly
- All expiry points are extracted and maintained
- Expiry point actions are correctly mapped
- Expiry points are sorted by offset value
- Counter reference is correctly resolved

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsScheduleTable objects remain in memory for verification |
| 2 | EBModel contains updated schedule table collection |
| 3 | No orphaned expiry points exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00004 | Schedule Tables - Schedule table and expiry point extraction | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |