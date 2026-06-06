# XDM Model Generator Design

Generate AUTOSAR model (instance) XDM files from schema XDM files for testing purposes.

## Problem

Only 5 integration test XDM files exist (Rte, EthIf, MemIf). Creating test data manually is tedious. The codebase has 50+ parsers but limited test coverage with real XDM data.

## Solution

A CLI tool that reads a schema XDM (defines parameter structure with `v:` prefix nodes) and produces a model XDM (contains actual configuration values with `d:` prefix nodes) in multiple variants.

## Architecture

```
schema XDM → [SchemaParser] → [Schema Model] → [DataGenerator] → model XDM
                                        ↑
                                  [Variant Strategy]
                                  (defaults/boundary/random)
```

### Components

1. **SchemaParser** (`schema_parser.py`) — Reads `v:` nodes from schema XDM using `ElementTree`. Extracts metadata (names, types, defaults, ranges, ENABLE conditions) into schema model objects. Namespace handling follows `AbstractEbModelParser` pattern.

2. **Schema Model** (`schema_model.py`) — Python dataclasses representing schema structure:
   - `SchemaVar`: name, type (BOOLEAN/INTEGER/FLOAT/STRING/ENUMERATION/FUNCTION-NAME), default value, range constraints, editable condition
   - `SchemaCtr`: name, type, child schemas, multiplicity
   - `SchemaLst`: name, type (MAP or empty), min/max entries, child schema
   - `SchemaRef`: name, ref target paths, range constraints
   - `SchemaChc`: name, value, child container schemas
   - `SchemaRoot`: top-level container holding the schema tree

3. **DataGenerator** (`data_generator.py`) — Takes schema model + variant strategy, produces `d:` element tree with proper namespace handling. Generates mock ASPath references and appropriate list entries.

4. **Strategies** (`strategies.py`) — Three value generation strategies:
   - `DefaultsStrategy`: Use DEFAULT attribute values from schema
   - `BoundaryStrategy`: Min/max range boundaries, edge values per type
   - `RandomStrategy`: Random valid values within RANGE constraints (seeded for reproducibility)

5. **CLI** (`cli.py`) — argparse-based entry point.

## Value Generation Rules

### Per-Type Defaults Fallback (when no DEFAULT attribute)

| Type | Fallback |
|---|---|
| BOOLEAN | `false` |
| INTEGER | `0` |
| FLOAT | `0.0` |
| STRING | `""` |
| ENUMERATION | First value from RANGE |
| FUNCTION-NAME | `""` |
| REFERENCE | empty (no value) |

### Variant Strategy Rules

| Schema Type | Defaults | Boundary | Random |
|---|---|---|---|
| BOOLEAN | DEFAULT attr | `true` | random bool |
| INTEGER | DEFAULT attr | `0`, min from RANGE, max from RANGE | random int in [min,max] |
| FLOAT | DEFAULT attr | `0.0`, min, max | random float in range |
| STRING | DEFAULT attr | `""`, short test string | random alphanumeric |
| ENUMERATION | DEFAULT attr | each RANGE value iterated | random from RANGE |
| FUNCTION-NAME | DEFAULT attr | placeholder `Func_<name>` | random function name |
| REFERENCE | mock ASPath from REF attr | mock ASPath | mock ASPath |

### RANGE Attribute Parsing

RANGE values determine valid value boundaries:
- Numeric ranges: `<value>-<value>`, `<<value>`, `<=<value>`, `><value>`, `>=<value>` — extract min/max bounds
- Enum ranges: list of string values — valid value set
- Regex ranges (STRING): `~<pattern>` — not used for generation, fallback to default
- BOOLEAN ranges: first value = true, second = false (defaults: `TRUE`/`FALSE`)

### List Generation

- Generate `min` entries (from MIN data attribute) for each `v:lst`
- Entry names use `NAME_PATTERN` if present, otherwise `<listName>_<index>`
- MAP-type lists generate `d:ctr` entries with unique names
- Empty-type lists generate `d:var` or `d:ref` entries

### Reference Generation

- Extract target paths from `REF` data attribute (ASPath format)
- Generate mock ASPath using the target path pattern
- Example: `REF="ASPathDataOfSchema:/AUTOSAR/CanIf/Container/Int"` → generates `value="ASPath:/CanIf/Container/Int_0"`

### ENABLE Handling

- Schema nodes with ENABLE data attributes → generate `<a:a name="ENABLE" value="true"/>` by default
- Cannot evaluate dynamic XPath expressions at generation time — default to enabled
- Optionally accept a config to disable specific containers

## File Structure

```
src/eb_model/
├── generator/
│   ├── __init__.py
│   ├── cli.py              # CLI entry point
│   ├── schema_parser.py    # Parse v: nodes → Schema Model
│   ├── schema_model.py     # Schema dataclasses
│   ├── data_generator.py   # Schema Model → d: element tree
│   └── strategies.py       # Variant strategies
```

