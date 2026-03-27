# Test Case: TC_UNIT_OS_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00006 |
| Title | OS Model - Application Mapping |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts application configurations from XDM containers and establishes mapping relationships between applications and their associated tasks and ISRs.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsApplication containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Application Name | "App1" | Example application identifier |
| Application Description | "Safety Application" | Application description |
| Application ID | 1 | Application identifier |
| Mapped Task | "Task1" | Task mapped to application |
| Mapped ISR | "Isr1" | ISR mapped to application |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsApplication container | OsApplication object created successfully |
| 2 | Verify application name extraction | getName() returns "App1" |
| 3 | Verify application description extraction | getDescription() returns "Safety Application" |
| 4 | Verify application ID extraction | getApplicationId() returns 1 |
| 5 | Verify task-to-application mapping | Task1 maps to App1 |
| 6 | Verify ISR-to-application mapping | Isr1 maps to App1 |
| 7 | Verify application-to-tasks lookup | getTasks() returns list of mapped tasks |
| 8 | Verify application-to-ISRs lookup | getIsrs() returns list of mapped ISRs |
| 9 | Verify bidirectional reference | Task's getApplication() returns App1 |
| 10 | Verify bidirectional reference | ISR's getApplication() returns App1 |

## Expected Results

- All application attributes are extracted correctly
- Task-to-application mappings are established bidirectionally
- ISR-to-application mappings are established bidirectionally
- Application lookup returns correct associated entities
- No orphaned mappings exist

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsApplication objects remain in memory for verification |
| 2 | EBModel contains updated application collection |
| 3 | Task and ISR objects have valid application references |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00006 | Applications - Application mapping and task/ISR lookup | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |