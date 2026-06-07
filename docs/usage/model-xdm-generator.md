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
| `--variant` | Value generation variant | defaults |
| `--seed` | Random seed for reproducibility | None |
| `--list-entries` | Number of entries for lists | 5 |
| `--verbose` | Enable verbose logging | False |

### Variants

The generator supports three value generation strategies:

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

## Value Generation Rules

### Primitive Types

| Type | Defaults | Boundary | Random |
|------|----------|----------|--------|
| BOOLEAN | false | true/false | random |
| INTEGER | 0 | min/max | random in range |
| FLOAT | 0.0 | min/max | random in range |
| STRING | "" | max length | random string |
| ENUMERATION | first value | all values | random choice |

### Reference Types

References are generated as valid ASPath strings:

```
/Module/Container/Element
```

Example: `/Os/OsTask/Task1`

### List Handling

Lists are populated with multiple entries:

```bash
# Generate 3 tasks
model-xdm-generator Os.xdm -o Os_3tasks.xdm --list-entries 3
```

List elements are named:
- `Element1`, `Element2`, `Element3`, ...

## Advanced Usage

### Custom Configuration

Create a configuration file for complex scenarios:

```json
{
  "variant": "combined",
  "list_entries": {
    "OsTask": 10,
    "OsIsr": 5,
    "OsAlarm": 8
  },
  "value_overrides": {
    "OsTaskPriority": 5,
    "OsIsrPriority": 2
  }
}
```

Use it:

```bash
model-xdm-generator Os.xdm -o Os_custom.xdm --config generator_config.json
```

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
    parser = OsXdmParser()
    return parser.parse(str(output))

def test_os_tasks(os_test_model):
    """Test OS task parsing"""
    tasks = os_test_model.getOsTasks()
    assert len(tasks) > 0
```

## Troubleshooting

### Schema Not Found

**Error**: `Schema XDM file not found`

**Solution**: Ensure the schema file path is correct and the file exists.

### Invalid Schema Format

**Error**: `Invalid XDM schema format`

**Solution**: Verify the schema XDM was exported by EB Tresos and contains proper schema definitions.

### Output Permission Denied

**Error**: `Permission denied: output.xdm`

**Solution**: Check write permissions for the output directory.

### Missing Dependencies

**Error**: `ModuleNotFoundError: No module named 'eb_model'`

**Solution**: Install eb-model:

```bash
pip install eb-model
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

Use the generator programmatically:

```python
from eb_model.cli.model_xdm_generator import XdmModelGenerator

generator = XdmModelGenerator()

# Generate with defaults
generator.generate(
    schema_path="Os.xdm",
    output_path="Os_model.xdm",
    variant="defaults"
)

# Generate with custom config
generator.generate(
    schema_path="Os.xdm",
    output_path="Os_custom.xdm",
    variant="combined",
    list_entries=10,
    seed=42
)
```

### Configuration API

Create custom configurations:

```python
from eb_model.cli.model_xdm_generator import GeneratorConfig

config = GeneratorConfig(
    variant="combined",
    list_entries={
        "OsTask": 5,
        "OsIsr": 3
    },
    value_overrides={
        "OsTaskPriority": 10
    }
)

generator.generate_with_config(
    schema_path="Os.xdm",
    output_path="Os_custom.xdm",
    config=config
)
```

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

- [Generator Quick Start](../getting-started/generator-quickstart.md)
- [CLI Reference](../usage/cli.md)
- [API Documentation](../api/modules.html)
- [Examples](../examples/)