# Unit Test Specification: XDM Model Generator

## Document Information
| Field | Value |
|-------|-------|
| Document Title | XDM Model Generator Unit Test Specifications |
| Document ID | UTS_GEN_00001 |
| Version | 1.0 |
| Date | 2026-06-07 |
| Project | py-eb-model |
| Module | Generator |
| Test Type | Unit Test |

---

## Overview

Unit test specifications for the XDM Model Generator covering schema model dataclasses, schema parser, value generation strategies, and data generator components.

**Test Implementation:** `tests/generator/`

---

## Traceability Summary
| Metric | Count | Percentage |
|--------|-------|------------|
| Total Requirements | 4 | 100% |
| Requirements with Tests | 4 | 100% |
| Requirements without Tests | 0 | 0% |
| Total Test Cases | 40 | - |

---

## Coverage Matrix
| Requirement ID | Test Case IDs | Coverage Status | Last Verified |
|----------------|---------------|-----------------|---------------|
| SWR_GEN_00001 | UTS_GEN_MODEL_00001 - UTS_GEN_MODEL_00010 | ✅ Covered | 2026-06-07 |
| SWR_GEN_00002 | UTS_GEN_PARSER_00001 - UTS_GEN_PARSER_00007 | ✅ Covered | 2026-06-07 |
| SWR_GEN_00003 | UTS_GEN_STRAT_00001 - UTS_GEN_STRAT_00022 | ✅ Covered | 2026-06-07 |
| SWR_GEN_00004 | UTS_GEN_DATAGEN_00001 - UTS_GEN_DATAGEN_00007 | ✅ Covered | 2026-06-07 |

---

## Test Specifications

### UTS_GEN_MODEL_00001 : SchemaRange Default Values

**Type:** Functional
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_GEN_00001
**Test Implementation:** test_schema_model.py::TestSchemaRange::test_default_range
**Last Validated:** 2026-06-07

**Test Design Technique:** Equivalence Partitioning

**Preconditions:**
1. SchemaRange dataclass is imported

**Test Steps:**
1. **Given:** SchemaRange is instantiated with no arguments
2. **When:** All fields are accessed
3. **Then:** min_value is None, max_value is None, enum_values is [], regex_pattern is None

---

### UTS_GEN_MODEL_00002 : SchemaRange with Enum Values

**Traces-To:** SWR_GEN_00001
**Test Implementation:** test_schema_model.py::TestSchemaRange::test_range_with_enum_values
**Status:** Passed

**Test Steps:**
1. **Given:** SchemaRange with enum_values=["VariantPostBuild", "VariantPreCompile"]
2. **When:** enum_values is accessed
3. **Then:** Length is 2

---

### UTS_GEN_MODEL_00003 : SchemaVar with Default

**Traces-To:** SWR_GEN_00001
**Test Implementation:** test_schema_model.py::TestSchemaVar::test_basic_var
**Status:** Passed

**Test Steps:**
1. **Given:** SchemaVar with name="CanIfDevErrorDetect", var_type="BOOLEAN", default="false"
2. **When:** Fields are accessed
3. **Then:** name, var_type, and default match expected values

---

### UTS_GEN_MODEL_00004 : SchemaVar without Default

**Traces-To:** SWR_GEN_00001
**Test Implementation:** test_schema_model.py::TestSchemaVar::test_var_without_default
**Status:** Passed

**Test Steps:**
1. **Given:** SchemaVar with no default value
2. **When:** default is accessed
3. **Then:** default is None

---

### UTS_GEN_MODEL_00005 : SchemaCtr Basic Container

**Traces-To:** SWR_GEN_00001
**Test Implementation:** test_schema_model.py::TestSchemaCtr::test_basic_container
**Status:** Passed

**Test Steps:**
1. **Given:** SchemaCtr with name="CanIfGeneral"
2. **When:** children is accessed
3. **Then:** children is empty list

---

### UTS_GEN_MODEL_00006 : SchemaCtr with Children

**Traces-To:** SWR_GEN_00001
**Test Implementation:** test_schema_model.py::TestSchemaCtr::test_container_with_children
**Status:** Passed

**Test Steps:**
1. **Given:** SchemaCtr with one SchemaVar child
2. **When:** children is accessed
3. **Then:** Length is 1, child name matches

---

### UTS_GEN_MODEL_00007 : SchemaLst MAP Type

**Traces-To:** SWR_GEN_00001
**Test Implementation:** test_schema_model.py::TestSchemaLst::test_map_list
**Status:** Passed

---

### UTS_GEN_MODEL_00008 : SchemaLst with MIN/MAX

**Traces-To:** SWR_GEN_00001
**Test Implementation:** test_schema_model.py::TestSchemaLst::test_list_with_min_max
**Status:** Passed

---

### UTS_GEN_MODEL_00009 : SchemaRef Basic

**Traces-To:** SWR_GEN_00001
**Test Implementation:** test_schema_model.py::TestSchemaRef::test_basic_ref
**Status:** Passed

---

### UTS_GEN_MODEL_00010 : SchemaRoot Basic

**Traces-To:** SWR_GEN_00001
**Test Implementation:** test_schema_model.py::TestSchemaRoot::test_basic_root
**Status:** Passed

---

### UTS_GEN_PARSER_00001 : Parse Boolean Variable

**Traces-To:** SWR_GEN_00002
**Test Implementation:** test_schema_parser.py::TestSchemaParserBasic::test_parse_simple_boolean_var
**Status:** Passed

**Test Steps:**
1. **Given:** XDM with v:var name="TestBool" type="BOOLEAN" with DEFAULT="true"
2. **When:** SchemaParser.parse() is called
3. **Then:** module_name is "TestMod", module_def has 1 child, var has default="true"

---

### UTS_GEN_PARSER_00002 : Parse Integer with Range

**Traces-To:** SWR_GEN_00002
**Test Implementation:** test_schema_parser.py::TestSchemaParserBasic::test_parse_integer_with_range
**Status:** Passed

**Test Steps:**
1. **Given:** XDM with v:var type="INTEGER" with DEFAULT="10" and RANGE="0-255"
2. **When:** parse() is called
3. **Then:** var.default="10", range_info.min_value=0, range_info.max_value=255

---

### UTS_GEN_PARSER_00003 : Parse Enumeration with Range Values

**Traces-To:** SWR_GEN_00002
**Test Implementation:** test_schema_parser.py::TestSchemaParserBasic::test_parse_enumeration_with_range_values
**Status:** Passed

**Test Steps:**
1. **Given:** XDM with v:var type="ENUMERATION" with multi-value RANGE
2. **When:** parse() is called
3. **Then:** range_info.enum_values == ["VariantA", "VariantB", "VariantC"]

---

### UTS_GEN_PARSER_00004 : Parse Container with Children

**Traces-To:** SWR_GEN_00002
**Test Implementation:** test_schema_parser.py::TestSchemaParserBasic::test_parse_container_with_children
**Status:** Passed

**Test Steps:**
1. **Given:** XDM with nested v:ctr containing two v:var children
2. **When:** parse() is called
3. **Then:** ctr has 2 children of type SchemaVar

---

### UTS_GEN_PARSER_00005 : Parse List with MIN/MAX

**Traces-To:** SWR_GEN_00002
**Test Implementation:** test_schema_parser.py::TestSchemaParserBasic::test_parse_list_with_min_max
**Status:** Passed

**Test Steps:**
1. **Given:** XDM with v:lst type="MAP" with MIN=1, MAX=10 and child v:ctr
2. **When:** parse() is called
3. **Then:** lst.min_entries=1, lst.max_entries=10, lst.child is SchemaCtr

---

### UTS_GEN_PARSER_00006 : Parse Reference

**Traces-To:** SWR_GEN_00002
**Test Implementation:** test_schema_parser.py::TestSchemaParserBasic::test_parse_reference
**Status:** Passed

**Test Steps:**
1. **Given:** XDM with v:ref with REF="ASPathDataOfSchema:/TestMod/Config/Target"
2. **When:** parse() is called
3. **Then:** ref has 1 ref_target containing "Target"

---

### UTS_GEN_PARSER_00007 : Parse Choice

**Traces-To:** SWR_GEN_00002
**Test Implementation:** test_schema_parser.py::TestSchemaParserBasic::test_parse_choice
**Status:** Passed

**Test Steps:**
1. **Given:** XDM with v:chc containing 2 v:ctr choices
2. **When:** parse() is called
3. **Then:** chc has 2 choices of type SchemaCtr

---

### UTS_GEN_STRAT_00001 - UTS_GEN_STRAT_00012 : DefaultsStrategy

**Traces-To:** SWR_GEN_00003
**Test Implementation:** test_strategies.py::TestDefaultsStrategy
**Status:** Passed

