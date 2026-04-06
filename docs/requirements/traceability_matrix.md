# Traceability Matrix for py-eb-model

## Document Information

| Field | Value |
|-------|-------|
| Document Title | Requirements-to-Code Traceability Matrix |
| Document ID | SWR_TRACEABILITY_00001 |
| Version | 1.0 |
| Date | 2026-04-05 |
| Project | py-eb-model |

## Purpose

This document provides bidirectional traceability between software requirements and their corresponding code implementations. It enables:

- **Requirements → Code**: Find what code implements each requirement
- **Code → Requirements**: Find what requirements each code unit satisfies
- **Change Impact**: Identify requirements affected by code changes
- **Audit Trail**: Verify implementation matches requirements

## Traceability Format

```
Requirement ID | Implementation Location | Files | Status | Last Validated
---------------|------------------------|-------|--------|---------------
```

- **Requirement ID**: SWR_ID for the requirement
- **Implementation Location**: `file_path.py:ClassName:line_number` format
- **Files**: Directory or file containing implementation
- **Status**: Implemented, Pending, Draft, Deprecated
- **Last Validated**: Date of last verification

---

## Parser Layer Requirements

### Core Parser Infrastructure

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_PARSER_00001 | `src/eb_model/parser/core/eb_parser.py:AbstractEbModelParser:17-46` | src/eb_model/parser/core/eb_parser.py | Implemented | 2026-04-07 |
| SWR_PARSER_00002 | `src/eb_model/parser/core/eb_parser.py:AbstractEbModelParser:read_namespaces:297-306` | src/eb_model/parser/core/eb_parser.py | Implemented | 2026-04-07 |
| SWR_PARSER_00003 | `src/eb_model/parser/core/eb_parser.py:AbstractEbModelParser:read_value:108-119` | src/eb_model/parser/core/eb_parser.py | Implemented | 2026-04-05 |
| SWR_PARSER_00004 | `src/eb_model/parser/core/eb_parser.py:AbstractEbModelParser:read_ref_raw_value:75-86` | src/eb_model/parser/core/eb_parser.py | Implemented | 2026-04-05 |
| SWR_PARSER_00005 | `src/eb_model/parser/core/eb_parser_factory.py:EbParserFactory:create` | src/eb_model/parser/core/eb_parser_factory.py | Implemented | 2026-04-05 |
| SWR_PARSER_00006 | `src/eb_model/parser/core/eb_parser.py:AbstractEbModelParser:find_ctr_tag:228-245` | src/eb_model/parser/core/eb_parser.py | Implemented | 2026-04-05 |

---

