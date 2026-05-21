# py-eb-model

Python parser engine for EB Tresos XDM (XML Data Model) files used in AUTOSAR automotive software development. Extracts configuration data from proprietary XML formats and exports to Excel for analysis and reporting.

## Features

- **50+ Module Support**: Covers core AUTOSAR modules including OS, RTE, NvM, EcuC, and communication stacks
- **Unified CLI**: Single `eb-convert` command with auto-detection of module types
- **Batch Processing**: Convert multiple XDM files in one operation
- **Standards Compliant**: ISO/IEC/IEEE 29119 compliant testing and requirements traceability
- **Enterprise Ready**: Comprehensive documentation, requirements traceability, and integration testing

## Installation

```bash
pip install py_eb_model
```

## Quick Start

### Convert XDM to Excel

```bash
# Convert a single file
eb-convert Os.xdm output/

# Convert multiple files
eb-convert Os.xdm NvM.xdm Rte.xdm output/

# With verbose logging
eb-convert --verbose Os.xdm output/

# With file logging
eb-convert --log conversion.log Os.xdm output/
```

### Auto-Detection

The CLI automatically detects module type from the XDM file's MODULE-CONFIGURATION tag. No need to specify module names - they're extracted from the file itself.

### Output

For each input file, an Excel file is generated in the output directory:
- `Os.xdm` → `output/Os.xlsx`
- `NvM.xdm` → `output/NvM.xlsx`
- `Rte.xdm` → `output/Rte.xlsx`
- etc.

## Supported Modules

### Core Modules
- **Os**: Operating System configuration (tasks, ISRs, resources, schedule tables, counters)
- **Rte**: Runtime Environment configuration (entities, events, data mappings)
- **NvM**: Non-Volatile Memory manager (block descriptors, datasets)
- **EcuC**: ECU Configuration (partitions, core definitions)
- **BswM**: Basic Software Mode manager
- **Tm**: Trigger Manager
- **PbcfgM**: Port Configuration Manager
- **EcuM**: ECU State Manager
- **Det**: Development Error Tracer

### Communication Stacks
- **CAN Stack**: CanIf, CanNm, CanSM, CanTp
- **LIN Stack**: LinIf, LinSM, LinTp
- **FlexRay Stack**: FrIf, FrNm, FrSM, FrTp, FrArTp
- **Ethernet Stack**: EthIf, EthSM, TcpIp, SoAd, UdpNm, DoIP, SomeIpTp

### Communication Modules
- **Com**: Communication layer
- **ComM**: Communication Manager
- **PduR**: PDU Router
- **IpduM**: IPDU Manager
- **LdCom**: Low-Level COM
- **Nm**: Network Management
- **Crc**: Cyclic Redundancy Check

### Memory Modules
- **MemIf**: Memory Abstraction Interface
- **Fee**: Flash EEPROM Emulation
- **Ea**: EEPROM Abstraction
- **MemMap**: Memory Mapping
- **MemAcc**: Memory Access

### Crypto/Security
- **Crypto**: Cryptographic services
- **CryIf**: Crypto Interface
- **Csm**: Cryptographic Service Manager
- **SecOC**: Secure Onboard Communication

### Diagnostics/Events
- **FiM**: Function Inhibition Manager
- **Dcm**: Diagnostic Communication Manager
- **Dem**: Diagnostic Event Manager
- **Dlt**: Diagnostic Log and Trace

### J1939 Stack
- **J1939Dcm**: J1939 Diagnostic Communication Manager
- **J1939Nm**: J1939 Network Management
- **J1939Rm**: J1939 Route Manager
- **J1939Tp**: J1939 Transport Protocol

## Development

### Building Distribution

```bash
# Build distribution
python -m build

# Verify distribution
twine check dist/*

# Upload to PyPI
twine upload dist/*
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/eb_model --cov-report=term-missing

# Run only unit tests
pytest -m "not integration"

# Run only integration tests
pytest -m integration
```

### Linting

```bash
# Using ruff
ruff check .

# Using flake8
flake8 . --max-line-length=150 --ignore=F401,W293,F403
```

## CLI Options

### eb-convert

```bash
eb-convert <input.xdm> [<input2.xdm> ...] <output_dir/> [options]
```

**Options:**
- `-v, --verbose`: Enable verbose (DEBUG) logging
- `--log LOG`: Log file path for file-based logging
- `--skip-os-task`: Skip generating Os task (OS module only)

### Legacy Commands

The following legacy commands are still available but deprecated:
- `os-xdm-xlsx`, `rte-xdm-xlsx`, `nvm-xdm-xlsx`, `ecuc-xdm-xlsx` (core modules)
- `bswm-xdm-xlsx`, `tm-xdm-xlsx`, `pbcfgm-xdm-xlsx`, `ecum-xdm-xlsx`, `det-xdm-xlsx` (system)
- 52+ additional module-specific commands

Please migrate to `eb-convert` for new usage.

### PrefSystemImporter

Reads EB preference XDM and generates ARXML file lists or AUTOSAR builder projects.

```bash
pref-system-importer [options] INPUTS [INPUTS ...] OUTPUT
```

**Key Options:**
- `--base-path BASE_PATH`: Base path for EB tresos project
- `--file-list`: Generate ARXML file list (default)
- `--ab-project`: Generate AUTOSAR builder project
- `--project PROJECT`: Project name for AUTOSAR builder project
- `--env ENV [ENV ...]`: Specify environment variables

