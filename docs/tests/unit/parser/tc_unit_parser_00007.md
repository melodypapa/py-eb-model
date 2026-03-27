# Test Case: TC_UNIT_PARSER_00007

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_PARSER_00007 |
| Title | EbParserFactory - Module Registration |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EbParserFactory correctly maintains module registrations and supports dynamic registration of new parsers.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | EbParserFactory is available |
| 3 | Sample parser classes are available for testing |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Registered Modules | List of 32 module types | Verify all modules registered |
| Module Mapping | Dictionary of module name to parser class | Verify mapping structure |
| New Parser Class | Custom parser for testing | Test dynamic registration |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Query factory for registered modules | Returns list of 32 module types |
| 2 | Verify expected modules are registered | OS, RTE, NVM, etc. all present |
| 3 | Verify module mapping structure | Dictionary structure is correct |
| 4 | Register new parser class | Registration succeeds |
| 5 | Verify new parser appears in module list | New module is in registered list |
| 6 | Create parser using new registration | Returns new parser instance |
| 7 | Attempt to register duplicate module | Registration fails or overwrites |
| 8 | Unregister module (if supported) | Module is removed from registry |
| 9 | Query registry after unregister | Module no longer in list |
| 10 | Verify registry persistence | Registry maintains state across calls |

## Expected Results

- All 32 modules are registered
- Module mapping is correct
- New parsers can be registered dynamically
- Duplicate registration is handled appropriately
- Unregistration works (if supported)
- Registry persists correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Factory registry is unchanged or appropriately modified |
| 2 | All original modules remain registered (unless intentionally unregistered) |
| 3 | Factory can be used for subsequent operations |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00009 | EbParserFactory - Module registration | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Factory Documentation | ../../src/eb_model/parser/eb_parser_factory.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |