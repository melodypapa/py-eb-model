# Software Requirements: NvM Module - Reporter Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | NvM Module Reporter Layer Requirements |
| Document ID | SWR_NVM_REPORTER_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | NvM (Non-Volatile Memory) - Reporter Layer |

---

## Overview

The NvM Reporter Layer provides Excel export functionality for AUTOSAR NvM configuration data.

**Implementation:** `src/eb_model/reporter/excel_reporter/mem_stack/nvm_xdm.py`

---

## Requirements

### SWR_NVM_REPORTER_00001 - Excel Workbook Creation

The reporter shall create an Excel workbook with multiple worksheets for NvM configuration.

**Worksheets:**
1. General - Version and common settings
2. BSW Distribution - Partition distribution
3. Block List - Block descriptor details

**Implementation:** `nvm_xdm.py:NvMXdmXlsWriter`
**Status:** Implemented

---

### SWR_NVM_REPORTER_00002 - General Sheet

The reporter shall write version information to the General worksheet.

**Columns:**
- AR Version (Major.Minor.Patch)
- SW Version (Major.Minor.Patch)
- Vendor ID
- Common settings (key-value pairs)

**Implementation:** `nvm_xdm.py:write_nvm_general`
**Status:** Implemented

---

### SWR_NVM_REPORTER_00003 - BSW Distribution Sheet

The reporter shall write partition distribution to the BSW Distribution worksheet.

**Columns:**
- Partition Name
- Block Count
- Master (indicator)

**Implementation:** `nvm_xdm.py:write_nvm_bsw_distribution`
**Status:** Implemented

---

### SWR_NVM_REPORTER_00004 - Block List Sheet

The reporter shall write block descriptor details to the Block List worksheet.

**Columns:**
- Name
- Block ID
- Block Number
- Block Length
- Management Type
- Job Priority
- CRC Type
- Memory Layer (EA/FEE)
- Partition

**Implementation:** `nvm_xdm.py:write_nvm_block_list`
**Status:** Implemented

---

### SWR_NVM_REPORTER_00005 - None Handling

The reporter shall handle missing NvMCommon gracefully.

- Skip General sheet if NvMCommon is None
- Skip BSW Distribution sheet if NvMCommon is None
- Continue with Block List sheet

**Implementation:** `nvm_xdm.py:write`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_NVM_REPORTER_00001 | nvm_xdm.py:NvMXdmXlsWriter | TC_UNIT_NVM_RPT_00001 |
| SWR_NVM_REPORTER_00002 | nvm_xdm.py:write_nvm_general | TC_UNIT_NVM_RPT_00002 |
| SWR_NVM_REPORTER_00003 | nvm_xdm.py:write_nvm_bsw_distribution | TC_UNIT_NVM_RPT_00003 |
| SWR_NVM_REPORTER_00004 | nvm_xdm.py:write_nvm_block_list | TC_UNIT_NVM_RPT_00004 |
| SWR_NVM_REPORTER_00005 | nvm_xdm.py:write | TC_UNIT_NVM_RPT_00005 |
