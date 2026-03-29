# Design Specification: Tier 6 Implementation

**Date**: 2026-03-29
**Status**: Approved
**Approach**: Single PR for all 15 modules

## Executive Summary

This design documents the implementation of Tier 6 of the py-eb-model expansion: 15 AUTOSAR modules for security, diagnostics, and J1939 protocols. All modules will be delivered as a single PR following the established patterns from Tiers 1-5.

## Background

**py-eb-model** is a Python parser engine for EB Tresos XDM files. Tiers 1-5 (35 modules) have been completed. Tier 6 adds the final 15 modules from the ACG-9_2_0_WIN32X86 release.

## Objectives

- Add support for 15 remaining modules from ACG-9_2_0_WIN32X86
- Maintain existing code quality, patterns, and conventions
- Create comprehensive SW requirements and test case documentation
- Ensure full test coverage for each module
- Enable validation through a single PR

## Architecture Overview

The system uses the established 3-layer architecture:

```
XDM File → Factory → Parser → Model → Reporter → Excel/Output
```

### Layers

1. **Parser Layer**: Reads EB Tresos XDM XML files, handles namespace-aware XPath queries
2. **Model Layer**: Domain objects representing AUTOSAR configuration hierarchies
3. **Reporter Layer**: Exports data to Excel format

### Key Components

- **AbstractEbModelParser**: Base class with common XML parsing methods
- **EbParserFactory**: Determines parser type from XDM file's MODULE-CONFIGURATION tag
- **Module classes**: Domain objects (Crypto, Dcm, J1939Nm, etc.) inheriting from Module
- **Reporter classes**: Format-specific Excel output writers

## Module List

### Security Modules (5)

| Module | Description |
|--------|-------------|
| Crypto | Cryptographic operations interface |
| CryIf | Crypto Interface layer |
| Csm | Crypto Service Manager |
| SecOC | Secure Onboard Communication |
| FiM | Fault Isolation Manager |

### Diagnostics Modules (3)

| Module | Description |
|--------|-------------|
| Dcm | Diagnostic Communication Manager |
| Dem | Diagnostic Event Manager |
| Dlt | Diagnostic Log and Trace |

### J1939 Modules (4)

| Module | Description |
|--------|-------------|
| J1939Dcm | J1939 diagnostics |
| J1939Nm | J1939 network management |
| J1939Rm | J1939 routing |
| J1939Tp | J1939 transport protocol |

## Implementation Pattern

### Per Module Artifacts

Each of the 15 modules requires 8 artifacts:

1. **Parser Class** (`{Module}XdmParser`): Inherits from `AbstractEbModelParser`, implements `parse()` method
2. **Model Classes** (`{Module}`, `*Config`): Domain classes inheriting from `Module` and `EcucParamConfContainerDef`
3. **Reporter Class** (`{Module}XdmXlsWriter`): Inherits from `ExcelReporter`
4. **CLI Entry Point**: `{module}-xdm-xlsx = eb_model.cli.{module}_xdm_2_xls_cli:main`
5. **Parser Test**: `test_{module}_xdm_parser.py`
6. **Model Test**: `test_{module}_xdm.py`
7. **Requirements Doc**: `docs/requirements/swr_{module}.md`
8. **Test Cases Doc**: `docs/tests/tc_{module}.md`

### File Structure

```
src/eb_model/
├── parser/
│   ├── eb_parser_factory.py            # Add 15 mappings
│   ├── {module}_xdm_parser.py          # 15 NEW
├── models/
│   ├── eb_doc.py                       # Add 15 getters
│   ├── {module}_xdm.py                 # 15 NEW
├── reporter/excel_reporter/
│   ├── {module}_xdm.py                 # 15 NEW
├── cli/
│   └── {module}_xdm_2_xls_cli.py       # 15 NEW
└── tests/
    ├── parser/
    │   └── test_{module}_xdm_parser.py # 15 NEW
    └── models/
        └── test_{module}_xdm.py        # 15 NEW

docs/
├── requirements/
│   └── swr_{module}.md                 # 15 NEW
└── tests/
    └── tc_{module}.md                  # 15 NEW
```

**Total new files: 120**

### Required Updates

**EbParserFactory.create()**: Add mapping for new modules
```python
parsers = {
    # ... existing modules ...
    "Crypto": CryptoXdmParser,
    "CryIf": CryIfXdmParser,
    "Csm": CsmXdmParser,
    "SecOC": SecOCXdmParser,
    "FiM": FiMXdmParser,
    "Dcm": DcmXdmParser,
    "Dem": DemXdmParser,
    "Dlt": DltXdmParser,
    "J1939Dcm": J1939DcmXdmParser,
    "J1939Nm": J1939NmXdmParser,
    "J1939Rm": J1939RmXdmParser,
    "J1939Tp": J1939TpXdmParser,
}
```

**EBModel**: Add singleton getter method for each module
```python
def getCrypto(self) -> Crypto:
    container = EcucParamConfContainerDef(self, "Crypto")
    Crypto(container)
    return self.find("/Crypto/Crypto")
```

**pyproject.toml**: Add CLI entry points
```toml
[project.scripts]
crypto-xdm-xlsx = "eb_model.cli.crypto_xdm_2_xls_cli:main"
# ... all 15 modules
```

## Documentation Requirements

### Software Requirements Template

Each module requires `docs/requirements/swr_{module}.md` with:

```markdown
# Software Requirements Specification: {Module} Module

## Document Information
| Document Title | {Module} Module Software Requirements Specification |
| Document ID | SWR_{MODULE}_00001 |
| Version | 1.0 |
| Date | 2026-03-29 |
| Project | py-eb-model |
| Module | {Module} ({Description}) |

## 1. Introduction
### 1.1 Purpose
### 1.2 Scope
### 1.3 Definitions
### 1.4 References

## 2. General Description
### 2.1 Product Functions
### 2.2 Constraints

## 3. Functional Requirements
**SWR_{MODULE}_00001 - Parser Layer**: Parse {Module} XDM files.
**SWR_{MODULE}_00002 - Configuration**: Parse {Module} general settings.
**SWR_{MODULE}_00003 - Reporter Layer**: Generate Excel output.
**SWR_{MODULE}_00004 - CLI Interface**: Provide CLI command.

## 4. Non-Functional Requirements
**SWR_{MODULE}_00005**: Process XDM files up to 10MB.
**SWR_{MODULE}_00006**: Use fluent interface pattern.

## 5. Appendix
### 5.1 Data Model
### 5.2 Change History
```

### Test Cases Template (NEW)

Each module requires `docs/tests/tc_{module}.md` with:

```markdown
# Test Cases: {Module} Module

## Document Information
| Document Title | {Module} Module Test Cases |
| Document ID | TC_{MODULE}_00001 |
| Version | 1.0 |
| Date | 2026-03-29 |
| Project | py-eb-model |
| Module | {Module} |

## 1. Test Coverage

| SWR ID | Test Case | Test Method | Status |
|--------|-----------|-------------|--------|
| SWR_{MODULE}_00001 | TC_{MODULE}_001 | test_parse_xdm | Planned |
| SWR_{MODULE}_00002 | TC_{MODULE}_002 | test_read_general | Planned |
| SWR_{MODULE}_00002 | TC_{MODULE}_003 | test_module_initialization | Planned |

## 2. Test Case Specifications

### TC_{MODULE}_001: Parse {Module} XDM File
**Traceability**: SWR_{MODULE}_00001
**Type**: Unit Test
**Priority**: High

**Preconditions**:
- Valid {Module}.xdm file exists
- Module factory is configured

**Test Steps**:
1. Load {Module}.xdm file
2. Call `parse_xdm()` method
3. Verify module name is "{Module}"
4. Verify version information extracted

**Expected Result**:
- Parser completes without error
- Module object created with correct data
- AR and SW versions populated

**Test Method**: `test_parse_xdm()`
**File**: `src/eb_model/tests/parser/test_{module}_xdm_parser.py`

### TC_{MODULE}_002: Parse {Module} General Configuration
**Traceability**: SWR_{MODULE}_00002
**Type**: Unit Test
**Priority**: High

**Preconditions**:
- Valid XML element with general configuration
- Parser initialized with namespace map

**Test Steps**:
1. Create mock XML with general container
2. Call `read_general()` method
3. Verify configuration values extracted

**Expected Result**:
- General configuration object created
- All expected values populated correctly
- Optional values handled properly

**Test Method**: `test_read_general()`
**File**: `src/eb_model/tests/parser/test_{module}_xdm_parser.py`

### TC_{MODULE}_003: Module Initialization
**Traceability**: SWR_{MODULE}_00002
**Type**: Unit Test
**Priority**: Medium

**Preconditions**:
- EBModel instance exists
- Parent container exists

**Test Steps**:
1. Create module instance via `get{Module}()`
2. Verify module name
3. Verify parent reference
4. Verify version objects initialized

**Expected Result**:
- Module created successfully
- Name set correctly
- Parent reference valid
- Version objects not None

**Test Method**: `test_module_initialization()`
**File**: `src/eb_model/tests/models/test_{module}_xdm.py`
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

Tests mirror source structure with mock XML:

```
src/eb_model/tests/
├── parser/
│   └── test_{module}_xdm_parser.py    # Parser unit tests
└── models/
    └── test_{module}_xdm.py            # Model unit tests
