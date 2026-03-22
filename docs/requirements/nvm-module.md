# NvM Module Requirements

## Module Overview

The NvM (Non-Volatile Memory) module extracts AUTOSAR NvM configuration from EB Tresos NvM.xdm files. The NvM module manages data persistence in automotive embedded systems, handling read/write operations to flash memory (EEPROM/EEPROM emulation) for preserving configuration data, adaptation values, and DTCs across power cycles.

This module enables engineers to:
- Extract NvM block configurations (size, location, CRC settings)
- Analyze memory block distribution across partitions
- Understand EEPROM/Flash abstraction layer references
- Document callback functions for data validation and synchronization
- Export block configurations for memory planning and verification

## Functional Requirements

The NvM module shall:

**Common Configuration**
- Parse NvMCommon configuration with global NvM settings:
  - API configuration class and version information
  - CRC configuration (number of bytes)
  - Dataset selection bits for multi-block datasets
  - Error detection and development error detection settings
  - Dynamic configuration support
  - Job prioritization and queue management
  - Main function period and polling mode
  - Multi-block callback settings
  - Repeat mirror operations configuration
  - Set RAM block status API
  - Immediate and standard job queue sizes
  - Version info API
  - Buffer alignment value
- Parse EcuC partition references for multi-partition systems
- Parse master EcuC partition reference

**Block Descriptors**
- Parse NvM block descriptor definitions including:
  - Block identifier and block number
  - NVRAM block base number
  - Block length (size in bytes)
  - Block management type
  - Job priority
  - ROM block number and data address
  - RAM block data address
  - EcuC partition reference
  - Resistance to software changes
  - CRC type and CRC usage
  - Read/Write all selection flags
  - RTE service port and job finished port flags
  - Block use synchronization mechanism
  - Callback function references
- Parse block-specific callback configurations:
  - Init block callback function
  - Single block callback function
  - Read RAM block from NvM callback
  - Write RAM block to NvM callback
- Parse target block references:
  - NvMEaRef: References EEPROM Abstraction layer blocks
  - NvMFeeRef: References Flash EEPROM Emulation layer blocks

**Version Information**
- Extract AUTOSAR version (major.minor.patch) from the NvM configuration
- Extract software version from the NvM configuration

## Data Model

Key classes and their relationships:

**NvM** (Module)
- Container for all NvM configuration objects
- Collections: block descriptors
- Singleton NvMCommon configuration

**NvMCommon**
- Global NvM configuration parameters
- Attributes: API config class, CRC settings, queue sizes, job prioritization
- References: EcuC partition references, master partition reference

**NvMBlockDescriptor**
- Represents a single NVRAM block configuration
- Attributes: block ID, size, addresses, CRC settings, management type
- References: EcuC partition, target block reference (EA or FEE)
- Callbacks: init block, single block, read RAM, write RAM

**NvMTargetBlockReference** (abstract)
- Abstract base for memory layer references
- Subclasses: NvMEaRef, NvMFeeRef

**NvMEaRef** (extends NvMTargetBlockReference)
- Reference to EEPROM Abstraction layer block
- Attribute: name of EA block

**NvMFeeRef** (extends NvMTargetBlockReference)
- Reference to Flash EEPROM Emulation layer block
- Attribute: name of FEE block

**NvMInitBlockCallback**
- Configuration for initialization callback
- Attribute: callback function name

**NvMSingleBlockCallback**
- Configuration for single-block operation callback
- Attribute: callback function name

## Supported Operations

| Operation | Description | CLI Command | Input | Output |
|-----------|-------------|-------------|-------|--------|
| Extract NvM config | Parse and export NvM configuration to Excel | `nvm-xdm-xlsx NvM.xdm output.xlsx` | NvM.xdm | Multi-sheet Excel (.xlsx) |

## Excel Output Structure

The Excel workbook contains the following sheets:

1. **General** - Global NvM configuration
   - Key-value pairs for common settings
   - Fields: NvMCompiledConfigId, NvMDatasetSelectionBits, retry counts

2. **BSW Distribution** - Partition distribution for multi-partition systems
   - Columns:
     - NvMEcucPartitionRef: Partition name
     - Master: Y/N indicator for master partition

3. **Block List** - NvM block descriptor details
   - Columns:
     - BlockId: NVRAM block identifier
     - Name: Block name
     - NvMBlockEcucPartitionRef: Partition reference
     - NvMRamBlockDataAddress: RAM address
     - NvMRomBlockDataAddress: ROM address
     - NvMBlockJobPriority: Job priority
     - NvMResistantToChangedSw: Y/N (boolean)
     - NvMBlockManagementType: Management type
     - NvMNvBlockLength: Block size
     - NvMBlockCrcType: CRC type (if CRC enabled)
     - NvMNvBlockNum: Block number
     - NvMSelectBlockForReadAll: Y/N (boolean)
     - NvMSelectBlockForWriteAll: Y/N (boolean)
     - NvMProvideRteJobFinishedPort: Y/N (boolean)
     - NvMProvideRteServicePort: Y/N (boolean)
     - NvMInitBlockCallbackFnc: Init callback name
     - NvMSingleBlockCallbackFnc: Single block callback name
     - NvMReadRamBlockFromNvCallback: Read callback name
     - NvMWriteRamBlockToNvCallback: Write callback name
     - NvMBlockUseSyncMechanism: Y/N (boolean)
     - NvMNvBlockBaseNumber: Base number
     - NvMFeeRef: FEE block reference (if applicable)

Each sheet includes auto-width column sizing and appropriate alignment.

## Practical Examples

### Command Line Usage

```bash
# Basic NvM configuration extraction
nvm-xdm-xlsx data/NvM.xdm reports/NvM.xlsx

# The Excel output will contain:
# - General: Global settings
# - BSW Distribution: Partition mapping
# - Block List: All block configurations
```

### Programmatic Usage

```python
from eb_model.parser import NvMXdmParser
from eb_model.models import EBModel
from eb_model.reporter import NvMXdmXlsWriter

# Get singleton document model
doc = EBModel.getInstance()

# Parse NvM XDM file
parser = NvMXdmParser()
parser.parse_xdm("data/NvM.xdm", doc)

# Access parsed data
nvm = doc.getNvM()
print(f"Found {len(nvm.getNvMBlockDescriptorList())} NvM blocks")

# Access common configuration
nvm_common = nvm.getNvMCommon()
if nvm_common:
    print(f"Config ID: {nvm_common.getNvMCompiledConfigId()}")
    print(f"Dataset Selection Bits: {nvm_common.getNvMDatasetSelectionBits()}")
    print(f"Partitions: {len(nvm_common.getNvMEcucPartitionRefList())}")

# Export to Excel
writer = NvMXdmXlsWriter()
writer.write("reports/NvM.xlsx", doc, options={})
```

### Querying NvM Data

```python
# Get all block descriptors
for block in nvm.getNvMBlockDescriptorList():
    print(f"Block: {block.getName()}")
    print(f"  ID: {block.getNvMNvramBlockIdentifier()}")
    print(f"  Size: {block.getNvMNvBlockLength()} bytes")
    print(f"  Management Type: {block.getNvMBlockManagementType()}")
    print(f"  CRC: {block.getNvMBlockUseCrc()} ({block.getNvMBlockCrcType()})")

    # Check target block reference
    target_ref = block.getNvMTargetBlockReference()
    if isinstance(target_ref, nvm_xdm.NvMFeeRef):
        print(f"  FEE Block: {target_ref.getNvMNameOfFeeBlock().getShortName()}")
    elif isinstance(target_ref, nvm_xdm.NvMEaRef):
        print(f"  EA Block: {target_ref.getNvMNameOfEaBlock().getShortName()}")

    # Check callbacks
    if block.getNvMInitBlockCallback():
        print(f"  Init Callback: {block.getNvMInitBlockCallback().getNvMInitBlockCallbackFnc()}")
    if block.getNvMSingleBlockCallback():
        print(f"  Single Callback: {block.getNvMSingleBlockCallback().getNvMSingleBlockCallbackFnc()}")

# Analyze partition distribution
nvm_common = nvm.getNvMCommon()
if nvm_common:
    master_ref = nvm_common.getNvMMasterEcucPartitionRef()
    print(f"\nMaster Partition: {master_ref.getShortName()}")

    print("\nAll Partitions:")
    for partition_ref in nvm_common.getNvMEcucPartitionRefList():
        is_master = (partition_ref.getShortName() == master_ref.getShortName())
        print(f"  - {partition_ref.getShortName()} {'(Master)' if is_master else ''}")
```

## Limitations and Known Issues

1. **XDM Format Only**: Only supports EB Tresos XDM format, not generic AUTOSAR XML files

2. **EA Reference Not Supported**: The reporter raises `NotImplementedError` when encountering NvMEaRef (EEPROM Abstraction) target block references. Only NvMFeeRef (Flash EEPROM Emulation) is fully supported in the Excel export.

3. **Missing Configuration**: If NvMCommon is not present in the XDM, the General and BSW Distribution sheets are skipped with an error log message.

4. **Hardcoded Values**: Some values in the General sheet are hardcoded (e.g., NvMMaxNumOfReadRetries and NvMMaxNumOfWriteRetries are always shown as "3" regardless of actual configuration).

5. **Optional Attributes**: Many block attributes are optional and may be None. Code using the model should check for None before accessing optional attributes.

6. **Limited Test Coverage**: Test coverage focuses on basic parsing functionality. Edge cases for different memory layer references and callback configurations have limited testing.

7. **Target Block Reference Choice**: The parser uses a choice field (`NvMTargetBlockReference`) to determine whether to parse NvMEaRef or NvMFeeRef. Invalid choice values raise a ValueError.

8. **Thread Safety**: The parser is not thread-safe. Use separate parser instances for concurrent parsing operations.

## Dependencies

The NvM module has no dependencies on other py-eb-model modules. It can be used standalone to parse NvM configuration files.

However, NvM blocks may reference EcuC partitions via `NvMBlockEcucPartitionRef` and `NvMEcucPartitionRef` in NvMCommon. If you need to resolve these references to partition details, you'll also need to parse the EcuC.xdm file using the EcuC module.

## Memory Layer References

NvM blocks can reference two types of memory abstraction layers:

1. **NvMEaRef**: References EEPROM Abstraction (EA) layer blocks
   - Used for direct EEPROM access
   - Contains `NvMNameOfEaBlock` reference

2. **NvMFeeRef**: References Flash EEPROM Emulation (FEE) layer blocks
   - Used for flash-based EEPROM emulation
   - Contains `NvMNameOfFeeBlock` reference
   - Fully supported in Excel export

The choice between EA and FEE depends on the hardware platform and memory architecture.

## Related Documentation

- **[overview.md](overview.md)** - System architecture and common patterns
- **[ecuc-module.md](ecuc-module.md)** - ECU Configuration module (for partition references)
- **[CLAUDE.md](../../CLAUDE.md)** - Development guide for contributors