| Test Case | Description |
| --- | --- |
| test_boolean_default | Returns "true" when default="true" |
| test_integer_default | Returns "42" when default="42" |
| test_float_default | Returns "3.14" when default="3.14" |
| test_string_default | Returns "hello" when default="hello" |
| test_enum_default | Returns "VariantA" when default="VariantA" |
| test_function_name_default | Returns "MyFunc" when default="MyFunc" |
| test_no_default_boolean | Returns "false" when no default |
| test_no_default_integer | Returns "0" when no default |
| test_no_default_string | Returns "" when no default |
| test_no_default_enum_with_range | Returns first RANGE value |
| test_reference_default | Generates mock ASPath from REF target |
| test_reference_no_target | Returns None when no REF targets |

---

### UTS_GEN_STRAT_00013 - UTS_GEN_STRAT_00016 : BoundaryStrategy

**Traces-To:** SWR_GEN_00003
**Test Implementation:** test_strategies.py::TestBoundaryStrategy
**Status:** Passed

| Test Case | Description |
| --- | --- |
| test_boolean_boundary | Returns "true" |
| test_integer_with_range | Returns min value "0" |
| test_integer_no_range | Returns "0" |
| test_enum_boundary_first | Returns first RANGE value |

---

### UTS_GEN_STRAT_00017 - UTS_GEN_STRAT_00022 : RandomStrategy

**Traces-To:** SWR_GEN_00003
**Test Implementation:** test_strategies.py::TestRandomStrategy
**Status:** Passed

| Test Case | Description |
| --- | --- |
| test_boolean_random | Returns "true" or "false" |
| test_integer_random_in_range | Returns value within [0, 100] |
| test_integer_random_no_range | Returns valid integer |
| test_enum_random_from_range | Returns value from RANGE set |
| test_seeded_reproducible | Same seed produces same values |
| test_string_random | Returns valid string |

---

### UTS_GEN_DATAGEN_00001 : Generate Simple Variable

**Traces-To:** SWR_GEN_00004
**Test Implementation:** test_data_generator.py::TestDataGeneratorBasic::test_generate_simple_var
**Status:** Passed

**Test Steps:**
1. **Given:** SchemaRoot with one SchemaVar (BOOLEAN, default="true")
2. **When:** DataGenerator.generate() + toString()
3. **Then:** XML contains `d:var name="TestBool" value="true"`

---

### UTS_GEN_DATAGEN_00002 : Generate Container with Children

**Traces-To:** SWR_GEN_00004
**Test Implementation:** test_data_generator.py::TestDataGeneratorBasic::test_generate_container_with_children
**Status:** Passed

---

### UTS_GEN_DATAGEN_00003 : Generate List with Entries

**Traces-To:** SWR_GEN_00004
**Test Implementation:** test_data_generator.py::TestDataGeneratorBasic::test_generate_list_with_entries
**Status:** Passed

**Test Steps:**
1. **Given:** SchemaLst with min_entries=2 and child SchemaCtr
2. **When:** generate() is called
3. **Then:** XML contains at least 2 entries named "Item_0", "Item_1"

---

### UTS_GEN_DATAGEN_00004 : Generate Reference

**Traces-To:** SWR_GEN_00004
**Test Implementation:** test_data_generator.py::TestDataGeneratorBasic::test_generate_reference
**Status:** Passed

---

### UTS_GEN_DATAGEN_00005 : Generate Choice (First Option)

**Traces-To:** SWR_GEN_00004
**Test Implementation:** test_data_generator.py::TestDataGeneratorBasic::test_generate_choice_first_option
**Status:** Passed

---

### UTS_GEN_DATAGEN_00006 : Output Has Wrapper Structure

**Traces-To:** SWR_GEN_00004
**Test Implementation:** test_data_generator.py::TestDataGeneratorBasic::test_output_has_wrapper_structure
**Status:** Passed

**Test Steps:**
1. **Given:** Any SchemaRoot
2. **When:** generate() + toString()
3. **Then:** XML contains datamodel, TOP-LEVEL-PACKAGES, AR-PACKAGE, MODULE-CONFIGURATION

---

### UTS_GEN_DATAGEN_00007 : Output Valid XML

**Traces-To:** SWR_GEN_00004
**Test Implementation:** test_data_generator.py::TestDataGeneratorBasic::test_output_valid_xml
**Status:** Passed

**Test Steps:**
1. **Given:** SchemaRoot with one SchemaVar
2. **When:** toString() is called
3. **Then:** ET.fromstring() parses without error
