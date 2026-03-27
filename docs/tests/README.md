# py-eb-model Test Case Documentation

This directory contains ISO/IEC/IEEE 29119-3 compliant test case documentation for the py-eb-model project.

## Overview

py-eb-model is a Python parser engine for EB Tresos XDM (XML Data Model) files used in AUTOSAR automotive software development. This test documentation provides complete traceability from software requirements (SWR) to test cases.

## Document Structure

```
docs/tests/
├── README.md                           # This file
├── template.md                         # ISO 29119 test case template
├── registry.md                         # Test case traceability matrix
├── unit/                               # Unit test cases
└── integration/                        # Integration test cases
```

## Test Case Organization

### Test Case ID Format

Test cases use the format: `TC_<TYPE>_<MODULE>_<NUMBER>`

- **TYPE**: `UNIT` (unit test) or `INT` (integration test)
- **MODULE**: Uppercase module identifier (OS, RTE, NVM, etc.)
- **NUMBER**: 5-digit sequential number

Examples: `TC_UNIT_OS_00001`, `TC_INT_RTE_00001`

### Test Types

#### Unit Tests (`TC_UNIT_*`)
Test individual components in isolation:
- Parser method functionality
- Model class methods
- Reporter generation methods
- CLI argument parsing
- Utility functions

#### Integration Tests (`TC_INT_*`)
Test component interactions and workflows:
- End-to-end parsing workflows
- Parser + model + reporter integration
- CLI command execution
- Cross-module data flow
- File I/O operations

## Module Coverage

The test documentation covers all 32 modules/layers:

| Category | Modules |
|----------|---------|
| Core | OS, RTE, NVM, EcuC, BswM |
| CAN Stack | CanIf, CanNm, CanSm, CanTp |
| LIN Stack | LinIf, LinSm, LinTp |
| FlexRay Stack | FrIf, FrNm, FrSm, FrTp, FrArTp |
| Ethernet Stack | EthIf, EthSm, DoIP, SoAd, SomeIpTp, TcpIp, UdpNm |
| System | Det, EcuM, Tm, PbcfgM |
| Infrastructure | Parser, Reporter, CLI |

## Requirements Traceability

All test cases trace back to software requirements (SWR IDs) defined in `docs/requirements/`. The `registry.md` file provides:

- Forward traceability: Test cases → Requirements covered
- Reverse traceability: Requirements → Test cases covering them
- Coverage statistics by module

## Using This Documentation

### For Testers

1. Navigate to the appropriate test type directory (`unit/` or `integration/`)
2. Select the module directory
3. Review individual test case files for detailed test specifications

### For Developers

1. Use `registry.md` to find tests covering specific requirements
2. Refer to test case files for expected behavior
3. Update test cases when requirements change

### For Auditors

1. Review `registry.md` for complete traceability
2. Verify ISO 29119-3 compliance in test case files
3. Check coverage statistics for audit requirements

## Standards Compliance

All test cases follow ISO/IEC/IEEE 29119-3:2013 (Software and systems engineering — Software testing — Part 3: Test documentation).

Key compliance features:
- Complete test case specification
- Clear preconditions and post-conditions
- Detailed test steps with expected results
- Requirements traceability
- Version tracking

## Related Documentation

- [Software Requirements](../requirements/requirements.md) - Complete SWR registry
- [System Overview](../requirements/overview.md) - Architecture documentation
- [Test Case Template](template.md) - ISO 29119-3 compliant template

## Document Control

| Field | Value |
|-------|-------|
| Document Title | py-eb-model Test Case Documentation |
| Document ID | TC_OVERVIEW_00001 |
| Version | 1.0 |
| Date | 2026-03-27 |
| Standard | ISO/IEC/IEEE 29119-3:2013 |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test documentation structure |