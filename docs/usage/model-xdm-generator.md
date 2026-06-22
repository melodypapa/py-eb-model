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

## Output Format Principles

Authentic EB Tresos config files under `doc/config/` (e.g. `Os.xdm`, `CanIf.xdm`) are the canonical XDM format. Generated output matches this format in every aspect **except concrete data values**. Data values legitimately differ because the generator cannot know real ECU topology.

### Aspects that align with `doc/config`

| Aspect | Alignment |
|---|---|
| `<datamodel version>` | Always `7.0`, regardless of schema source version |
| Namespace URIs | Always `DataModel2/16/*` set (root, attribute, schema, data) |
| `xmlns:*` declarations on `<datamodel>` root | Full set per config style |
| `<a:a name="IMPORTER_INFO" value="@DEF"/>` | Emitted on elements whose value came from schema `DEFAULT` |
| `<a:a name="ENABLE" value="false"/>` format | Always `<a:a>` tag in output (never `<a:da>`, which is schema-side only) |
| Element ordering within `MODULE-CONFIGURATION` | Preserved from schema source, which should match config layout (see [Element Ordering](#element-ordering)) |

### Aspects that legitimately differ

| Aspect | Reason |
|---|---|
| Container `<d:ctr name="...">` | Generator uses indexed names (`OsAlarm_0`, `OsTask_1`); authentic config uses ECU-specific names (`HOH_0_EcuTestNode`) |
| Concrete values | Strategy-driven (`defaults` / `boundary` / `random` / `combined`) |
| `<d:ref value="...">` cross-module targets | Generator cannot know ECU topology. Refs whose schema `REF` points to a definition path (`AUTOSAR/EcucDefs/...`) are emitted without a `value` attribute |
| `IMPORTER_INFO` variants other than `@DEF` | `@CALC`, `@REC`, `ImportEcuConfig` are EB Tresos runtime artifacts that depend on real ECU state; generator never emits them |

## Command Line Interface

### Basic Usage

```bash
model-xdm-generator <schema_xdm> -o <output_xdm>
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-o, --output` | Output file path | Required |
| `--variant` | Value generation variant | combined |
| `--seed` | Random seed for reproducibility | None |
| `--list-entries` | Number of entries per list (overrides MIN) | None |

### Variants

The generator supports four value generation strategies:

#### 1. Defaults Variant

Uses default values from schema definitions:

```bash
model-xdm-generator Os.xdm -o Os_defaults.xdm --variant defaults
```

**Characteristics:**
- Safe, predictable values
- Matches EB Tresos defaults
- Good for baseline testing

#### 2. Boundary Variant

Uses boundary values (min/max) from schema constraints:

```bash
model-xdm-generator Os.xdm -o Os_boundary.xdm --variant boundary
```

**Characteristics:**
- Tests edge cases
- Validates constraint handling
- Good for stress testing

#### 3. Random Variant

Uses random values within constraints:

```bash
model-xdm-generator Os.xdm -o Os_random.xdm --variant random --seed 42
```

**Characteristics:**
- Diverse test coverage
- Reproducible with seed
- Good for discovering bugs

#### 4. Combined Variant (default)

Cycles through defaults, boundary, and random strategies per element using `idx % 3`: index 0 uses defaults, 1 uses boundary, 2 uses random, then repeats. Activates optional elements.

```bash
model-xdm-generator Os.xdm -o Os_combined.xdm --variant combined
```

**Characteristics:**
- Comprehensive coverage in single file
- Activates optional elements (adds `ENABLE=true` only to elements marked optional via `<a:a name="OPTIONAL" value="true"/>` or wrapped in list with `MIN=0 MAX=1` — see [Optional Elements](#optional-elements))
- Default variant when `--variant` omitted

## Value Generation Rules

### Primitive Types

| Type | Defaults | Boundary | Random |
|------|----------|----------|--------|
| BOOLEAN | DEFAULT attr or false | true | random |
| INTEGER | DEFAULT attr or 0 | min from RANGE | random in range |
| FLOAT | DEFAULT attr or 0.0 | min from RANGE | random in range |
| STRING | DEFAULT attr or "" | "" | random alphanumeric |
| MULTILINE-STRING | DEFAULT attr or "" | "" | random alphanumeric |
| ENUMERATION | DEFAULT attr or first RANGE value | first RANGE value | random from RANGE |
| FUNCTION-NAME | DEFAULT attr or "" | `Func_<name>` | `<prefix>_<name>` |
| LINKER-SYMBOL | DEFAULT attr or "" | `Func_<name>` | `<prefix>_<name>` |
| REFERENCE | empty or mock ASPath (see [Reference Types](#reference-types)) | empty or mock ASPath | empty or mock ASPath |

### Reference Types

Authentic config references point to real cross-module paths populated by EB Tresos from ECU topology (e.g. `ASPath:/Can/Can/CanConfigSet`, `ASPath:/EcuC/EcuC/EcucPduCollection/Pdu_CounterIn_256R`). The generator cannot know this topology, so reference handling follows this rule:

- **Schema `REF` attribute points to a definition path** (contains `AUTOSAR/EcucDefs/`, e.g. `ASPathDataOfSchema:/AUTOSAR/EcucDefs/Os/OsCounter`) → generator emits `<d:ref name="..." type="REFERENCE"/>` with **no** `value` attribute. This mirrors how authentic config marks unbound references (e.g. `CanIfHrhCanHandleTypeRef` at `doc/config/CanIf.xdm:73-77`).
- **Schema `REF` points to a concrete config path** (rare) → generator strips `ASPathDataOfSchema:` prefix and rewrites as `ASPath:`.

Emitted empty reference example (aligns with authentic style for unbound refs):

```xml
<d:ref name="OsAlarmCounterRef" type="REFERENCE" />
```

### List Handling

Lists are populated with multiple entries. Without `--list-entries`, the generator uses schema multiplicity:
- Optional singleton (`MIN=0`, `MAX=1`): handled per [Optional Elements](#optional-elements) below
- `MIN == 0` (non-singleton) → 2 entries (basic coverage)
- `MIN > 0` → `max(MIN + 2, 3)` entries (capped at MAX if set)

```bash
# Override list size
model-xdm-generator Os.xdm -o Os_3tasks.xdm --list-entries 3
```

List entry naming follows schema convention:
- If schema defines `NAME_PATTERN`: pattern with `?` replaced by index
- Otherwise: `<childName>_<index>` (e.g., `OsTask_0`, `OsTask_1`)

### Container Type Mapping

The generator applies schema-to-data node type rules from [XDM Mapping Rules](xdm-mapping-rules.md). See also [Output Format Principles](#output-format-principles) for overall alignment requirements.

- **`v:ctr type="MULTIPLE-CONFIGURATION-CONTAINER"`**: standalone occurrences are auto-wrapped in `d:lst` (per XDM Spec 5.2.5). When schema already wraps the container in `v:lst`, generator honors the existing wrap.
- **`v:ctr type="INSTANCE"`**: preserves `TARGET` and `CONTEXT` data attributes, emitting them as `a:da` children on the `d:ctr`.
- **`v:var` with `<a:a name="DERIVED" value="true"/>`**: emits matching `<a:a name="DERIVED" value="true"/>` on the `d:var`.
- **Multiplicity auto-wrap** (XDM Spec 5.2.5): any `v:var`, `v:ctr`, or `v:ref` carrying `LOWER-MULTIPLICITY != 1` or `UPPER-MULTIPLICITY != 1` (without being inside a `v:lst`) is auto-wrapped in `d:lst` with the element's SHORT-NAME.
- **Choice type default**: when a `v:chc` element lacks a `type` attribute, generator infers from schema namespace — `DataModel2/08` namespaces default to `type="CHOICE"` (AUTOSAR 2.x style); all others default to `type="IDENTIFIABLE"` (AUTOSAR 3.x+).

### Optional Elements

Optional elements follow XDM Spec 5.2.5.1. Two schema representations are recognized:

- **New style**: `<a:a name="OPTIONAL" value="true"/>` plus `<a:da name="ENABLE" value="false"/>` on the element directly.
- **Old style**: element wrapped in `<v:lst>` with `<a:da name="MIN" value="0"/>` and `<a:da name="MAX" value="1"/>`.

In authentic config style, the output `ENABLE` attribute is always carried on the `<a:a>` tag (never `<a:da>`, which is schema-side only). Generator behavior by variant:

| Variant | Optional element output |
|---------|-------------------------|
| `combined` | Element populated, `<a:a name="ENABLE" value="true"/>` emitted |
| `defaults` / `boundary` / `random` | Element skipped, `<a:a name="ENABLE" value="false"/>` emitted (matches authentic config style for inactive optional elements) |

For non-optional elements, no `ENABLE` attribute is emitted.

### Schema Version and Namespaces

Generator output always declares the `DataModel2/16` namespace set on `<datamodel>`, regardless of what the schema source declares:

```xml
<datamodel version="7.0"
           xmlns="http://www.tresos.de/_projects/DataModel2/16/root.xsd"
           xmlns:a="http://www.tresos.de/_projects/DataModel2/16/attribute.xsd"
           xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
           xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
```

Some schema source files declare older versions (for example `doc/os/schema/Os.xdm` is `version="3.0"` with `DataModel2/08` URIs). The generator normalizes these to `7.0` / `DataModel2/16` on output so the generated file is byte-comparable to authentic config in all structural metadata.

The inner `<d:ctr type="AUTOSAR" factory="autosar">` in authentic config also carries additional `xmlns:ad|ce|cd|f|icc|mt|variant` declarations. The generator should emit these declarations when matching authentic layout exactly; they are unused if no child element references them, so absence is not a correctness issue.

### IMPORTER_INFO Emission

Authentic config carries `<a:a name="IMPORTER_INFO" value="..."/>` attributes tracking value origin. The generator emits only the subset it can soundly claim from schema information:

| Value | When emitted |
|---|---|
| `@DEF` | Element value equals the schema `DEFAULT` attribute (placed by `DefaultsStrategy`, or default fallback of other strategies) |
| `@CALC(...)` | Never — calculated values depend on real ECU state |
| `@REC` | Never — received-value marker is a Tresos runtime artifact |
| `ImportEcuConfig` | Never — set by EB Tresos during ECU config import |

Order of `<a:a>` children within `<d:var>` / `<d:ref>` / `<d:ctr>` (matching authentic config): `DEF` (root `MODULE-CONFIGURATION` only) → `ENABLE` → `IMPORTER_INFO`.

### Element Ordering

The generator preserves schema-declared child order. Schema source files must be maintained so their child order matches the corresponding `doc/config/<Module>.xdm` authentic layout — otherwise generated output will diverge in element ordering.

Example: in `doc/config/Os.xdm:23-74`, the top-level order within `MODULE-CONFIGURATION` is:

1. `POST_BUILD_VARIANT_USED`
2. `OsPeripheralArea`
3. `CommonPublishedInformation`
4. `PublishedInformation`
5. `IMPLEMENTATION_CONFIG_VARIANT`
6. `OsOS` (and remaining containers)

Schema source `doc/os/schema/Os.xdm` must declare `CommonPublishedInformation` and `PublishedInformation` near the top of the module definition (immediately after `POST_BUILD_VARIANT_USED`), not deep in the file. If a schema source is found to place containers in a different order than its authentic config counterpart, the schema source is the bug — fix the schema, not the generator.

## Advanced Usage

### Batch Generation

Generate multiple models for different scenarios:

```bash
# Generate defaults
model-xdm-generator Os.xdm -o Os_defaults.xdm --variant defaults

# Generate boundary
model-xdm-generator Os.xdm -o Os_boundary.xdm --variant boundary

# Generate random
model-xdm-generator Os.xdm -o Os_random.xdm --variant random --seed 42

# Generate combined (mix of all variants)
model-xdm-generator Os.xdm -o Os_combined.xdm --variant combined
```

### Integration with Testing

Use in pytest fixtures:

```python
import pytest
from eb_model.parser import OsXdmParser
from eb_model.models import EBModel

@pytest.fixture
def os_test_model(tmp_path):
    """Generate OS test model"""
    schema = "docs/Os.xdm"
    output = tmp_path / "Os_test.xdm"

    # Generate model
    import subprocess
    subprocess.run([
        "model-xdm-generator",
        schema,
        "-o", str(output),
        "--variant", "defaults"
    ])

    # Parse and return
    doc = EBModel.getInstance()
    parser = OsXdmParser()
    parser.parse_xdm(str(output), doc)
    return doc.find("/Os/Os")

def test_os_tasks(os_test_model):
    """Test OS task parsing"""
    tasks = os_test_model.getOsTasks()
    assert len(tasks) > 0
```

## Troubleshooting

### Schema Parse Error

**Error**: `Error parsing schema XDM: <details>`

**Cause**: Schema file missing, unreadable, or invalid XML.

**Solution**: Verify schema file path correct and file exists. Ensure schema XDM exported by EB Tresos with proper `v:` schema definitions.

### Output Write Error

**Error**: `Error writing output: <details>`

**Solution**: Check write permissions for output directory and path validity.

### Missing Dependencies

**Error**: `ModuleNotFoundError: No module named 'eb_model'`

**Solution**: Install py-eb-model:

```bash
pip install py-eb-model
```

## Best Practices

### 1. Use Seeds for Reproducibility

Always specify a seed for random variant in tests:

```bash
model-xdm-generator Os.xdm -o Os_test.xdm --variant random --seed 42
```

This ensures consistent test data across runs.

### 2. Validate Generated Models

Always parse and validate the generated model:

```bash
# Generate
model-xdm-generator Os.xdm -o Os_test.xdm

# Validate
eb-convert Os_test.xdm output/
```

### 3. Use Appropriate Variants

| Testing Level | Recommended Variant |
|---------------|---------------------|
| Unit tests | defaults |
| Integration tests | combined |
| Stress tests | boundary |
| Coverage tests | random |

### 4. Document Test Data Generation

Include generation parameters in test documentation:

```python
"""
Test OS task scheduling.

Generated using:
  model-xdm-generator Os.xdm -o Os_test.xdm --variant defaults --seed 42
"""
def test_os_scheduling():
    ...
```

## API Reference

### Python API

Use the generator programmatically via `SchemaParser` + `DataGenerator`:

```python
import xml.etree.ElementTree as ET
from eb_model.generator.schema_parser import SchemaParser
from eb_model.generator.data_generator import DataGenerator
from eb_model.generator.strategies import DefaultsStrategy, BoundaryStrategy, RandomStrategy, CombinedStrategy

# Parse schema XDM
tree = ET.parse("Os.xdm")
schema = SchemaParser().parse(tree.getroot())

# Generate model XDM
strategy = DefaultsStrategy()  # or BoundaryStrategy(), RandomStrategy(seed=42), CombinedStrategy(seed=42)
generator = DataGenerator(strategy=strategy, list_entries=None)
result_tree = generator.generate(schema)

# Serialize to string
xml_str = generator.toString(result_tree)

# Write to file
with open("Os_model.xdm", "w") as f:
    f.write(xml_str)
```

**Strategy classes** (`eb_model.generator.strategies`):
- `DefaultsStrategy()` — use DEFAULT attributes
- `BoundaryStrategy()` — min/max edge values
- `RandomStrategy(seed=42)` — random within RANGE
- `CombinedStrategy(seed=42)` — cycle through all three

## Examples

### Example 1: Basic Generation

```bash
# Simple generation
model-xdm-generator Os.xdm -o Os_model.xdm

# Convert to Excel
eb-convert Os_model.xdm output/

# View results
open output/Os.xlsx
```

### Example 2: Test Suite Generation

```bash
# Generate test suite
for module in Os CanIf NvM; do
    model-xdm-generator ${module}.xdm -o test_${module}.xdm --variant defaults
    eb-convert test_${module}.xdm test_output/
done
```

### Example 3: CI/CD Integration

```yaml
# .github/workflows/test.yml
- name: Generate Test Data
  run: |
    model-xdm-generator Os.xdm -o Os_test.xdm --variant defaults --seed 42
    model-xdm-generator CanIf.xdm -o CanIf_test.xdm --variant defaults --seed 42

- name: Run Tests
  run: |
    pytest tests/ --test-data-dir=test_data/
```

## Validation

Verify generator output conforms to the [Output Format Principles](#output-format-principles) after every schema or generator change:

```bash
# Regenerate test fixtures
bash scripts/generate_os_test_xdm.sh

# Structural header should match doc/config (version + namespaces)
diff <(head -10 doc/config/Os.xdm) <(head -10 tests/integration/data_files/generated/Os.xdm)
diff <(head -10 doc/config/CanIf.xdm) <(head -10 tests/integration/data_files/generated/CanIf.xdm)

# No AUTOSAR/EcucDefs definition paths in emitted ref values
grep -c 'AUTOSAR/EcucDefs' tests/integration/data_files/generated/*.xdm  # expect 0

# IMPORTER_INFO=@DEF should appear on defaulted elements
grep -c 'name="IMPORTER_INFO" value="@DEF"' tests/integration/data_files/generated/*.xdm  # expect > 0

# ENABLE attributes should use <a:a> tag, never <a:da>
grep -c '<a:da name="ENABLE"' tests/integration/data_files/generated/*.xdm  # expect 0
```

Round-trip validation: parse the generated XDM with the module parser and confirm no exceptions:

```bash
eb-convert tests/integration/data_files/generated/Os.xdm /tmp/os_check.xlsx
eb-convert tests/integration/data_files/generated/CanIf.xdm /tmp/canif_check.xlsx
```

## Related Documentation

- [Schema→Model XDM Mapping Rules](xdm-mapping-rules.md)
- [Generator Quick Start](../getting-started/generator-quickstart.md)
- [CLI Reference](../usage/cli.md)
- [API Documentation](../api/modules.html)
- [Examples](../examples/)