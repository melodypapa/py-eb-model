# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**py-eb-model** is a Python parser engine for EB Tresos XDM (XML Data Model) files used in AUTOSAR automotive software development. It extracts configuration data from proprietary XML formats and exports to Excel for analysis and reporting.

### Key Architecture

This is a layered XML parsing system with three main components:

1. **Parser Layer** (`src/eb_model/parser/`): Reads EB Tresos XDM XML files
   - Organized by stack type: `core/`, `can_stack/`, `lin_stack/`, `fr_stack/`, `eth_stack/`, `com_stack/`, `mem_stack/`, `crypto_stack/`, `diag_stack/`, `j1939_stack/`
   - `AbstractEbModelParser`: Base class in `core/eb_parser.py` with common XML parsing methods using XPath with namespace handling
   - `EbParserFactory`: Automatically determines parser type from XDM file's MODULE-CONFIGURATION tag
   - Module-specific parsers: 50+ parsers across all stacks (e.g., `OsXdmParser`, `RteXdmParser`, `CanIfXdmParser`, `EthIfXdmParser`)

2. **Model Layer** (`src/eb_model/models/`): Domain objects representing AUTOSAR configuration
   - `EBModel`: Singleton root document model containing module containers
   - `Module`: Base class for AUTOSAR modules (Os, Rte, NvM, EcuC, BswM, Tm, PbcfgM, EcuM, Det, etc.)
   - `EcucObject`: Abstract base for all configuration objects with hierarchical naming
   - `EcucParamConfContainerDef`: Container for configuration parameters with element management
   - `EcucRefType`: Reference type for AUTOSAR path references (ASPath format)

3. **Reporter Layer** (`src/eb_model/reporter/`): Outputs data to various formats
   - Organized by stack type matching parser structure: `excel_reporter/core/`, `excel_reporter/can_stack/`, etc.
   - `AbstractEbModelXlsWriter`: Base class in `excel_reporter/core/abstract.py`
   - Excel reporters: 50+ reporters using naming convention `{Module}Xdm` (e.g., `OsXdm`, `RteXdm`, `CanIfXdm`)
   - `parser_writer_registry`: Auto-discovers writer classes from parser class names (e.g., `OsXdmParser` → `OsXdm`)
   - Markdown reporter: `OsApplicationMarkdownWriter`
   - Text writers: `TextPreferenceModelWriter`, `ABProjectWriter`

### Critical XML Parsing Patterns

The XDM format uses namespaces extensively. All parsers inherit namespace handling from `AbstractEbModelParser`:

- Namespaces are read from XML and stored in `self.nsmap` dictionary
- XPath queries use namespace prefix: `.//d:var[@name='%s']` with `self.nsmap`
- References use ASPath format: `ASPath:/path/to/element` - extracted via `read_ref_raw_value()`
- ENABLE attribute checking determines if optional elements are active
- Some values use calculated syntax: `@CALC(SvcAs,os.resources,1)` for dynamic references

The factory pattern in `EbParserFactory` inspects the XML root's MODULE-CONFIGURATION choice tag to determine which specific parser to instantiate.

**Common XML Elements:**
- `<d:var>`: Simple values (types: INTEGER, BOOLEAN, ENUMERATION, STRING)
- `<d:lst>`: Lists/containers of elements
- `<d:ctr>`: Container with nested elements
- `<d:ref>`: References to other elements with ASPath format
- `<a:a>`: Attributes including ENABLE, IMPORTER_INFO, and calculated values

## Development Commands

#### Testing
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/integration/test_xdm_file_parsing.py

# Run single test method
pytest tests/parser/core/test_os_xdm_parser.py::TestOsXdmParser::test_read_os_resources

# Run tests with coverage
pytest --cov=src/eb_model --cov-report=term-missing

# Run only unit tests (exclude integration)
pytest -m "not integration"

# Run only integration tests
pytest -m integration

# Run tests for specific Python version (CI tests 3.9, 3.10, 3.11)
python3.9 -m pytest
```

**Testing Patterns:**
- Unit tests use mock XML elements with `ET.fromstring()` for isolated testing
- Integration tests require real EB Tresos XDM demo files in `tests/integration/data_files/`
- Test files mirror source structure: `tests/parser/`, `tests/models/`, `tests/reporter/`
- Pytest markers distinguish integration tests with `@pytest.mark.integration`

### Building and Packaging
```bash
# Build distribution (preferred method)
python -m build

# Alternative: build wheel distribution with setup.py
python setup.py bdist_wheel

# Install in development mode
pip install -e .

# Install dependencies
pip install openpyxl  # runtime dependency
pip install pytest ruff mypy  # development dependencies

