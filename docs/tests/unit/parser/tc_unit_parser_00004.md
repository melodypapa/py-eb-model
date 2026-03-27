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