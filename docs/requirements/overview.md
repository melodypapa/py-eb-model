# py-eb-model Requirements Overview

## Purpose

py-eb-model is a Python parser engine for EB Tresos XDM (XML Data Model) files. EB Tresos is an AUTOSAR configuration tool used in automotive software development, and XDM is its proprietary XML format for storing configuration data.

This library exists to:
- Extract AUTOSAR configuration data from EB Tresos XDM files
- Transform proprietary XML formats into structured Python objects
- Export configuration data to Excel for analysis, reporting, and documentation
- Generate AUTOSAR Builder project files from EB preference configurations

Without this tool, automotive engineers would need to manually navigate complex XML files or use the EB Tresos GUI to extract configuration information.

## System Architecture

py-eb-model is organized as a three-layer parsing system:

```
┌─────────────────────────────────────────────────────────────┐
│                     CLI Layer                                │
│  (os-xdm-xlsx, rte-xdm-xlsx, nvm-xdm-xlsx, etc.)            │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Reporter Layer                              │
│  (ExcelWriter, MarkdownWriter, ProjectWriter)               │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   Model Layer                                │
│  (EBModel, Module, OsTask, RteRunnableEntity, etc.)         │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Parser Layer                                │
│  (OsXdmParser, RteXdmParser, NvMXdmParser, etc.)            │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              EB Tresos XDM Files                             │
│  (Os.xdm, Rte.xdm, NvM.xdm, EcuC.xdm, BswM.xdm)             │
└─────────────────────────────────────────────────────────────┘
```

### Layer Responsibilities

**Parser Layer** (`src/eb_model/parser/`)
- Reads XML from EB Tresos XDM files
- Handles namespace-aware XML parsing (XDM uses extensive XML namespaces)
- XPath-based extraction of configuration elements
- Factory pattern automatically selects correct parser based on file content

**Model Layer** (`src/eb_model/models/`)
- Domain objects representing AUTOSAR configuration
- Hierarchical object structure (container → elements)
- Fluent interface for object configuration
- Reference path handling (ASPath format)

**Reporter Layer** (`src/eb_model/reporter/`)
- Exports model data to various formats
- Excel reporters with auto-width formatting
- Markdown generation for documentation
- Text output for file lists and project configurations

**CLI Layer** (`src/eb_model/cli/`)
- Command-line entry points for common operations
- Argument parsing and validation
- Logging configuration
- User-friendly error messages

## Supported Modules

| Module | Description | Requirements Document |
|--------|-------------|----------------------|
| **Os** | Operating System configuration (tasks, ISRs, schedule tables, counters, resources, applications, alarms) | [os-module.md](os-module.md) |
| **Rte** | Runtime Environment configuration (runnable entities, BSW module instances, event-to-task mappings) | [rte-module.md](rte-module.md) |
| **NvM** | Non-volatile Memory management (block descriptors, EA/FEE references) | [nvm-module.md](nvm-module.md) |
| **EcuC** | ECU Configuration (partitions, software component references) | [ecuc-module.md](ecuc-module.md) |
| **BswM** | Basic Software Mode management | [bswm-module.md](bswm-module.md) |

## Common Patterns

### Namespace Handling

EB Tresos XDM files use XML namespaces extensively. All parsers inherit this behavior from `AbstractEbModelParser`:

```python
# Namespaces extracted from XML and stored in dictionary
self.nsmap = dict([node for _, node in ET.iterparse(xdm, events=['start-ns'])])

# XPath queries use namespace prefix
element = parent.find(".//d:var[@name='ConfigValue']", self.nsmap)
```

### ASPath References

Configuration references use the ASPath format: `ASPath:/path/to/element`

```python
# Raw reference from XML
ref_value = "ASPath:/Os/OsTask/Task1"

# Extracted by parser
target = read_ref_raw_value(ref_value)  # Returns "/Os/OsTask/Task1"
```

### Factory Pattern

The parser factory automatically determines which parser to use based on the XDM file's MODULE-CONFIGURATION tag:

```python
parser = EbParserFactory.create("data/Os.xdm")  # Returns OsXdmParser
parser = EbParserFactory.create("data/Rte.xdm")  # Returns RteXdmParser
```

### Fluent Interface

Model objects support method chaining for convenient configuration:

```python
task.setName("Task1").setPriority(5).setStackSize(4096)
```

### ENABLE Attribute Handling

Optional elements in XDM files use an ENABLE attribute to indicate activation:

```python
# Returns value only if ENABLE is not FALSE
value = read_optional_value(parent, "OptionalConfig", default=None)
```

## Quick Start Example

Extract OS configuration to Excel:

```bash
# Install the package
pip install py_eb_model

# Run the OS extraction
os-xdm-xlsx data/Os.xdm reports/Os.xlsx

# Result: Multi-sheet Excel file with:
# - OsIsrs (interrupt service routines)
# - OsTasks (tasks with priorities, stacks, autostart)
# - OsScheduleTable (schedule tables and expiry points)
# - OsCounter (counter definitions)
# - OsApplication (application mappings)
# - OsAlarm (alarm configurations)
```

Programmatic usage:

```python
from eb_model.parser import OsXdmParser
from eb_model.models import EBModel
from eb_model.reporter import OsXdmXlsWriter

# Get singleton document model
doc = EBModel.getInstance()

# Parse XDM file
parser = OsXdmParser()
parser.parse_xdm("data/Os.xdm", doc)

# Export to Excel
writer = OsXdmXlsWriter()
writer.write(doc, "reports/Os.xlsx")
```

## CLI Tools Available

| Command | Purpose | Input | Output |
|---------|---------|-------|--------|
| `os-xdm-xlsx` | Extract OS configuration | Os.xdm | Excel (.xlsx) |
| `rte-xdm-xlsx` | Extract RTE configuration | Rte.xdm | Excel (.xlsx) |
| `nvm-xdm-xlsx` | Extract NvM configuration | NvM.xdm | Excel (.xlsx) |
| `ecuc-xdm-xlsx` | Extract EcuC configuration | EcuC.xdm | Excel (.xlsx) |
| `secoc-xdm-xlsx` | Extract SecOC configuration | SecOC.xdm | Excel (.xlsx) |
| `PrefSystemImporter` | Generate file list or project | preference XDM(s) | Text or .project file |

## Related Documentation

- **[CLAUDE.md](../../CLAUDE.md)** - Development guide for contributors (build, test, lint commands, code style)
- **[AGENTS.md](../../AGENTS.md)** - Detailed implementation patterns and architecture
- **[README.md](../../README.md)** - User-facing documentation with examples

## Module-Specific Requirements

For detailed requirements of each module, see the individual module requirement documents listed in the table above. Each document includes:
- Functional requirements (what the module shall do)
- Data models (key classes and their purposes)
- Supported operations (with CLI commands)
- Practical examples
- Limitations and known issues
