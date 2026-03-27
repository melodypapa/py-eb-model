# Test Case: TC_UNIT_RTE_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_RTE_00004 |
| Title | RTE Model - Event to Task Mapping |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the RTE parser correctly extracts event-to-task mapping configurations from XDM containers, establishing relationships between RTE events and OS tasks.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing event-to-task mapping containers is available |
| 3 | EBModel singleton is initialized with OS module |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Event Name | "Event1" | Example event identifier |
| Event Type | "DataReceivedEvent" | RTE event type |
| Mapped Task | "Task1" | OS task that handles this event |
| Event Priority | 5 | Event priority |
| Event Mask | 0xFF | Event mask value |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with event-to-task mapping container | EventMapping object created successfully |
| 2 | Verify event name extraction | getName() returns "Event1" |
| 3 | Verify event type extraction | getType() returns "DataReceivedEvent" |
| 4 | Verify mapped task extraction | getMappedTask() returns "Task1" |
| 5 | Verify event priority extraction | getPriority() returns 5 |
| 6 | Verify event mask extraction | getMask() returns 0xFF |
| 7 | Verify bidirectional relationship | Task's getEvents() includes this event |
| 8 | Validate task reference exists | Referenced task is found in OS module |
| 9 | Handle unmapped events | Events without task reference don't cause error |
| 10 | Verify parent-child relationship | Event's parent is RTE module |

## Expected Results

- All event attributes are extracted correctly
- Task reference is correctly resolved when present
- Bidirectional relationship is established between event and task
- Events without task references are handled gracefully
- Parent-child relationship is established
- Event lookup is efficient

## Post-conditions

| # | Description |
|---|-------------|
| 1 | EventMapping objects remain in memory for verification |
| 2 | EBModel contains updated event mapping collection |
| 3 | No orphaned event objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_RTE_00004 | Event to Task Mapping | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_rte-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |