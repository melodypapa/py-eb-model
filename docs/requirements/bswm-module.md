# BswM Module Requirements

## Module Overview

The BswM (Basic Software Mode Manager) module is designed to extract AUTOSAR BswM configuration from EB Tresos BswM.xdm files. The BswM module is responsible for managing mode switches and coordinating mode changes across basic software modules in automotive embedded systems.

**⚠️ Current Implementation Status:**

The BswM module in py-eb-model is currently a **minimal/stub implementation**. The parser exists but does not extract any BswM-specific configuration data. The reporter exports OS configuration data rather than BswM configuration.

## Current Implementation

### Parser (`BswMXdmParser`)
- **Status**: Stub implementation
- Validates that the XDM file is a BswM configuration
- Does not parse any BswM-specific configuration elements
- No functional requirements implemented

### Model (`BswM`)
- **Status**: Minimal implementation
- Extends the base `Module` class
- Contains only a logger instance
- No BswM-specific attributes or methods

### Reporter (`BswMXdmXlsWriter`)
- **Status**: Incorrect implementation (exports OS data instead of BswM)
- Currently exports the same sheets as the OS module:
  - OsTask
  - OsIsr
  - OsScheduleTable
  - OsCounter
  - OsScheduleTableExpiryPoint
  - MkMemoryRegion
- This appears to be duplicate code from the OS reporter

## Intended Functional Requirements (Not Yet Implemented)

The BswM module should:

**Mode Management**
- Parse mode declaration groups
- Parse mode declaration instances
- Parse mode request sources and targets
- Parse mode switching conditions

**Mode Arbitration**
- Parse mode arbitration rules
- Parse mode dependencies
- Parse mode transition constraints

**Action Lists**
- Parse mode switch action lists
- Parse initialization action lists
- Parse mode indication callbacks

**BswM Configuration**
- Parse BswM module configuration
- Parse BswM general settings
- Extract version information (AR version, SW version)

## Data Model

### Current Model
**BswM** (Module)
- Container for BswM configuration
- Currently contains only a logger
- No BswM-specific child elements

### Intended Model (Not Implemented)
The following classes should be implemented:

**BswMModeDeclarationGroup**
- Represents a group of related modes
- Contains mode declarations

**BswMModeDeclarationInstance**
- Represents a specific mode instance
- References mode declaration group

**BswMModeRequestSource**
- Source of mode change requests (e.g., RTE, BSW module)

**BswMModeRequestPoint**
- Point where mode requests are processed

**BswMSwitchActionList**
- List of actions to execute on mode switch

**BswMConfiguration**
- General BswM configuration parameters

## Supported Operations

| Operation | Description | CLI Command | Input | Output |
|-----------|-------------|-------------|-------|--------|
| Export (current) | Exports OS configuration data (incorrect) | No CLI command exists | BswM.xdm | Excel with OS data |

**Note**: There is currently no CLI entry point for the BswM module in `setup.py`.

## Practical Examples

### Current Usage (Not Recommended)

```python
from eb_model.parser import BswMXdmParser
from eb_model.models import EBModel
from eb_model.reporter import BswMXdmXlsWriter

# Get singleton document model
doc = EBModel.getInstance()

# Parse BswM XDM file
parser = BswMXdmParser()
parser.parse_xdm("data/BswM.xdm", doc)

# The parser validates the file but doesn't extract any data
bswm = doc.getBswM()
# bswm has no BswM-specific data

# The reporter incorrectly exports OS data
writer = BswMXdmXlsWriter()
writer.write("reports/BswM.xlsx", doc, options={})
# This creates an Excel file with OS data, not BswM data
```

## Limitations and Known Issues

1. **No BswM Parsing**: The parser does not extract any BswM configuration from the XDM file

2. **Incorrect Reporter**: The reporter exports OS configuration data instead of BswM data. This appears to be copy-pasted from the OS reporter.

3. **No CLI Entry**: There is no `bswm-xdm-xlsx` command available. The module cannot be used from the command line.

4. **No Test Coverage**: No test files exist for the BswM module.

5. **No Documentation**: The BswM module is not documented in the README.md.

6. **Placeholder Status**: This module appears to be a placeholder for future implementation.

## Dependencies

The BswM module has no functional dependencies in its current state.

In a complete implementation, BswM would likely reference:
- **OS Module**: For mode-dependent task scheduling
- **RTE Module**: For mode requests from software components
- Other BSW modules that participate in mode management

## Recommendations

For the BswM module to be useful, the following implementation work is needed:

1. **Define the data model**: Create classes for BswM mode management concepts

2. **Implement the parser**: Extract BswM configuration from XDM files

3. **Implement the reporter**: Export BswM-specific configuration to Excel

4. **Add CLI entry point**: Register `bswm-xdm-xlsx` in `setup.py`

5. **Add tests**: Create test files to verify parsing and reporting

6. **Remove duplicate code**: The current reporter should be replaced with BswM-specific implementation

## Related Documentation

- **[overview.md](overview.md)** - System architecture and common patterns
- **[os-module.md](os-module.md)** - OS module (incorrectly exported by current BswM reporter)
- **[CLAUDE.md](../../CLAUDE.md)** - Development guide for contributors
