# Test Case: TC_UNIT_OS_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_OS_00003 |
| Title | OS Model - ISR Attribute Extraction |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the OS parser correctly extracts ISR (Interrupt Service Routine) attributes from XDM configuration containers, creates OsIsr model objects, and handles hardware-specific attributes for different processor types (TriCore, ARM, etc.).

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML fragment containing OsIsr containers is available |
| 3 | EBModel singleton is initialized |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| ISR Name | "Isr1" | Example ISR identifier |
| ISR Category | 2 | ISR category (1=ISR1, 2=ISR2, etc.) |
| ISR Priority | 10 | ISR priority value |
| Interrupt Vector | 0x42 | Hardware interrupt vector |
| Stack Size | 512 | Stack size in bytes |
| Processor Type | "Tricore" | Hardware-specific attributes |
| Hardware Attributes | TriCore/ARM-specific fields | Verify hardware-specific extraction |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse XML fragment with OsIsr container (TriCore) | OsIsr object created successfully |
| 2 | Verify ISR name extraction | getName() returns "Isr1" |
| 3 | Verify ISR category extraction | getCategory() returns 2 |
| 4 | Verify ISR priority extraction | getPriority() returns 10 |
| 5 | Verify interrupt vector extraction | getInterruptVector() returns 0x42 |
| 6 | Verify stack size extraction | getStackSize() returns 512 |
| 7 | Verify TriCore-specific attributes | Hardware attributes extracted correctly |
| 8 | Parse XML fragment with OsIsr container (ARM) | OsIsr object created successfully |
| 9 | Verify ARM-specific attributes | ARM-specific attributes extracted correctly |
| 10 | Verify parent-child relationship | ISR's parent is OS module |

## Expected Results

- All ISR attributes are extracted correctly
- Hardware-specific attributes are handled based on processor type
- ISR object is properly registered with parent module
- Both TriCore and ARM configurations are supported
- ISR category mapping is correct (1=ISR1, 2=ISR2, etc.)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | OsIsr objects remain in memory for verification |
| 2 | EBModel contains updated ISR collection |
| 3 | No orphaned ISR objects exist |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_OS_00003 | ISR Management - ISR attribute extraction and hardware-specific handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_os-module.md |
| Model Documentation | ../../src/eb_model/models/module.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |