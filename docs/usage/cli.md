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