# EcuC Module Requirements

## Module Overview

The EcuC (ECU Configuration) module extracts AUTOSAR ECU Configuration from EB Tresos EcuC.xdm files. The EcuC module defines the partitioning of ECU software, separating software components and BSW modules into partitions for memory protection, isolation, and multi-core support.

This module enables engineers to:
- Extract ECU partition definitions and their properties
- Understand which software components are assigned to each partition
- Document partition restart capabilities and BSW partition settings
- Analyze partition-to-core mappings for multi-core systems
- Export partition configurations for system architecture documentation

## Functional Requirements

The EcuC module shall:

**Partition Collection**
- Parse the EcucPartitionCollection container
- Extract all EcucPartition definitions within the collection

**Partition Configuration**
- Parse partition attributes including:
  - Partition name
  - Default BSW partition flag
  - Partition restart capability
  - Partition reference (self-reference to partition definition)

**Software Component Instance References**
- Parse software component instance references within each partition
- Extract target references for each software component instance
- Support linking software components to their hosting partitions

**Version Information**
- Extract AUTOSAR version (major.minor.patch) from the EcuC configuration
- Extract software version from the EcuC configuration

## Data Model

Key classes and their relationships:

**EcuC** (Module)
- Container for all ECU configuration objects
- Singleton EcucPartitionCollection

**EcucPartitionCollection**
- Container for partition definitions
- Collections: partitions

**EcucPartition** (EcucParamConfContainerDef)
- Represents an ECU partition (memory isolation boundary)
- Attributes:
  - Name: Partition identifier
  - EcucDefaultBswPartition: Whether this is the default BSW partition
  - PartitionCanBeRestarted: Whether the partition can be restarted independently
  - EcucPartitionRef: Self-reference to partition definition
  - EcucPartitionId: Partition ID number
  - EcucPartitionCoreRef: Core assignment (for multi-core)
- Collections: software component instance references, BSW module distinguished partitions

**EcucPartitionSoftwareComponentInstanceRef**
- Reference to a software component instance assigned to a partition
- Attributes:
  - Type: Instance type (from XML type attribute)
  - TargetRef: Reference to the software component instance

## Supported Operations

| Operation | Description | CLI Command | Input | Output |
|-----------|-------------|-------------|-------|--------|
| Extract EcuC config | Parse and export EcuC configuration to Excel | `ecuc-xdm-xlsx EcuC.xdm output.xlsx` | EcuC.xdm | Multi-sheet Excel (.xlsx) |

## Excel Output Structure

The Excel workbook contains the following sheets:

1. **EcucPartition** - Partition definitions
   - Columns:
     - EcucPartition: Partition name
     - PartitionCanBeRestarted: Y/N (boolean)
     - EcucPartitionRef: Partition reference path

2. **SoftwareComponent** - Software component assignments
   - Columns:
     - Instance: Software component instance reference path
     - EcucPartition: Hosting partition name

Each sheet includes auto-width column sizing.

## Practical Examples

### Command Line Usage

```bash
# Basic EcuC configuration extraction
ecuc-xdm-xlsx data/EcuC.xdm reports/EcuC.xlsx

# The Excel output will contain:
# - EcucPartition: All partition definitions
# - SoftwareComponent: Software component assignments to partitions
```

### Programmatic Usage

```python
from eb_model.parser import EcucXdmParser
from eb_model.models import EBModel
from eb_model.reporter import EcucXdmXlsWriter

# Get singleton document model
doc = EBModel.getInstance()

# Parse EcuC XDM file
parser = EcucXdmParser()
parser.parse_xdm("data/EcuC.xdm", doc)

# Access parsed data
ecuc = doc.getEcuC()
collection = ecuc.getEcucPartitionCollection()
print(f"Found {len(collection.getEcucPartitions())} partitions")

# Export to Excel
writer = EcucXdmXlsWriter()
writer.write("reports/EcuC.xlsx", doc)
```

### Querying EcuC Data

```python
# Get all partitions
collection = doc.getEcuC().getEcucPartitionCollection()
for partition in collection.getEcucPartitions():
    print(f"Partition: {partition.getName()}")
    print(f"  Can Restart: {partition.getPartitionCanBeRestarted()}")
    print(f"  Default BSW: {partition.getEcucDefaultBswPartition()}")
    print(f"  Software Components: {len(partition.getEcucPartitionSoftwareComponentInstanceRefs())}")

    # List software components in this partition
    for instance_ref in partition.getEcucPartitionSoftwareComponentInstanceRefs():
        target = instance_ref.getTargetRef()
        print(f"    - {target.getValue()}")

# Analyze software component distribution
print("\nSoftware Component Distribution:")
for partition in collection.getEcucPartitions():
    count = len(partition.getEcucPartitionSoftwareComponentInstanceRefs())
    print(f"  {partition.getName()}: {count} components")
```

## Use Cases

### Multi-Partition Systems

Document how software is distributed across partitions for memory protection and isolation:

```python
# Find BSW partitions
bsw_partitions = [p for p in collection.getEcucPartitions()
                  if p.getEcucDefaultBswPartition()]

print("BSW Partitions:")
for partition in bsw_partitions:
    print(f"  - {partition.getName()}")

# Find application partitions
app_partitions = [p for p in collection.getEcucPartitions()
                  if not p.getEcucDefaultBswPartition()]

print("\nApplication Partitions:")
for partition in app_partitions:
    print(f"  - {partition.getName()} ({len(partition.getEcucPartitionSoftwareComponentInstanceRefs())} components)")
```

### Partition Restart Capability

Identify which partitions support independent restart (useful for fault management analysis):

```python
restartable_partitions = [p for p in collection.getEcucPartitions()
                          if p.getPartitionCanBeRestarted()]

print("Restartable Partitions:")
for partition in restartable_partitions:
    print(f"  - {partition.getName()}")
```

## Limitations and Known Issues

1. **XDM Format Only**: Only supports EB Tresos XDM format, not generic AUTOSAR XML files

2. **Missing Partition ID**: The `EcucPartitionId` attribute is defined in the model but not parsed from the XDM file. It will always be None.

3. **Limited Attributes**: Several attributes defined in the model are not parsed:
   - `EcucPartitionRef` (commented out in parser)
   - `EcucPartitionBswModuleDistinguishedPartitions`
   - `EcucPartitionCoreRef`
   - These are reserved for future use or EB-specific extensions

4. **Empty Target References**: The reporter does not check if `instance.getTargetRef()` is None before accessing it in the SoftwareComponent sheet. Empty TARGET references in the XDM will cause a runtime error.

5. **No Test Coverage**: No dedicated test files exist for the EcuC parser in the current codebase.

6. **Partition Collection Required**: If EcucPartitionCollection is not present in the XDM, accessing it will return None, and the reporter will fail.

7. **Thread Safety**: The parser is not thread-safe. Use separate parser instances for concurrent parsing operations.

## Dependencies

The EcuC module has no dependencies on other py-eb-model modules. It can be used standalone to parse EcuC configuration files.

However, EcuC partitions are referenced by other modules:
- **OS Module**: OS applications reference EcuC partitions via `OsAppEcucPartitionRef`
- **NvM Module**: NvM common configuration and blocks reference EcuC partitions

To resolve these references to partition details, you'll also need to parse the EcuC.xdm file.

## Partition Architecture

AUTOSAR partitions provide:
- **Memory Isolation**: Separate memory regions for different software components
- **Fault Containment**: Faults in one partition don't affect others
- **Independent Restart**: Partitions can be restarted without rebooting the entire ECU
- **Multi-Core Support**: Partitions can be assigned to different cores

A typical ECU has:
- One or more BSW partitions (contain basic software modules)
- One or more application partitions (contain software components)

## Related Documentation

- **[overview.md](overview.md)** - System architecture and common patterns
- **[os-module.md](os-module.md)** - OS module (for application partition references)
- **[nvm-module.md](nvm-module.md)** - NvM module (for partition references)
- **[CLAUDE.md](../../CLAUDE.md)** - Development guide for contributors
