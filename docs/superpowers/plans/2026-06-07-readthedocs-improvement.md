# ReadTheDocs Documentation Improvement Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix and expand ReadTheDocs documentation for py-eb-model to serve AUTOSAR engineers

**Architecture:** Incremental phased approach - fix foundation first, then add user-facing content, then comprehensive reference

**Tech Stack:** Sphinx, sphinx_rtd_theme, myst_parser, sphinx.ext.autodoc

---

## File Structure Overview

**Files to create:**
```
docs/
├── requirements/index.rst                    # Phase 1
├── testing/index.rst                         # Phase 1
├── getting-started/
│   ├── index.rst                             # Phase 2
│   ├── installation.md                       # Phase 2
│   ├── first-xdm.md                          # Phase 2
│   ├── concepts.md                           # Phase 2
│   └── generator-quickstart.md               # Phase 3
├── usage/
│   └── model-xdm-generator.md                # Phase 3
├── examples/
│   ├── generator-basic.py                    # Phase 3
│   └── generator-advanced.py                 # Phase 3
└── api/
    └── generator.rst                          # Phase 3
```

**Files to modify:**
- `docs/index.rst` - Update version, fix toctree links

---

## Chunk 1: Phase 1 - Fix Foundation

### Task 1: Create Requirements Index

**Files:**
- Create: `docs/requirements/index.rst`

- [ ] **Step 1: Create requirements index file**

```bash
cat > docs/requirements/index.rst << 'EOF'
Software Requirements
=====================

This section contains the software requirements (SWR) for all supported AUTOSAR modules.

.. toctree::
   :maxdepth: 2

   infrastructure/swr_parser_factory
   infrastructure/swr_parser_methods
   infrastructure/swr_cli_layer
   infrastructure/swr_common_types
   infrastructure/swr_generator
   core/models/swr_os_models
   core/parser/swr_os_parser
   core/reporter/swr_os_reporter
   core/models/swr_ecuc_models
   core/models/swr_rte_models
   core/models/swr_bsw_models
   can_stack/parser/swr_can_parser
   can_stack/models/swr_can_models
   can_stack/reporter/swr_can_reporter
   eth_stack/parser/swr_eth_parser
   eth_stack/models/swr_eth_models
   eth_stack/reporter/swr_eth_reporter
   lin_stack/models/swr_lin_models
   fr_stack/models/swr_fr_models
   com_stack/models/swr_com_models
   mem_stack/models/swr_mem_models
   mem_stack/parser/swr_nvm_parser
   mem_stack/reporter/swr_nvm_reporter
   mem_stack/models/swr_nvm_models
   j1939_stack/models/swr_j1939_models
   crypto_stack/models/swr_crypto_models
   diag_stack/models/swr_diag_models
EOF
```

- [ ] **Step 2: Verify file created**

Run: `ls -la docs/requirements/index.rst`
Expected: File exists with content

- [ ] **Step 3: Commit**

```bash
git add docs/requirements/index.rst
git commit -m "docs: Add requirements index for navigation"
```

---

### Task 2: Create Testing Index

**Files:**
- Create: `docs/testing/index.rst`

- [ ] **Step 1: Create testing index file**

```bash
cat > docs/testing/index.rst << 'EOF'
Test Specifications
==================

This section contains test specifications for all modules.

Unit Tests
----------

.. toctree::
   :maxdepth: 1

   unit/uts_os_models_test-specs
   unit/uts_os_parser_test-specs
   unit/uts_os_reporter_test-specs
   unit/uts_bsw_models_test-specs
   unit/uts_ecuc_models_test-specs
   unit/uts_rte_models_test-specs
   unit/uts_can_stack_test-specs
   unit/uts_eth_stack_test-specs
   unit/uts_mem_stack_test-specs
   unit/uts_nvm_test-specs
   unit/uts_remaining_modules_test-specs
   unit/uts_generator

Integration Tests
-----------------

.. toctree::
   :maxdepth: 1

   integration/its_os_models_test-specs
   integration/its_os_parser_test-specs
   integration/its_os_reporter_test-specs
   integration/its_bsw_models_test-specs
   integration/its_ecuc_models_test-specs
   integration/its_rte_models_test-specs
   integration/its_can_stack_test-specs
   integration/its_eth_stack_test-specs
   integration/its_mem_stack_test-specs
   integration/its_nvm_test-specs
   integration/its_remaining_modules_test-specs
   integration/its_generator

System Tests
------------

.. toctree::
   :maxdepth: 1

   system/syts_os_models_test-specs
   system/syts_os_parser_test-specs
   system/syts_os_reporter_test-specs
   system/syts_bsw_models_test-specs
   system/syts_ecuc_models_test-specs
   system/syts_rte_models_test-specs
   system/syts_can_stack_test-specs
   system/syts_eth_stack_test-specs
   system/syts_mem_stack_test-specs
   system/syts_nvm_test-specs
   system/syts_remaining_modules_test-specs

Requirements Traceability
---------------------------

.. toctree::
   :maxdepth: 1

   requirements-traceability-matrix
EOF
```

- [ ] **Step 2: Verify file created**

Run: `ls -la docs/testing/index.rst`
Expected: File exists with content

- [ ] **Step 3: Commit**

```bash
git add docs/testing/index.rst
git commit -m "docs: Add testing index for navigation"
```

---

### Task 3: Update index.rst Version Information

**Files:**
- Modify: `docs/index.rst:8-10`

- [ ] **Step 1: Update version in index.rst**

Read the file first to see exact content:
```bash
cat docs/index.rst | head -15
```

Edit lines 8-10 to update version and Python requirement:

```bash
sed -i '' 's/\*\*Current Version\*\*: 1\.0\.0/**Current Version**: 1.3.1/' docs/index.rst
sed -i '' 's/\*\*Python Requirements\*\*: >= 3\.8/**Python Requirements**: >= 3.9/' docs/index.rst
```

- [ ] **Step 2: Verify changes**

Run: `head -15 docs/index.rst | grep -E "(Current Version|Python Requirements)"`
Expected:
```
**Current Version**: 1.3.1
**Python Requirements**: >= 3.9
```

- [ ] **Step 3: Test documentation build**

Run: `cd docs && make clean && make html`
Expected: Build completes without errors

- [ ] **Step 4: Commit**

```bash
git add docs/index.rst
git commit -m "docs: Update version to 1.3.1 and Python requirement to 3.9+"
```

---

### Task 4: Fix toctree Links in index.rst

**Files:**
- Modify: `docs/index.rst:127-140`

- [ ] **Step 1: Check current toctree structure**

Run: `grep -A 15 "Documentation Structure" docs/index.rst`

- [ ] **Step 2: Update toctree to include new indexes**

The toctree should reference the new index files. Verify the structure is correct:

```bash
grep -A 10 "toctree" docs/index.rst | grep -E "(requirements|testing)"
```

Expected output should show references to both indexes (they may already be there as `requirements/index` and `testing/index`)

- [ ] **Step 3: Build and test navigation**

Run: `cd docs && make html && open _build/html/index.html`

Expected: Page loads, links to Requirements and Testing sections work

- [ ] **Step 4: Commit**

```bash
git add docs/index.rst
git commit -m "docs: Verify and fix toctree links"
```

---

### Task 5: Verify All Navigation Links

**Files:**
- Test: Build output

- [ ] **Step 1: Full documentation build**

Run: `cd docs && make clean && make html 2>&1 | tee build.log`

- [ ] **Step 2: Check for broken links**

Run: `grep -i "warning\|error" docs/build.log || echo "No warnings or errors found"`

Expected: No broken link warnings

- [ ] **Step 3: Test key navigation paths**

Run: `ls docs/_build/html/requirements/index.html docs/_build/html/testing/index.html`

Expected: Both files exist

- [ ] **Step 4: Commit if any fixes needed**

```bash
# Only if changes were made
git add docs/
git commit -m "docs: Fix broken navigation links"
```

---

## Chunk 2: Phase 2 - Getting Started

### Task 6: Create Getting Started Index

**Files:**
- Create: `docs/getting-started/index.rst`

- [ ] **Step 1: Create getting-started index**

```bash
cat > docs/getting-started/index.rst << 'EOF'
Getting Started
===============

New to py-eb-model? Start here.

.. toctree::
   :maxdepth: 1

   installation
   first-xdm
   concepts
   generator-quickstart
EOF
```

- [ ] **Step 2: Verify file created**

Run: `cat docs/getting-started/index.rst`
Expected: File with toctree content

- [ ] **Step 3: Commit**

```bash
git add docs/getting-started/index.rst
git commit -m "docs: Add getting-started index"
```

---

### Task 7: Create Installation Guide

**Files:**
- Create: `docs/getting-started/installation.md`

- [ ] **Step 1: Create installation guide**

```bash
cat > docs/getting-started/installation.md << 'EOF'
# Installation

## Requirements

- Python 3.9 or higher
- pip package manager

## Install from PyPI

```bash
pip install eb-model
```

## Development Install

For contributing or running from source:

```bash
git clone https://github.com/melodypapa/py-eb-model.git
cd py-eb-model
pip install -e .
```

## Verify Installation

Test the installation:

```bash
# Test unified CLI
eb-convert --help

# Test specific module CLI
os-xdm-xlsx --help

# Test generator
model-xdm-generator --help
```

## Dependencies

Runtime dependencies are installed automatically:
- openpyxl - Excel file support

Development dependencies (for testing):
- pytest
- ruff
- mypy

## Troubleshooting

### Python version error

If you see "Python version too old", ensure you're using Python 3.9+:

```bash
python --version
```

### Command not found

If `eb-convert` is not found, try:

```bash
python -m eb_model.cli.eb_convert --help
```

Or reinstall:

```bash
pip install --force-reinstall eb-model
```
EOF
```

- [ ] **Step 2: Build and verify**

Run: `cd docs && make html`
Expected: Build succeeds, installation.html created

- [ ] **Step 3: View output**

Run: `open docs/_build/html/getting-started/installation.html`
Expected: Page renders correctly with Markdown

- [ ] **Step 4: Commit**

```bash
git add docs/getting-started/installation.md
git commit -m "docs: Add installation guide"
```

---

### Task 8: Create First XDM Guide

**Files:**
- Create: `docs/getting-started/first-xdm.md`

- [ ] **Step 1: Create first conversion guide**

```bash
cat > docs/getting-started/first-xdm.md << 'EOF'
# Your First XDM Conversion

This guide walks through converting your first EB Tresos XDM file to Excel.

## Prerequisites

1. Have an EB Tresos XDM file (e.g., `Os.xdm`)
2. eb-model installed (see [Installation](installation.md))

## Step 1: Locate Your XDM File

EB Tresos exports XDM files from your project. Find them in your project's configuration directory.

Common locations:
- `MyProject/Config/Os.xdm`
- `MyProject/Generated/Os.xdm`

## Step 2: Run the Conversion

Use the unified `eb-convert` command:

```bash
eb-convert Os.xdm output/
```

This creates `output/Os.xlsx` with all OS configuration data.

## Step 3: Understand the Output

Open `Os.xlsx`. You'll see:

- **General**: OS version, API settings, hooks
- **Tasks**: All task configurations (priority, stack, autostart)
- **ISRs**: ISR configurations
- **Resources**: Resource management
- **Counters**: OS counters
- **Alarms**: Alarm configurations
- **Events**: OS events

Each sheet contains:
- **Name**: Element name from XDM
- **Value**: Configuration value
- **Attribute**: Additional metadata (ENABLE, IMPORTER_INFO)

## Step 4: Verify Key Data

Check that critical data is present:

1. Task priorities are correct
2. ISR names match your ISRs
3. Resource references are resolved

## Common Issues

### Empty Output

**Cause**: ENABLE attribute filtering

Some XDM elements have `ENABLE="false"`. These are skipped by default.

**Solution**: Check if expected elements have `ENABLE="true"` in the XDM.

### Namespace Errors

**Cause**: Invalid XDM format

**Solution**: Ensure the XDM file was exported by EB Tresos, not hand-edited.

### Missing Values

**Cause**: Calculated values using `@CALC()` syntax

**Solution**: These are shown as-is. The actual value depends on your EB Tresos project configuration.

## Next Steps

- Explore other modules: `eb-convert NvM.xdm output/`
- Learn [concepts](concepts.md)
- Try the [model-xdm-generator](generator-quickstart.md)
EOF
```

- [ ] **Step 2: Build and verify**

Run: `cd docs && make html`
Expected: Build succeeds

- [ ] **Step 3: Commit**

```bash
git add docs/getting-started/first-xdm.md
git commit -m "docs: Add first XDM conversion guide"
```

---

### Task 9: Create Concepts Guide

**Files:**
- Create: `docs/getting-started/concepts.md`

- [ ] **Step 1: Create concepts guide**

```bash
cat > docs/getting-started/concepts.md << 'EOF'
# Core Concepts

## What is EB Tresos XDM?

EB Tresos (Elektrobit Tresos) is an AUTOSAR configuration tool. It exports configuration in XDM (XML Data Model) format - a proprietary XML schema representing AUTOSAR module configurations.

**Example XDM structure:**
```xml
<MODULE-CONFIGURATION>
  <d:ctr name="OsGeneral">
    <d:var name="OsStatus" type="BOOLEAN" value="true"/>
  </d:ctr>
  <d:lst name="OsTask">
    <d:ctr name="Task1">
      <d:var name="Priority" type="INTEGER" value="5"/>
    </d:ctr>
  </d:lst>
</MODULE-CONFIGURATION>
```

## Architecture Overview

py-eb-model has three layers:

### 1. Parser Layer (`src/eb_model/parser/`)

**Purpose**: Convert XDM XML to Python objects

**Key components:**
- `AbstractEbModelParser`: Base parser with common XML parsing methods
- `OsXdmParser`, `CanIfXdmParser`, etc.: Module-specific parsers
- `EbParserFactory`: Auto-detects module type from XDM

**How it works:**
1. Read XDM file with ElementTree
2. Extract namespace information
3. Parse MODULE-CONFIGURATION tag
4. Walk XML tree, extract values
5. Create model objects

### 2. Model Layer (`src/eb_model/models/`)

**Purpose**: Represent AUTOSAR domain as Python objects

**Key components:**
- `EcucObject`: Base class for all configuration objects
- `Module`: Root container (e.g., `Os`, `CanIf`)
- `OsTask`, `CanIfRxPduCfg`, etc.: Specific configuration objects

**Features:**
- Hierarchical naming (e.g., `Os/Task1`)
- Fluent interface for chaining
- Type-safe accessors

### 3. Reporter Layer (`src/eb_model/reporter/`)

**Purpose**: Export model objects to various formats

**Key components:**
- `AbstractEbModelXlsWriter`: Base Excel writer
- `OsXdmXlsWriter`, `CanIfXdmXlsWriter`, etc.: Module-specific writers
- `ExcelReporter`: Utility class for formatting

**How it works:**
1. Receive model object
2. Create Excel workbook
3. Write sheets for each configuration container
4. Save to file

## Module Mapping

py-eb-model supports 50+ AUTOSAR modules organized by stack:

| Stack | Modules |
|-------|---------|
| **Core** | Os, EcuC, RTE, BswM, Det, EcuM, PbcfgM, Tm |
| **CAN** | CanIf, CanNm, CanSM, CanTp |
| **Ethernet** | EthIf, EthSM, SoAd, TcpIp, SomeIpTp, UdpNm, DoIP |
| **LIN** | LinIf, LinSM, LinTp |
| **FlexRay** | FrIf, FrNm, FrSM, FrTp, FrArTp |
| **COM** | Com, LdCom, ComM, PduR, IpduM, Nm |
| **Memory** | NvM, Fee, Ea, MemIf, MemAcc, MemMap, Crc |
| **Crypto** | Crypto, CryIf, Csm, SecOC |
| **Diagnostic** | Dcm, Dem, DLT, FiM |
| **J1939** | J1939Dcm, J1939Nm, J1939Rm, J1939Tp |

## CLI vs Python API

### CLI (Recommended for most users)

```bash
eb-convert Os.xdm output/
```

**When to use:**
- Converting files
- Batch processing
- Quick data extraction
- No custom logic needed

### Python API

```python
from eb_model.parser import OsXdmParser
from eb_model.reporter import OsXdmXlsWriter

parser = OsXdmParser()
os_model = parser.parse("Os.xdm")
writer = OsXdmXlsWriter()
writer.write(os_model, "Os.xlsx")
```

**When to use:**
- Custom data processing
- Integrating into tools
- Validation scripts
- Generating multiple outputs

## Next Steps

- Try [converting your first XDM](first-xdm.md)
- Learn about the [generator](generator-quickstart.md)
- See [CLI usage](../usage/cli.md)
EOF
```

- [ ] **Step 2: Build and verify**

Run: `cd docs && make html`
Expected: Build succeeds

- [ ] **Step 3: Commit**

```bash
git add docs/getting-started/concepts.md
git commit -m "docs: Add concepts guide"
```

---

### Task 10: Update Main Index to Include Getting Started

**Files:**
- Modify: `docs/index.rst:94-133`

- [ ] **Step 1: Add getting-started to toctree**

Read the current Documentation Structure section:

```bash
grep -A 20 "Documentation Structure" docs/index.rst
```

Add getting-started to the User Guide toctree:

```bash
# Update the toctree in Documentation Structure section
# Add "getting-started/index" after the caption line
```

Edit the file to include:

```rst
.. toctree::
   :maxdepth: 2
   :caption: User Guide

   getting-started/index
   usage/cli
   requirements/index
   testing/index
```

- [ ] **Step 2: Build and test**

Run: `cd docs && make html && open _build/html/index.html`

Expected: Getting Started appears in User Guide section

- [ ] **Step 3: Commit**

```bash
git add docs/index.rst
git commit -m "docs: Add getting-started to main index"
```

---

## Chunk 3: Phase 3 - Generator Documentation

### Task 11: Create Generator Quick Start

**Files:**
- Create: `docs/getting-started/generator-quickstart.md`

- [ ] **Step 1: Create quick start guide**

```bash
cat > docs/getting-started/generator-quickstart.md << 'EOF'
# Model XDM Generator - Quick Start

The **model-xdm-generator** creates test model XDM files from schema XDM files. Perfect for testing, validation, and development.

## What is it?

EB Tresos has two file types:
- **Schema XDM**: Defines the structure (templates, types)
- **Model XDM**: Actual configuration data (instances)

The generator creates model instances from schemas, filling in realistic test values.

## Install

Already included with eb-model:

```bash
model-xdm-generator --help
```

## Generate Your First Model

### Basic OS Model

```bash
model-xdm-generator path/to/Os.xdm -o Os_model.xdm
```

This creates a complete OS configuration with:
- Multiple tasks
- ISRs
- Resources
- Counters
- Alarms

### Generate with Specific Variant

```bash
# Use only default values
model-xdm-generator Os.xdm -o Os_defaults.xdm --variant defaults

# Use boundary values (min/max)
model-xdm-generator Os.xdm -o Os_boundary.xdm --variant boundary

# Use random values
model-xdm-generator Os.xdm -o Os_random.xdm --variant random --seed 42
```

### Generate with Custom List Sizes

```bash
# Generate exactly 3 tasks
model-xdm-generator Os.xdm -o Os_3tasks.xdm --list-entries 3
```

## Use the Generated Model

Now convert it to Excel to see the values:

```bash
eb-convert Os_model.xdm output/
open output/Os.xlsx
```

## Common Use Cases

### 1. Test Your Conversion Pipeline

```bash
# Generate test data
model-xdm-generator CanIf.xdm -o CanIf_test.xdm

# Convert and verify
eb-convert CanIf_test.xdm test_output/

# Use in tests
pytest tests/integration/test_canif_parsing.py
```

### 2. Verify Schema Changes

```bash
# After schema changes, regenerate
model-xdm-generator MyModule.xdm -o MyModule_test.xdm

# Check for parsing issues
eb-convert MyModule_test.xdm output/
```

### 3. Create Demo Data

```bash
# Generate for presentation
model-xdm-generator Os.xdm -o Os_demo.xdm --variant combined
eb-convert Os_demo.xdm demo/
```

## Next Steps

- Full [User Manual](../usage/model-xdm-generator.md)
- [CLI Reference](../usage/cli.md#model-xdm-generator)
- [Examples](../examples/)
EOF
```

- [ ] **Step 2: Build and verify**

Run: `cd docs && make html`
Expected: Build succeeds

- [ ] **Step 3: Commit**

```bash
git add docs/getting-started/generator-quickstart.md
git commit -m "docs: Add generator quick start guide"
```

---

### Task 12: Create Generator User Manual

**Files:**
- Create: `docs/usage/model-xdm-generator.md`

- [ ] **Step 1: Create comprehensive user manual**

```bash
cat > docs/usage/model-xdm-generator.md << 'EOF'
# Model XDM Generator - User Manual

## Introduction

The model-xdm-generator creates model (instance) XDM files from schema XDM files for testing and validation purposes.

### Purpose

- **Testing**: Generate test data without needing real AUTOSAR configurations
- **Validation**: Verify parsers and reporters handle all XDM elements
- **Development**: Test code changes without waiting for real XDM files
- **Documentation**: Create example configurations

### When to Use vs Real XDM Files

| Use Case | Recommended Approach |
|----------|---------------------|
| Unit testing | Generator (faster, controlled) |
| Integration testing | Real XDM files (realistic) |
| CI/CD | Generator (deterministic with seeds) |
| Documentation | Generator (clean examples) |
| Production validation | Real XDM files |

## CLI Reference

```bash
model-xdm-generator <schema.xdm> -o <output.xdm> [options]
```

### Options

| Option | Description | Default |
|--------|-------------|----------|
| `-o, --output OUTPUT` | Output path (required) | - |
| `--variant {combined,defaults,boundary,random}` | Value generation strategy | combined |
| `--seed SEED` | Random seed (for reproducibility) | None |
| `--list-entries LIST_ENTRIES` | Number of entries per list | Auto (from schema MIN) |

### Examples

#### Basic generation

```bash
model-xdm-generator Os.xdm -o Os_model.xdm
```

#### Reproducible random generation

```bash
# Same seed = same output
model-xdm-generator CanIf.xdm -o CanIf_test.xdm --variant random --seed 12345
```

#### Custom list size

```bash
# Generate exactly 5 controllers
model-xdm-generator EthIf.xdm -o EthIf_test.xdm --list-entries 5
```

## Generation Strategies

### Combined (Default)

Cycles through defaults, boundary values, and random values. Best for comprehensive testing.

**Characteristics:**
- First entry: defaults
- Second entry: boundary (min/max)
- Third+ entries: random
- Includes ENABLE attributes on all optional items
- Covers all choice options

**Example output:**
```xml
<d:lst name="OsTask">
  <d:ctr name="Task1"> <!-- defaults -->
    <d:var name="Priority" value="1"/>
    <d:var name="Autostart" value="true"/>
  </d:ctr>
  <d:ctr name="Task2"> <!-- boundary -->
    <d:var name="Priority" value="255"/> <!-- max -->
    <d:var name="Autostart" value="false"/>
  </d:ctr>
  <d:ctr name="Task3_Random"> <!-- random -->
    <d:var name="Priority" value="42"/> <!-- random -->
    <d:var name="Autostart" value="true"/>
  </d:ctr>
</d:lst>
```

**When to use:**
- General testing
- Coverage verification
- Documentation examples

### Defaults

Uses DEFAULT values from schema, or type-specific defaults.

**Type defaults:**
- INTEGER: 1
- BOOLEAN: true
- STRING: "default"
- ENUMERATION: first option

**When to use:**
- Simple smoke tests
- Basic functionality verification

### Boundary

Uses boundary values for comprehensive edge case testing.

**Boundary rules:**
- INTEGER: min, max, min+1, max-1
- BOOLEAN: true, false
- ENUMERATION: first, last

**When to use:**
- Edge case testing
- Boundary condition verification
- Range validation testing

### Random

Uses random values within RANGE constraints.

**Characteristics:**
- Unpredictable values
- Requires seed for reproducibility
- Good for finding unexpected issues

**When to use:**
- Fuzz testing
- Finding edge cases
- Reproducible tests (with seed)

## Schema Guide

### XDM Schema Structure

A schema XDM defines:

1. **Containers** (`<d:ctr>`): Group related elements
2. **Variables** (`<d:var>`): Typed values
3. **Lists** (`<d:lst>`): Collections with multiplicity
4. **References** (`<d:ref>`): Links to other elements
5. **Choices** (`<d:choice>`): Optional selections

### Creating Custom Schemas

To create a schema for generation:

1. **Define the module structure**

```xml
<MODULE-CONFIGURATION>
  <d:ctr name="MyModuleGeneral">
    <d:var name="Version" type="INTEGER" default="1"/>
    <d:var name="Enabled" type="BOOLEAN" default="true"/>
  </d:ctr>
  <d:lst name="MyConfig" min="0" max="10">
    <d:ctr name="MyConfigItem">
      <d:var name="Id" type="INTEGER"/>
      <d:var name="Name" type="STRING"/>
    </d:ctr>
  </d:lst>
</MODULE-CONFIGURATION>
```

2. **Specify types and constraints**

- `type`: INTEGER, BOOLEAN, STRING, ENUMERATION
- `default`: Value for defaults variant
- `min`/`max`: Range for boundary and random variants
- `ENABLE="true"`: Mark optional items

### Common Schema Patterns

#### Optional Container

```xml
<d:ctr name="OptionalFeature" ENABLE="true">
  <d:var name="Setting" type="INTEGER"/>
</d:ctr>
```

#### Enumerations

```xml
<d:var name="Mode" type="ENUMERATION">
  <d:enumeration name="MODE_A"/>
  <d:enumeration name="MODE_B"/>
  <d:enumeration name="MODE_C"/>
</d:var>
```

#### References

```xml
<d:ref name="TargetRef" type="ASPath"/>
```

Generator creates mock references like `ASPath:/MockTarget`.

## Troubleshooting

### "No MODULE-CONFIGURATION found"

**Cause**: File is not a valid schema XDM

**Solution**: Ensure the XDM has `<MODULE-CONFIGURATION>` as root.

### Empty lists in output

**Cause**: Schema has `min="0"` and generator respects minimum

**Solution**: Use `--list-entries` to override.

### Non-reproducible output

**Cause**: Using random variant without seed

**Solution**: Add `--seed` for reproducible output

### Parser errors on generated file

**Cause**: Schema has structural issues

**Solution**:
1. Validate schema against XDM specification
2. Check for missing required attributes
3. Verify namespace declarations

## Examples

See [examples/](../examples/) for complete working examples.
EOF
```

- [ ] **Step 2: Build and verify**

Run: `cd docs && make html`
Expected: Build succeeds

- [ ] **Step 3: Commit**

```bash
git add docs/usage/model-xdm-generator.md
git commit -m "docs: Add generator user manual"
```

---

### Task 13: Create Generator Basic Example

**Files:**
- Create: `docs/examples/generator-basic.py`
- Create: `docs/examples/README.md`

- [ ] **Step 1: Create examples directory and README**

```bash
mkdir -p docs/examples
cat > docs/examples/README.md << 'EOF'
# Examples

This directory contains code examples for using py-eb-model.

## Generator Examples

- [generator-basic.py](generator-basic.py): Simple OS model generation
- [generator-advanced.py](generator-advanced.py): Advanced generation with custom strategies

## Usage

```bash
python docs/examples/generator-basic.py
```
EOF
```

- [ ] **Step 2: Create basic example**

```bash
cat > docs/examples/generator-basic.py << 'EOF'
"""
Basic Model XDM Generator Example

This example demonstrates simple OS model generation.
"""

import subprocess
import sys
import os
from pathlib import Path

def generate_os_model():
    """Generate a basic OS model XDM file."""

    # Path to schema (adjust for your setup)
    schema_path = "doc/os/schema/Os.xdm"

    # Output path
    output_path = "Os_generated.xdm"

    # Check if schema exists
    if not os.path.exists(schema_path):
        print(f"Schema not found: {schema_path}")
        print("This example requires an OS schema XDM file.")
        print("Adjust schema_path in the script to point to your schema.")
        return False

    # Run generator
    print(f"Generating OS model from {schema_path}...")

    result = subprocess.run(
        [
            "model-xdm-generator",
            schema_path,
            "-o", output_path,
            "--variant", "combined",
            "--seed", "42"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False

    print(f"Generated: {output_path}")
    print(f"\nFile size: {os.path.getsize(output_path)} bytes")

    # Show first few lines
    print("\nFirst 20 lines of generated file:")
    with open(output_path, 'r') as f:
        for i, line in enumerate(f):
            if i >= 20:
                break
            print(line.rstrip())

    return True

if __name__ == "__main__":
    success = generate_os_model()
    sys.exit(0 if success else 1)
EOF
```

- [ ] **Step 3: Verify and build**

Run: `cd docs && make html`
Expected: Build succeeds, examples/README.html created

- [ ] **Step 4: Commit**

```bash
git add docs/examples/
git commit -m "docs: Add generator basic example and examples README"
```

---

### Task 14: Create Generator Advanced Example

**Files:**
- Create: `docs/examples/generator-advanced.py`

- [ ] **Step 1: Create advanced example**

```bash
cat > docs/examples/generator-advanced.py << 'EOF'
"""
Advanced Model XDM Generator Example

This example demonstrates advanced generation strategies:
- Different variants for different purposes
- Custom list sizes
- Batch generation
"""

import subprocess
import sys
import os
from pathlib import Path

def generate_with_variant(variant: str, suffix: str):
    """Generate model with specific variant."""

    schema_path = "doc/os/schema/Os.xdm"
    output_path = f"Os_{suffix}.xdm"

    if not os.path.exists(schema_path):
        print(f"Schema not found: {schema_path}")
        return None

    print(f"Generating {suffix}...")

    result = subprocess.run(
        [
            "model-xdm-generator",
            schema_path,
            "-o", output_path,
            "--variant", variant,
            "--seed", "42"  # Same seed for fair comparison
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None

    return output_path

def generate_with_custom_list_size(count: int):
    """Generate model with custom list size."""

    schema_path = "doc/os/schema/Os.xdm"
    output_path = f"Os_{count}tasks.xdm"

    if not os.path.exists(schema_path):
        print(f"Schema not found: {schema_path}")
        return None

    print(f"Generating with {count} list entries...")

    result = subprocess.run(
        [
            "model-xdm-generator",
            schema_path,
            "-o", output_path,
            "--list-entries", str(count),
            "--seed", "42"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None

    return output_path

def compare_outputs(files: list):
    """Compare generated files."""

    print("\nComparison:")
    print(f"{'File':<30} {'Size':>10}")
    print("-" * 42)

    for file in files:
        if file and os.path.exists(file):
            size = os.path.getsize(file)
            print(f"{os.path.basename(file):<30} {size:>10} bytes")

def main():
    """Run advanced generation examples."""

    print("=== Advanced Model XDM Generator Examples ===\n")

    generated_files = []

    # 1. Generate with different variants
    variants = [
        ("defaults", "defaults"),
        ("boundary", "boundary"),
        ("random", "random"),
        ("combined", "combined"),
    ]

    print("1. Generating with different variants:")
    print("-" * 40)

    for variant, suffix in variants:
        output = generate_with_variant(variant, suffix)
        if output:
            generated_files.append(output)

    # 2. Generate with custom list sizes
    print("\n2. Generating with custom list sizes:")
    print("-" * 40)

    for count in [1, 3, 5]:
        output = generate_with_custom_list_size(count)
        if output:
            generated_files.append(output)

    # 3. Compare results
    if generated_files:
        compare_outputs(generated_files)

        print("\n✓ Generation complete!")
        print("\nYou can now convert these files:")
        print("  eb-convert Os_*.xdm output/")
    else:
        print("\n✗ No files generated (schema not found)")
        print("Adjust schema_path in the script to point to your schema.")
        return False

    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
EOF
```

- [ ] **Step 2: Build and verify**

Run: `cd docs && make html`
Expected: Build succeeds

- [ ] **Step 3: Commit**

```bash
git add docs/examples/generator-advanced.py
git commit -m "docs: Add generator advanced example"
```

---

### Task 15: Create Generator API Reference

**Files:**
- Create: `docs/api/generator.rst`

- [ ] **Step 1: Create API reference for generator**

```bash
cat > docs/api/generator.rst << 'EOF'
Generator API Reference
======================

This section documents the model-xdm-generator API.

.. toctree::
   :maxdepth: 4

   eb_model.generator.data_generator
   eb_model.generator.schema_parser
   eb_model.generator.strategies

Module Reference
----------------

Data Generator
~~~~~~~~~~~~~~~

.. automodule:: eb_model.generator.data_generator
   :members:
   :undoc-members:
   :show-inheritance:

Schema Parser
~~~~~~~~~~~~~~

.. automodule:: eb_model.generator.schema_parser
   :members:
   :undoc-members:
   :show-inheritance:

Strategies
~~~~~~~~~~

.. automodule:: eb_model.generator.strategies
   :members:
   :undoc-members:
   :show-inheritance:
EOF
```

- [ ] **Step 2: Update api/modules.rst to include generator**

Check if `api/modules.rst` exists and add generator:

```bash
# Add generator to the modules list
grep -q "generator" docs/api/modules.rst || echo "
Generator
---------

.. toctree::
   :maxdepth: 1

   generator
" >> docs/api/modules.rst
```

- [ ] **Step 3: Build and verify**

Run: `cd docs && make html`
Expected: Build succeeds, API docs generated for generator module

- [ ] **Step 4: Commit**

```bash
git add docs/api/generator.rst docs/api/modules.rst
git commit -m "docs: Add generator API reference"
```

---

## Chunk 4: Phase 4 Starter - Additional Usage Documentation

**Note:** Phase 4 in the spec is "Complete Reference (Ongoing)" for comprehensive API documentation covering parser, models, and reporters layers. This chunk provides starter usage documentation. Full API reference (parser.rst, models.rst, reporters.rst) is future work to be done incrementally by stack priority (core → CAN → ETH → LIN → FR → MEM → DIAG).

### Task 16: Create Python API Guide

**Files:**
- Create: `docs/usage/python-api.md`

- [ ] **Step 1: Create Python API usage guide**

```bash
cat > docs/usage/python-api.md << 'EOF'
# Python API Usage

While the CLI covers most use cases, the Python API enables custom processing and integration.

## Basic Pattern

All modules follow the same pattern:

```python
from eb_model.parser import ModuleXdmParser
from eb_model.reporter import ModuleXdmXlsWriter

# Parse
parser = ModuleXdmParser()
model = parser.parse("input.xdm")

# Report
writer = ModuleXdmXlsWriter()
writer.write(model, "output.xlsx")
```

## Common Patterns

### Batch Processing

```python
from pathlib import Path
from eb_model.parser import EbParserFactory
from eb_model.reporter import parser_writer_registry

xdm_dir = Path("xdm_files")
output_dir = Path("output")

for xdm_file in xdm_dir.glob("*.xdm"):
    # Auto-detect parser type
    parser = EbParserFactory.create(xdm_file)
    model = parser.parse(xdm_file)

    # Auto-detect writer type
    writer_class = parser_writer_registry.get(parser.__class__)
    writer = writer_class()
    writer.write(model, output_dir / f"{model.name}.xlsx")

    print(f"Converted {xdm_file.name}")
```

### Data Validation

```python
from eb_model.parser import OsXdmParser

parser = OsXdmParser()
os = parser.parse("Os.xdm")

# Validate task priorities
for task in os.getOsTaskList():
    priority = task.getOsTaskPriority()
    if priority < 1 or priority > 255:
        print(f"Invalid priority for {task.getName()}: {priority}")

# Verify all tasks have stacks
for task in os.getOsTaskList():
    if not task.getOsTaskStackName():
        print(f"Task {task.getName()} has no stack")
```

### Custom Excel Output

```python
from eb_model.parser import CanIfXdmParser
from eb_model.reporter.excel_reporter.can_stack.canif_xdm import CanIfXdmXlsWriter
from openpyxl import Workbook

parser = CanIfXdmParser()
canif = parser.parse("CanIf.xdm")

# Use standard writer
writer = CanIfXdmXlsWriter()
writer.write(canif, "CanIf.xlsx")

# Or create custom output
wb = Workbook()
ws = wb.active
ws.title = "Custom Report"

# Write custom data
ws.append(["Controller", "Baudrate"])
for ctrl in canif.getCanIfCtrlCfgList():
    ws.append([ctrl.getName(), ctrl.getCanIfControllerBaudrate()])

wb.save("CanIf_custom.xlsx")
```

### Combining Multiple Modules

```python
from eb_model.parser import OsXdmParser, RteXdmParser, CanIfXdmParser

# Parse multiple modules
os_parser = OsXdmParser()
rte_parser = RteXdmParser()
canif_parser = CanIfXdmParser()

os = os_parser.parse("Os.xdm")
rte = rte_parser.parse("Rte.xdm")
canif = canif_parser.parse("CanIf.xdm")

# Cross-reference: Find ISRs referenced by RTE
for isr in os.getOsIsrList():
    isr_name = isr.getName()
    # Check if RTE uses this ISR
    for mapping in rte.getRteBswEventToIsrMappingList():
        if isr_name in mapping.getRteBswIsrRef():
            print(f"ISR {isr_name} used by RTE")
```

## Error Handling

```python
from eb_model.parser import OsXdmParser
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

parser = OsXdmParser()

try:
    os = parser.parse("Os.xdm")
except FileNotFoundError:
    print("XDM file not found")
except Exception as e:
    print(f"Error parsing XDM: {e}")
```

## Working with Models

### Navigating the Model

```python
from eb_model.parser import OsXdmParser

parser = OsXdmParser()
os = parser.parse("Os.xdm")

# Access general configuration
general = os.getOsGeneral()
print(f"OS Status: {general.getOsStatus()}")

# Access lists
tasks = os.getOsTaskList()
for task in tasks:
    print(f"Task: {task.getName()}, Priority: {task.getOsTaskPriority()}")

# Nested access
for task in tasks:
    resources = task.getOsTaskResourceList()
    for res in resources:
        print(f"  Resource: {res.getName()}")
```

### Fluent Interface

```python
# Most setters return self for chaining
task = OsTask(parent, "MyTask")
task.setOsTaskPriority(5).setOsTaskAutostart(True).setOsTaskStackName("Stack1")
```

## Next Steps

- See [CLI Usage](cli.md) for command-line interface
- See [API Reference](../api/modules.html) for complete API docs
- See [Examples](../examples/) for code examples
EOF
```

- [ ] **Step 2: Build and verify**

Run: `cd docs && make html`
Expected: Build succeeds

- [ ] **Step 3: Commit**

```bash
git add docs/usage/python-api.md
git commit -m "docs: Add Python API usage guide"
```

---

### Task 17: Create CLI Examples Guide

**Files:**
- Create: `docs/examples/cli-usage.md`

- [ ] **Step 1: Create CLI examples guide**

```bash
cat > docs/examples/cli-usage.md << 'EOF'
# CLI Usage Examples

## Basic Conversion

### Single File

```bash
eb-convert Os.xdm output/
# Creates: output/Os.xlsx
```

### Multiple Files

```bash
eb-convert Os.xdm NvM.xdm Rte.xdm output/
# Creates: output/Os.xlsx, output/NvM.xlsx, output/Rte.xlsx
```

## Advanced Options

### Verbose Logging

```bash
eb-convert --verbose Os.xdm output/
```

### File Logging

```bash
eb-convert --log conversion.log Os.xdm output/
```

### Module-Specific Options

```bash
# Skip OS task generation
eb-convert --skip-os-task Os.xdm output/
```

## Module-Specific Commands

### OS Module

```bash
os-xdm-xlsx -i Os.xdm -o Os.xlsx
```

### CAN Interface

```bash
canif-xdm-xlsx -i CanIf.xdm -o CanIf.xlsx
```

### NVM Manager

```bash
nvm-xdm-xlsx -i NvM.xdm -o NvM.xlsx
```

## Generator

### Basic Generation

```bash
model-xdm-generator Os.xdm -o Os_model.xdm
```

### With Variant

```bash
model-xdm-generator Os.xdm -o Os_model.xdm --variant boundary
```

### Reproducible Random

```bash
model-xdm-generator Os.xdm -o Os_test.xdm --variant random --seed 42
```

## Batch Processing

### Process Directory

```bash
# Convert all XDM files in a directory
for file in *.xdm; do
    eb-convert "$file" output/
done
```

### With Pattern Matching

```bash
# Convert only OS files
eb-convert Os*.xdm output/
```

## Integration Examples

### With Git

```bash
# Convert XDM files from repository
git archive HEAD | tar xO '*.xdm' | while read file; do
    eb-convert "$file" docs/
done
```

### With Find

```bash
# Convert all XDM files in subdirectories
find . -name "*.xdm" -exec eb-convert {} output/ \;
```

## Troubleshooting

### Check Module Type

```bash
# See what module type is detected
model-xdm-generator --help
```

### Verify Output

```bash
# Check if Excel file was created
ls -la output/*.xlsx
```
EOF
```

- [ ] **Step 2: Build and verify**

Run: `cd docs && make html`
Expected: Build succeeds

- [ ] **Step 3: Commit**

```bash
git add docs/examples/cli-usage.md
git commit -m "docs: Add CLI usage examples"
```

---

### Task 18: Update Main Index with New Content

**Files:**
- Modify: `docs/index.rst:94-150` (Documentation Structure section)

- [ ] **Step 1: Add examples section to main index**

First, read the current Documentation Structure section to understand exact formatting:

```bash
grep -A 60 "Documentation Structure" docs/index.rst
```

Add the Examples toctree after API Reference section. The exact addition:

```bash
# Insert this after the API Reference toctree (around line 140):

.. toctree::
   :maxdepth: 2
   :caption: Examples

   examples/cli-usage
   examples/README
```

To apply, edit docs/index.rst manually or use:

```bash
# Find the line with ".. toctree::" under "API Reference" 
# Add the Examples section after it
```

- [ ] **Step 2: Verify getting-started includes python-api in usage**

The getting-started/index.rst already includes generator-quickstart from Task 11 (not Task 6 - that was index.rst).

Check that usage/python-api will be accessible. The main index should reference it in the User Guide section. Verify the current structure:

```bash
grep -A 10 "User Guide" docs/index.rst
```

- [ ] **Step 3: Add python-api link if not present**

If `usage/python-api` is not in the User Guide toctree, add it:

```bash
# The User Guide section should include:
# getting-started/index
# usage/cli
# usage/model-xdm-generator  
# usage/python-api  <-- Add this if missing
# requirements/index
# testing/index
```

- [ ] **Step 4: Build and verify all links**

Run: `cd docs && make clean && make html`

Check for warnings:
```bash
grep -i "warning" docs/build.log || echo "No warnings"
```

- [ ] **Step 5: Test key pages**

```bash
# Test that pages exist
ls docs/_build/html/getting-started/*.html
ls docs/_build/html/usage/*.html
ls docs/_build/html/examples/*.html
ls docs/_build/html/api/generator.html
```

- [ ] **Step 6: Commit**

```bash
git add docs/index.rst
git commit -m "docs: Update main index with new content"
```

---

### Task 19: Final Documentation Build and Verification

**Files:**
- Test: Complete documentation build

- [ ] **Step 1: Clean build**

Run: `cd docs && make clean && make html 2>&1 | tee final-build.log`

- [ ] **Step 2: Check for errors**

Run: `grep -i "error\|severe" final-build.log || echo "No errors found"`

- [ ] **Step 3: Check for warnings**

Run: `grep -i "warning" final-build.log | head -20`

Expected: No broken link warnings

- [ ] **Step 4: Verify key navigation paths**

```bash
# Test main navigation
ls docs/_build/html/index.html

# Test getting-started
ls docs/_build/html/getting-started/index.html
ls docs/_build/html/getting-started/installation.html
ls docs/_build/html/getting-started/first-xdm.html
ls docs/_build/html/getting-started/concepts.html
ls docs/_build/html/getting-started/generator-quickstart.html

# Test usage
ls docs/_build/html/usage/cli.html
ls docs/_build/html/usage/model-xdm-generator.html
ls docs/_build/html/usage/python-api.html

# Test examples
ls docs/_build/html/examples/cli-usage.html
ls docs/_build/html/examples/README.html

# Test api
ls docs/_build/html/api/generator.html

# Test requirements and testing
ls docs/_build/html/requirements/index.html
ls docs/_build/html/testing/index.html
```

- [ ] **Step 5: Open and visually inspect**

Run: `open docs/_build/html/index.html`

Manually verify:
- Main page loads
- Version is 1.3.1
- Navigation links work
- Getting Started section visible
- Generator docs accessible

- [ ] **Step 6: Commit any final fixes**

```bash
# Only if issues were found and fixed
git add docs/
git commit -m "docs: Final documentation fixes"
```

---

## Completion Checklist

After implementing all tasks:

- [ ] Phase 1 complete: Foundation fixed, navigation works
- [ ] Phase 2 complete: Getting-started guides new users
- [ ] Phase 3 complete: Generator documentation comprehensive
- [ ] Phase 4 starter: Usage examples and basic API guide added (comprehensive API reference is future work)
- [ ] Documentation builds without errors
- [ ] All key navigation paths tested
- [ ] Version information accurate
- [ ] Ready for ReadTheDocs deployment

## Phase 4 Future Work

For comprehensive "Complete Reference" as specified in the design spec, future iterations should add:

- `docs/api/parser.rst` - Parser layer documentation
- `docs/api/models.rst` - Model layer documentation  
- `docs/api/reporters.rst` - Reporter layer documentation
- `docs/examples/batch-processing.md` - Advanced batch processing examples
- Per-stack module documentation (core → CAN → ETH → LIN → FR → MEM → DIAG priority)

These should be done incrementally as needed by users.

## Deployment

Documentation will auto-build on ReadTheDocs when pushed to main. Verify at:
```
https://py-eb-model.readthedocs.io/
```

For local preview:
```bash
cd docs && make html && open _build/html/index.html
```