```

### Test Patterns

- **Parser tests**: Mock XML with namespaces, test each `read_*()` method
- **Model tests**: Initialization, getter/setter, fluent interface
- Test XML structure matches XDM format with proper namespaces

### Mock XML Example

```python
xml_content = """
<datamodel version="8.0"
        xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
        xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
        xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
        xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
    <d:ctr name="{Module}General" type="IDENTIFIABLE">
        <d:var name="{Module}DevErrorDetect" type="BOOLEAN" value="true"/>
    </d:ctr>
</datamodel>
"""
```

## Code Conventions

- **Classes**: PascalCase (`EcucObject`, `CryptoXdmParser`, `SecOC`)
- **Methods**: camelCase (`getName()`, `read_value()`, `findCtrTag()`)
- **Properties/Attributes**: camelCase (`name`, `parent`, `nsmap`)
- **Constants**: UPPER_CASE
- **Fluent interface**: Setter methods return `self` for chaining
- **Module naming**: Use AUTOSAR convention (e.g., `SecOC`, `J1939Nm`)

### SWR/TC Naming

- SWR: `SWR_<MODULE>_00001` (uppercase module name)
- TC: `TC_<MODULE>_001` (uppercase module name)

## Implementation Order

1. **Infrastructure updates**
   - `eb_parser_factory.py`
   - `eb_doc.py`
   - `__init__.py` files
   - `pyproject.toml`

2. **Security modules** (5 modules)
   - Crypto
   - CryIf
   - Csm
   - SecOC
   - FiM

3. **Diagnostics modules** (3 modules)
   - Dcm
   - Dem
   - Dlt

4. **J1939 modules** (4 modules)
   - J1939Dcm
   - J1939Nm
   - J1939Rm
   - J1939Tp

For each module (per module order):
1. Parser → Model → Reporter → CLI → Parser Test → Model Test → Requirements → Test Cases

## Success Criteria

- [ ] All 15 parsers created and parse XDM files correctly
- [ ] All 30 test files created (15 parser + 15 model tests)
- [ ] All 15 SW requirements documents created
- [ ] All 15 test case documents created
- [ ] All 15 CLI commands functional
- [ ] All 15 Excel exports working
- [ ] Code passes linting (ruff)
- [ ] CI tests pass
- [ ] Requirements traceability in code docstrings
- [ ] PR reviewed and approved

## Estimated Timeline

- **Infrastructure updates**: 1-2 hours
- **Security modules (5)**: 2-3 hours per module
- **Diagnostics modules (3)**: 2-3 hours per module
- **J1939 modules (4)**: 2-3 hours per module

**Total**: 25-40 hours for all 15 modules

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Module complexity varies widely | Start with simpler modules to establish patterns |
| XDM format inconsistencies | Comprehensive test coverage with mock XML |
| Breaking changes to existing code | Run full test suite on completion |
| Large PR review burden | Modular code structure aids review |
| Timeline slippage | Focus on core functionality first |

## References

- CLAUDE.md: Project instructions and conventions
- 2026-03-23-multi-module-xdm-parser-design.md: Tiered rollout design
- Existing module implementations (Tiers 1-5)
- docs/requirements/: SWR documents for existing modules