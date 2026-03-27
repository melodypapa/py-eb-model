# Test Case: TC_INT_CROSS_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_CROSS_00001 |
| Title | Cross-Module - OS and RTE Integration |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the integration between OS and RTE modules, ensuring that RTE event-to-task mappings correctly reference OS tasks and that bidirectional relationships are maintained.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | OS XDM file with tasks is available |
| 3 | RTE XDM file with event mappings is available |
| 4 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| OS XDM File | `data/test/Os_with_tasks.xdm` | OS file with defined tasks |
| RTE XDM File | `data/test/Rte_with_events.xdm` | RTE file with event mappings |
| OS Tasks | List of task names | Tasks referenced by RTE events |
| RTE Events | List of event names | Events referencing OS tasks |
| Mappings | Event-to-task relationships | Integration points between modules |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse OS XDM file | OS model populated with tasks |
| 2 | Parse RTE XDM file | RTE model populated with events |
| 3 | Verify event-to-task references | Events reference OS tasks correctly |
| 4 | Verify task lookup by name | OS tasks accessible to RTE |
| 5 | Verify bidirectional relationship | Tasks can access associated events |
| 6 | Generate combined Excel report | Both OS and RTE data in workbook |
| 7 | Verify OS worksheet | OS tasks present |
| 8 | Verify RTE worksheet | RTE events present |
| 9 | Verify event task references | Task names visible in RTE worksheet |
| 10 | Reset EBModel and re-parse | Integration works consistently |

## Expected Results

- OS and RTE modules parse successfully in sequence
- RTE event-to-task references are resolved correctly
- Bidirectional relationships are established
- Combined reports include both module data
- Integration is consistent across multiple parses

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Combined output file persists for review |
| 2 | EBModel contains both OS and RTE data |
| 3 | No reference resolution errors |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00002 | Task Management - Task extraction and modeling | Covered |
| SWR_RTE_00004 | Event to Task Mapping | Covered |
| SWR_PARSER_00001 | Abstract Parser - XML parsing and namespace handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Requirement Document | ../requirements/swr_rte-module.md |
| System Overview | ../requirements/overview.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |