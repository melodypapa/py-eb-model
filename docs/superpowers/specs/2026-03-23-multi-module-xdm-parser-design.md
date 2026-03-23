# Design Specification: Multi-Module XDM Parser Expansion

**Date**: 2026-03-23
**Status**: Approved
**Approach**: Tiered Phased Rollout

## Executive Summary

This design documents the expansion of py-eb-model to support 80+ AUTOSAR modules from the ACG-9_2_0_WIN32X86 EB Tresos release. The implementation follows a tiered phased rollout approach, with each tier delivered as a separate PR.

## Background

**py-eb-model** is a Python parser engine for EB Tresos XDM (XML Data Model) files used in AUTOSAR automotive software development. Currently supports 5 modules: Os, Rte, NvM, EcuC, BswM.

The ACG-9_2_0_WIN32X86 release contains XDM files for 80+ additional modules including CAN/LIN communication, Ethernet networking, memory management, security, and diagnostics.

## Objectives

- Add support for all 80+ modules from ACG-9_2_0_WIN32X86
- Maintain existing code quality, patterns, and conventions
- Ensure full test coverage for each module
- Provide formal requirements documentation
- Enable incremental validation through tiered PRs

## Architecture Overview

The system uses a 3-layer architecture:

```
XDM File → Factory → Parser → Model → Reporter → Excel/Output
```

### Layers

1. **Parser Layer**: Reads EB Tresos XDM XML files, handles namespace-aware XPath queries
2. **Model Layer**: Domain objects representing AUTOSAR configuration hierarchies
3. **Reporter Layer**: Exports data to Excel/Markdown/Text formats

### Key Components

- **AbstractEbModelParser**: Base class with common XML parsing methods
- **EbParserFactory**: Determines parser type from XDM file's MODULE-CONFIGURATION tag
- **Module classes**: Domain objects (Os, Rte, NvM, etc.) inheriting from EcucObject
- **Reporter classes**: Format-specific output writers

## Tiered Phased Rollout

### Tier Structure

| Tier | Modules | Description |
|------|---------|-------------|
| T1 | Base, Tm, PbcfgM, EcuM, Det | Foundational and system management |
| T2 | CanIf, CanNm, CanSM, CanTp, LinIf, LinSM, LinTp | CAN/LIN communication stack |
| T3 | EthIf, EthSM, SoAd, TcpIp, UdpNm, DoIP, SomeIpTp, FrIf, FrTp, FrNm, FrSM, FrArTp | Ethernet and FlexRay |
| T4 | Com, LdCom, PduR, IpduM, ComM, Nm, Crc | Communication management layer |
| T5 | NvM, MemIf, Fee, Ea, MemMap, MemAcc | Memory management |
| T6 | Crypto, CryIf, Csm, SecOC, FiM, Dcm, Dem, Dlt, J1939Dcm, J1939Nm, J1939Rm, J1939Tp | Security, diagnostics, specialized |

### Tier Rationale

T1 provides foundational modules required by other tiers. T2-T6 implement vertical stacks based on technology and function. This order ensures dependencies are available before dependent modules.

## Implementation Pattern

### Per Module Artifacts

Each module requires:

1. **Parser Class** (`{Module}XdmParser`): Inherits from `AbstractEbModelParser`, implements `parse()` method

```python
class TmXdmParser(AbstractEbModelParser):
    def __init__(self):
        super().__init__()
        self.tm = None

    def parse(self, element: ET.Element, doc: EBModel):
        if self.get_component_name(element) != "Tm":
            raise ValueError("Invalid Tm xdm file")

        tm = doc.getTm()
        self.read_version(element, tm)
        # Module-specific parsing
        self.tm = tm
```

2. **Model Class** (`{Module}`): Inherits from `Module`, contains configuration objects

```python
class Tm(Module):
    def __init__(self, parent, name):
        super().__init__(parent, name)
        self.general = None
```

3. **Reporter Class** (`{Module}XdmXlsWriter`): Inherits from abstract Excel writer, implements module-specific export

4. **CLI Entry Point**: Added to `setup.py` under `console_scripts`

### File Structure

```
src/eb_model/
├── parser/
│   ├── eb_parser.py                    # Base class (existing)
│   ├── eb_parser_factory.py            # Factory (needs updates)
│   ├── {module}_xdm_parser.py          # NEW
├── models/
│   ├── abstract.py                     # Base classes (existing)
│   ├── eb_doc.py                       # Document model (needs updates)
│   ├── {module}_xdm.py                 # NEW
├── reporter/excel_reporter/
│   ├── abstract.py                     # Base reporter (existing)
│   ├── {module}_xdm.py                 # NEW
└── cli/
    └── {module}_xdm_2_xls_cli.py       # NEW
```

### Required Updates

**EbParserFactory.create()**: Add mapping for new modules
```python
parsers = {
    "Os": OsXdmParser,
    "Tm": TmXdmParser,
    "PbcfgM": PbcfgMXdmParser,
    # ... all modules
}
```

**EBModel**: Add singleton getter method for each module
```python
def getTm(self) -> Tm:
    if self.tm is None:
        self.tm = Tm(self, "Tm")
    return self.tm
```

## Data Flow

1. **CLI entry point** receives XDM file path
2. **Factory** reads XML, extracts module name from `MODULE-CONFIGURATION` tag
3. **Parser** instantiated, loads XML with namespace handling
4. **Parser.parse()** traverses XML using XPath, populates Model objects
5. **Model** represents hierarchical AUTOSAR configuration
6. **Reporter** exports Model to Excel

## Namespace Handling

The XDM format uses namespaces extensively. All parsers inherit namespace handling from `AbstractEbModelParser`:

- Namespaces are read from XML and stored in `self.nsmap` dictionary
- XPath queries use namespace prefix: `.//d:var[@name='%s']` with `self.nsmap`
- Common namespaces: `d` (data), `a` (attribute), `v` (schema)

## Reference Resolution

ASPath references (e.g., `ASPath:/AUTOSAR/EcucDefs/...`) are handled by `EcucRefType`:

- Raw value stored as string
- Short name extracted via regex from `getShortName()`
- Calculated values (`@CALC(SvcAs:...)`) flagged via `isCalculatedSvcAs()`

## Error Handling

| Stage | Validation | Error Type |
|-------|-----------|------------|
| Factory | XML format valid, module name detected | `ValueError` |
| Parser.load_xdm() | Root tag is `datamodel` | `ValueError` |
| Parser.parse() | Component name matches expected module | `ValueError` |
| read_value() | Required element exists | `KeyError` |
| read_optional_value() | Element may be missing (returns None) | N/A |

### ENABLE Attribute Handling

Optional elements are controlled by `ENABLE` attribute:
- If `ENABLE="false"` → element is ignored, method returns None
- If `ENABLE` not present → element is active
- Checked in: `find_ctr_tag()`, `read_optional_value()`, `read_optional_ref_value()`

## Testing

### Test Structure

Tests mirror source structure:

```
src/eb_model/tests/
├── parser/
│   ├── test_{module}_xdm_parser.py    # NEW
└── models/
    └── test_{module}_xdm.py            # NEW
```

### Test Patterns

- **Parser tests**: Full XDM parsing, version extraction, section parsing
- **Model tests**: Initialization, getter/setter, fluent interface
- **Integration tests**: Parse XDM → Export to Excel → Validate output

### Test Data

Use sample XDM files from ACG-9_2_0_WIN32X86 as test fixtures in `tests/fixtures/xdm/`

## Code Conventions

- **Classes**: PascalCase (`EcucObject`, `OsXdmParser`)
- **Methods**: camelCase (`getName()`, `read_value()`) - intentional for AUTOSAR consistency
- **Properties/Attributes**: camelCase (`name`, `parent`, `nsmap`)
- **Constants**: UPPER_CASE
- **Fluent interface**: Setter methods return `self` for chaining

## Documentation

- Update `CLAUDE.md` with new CLI entry points and patterns
- Create formal requirements specification: `docs/requirements/swr_os-module.md`
- Document each module's specific structure and requirements

## Success Criteria

Each tier must meet these criteria before moving to the next tier:

- All modules in tier parse correctly from sample XDM files
- Full unit test coverage for parsers and models
- Integration tests for Excel export
- Updated documentation (CLAUDE.md, requirements)
- Code passes linting and CI checks
- PR reviewed and approved

## Estimated Timeline

- **Tier 1**: 1-2 weeks (5 modules)
- **Tier 2**: 2-3 weeks (7 modules)
- **Tier 3**: 3-4 weeks (13 modules)
- **Tier 4**: 2-3 weeks (6 modules)
- **Tier 5**: 2-3 weeks (6 modules)
- **Tier 6**: 3-4 weeks (15 modules)

**Total**: 13-19 weeks for all 80+ modules

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Module complexity varies widely | Start with simpler modules (Tier 1) to establish patterns |
| XDM format inconsistencies | Comprehensive test coverage with sample files |
| Breaking changes to existing code | Run full test suite on each tier completion |
| Large code review burden | Tiered approach limits PR size |
| Timeline slippage | Focus on core modules first, optional modules can be deferred |

## References

- CLAUDE.md: Project instructions and conventions
- ACG-9_2_0_WIN32X86/: Source XDM files for all modules
- Existing module implementations (Os, Rte, NvM, EcuC, BswM)