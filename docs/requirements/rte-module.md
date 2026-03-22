# RTE Module Requirements

## Module Overview

The RTE (Runtime Environment) module extracts AUTOSAR RTE configuration from EB Tresos Rte.xdm files. The RTE is the middleware layer that enables communication between software components and the underlying OS and BSW (Basic Software) modules in automotive embedded systems.

This module enables engineers to:
- Understand how runnable entities are mapped to OS tasks
- Analyze BSW module instance configurations and their event-to-task mappings
- Trace trigger events from software components to OS tasks
- Document activation timing, position in task, and server queue configurations
- Export event mappings for timing analysis and scheduling verification

## Functional Requirements

The RTE module shall:

**BSW Module Instance Configuration**
- Parse BSW module instance definitions with implementation references
- Extract OS application mappings for BSW instances
- Read BSW event-to-task mappings including:
  - Event references (single in AR 3.x, multiple in AR 4.0+)
  - Task references (mapped OS tasks)
  - Activation offset and position in task
  - Server queue length for client-server communication
  - Period for cyclic events

**Software Component Instance Configuration**
- Parse software component instance definitions
- Extract software component instance references
- Read OS application mappings for component instances
- Read event-to-task mappings including:
  - Event references (single in AR 3.x, multiple in AR 4.0+)
  - Task references (mapped OS tasks)
  - Activation offset and position in task
  - Server queue length for client-server communication
  - Period for cyclic events

**AUTOSAR Version Compatibility**
- Support AUTOSAR 3.x event reference format (single event reference)
- Support AUTOSAR 4.0+ event reference format (multiple event references)
- Automatically select appropriate parsing model based on AR major version

**Event Mapping Analysis**
- Group event-to-task mappings by target OS task
- Sort mappings by position in task for execution order analysis
- Distinguish between BSW module events and software component events
- Support events with no task mapping (events not mapped to any task)

**Version Information**
- Extract AUTOSAR version (major.minor.patch) from the RTE configuration
- Extract software version from the RTE configuration

## Data Model

Key classes and their relationships:

**Rte** (Module)
- Container for all RTE configuration objects
- Collections: BSW module instances, software component instances
- Method `getMappedEvents()` returns grouped event-to-task mappings by OS task name

**RteBswModuleInstance**
- Represents a BSW module instance (e.g., CAN driver, PWM handler)
- Attributes: implementation reference, OS application mapping
- Collections: event-to-task mappings, ISR mappings, trigger configurations

**RteSwComponentInstance**
- Represents a software component instance (application-level component)
- Attributes: software component instance reference, OS application mapping
- Collections: event-to-task mappings, ISR mappings, trigger configurations

**AbstractEventToTaskMapping**
- Abstract base for event-to-task mapping configurations
- Common attributes: position in task (execution order)

**RteBswEventToTaskMapping** (extends AbstractEventToTaskMapping)
- Represents mapping from BSW event to OS task
- Attributes: activation offset, period, server queue length
- References: BSW event reference(s), task reference

**RteEventToTaskMapping** (extends AbstractEventToTaskMapping)
- Represents mapping from software component event to OS task
- Attributes: activation offset, period, server queue length
- References: event reference(s), task reference

**Version-Specific Models:**
- `RteBswEventToTaskMappingV3` / `RteEventToTaskMappingV3` - AUTOSAR 3.x (single event ref)
- `RteBswEventToTaskMappingV4` / `RteEventToTaskMappingV4` - AUTOSAR 4.0+ (multiple event refs)

## Supported Operations

| Operation | Description | CLI Command | Input | Output |
|-----------|-------------|-------------|-------|--------|
| Extract RTE config | Parse RTE and export OS tasks/ISRs referenced by RTE | `rte-xdm-xlsx Rte.xdm output.xlsx` | Rte.xdm | Excel with OsTask/OsIsr sheets |
| Extract runnable entities | Parse RTE+OS and export event-to-task mappings | `rte-xdm-xlsx -r Rte.xdm Os.xdm output.xlsx` | Rte.xdm + Os.xdm | Excel with Event Mapping sheet |
| Multiple input files | Parse multiple XDM files (e.g., RTE + OS) | `rte-xdm-xlsx Rte.xdm Os.xdm output.xlsx` | Multiple XDMs | Combined Excel output |

## Excel Output Structure

### Basic RTE Export (`rte-xdm-xlsx Rte.xdm output.xlsx`)

The Excel workbook contains sheets referencing OS configuration:

1. **OsTask** - OS tasks referenced by RTE configuration
   - Columns: Name, Activation, Priority, Schedule, Stack Size
   - Read from Os.xdm (must be parsed as additional input)

2. **OsIsr** - OS ISRs referenced by RTE configuration
   - Columns: Name, Category, Stack Size
   - Read from Os.xdm (must be parsed as additional input)

### Runnable Entities Export (`rte-xdm-xlsx -r Rte.xdm Os.xdm output.xlsx`)

The Excel workbook contains event mapping information:

1. **Event Mapping** - Event-to-task mappings with execution details
   - Columns:
     - OsTask: Target OS task name
     - Event: Event name (or space-separated list for AR 4.0+)
     - Event Type: BSW or SW Component (indicated by executable entity)
     - Executable Entity: Implementation reference or software component instance
     - Instance: Module/component instance name
     - Position: Execution order within task (0 = first)
     - Offset: Activation offset (timing adjustment)

Each sheet includes auto-width column sizing and appropriate alignment.

## Practical Examples

### Command Line Usage

```bash
# Basic RTE configuration export (requires Os.xdm to be loaded separately)
rte-xdm-xlsx data/Rte.xdm data/Os.xdm data/Rte.xlsx

# Export runnable entity event mappings
rte-xdm-xlsx -r data/Rte.xdm data/Os.xdm data/Runnable.xlsx

# With verbose logging
rte-xdm-xlsx -v -r data/Rte.xdm data/Os.xdm data/Runnable.xlsx --log rte.log

# Multiple input files (factory pattern auto-detects module type)
rte-xdm-xlsx data/Rte.xdm data/Os.xdm data/NvM.xdm data/Combined.xlsx
```

### Programmatic Usage

```python
from eb_model.parser import RteXdmParser, OsXdmParser
from eb_model.models import EBModel
from eb_model.reporter import RteRunnableEntityXlsWriter, RteXdmXlsWriter

# Get singleton document model
doc = EBModel.getInstance()

# Parse RTE configuration
rte_parser = RteXdmParser()
rte_parser.parse_xdm("data/Rte.xdm", doc)

# Parse OS configuration (required for runnable entity export)
os_parser = OsXdmParser()
os_parser.parse_xdm("data/Os.xdm", doc)

# Access parsed data
rte = doc.getRte()
print(f"Found {len(rte.getRteBswModuleInstanceList())} BSW instances")
print(f"Found {len(rte.getRteSwComponentInstanceList())} SW component instances")

# Export basic RTE configuration
writer = RteXdmXlsWriter()
writer.write("reports/Rte.xlsx", doc)

# Export runnable entity event mappings
runnable_writer = RteRunnableEntityXlsWriter()
runnable_writer.write("reports/Runnable.xlsx", doc)
```

### Querying RTE Data

```python
# Get all BSW module instances
for bsw_instance in rte.getRteBswModuleInstanceList():
    print(f"BSW Module: {bsw_instance.getName()}")
    print(f"  Implementation: {bsw_instance.getRteBswImplementationRef().getValue()}")
    print(f"  Event Mappings: {len(bsw_instance.getRteBswEventToTaskMappingList())}")

# Get all software component instances
for swc_instance in rte.getRteSwComponentInstanceList():
    print(f"Component: {swc_instance.getName()}")
    print(f"  SWC Ref: {swc_instance.getRteSoftwareComponentInstanceRef().getValue()}")
    print(f"  Event Mappings: {len(swc_instance.getRteEventToTaskMappingList())}")

# Get event mappings grouped by OS task
mapped_events = rte.getMappedEvents()
for task_name, mappings in mapped_events.items():
    print(f"\nTask: {task_name}")
    for mapping in sorted(mappings, key=lambda m: m.getRtePositionInTaskNumber()):
        if isinstance(mapping, rte_xdm.RteBswEventToTaskMapping):
            event = mapping.getRteBswEventRef().getShortName()
            instance = mapping.getRteBswModuleInstance().getName()
        else:  # RteEventToTaskMapping
            event = mapping.getRteEventRef().getShortName()
            instance = mapping.getRteSwComponentInstance().getName()
        print(f"  Position {mapping.getRtePositionInTask()}: {event} from {instance}")
```

## AUTOSAR Version Handling

The parser automatically detects the AUTOSAR version and uses the appropriate model:

```python
# AUTOSAR 3.x (major version < 4)
# Uses RteEventToTaskMappingV3 with single event reference
mapping.setRteEventRef(single_event_ref)
event = mapping.getRteEventRef()  # Returns single EcucRefType

# AUTOSAR 4.0+ (major version >= 4)
# Uses RteEventToTaskMappingV4 with multiple event references
mapping.addRteEventRef(event_ref1)
mapping.addRteEventRef(event_ref2)
events = mapping.getRteEventRefs()  # Returns list of EcucRefType
```

## Limitations and Known Issues

1. **XDM Format Only**: Only supports EB Tresos XDM format, not generic AUTOSAR XML files

2. **OS Dependency**: Runnable entity export requires both Rte.xdm and Os.xdm to be parsed. The OS module provides task definitions that RTE events map to.

3. **Event Reference Validation**: ASPath references are extracted but not validated. References to non-existent tasks or events are stored as-is.

4. **AR 4.0 Multiple Events**: When using AR 4.0+ format with multiple event references per mapping, calling `getRteEventRef()` or `getRteBswEventRef()` will raise a ValueError if the mapping doesn't have exactly one event. Use `getRteEventRefs()` or `getRteBswEventRefs()` instead.

5. **Limited Test Coverage**: No dedicated test files for RTE parser exist in the current codebase.

6. **Unmapped Events**: Events with no task mapping (`RteMappedToTaskRef` is None) are excluded from the `getMappedEvents()` output.

7. **Typo in Reporter**: Line 82 in `rte_xdm.py` reporter has `isinstance` misspelled as `instance`. This may cause a runtime error when processing AR 4.0+ software component events.

8. **Position Default**: Events without explicit position default to 0, treated as first in task.

## Dependencies

The RTE module depends on:
- **OS Module**: Required for resolving task references in runnable entity export
- Both Rte.xdm and Os.xdm should be parsed when using `-r` (runnable entities) flag

The factory pattern in `EbParserFactory` automatically creates the correct parser instance when you pass multiple XDM files to the CLI.

## Related Documentation

- **[overview.md](overview.md)** - System architecture and common patterns
- **[os-module.md](os-module.md)** - OS module (for task definitions)
- **[CLAUDE.md](../../CLAUDE.md)** - Development guide for contributors
