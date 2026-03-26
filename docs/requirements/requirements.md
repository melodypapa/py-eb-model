# py-eb-model Requirements Registry

## Document Information

| Field | Value |
|-------|-------|
| Document Title | py-eb-model Requirements Registry |
| Document ID | SWR_REGISTRY_00001 |
| Version | 1.0 |
| Date | 2026-03-26 |
| Project | py-eb-model |

## Purpose

This document serves as the central registry for all software requirements specifications (SWR) in the py-eb-model project. It provides traceability between requirement IDs and their corresponding documents.

## Requirement ID Format

**Format**: `SWR_<MODULE>_<NUMBER>`

- **SWR**: Software Requirement identifier
- **MODULE**: Module abbreviation (OS, RTE, NVM, etc.)
- **NUMBER**: 5-digit sequential number within module range

Examples:
- `SWR_OS_00001` - First OS module requirement
- `SWR_RTE_00001` - First RTE module requirement
- `SWR_CANIF_00001` - First CanIf module requirement

## Maturity Levels

| Level | Description |
|-------|-------------|
| **draft** | Newly created, under review, or not yet implemented |
| **accept** | Accepted, implemented, and validated |
| **invalid** | Deprecated, superseded, or no longer applicable |

## Requirements by Module

### Core Modules

| Module | ID Range | Document | Status |
|--------|----------|----------|--------|
| OS (Operating System) | SWR_OS_00001+ | [swr_os-module.md](swr_os-module.md) | accept |
| RTE (Runtime Environment) | SWR_RTE_00001+ | [swr_rte-module.md](swr_rte-module.md) | draft |
| NvM (Non-volatile Memory) | SWR_NVM_00001+ | [swr_nvm-module.md](swr_nvm-module.md) | draft |
| EcuC (ECU Configuration) | SWR_ECUC_00001+ | [swr_ecuc-module.md](swr_ecuc-module.md) | draft |
| BswM (Basic Software Mode) | SWR_BSWM_00001+ | [swr_bswm-module.md](swr_bswm-module.md) | draft |

### CAN Communication Stack

| Module | ID Range | Document | Status |
|--------|----------|----------|--------|
| CanIf (CAN Interface) | SWR_CANIF_00001+ | [swr_canif-module.md](swr_canif-module.md) | draft |
| CanNm (CAN Network Management) | SWR_CANNM_00001+ | [swr_cannm-module.md](swr_cannm-module.md) | draft |
| CanSm (CAN State Manager) | SWR_CANSM_00001+ | [swr_cansm-module.md](swr_cansm-module.md) | draft |
| CanTp (CAN Transport Protocol) | SWR_CANTP_00001+ | [swr_cantp-module.md](swr_cantp-module.md) | draft |

### LIN Communication Stack

| Module | ID Range | Document | Status |
|--------|----------|----------|--------|
| LinIf (LIN Interface) | SWR_LINIF_00001+ | [swr_linif-module.md](swr_linif-module.md) | draft |
| LinSm (LIN State Manager) | SWR_LINSM_00001+ | [swr_linsm-module.md](swr_linsm-module.md) | draft |
| LinTp (LIN Transport Protocol) | SWR_LINTP_00001+ | [swr_lintp-module.md](swr_lintp-module.md) | draft |

### System Modules

| Module | ID Range | Document | Status |
|--------|----------|----------|--------|
| Det (Development Error Tracer) | SWR_DET_00001+ | [swr_det-module.md](swr_det-module.md) | draft |
| EcuM (ECU State Manager) | SWR_ECUM_00001+ | [swr_ecum-module.md](swr_ecum-module.md) | draft |
| Tm (Timing) | SWR_TM_00001+ | [swr_tm-module.md](swr_tm-module.md) | draft |
| PbcfgM (Post-Build Configuration) | SWR_PBCFGM_00001+ | [swr_pbcfgm-module.md](swr_pbcfgm-module.md) | draft |

### Infrastructure Layers

| Layer | ID Range | Document | Status |
|-------|----------|----------|--------|
| Parser Layer | SWR_PARSER_00001+ | [swr_parser-layer.md](swr_parser-layer.md) | draft |
| Reporter Layer | SWR_REPORTER_00001+ | [swr_reporter-layer.md](swr_reporter-layer.md) | draft |
| CLI Layer | SWR_CLI_00001+ | [swr_cli-layer.md](swr_cli-layer.md) | draft |

## Related Documents

- [overview.md](overview.md) - System architecture overview
- [CLAUDE.md](../../CLAUDE.md) - Development guide for contributors

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-26 | Claude Code | Initial requirements registry |