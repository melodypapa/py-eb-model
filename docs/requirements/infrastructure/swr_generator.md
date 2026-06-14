# Software Requirements: XDM Model Generator

## Document Information
| Item | Value |
|------|-------|
| Module | Generator |
| Stack | infrastructure |
| Abbreviation | GEN |
| Generated From | CanIf.xdm, Os.xdm |
| Generation Date | 2026-06-07 |

## Overview

The XDM Model Generator produces model (instance) XDM files from schema XDM files for testing. It reads schema definitions (`v:` prefix nodes) and generates configuration instances (`d:` prefix nodes) with pluggable value generation strategies.

## Requirements

### SWR_GEN_00001 - Schema Model Dataclasses

Define Python dataclasses representing XDM schema node structure for type-safe schema traversal.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| SchemaRange | [1] | dataclass | RANGE constraints (min/max values, enum values, regex) | XDM Spec 5.1.6.4 |
| SchemaVar | [1] | dataclass | Schema variable definition with name, type, default, range | XDM Spec 5.1.6.4 |
| SchemaCtr | [1] | dataclass | Schema container with children list | XDM Spec 5.1.6.1 |
| SchemaLst | [1] | dataclass | Schema list with MAP/empty type, MIN/MAX entries | XDM Spec 5.1.6.3 |
| SchemaRef | [1] | dataclass | Schema reference with REF and RANGE targets | XDM Spec 5.1.6.5 |
| SchemaChc | [1] | dataclass | Schema choice with alternative containers | XDM Spec 5.1.6.2 |
| SchemaRoot | [1] | dataclass | Root holding module name, version, namespaces, module_def | XDM Spec 5.1.2 |

**Implementation:** `generator/schema_model.py`
**Status:** Implemented
**Last Validated:** 2026-06-07

---

### SWR_GEN_00002 - Schema Parser

Parse XDM schema files containing `v:` prefix nodes and build SchemaRoot model tree. Handle dynamic namespace resolution for different XDM versions (DataModel2/08, DataModel2/16).

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| parse() | [1] | method | Parse schema XDM root element into SchemaRoot | XDM Spec 5.1.6 |
| _parse_var() | [0..*] | method | Parse v:var with DEFAULT, RANGE, LABEL extraction | XDM Spec 5.1.6.4 |
| _parse_ctr() | [0..*] | method | Parse v:ctr with recursive child parsing | XDM Spec 5.1.6.1 |
| _parse_lst() | [0..*] | method | Parse v:lst with MIN/MAX and child schema | XDM Spec 5.1.6.3 |
| _parse_ref() | [0..*] | method | Parse v:ref with REF and RANGE target extraction | XDM Spec 5.1.6.5 |
| _parse_chc() | [0..*] | method | Parse v:chc with choice container extraction | XDM Spec 5.1.6.2 |
| _extract_namespaces() | [1] | method | Extract d:, v:, a: namespace URIs from element tree | XDM Spec 5.1.2 |
| _parse_range() | [0..*] | method | Parse RANGE attribute (numeric, enum, regex) | XDM Spec 5.1.4.3 |

**Implementation:** `generator/schema_parser.py`
**Status:** Implemented
**Last Validated:** 2026-06-07

---

### SWR_GEN_00003 - Value Generation Strategies

Provide pluggable strategies for generating configuration values from schema metadata.

| Strategy | Description |
| --- | --- |
| DefaultsStrategy | Use DEFAULT attribute values from schema; type-specific fallbacks |
| BoundaryStrategy | Generate boundary values (min from RANGE, true for BOOLEAN) |
| RandomStrategy | Seeded random values within RANGE constraints |
| CombinedStrategy | Cycle through defaults/boundary/random per element (idx % 3); activates optional elements via ENABLE=true |

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| generateValue() | [1] | method | Generate value for SchemaVar based on strategy | Design Spec |
| generateRefValue() | [1] | method | Generate mock ASPath reference for SchemaRef | Design Spec |
| seed | [0..1] | int | Random seed for reproducible RandomStrategy/CombinedStrategy output | Design Spec |

**Value Fallback Rules (no DEFAULT):**

| Type | Fallback |
| --- | --- |
| BOOLEAN | `false` |
| INTEGER | `0` |
| FLOAT | `0.0` |
| STRING | `""` |
| MULTILINE-STRING | `""` |
| ENUMERATION | First value from RANGE, else `""` |
| FUNCTION-NAME | `""` |
| LINKER-SYMBOL | `""` |
| REFERENCE | Mock ASPath from REF attr, else empty (no value) |

**Implementation:** `generator/strategies.py`
**Status:** Implemented
**Last Validated:** 2026-06-07

---

### SWR_GEN_00004 - Data Generator

Convert schema model tree into `d:` prefix element tree following XDM data-node structure (XDM Spec 5.1.7). Produce valid XML with proper namespace declarations.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| generate() | [1] | method | Generate complete model XDM ElementTree from SchemaRoot | XDM Spec 5.1.7 |
| toString() | [1] | method | Serialize ElementTree to XML string with xmlns declarations | XDM Spec 5.1.2 |
| _generate_var() | [0..*] | method | Generate d:var element with value from strategy; CombinedStrategy adds ENABLE=true | XDM Spec 5.1.7.4 |
| _generate_ctr() | [0..*] | method | Generate d:ctr element with children; CombinedStrategy adds ENABLE=true | XDM Spec 5.1.7.1 |
| _generate_lst() | [0..*] | method | Generate d:lst with MIN entries, unique names | XDM Spec 5.1.7.3 |
| _generate_ref() | [0..*] | method | Generate d:ref with mock ASPath value; CombinedStrategy adds ENABLE=true | XDM Spec 5.1.7.5 |
| _generate_chc() | [0..*] | method | Generate d:chc with value=selected choice name. Non-combined: first choice only; CombinedStrategy: all choices as separate d:chc elements | XDM Spec 5.1.7.2 |

**Output Wrapper Structure:**
```
datamodel → d:ctr(AUTOSAR) → d:lst(TOP-LEVEL-PACKAGES) → d:ctr(AR-PACKAGE)
→ d:lst(ELEMENTS) → d:chc(MODULE-CONFIGURATION) → d:ctr(MODULE-CONFIGURATION)
```

**Implementation:** `generator/data_generator.py`
**Status:** Implemented
**Last Validated:** 2026-06-07

---

### SWR_GEN_00005 - CLI Entry Point

Command-line interface for the XDM model generator tool.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| input | [1] | positional | Path to schema XDM file | CLI Design |
| --output / -o | [1] | option | Output path for generated model XDM | CLI Design |
| --variant | [0..1] | option | Value generation variant: combined/defaults/boundary/random (default: combined) | CLI Design |
| --seed | [0..1] | option | Random seed for reproducible output | CLI Design |
| --list-entries | [0..1] | option | Override MIN entries per list | CLI Design |

**Entry Point:** `model-xdm-generator` in `pyproject.toml`
**Implementation:** `generator/cli.py`
**Status:** Implemented
**Last Validated:** 2026-06-07

---

### SWR_GEN_00006 - eb-convert Verification

Generated model XDM files must be detectable by the existing `eb-convert` tool. Module name must be correctly identified from the generated XDM structure.

| Field | Multiplicity | Type | Description | Origin |
| --- | --- | --- | --- | --- |
| Module detection | [1] | verification | eb-convert detects correct module name from generated XDM | Design Spec |
| Namespace readability | [1] | verification | Generated xmlns declarations readable via ET.iterparse start-ns | XDM Spec 5.1.2 |
| Valid XML | [1] | verification | Output parses without error with ET.parse | Design Spec |
| Multi-variant | [1] | verification | All four variants produce valid XML | Design Spec |

**Implementation:** `tests/generator/test_eb_convert_verification.py`
**Status:** Implemented
**Last Validated:** 2026-06-07
