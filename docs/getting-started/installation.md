# Installation

## Requirements

- Python 3.9 or higher
- pip package manager

## Install from PyPI

```bash
pip install eb-model
```

## Development Install

For contributing or running from source:

```bash
git clone https://github.com/melodypapa/py-eb-model.git
cd py-eb-model
pip install -e .
```

## Verify Installation

Test the installation:

```bash
# Test unified CLI
eb-convert --help

# Test specific module CLI
os-xdm-xlsx --help

# Test generator
model-xdm-generator --help
```

## Dependencies

Runtime dependencies are installed automatically:
- openpyxl - Excel file support

Development dependencies (for testing):
- pytest
- ruff
- mypy

## Troubleshooting

### Python version error

If you see "Python version too old", ensure you're using Python 3.9+:

```bash
python --version
```

### Command not found

If `eb-convert` is not found, try:

```bash
python -m eb_model.cli.eb_convert --help
```

Or reinstall:

```bash
pip install --force-reinstall eb-model
```