# Verify distribution before upload
twine check dist/*

# Upload to PyPI (requires credentials)
twine upload dist/*
```

### Linting
```bash
# Using ruff (configured in pyproject.toml)
ruff check .

# Using flake8 (legacy CI standard)
flake8 . --max-line-length=150 --ignore=F401,W293,F403

# CI strict mode (from GitHub Actions)
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

### Git Commit Conventions

**Do NOT add Claude as co-author** to commits. When creating commits, use only the actual human author information. Do not include `Co-Authored-By: Claude Opus` or similar attribution lines in commit messages.

**ALWAYS work on feature branches, not main.**
- Create a feature branch for any work (feature/feature-name)
- Commit all work to the feature branch
- Only merge to main after work is complete and reviewed
- Never commit directly to main unless explicitly authorized

## Code Style Conventions

**Important**: This codebase uses **camelCase** for methods and properties (not snake_case per Python conventions). This is intentional for consistency with AUTOSAR naming conventions.

- **Classes**: PascalCase (`EcucObject`, `OsXdmParser`)
- **Methods**: camelCase (`getName()`, `read_value()`, `findCtrTag()`)
- **Properties/Attributes**: camelCase (`name`, `parent`, `nsmap`)
- **Constants**: UPPER_CASE

### Fluent Interface Pattern
Most setter methods return `self` to enable method chaining:
```python
module.setName("Os").setArVersion(version)
```

### Import Organization
Standard library imports first, then relative imports with blank line separator:
```python
import logging
import xml.etree.ElementTree as ET
from typing import List

from ..models.eb_doc import EBModel
from ..models.abstract import EcucRefType
```

### Module Organization
- `src/eb_model/parser/`: XML parsing logic organized by stack type
- `src/eb_model/models/`: Domain models mirroring parser structure
- `src/eb_model/reporter/`: Output generators (Excel, Markdown, text)
- `src/eb_model/cli/`: Command-line interfaces
- `src/eb_model/writer/`: Specialized writers (preference models, project files)
- `tests/`: Comprehensive test suite mirroring source structure

## Common Patterns

### Registry Pattern

The codebase uses registry patterns for automatic discovery:

**Parser Registry** (`EbParserFactory._PARSERS`):
- Maps module names to parser classes: `"Os": OsXdmParser`
- Auto-detects parser type from XDM file's MODULE-CONFIGURATION tag
- Supports 50+ modules across all stacks

**Writer Registry** (`parser_writer_registry`):
- Auto-discovers Excel writer classes from parser class names
- Naming convention: `OsXdmParser` → `OsXdm` writer
- Enables unified `eb-convert` CLI command

### Creating a New Parser
1. Inherit from `AbstractEbModelParser`
2. Implement `parse()` method to traverse XML and populate model objects
3. Use inherited methods: `read_value()`, `read_optional_value()`, `read_ref_value()`, `find_ctr_tag()`
4. Register in `EbParserFactory._PARSERS` dictionary
5. Create corresponding model class in `src/eb_model/models/`

### Creating a New Model Class
1. Inherit from `EcucObject` or `EcucParamConfContainerDef`
2. Call `super().__init__(parent, name)` which auto-registers with parent
3. Add properties with camelCase naming
4. Provide getter/setter methods following `getProperty()`/`setProperty()` pattern
5. Use type hints: `self.elements: Dict[str, EcucObject] = {}`

### Creating a New Excel Reporter
1. Inherit from `AbstractEbModelXlsWriter` in `excel_reporter/core/abstract.py`
2. Implement `write()` method to generate Excel output
3. Place in appropriate stack directory: `excel_reporter/can_stack/`, `excel_reporter/core/`, etc.
4. Follow naming convention: `{Module}Xdm` class name
5. Register will happen automatically via `parser_writer_registry`

### Adding CLI Commands
Add entry point in `pyproject.toml` under `[project.scripts]` section following pattern:
```python
'module-xdm-xlsx = "eb_model.cli.module_xdm_2_xls_cli:main"'
```

**Error Handling Patterns:**
- Use `logging.getLogger()` for logging (inherited in `AbstractEbModelParser`)
- Raise `NotImplementedError` for unsupported module types
- Raise `ValueError` for abstract class instantiation attempts
- Check ENABLE attributes before processing optional elements via `read_optional_value()`

**Version Checking:**
- Use `pkg_resources.require("py_eb_model")[0].version` to get current version
- CLI commands display version in help text

**Unified CLI command (recommended):**
- `eb-convert`: Auto-detects module type from XDM file, supports batch conversion

**Legacy module-specific commands** (52 commands):
- `os-xdm-xlsx`, `rte-xdm-xlsx`, `nvm-xdm-xlsx`, `ecuc-xdm-xlsx` (core modules)
- `bswm-xdm-xlsx`, `tm-xdm-xlsx`, `pbcfgm-xdm-xlsx`, `ecum-xdm-xlsx`, `det-xdm-xlsx` (system)
- CAN stack: `canif-xdm-xlsx`, `cannm-xdm-xlsx`, `cansm-xdm-xlsx`, `cantp-xdm-xlsx`
- LIN stack: `linif-xdm-xlsx`, `linsm-xdm-xlsx`, `lintp-xdm-xlsx`
- FlexRay: `frif-xdm-xlsx`, `frnm-xdm-xlsx`, `frsm-xdm-xlsx`, `frtp-xdm-xlsx`, `frartp-xdm-xlsx`
- Ethernet: `ethif-xdm-xlsx`, `ethsm-xdm-xlsx`, `tcpip-xdm-xlsx`, `soad-xdm-xlsx`, `udpnm-xdm-xlsx`, `doip-xdm-xlsx`, `someiptp-xdm-xlsx`
- PDU/COM: `pdur-xdm-xlsx`, `ipdum-xdm-xlsx`, `com-xdm-xlsx`, `ldcom-xdm-xlsx`, `comm-xdm-xlsx`, `nm-xdm-xlsx`, `crc-xdm-xlsx`
- Memory: `memif-xdm-xlsx`, `fee-xdm-xlsx`, `ea-xdm-xlsx`, `memmap-xdm-xlsx`, `memacc-xdm-xlsx`
- Crypto: `crypto-xdm-xlsx`, `cryif-xdm-xlsx`, `csm-xdm-xlsx`, `secoc-xdm-xlsx`
- Diagnostics: `fim-xdm-xlsx`, `dcm-xdm-xlsx`, `dem-xdm-xlsx`, `dlt-xdm-xlsx`
- J1939: `j1939dcm-xdm-xlsx`, `j1939nm-xdm-xlsx`, `j1939rm-xdm-xlsx`, `j1939tp-xdm-xlsx`
- `PrefSystemImporter`: EB preference XDM to ARXML file list or AUTOSAR builder project

See [docs/usage/cli.md](docs/usage/cli.md) for detailed CLI usage documentation.

## File Structure Notes

- Source code in `src/eb_model/` using setuptools src layout
- Tests in `tests/` directory (integration tests in `tests/integration/`)
- CLI entry points in `src/eb_model/cli/`
- Configuration in `pyproject.toml` (build dependencies, tool config, pytest markers)
- No `requirements.txt` - dependencies declared in `pyproject.toml`

### Documentation Structure

The project uses a three-tier documentation structure:

```
docs/
├── requirements/          # Software requirements (273 requirements)
│   ├── can_stack/        # CAN stack requirements
│   ├── core/             # Core modules (OS, RTE, EcuC, BSW)
│   ├── eth_stack/        # Ethernet stack requirements
│   ├── mem_stack/        # Memory stack requirements
│   └── ...               # Other stacks
├── tests/                # Test specifications (765 test cases)
│   ├── unit/             # Unit test specs (UTS_*.md)
│   ├── integration/      # Integration test specs (ITS_*.md)
│   ├── system/           # System test specs (SYTS_*.md)
│   └── requirements-traceability-matrix.md
└── usage/                # User documentation
    └── cli.md            # CLI usage guide
```

**Key Points:**
- Requirements organized by stack type (not flat structure)
- Tests organized by test type (unit/integration/system)
- User documentation in separate `usage/` folder
- Complete traceability matrix linking requirements to tests

## Known Constraints

- Python 3.9+ (tested on 3.9, 3.10, 3.11, 3.14 in CI)
- EB Tresos XDM files use proprietary XML schema with namespace handling
- Some AUTOSAR path references use special `@CALC(SvcAs:...)` syntax for calculated values
- The `read_optional_value()` method checks ENABLE attribute before returning values
- Fluent interface pattern means many methods return `self` for chaining
- Integration tests require real EB Tresos XDM demo files in `tests/integration/data_files/`
- Abstract classes raise `ValueError` if directly instantiated
- Namespace prefixes must be used in XPath queries: `d:var`, `d:lst`, `d:ctr`, `d:ref`, `a:a`
- Reference values are wrapped in `EcucRefType` objects with ASPath format

## Version Information

Current version: 1.3.1 (defined in `pyproject.toml`)

Check version in code: `pkg_resources.require("py_eb_model")[0].version`

## CI/CD

**Testing**: GitHub Actions CI runs on Python 3.9, 3.10, 3.11, and 3.14 with both linting (flake8) and testing (pytest)

**Publishing**: PyPI publishing happens automatically via GitHub Actions when releases are created (using OIDC authentication)

**Coverage**: pytest always runs with coverage reporting due to `addopts` in `pyproject.toml` configuration

**Type Checking**: mypy is configured but very permissive (many error codes disabled) - type annotations are present but not strictly enforced

## Documentation Conventions

### Requirement Traceability

All module, class, and key method docstrings should include "Implements" references to link code to software requirements (SWR documents):

```python
class OsXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR OS module configuration from EB Tresos XDM files.

    Implements: SWR_OS_00001 (OS Module Parser)
    """

    def read_os_tasks(self, element: ET.Element, os: Os):
        """
        Parse all OsTask containers from XDM.

        Implements: SWR_OS_00002 (Task parsing)
        """
```

**Rules:**
- Module-level docstrings: List all SWR IDs implemented in that module
- Class-level docstrings: Include the primary SWR ID for that class
- Method-level docstrings: Include SWR ID only for significant features (not for simple methods like `__init__`)
- SWR ID format: `SWR_<MODULE>_<NUMBER>` (e.g., `SWR_OS_00001`, `SWR_CANIF_00003`)
- Requirements are documented in `docs/requirements/swr_*.md` files

### Docstring Style

- Use Google-style docstrings
- Focus on **WHY** and non-obvious behavior, not just **WHAT**
- Avoid redundant docstrings that only restate the method name
- Document constraints, side effects, and edge cases
