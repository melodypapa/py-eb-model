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