# Integration Test Specification: XDM Model Generator

## Document Information
| Field | Value |
|-------|-------|
| Document Title | XDM Model Generator Integration Test Specifications |
| Document ID | ITS_GEN_00001 |
| Version | 1.0 |
| Date | 2026-06-07 |
| Project | py-eb-model |
| Module | Generator |
| Test Type | Integration Test |

---

## Overview

Integration tests verifying the XDM Model Generator works with real schema XDM files (CanIf, Os) and that generated output integrates with the existing `eb-convert` toolchain.

**Test Implementation:** `tests/generator/test_integration.py`, `tests/generator/test_eb_convert_verification.py`

---

## Traceability Summary
| Metric | Count | Percentage |
|--------|-------|------------|
| Total Requirements | 2 | 100% |
| Requirements with Tests | 2 | 100% |
| Requirements without Tests | 0 | 0% |
| Total Test Cases | 13 | - |

---

## Coverage Matrix
| Requirement ID | Test Case IDs | Coverage Status | Last Verified |
|----------------|---------------|-----------------|---------------|
| SWR_GEN_00002, SWR_GEN_00004 | ITS_GEN_CANIF_00001 - ITS_GEN_CANIF_00005 | ✅ Covered | 2026-06-07 |
| SWR_GEN_00002, SWR_GEN_00004 | ITS_GEN_OS_00001 - ITS_GEN_OS_00003 | ✅ Covered | 2026-06-07 |
| SWR_GEN_00006 | ITS_GEN_EBCONV_00001 - ITS_GEN_EBCONV_00005 | ✅ Covered | 2026-06-07 |

---

## Test Specifications

### ITS_GEN_CANIF_00001 : Parse CanIf Schema XDM

**Type:** Integration
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_GEN_00002
**Test Implementation:** test_integration.py::TestCanIfGeneration::test_parse_canif_schema
**Last Validated:** 2026-06-07

**Preconditions:**
1. CanIf schema XDM exists at `doc/canif/schema/CanIf.xdm`
2. SchemaParser is initialized

**Test Steps:**
1. **Given:** CanIf schema XDM (6100 lines, DataModel2/16 namespaces)
2. **When:** SchemaParser.parse() processes the file
3. **Then:** module_name="CanIf", module_def has children > 0

---

### ITS_GEN_CANIF_00002 : Generate CanIf Defaults Variant

**Traces-To:** SWR_GEN_00004
**Test Implementation:** test_integration.py::TestCanIfGeneration::test_generate_canif_defaults
**Status:** Passed

**Test Steps:**
1. **Given:** Parsed CanIf schema with DefaultsStrategy
2. **When:** DataGenerator.generate() + toString()
3. **Then:** Output is valid XML containing "CanIf"

---

### ITS_GEN_CANIF_00003 : Generate CanIf Boundary Variant

**Traces-To:** SWR_GEN_00004
**Test Implementation:** test_integration.py::TestCanIfGeneration::test_generate_canif_boundary
**Status:** Passed

---

### ITS_GEN_CANIF_0004 : Generate CanIf Random Variant (Seeded)

**Traces-To:** SWR_GEN_00004
**Test Implementation:** test_integration.py::TestCanIfGeneration::test_generate_canif_random
**Status:** Passed

**Test Steps:**
1. **Given:** Parsed CanIf schema with RandomStrategy(seed=42)
2. **When:** DataGenerator.generate() + toString()
3. **Then:** Output is valid XML (reproducible with same seed)

---

### ITS_GEN_CANIF_00005 : Write CanIf XDM to File

**Traces-To:** SWR_GEN_00004
**Test Implementation:** test_integration.py::TestCanIfGeneration::test_generate_canif_write_file
**Status:** Passed

**Test Steps:**
1. **Given:** Generated CanIf model XDM as string
2. **When:** Written to temp file and parsed with ET.parse()
3. **Then:** File is readable, root element exists

---

### ITS_GEN_OS_00001 : Parse Os Schema XDM (Different Namespace Version)

**Traces-To:** SWR_GEN_00002
**Test Implementation:** test_integration.py::TestOsGeneration::test_parse_os_schema
**Status:** Passed

**Test Steps:**
1. **Given:** Os schema XDM (4454 lines, DataModel2/08 namespaces — different version)
2. **When:** SchemaParser.parse() processes the file
3. **Then:** module_name="Os", module_def has children > 0

---

### ITS_GEN_OS_00002 : Generate Os Defaults Variant

**Traces-To:** SWR_GEN_00004
**Test Implementation:** test_integration.py::TestOsGeneration::test_generate_os_defaults
**Status:** Passed

---

### ITS_GEN_OS_00003 : Generate Os All Variants

**Traces-To:** SWR_GEN_00003, SWR_GEN_00004
**Test Implementation:** test_integration.py::TestOsGeneration::test_generate_os_all_variants
**Status:** Passed

**Test Steps:**
1. **Given:** Parsed Os schema with each strategy (defaults, boundary, random)
2. **When:** DataGenerator.generate() + toString() for each
3. **Then:** All three outputs are valid XML

---

### ITS_GEN_EBCONV_00001 : eb-convert Detects CanIf Module

**Type:** Integration
**Priority:** Critical
**Status:** Passed

**Traces-To:** SWR_GEN_00006
**Test Implementation:** test_eb_convert_verification.py::TestEbConvertDetection::test_canif_module_detected
**Last Validated:** 2026-06-07

**Preconditions:**
1. CanIf schema XDM exists
2. `eb-convert` CLI is installed and accessible

**Test Steps:**
1. **Given:** Generated CanIf model XDM (defaults variant)
2. **When:** `eb-convert <xdm_path> <output_dir>` is run
3. **Then:** stderr contains "Detected module: CanIf"

---

### ITS_GEN_EBCONV_00002 : eb-convert Detects Os Module

**Traces-To:** SWR_GEN_00006
**Test Implementation:** test_eb_convert_verification.py::TestEbConvertDetection::test_os_module_detected
**Status:** Passed

**Test Steps:**
1. **Given:** Generated Os model XDM (defaults variant)
2. **When:** `eb-convert <xdm_path> <output_dir>` is run
3. **Then:** stderr contains "Detected module: Os"

---

### ITS_GEN_EBCONV_00003 : CanIf Namespace Declarations Readable

**Traces-To:** SWR_GEN_00006
**Test Implementation:** test_eb_convert_verification.py::TestGeneratedXdmValidXml::test_canif_namespaces_readable
**Status:** Passed

**Test Steps:**
1. **Given:** Generated CanIf XDM file
2. **When:** ET.iterparse with start-ns events
3. **Then:** Namespace map contains 'd' or '' key

---

### ITS_GEN_EBCONV_00004 : Os Namespace Declarations Readable

**Traces-To:** SWR_GEN_00006
**Test Implementation:** test_eb_convert_verification.py::TestGeneratedXdmValidXml::test_os_namespaces_readable
**Status:** Passed

---

### ITS_GEN_EBCONV_00005 : All Variants Produce Valid XML

**Traces-To:** SWR_GEN_00006
**Test Implementation:** test_eb_convert_verification.py::TestGeneratedXdmValidXml::test_canif_all_variants_valid_xml
**Status:** Passed

**Test Steps:**
1. **Given:** CanIf schema with defaults, boundary, and random strategies
2. **When:** XDM generated for each variant
3. **Then:** All three parse successfully with ET.parse()
