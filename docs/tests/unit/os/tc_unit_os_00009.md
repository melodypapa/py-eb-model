# Test Case: TC_UNIT_OS_00009

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00009 |
| Title | OS Model - Memory Protection Parsing |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts memory protection configurations from XDM containers, including microkernel configuration and memory region definitions.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing memory protection containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Microkernel Use | true | Microkernel enabled flag |
| Memory Region Name | "Region1" | Memory region identifier |
| Region Start Address | 0x10000000 | Region start address |
| Region End Address | 0x10000FFF | Region end address |
| Region Access | "READ_WRITE" | Access permissions |
| Region Application | "App1" | Application owning region |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with memory protection container | Memory protection object created successfully |
| 2 | Verify microkernel enabled extraction | isMicrokernelUsed() returns true |
| 3 | Verify memory region extraction | Memory region object created |
| 4 | Verify region name extraction | getName() returns "Region1" |
| 5 | Verify region start address extraction | getStartAddress() returns 0x10000000 |
| 6 | Verify region end address extraction | getEndAddress() returns 0x10000FFF |
| 7 | Verify region access permissions extraction | getAccess() returns "READ_WRITE" |
| 8 | Verify region application extraction | getApplication() returns "App1" |
| 9 | Validate address range | Start address < end address |

## Expected Results

- Microkernel configuration is extracted correctly
- Memory region attributes are extracted correctly
- Access permissions are validated
- Application ownership is established
- Address ranges are validated

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Memory protection objects remain in memory for verification |
| 2 | EBModel contains updated memory protection collection |
| 3 | No orphaned memory regions exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00009 | Memory Protection - Microkernel configuration and memory region parsing | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |