# CLI Usage

## eb-convert

The unified CLI command for converting EB Tresos XDM files to Excel format.

### Usage

```bash
eb-convert <input.xdm> [<input2.xdm> ...] <output_dir/> [options]
```

### Examples

```bash
# Convert a single file
eb-convert Os.xdm output/

# Convert multiple files
eb-convert Os.xdm NvM.xdm Rte.xdm output/

# With verbose logging
eb-convert --verbose Os.xdm output/

# With file logging
eb-convert --log conversion.log Os.xdm output/

# OS-specific options
eb-convert --skip-os-task Os.xdm output/
```

### Options

- `-v, --verbose`: Enable verbose (DEBUG) logging
- `--log LOG`: Log file path for file-based logging
- `--skip-os-task`: Skip generating Os task (OS module only)

### Auto-Detection

The CLI automatically detects the module type from the XDM file's MODULE-CONFIGURATION tag.
You don't need to specify the module name - it's extracted from the file itself.

### Output

For each input file, an Excel file is generated in the output directory named after the module:
- `Os.xdm` → `output/Os.xlsx`
- `NvM.xdm` → `output/NvM.xlsx`
- etc.

## Legacy Commands

The following legacy commands are still available but deprecated:
- `os-xdm-xlsx`
- `nvm-xdm-xlsx`
- `rte-xdm-xlsx`
- ... (52 more)

Please migrate to `eb-convert` for new usage.

## model-xdm-generator

Generate model (instance) XDM files from schema XDM files for testing.

### Usage

```bash
model-xdm-generator <schema.xdm> -o <output.xdm> [options]
```

### Examples

```bash
# Generate with combined variant (default)
model-xdm-generator doc/canif/schema/CanIf.xdm -o CanIf_model.xdm

# Generate with specific variant
model-xdm-generator doc/os/schema/Os.xdm -o Os_model.xdm --variant boundary

# Generate with seeded random values
model-xdm-generator doc/canif/schema/CanIf.xdm -o CanIf_random.xdm --variant random --seed 42

# Override list entry count
model-xdm-generator doc/os/schema/Os.xdm -o Os_model.xdm --list-entries 5
```

### Options

- `-o, --output OUTPUT`: Output path for the generated model XDM file (required)
- `--variant {combined,defaults,boundary,random}`: Value generation variant (default: combined)
- `--seed SEED`: Random seed for reproducible output (used with `--variant random` or `--variant combined`)
- `--list-entries LIST_ENTRIES`: Number of entries per list (overrides MIN from schema)

### Variants

- **combined** (default): Generates comprehensive test data cycling through defaults, boundary, and random values. Includes all choice options and optional items with ENABLE attributes.
- **defaults**: Uses DEFAULT values from schema, or type-specific defaults if not specified
- **boundary**: Uses boundary values (min/max, edge cases) for comprehensive testing
- **random**: Uses random values within RANGE constraints (use `--seed` for reproducibility)

### Output

The generated model XDM file contains:
- Complete XDM structure matching the schema
- Generated values for all variables based on the selected variant
- Mock references for all REFERENCE types
- Multiple list entries to verify multiplicity (2 for min=0, min+2 for min>0)
- ENABLE attributes on all items (combined variant only)