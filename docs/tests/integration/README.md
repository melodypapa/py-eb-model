# Integration Test Cases

This directory contains ISO/IEC/IEEE 29119-3 compliant integration test case documentation for the py-eb-model project.

## Purpose

Integration tests verify the interaction between multiple components, testing workflows and data flow across the system layers.

## Organization

Each subdirectory corresponds to a module or integration category:

| Directory | Description |
|-----------|-------------|
| `os/` | Operating System module integration tests |
| `rte/` | Runtime Environment module integration tests |
| `nvm/` | Non-Volatile Memory module integration tests |
| `ecuc/` | ECU Configuration module integration tests |
| `bswm/` | Basic Software Mode Manager integration tests |
| `can/` | CAN Stack integration tests (CanIf, CanNm, CanSm, CanTp) |
| `lin/` | LIN Stack integration tests (LinIf, LinSm, LinTp) |
| `flexray/` | FlexRay Stack integration tests (FrIf, FrNm, FrSm, FrTp, FrArTp) |
| `ethernet/` | Ethernet Stack integration tests (EthIf, EthSm, DoIP, SoAd, SomeIpTp, TcpIp, UdpNm) |
| `cross-module/` | Cross-module integration tests |

## Test Case ID Format

Integration test case IDs follow the format: `TC_INT_<MODULE>_<NUMBER>`

- **INT**: Indicates this is an integration test
- **MODULE**: Uppercase module identifier (OS, RTE, NVM, CAN, LIN, FLEXRAY, ETHERNET, CROSS)
- **NUMBER**: 5-digit sequential number starting at 00001

Examples: `TC_INT_OS_00001`, `TC_INT_CAN_00001`, `TC_INT_CROSS_00001`

## Integration Test Categories

### End-to-End Module Tests
Test complete workflows for individual modules:
- XDM file parsing
- Model population
- Excel report generation
- CLI command execution

### Stack Integration Tests
Test interaction between modules within a communication stack:
- PDU routing across layers
- State machine coordination
- Multi-channel configuration
- Cross-layer error handling

### Cross-Module Integration Tests
Test interaction between different modules and layers:
- Multi-module parsing
- Parser + Model + Reporter integration
- Full system workflows
- Cross-module data flow

## Execution Guidelines

### Prerequisites
1. py-eb-model package installed
2. Complete test XDM files available
3. Output directory writable
4. Required dependencies installed

### Running Integration Tests
Integration tests are implemented in Python using pytest. Execute from project root:

```bash
# Run all integration tests
pytest src/eb_model/tests/

# Run integration tests for specific module
pytest src/eb_model/tests/integration/test_os_integration.py

# Run with coverage
pytest --cov=src/eb_model --cov-report=html
```

### Test Data
Integration tests require complete XDM files with realistic configurations:
- Full module configurations
- Multiple entity types
- Edge cases and error scenarios

## Dependencies

- pytest: Test framework
- openpyxl: Excel file handling
- xml.etree.ElementTree: XML parsing (built-in)
- Complete XDM test files

## Test Scenarios

### End-to-End Workflow Tests
1. Parse XDM file
2. Validate parsing completeness
3. Generate Excel report
4. Verify report accuracy
5. Verify formatting

### Error Handling Tests
1. Parse malformed XDM file
2. Handle missing required elements
3. Validate error messages
4. Verify system recovery

### Performance Tests
1. Large file processing
2. Multi-module parsing
3. Concurrent operations
4. Memory usage validation

## Related Documentation

- [Unit Tests](../unit/README.md)
- [Test Case Template](../template.md)
- [Test Case Registry](../registry.md)
- [Software Requirements](../requirements/requirements.md)

## Document Control

| Field | Value |
|-------|-------|
| Document Title | Integration Test Cases |
| Document ID | TC_INT_README_00001 |
| Version | 1.0 |
| Date | 2026-03-27 |
| Standard | ISO/IEC/IEEE 29119-3:2013 |