# Parser Module Unit Test Cases

This document contains all unit test cases for the Parser module following ISO/IEC/IEEE 29119-3 standard.

---

# Test Case: TC_UNIT_PARSER_00001

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_PARSER_00001 |
| Title | Abstract Parser - XML Parsing and Namespace Handling |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the AbstractEbModelParser correctly reads and stores XML namespace definitions from EB Tresos XDM files, and uses namespaces correctly in XPath queries.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML file with namespace definitions is available |
| 3 | AbstractEbModelParser subclass is instantiated |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Root Namespace | "http://www.tresos.de/_projects/DataModel2/18/root.xsd" | Default namespace |
| Attribute Namespace | "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd" | Attribute namespace |
| Schema Namespace | "http://www.tresos.de/_projects/DataModel2/06/schema.xsd" | Schema namespace |
| Data Namespace | "http://www.tresos.de/_projects/DataModel2/06/data.xsd" | Data namespace |
| Default Prefix | "" | Empty prefix for root namespace |
| Attribute Prefix | "a" | Prefix for attribute namespace |
| Schema Prefix | "v" | Prefix for schema namespace |
| Data Prefix | "d" | Prefix for data namespace |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Read XML file with namespace definitions | Namespaces extracted and stored in nsmap |
| 2 | Verify nsmap contains all 4 namespaces | nsmap dict has 4 entries |
| 3 | Verify namespace prefixes are correct | Prefixes match expected values |
| 4 | Verify namespace URIs are correct | URIs match expected values |
| 5 | Query element using namespace prefix | XPath with namespace works correctly |
| 6 | Query attribute using namespace prefix | Attribute value retrieved correctly |
| 7 | Test XPath with wrong namespace prefix | Query fails gracefully or returns empty |
| 8 | Verify namespace reuse | Same nsmap used for all queries |

## Expected Results

- All namespaces are extracted correctly
- Namespace map is properly structured as dictionary
- XPath queries using namespace prefixes work correctly
- Attribute queries using namespace prefixes work correctly
- Namespace handling is consistent across all operations
- No namespace-related errors during parsing

## Post-conditions

| # | Description |
|---|-------------|
| 1 | nsmap remains available for subclass use |
| 2 | XML element tree is available for further processing |
| 3 | Parser can be reused for additional XML files |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00001 | Abstract Parser - XML parsing and namespace handling | Covered |
| SWR_PARSER_00006 | Non-Functional - Inherit namespace handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Parser Documentation | ../../src/eb_model/parser/abstract_eb_model_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_PARSER_00002

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_PARSER_00002 |
| Title | Abstract Parser - Value Reading Methods |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the AbstractEbModelParser's read_value() and read_optional_value() methods correctly extract values from XML elements, handling different data types and optional elements.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML file with various value types is available |
| 3 | AbstractEbModelParser subclass is instantiated |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| BOOLEAN Value | "true" | Boolean data type |
| INTEGER Value | "42" | Integer data type |
| FLOAT Value | "3.14159" | Float data type |
| STRING Value | "Test String" | String data type |
| ENUMERATION Value | "SCHEDULE_FULL" | Enumeration data type |
| Optional Value Present | Value is present | Test read_optional_value() with present value |
| Optional Value Missing | Element missing ENABLE="false" | Test read_optional_value() with missing value |
| ENABLE Attribute | "true" | Element is enabled |
| DISABLE Attribute | "false" | Element is disabled |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Read BOOLEAN value using read_value() | Returns boolean "true" |
| 2 | Read INTEGER value using read_value() | Returns integer 42 |
| 3 | Read FLOAT value using read_value() | Returns float 3.14159 |
| 4 | Read STRING value using read_value() | Returns string "Test String" |
| 5 | Read ENUMERATION value using read_value() | Returns "SCHEDULE_FULL" |
| 6 | Read optional value with ENABLE="true" | Returns value |
| 7 | Read optional value with ENABLE="false" | Returns None or empty string |
| 8 | Read optional value with missing element | Returns None or empty string |
| 9 | Read required value that is missing | Raises appropriate error |
| 10 | Verify type conversion for numeric values | Numeric values are converted correctly |

## Expected Results

- All data types are read correctly
- Boolean values are properly converted
- Numeric values maintain precision
- String values are returned as-is
- Enumeration values are returned as strings
- Optional values with ENABLE="false" return None
- Missing optional values return None
- Missing required values raise errors
- Type conversion is accurate

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Read values are available to calling code |
| 2 | Parser state is unchanged after reading |
| 3 | No side effects on XML element tree |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00002 | Abstract Parser - Value reading methods | Covered |
| SWR_PARSER_00007 | Non-Functional - Type handling for values | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Parser Documentation | ../../src/eb_model/parser/abstract_eb_model_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_PARSER_00003

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_PARSER_00003 |
| Title | Abstract Parser - Reference Reading Methods |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the AbstractEbModelParser's read_ref_value() and read_ref_raw_value() methods correctly extract AUTOSAR path references from XML elements, handling both direct references and calculated references.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML file with various reference types is available |
| 3 | AbstractEbModelParser subclass is instantiated |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Direct Reference | "ASPath:/Os/Task1" | Simple ASPath reference |
| Nested Reference | "ASPath:/EcuC/Partition1/Task2" | Nested ASPath reference |
| Calculated Reference | "@CALC(SvcAs:/Os/Task1)" | Calculated reference |
| Complex Calculated Reference | "@CALC(SvcAs:/Os/Counter1) + 100" | Calculated reference with expression |
| Missing Reference | Element missing | Test missing reference handling |
| Invalid Reference | "NotASPath:/Invalid" | Test invalid reference format |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Read direct reference using read_ref_value() | Returns "ASPath:/Os/Task1" |
| 2 | Read nested reference using read_ref_value() | Returns "ASPath:/EcuC/Partition1/Task2" |
| 3 | Read calculated reference using read_ref_raw_value() | Returns "@CALC(SvcAs:/Os/Task1)" |
| 4 | Extract ASPath from calculated reference | Returns "/Os/Task1" |
| 5 | Read complex calculated reference | Returns full calculated expression |
| 6 | Read missing reference using read_ref_value() | Returns None or empty string |
| 7 | Read invalid reference format | Handles gracefully or raises error |
| 8 | Verify reference format validation | Valid ASPath format is recognized |
| 9 | Verify calculated reference detection | Calculated references are identified |
| 10 | Test reference path extraction | Path component extracted correctly |

## Expected Results

- Direct references are read correctly
- Calculated references are identified and processed
- ASPath format is validated
- Path extraction works for calculated references
- Missing references return None
- Invalid references are handled appropriately
- Reference format is preserved
- Calculated expressions are not evaluated (returned as-is)

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Read references are available to calling code |
| 2 | Parser state is unchanged after reading |
| 3 | No side effects on XML element tree |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00003 | Abstract Parser - Reference reading methods | Covered |
| SWR_PARSER_00008 | Non-Functional - ASPath reference handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Parser Documentation | ../../src/eb_model/parser/abstract_eb_model_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_PARSER_00004

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_PARSER_00004 |
| Title | Abstract Parser - Container Tag Finding |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the AbstractEbModelParser's find_ctr_tag() method correctly locates container tags in XML structure, supporting both direct name matching and XPath queries.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML file with nested container structures is available |
| 3 | AbstractEbModelParser subclass is instantiated |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Container Name | "OsTask" | Container to find |
| Parent Element | Root XML element | Search starting point |
| Nested Container | "OsIsr" within "Os" | Nested container search |
| Multiple Containers | Multiple "OsTask" elements | Find all instances |
| Non-existent Container | "InvalidContainer" | Test missing container |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Find container by simple name | Returns element or list of elements |
| 2 | Find nested container | Returns correct nested element |
| 3 | Find multiple containers with same name | Returns list of all matching elements |
| 4 | Find non-existent container | Returns None or empty list |
| 5 | Find container using namespace prefix | XPath with namespace works correctly |
| 6 | Find container at specific path | Returns element at exact path |
| 7 | Find container with attribute filter | Returns element matching attributes |
| 8 | Verify container element structure | Returned element has expected structure |
| 9 | Test performance with deep nesting | Find operation completes efficiently |
| 10 | Test error handling for malformed queries | Query errors handled gracefully |

## Expected Results

- Container names are found correctly
- Nested containers are found with proper path resolution
- Multiple containers with same name are all returned
- Non-existent containers return None or empty list
- Namespace-prefixed queries work correctly
- Attribute filtering works as expected
- Deep nesting queries are efficient
- Malformed queries are handled gracefully

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Found containers are available for processing |
| 2 | XML element tree is unchanged |
| 3 | No side effects from find operation |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00004 | Abstract Parser - Container tag finding | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Parser Documentation | ../../src/eb_model/parser/abstract_eb_model_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_PARSER_00005

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_PARSER_00005 |
| Title | Abstract Parser - ENABLE Attribute Handling |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the AbstractEbModelParser correctly handles the ENABLE attribute on XML elements, using it to determine whether optional elements should be processed.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XML file with ENABLE attribute variants is available |
| 3 | AbstractEbModelParser subclass is instantiated |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| ENABLE True | ENABLE="true" | Element is enabled |
| ENABLE False | ENABLE="false" | Element is disabled |
| ENABLE Missing | No ENABLE attribute | Element treated as enabled |
| ENABLE Attribute on Optional Element | ENABLE="false" on optional element | Element should be skipped |
| ENABLE Attribute on Required Element | ENABLE="false" on required element | May cause error or warning |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Read element with ENABLE="true" | Element is processed normally |
| 2 | Read element with ENABLE="false" | Element is skipped or returns None |
| 3 | Read element without ENABLE attribute | Element is processed (default enabled) |
| 4 | Read optional element with ENABLE="false" | Element is skipped without error |
| 5 | Read required element with ENABLE="false" | Appropriate error or warning |
| 6 | Verify ENABLE attribute checking | ENABLE value is checked before processing |
| 7 | Test case-insensitive ENABLE handling | "TRUE", "True", "true" all recognized |
| 8 | Test invalid ENABLE value | Invalid value handled gracefully |
| 9 | Verify ENABLE inheritance | Child elements inherit from parent if not specified |
| 10 | Test performance of ENABLE checking | ENABLE check is efficient |

## Expected Results

- ENABLE="true" elements are processed
- ENABLE="false" elements are skipped
- Missing ENABLE defaults to enabled
- Optional elements with ENABLE="false" are skipped without error
- Required elements with ENABLE="false" generate appropriate errors
- ENABLE values are case-insensitive
- Invalid ENABLE values are handled gracefully
- ENABLE inheritance works correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Only enabled elements are processed |
| 2 | Disabled elements are not in model |
| 3 | Parser state is consistent |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00005 | Abstract Parser - ENABLE attribute handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Parser Documentation | ../../src/eb_model/parser/abstract_eb_model_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

# Test Case: TC_UNIT_PARSER_00006

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_PARSER_00006 |
| Title | EbParserFactory - Parser Type Determination |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the EbParserFactory correctly determines the parser type from XDM file's MODULE-CONFIGURATION tag and instantiates the appropriate parser class.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | XDM files for various modules are available |
| 3 | EbParserFactory is available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| OS XDM File | MODULE-CONFIGURATION choice="Os" | Test OS parser selection |
| RTE XDM File | MODULE-CONFIGURATION choice="Rte" | Test RTE parser selection |
| NVM XDM File | MODULE-CONFIGURATION choice="NvM" | Test NvM parser selection |
| CanIf XDM File | MODULE-CONFIGURATION choice="CanIf" | Test CanIf parser selection |
| Invalid Module | MODULE-CONFIGURATION choice="InvalidModule" | Test error handling |
| Missing Choice | No MODULE-CONFIGURATION choice | Test error handling |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Call EbParserFactory.create() with OS XDM file | Returns OsXdmParser instance |
| 2 | Call EbParserFactory.create() with RTE XDM file | Returns RteXdmParser instance |
| 3 | Call EbParserFactory.create() with NVM XDM file | Returns NvMXdmParser instance |
| 4 | Call EbParserFactory.create() with CanIf XDM file | Returns CanIfXdmParser instance |
| 5 | Call with invalid module choice | Raises ValueError with appropriate message |
| 6 | Call with missing choice | Raises ValueError with appropriate message |
| 7 | Verify parser type is correct | Returned parser is instance of expected class |
| 8 | Verify parser is initialized | Parser can be used for parsing |
| 9 | Test all registered module parsers | All 32 modules can be instantiated |
| 10 | Verify factory pattern usage | Factory returns proper parser for each type |

