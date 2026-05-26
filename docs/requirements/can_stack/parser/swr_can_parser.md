# Software Requirements: CAN Stack - Parser Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | CAN Stack Parser Layer Requirements |
| Document ID | SWR_CAN_PARSER_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | CAN Stack - Parser Layer |

---

## Overview

The CAN Stack Parser Layer provides XDM file parsing for AUTOSAR CAN communication modules.

**Implementation:** `src/eb_model/parser/can_stack/`

---

## Requirements

### SWR_CANIF_PARSER_00001 - CanIf Module Validation

The parser shall validate that the XDM file contains CanIf module configuration.

- Extract module name from XDM datamodel root element
- Raise `ValueError` if module name is not "CanIf"
- Store namespace map for XPath queries

**Implementation:** `can_stack/canif_xdm_parser.py:CanIfXdmParser.parse`
**Status:** Implemented

---

### SWR_CANIF_PARSER_00002 - CanIf General Configuration Parsing

The parser shall parse CanIfGeneral element from XDM.

- Extract error detection settings
- Extract hardware unit counts
- Extract maximum PDU counts

**Implementation:** `can_stack/canif_xdm_parser.py:read_canif_general`
**Status:** Implemented

---

### SWR_CANIF_PARSER_00003 - CanIf Controller Parsing

The parser shall parse CanIfCtrlCfg elements from XDM.

- Extract controller ID and wakeup support
- Extract CAN controller references

**Implementation:** `can_stack/canif_xdm_parser.py:read_canif_ctrl_cfg`
**Status:** Implemented

---

### SWR_CANNM_PARSER_00001 - CanNm Module Validation

The parser shall validate that the XDM file contains CanNm module configuration.

**Implementation:** `can_stack/cannm_xdm_parser.py:CanNmXdmParser.parse`
**Status:** Implemented

---

### SWR_CANNM_PARSER_00002 - CanNm Channel Parsing

The parser shall parse CanNmChannel elements from XDM.

- Extract timing parameters
- Extract NM coordinator settings

**Implementation:** `can_stack/cannm_xdm_parser.py:read_cannm_channels`
**Status:** Implemented

---

### SWR_CANSM_PARSER_00001 - CanSm Module Validation

The parser shall validate that the XDM file contains CanSm module configuration.

**Implementation:** `can_stack/cansm_xdm_parser.py:CanSmXdmParser.parse`
**Status:** Implemented

---

### SWR_CANSM_PARSER_00002 - CanSm Network Parsing

The parser shall parse CanSmNetwork elements from XDM.

- Extract network ID and references
- Extract state transition parameters

**Implementation:** `can_stack/cansm_xdm_parser.py:read_cansm_networks`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_CANIF_PARSER_00001 | canif_xdm_parser.py:parse | TC_UNIT_CANIF_00001 |
| SWR_CANIF_PARSER_00002 | canif_xdm_parser.py:read_canif_general | TC_UNIT_CANIF_00002 |
| SWR_CANIF_PARSER_00003 | canif_xdm_parser.py:read_canif_ctrl_cfg | TC_UNIT_CANIF_00003 |
| SWR_CANNM_PARSER_00001 | cannm_xdm_parser.py:parse | TC_UNIT_CANNM_00001 |
| SWR_CANNM_PARSER_00002 | cannm_xdm_parser.py:read_cannm_channels | TC_UNIT_CANNM_00002 |
| SWR_CANSM_PARSER_00001 | cansm_xdm_parser.py:parse | TC_UNIT_CANSM_00001 |
| SWR_CANSM_PARSER_00002 | cansm_xdm_parser.py:read_cansm_networks | TC_UNIT_CANSM_00002 |
