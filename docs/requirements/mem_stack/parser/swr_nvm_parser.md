# Software Requirements: NvM Module - Parser Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | NvM Module Parser Layer Requirements |
| Document ID | SWR_NVM_PARSER_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | NvM (Non-Volatile Memory) - Parser Layer |

---

## Overview

The NvM Parser Layer provides XDM file parsing for AUTOSAR NvM configuration data.

**Implementation:** `src/eb_model/parser/mem_stack/nvm_xdm_parser.py`

---

## Requirements

### SWR_NVM_PARSER_00001 - Module Validation

The parser shall validate that the XDM file contains NvM module configuration.

- Extract module name from XDM datamodel root element
- Raise `ValueError` if module name is not "NvM"
- Store namespace map for XPath queries

**Implementation:** `nvm_xdm_parser.py:NvMXdmParser.parse`
**Status:** Implemented

---

### SWR_NVM_PARSER_00002 - Version Extraction

The parser shall extract version information from NvM configuration.

- Extract ARVersion (ArMajorVersion, ArMinorVersion, ArPatchVersion)
- Extract SwVersion (SwMajorVersion, SwMinorVersion, SwPatchVersion)
- Extract VendorId

**Implementation:** `nvm_xdm_parser.py:read_version_info`
**Status:** Implemented

---

### SWR_NVM_PARSER_00003 - Common Configuration Parsing

The parser shall parse NvMCommon element from XDM.

- Extract API configuration class and version
- Extract CRC configuration (NvMCrcNumOfBytes)
- Extract job prioritization and queue sizes
- Extract main function period
- Extract EcuC partition references

**Implementation:** `nvm_xdm_parser.py:read_nvm_common`
**Status:** Implemented

---

### SWR_NVM_PARSER_00004 - Block Descriptor Parsing

The parser shall parse NvMBlockDescriptor elements from XDM.

- Extract block identifier, number, and base number
- Extract block length and management type
- Extract job priority and retry counts
- Extract CRC type and usage settings
- Extract read/write all selection flags
- Extract EcuC partition reference

**Implementation:** `nvm_xdm_parser.py:read_nvm_block_descriptors`
**Status:** Implemented

---

### SWR_NVM_PARSER_00005 - Memory Layer Reference Parsing

The parser shall parse memory layer references from XDM.

- Parse NvMEaRef for EEPROM Abstraction layer
- Parse NvMFeeRef for Flash EEPROM Emulation layer
- Use choice field to determine correct reference type
- Raise `ValueError` for invalid choice values

**Implementation:** `nvm_xdm_parser.py:read_target_block_reference`
**Status:** Implemented

---

### SWR_NVM_PARSER_00006 - Callback Parsing

The parser shall parse NvM callback configurations from XDM.

- Extract init block callback function reference
- Extract single block callback function reference
- Extract read RAM block from NvM callback
- Extract write RAM block to NvM callback
- Handle absence of optional callbacks gracefully

**Implementation:** `nvm_xdm_parser.py:read_callbacks`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_NVM_PARSER_00001 | nvm_xdm_parser.py:parse | TC_UNIT_NVM_00001 |
| SWR_NVM_PARSER_00002 | nvm_xdm_parser.py:read_version_info | TC_UNIT_NVM_00002 |
| SWR_NVM_PARSER_00003 | nvm_xdm_parser.py:read_nvm_common | TC_UNIT_NVM_00003 |
| SWR_NVM_PARSER_00004 | nvm_xdm_parser.py:read_nvm_block_descriptors | TC_UNIT_NVM_00004 |
| SWR_NVM_PARSER_00005 | nvm_xdm_parser.py:read_target_block_reference | TC_UNIT_NVM_00005 |
| SWR_NVM_PARSER_00006 | nvm_xdm_parser.py:read_callbacks | TC_UNIT_NVM_00006 |
