# Software Requirements: NvM Module - Model Layer

## Document Information

| Field | Value |
|-------|-------|
| Document Title | NvM Module Model Layer Requirements |
| Document ID | SWR_NVM_MODELS_00001 |
| Version | 1.0 |
| Date | 2026-05-27 |
| Project | py-eb-model |
| Module | NvM (Non-Volatile Memory) - Model Layer |

---

## Overview

The NvM Model Layer provides Python classes representing AUTOSAR NvM configuration entities.

**Implementation:** `src/eb_model/models/mem_stack/nvm_xdm.py`

---

## Requirements

### SWR_NVM_MODELS_00001 - NvM Model (Root)

The system shall provide an `NvM` root model class containing all NvM entities.

**Methods:**
- `getNvMBlockDescriptorList()` - Get all block descriptors
- `getNvMCommon()` - Get common configuration
- `setNvMCommon(common)` - Set common configuration
- `addNvMBlockDescriptor(block)` - Add block descriptor

**Implementation:** `nvm_xdm.py:NvM`
**Status:** Implemented

---

### SWR_NVM_MODELS_00002 - NvMCommon Model

The system shall provide an `NvMCommon` model class for global NvM settings.

| Field | Type | Description |
|-------|------|-------------|
| NvMApiConfigClass | str | API configuration class |
| NvMCrcNumOfBytes | int | CRC number of bytes |
| NvMJobPrioritization | bool | Job prioritization enabled |
| NvMMainFunctionPeriod | float | Main function period |
| NvMSizeImmediateJobQueue | int | Immediate job queue size |
| NvMSizeStandardJobQueue | int | Standard job queue size |
| NvMEcuCPartitionRefs | List[EcucRefType] | ECU partition references |
| NvMMasterEcuCPartitionRef | EcucRefType | Master partition reference |

**Implementation:** `nvm_xdm.py:NvMCommon`
**Status:** Implemented

---

### SWR_NVM_MODELS_00003 - NvMBlockDescriptor Model

The system shall provide an `NvMBlockDescriptor` model class for NvM block configuration.

| Field | Type | Description |
|-------|------|-------------|
| NvMBlockIdentifier | int | Block identifier |
| NvMBlockNumber | int | Block number |
| NvMBlockBaseNumber | int | Base number |
| NvMBlockLength | int | Block length in bytes |
| NvMNvBlockNum | int | Number of NV blocks |
| NvMRomBlockNum | int | Number of ROM blocks |
| NvMRamBlockNum | int | Number of RAM blocks |
| NvMJobPriority | int | Job priority |
| NvMBlockManagementType | str | Management type |
| NvMSelectBlockForReadAll | bool | Read all selection |
| NvMSelectBlockForWriteAll | bool | Write all selection |
| NvMCrcType | str | CRC type |
| NvMUseCrc | bool | CRC usage flag |
| NvMUseSyncMechanism | bool | Sync mechanism flag |
| NvMBlockWriteProt | bool | Write protection flag |
| NvMBlockUseAutoValidation | bool | Auto validation flag |
| NvMBlockUseSetRamBlockStatus | bool | Set RAM block status flag |
| NvMBlockHeaderInclude | bool | Block header include flag |
| NvMBlockUseCRCCompMechanism | bool | CRC comparison flag |
| NvMWriteBlockOnce | bool | Write once flag |
| NvMBlockJobPriority | int | Block job priority |
| NvMBlockMaxNumOfReadRetries | int | Max read retries |
| NvMBlockMaxNumOfWriteRetries | int | Max write retries |

**Implementation:** `nvm_xdm.py:NvMBlockDescriptor`
**Status:** Implemented

---

### SWR_NVM_MODELS_00004 - Memory Layer References

The system shall provide memory layer reference models.

| Class | Purpose |
|-------|---------|
| NvMEaRef | EEPROM Abstraction layer reference |
| NvMFeeRef | Flash EEPROM Emulation layer reference |

**Implementation:** `nvm_xdm.py:NvMEaRef`, `nvm_xdm.py:NvMFeeRef`
**Status:** Implemented

---

### SWR_NVM_MODELS_00005 - NvMTargetBlockReference Model

The system shall provide an `NvMTargetBlockReference` model class for block references.

| Field | Type | Description |
|-------|------|-------------|
| NvMEaRef | NvMEaRef | EA reference (choice) |
| NvMFeeRef | NvMFeeRef | FEE reference (choice) |

**Implementation:** `nvm_xdm.py:NvMTargetBlockReference`
**Status:** Implemented

---

## Traceability

| Requirement ID | Implementation | Test Cases |
|----------------|----------------|------------|
| SWR_NVM_MODELS_00001 | nvm_xdm.py:NvM | UTS_NVM_MODEL_00001 |
| SWR_NVM_MODELS_00002 | nvm_xdm.py:NvMCommon | UTS_NVM_MODEL_00002 |
| SWR_NVM_MODELS_00003 | nvm_xdm.py:NvMBlockDescriptor | UTS_NVM_MODEL_00003 |
| SWR_NVM_MODELS_00004 | nvm_xdm.py:NvMEaRef | UTS_NVM_MODEL_00004 |
| SWR_NVM_MODELS_00005 | nvm_xdm.py:NvMTargetBlockReference | UTS_NVM_MODEL_00005 |
