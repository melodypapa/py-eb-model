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

Cycles through defaults, boundary, and random strategies per element using `idx % 3`: index 0 uses defaults, 1 uses boundary, 2 uses random, then repeats. Enables all optional elements.

```bash
model-xdm-generator Os.xdm -o Os_combined.xdm --variant combined
```

**Characteristics:**
- Comprehensive coverage in single file
- Activates optional elements (adds `ENABLE=true`)
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
| REFERENCE | mock ASPath from REF attr | mock ASPath | mock ASPath |

### Reference Types

References are generated as ASPath strings derived from the schema's `REF` data attribute. The generator strips the `ASPathDataOfSchema:` prefix and rewrites as `ASPath:`:

```
ASPath:/AUTOSAR/EcucDefs/<Module>/<Container>/<Element>
```

Example: `ASPath:/AUTOSAR/EcucDefs/Os/OsCounter`

### List Handling

Lists are populated with multiple entries. Without `--list-entries`, the generator uses schema multiplicity:
- `MIN == 0` → 2 entries (basic coverage)
- `MIN > 0` → `max(MIN + 2, 3)` entries (capped at MAX if set)

```bash
# Override list size
model-xdm-generator Os.xdm -o Os_3tasks.xdm --list-entries 3
```

List entry naming follows schema convention:
- If schema defines `NAME_PATTERN`: pattern with `?` replaced by index
- Otherwise: `<childName>_<index>` (e.g., `OsTask_0`, `OsTask_1`)

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

## Related Documentation

- [Schema→Model XDM Mapping Rules](xdm-mapping-rules.md)
- [Generator Quick Start](../getting-started/generator-quickstart.md)
- [CLI Reference](../usage/cli.md)
- [API Documentation](../api/modules.html)
- [Examples](../examples/)