## Expected Results

- Correct parser is instantiated for each module type
- Invalid module choices raise ValueError
- Missing choices raise ValueError
- Returned parsers are properly initialized
- All registered modules work through factory
- Factory pattern is implemented correctly

## Post-conditions

| # | Description |
|---|-------------|
| 1 | Parsers can be used for parsing |
| 2 | Factory state is unchanged |
| 3 | No side effects from factory calls |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00009 | EbParserFactory - Parser type determination | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Factory Documentation | ../../src/eb_model/parser/eb_parser_factory.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
---

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
---

# Test Case: TC_UNIT_PARSER_00008

## Document Information

| Field | Value |
|-------|-------|
| Test Case ID | TC_UNIT_PARSER_00008 |
| Title | Parser Layer - Error Handling |
| Version | 1.0 |
| Date | 2026-03-27 |
| Author | Test Architect |
| Test Type | Unit |
| Priority | High |

## Purpose/Objective

Verify that the parser layer handles errors consistently across all parser types, providing clear error messages and preventing system crashes.

## Preconditions

| # | Description |
|---|-------------|
| 1 | py-eb-model package is installed |
| 2 | Test files with various error conditions are available |
| 3 | All parser classes are available |

## Test Data/Input Specifications

| Data Element | Value/Description | Purpose |
|--------------|-------------------|---------|
| Malformed XML File | Invalid XML structure | Test XML error handling |
| Missing Required Element | Required element absent | Test validation error handling |
| Invalid Data Type | String where number expected | Test type error handling |
| File Not Found | Non-existent file path | Test file error handling |
| Permission Denied | File without read permission | Test permission error handling |

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Parse malformed XML file | Raises XMLSyntaxError or ValueError |
| 2 | Verify error message is descriptive | Error message indicates XML issue |
| 3 | Parse file with missing required element | Raises ValueError with element name |
| 4 | Verify error message includes location | Error indicates where issue occurred |
| 5 | Parse file with invalid data type | Raises ValueError with type mismatch |
| 6 | Verify error message includes expected type | Message shows expected vs actual type |
| 7 | Attempt to parse non-existent file | Raises FileNotFoundError or IOError |
| 8 | Verify error message includes file path | Message identifies missing file |
| 9 | Attempt to parse file without permission | Raises PermissionError or IOError |
| 10 | Verify error message includes permission issue | Message indicates permission problem |

## Expected Results

- All error conditions are detected
- Error messages are clear and actionable
- Errors include context (file, line, element, type)
- No system crashes occur
- Errors are raised with appropriate exception types
- Error handling is consistent across parser types

## Post-conditions

| # | Description |
|---|-------------|
| 1 | System is stable after errors |
| 2 | Parser can be reused for valid files |
| 3 | No corrupted state from errors |

## Requirements Coverage

| Requirement ID | Description | Status |
|----------------|-------------|--------|
| SWR_PARSER_00010 | Parser Layer - Error handling | Covered |

## References

| Document Type | Reference |
|---------------|-----------|
| Requirement Document | ../requirements/swr_parser-layer.md |
| Parser Documentation | ../../src/eb_model/parser/abstract_eb_model_parser.py |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-27 | Test Architect | Initial test case |
