# Unit Test Cases

This directory contains ISO/IEC/IEEE 29119-3 compliant unit test case documentation for the py-eb-model project.

## Purpose

Unit tests verify individual components in isolation, testing specific methods, classes, or functions without dependencies on other system components.

## Organization

Each subdirectory corresponds to a module or layer:

| Directory | Description |
|-----------|-------------|
| `os/` | Operating System module unit tests |
| `rte/` | Runtime Environment module unit tests |
| `nvm/` | Non-Volatile Memory module unit tests |
| `ecuc/` | ECU Configuration module unit tests |
| `bswm/` | Basic Software Mode Manager unit tests |
| `canif/` | CAN Interface module unit tests |
| `cannm/` | CAN Network Management unit tests |
| `cansm/` | CAN State Manager unit tests |
| `cantp/` | CAN Transport Protocol unit tests |
| `linif/` | LIN Interface module unit tests |
| `linsm/` | LIN State Manager unit tests |
| `lintp/` | LIN Transport Protocol unit tests |
| `frif/` | FlexRay Interface module unit tests |
| `frnm/` | FlexRay Network Management unit tests |
| `frsm/` | FlexRay State Manager unit tests |
| `frtp/` | FlexRay Transport Protocol unit tests |
| `frartp/` | FlexRay AR Transport Protocol unit tests |
| `ethif/` | Ethernet Interface module unit tests |
| `ethsm/` | Ethernet State Manager unit tests |
| `doip/` | Diagnostics over IP unit tests |
| `soad/` | Socket Adapter unit tests |
| `someiptp/` | SOME/IP Transport Protocol unit tests |
| `tcpip/` | TCP/IP Stack unit tests |
| `udpnm/` | UDP Network Management unit tests |
| `det/` | Development Error Tracer unit tests |
| `ecum/` | ECU State Manager unit tests |
| `tm/` | Timing Module unit tests |
| `pbcfgm/` | Post-Build Configuration Manager unit tests |
| `parser/` | Parser Layer unit tests |
| `reporter/` | Reporter Layer unit tests |
| `cli/` | CLI Layer unit tests |

## Test Case ID Format

Unit test case IDs follow the format: `TC_UNIT_<MODULE>_<NUMBER>`

- **UNIT**: Indicates this is a unit test
- **MODULE**: Uppercase module identifier (OS, RTE, NVM, etc.)
- **NUMBER**: 5-digit sequential number starting at 00001

Example: `TC_UNIT_OS_00001`

## Unit Test Categories

### Parser Unit Tests
- Test individual parser methods
- Verify XML parsing functionality
- Validate namespace handling
- Test value extraction methods
- Verify reference resolution

### Model Unit Tests
- Test individual model class methods
- Verify object creation and initialization
- Test attribute getter/setter methods
- Validate parent-child relationships
- Test data structure operations

### Reporter Unit Tests
- Test worksheet creation methods
- Verify cell formatting
- Test auto-width calculation
- Validate data population
- Test export functionality

### CLI Unit Tests
- Test argument parsing
- Verify help display
- Test logging configuration
- Validate error messages
- Test exit code handling

## Execution Guidelines

### Prerequisites
1. py-eb-model package installed
2. Test data files available
3. Required dependencies installed

### Running Unit Tests
Unit tests are implemented in Python using pytest. Execute from project root:

```bash
# Run all unit tests
pytest src/eb_model/tests/

# Run unit tests for specific module
pytest src/eb_model/tests/parser/test_os_xdm_parser.py
pytest src/eb_model/tests/models/test_abstract.py

# Run with coverage
pytest --cov=src/eb_model
```

### Test Data
Unit tests use mock XML data generated within test files. No external test data files are required.

## Dependencies

- pytest: Test framework
- openpyxl: Excel file handling (for reporter tests)
- xml.etree.ElementTree: XML parsing (built-in)

## Related Documentation

- [Integration Tests](../integration/README.md)
- [Test Case Template](../template.md)
- [Test Case Registry](../registry.md)
- [Software Requirements](../requirements/requirements.md)

## Document Control

| Field | Value |
|-------|-------|
| Document Title | Unit Test Cases |
| Document ID | TC_UNIT_README_00001 |
| Version | 1.0 |
| Date | 2026-03-27 |
| Standard | ISO/IEC/IEEE 29119-3:2013 |