**Example:**
```bash
# Generate ARXML file list
pref-system-importer --base-path /path/to/project .prefs/pref_imp_exp_Imp_System.xdm output.lst

# Generate AUTOSAR builder project
pref-system-importer --base-path /path/to/project --ab-project --project MyProject .prefs/pref_system.xdm .project
```

## Documentation

- **[CLAUDE.md](CLAUDE.md)**: Development guide for contributors
- **[docs/cli.md](docs/cli.md)**: Detailed CLI usage documentation
- **[docs/requirements/](docs/requirements/)**: Software requirements with traceability
- **[docs/tests/](docs/tests/)**: ISO 29119 compliant test documentation

## Change History

### Version 1.3.0

**Major Release - Complete XDM Model Coverage**

1. **CLI Refactoring**
   - Unified `eb-convert` command replacing 52+ module-specific CLI commands
   - Auto-detection of module types from XDM files
   - Batch processing support for multiple files
   - Enhanced logging with file and console output

2. **Module Expansion**
   - Added J1939 stack: J1939Dcm, J1939Nm, J1939Rm, J1939Tp
   - Added diagnostic stack: FiM, Dcm, Dem, Dlt
   - Added crypto/security stack: Crypto, CryIf, Csm, SecOC
   - Added memory stack: MemIf, Fee, Ea, MemMap, MemAcc, Crc
   - Added communication stack: Com, LdCom, PduR, IpduM, Nm, ComM
   - Added Ethernet and FlexRay communication stack modules

3. **Testing Improvements**
   - Integration tests for XDM file parsing
   - ISO/IEC/IEEE 29119 compliant test documentation
   - Test reorganization following modern Python layout
   - Expanded test coverage for new modules

4. **Documentation**
   - Requirements traceability matrix linking code to SWR documents
   - Comprehensive CLI usage documentation
   - Enterprise-standard software requirements documentation
   - Architecture design specifications

5. **Code Quality**
   - Migration from setup.py to pyproject.toml
   - Type annotations throughout codebase
   - Linting tooling configuration (ruff, flake8)
   - Code quality improvements and bug fixes
   - Import hygiene improvements with explicit imports

6. **Infrastructure**
   - Parser-writer registry with auto-discovery
   - CLI options registry for module-specific arguments
   - Modern Python project layout with src/ directory
   - Enhanced error handling and logging

**Version 1.2.3**

1. Implement OsApplication parser.

**Version 1.2.2**

1. Fix TARGET of EcucPartitionSoftwareComponentInstanceRef is empty and skipped to added.

**Version 1.2.1**

1. Read EcucPartition from EcuC.xdm
2. Read EcucPartitionSoftwareComponentInstanceRef from EcuC.xdm

**Version 1.2.0**

1. Fix AbstractEbModelParser::_convert_value error.
2. Add structure for Ecuc.xdm and BswM.xdm.

**Version 1.1.9**

1. Parse OsAppAlarmRef List of OsApplication
2. Parse OsAppCounterRef List of OsApplication
3. Parse OsAppScheduleTableRef Lis of OsApplication
4. Add **read_eb_origin_value** method to read optional EB extended configuration
5. Fix OsIsrPriority and OsIsrVector issue.

**Version 1.1.8**

1. Support to read NvM configuration from EB tresos Xdm file
2. Export NvM Configuration to excel file.

**Version 1.1.7**

1. Solve case issue of read_optional_value enables attribute.
2. Support to read IMPORT_INFO for OsResource.
3. Add test cases for OsXdmParser.

**Version 1.1.6**

1. Add OsResource support in Os Module:
   - Os::getOsResourceList
   - Os::addOsResource
2. Read NvMBlockDescriptor List

**Version 1.1.5**

1. Add new interfaces to support to get the instance by name:
   - Rte::getRteBswModuleInstance
   - Rte::getRteBswModuleInstance

**Version 1.1.4**

1. Fix incorrect attribute of osTaskAutostart.
2. Add isOsTaskAutostart method to get enabled flag of osTaskAutostart.
3. Add flake8 change rules.

**Version 1.1.3**

1. Support to read Isr Priority and Vector for R52+ core.
2. Export Isr Priority and Vector to Excel.
3. Read OsAppResourceRef, OsAppIsrRef from OsApplication.

**Version 1.1.2**

1. Read OsAppTaskRef from OsApplication.

**Version 1.1.1**

1. Add support to append SystemMod/EcuExtract.arxml into list automatically for PrefSystemImporter.

**Version 1.0.3**

1. Generate System import file list based on EB preference Xdm.
2. Add support to read OsTaskAutostart element.
3. Add support to read OsTaskType element.

**Version 1.0.2**

1. Fix setOsAlarmCallbackName bug

**Version 1.0.1**

1. Change attribute to start with lowercase
2. read_ref_value and read_optional_ref_value method returns EcucRefType.
3. Read OsScheduleTable and export to excel
4. Read OsCounter and export to excel

**Version 0.8.0**

1. Create basic model for EB xdm. (Issue #1)
2. Support to extract Os Tasks/Isrs from EB xdm and store them in excel files. (Issue #1)

## License

MIT License - see LICENSE file for details

## Links

- **Repository**: https://github.com/melodypapa/py-eb-model
- **Issues**: https://github.com/melodypapa/py-eb-model/issues
- **PyPI**: https://pypi.org/project/py_eb_model/