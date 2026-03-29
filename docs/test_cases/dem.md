# Test Cases: Dem Module

## Document Information

| Field | Value |
|-------|-------|
| Document Title | Dem Module Test Cases |
| Version | 1.0 |
| Date | 2026-03-29 |
| Module | Dem (Diagnostic Event Manager) |

## Test Coverage

### Model Layer Tests

#### TestDem Class

| Test ID | Test Method | Description | Requirements |
|---------|-------------|-------------|--------------|
| TC_DEM_001 | `test_module_initialization` | Verify Dem module initialization with correct name and parent | SWR_DEM_00001 |
| TC_DEM_002 | `test_module_properties` | Verify inherited Module properties (AR version, SW version, element count) | SWR_DEM_00001 |
| TC_DEM_003 | `test_get_set_general` | Verify DemGeneral container getter/setter | SWR_DEM_00002 |

#### TestDemGeneral Class

| Test ID | Test Method | Description | Requirements |
|---------|-------------|-------------|--------------|
| TC_DEM_004 | `test_initialization` | Verify DemGeneral container initialization | SWR_DEM_00002 |
| TC_DEM_005 | `test_get_set_dev_error_detect` | Verify DemDevErrorDetect property getter/setter | SWR_DEM_00002 |
| TC_DEM_006 | `test_get_set_dem_enabled` | Verify DemEnabled property getter/setter | SWR_DEM_00002 |
| TC_DEM_007 | `test_fluent_interface` | Verify fluent interface pattern returns self | SWR_DEM_00006 |

### Parser Layer Tests

#### TestDemXdmParser Class

| Test ID | Test Method | Description | Requirements |
|---------|-------------|-------------|--------------|
| TC_DEM_008 | `test_read_dem_general` | Verify parsing of DemGeneral container from XDM XML | SWR_DEM_00002 |

### Reporter Layer Tests

#### DemXdmXlsWriter Class

| Test ID | Test Method | Description | Requirements |
|---------|-------------|-------------|--------------|
| TC_DEM_009 | `write_dem_general` | Verify Excel sheet creation for DemGeneral configuration | SWR_DEM_00003 |
| TC_DEM_010 | `write` | Verify complete Excel file generation | SWR_DEM_00003 |

### CLI Tests

#### dem-xdm-xlsx Command

| Test ID | Test Command | Description | Requirements |
|---------|--------------|-------------|--------------|
| TC_DEM_011 | `dem-xdm-xlsx INPUT.xdm OUTPUT.xlsx` | Verify CLI executes successfully | SWR_DEM_00004 |
| TC_DEM_012 | `dem-xdm-xlsx --verbose INPUT.xdm OUTPUT.xlsx` | Verify verbose logging mode | SWR_DEM_00004 |

## Test Data Examples

### Sample XDM XML Structure

```xml
<datamodel version="8.0"
        xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
        xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
        xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
        xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
    <d:ctr name="DemGeneral" type="IDENTIFIABLE">
        <d:var name="DemDevErrorDetect" type="BOOLEAN" value="true"/>
        <d:var name="DemEnabled" type="BOOLEAN" value="true"/>
    </d:ctr>
</datamodel>
```

### Expected Excel Output

| Sheet | Columns |
|-------|---------|
| DemGeneral | Name, DevErrorDetect, Enabled |

## Test Execution

### Running All Dem Tests

```bash
pytest src/eb_model/tests/models/test_dem_xdm.py
pytest src/eb_model/tests/parser/test_dem_xdm_parser.py
```

### Running Individual Tests

```bash
pytest src/eb_model/tests/models/test_dem_xdm.py::TestDem::test_module_initialization
pytest src/eb_model/tests/parser/test_dem_xdm_parser.py::TestDemXdmParser::test_read_dem_general
```

### Running with Coverage

```bash
pytest src/eb_model/tests/models/test_dem_xdm.py src/eb_model/tests/parser/test_dem_xdm_parser.py --cov=src/eb_model/models/dem_xdm --cov=src/eb_model/parser/dem_xdm_parser
```

## Test Results Summary

| Category | Total Tests | Passed | Failed |
|----------|-------------|--------|--------|
| Model Layer | 7 | 7 | 0 |
| Parser Layer | 1 | 1 | 0 |
| **Total** | **8** | **8** | **0** |

## Traceability Matrix

| Requirement | Test IDs |
|-------------|----------|
| SWR_DEM_00001 | TC_DEM_001, TC_DEM_002 |
| SWR_DEM_00002 | TC_DEM_003, TC_DEM_004, TC_DEM_005, TC_DEM_006, TC_DEM_008 |
| SWR_DEM_00003 | TC_DEM_009, TC_DEM_010 |
| SWR_DEM_00004 | TC_DEM_011, TC_DEM_012 |
| SWR_DEM_00006 | TC_DEM_007 |

---

**Document End**