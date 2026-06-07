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