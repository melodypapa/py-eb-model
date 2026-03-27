# Test Case: TC_INT_CROSS_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_INT_CROSS_00002 |
| Title | Cross-Module - CAN Stack End-to-End |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Integration |
| Priority | High |

## Purpose/Objective

Verify the complete CAN stack integration, ensuring that CanIf, CanNm, CanSm, and CanTp modules work together correctly, with proper PDU routing and state coordination.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | CAN stack XDM files are available |
| 3 | EBModel singleton is clean |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| CanIf XDM File | `data/test/CanIf.xdm` | CAN Interface configuration |
| CanNm XDM File | `data/test/CanNm.xdm` | CAN Network Management |
| CanSm XDM File | `data/test/CanSm.xdm` | CAN State Manager |
| CanTp XDM File | `data/test/CanTp.xdm` | CAN Transport Protocol |
| Rx/Tx PDUs | List of PDU configurations | Data flow across stack |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse CanIf XDM file | CanIf model populated with controllers and PDUs |
| 2 | Parse CanNm XDM file | CanNm model populated with channels |
| 3 | Parse CanSm XDM file | CanSm model populated with network configurations |
| 4 | Parse CanTp XDM file | CanTp model populated with channels |
| 5 | Verify controller references | CanNm references CanIf controllers |
| 6 | Verify PDU routing | PDUs flow through stack correctly |
| 7 | Verify state coordination | State machine coordination across modules |
| 8 | Generate combined CAN stack report | All modules in one workbook |
| 9 | Verify cross-module references | References visible in reports |
| 10 | Verify data consistency | No conflicting data across modules |

## Expected Results

- All CAN stack modules parse successfully
- Cross-module references are resolved correctly
- PDU routing is consistent across modules
- State coordination is maintained
- Combined reports include all stack data
- No conflicting data between modules

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Combined CAN stack output persists for review |
| 2 | EBModel contains all CAN stack data |
| 3 | No reference resolution errors |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_CANIF_00001-00016 | CanIf module requirements | Covered |
| SWR_CANNM_00001-00010 | CanNm module requirements | Covered |
| SWR_CANSM_00001-00008 | CanSm module requirements | Covered |
| SWR_CANTP_00001-00009 | CanTp module requirements | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_canif-module.md |
| Requirement Document | ../requirements/swr_cannm-module.md |
| Requirement Document | ../requirements/swr_cansm-module.md |
| Requirement Document | ../requirements/swr_cantp-module.md |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |