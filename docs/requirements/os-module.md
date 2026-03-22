# OS Module Requirements

## Module Overview

The OS module extracts AUTOSAR Operating System configuration from EB Tresos Os.xdm files. The OS configuration defines task scheduling, interrupt handling, resource management, and memory protection for automotive embedded systems.

This module enables engineers to:
- Extract and analyze OS task configurations (priorities, stack sizes, autostart settings)
- Review Interrupt Service Routine (ISR) definitions and their hardware mappings
- Understand schedule table structures and timing relationships
- Document resource allocation and application boundaries for safety-critical systems
- Export complex OS configurations to Excel for review and documentation purposes

## Functional Requirements

The OS module shall:

**Task Management**
- Parse OS task definitions including name, priority, activation count, and schedule type
- Extract task stack size and type (BASIC/EXTENDED) for memory planning
- Read task autostart configuration with application mode references
- Parse task resource references for resource locking analysis
- Support task schedule types: FULL (preemptable) and NON (non-preemptable)

**Interrupt Service Routines**
- Parse ISR definitions including category (CATEGORY_1 or CATEGORY_2) and stack size
- Extract ISR priority and vector information
- Support Infineon AURIX TriCore-specific attributes (IrqLevel, Vector)
- Support ARM core-specific attributes (IrqLevel, Vector)
- Parse EB Safety OS memory region references for memory protection

**Schedule Tables**
- Parse schedule table definitions including duration, repeating behavior, and counter references
- Extract expiry points with offset values
- Read task activation configurations at expiry points
- Read event settings with event and task references
- Support adjustable expiry points with max lengthen/shorten values
- Parse time unit specifications (NANOSECONDS or TICKS)

**Counters**
- Parse counter definitions including max allowed value, min cycle, and ticks per base
- Extract counter type (HARDWARE or SOFTWARE)
- Read seconds per tick configuration for timing calculations

**Applications**
- Parse OS application definitions including trusted status and core assignment
- Extract application-to-partition references for multi-core systems
- Read application references to tasks, ISRs, resources, alarms, counters, and schedule tables
- Support application boundary definitions for memory protection and isolation

**Alarms**
- Parse alarm definitions with counter references
- Extract alarm action configurations:
  - ActivateTask: Reference to task to activate
  - IncrementCounter: Reference to counter to increment
  - SetEvent: Reference to event and task
  - Callback: Callback function name
- Read alarm accessing application references

**Resources**
- Parse resource definitions with properties (STANDARD or INTERNAL)
- Extract resource accessing application references
- Support calculated service access (`@CALC(SvcAs,...)` ) for EB-specific configurations

**Memory Protection**
- Parse microkernel memory protection configuration
- Extract memory region definitions with access permissions
- Read access flags for different thread types:
  - InitThread, IdleThread, OsThread, ErrorHook, ProtHook, ShutdownHook
  - Shutdown, Kernel access
  - Initialize per-core settings
- Support memory region initialization and global scope flags

**Version Information**
- Extract AUTOSAR version (major.minor.patch) from the OS configuration
- Extract software version from the OS configuration

## Data Model

Key classes and their relationships:

**Os** (Module)
- Container for all OS configuration objects
- Manages task-to-application and ISR-to-application mappings for quick lookup
- Collections: tasks, ISRs, alarms, schedule tables, counters, applications, resources

**OsTask**
- Represents an OS task with priority, activation, schedule type, stack size
- Optional: task type, autostart configuration, resource references
- Method `IsPreemptable()` returns true if schedule type is FULL

**OsIsr**
- Represents an interrupt service routine
- Attributes: category, priority, vector, stack size
- Vendor-specific: TriCore IRQ level/vector, ARM IRQ level/vector
- Memory protection: MkMemoryRegion references (EB Safety OS)

**OsScheduleTable**
- Represents a schedule table for cyclic scheduling
- References a counter for timing
- Contains expiry points with offsets and actions

**OsScheduleTableExpiryPoint**
- Represents a point in time within a schedule table
- Contains task activations and event settings
- Optional: adjustable expiry point configuration

**OsApplication**
- Represents an OS application for memory protection and isolation
- Attributes: trusted status, core assignment, partition reference
- References: tasks, ISRs, resources, alarms, counters, schedule tables

**OsCounter**
- Represents a counter for time measurement
- Type: HARDWARE or SOFTWARE
- Attributes: max allowed value, min cycle, ticks per base, seconds per tick

**OsAlarm**
- Represents an alarm for time-based events
- References a counter
- Action: ActivateTask, IncrementCounter, SetEvent, or Callback

**OsResource**
- Represents a resource for exclusive access management
- Property: STANDARD or INTERNAL
- References to accessing applications

**OsMicrokernel / MkMemoryProtection / MkMemoryRegion**
- Memory protection configuration for EB Safety OS
- Memory region access permissions per thread type
- Initialization and scope settings

## Supported Operations

| Operation | Description | CLI Command | Input | Output |
|-----------|-------------|-------------|-------|--------|
| Extract OS config | Parse and export OS configuration to Excel | `os-xdm-xlsx input.xdm output.xlsx` | Os.xdm | Multi-sheet Excel (.xlsx) |
| Extract with verbose logging | Enable debug logging during extraction | `os-xdm-xlsx -v input.xdm output.xlsx` | Os.xdm | Excel + log file |
| Skip OS tasks | Export all OS data except tasks | `os-xdm-xlsx --skip-os-task input.xdm output.xlsx` | Os.xdm | Excel without OsTask sheet |

## Excel Output Structure

The Excel workbook contains the following sheets:

1. **OsTask** - Task definitions with priorities, stacks, autostart, and resource references
2. **OsApplications** - Application definitions with trusted status and core assignment
3. **OsIsr** - ISR definitions with category, priority, vector, and memory regions
4. **OsScheduleTable** - Schedule table definitions with duration and counter references
5. **OsCounter** - Counter definitions with type and timing parameters
6. **OsScheduleTableExpiryPoint** - Expiry points with offsets and task activations
7. **MkMemoryRegion** - Memory protection regions with access permissions (if present)

Each sheet includes:
- Auto-width column sizing
- Centered alignment for numeric data
- Wrap text for multi-line content (e.g., resource lists, memory regions)

## Practical Examples

### Command Line Usage

```bash
# Basic OS configuration extraction
os-xdm-xlsx data/Os.xdm reports/Os.xlsx

# With verbose logging (creates os_xdm_2_xls.log in output directory)
os-xdm-xlsx -v data/Os.xdm reports/Os.xlsx

# Skip task sheet (export only ISRs, counters, schedule tables, applications)
os-xdm-xlsx --skip-os-task data/Os.xdm reports/Os.xlsx
```

### Programmatic Usage

```python
from eb_model.parser import OsXdmParser
from eb_model.models import EBModel
from eb_model.reporter import OsXdmXlsWriter

# Get singleton document model
doc = EBModel.getInstance()

# Parse OS XDM file
parser = OsXdmParser()
parser.parse_xdm("data/Os.xdm", doc)

# Access parsed data
os = doc.getOs()
print(f"Found {len(os.getOsTaskList())} tasks")
print(f"Found {len(os.getOsIsrList())} ISRs")
print(f"Found {len(os.getOsApplicationList())} applications")

# Export to Excel
writer = OsXdmXlsWriter()
writer.write("reports/Os.xlsx", doc)

# With options
writer.write("reports/Os.xlsx", doc, options={"skip_os_task": True})
```

### Querying OS Data

```python
# Get all tasks with their applications
for task in os.getOsTaskList():
    app = os.getOsTaskOsApplication(task.getName())
    print(f"Task: {task.getName()}, Priority: {task.getOsTaskPriority()}")
    if app:
        print(f"  Application: {app.getName()}, Core: {app.getOsApplicationCoreAssignment()}")

# Get all ISRs with memory regions
for isr in os.getOsIsrList():
    print(f"ISR: {isr.getName()}, Category: {isr.getOsIsrCategory()}")
    if isr.getOsIsrMkMemoryRegionRefs():
        for region_ref in isr.getOsIsrMkMemoryRegionRefs():
            print(f"  Memory Region: {region_ref.getShortName()}")

# Get schedule tables with expiry points
for table in os.getOsScheduleTableList():
    print(f"Schedule Table: {table.getName()}")
    print(f"  Duration: {table.getOsScheduleTableDuration()}")
    print(f"  Counter: {table.getOsScheduleTableCounterRef().getShortName()}")
    for expiry_point in table.getOsScheduleTableExpiryPointList():
        print(f"  Expiry Point: {expiry_point.getName()}, Offset: {expiry_point.getOsScheduleTblExpPointOffset()}")
```

## Limitations and Known Issues

1. **XDM Format Only**: Only supports EB Tresos XDM format, not generic AUTOSAR XML files

2. **ENABLE Attribute Handling**: Optional elements with `ENABLE="false"` are skipped during parsing. Ensure the XDM file has proper ENABLE attributes for optional configuration.

3. **Reference Validation**: ASPath references are extracted but not validated against actual targets. Invalid references in the XDM will be stored as-is without error.

4. **Vendor-Specific Attributes**:
   - TriCore-specific attributes (IrqLevel, Vector) are read independently
   - ARM-specific attributes (IrqLevel, Vector) are read independently
   - Which set is populated depends on the target hardware in the XDM

5. **Calculated References**: Some resource references use `@CALC(SvcAs,...)` syntax for EB-specific calculated service access. These are stored but not evaluated.

6. **Test Coverage**: Current tests focus on OS resources and OS tasks. Alarms, schedule tables, and microkernel features have limited test coverage.

7. **Memory Protection**: Memory protection configuration (MkMemoryRegion) is only parsed if present in the XDM. The Excel sheet is only created if memory regions exist.

8. **Thread Safety**: The parser is not thread-safe. Use separate parser instances for concurrent parsing operations.

## Dependencies

The OS module has no dependencies on other py-eb-model modules. It can be used standalone to parse OS configuration files.

However, OS applications may reference EcuC partitions via `OsAppEcucPartitionRef`. If you need to resolve these references to partition details, you'll also need to parse the EcuC.xdm file using the EcuC module.

## Related Documentation

- **[overview.md](overview.md)** - System architecture and common patterns
- **[ecuc-module.md](ecuc-module.md)** - ECU Configuration module (for partition references)
- **[CLAUDE.md](../../CLAUDE.md)** - Development guide for contributors