## OS Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_OS_00001 | `src/eb_model/parser/core/os_xdm_parser.py:OsXdmParser:parse:46-80` | src/eb_model/parser/core/os_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_OS_00002 | `src/eb_model/parser/core/os_xdm_parser.py:OsXdmParser:read_os_tasks:91-114` | src/eb_model/parser/core/os_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_OS_00002 | `src/eb_model/models/core/os_xdm.py:OsTask:793-939` | src/eb_model/models/core/os_xdm.py | Implemented | 2026-04-07 |
| SWR_OS_00003 | `src/eb_model/parser/core/os_xdm_parser.py:OsXdmParser:read_os_isrs:116-146` | src/eb_model/parser/core/os_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_OS_00003 | `src/eb_model/models/core/os_xdm.py:OsIsr:624-762` | src/eb_model/models/core/os_xdm.py | Implemented | 2026-04-07 |
| SWR_OS_00004 | `src/eb_model/parser/core/os_xdm_parser.py:OsXdmParser:read_os_alarms:173-189` | src/eb_model/parser/core/os_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_OS_00004 | `src/eb_model/models/core/os_xdm.py:OsAlarm:113-169` | src/eb_model/models/core/os_xdm.py | Implemented | 2026-04-07 |
| SWR_OS_00005 | `src/eb_model/parser/core/os_xdm_parser.py:OsXdmParser:read_os_schedule_tables:226-242` | src/eb_model/parser/core/os_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_OS_00005 | `src/eb_model/models/core/os_xdm.py:OsScheduleTable:1071-1149` | src/eb_model/models/core/os_xdm.py | Implemented | 2026-04-07 |
| SWR_OS_00006 | `src/eb_model/parser/core/os_xdm_parser.py:OsXdmParser:read_os_counters:244-263` | src/eb_model/parser/core/os_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_OS_00006 | `src/eb_model/models/core/os_xdm.py:OsCounter:442-574` | src/eb_model/models/core/os_xdm.py | Implemented | 2026-04-07 |
| SWR_OS_00007 | `src/eb_model/parser/core/os_xdm_parser.py:OsXdmParser:read_os_applications:265-300` | src/eb_model/parser/core/os_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_OS_00007 | `src/eb_model/models/core/os_xdm.py:OsApplication:237-399` | src/eb_model/models/core/os_xdm.py | Implemented | 2026-04-07 |
| SWR_OS_00008 | `src/eb_model/parser/core/os_xdm_parser.py:OsXdmParser:read_os_resources:302-316` | src/eb_model/parser/core/os_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_OS_00008 | `src/eb_model/models/core/os_xdm.py:OsResource:576-607` | src/eb_model/models/core/os_xdm.py | Implemented | 2026-04-07 |
| SWR_OS_00009 | `src/eb_model/parser/core/os_xdm_parser.py:OsXdmParser:read_os_microkernel:345-355` | src/eb_model/parser/core/os_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_OS_00009 | `src/eb_model/models/core/os_xdm.py:OsMicrokernel:1300-1349` | src/eb_model/models/core/os_xdm.py | Implemented | 2026-04-07 |
| SWR_OS_00010 | `src/eb_model/reporter/excel_reporter/core/os_xdm.py:OsXdmXlsWriter:write:218-230` | src/eb_model/reporter/excel_reporter/core/os_xdm.py | Implemented | 2026-04-05 |
| SWR_OS_00011 | `src/eb_model/cli/os_xdm_2_xls_cli.py:main` | src/eb_model/cli/os_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## RTE Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_RTE_00001 | `src/eb_model/parser/core/rte_xdm_parser.py:RteXdmParser:parse:43-81` | src/eb_model/parser/core/rte_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_RTE_00002 | `src/eb_model/reporter/excel_reporter/core/rte_xdm.py:RteXdmXlsWriter:write:43-48` | src/eb_model/reporter/excel_reporter/core/rte_xdm.py | Implemented | 2026-04-05 |
| SWR_RTE_00003 | `src/eb_model/reporter/excel_reporter/core/rte_xdm.py:RteRunnableEntityXlsWriter:write:96-100` | src/eb_model/reporter/excel_reporter/core/rte_xdm.py | Implemented | 2026-04-05 |
| SWR_RTE_00004 | `src/eb_model/cli/rte_xdm_2_xls_cli.py:main` | src/eb_model/cli/rte_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## NvM Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_NVM_00001 | `src/eb_model/parser/mem_stack/nvm_xdm_parser.py:NvMXdmParser:parse:37-197` | src/eb_model/parser/mem_stack/nvm_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_NVM_00002 | `src/eb_model/parser/mem_stack/nvm_xdm_parser.py:NvMXdmParser:read_nvm_common:66-90` | src/eb_model/parser/mem_stack/nvm_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_NVM_00003 | `src/eb_model/parser/mem_stack/nvm_xdm_parser.py:NvMXdmParser:read_nvm_block_descriptors:217-295` | src/eb_model/parser/mem_stack/nvm_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_NVM_00004 | `src/eb_model/reporter/excel_reporter/mem_stack/nvm_xdm.py:NvMXdmXlsWriter:write:123-130` | src/eb_model/reporter/excel_reporter/mem_stack/nvm_xdm.py | Implemented | 2026-04-05 |
| SWR_NVM_00005 | `src/eb_model/cli/nvm_xdm_2_xls_cli.py:main` | src/eb_model/cli/nvm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## EcuC Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_ECUC_00001 | `src/eb_model/parser/core/ecuc_xdm_parser.py:EcucXdmParser:parse:154-184` | src/eb_model/parser/core/ecuc_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_ECUC_00002 | `src/eb_model/parser/core/ecuc_xdm_parser.py:EcucXdmParser:read_ecuc_partition_collection:186-192` | src/eb_model/parser/core/ecuc_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_ECUC_00003 | `src/eb_model/reporter/excel_reporter/core/ecuc_xdm.py:EcucXdmXlsWriter:write:45-50` | src/eb_model/reporter/excel_reporter/core/ecuc_xdm.py | Implemented | 2026-04-07 |
| SWR_ECUC_00004 | `src/eb_model/cli/ecuc_xdm_2_xls_cli.py:main` | src/eb_model/cli/ecuc_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## BswM Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_BSWM_00001 | `src/eb_model/parser/core/bswm_xdm_parser.py:BswMXdmParser:parse:30-48` | src/eb_model/parser/core/bswm_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_BSWM_00002 | `src/eb_model/parser/core/bswm_xdm_parser.py:BswMXdmParser:read_bswm_general:50-56` | src/eb_model/parser/core/bswm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_BSWM_00003 | `src/eb_model/parser/core/bswm_xdm_parser.py:BswMXdmParser:read_bswm_mode_conditions:68-73` | src/eb_model/parser/core/bswm_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_BSWM_00004 | `src/eb_model/reporter/excel_reporter/core/bswm_xdm.py:BswMXdmXlsWriter:write:59-64` | src/eb_model/reporter/excel_reporter/core/bswm_xdm.py | Implemented | 2026-04-07 |
| SWR_BSWM_00005 | `src/eb_model/cli/bswm_xdm_2_xls_cli.py:main` | src/eb_model/cli/bswm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## Det Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_DET_00001 | `src/eb_model/parser/core/det_xdm_parser.py:DetXdmParser:parse:31-57` | src/eb_model/parser/core/det_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_DET_00002 | `src/eb_model/parser/core/det_xdm_parser.py:DetXdmParser:read_det_error_hook:72-78` | src/eb_model/parser/core/det_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_DET_00003 | `src/eb_model/reporter/excel_reporter/core/det_xdm.py:DetXdmXlsWriter:write:56-61` | src/eb_model/reporter/excel_reporter/core/det_xdm.py | Implemented | 2026-04-07 |
| SWR_DET_00004 | `src/eb_model/cli/det_xdm_2_xls_cli.py:main` | src/eb_model/cli/det_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## EcuM Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_ECUM_00001 | `src/eb_model/parser/core/ecum_xdm_parser.py:EcuMXdmParser:parse:40-89` | src/eb_model/parser/core/ecum_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_ECUM_00002 | `src/eb_model/parser/core/ecum_xdm_parser.py:EcuMXdmParser:read_ecum_startup:403-412` | src/eb_model/parser/core/ecum_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_ECUM_00003 | `src/eb_model/parser/core/ecum_xdm_parser.py:EcuMXdmParser:read_ecum_shutdown:414-423` | src/eb_model/parser/core/ecum_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_ECUM_00004 | `src/eb_model/reporter/excel_reporter/core/ecum_xdm.py:EcumXdmXlsWriter:write:76-83` | src/eb_model/reporter/excel_reporter/core/ecum_xdm.py | Implemented | 2026-04-07 |
| SWR_ECUM_00005 | `src/eb_model/cli/ecum_xdm_2_xls_cli.py:main` | src/eb_model/cli/ecum_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## Tm Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_TM_00001 | `src/eb_model/parser/core/tm_xdm_parser.py:TmXdmParser:parse:33-55` | src/eb_model/parser/core/tm_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_TM_00002 | `src/eb_model/parser/core/tm_xdm_parser.py:TmXdmParser:read_tm_tick_time:112-119` | src/eb_model/parser/core/tm_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_TM_00003 | `src/eb_model/parser/core/tm_xdm_parser.py:TmXdmParser:read_tm_triggers:121-126` | src/eb_model/parser/core/tm_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_TM_00004 | `src/eb_model/reporter/excel_reporter/core/tm_xdm.py:TmXdmXlsWriter:write:71-78` | src/eb_model/reporter/excel_reporter/core/tm_xdm.py | Implemented | 2026-04-07 |
| SWR_TM_00005 | `src/eb_model/cli/tm_xdm_2_xls_cli.py:main` | src/eb_model/cli/tm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## PbcfgM Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_PBCFGM_00001 | `src/eb_model/parser/core/pbcfgm_xdm_parser.py:PbcfgMXdmParser:parse:29-48` | src/eb_model/parser/core/pbcfgm_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_PBCFGM_00002 | `src/eb_model/parser/core/pbcfgm_xdm_parser.py:PbcfgMXdmParser:read_pbcfgm_protection_sets:59-64` | src/eb_model/parser/core/pbcfgm_xdm_parser.py | Implemented | 2026-04-07 |
| SWR_PBCFGM_00003 | `src/eb_model/reporter/excel_reporter/core/pbcfgm_xdm.py:PbcfgMXdmXlsWriter:write:54-59` | src/eb_model/reporter/excel_reporter/core/pbcfgm_xdm.py | Implemented | 2026-04-07 |
| SWR_PBCFGM_00004 | `src/eb_model/cli/pbcfgm_xdm_2_xls_cli.py:main` | src/eb_model/cli/pbcfgm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## CanIf Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_CANIF_00001 | `src/eb_model/parser/can_stack/canif_xdm_parser.py:CanIfXdmParser:parse:34-145` | src/eb_model/parser/can_stack/canif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CANIF_00002 | `src/eb_model/parser/can_stack/canif_xdm_parser.py:CanIfXdmParser:read_canif_ctrl_cfgs:78-86` | src/eb_model/parser/can_stack/canif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CANIF_00003 | `src/eb_model/parser/can_stack/canif_xdm_parser.py:CanIfXdmParser:read_canif_rx_pdu_cfgs:128-139` | src/eb_model/parser/can_stack/canif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CANIF_00004 | `src/eb_model/reporter/excel_reporter/can_stack/canif_xdm.py:CanIfXdmXlsWriter:write:171-184` | src/eb_model/reporter/excel_reporter/can_stack/canif_xdm.py | Implemented | 2026-04-05 |
| SWR_CANIF_00005 | `src/eb_model/cli/canif_xdm_2_xls_cli.py:main` | src/eb_model/cli/canif_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## CanNm Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_CANNM_00001 | `src/eb_model/parser/can_stack/cannm_xdm_parser.py:CanNmXdmParser:parse:32-117` | src/eb_model/parser/can_stack/cannm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CANNM_00002 | `src/eb_model/parser/can_stack/cannm_xdm_parser.py:CanNmXdmParser:read_cannm_channels:89-101` | src/eb_model/parser/can_stack/cannm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CANNM_00003 | `src/eb_model/parser/can_stack/cannm_xdm_parser.py:CanNmXdmParser:read_cannm_rx_pdus:102-109` | src/eb_model/parser/can_stack/cannm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CANNM_00004 | `src/eb_model/reporter/excel_reporter/can_stack/cannm_xdm.py:CanNmXdmXlsWriter:write:138-149` | src/eb_model/reporter/excel_reporter/can_stack/cannm_xdm.py | Implemented | 2026-04-05 |
| SWR_CANNM_00005 | `src/eb_model/cli/cannm_xdm_2_xls_cli.py:main` | src/eb_model/cli/cannm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## CanSM Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_CANSM_00001 | `src/eb_model/parser/can_stack/cansm_xdm_parser.py:CanSMXdmParser:parse:32-86` | src/eb_model/parser/can_stack/cansm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CANSM_00002 | `src/eb_model/parser/can_stack/cansm_xdm_parser.py:CanSMXdmParser:read_cansm_manager_networks:64-80` | src/eb_model/parser/can_stack/cansm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CANSM_00003 | `src/eb_model/reporter/excel_reporter/can_stack/cansm_xdm.py:CanSMXdmXlsWriter:write:67-74` | src/eb_model/reporter/excel_reporter/can_stack/cansm_xdm.py | Implemented | 2026-04-05 |
| SWR_CANSM_00004 | `src/eb_model/cli/cansm_xdm_2_xls_cli.py:main` | src/eb_model/cli/cansm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## CanTp Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_CANTP_00001 | `src/eb_model/parser/can_stack/cantp_xdm_parser.py:CanTpXdmParser:parse:31-95` | src/eb_model/parser/can_stack/cantp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CANTP_00002 | `src/eb_model/parser/can_stack/cantp_xdm_parser.py:CanTpXdmParser:read_cantp_channels:69-76` | src/eb_model/parser/can_stack/cantp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CANTP_00003 | `src/eb_model/parser/can_stack/cantp_xdm_parser.py:CanTpXdmParser:read_cantp_rx_nsdus:77-86` | src/eb_model/parser/can_stack/cantp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CANTP_00004 | `src/eb_model/reporter/excel_reporter/can_stack/cantp_xdm.py:CanTpXdmXlsWriter:write:74-82` | src/eb_model/reporter/excel_reporter/can_stack/cantp_xdm.py | Implemented | 2026-04-05 |
| SWR_CANTP_00005 | `src/eb_model/cli/cantp_xdm_2_xls_cli.py:main` | src/eb_model/cli/cantp_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## LinIf Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_LINIF_00001 | `src/eb_model/parser/lin_stack/linif_xdm_parser.py:LinIfXdmParser:parse:29-82` | src/eb_model/parser/lin_stack/linif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_LINIF_00002 | `src/eb_model/parser/lin_stack/linif_xdm_parser.py:LinIfXdmParser:read_linif_channels:65-73` | src/eb_model/parser/lin_stack/linif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_LINIF_00003 | `src/eb_model/parser/lin_stack/linif_xdm_parser.py:LinIfXdmParser:read_linif_frames:74-82` | src/eb_model/parser/lin_stack/linif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_LINIF_00004 | `src/eb_model/reporter/excel_reporter/lin_stack/linif_xdm.py:LinIfXdmXlsWriter:write:58-65` | src/eb_model/reporter/excel_reporter/lin_stack/linif_xdm.py | Implemented | 2026-04-05 |
| SWR_LINIF_00005 | `src/eb_model/cli/linif_xdm_2_xls_cli.py:main` | src/eb_model/cli/linif_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## LinSM Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_LINSM_00001 | `src/eb_model/parser/lin_stack/linsm_xdm_parser.py:LinSMXdmParser:parse:28-65` | src/eb_model/parser/lin_stack/linsm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_LINSM_00002 | `src/eb_model/parser/lin_stack/linsm_xdm_parser.py:LinSMXdmParser:read_linsm_channels:62-71` | src/eb_model/parser/lin_stack/linsm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_LINSM_00003 | `src/eb_model/reporter/excel_reporter/lin_stack/linsm_xdm.py:LinSMXdmXlsWriter:write:41-47` | src/eb_model/reporter/excel_reporter/lin_stack/linsm_xdm.py | Implemented | 2026-04-05 |
| SWR_LINSM_00004 | `src/eb_model/cli/linsm_xdm_2_xls_cli.py:main` | src/eb_model/cli/linsm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## LinTp Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_LINTP_00001 | `src/eb_model/parser/lin_stack/lintp_xdm_parser.py:LinTpXdmParser:parse:28-85` | src/eb_model/parser/lin_stack/lintp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_LINTP_00002 | `src/eb_model/parser/lin_stack/lintp_xdm_parser.py:LinTpXdmParser:read_lintp_rx_nsdus:68-75` | src/eb_model/parser/lin_stack/lintp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_LINTP_00003 | `src/eb_model/reporter/excel_reporter/lin_stack/lintp_xdm.py:LinTpXdmXlsWriter:write:55-62` | src/eb_model/reporter/excel_reporter/lin_stack/lintp_xdm.py | Implemented | 2026-04-05 |
| SWR_LINTP_00004 | `src/eb_model/cli/lintp_xdm_2_xls_cli.py:main` | src/eb_model/cli/lintp_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## EthIf Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_ETHIF_00001 | `src/eb_model/parser/eth_stack/ethif_xdm_parser.py:EthIfXdmParser:parse:39-222` | src/eb_model/parser/eth_stack/ethif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_ETHIF_00002 | `src/eb_model/parser/eth_stack/ethif_xdm_parser.py:EthIfXdmParser:read_ethif_general:70-93` | src/eb_model/parser/eth_stack/ethif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_ETHIF_00003 | `src/eb_model/parser/eth_stack/ethif_xdm_parser.py:EthIfXdmParser:read_ethif_controllers:108-125` | src/eb_model/parser/eth_stack/ethif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_ETHIF_00004 | `src/eb_model/parser/eth_stack/ethif_xdm_parser.py:EthIfXdmParser:read_ethif_phys_controllers:135-148` | src/eb_model/parser/eth_stack/ethif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_ETHIF_00005 | `src/eb_model/parser/eth_stack/ethif_xdm_parser.py:EthIfXdmParser:read_ethif_switches:149-161` | src/eb_model/parser/eth_stack/ethif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_ETHIF_00006 | `src/eb_model/parser/eth_stack/ethif_xdm_parser.py:EthIfXdmParser:read_ethif_transceivers:171-184` | src/eb_model/parser/eth_stack/ethif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_ETHIF_00007 | `src/eb_model/parser/eth_stack/ethif_xdm_parser.py:EthIfXdmParser:read_ethif_rx_indication_configs:185-195` | src/eb_model/parser/eth_stack/ethif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_ETHIF_00008 | `src/eb_model/reporter/excel_reporter/eth_stack/ethif_xdm.py:EthIfXdmXlsWriter:write:157-169` | src/eb_model/reporter/excel_reporter/eth_stack/ethif_xdm.py | Implemented | 2026-04-05 |
| SWR_ETHIF_00009 | `src/eb_model/cli/ethif_xdm_2_xls_cli.py:main` | src/eb_model/cli/ethif_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## EthSM Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_ETHSM_00001 | `src/eb_model/parser/eth_stack/ethsm_xdm_parser.py:EthSMXdmParser:parse:31-92` | src/eb_model/parser/eth_stack/ethsm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_ETHSM_00002 | `src/eb_model/parser/eth_stack/ethsm_xdm_parser.py:EthSMXdmParser:read_ethsm_general:52-72` | src/eb_model/parser/eth_stack/ethsm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_ETHSM_00003 | `src/eb_model/parser/eth_stack/ethsm_xdm_parser.py:EthSMXdmParser:read_ethsm_networks:87-105` | src/eb_model/parser/eth_stack/ethsm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_ETHSM_00004 | `src/eb_model/reporter/excel_reporter/eth_stack/ethsm_xdm.py:EthSMXdmXlsWriter:write:64-71` | src/eb_model/reporter/excel_reporter/eth_stack/ethsm_xdm.py | Implemented | 2026-04-05 |
| SWR_ETHSM_00005 | `src/eb_model/cli/ethsm_xdm_2_xls_cli.py:main` | src/eb_model/cli/ethsm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## SoAd Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_SOAD_00001 | `src/eb_model/parser/eth_stack/soad_xdm_parser.py:SoAdXdmParser:parse:36-194` | src/eb_model/parser/eth_stack/soad_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_SOAD_00002 | `src/eb_model/parser/eth_stack/soad_xdm_parser.py:SoAdXdmParser:read_soad_general:59-79` | src/eb_model/parser/eth_stack/soad_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_SOAD_00003 | `src/eb_model/parser/eth_stack/soad_xdm_parser.py:SoAdXdmParser:read_soad_socket_connection_groups:80-130` | src/eb_model/parser/eth_stack/soad_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_SOAD_00004 | `src/eb_model/parser/eth_stack/soad_xdm_parser.py:SoAdXdmParser:read_soad_pdu_routes:131-157` | src/eb_model/parser/eth_stack/soad_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_SOAD_00005 | `src/eb_model/reporter/excel_reporter/eth_stack/soad_xdm.py:SoAdXdmXlsWriter:write:85-93` | src/eb_model/reporter/excel_reporter/eth_stack/soad_xdm.py | Implemented | 2026-04-05 |
| SWR_SOAD_00006 | `src/eb_model/cli/soad_xdm_2_xls_cli.py:main` | src/eb_model/cli/soad_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## TcpIp Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_TCPIP_00001 | `src/eb_model/parser/eth_stack/tcpip_xdm_parser.py:TcpIpXdmParser:parse:35-132` | src/eb_model/parser/eth_stack/tcpip_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_TCPIP_00002 | `src/eb_model/parser/eth_stack/tcpip_xdm_parser.py:TcpIpXdmParser:read_tcpip_general:56-71` | src/eb_model/parser/eth_stack/tcpip_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_TCPIP_00003 | `src/eb_model/parser/eth_stack/tcpip_xdm_parser.py:TcpIpXdmParser:read_tcpip_ctrls:72-109` | src/eb_model/parser/eth_stack/tcpip_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_TCPIP_00004 | `src/eb_model/parser/eth_stack/tcpip_xdm_parser.py:TcpIpXdmParser:read_tcpip_local_addrs:110-132` | src/eb_model/parser/eth_stack/tcpip_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_TCPIP_00005 | `src/eb_model/reporter/excel_reporter/eth_stack/tcpip_xdm.py:TcpIpXdmXlsWriter:write:77-85` | src/eb_model/reporter/excel_reporter/eth_stack/tcpip_xdm.py | Implemented | 2026-04-05 |
| SWR_TCPIP_00006 | `src/eb_model/cli/tcpip_xdm_2_xls_cli.py:main` | src/eb_model/cli/tcpip_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## UdpNm Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_UDPNM_00001 | `src/eb_model/parser/eth_stack/udpnm_xdm_parser.py:UdpNmXdmParser:parse:32-75` | src/eb_model/parser/eth_stack/udpnm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_UDPNM_00002 | `src/eb_model/parser/eth_stack/udpnm_xdm_parser.py:UdpNmXdmParser:read_udpnm_general:52-66` | src/eb_model/parser/eth_stack/udpnm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_UDPNM_00003 | `src/eb_model/parser/eth_stack/udpnm_xdm_parser.py:UdpNmXdmParser:read_udpnm_channels:67-75` | src/eb_model/parser/eth_stack/udpnm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_UDPNM_00004 | `src/eb_model/reporter/excel_reporter/eth_stack/udpnm_xdm.py:UdpNmXdmXlsWriter:write:56-63` | src/eb_model/reporter/excel_reporter/eth_stack/udpnm_xdm.py | Implemented | 2026-04-05 |
| SWR_UDPNM_00005 | `src/eb_model/cli/udpnm_xdm_2_xls_cli.py:main` | src/eb_model/cli/udpnm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## DoIP Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_DOIP_00001 | `src/eb_model/parser/eth_stack/doip_xdm_parser.py:DoIPXdmParser:parse:35-149` | src/eb_model/parser/eth_stack/doip_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_DOIP_00002 | `src/eb_model/parser/eth_stack/doip_xdm_parser.py:DoIPXdmParser:read_doip_general:57-71` | src/eb_model/parser/eth_stack/doip_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_DOIP_00003 | `src/eb_model/parser/eth_stack/doip_xdm_parser.py:DoIPXdmParser:read_doip_channels:72-98` | src/eb_model/parser/eth_stack/doip_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_DOIP_00004 | `src/eb_model/parser/eth_stack/doip_xdm_parser.py:DoIPXdmParser:read_doip_connections:122-149` | src/eb_model/parser/eth_stack/doip_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_DOIP_00005 | `src/eb_model/reporter/excel_reporter/eth_stack/doip_xdm.py:DoIPXdmXlsWriter:write:44-51` | src/eb_model/reporter/excel_reporter/eth_stack/doip_xdm.py | Implemented | 2026-04-05 |
| SWR_DOIP_00006 | `src/eb_model/cli/doip_xdm_2_xls_cli.py:main` | src/eb_model/cli/doip_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## SomeIpTp Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_SOMEIPTP_00001 | `src/eb_model/parser/eth_stack/someiptp_xdm_parser.py:SomeIpTpXdmParser:parse:34-148` | src/eb_model/parser/eth_stack/someiptp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_SOMEIPTP_00002 | `src/eb_model/parser/eth_stack/someiptp_xdm_parser.py:SomeIpTpXdmParser:read_someiptp_general:55-70` | src/eb_model/parser/eth_stack/someiptp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_SOMEIPTP_00003 | `src/eb_model/parser/eth_stack/someiptp_xdm_parser.py:SomeIpTpXdmParser:read_someiptp_channels:71-93` | src/eb_model/parser/eth_stack/someiptp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_SOMEIPTP_00004 | `src/eb_model/parser/eth_stack/someiptp_xdm_parser.py:SomeIpTpXdmParser:read_someiptp_rx_nsdus:94-116` | src/eb_model/parser/eth_stack/someiptp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_SOMEIPTP_00005 | `src/eb_model/reporter/excel_reporter/eth_stack/someiptp_xdm.py:SomeIpTpXdmXlsWriter:write:74-81` | src/eb_model/reporter/excel_reporter/eth_stack/someiptp_xdm.py | Implemented | 2026-04-05 |
| SWR_SOMEIPTP_00006 | `src/eb_model/cli/someiptp_xdm_2_xls_cli.py:main` | src/eb_model/cli/someiptp_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## FrIf Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_FRIF_00001 | `src/eb_model/parser/fr_stack/frif_xdm_parser.py:FrIfXdmParser:parse:31-89` | src/eb_model/parser/fr_stack/frif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRIF_00002 | `src/eb_model/parser/fr_stack/frif_xdm_parser.py:FrIfXdmParser:read_frif_general:52-73` | src/eb_model/parser/fr_stack/frif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRIF_00003 | `src/eb_model/parser/fr_stack/frif_xdm_parser.py:FrIfXdmParser:read_frif_controllers:85-94` | src/eb_model/parser/fr_stack/frif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRIF_00004 | `src/eb_model/reporter/excel_reporter/fr_stack/frif_xdm.py:FrIfXdmXlsWriter:write:70-78` | src/eb_model/reporter/excel_reporter/fr_stack/frif_xdm.py | Implemented | 2026-04-05 |
| SWR_FRIF_00005 | `src/eb_model/cli/frif_xdm_2_xls_cli.py:main` | src/eb_model/cli/frif_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## FrNm Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_FRNM_00001 | `src/eb_model/parser/fr_stack/frnm_xdm_parser.py:FrNmXdmParser:parse:32-74` | src/eb_model/parser/fr_stack/frnm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRNM_00002 | `src/eb_model/parser/fr_stack/frnm_xdm_parser.py:FrNmXdmParser:read_frnm_general:52-66` | src/eb_model/parser/fr_stack/frnm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRNM_00003 | `src/eb_model/parser/fr_stack/frnm_xdm_parser.py:FrNmXdmParser:read_frnm_channels:67-74` | src/eb_model/parser/fr_stack/frnm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRNM_00004 | `src/eb_model/reporter/excel_reporter/fr_stack/frnm_xdm.py:FrNmXdmXlsWriter:write:56-63` | src/eb_model/reporter/excel_reporter/fr_stack/frnm_xdm.py | Implemented | 2026-04-05 |
| SWR_FRNM_00005 | `src/eb_model/cli/frnm_xdm_2_xls_cli.py:main` | src/eb_model/cli/frnm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## FrSM Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_FRSM_00001 | `src/eb_model/parser/fr_stack/frsm_xdm_parser.py:FrSMXdmParser:parse:31-89` | src/eb_model/parser/fr_stack/frsm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRSM_00002 | `src/eb_model/parser/fr_stack/frsm_xdm_parser.py:FrSMXdmParser:read_frsm_general:52-75` | src/eb_model/parser/fr_stack/frsm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRSM_00003 | `src/eb_model/parser/fr_stack/frsm_xdm_parser.py:FrSMXdmParser:read_frsm_clusters:90-108` | src/eb_model/parser/fr_stack/frsm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRSM_00004 | `src/eb_model/reporter/excel_reporter/fr_stack/frsm_xdm.py:FrSMXdmXlsWriter:write:85-92` | src/eb_model/reporter/excel_reporter/fr_stack/frsm_xdm.py | Implemented | 2026-04-05 |
| SWR_FRSM_00005 | `src/eb_model/cli/frsm_xdm_2_xls_cli.py:main` | src/eb_model/cli/frsm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## FrTp Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_FRTP_00001 | `src/eb_model/parser/fr_stack/frtp_xdm_parser.py:FrTpXdmParser:parse:33-143` | src/eb_model/parser/fr_stack/frtp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRTP_00002 | `src/eb_model/parser/fr_stack/frtp_xdm_parser.py:FrTpXdmParser:read_frtp_general:54-71` | src/eb_model/parser/fr_stack/frtp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRTP_00003 | `src/eb_model/parser/fr_stack/frtp_xdm_parser.py:FrTpXdmParser:read_frtp_connections:83-117` | src/eb_model/parser/fr_stack/frtp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRTP_00004 | `src/eb_model/parser/fr_stack/frtp_xdm_parser.py:FrTpXdmParser:read_frtp_rx_sdu:118-130` | src/eb_model/parser/fr_stack/frtp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRTP_00005 | `src/eb_model/reporter/excel_reporter/fr_stack/frtp_xdm.py:FrTpXdmXlsWriter:write:88-96` | src/eb_model/reporter/excel_reporter/fr_stack/frtp_xdm.py | Implemented | 2026-04-05 |
| SWR_FRTP_00006 | `src/eb_model/cli/frtp_xdm_2_xls_cli.py:main` | src/eb_model/cli/frtp_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## FrArTp Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_FRARTP_00001 | `src/eb_model/parser/fr_stack/frartp_xdm_parser.py:FrArTpXdmParser:parse:33-183` | src/eb_model/parser/fr_stack/frartp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRARTP_00002 | `src/eb_model/parser/fr_stack/frartp_xdm_parser.py:FrArTpXdmParser:read_frartp_general:54-78` | src/eb_model/parser/fr_stack/frartp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRARTP_00003 | `src/eb_model/parser/fr_stack/frartp_xdm_parser.py:FrArTpXdmParser:read_frartp_channels:93-131` | src/eb_model/parser/fr_stack/frartp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRARTP_00004 | `src/eb_model/parser/fr_stack/frartp_xdm_parser.py:FrArTpXdmParser:read_frartp_connections:132-164` | src/eb_model/parser/fr_stack/frartp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FRARTP_00005 | `src/eb_model/reporter/excel_reporter/fr_stack/frartp_xdm.py:FrArTpXdmXlsWriter:write:100-108` | src/eb_model/reporter/excel_reporter/fr_stack/frartp_xdm.py | Implemented | 2026-04-05 |
| SWR_FRARTP_00006 | `src/eb_model/cli/frartp_xdm_2_xls_cli.py:main` | src/eb_model/cli/frartp_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## Com Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_COM_00001 | `src/eb_model/parser/com_stack/com_xdm_parser.py:ComXdmParser:parse:30-51` | src/eb_model/parser/com_stack/com_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_COM_00002 | `src/eb_model/parser/com_stack/com_xdm_parser.py:ComXdmParser:read_com_general:49-64` | src/eb_model/parser/com_stack/com_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_COM_00003 | `src/eb_model/reporter/excel_reporter/com_stack/com_xdm.py:ComXdmXlsWriter:write:25-30` | src/eb_model/reporter/excel_reporter/com_stack/com_xdm.py | Implemented | 2026-04-05 |
| SWR_COM_00004 | `src/eb_model/cli/com_xdm_2_xls_cli.py:main` | src/eb_model/cli/com_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## ComM Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_COMM_00001 | `src/eb_model/parser/com_stack/comm_xdm_parser.py:ComMXdmParser:parse:28-49` | src/eb_model/parser/com_stack/comm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_COMM_00002 | `src/eb_model/parser/com_stack/comm_xdm_parser.py:ComMXdmParser:read_comm_channels:47-63` | src/eb_model/parser/com_stack/comm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_COMM_00003 | `src/eb_model/reporter/excel_reporter/com_stack/comm_xdm.py:ComMXdmXlsWriter:write:25-30` | src/eb_model/reporter/excel_reporter/com_stack/comm_xdm.py | Implemented | 2026-04-05 |
| SWR_COMM_00004 | `src/eb_model/cli/comm_xdm_2_xls_cli.py:main` | src/eb_model/cli/comm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## PduR Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_PDUR_00001 | `src/eb_model/parser/com_stack/pdur_xdm_parser.py:PduRXdmParser:parse:28-49` | src/eb_model/parser/com_stack/pdur_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_PDUR_00002 | `src/eb_model/parser/com_stack/pdur_xdm_parser.py:PduRXdmParser:read_pdur_routing_cfgs:47-63` | src/eb_model/parser/com_stack/pdur_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_PDUR_00003 | `src/eb_model/reporter/excel_reporter/com_stack/pdur_xdm.py:PduRXdmXlsWriter:write:25-30` | src/eb_model/reporter/excel_reporter/com_stack/pdur_xdm.py | Implemented | 2026-04-05 |
| SWR_PDUR_00004 | `src/eb_model/cli/pdur_xdm_2_xls_cli.py:main` | src/eb_model/cli/pdur_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## IpduM Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_IPDUM_00001 | `src/eb_model/parser/com_stack/ipdum_xdm_parser.py:IpduMXdmParser:parse:28-49` | src/eb_model/parser/com_stack/ipdum_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_IPDUM_00002 | `src/eb_model/parser/com_stack/ipdum_xdm_parser.py:IpduMXdmParser:read_ipdum_dynamic_pdus:47-63` | src/eb_model/parser/com_stack/ipdum_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_IPDUM_00003 | `src/eb_model/reporter/excel_reporter/com_stack/ipdum_xdm.py:IpduMXdmXlsWriter:write:25-30` | src/eb_model/reporter/excel_reporter/com_stack/ipdum_xdm.py | Implemented | 2026-04-05 |
| SWR_IPDUM_00004 | `src/eb_model/cli/ipdum_xdm_2_xls_cli.py:main` | src/eb_model/cli/ipdum_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## Nm Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_NM_00001 | `src/eb_model/parser/com_stack/nm_xdm_parser.py:NmXdmParser:parse:28-49` | src/eb_model/parser/com_stack/nm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_NM_00002 | `src/eb_model/parser/com_stack/nm_xdm_parser.py:NmXdmParser:read_nm_channels:47-63` | src/eb_model/parser/com_stack/nm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_NM_00003 | `src/eb_model/reporter/excel_reporter/com_stack/nm_xdm.py:NmXdmXlsWriter:write:25-30` | src/eb_model/reporter/excel_reporter/com_stack/nm_xdm.py | Implemented | 2026-04-05 |
| SWR_NM_00004 | `src/eb_model/cli/nm_xdm_2_xls_cli.py:main` | src/eb_model/cli/nm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## LdCom Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_LDCOM_00001 | `src/eb_model/parser/com_stack/ldcom_xdm_parser.py:LdComXdmParser:parse:28-38` | src/eb_model/parser/com_stack/ldcom_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_LDCOM_00002 | `src/eb_model/reporter/excel_reporter/com_stack/ldcom_xdm.py:LdComXdmXlsWriter:write:25-30` | src/eb_model/reporter/excel_reporter/com_stack/ldcom_xdm.py | Implemented | 2026-04-05 |
| SWR_LDCOM_00003 | `src/eb_model/cli/ldcom_xdm_2_xls_cli.py:main` | src/eb_model/cli/ldcom_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## Crc Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_CRC_00001 | `src/eb_model/parser/mem_stack/crc_xdm_parser.py:CrcXdmParser:parse:28-49` | src/eb_model/parser/mem_stack/crc_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CRC_00002 | `src/eb_model/parser/mem_stack/crc_xdm_parser.py:CrcXdmParser:read_crc_configs:47-63` | src/eb_model/parser/mem_stack/crc_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CRC_00003 | `src/eb_model/reporter/excel_reporter/mem_stack/crc_xdm.py:CrcXdmXlsWriter:write:25-30` | src/eb_model/reporter/excel_reporter/mem_stack/crc_xdm.py | Implemented | 2026-04-05 |
| SWR_CRC_00004 | `src/eb_model/cli/crc_xdm_2_xls_cli.py:main` | src/eb_model/cli/crc_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## Ea Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_EA_00001 | `src/eb_model/parser/mem_stack/ea_xdm_parser.py:EaXdmParser:parse:30-49` | src/eb_model/parser/mem_stack/ea_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_EA_00002 | `src/eb_model/parser/mem_stack/ea_xdm_parser.py:EaXdmParser:read_ea_general:48-63` | src/eb_model/parser/mem_stack/ea_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_EA_00003 | `src/eb_model/reporter/excel_reporter/mem_stack/ea_xdm.py:EaXdmXlsWriter:write:45-51` | src/eb_model/reporter/excel_reporter/mem_stack/ea_xdm.py | Implemented | 2026-04-05 |
| SWR_EA_00004 | `src/eb_model/cli/ea_xdm_2_xls_cli.py:main` | src/eb_model/cli/ea_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## Fee Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_FEE_00001 | `src/eb_model/parser/mem_stack/fee_xdm_parser.py:FeeXdmParser:parse:30-49` | src/eb_model/parser/mem_stack/fee_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FEE_00002 | `src/eb_model/parser/mem_stack/fee_xdm_parser.py:FeeXdmParser:read_fee_general:48-63` | src/eb_model/parser/mem_stack/fee_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FEE_00003 | `src/eb_model/reporter/excel_reporter/mem_stack/fee_xdm.py:FeeXdmXlsWriter:write:45-51` | src/eb_model/reporter/excel_reporter/mem_stack/fee_xdm.py | Implemented | 2026-04-05 |
| SWR_FEE_00004 | `src/eb_model/cli/fee_xdm_2_xls_cli.py:main` | src/eb_model/cli/fee_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## MemIf Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_MEMIF_00001 | `src/eb_model/parser/mem_stack/memif_xdm_parser.py:MemIfXdmParser:parse:30-49` | src/eb_model/parser/mem_stack/memif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_MEMIF_00002 | `src/eb_model/parser/mem_stack/memif_xdm_parser.py:MemIfXdmParser:read_memif_init:48-63` | src/eb_model/parser/mem_stack/memif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_MEMIF_00003 | `src/eb_model/reporter/excel_reporter/mem_stack/memif_xdm.py:MemIfXdmXlsWriter:write:45-51` | src/eb_model/reporter/excel_reporter/mem_stack/memif_xdm.py | Implemented | 2026-04-05 |
| SWR_MEMIF_00004 | `src/eb_model/cli/memif_xdm_2_xls_cli.py:main` | src/eb_model/cli/memif_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## MemMap Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_MEMMAP_00001 | `src/eb_model/parser/mem_stack/memmap_xdm_parser.py:MemMapXdmParser:parse:30-49` | src/eb_model/parser/mem_stack/memmap_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_MEMMAP_00002 | `src/eb_model/parser/mem_stack/memmap_xdm_parser.py:MemMapXdmParser:read_memmap_common:48-63` | src/eb_model/parser/mem_stack/memmap_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_MEMMAP_00003 | `src/eb_model/reporter/excel_reporter/mem_stack/memmap_xdm.py:MemMapXdmXlsWriter:write:44-50` | src/eb_model/reporter/excel_reporter/mem_stack/memmap_xdm.py | Implemented | 2026-04-05 |
| SWR_MEMMAP_00004 | `src/eb_model/cli/memmap_xdm_2_xls_cli.py:main` | src/eb_model/cli/memmap_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## MemAcc Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_MEMACC_00001 | `src/eb_model/parser/mem_stack/memacc_xdm_parser.py:MemAccXdmParser:parse:30-49` | src/eb_model/parser/mem_stack/memacc_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_MEMACC_00002 | `src/eb_model/parser/mem_stack/memacc_xdm_parser.py:MemAccXdmParser:read_memacc_common:48-63` | src/eb_model/parser/mem_stack/memacc_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_MEMACC_00003 | `src/eb_model/reporter/excel_reporter/mem_stack/memacc_xdm.py:MemAccXdmXlsWriter:write:44-50` | src/eb_model/reporter/excel_reporter/mem_stack/memacc_xdm.py | Implemented | 2026-04-05 |
| SWR_MEMACC_00004 | `src/eb_model/cli/memacc_xdm_2_xls_cli.py:main` | src/eb_model/cli/memacc_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## Crypto Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_CRYPTO_00001 | `src/eb_model/parser/crypto_stack/crypto_xdm_parser.py:CryptoXdmParser:parse:25-46` | src/eb_model/parser/crypto_stack/crypto_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CRYPTO_00002 | `src/eb_model/parser/crypto_stack/crypto_xdm_parser.py:CryptoXdmParser:read_crypto_general:43-59` | src/eb_model/parser/crypto_stack/crypto_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CRYPTO_00003 | `src/eb_model/reporter/excel_reporter/crypto_stack/crypto_xdm.py:CryptoXdmXlsWriter:write:43-53` | src/eb_model/reporter/excel_reporter/crypto_stack/crypto_xdm.py | Implemented | 2026-04-05 |
| SWR_CRYPTO_00004 | `src/eb_model/cli/crypto_xdm_2_xls_cli.py:main` | src/eb_model/cli/crypto_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## CryIf Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_CRYIF_00001 | `src/eb_model/parser/crypto_stack/cryif_xdm_parser.py:CryIfXdmParser:parse:25-46` | src/eb_model/parser/crypto_stack/cryif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CRYIF_00002 | `src/eb_model/parser/crypto_stack/cryif_xdm_parser.py:CryIfXdmParser:read_cryif_general:42-58` | src/eb_model/parser/crypto_stack/cryif_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CRYIF_00003 | `src/eb_model/reporter/excel_reporter/crypto_stack/cryif_xdm.py:CryIfXdmXlsWriter:write:43-53` | src/eb_model/reporter/excel_reporter/crypto_stack/cryif_xdm.py | Implemented | 2026-04-05 |
| SWR_CRYIF_00004 | `src/eb_model/cli/cryif_xdm_2_xls_cli.py:main` | src/eb_model/cli/cryif_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## Csm Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_CSM_00001 | `src/eb_model/parser/crypto_stack/csm_xdm_parser.py:CsmXdmParser:parse:25-46` | src/eb_model/parser/crypto_stack/csm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CSM_00002 | `src/eb_model/parser/crypto_stack/csm_xdm_parser.py:CsmXdmParser:read_csm_general:42-58` | src/eb_model/parser/crypto_stack/csm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_CSM_00003 | `src/eb_model/reporter/excel_reporter/crypto_stack/csm_xdm.py:CsmXdmXlsWriter:write:43-53` | src/eb_model/reporter/excel_reporter/crypto_stack/csm_xdm.py | Implemented | 2026-04-05 |
| SWR_CSM_00004 | `src/eb_model/cli/csm_xdm_2_xls_cli.py:main` | src/eb_model/cli/csm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## SecOC Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_SECOC_00001 | `src/eb_model/parser/crypto_stack/secoc_xdm_parser.py:SecOCXdmParser:parse:25-46` | src/eb_model/parser/crypto_stack/secoc_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_SECOC_00002 | `src/eb_model/parser/crypto_stack/secoc_xdm_parser.py:SecOCXdmParser:read_secoc_general:42-58` | src/eb_model/parser/crypto_stack/secoc_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_SECOC_00003 | `src/eb_model/reporter/excel_reporter/crypto_stack/secoc_xdm.py:SecOCXdmXlsWriter:write:43-53` | src/eb_model/reporter/excel_reporter/crypto_stack/secoc_xdm.py | Implemented | 2026-04-05 |
| SWR_SECOC_00004 | `src/eb_model/cli/secoc_xdm_2_xls_cli.py:main` | src/eb_model/cli/secoc_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## FiM Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_FIM_00001 | `src/eb_model/parser/diag_stack/fim_xdm_parser.py:FiMXdmParser:parse:25-46` | src/eb_model/parser/diag_stack/fim_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FIM_00002 | `src/eb_model/parser/diag_stack/fim_xdm_parser.py:FiMXdmParser:read_fim_general:42-58` | src/eb_model/parser/diag_stack/fim_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_FIM_00003 | `src/eb_model/reporter/excel_reporter/diag_stack/fim_xdm.py:FiMXdmXlsWriter:write:43-53` | src/eb_model/reporter/excel_reporter/diag_stack/fim_xdm.py | Implemented | 2026-04-05 |
| SWR_FIM_00004 | `src/eb_model/cli/fim_xdm_2_xls_cli.py:main` | src/eb_model/cli/fim_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## Dcm Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_DCM_00001 | `src/eb_model/parser/diag_stack/dcm_xdm_parser.py:DcmXdmParser:parse:25-46` | src/eb_model/parser/diag_stack/dcm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_DCM_00002 | `src/eb_model/parser/diag_stack/dcm_xdm_parser.py:DcmXdmParser:read_dcm_general:42-58` | src/eb_model/parser/diag_stack/dcm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_DCM_00003 | `src/eb_model/reporter/excel_reporter/diag_stack/dcm_xdm.py:DcmXdmXlsWriter:write:43-53` | src/eb_model/reporter/excel_reporter/diag_stack/dcm_xdm.py | Implemented | 2026-04-05 |
| SWR_DCM_00004 | `src/eb_model/cli/dcm_xdm_2_xls_cli.py:main` | src/eb_model/cli/dcm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## Dem Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_DEM_00001 | `src/eb_model/parser/diag_stack/dem_xdm_parser.py:DemXdmParser:parse:25-46` | src/eb_model/parser/diag_stack/dem_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_DEM_00002 | `src/eb_model/parser/diag_stack/dem_xdm_parser.py:DemXdmParser:read_dem_general:42-58` | src/eb_model/parser/diag_stack/dem_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_DEM_00003 | `src/eb_model/reporter/excel_reporter/diag_stack/dem_xdm.py:DemXdmXlsWriter:write:43-53` | src/eb_model/reporter/excel_reporter/diag_stack/dem_xdm.py | Implemented | 2026-04-05 |
| SWR_DEM_00004 | `src/eb_model/cli/dem_xdm_2_xls_cli.py:main` | src/eb_model/cli/dem_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## Dlt Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_DLT_00001 | `src/eb_model/parser/diag_stack/dlt_xdm_parser.py:DltXdmParser:parse:25-46` | src/eb_model/parser/diag_stack/dlt_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_DLT_00002 | `src/eb_model/parser/diag_stack/dlt_xdm_parser.py:DltXdmParser:read_dlt_general:42-58` | src/eb_model/parser/diag_stack/dlt_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_DLT_00003 | `src/eb_model/reporter/excel_reporter/diag_stack/dlt_xdm.py:DltXdmXlsWriter:write:43-53` | src/eb_model/reporter/excel_reporter/diag_stack/dlt_xdm.py | Implemented | 2026-04-05 |
| SWR_DLT_00004 | `src/eb_model/cli/dlt_xdm_2_xls_cli.py:main` | src/eb_model/cli/dlt_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## J1939Dcm Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_J1939DCM_00001 | `src/eb_model/parser/j1939_stack/j1939dcm_xdm_parser.py:J1939DcmXdmParser:parse:25-46` | src/eb_model/parser/j1939_stack/j1939dcm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_J1939DCM_00002 | `src/eb_model/parser/j1939_stack/j1939dcm_xdm_parser.py:J1939DcmXdmParser:read_j1939dcm_general:42-58` | src/eb_model/parser/j1939_stack/j1939dcm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_J1939DCM_00003 | `src/eb_model/reporter/excel_reporter/j1939_stack/j1939dcm_xdm.py:J1939DcmXdmXlsWriter:write:44-54` | src/eb_model/reporter/excel_reporter/j1939_stack/j1939dcm_xdm.py | Implemented | 2026-04-05 |
| SWR_J1939DCM_00004 | `src/eb_model/cli/j1939dcm_xdm_2_xls_cli.py:main` | src/eb_model/cli/j1939dcm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## J1939Nm Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_J1939NM_00001 | `src/eb_model/parser/j1939_stack/j1939nm_xdm_parser.py:J1939NmXdmParser:parse:25-46` | src/eb_model/parser/j1939_stack/j1939nm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_J1939NM_00002 | `src/eb_model/parser/j1939_stack/j1939nm_xdm_parser.py:J1939NmXdmParser:read_j1939nm_general:42-58` | src/eb_model/parser/j1939_stack/j1939nm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_J1939NM_00003 | `src/eb_model/reporter/excel_reporter/j1939_stack/j1939nm_xdm.py:J1939NmXdmXlsWriter:write:44-54` | src/eb_model/reporter/excel_reporter/j1939_stack/j1939nm_xdm.py | Implemented | 2026-04-05 |
| SWR_J1939NM_00004 | `src/eb_model/cli/j1939nm_xdm_2_xls_cli.py:main` | src/eb_model/cli/j1939nm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## J1939Rm Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_J1939RM_00001 | `src/eb_model/parser/j1939_stack/j1939rm_xdm_parser.py:J1939RmXdmParser:parse:25-46` | src/eb_model/parser/j1939_stack/j1939rm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_J1939RM_00002 | `src/eb_model/parser/j1939_stack/j1939rm_xdm_parser.py:J1939RmXdmParser:read_j1939rm_general:42-58` | src/eb_model/parser/j1939_stack/j1939rm_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_J1939RM_00003 | `src/eb_model/reporter/excel_reporter/j1939_stack/j1939rm_xdm.py:J1939RmXdmXlsWriter:write:44-54` | src/eb_model/reporter/excel_reporter/j1939_stack/j1939rm_xdm.py | Implemented | 2026-04-05 |
| SWR_J1939RM_00004 | `src/eb_model/cli/j1939rm_xdm_2_xls_cli.py:main` | src/eb_model/cli/j1939rm_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## J1939Tp Module Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_J1939TP_00001 | `src/eb_model/parser/j1939_stack/j1939tp_xdm_parser.py:J1939TpXdmParser:parse:25-47` | src/eb_model/parser/j1939_stack/j1939tp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_J1939TP_00002 | `src/eb_model/parser/j1939_stack/j1939tp_xdm_parser.py:J1939TpXdmParser:read_j1939tp_general:43-59` | src/eb_model/parser/j1939_stack/j1939tp_xdm_parser.py | Implemented | 2026-04-05 |
| SWR_J1939TP_00003 | `src/eb_model/reporter/excel_reporter/j1939_stack/j1939tp_xdm.py:J1939TpXdmXlsWriter:write:44-54` | src/eb_model/reporter/excel_reporter/j1939_stack/j1939tp_xdm.py | Implemented | 2026-04-05 |
| SWR_J1939TP_00004 | `src/eb_model/cli/j1939tp_xdm_2_xls_cli.py:main` | src/eb_model/cli/j1939tp_xdm_2_xls_cli.py | Implemented | 2026-04-05 |

---

## CLI Layer Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_CLI_00001 | `src/eb_model/cli/eb_convert.py:main` | src/eb_model/cli/eb_convert.py | Implemented | 2026-04-05 |
| SWR_CLI_00002 | `src/eb_model/cli/eb_convert.py:main` | src/eb_model/cli/eb_convert.py | Implemented | 2026-04-05 |
| SWR_CLI_00003 | `src/eb_model/cli/pref_system_importer_cli.py:main` | src/eb_model/cli/pref_system_importer_cli.py | Implemented | 2026-04-05 |

---

## Reporter Layer Requirements

| Requirement ID | Implementation Location | Files | Status | Last Validated |
|----------------|------------------------|-------|--------|----------------|
| SWR_REPORTER_00001 | `src/eb_model/reporter/excel_reporter/core/abstract.py:ExcelReporter:27-74` | src/eb_model/reporter/excel_reporter/core/abstract.py | Implemented | 2026-04-05 |
| SWR_REPORTER_00002 | `src/eb_model/reporter/excel_reporter/core/abstract.py:ExcelReporter:auto_width:32-46` | src/eb_model/reporter/excel_reporter/core/abstract.py | Implemented | 2026-04-05 |
| SWR_REPORTER_00003 | `src/eb_model/reporter/excel_reporter/core/abstract.py:ExcelReporter:write_cell:53-64` | src/eb_model/reporter/excel_reporter/core/abstract.py | Implemented | 2026-04-05 |
| SWR_REPORTER_00004 | `src/eb_model/reporter/excel_reporter/core/abstract.py:ExcelReporter:save:75-85` | src/eb_model/reporter/excel_reporter/core/abstract.py | Implemented | 2026-04-05 |

---

## Summary Statistics

| Category | Total Requirements | Implemented | Pending | Draft | Deprecated |
|----------|-------------------|-------------|---------|-------|-------------|
| Parser Layer | 6 | 6 | 0 | 0 | 0 |
| Core Modules | 45 | 45 | 0 | 0 | 0 |
| CAN Stack | 20 | 20 | 0 | 0 | 0 |
| LIN Stack | 15 | 15 | 0 | 0 | 0 |
| FlexRay Stack | 25 | 25 | 0 | 0 | 0 |
| Ethernet Stack | 45 | 45 | 0 | 0 | 0 |
| COM Stack | 16 | 16 | 0 | 0 | 0 |
| Memory Stack | 28 | 28 | 0 | 0 | 0 |
| Crypto Stack | 16 | 16 | 0 | 0 | 0 |
| Diagnostics Stack | 16 | 16 | 0 | 0 | 0 |
| J1939 Stack | 16 | 16 | 0 | 0 | 0 |
| CLI Layer | 3 | 3 | 0 | 0 | 0 |
| Reporter Layer | 4 | 4 | 0 | 0 | 0 |
| **TOTAL** | **255** | **255** | **0** | **0** | **0** |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.1 | 2026-04-07 | Claude Code | Synchronization update - fixed ORPHAN_REQ (NvM file paths) and DRIFT (line number mismatches for Parser, OS, RTE, EcuC, BswM, Det, EcuM, Tm, PbcfgM modules) |
| 1.0 | 2026-04-05 | Claude Code | Initial traceability matrix with complete code-to-requirements mapping |

---

**Document End**