## CLI Interface

```bash
# Generate with defaults variant
model-xdm-generator schema.xdm -o model.xdm

# Specify variant
model-xdm-generator schema.xdm -o model.xdm --variant boundary

# Control list entries (overrides MIN)
model-xdm-generator schema.xdm -o model.xdm --list-entries 3

# Seed for reproducible random variant
model-xdm-generator schema.xdm -o model.xdm --variant random --seed 42
```

**Entry point in `pyproject.toml`:**
```
'model-xdm-generator = "eb_model.generator.cli:main"'
```

## Namespace Handling

Schema XDM uses these namespaces (consistent across files):
```xml
xmlns="http://www.tresos.de/_projects/DataModel2/16/root.xsd"
xmlns:a="http://www.tresos.de/_projects/DataModel2/16/attribute.xsd"
xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd"
```

Schema nodes use `v:` prefix, generated data nodes use `d:` prefix. The generator reads namespaces dynamically from input file.

## Output XDM Structure

Generated model XDM follows the same wrapper structure as the model CanIf.xdm example:

```xml
<?xml version='1.0'?>
<datamodel version="7.0"
           xmlns="http://www.tresos.de/_projects/DataModel2/16/root.xsd"
           xmlns:a="http://www.tresos.de/_projects/DataModel2/16/attribute.xsd"
           xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
           xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
  <d:ctr type="AUTOSAR" factory="autosar"
         xmlns:ad="..." xmlns:ce="..." xmlns:cd="..."
         xmlns:f="..." xmlns:icc="..." xmlns:mt="..."
         xmlns:variant="...">
    <d:lst type="TOP-LEVEL-PACKAGES">
      <d:ctr name="<ModuleName>" type="AR-PACKAGE">
        <d:lst type="ELEMENTS">
          <d:chc name="<ModuleName>" type="AR-ELEMENT" value="MODULE-CONFIGURATION">
            <d:ctr type="MODULE-CONFIGURATION">
              <!-- generated d:var, d:ctr, d:lst, d:ref, d:chc nodes -->
            </d:ctr>
          </d:chc>
        </d:lst>
      </d:ctr>
    </d:lst>
  </d:ctr>
</datamodel>
```

The wrapper structure (`TOP-LEVEL-PACKAGES` → `AR-PACKAGE` → `ELEMENTS` → `MODULE-CONFIGURATION`) is fixed. The module name is extracted from the schema's `d:chc` name attribute.

## Code Style

- Follow existing codebase conventions: camelCase for methods/properties
- Use `ElementTree` for XML processing (no new dependencies)
- Google-style docstrings with `Implements: SWR_*` references
- Type hints on all public methods
- Logging via `logging.getLogger()`

## Dependencies

No new runtime dependencies. Uses only:
- `xml.etree.ElementTree` (stdlib)
- `argparse` (stdlib)
- `dataclasses` (stdlib, Python 3.9+)
- `random` (stdlib)
- `re` (stdlib)

## Testing

- Unit tests for SchemaParser with mock schema XML fragments
- Unit tests for each variant strategy (value generation per type)
- Unit tests for DataGenerator (schema model → element tree)
- Integration test: generate model from CanIf schema, verify parsers can read it
- Integration test: generate model → parse with `CanIfXdmParser` → verify model populated

## Verification with eb-convert

The generated model XDM must be parseable by the existing `eb-convert` CLI tool. This serves as end-to-end validation:

### CanIf Verification

```bash
# Generate model from CanIf schema
model-xdm-generator doc/canif/schema/CanIf.xdm -o /tmp/CanIf_generated.xdm --variant defaults

# Verify eb-convert can parse it
eb-convert /tmp/CanIf_generated.xdm -o /tmp/CanIf_output.xlsx

# Verify with boundary variant
model-xdm-generator doc/canif/schema/CanIf.xdm -o /tmp/CanIf_boundary.xdm --variant boundary
eb-convert /tmp/CanIf_boundary.xdm -o /tmp/CanIf_boundary_output.xlsx
```

### Os Verification

```bash
# Generate model from Os schema
model-xdm-generator doc/os/schema/Os.xdm -o /tmp/Os_generated.xdm --variant defaults

# Verify eb-convert can parse it
eb-convert /tmp/Os_generated.xdm -o /tmp/Os_output.xlsx
```

### Automated Verification Test

Integration test that:
1. Generates model XDM from each available schema (CanIf, Os)
2. Runs `eb-convert` on generated XDM
3. Asserts exit code 0 (successful parse)
4. Asserts output Excel file is non-empty
5. Runs all three variants (defaults, boundary, random)
