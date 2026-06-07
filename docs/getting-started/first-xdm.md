# Your First XDM Conversion

This guide walks through converting your first EB Tresos XDM file to Excel.

## Prerequisites

1. Have an EB Tresos XDM file (e.g., `Os.xdm`)
2. eb-model installed (see [Installation](installation.md))

## Step 1: Locate Your XDM File

EB Tresos exports XDM files from your project. Find them in your project's configuration directory.

Common locations:
- `MyProject/Config/Os.xdm`
- `MyProject/Generated/Os.xdm`

## Step 2: Run the Conversion

Use the unified `eb-convert` command:

```bash
eb-convert Os.xdm output/
```

This creates `output/Os.xlsx` with all OS configuration data.

## Step 3: Understand the Output

Open `Os.xlsx`. You'll see:

- **General**: OS version, API settings, hooks
- **Tasks**: All task configurations (priority, stack, autostart)
- **ISRs**: ISR configurations
- **Resources**: Resource management
- **Counters**: OS counters
- **Alarms**: Alarm configurations
- **Events**: OS events

Each sheet contains:
- **Name**: Element name from XDM
- **Value**: Configuration value
- **Attribute**: Additional metadata (ENABLE, IMPORTER_INFO)

## Step 4: Verify Key Data

Check that critical data is present:

1. Task priorities are correct
2. ISR names match your ISRs
3. Resource references are resolved

## Common Issues

### Empty Output

**Cause**: ENABLE attribute filtering

Some XDM elements have `ENABLE="false"`. These are skipped by default.

**Solution**: Check if expected elements have `ENABLE="true"` in the XDM.

### Namespace Errors

**Cause**: Invalid XDM format

**Solution**: Ensure the XDM file was exported by EB Tresos, not hand-edited.

### Missing Values

**Cause**: Calculated values using `@CALC()` syntax

**Solution**: These are shown as-is. The actual value depends on your EB Tresos project configuration.

## Next Steps

- Explore other modules: `eb-convert NvM.xdm output/`
- Learn [concepts](concepts.md)
- Try the [model-xdm-generator](generator-quickstart.md)