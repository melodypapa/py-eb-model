# XDM Model Generator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a CLI tool that generates model (instance) XDM files from schema XDM files for testing, supporting defaults/boundary/random variants.

**Architecture:** Two-pass schema-aware generator. First pass: SchemaParser reads `v:` nodes into Python dataclass model. Second pass: DataGenerator walks the schema model and produces `d:` element tree using a pluggable variant strategy for value selection.

**Tech Stack:** Python 3.9+, `xml.etree.ElementTree` (stdlib), `dataclasses` (stdlib), `argparse` (stdlib), `pytest`

---

### Task 1: Schema Model Dataclasses

**Files:**
- Create: `src/eb_model/generator/__init__.py`
- Create: `src/eb_model/generator/schema_model.py`
- Test: `tests/generator/__init__.py`
- Test: `tests/generator/test_schema_model.py`

- [ ] **Step 1: Create package directories**

```bash
mkdir -p src/eb_model/generator
mkdir -p tests/generator
touch src/eb_model/generator/__init__.py
touch tests/generator/__init__.py
```

- [ ] **Step 2: Write schema model dataclasses**

Create `src/eb_model/generator/schema_model.py`:

```python
"""Schema model dataclasses representing XDM schema node structure.

Implements: SWR_GEN_00001 (Schema Model)
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class SchemaRange:
    """Parsed RANGE constraints for a schema variable."""
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    enum_values: List[str] = field(default_factory=list)
    regex_pattern: Optional[str] = None


@dataclass
class SchemaVar:
    """Schema variable definition (v:var)."""
    name: str
    var_type: str  # BOOLEAN, INTEGER, FLOAT, STRING, ENUMERATION, FUNCTION-NAME
    default: Optional[str] = None
    range_info: Optional[SchemaRange] = None
    label: Optional[str] = None
    desc: Optional[str] = None


@dataclass
class SchemaRef:
    """Schema reference definition (v:ref)."""
    name: str
    ref_type: str  # REFERENCE
    ref_targets: List[str] = field(default_factory=list)
    range_targets: List[str] = field(default_factory=list)


@dataclass
class SchemaCtr:
    """Schema container definition (v:ctr)."""
    name: str
    ctr_type: str  # IDENTIFIABLE, MODULE-DEF, AR-PACKAGE, etc.
    children: List = field(default_factory=list)  # List of schema nodes
    name_pattern: Optional[str] = None
    label: Optional[str] = None


@dataclass
class SchemaLst:
    """Schema list definition (v:lst)."""
    name: str
    lst_type: str  # MAP or empty string
    min_entries: int = 0
    max_entries: Optional[int] = None
    child: Optional[object] = None  # SchemaCtr, SchemaVar, or SchemaRef
    name_pattern: Optional[str] = None


@dataclass
class SchemaChc:
    """Schema choice definition (v:chc)."""
    name: str
    chc_type: str
    choices: List = field(default_factory=list)  # List of SchemaCtr


@dataclass
class SchemaRoot:
    """Root of a parsed schema tree."""
    module_name: str
    module_def: Optional[SchemaCtr] = None
    version: str = "7.0"
    namespaces: Dict[str, str] = field(default_factory=dict)
    ar_package_name: str = ""
```

- [ ] **Step 3: Write basic model tests**

Create `tests/generator/test_schema_model.py`:

```python
"""Tests for schema model dataclasses."""
from eb_model.generator.schema_model import (
    SchemaVar, SchemaCtr, SchemaLst, SchemaRef, SchemaChc,
    SchemaRange, SchemaRoot,
)


class TestSchemaRange:
    def test_default_range(self):
        r = SchemaRange()
        assert r.min_value is None
        assert r.max_value is None
        assert r.enum_values == []
        assert r.regex_pattern is None

    def test_range_with_enum_values(self):
        r = SchemaRange(enum_values=["VariantPostBuild", "VariantPreCompile"])
        assert len(r.enum_values) == 2


class TestSchemaVar:
    def test_basic_var(self):
        var = SchemaVar(name="CanIfDevErrorDetect", var_type="BOOLEAN", default="false")
        assert var.name == "CanIfDevErrorDetect"
        assert var.var_type == "BOOLEAN"
        assert var.default == "false"

    def test_var_without_default(self):
        var = SchemaVar(name="SomeInt", var_type="INTEGER")
        assert var.default is None


class TestSchemaCtr:
    def test_basic_container(self):
        ctr = SchemaCtr(name="CanIfGeneral", ctr_type="IDENTIFIABLE")
        assert ctr.name == "CanIfGeneral"
        assert ctr.children == []

    def test_container_with_children(self):
        child = SchemaVar(name="Enabled", var_type="BOOLEAN", default="true")
        ctr = SchemaCtr(name="Parent", ctr_type="IDENTIFIABLE", children=[child])
        assert len(ctr.children) == 1
        assert ctr.children[0].name == "Enabled"


class TestSchemaLst:
    def test_map_list(self):
        lst = SchemaLst(name="OsAlarm", lst_type="MAP", min_entries=0)
        assert lst.lst_type == "MAP"
        assert lst.min_entries == 0

    def test_list_with_min_max(self):
        lst = SchemaLst(name="Items", lst_type="", min_entries=1, max_entries=10)
        assert lst.min_entries == 1
        assert lst.max_entries == 10


class TestSchemaRef:
    def test_basic_ref(self):
        ref = SchemaRef(name="CanIfCtrlCanCtrlRef", ref_type="REFERENCE")
        assert ref.name == "CanIfCtrlCanCtrlRef"
        assert ref.ref_targets == []


class TestSchemaRoot:
    def test_basic_root(self):
        root = SchemaRoot(module_name="CanIf")
        assert root.module_name == "CanIf"
        assert root.module_def is None
```

- [ ] **Step 4: Run tests**

Run: `pytest tests/generator/test_schema_model.py -v`
Expected: All 8 tests PASS

- [ ] **Step 5: Commit**

```bash
git add src/eb_model/generator/__init__.py src/eb_model/generator/schema_model.py tests/generator/__init__.py tests/generator/test_schema_model.py
git commit -m "feat(generator): add schema model dataclasses"
```

---

### Task 2: Schema Parser

**Files:**
- Create: `src/eb_model/generator/schema_parser.py`
- Test: `tests/generator/test_schema_parser.py`

This parser reads XDM schema files containing `v:` nodes and builds the schema model. It handles namespace resolution dynamically since schemas use different namespace versions (e.g., DataModel2/08 vs DataModel2/16).

- [ ] **Step 1: Write failing tests for schema parser**

Create `tests/generator/test_schema_parser.py`:

```python
"""Tests for XDM schema parser."""
import xml.etree.ElementTree as ET
import pytest
from eb_model.generator.schema_parser import SchemaParser
from eb_model.generator.schema_model import (
    SchemaVar, SchemaCtr, SchemaLst, SchemaRef, SchemaChc, SchemaRoot,
)


class TestSchemaParserBasic:
    def _parse_xml(self, xml_str):
        """Helper to parse XML string and return schema root."""
        element = ET.fromstring(xml_str)
        parser = SchemaParser()
        return parser.parse(element)

    def test_parse_simple_boolean_var(self):
        xml = """<datamodel version="7.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/16/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/16/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
          <d:ctr type="AUTOSAR" factory="autosar">
            <d:lst type="TOP-LEVEL-PACKAGES">
              <d:ctr name="TestPkg" type="AR-PACKAGE">
                <d:lst type="ELEMENTS">
                  <d:chc name="TestMod" type="AR-ELEMENT" value="MODULE-DEF">
                    <v:ctr type="MODULE-DEF">
                      <v:var name="TestBool" type="BOOLEAN">
                        <a:da name="DEFAULT" value="true"/>
                      </v:var>
                    </v:ctr>
                  </d:chc>
                </d:lst>
              </d:ctr>
            </d:lst>
          </d:ctr>
        </datamodel>"""
        root = self._parse_xml(xml)
        assert root.module_name == "TestMod"
        assert root.module_def is not None
        assert len(root.module_def.children) == 1
        var = root.module_def.children[0]
        assert isinstance(var, SchemaVar)
        assert var.name == "TestBool"
        assert var.var_type == "BOOLEAN"
        assert var.default == "true"

    def test_parse_integer_with_range(self):
        xml = """<datamodel version="7.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/16/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/16/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
          <d:ctr type="AUTOSAR" factory="autosar">
            <d:lst type="TOP-LEVEL-PACKAGES">
              <d:ctr name="TestPkg" type="AR-PACKAGE">
                <d:lst type="ELEMENTS">
                  <d:chc name="TestMod" type="AR-ELEMENT" value="MODULE-DEF">
                    <v:ctr type="MODULE-DEF">
                      <v:var name="TestInt" type="INTEGER">
                        <a:da name="DEFAULT" value="10"/>
                        <a:da name="RANGE" value="0-255"/>
                      </v:var>
                    </v:ctr>
                  </d:chc>
                </d:lst>
              </d:ctr>
            </d:lst>
          </d:ctr>
        </datamodel>"""
        root = self._parse_xml(xml)
        var = root.module_def.children[0]
        assert var.default == "10"
        assert var.range_info is not None
        assert var.range_info.min_value == 0
        assert var.range_info.max_value == 255

    def test_parse_enumeration_with_range_values(self):
        xml = """<datamodel version="7.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/16/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/16/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
          <d:ctr type="AUTOSAR" factory="autosar">
            <d:lst type="TOP-LEVEL-PACKAGES">
              <d:ctr name="TestPkg" type="AR-PACKAGE">
                <d:lst type="ELEMENTS">
                  <d:chc name="TestMod" type="AR-ELEMENT" value="MODULE-DEF">
                    <v:ctr type="MODULE-DEF">
                      <v:var name="TestEnum" type="ENUMERATION">
                        <a:da name="DEFAULT" value="VariantA"/>
                        <a:da name="RANGE">
                          <a:v>VariantA</a:v>
                          <a:v>VariantB</a:v>
                          <a:v>VariantC</a:v>
                        </a:da>
                      </v:var>
                    </v:ctr>
                  </d:chc>
                </d:lst>
              </d:ctr>
            </d:lst>
          </d:ctr>
        </datamodel>"""
        root = self._parse_xml(xml)
        var = root.module_def.children[0]
        assert var.var_type == "ENUMERATION"
        assert var.default == "VariantA"
        assert var.range_info.enum_values == ["VariantA", "VariantB", "VariantC"]

    def test_parse_container_with_children(self):
        xml = """<datamodel version="7.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/16/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/16/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
          <d:ctr type="AUTOSAR" factory="autosar">
            <d:lst type="TOP-LEVEL-PACKAGES">
              <d:ctr name="TestPkg" type="AR-PACKAGE">
                <d:lst type="ELEMENTS">
                  <d:chc name="TestMod" type="AR-ELEMENT" value="MODULE-DEF">
                    <v:ctr type="MODULE-DEF">
                      <v:ctr name="General" type="IDENTIFIABLE">
                        <v:var name="Enabled" type="BOOLEAN">
                          <a:da name="DEFAULT" value="true"/>
                        </v:var>
                        <v:var name="Count" type="INTEGER">
                          <a:da name="DEFAULT" value="5"/>
                        </v:var>
                      </v:ctr>
                    </v:ctr>
                  </d:chc>
                </d:lst>
              </d:ctr>
            </d:lst>
          </d:ctr>
        </datamodel>"""
        root = self._parse_xml(xml)
        ctr = root.module_def.children[0]
        assert isinstance(ctr, SchemaCtr)
        assert ctr.name == "General"
        assert len(ctr.children) == 2

    def test_parse_list_with_min_max(self):
        xml = """<datamodel version="7.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/16/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/16/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
          <d:ctr type="AUTOSAR" factory="autosar">
            <d:lst type="TOP-LEVEL-PACKAGES">
              <d:ctr name="TestPkg" type="AR-PACKAGE">
                <d:lst type="ELEMENTS">
                  <d:chc name="TestMod" type="AR-ELEMENT" value="MODULE-DEF">
                    <v:ctr type="MODULE-DEF">
                      <v:lst name="Items" type="MAP">
                        <a:da name="MIN" value="1"/>
                        <a:da name="MAX" value="10"/>
                        <v:ctr name="Item" type="IDENTIFIABLE">
                          <v:var name="Value" type="INTEGER">
                            <a:da name="DEFAULT" value="0"/>
                          </v:var>
                        </v:ctr>
                      </v:lst>
                    </v:ctr>
                  </d:chc>
                </d:lst>
              </d:ctr>
            </d:lst>
          </d:ctr>
        </datamodel>"""
        root = self._parse_xml(xml)
        lst = root.module_def.children[0]
        assert isinstance(lst, SchemaLst)
        assert lst.name == "Items"
        assert lst.lst_type == "MAP"
        assert lst.min_entries == 1
        assert lst.max_entries == 10
        assert lst.child is not None
        assert isinstance(lst.child, SchemaCtr)

    def test_parse_reference(self):
        xml = """<datamodel version="7.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/16/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/16/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
          <d:ctr type="AUTOSAR" factory="autosar">
            <d:lst type="TOP-LEVEL-PACKAGES">
              <d:ctr name="TestPkg" type="AR-PACKAGE">
                <d:lst type="ELEMENTS">
                  <d:chc name="TestMod" type="AR-ELEMENT" value="MODULE-DEF">
                    <v:ctr type="MODULE-DEF">
                      <v:ctr name="Config" type="IDENTIFIABLE">
                        <v:ref name="TargetRef" type="REFERENCE">
                          <a:da name="REF" value="ASPathDataOfSchema:/TestMod/Config/Target"/>
                        </v:ref>
                      </v:ctr>
                    </v:ctr>
                  </d:chc>
                </d:lst>
              </d:ctr>
            </d:lst>
          </d:ctr>
        </datamodel>"""
        root = self._parse_xml(xml)
        config = root.module_def.children[0]
        ref = config.children[0]
        assert isinstance(ref, SchemaRef)
        assert ref.name == "TargetRef"
        assert len(ref.ref_targets) == 1
        assert "Target" in ref.ref_targets[0]

    def test_parse_choice(self):
        xml = """<datamodel version="7.0"
            xmlns="http://www.tresos.de/_projects/DataModel2/16/root.xsd"
            xmlns:a="http://www.tresos.de/_projects/DataModel2/16/attribute.xsd"
            xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
            xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
          <d:ctr type="AUTOSAR" factory="autosar">
            <d:lst type="TOP-LEVEL-PACKAGES">
              <d:ctr name="TestPkg" type="AR-PACKAGE">
                <d:lst type="ELEMENTS">
                  <d:chc name="TestMod" type="AR-ELEMENT" value="MODULE-DEF">
                    <v:ctr type="MODULE-DEF">
                      <v:chc name="Action" type="IDENTIFIABLE">
                        <v:ctr name="ActivateTask" type="IDENTIFIABLE">
                          <v:ref name="TaskRef" type="REFERENCE"/>
                        </v:ctr>
                        <v:ctr name="SetEvent" type="IDENTIFIABLE">
                          <v:ref name="EventRef" type="REFERENCE"/>
                        </v:ctr>
                      </v:chc>
                    </v:ctr>
                  </d:chc>
                </d:lst>
              </d:ctr>
            </d:lst>
          </d:ctr>
        </datamodel>"""
        root = self._parse_xml(xml)
        chc = root.module_def.children[0]
        assert isinstance(chc, SchemaChc)
        assert chc.name == "Action"
        assert len(chc.choices) == 2
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/generator/test_schema_parser.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'eb_model.generator.schema_parser'`

- [ ] **Step 3: Implement SchemaParser**

Create `src/eb_model/generator/schema_parser.py`:

```python
"""Parser for XDM schema files (v: prefix nodes).

Reads schema XDM and builds SchemaModel tree.

Implements: SWR_GEN_00002 (Schema Parser)
"""

import logging
import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional

from .schema_model import (
    SchemaChc, SchemaCtr, SchemaLst, SchemaRange, SchemaRef, SchemaRoot, SchemaVar,
)


logger = logging.getLogger(__name__)


class SchemaParser:
    """Parse XDM schema files into schema model objects."""

    # Common XPath namespace prefixes used in schema XDM
    _NS_V = 'v'  # schema nodes
    _NS_D = 'd'  # data wrapper nodes
    _NS_A = 'a'  # attribute nodes

    def __init__(self) -> None:
        self.nsmap: Dict[str, str] = {}

    def parse(self, root_element: ET.Element) -> SchemaRoot:
        """Parse a schema XDM root element into a SchemaRoot model."""
        self._extract_namespaces(root_element)

        version = root_element.get('version', '7.0')

        # Navigate to the v:ctr MODULE-DEF inside the wrapper structure
        # Structure: d:ctr AUTOSAR → d:lst TOP-LEVEL-PACKAGES → d:ctr AR-PACKAGE
        #            → d:lst ELEMENTS → d:chc → v:ctr MODULE-DEF
        xpath_d = self._xpath_d
        xpath_v = self._xpath_v

        top_lst = root_element.find(f'.//{xpath_d}lst[@type="TOP-LEVEL-PACKAGES"]')
        if top_lst is None:
            raise ValueError("Cannot find TOP-LEVEL-PACKAGES in schema XDM")

        ar_pkg = top_lst.find(f'{xpath_d}ctr[@type="AR-PACKAGE"]')
        if ar_pkg is None:
            raise ValueError("Cannot find AR-PACKAGE in schema XDM")

        ar_pkg_name = ar_pkg.get('name', '')
        elements_lst = ar_pkg.find(f'{xpath_d}lst[@type="ELEMENTS"]')
        if elements_lst is None:
            raise ValueError("Cannot find ELEMENTS list in schema XDM")

        chc = elements_lst.find(f'{xpath_d}chc')
        if chc is None:
            raise ValueError("Cannot find choice element in schema XDM")

        module_name = chc.get('name', 'Unknown')
        module_def_elem = chc.find(f'{xpath_v}ctr[@type="MODULE-DEF"]')
        if module_def_elem is None:
            raise ValueError("Cannot find MODULE-DEF in schema XDM")

        module_def = self._parse_ctr(module_def_elem)

        return SchemaRoot(
            module_name=module_name,
            module_def=module_def,
            version=version,
            namespaces=dict(self.nsmap),
            ar_package_name=ar_pkg_name,
        )

    def _extract_namespaces(self, element: ET.Element) -> None:
        """Extract namespace mappings from element tag attributes."""
        # ET stores namespaces in tag as Clark notation: {uri}localname
        # We need to find them from the raw XML or from known patterns
        # Since ET doesn't preserve xmlns declarations, we detect from tag format
        nsmap = {}

        # Check the element and its immediate children for namespace URIs
        tag = element.tag
        if tag.startswith('{'):
            nsmap[''] = tag[1:tag.index('}')]

        for child in element:
            tag = child.tag
            if tag.startswith('{'):
                uri = tag[1:tag.index('}')]
                nsmap['d'] = uri  # data nodes
                break

        # Find attribute namespace
        for child in element.iter():
            for attr_name in child.attrib:
                if attr_name.startswith('{'):
                    uri = attr_name[1:attr_name.index('}')]
                    if 'attribute' in uri:
                        nsmap['a'] = uri
                    elif 'schema' in uri and 'DataModel' in uri:
                        nsmap['v'] = uri
            # Also check sub-elements for v: namespace
            tag = child.tag
            if tag.startswith('{'):
                uri = tag[1:tag.index('}')]
                if 'schema' in uri and 'DataModel' in uri:
                    nsmap['v'] = uri

        self.nsmap = nsmap

    @property
    def _xpath_d(self) -> str:
        """XPath prefix for data nodes (d:)."""
        uri = self.nsmap.get('d', '')
        if uri:
            return '{%s}' % uri
        return ''

    @property
    def _xpath_v(self) -> str:
        """XPath prefix for schema nodes (v:)."""
        uri = self.nsmap.get('v', '')
        if uri:
            return '{%s}' % uri
        return ''

    @property
    def _xpath_a(self) -> str:
        """XPath prefix for attribute nodes (a:)."""
        uri = self.nsmap.get('a', '')
        if uri:
            return '{%s}' % uri
        return ''

    def _parse_ctr(self, element: ET.Element) -> SchemaCtr:
        """Parse a v:ctr element into SchemaCtr."""
        name = element.get('name', '')
        ctr_type = element.get('type', 'IDENTIFIABLE')
        name_pattern = self._get_attribute_value(element, 'NAME_PATTERN')

        children = []
        for child in element:
            local_name = self._local_tag(child.tag)
            if local_name == 'var':
                children.append(self._parse_var(child))
            elif local_name == 'ctr':
                children.append(self._parse_ctr(child))
            elif local_name == 'lst':
                children.append(self._parse_lst(child))
            elif local_name == 'ref':
                children.append(self._parse_ref(child))
            elif local_name == 'chc':
                children.append(self._parse_chc(child))

        return SchemaCtr(
            name=name,
            ctr_type=ctr_type,
            children=children,
            name_pattern=name_pattern,
        )

    def _parse_var(self, element: ET.Element) -> SchemaVar:
        """Parse a v:var element into SchemaVar."""
        name = element.get('name', '')
        var_type = element.get('type', 'STRING')
        default = self._get_da_value(element, 'DEFAULT')
        label = self._get_attribute_value(element, 'LABEL')
        range_info = self._parse_range(element)

        return SchemaVar(
            name=name,
            var_type=var_type,
            default=default,
            range_info=range_info,
            label=label,
        )

    def _parse_lst(self, element: ET.Element) -> SchemaLst:
        """Parse a v:lst element into SchemaLst."""
        name = element.get('name', '')
        lst_type = element.get('type', '')
        name_pattern = self._get_attribute_value(element, 'NAME_PATTERN')

        min_entries = 0
        min_val = self._get_da_value(element, 'MIN')
        if min_val is not None:
            min_entries = int(min_val)

        max_entries = None
        max_val = self._get_da_value(element, 'MAX')
        if max_val is not None:
            max_entries = int(max_val)

        # Parse child schema (first v: node child)
        child = None
        xpath_v = self._xpath_v
        for child_tag in ['ctr', 'var', 'ref']:
            child_elem = element.find(f'{xpath_v}{child_tag}')
            if child_elem is not None:
                if child_tag == 'ctr':
                    child = self._parse_ctr(child_elem)
                elif child_tag == 'var':
                    child = self._parse_var(child_elem)
                elif child_tag == 'ref':
                    child = self._parse_ref(child_elem)
                break

        return SchemaLst(
            name=name,
            lst_type=lst_type,
            min_entries=min_entries,
            max_entries=max_entries,
            child=child,
            name_pattern=name_pattern,
        )

    def _parse_ref(self, element: ET.Element) -> SchemaRef:
        """Parse a v:ref element into SchemaRef."""
        name = element.get('name', '')
        ref_type = element.get('type', 'REFERENCE')

        ref_targets = []
        range_targets = []

        # Parse REF data attribute
        ref_val = self._get_da_value(element, 'REF')
        if ref_val:
            ref_targets = [v.strip() for v in ref_val.split() if v.strip()]

        # Parse RANGE data attribute (may have multiple values)
        range_info = self._parse_da_multi_value(element, 'RANGE')
        if range_info:
            range_targets = range_info

        return SchemaRef(
            name=name,
            ref_type=ref_type,
            ref_targets=ref_targets,
            range_targets=range_targets,
        )

    def _parse_chc(self, element: ET.Element) -> SchemaChc:
        """Parse a v:chc element into SchemaChc."""
        name = element.get('name', '')
        chc_type = element.get('type', 'IDENTIFIABLE')

        choices = []
        xpath_v = self._xpath_v
        for ctr_elem in element.findall(f'{xpath_v}ctr'):
            choices.append(self._parse_ctr(ctr_elem))

        return SchemaChc(
            name=name,
            chc_type=chc_type,
            choices=choices,
        )

    def _parse_range(self, element: ET.Element) -> Optional[SchemaRange]:
        """Parse RANGE data attribute from a v:var element."""
        # Check for multi-value RANGE (enum values)
        range_values = self._parse_da_multi_value(element, 'RANGE')
        if not range_values:
            # Check for single-value RANGE attribute
            range_val = self._get_da_value(element, 'RANGE')
            if range_val is None:
                return None
            range_values = [range_val]

        # Determine type from content
        # Single value with dash: numeric range "0-255"
        if len(range_values) == 1:
            val = range_values[0]
            # Regex pattern for strings
            if val.startswith('~'):
                return SchemaRange(regex_pattern=val[1:])
            # Numeric range: "0-255", "<=100", ">=0"
            parsed = self._parse_numeric_range(val)
            if parsed:
                return parsed
            # Single enum value
            return SchemaRange(enum_values=[val])

        # Multiple values: enum values
        return SchemaRange(enum_values=range_values)

    def _parse_numeric_range(self, val: str) -> Optional[SchemaRange]:
        """Parse a numeric range string like '0-255', '<=100', '>=0'."""
        # Range with min-max: "0-255"
        range_pattern = re.compile(r'^(-?\d+)\s*-\s*(-?\d+)$')
        m = range_pattern.match(val)
        if m:
            return SchemaRange(min_value=float(m.group(1)), max_value=float(m.group(2)))

        return None

    def _get_da_value(self, element: ET.Element, attr_name: str) -> Optional[str]:
        """Get a:da value by name from element's direct children."""
        xpath_a = self._xpath_a
        for da in element.findall(f'{xpath_a}da'):
            if da.get('name') == attr_name:
                return da.get('value')
        return None

    def _get_attribute_value(self, element: ET.Element, attr_name: str) -> Optional[str]:
        """Get a:a value by name from element's direct children."""
        xpath_a = self._xpath_a
        for a_elem in element.findall(f'{xpath_a}a'):
            if a_elem.get('name') == attr_name:
                return a_elem.get('value')
        return None

    def _parse_da_multi_value(self, element: ET.Element, attr_name: str) -> List[str]:
        """Parse a:da with multiple a:v children."""
        xpath_a = self._xpath_a
        values = []
        for da in element.findall(f'{xpath_a}da'):
            if da.get('name') == attr_name:
                # Direct value attribute
                direct = da.get('value')
                if direct:
                    values.append(direct)
                # Child a:v elements
                for v_elem in da.findall(f'{xpath_a}v'):
                    v_text = v_elem.text
                    if v_text:
                        values.append(v_text.strip())
        return values

    @staticmethod
    def _local_tag(tag: str) -> str:
        """Extract local tag name from Clark notation {uri}localname."""
        if tag.startswith('{'):
            return tag[tag.index('}') + 1:]
        return tag
```

- [ ] **Step 4: Run tests**

Run: `pytest tests/generator/test_schema_parser.py -v`
Expected: All 8 tests PASS

- [ ] **Step 5: Commit**

```bash
git add src/eb_model/generator/schema_parser.py tests/generator/test_schema_parser.py
git commit -m "feat(generator): add schema parser for v: nodes"
```

---

### Task 3: Value Generation Strategies

**Files:**
- Create: `src/eb_model/generator/strategies.py`
- Test: `tests/generator/test_strategies.py`

Three strategies for generating values from schema metadata.

- [ ] **Step 1: Write failing tests for strategies**

Create `tests/generator/test_strategies.py`:

```python
"""Tests for value generation strategies."""
import pytest
from eb_model.generator.strategies import (
    DefaultsStrategy, BoundaryStrategy, RandomStrategy,
)
from eb_model.generator.schema_model import SchemaVar, SchemaRange, SchemaRef


class TestDefaultsStrategy:
    def setup_method(self):
        self.strategy = DefaultsStrategy()

    def test_boolean_default(self):
        var = SchemaVar(name="Test", var_type="BOOLEAN", default="true")
        assert self.strategy.generateValue(var) == "true"

    def test_integer_default(self):
        var = SchemaVar(name="Test", var_type="INTEGER", default="42")
        assert self.strategy.generateValue(var) == "42"

    def test_float_default(self):
        var = SchemaVar(name="Test", var_type="FLOAT", default="3.14")
        assert self.strategy.generateValue(var) == "3.14"

    def test_string_default(self):
        var = SchemaVar(name="Test", var_type="STRING", default="hello")
        assert self.strategy.generateValue(var) == "hello"

    def test_enum_default(self):
        var = SchemaVar(name="Test", var_type="ENUMERATION", default="VariantA")
        assert self.strategy.generateValue(var) == "VariantA"

    def test_function_name_default(self):
        var = SchemaVar(name="Test", var_type="FUNCTION-NAME", default="MyFunc")
        assert self.strategy.generateValue(var) == "MyFunc"

    def test_no_default_boolean(self):
        var = SchemaVar(name="Test", var_type="BOOLEAN")
        assert self.strategy.generateValue(var) == "false"

    def test_no_default_integer(self):
        var = SchemaVar(name="Test", var_type="INTEGER")
        assert self.strategy.generateValue(var) == "0"

    def test_no_default_string(self):
        var = SchemaVar(name="Test", var_type="STRING")
        assert self.strategy.generateValue(var) == ""

    def test_no_default_enum_with_range(self):
        var = SchemaVar(name="Test", var_type="ENUMERATION",
                        range_info=SchemaRange(enum_values=["A", "B"]))
        assert self.strategy.generateValue(var) == "A"

    def test_reference_default(self):
        ref = SchemaRef(name="TestRef", ref_type="REFERENCE",
                        ref_targets=["ASPathDataOfSchema:/Mod/Cfg/Target"])
        result = self.strategy.generateRefValue(ref)
        assert result is not None
        assert "ASPath:" in result

    def test_reference_no_target(self):
        ref = SchemaRef(name="TestRef", ref_type="REFERENCE")
        result = self.strategy.generateRefValue(ref)
        assert result is None


class TestBoundaryStrategy:
    def setup_method(self):
        self.strategy = BoundaryStrategy()

    def test_boolean_boundary(self):
        var = SchemaVar(name="Test", var_type="BOOLEAN")
        # Boundary returns "true" for boolean
        assert self.strategy.generateValue(var) == "true"

    def test_integer_with_range(self):
        var = SchemaVar(name="Test", var_type="INTEGER",
                        range_info=SchemaRange(min_value=0, max_value=255))
        val = self.strategy.generateValue(var)
        assert int(val) == 0  # Boundary: min value

    def test_integer_no_range(self):
        var = SchemaVar(name="Test", var_type="INTEGER")
        assert self.strategy.generateValue(var) == "0"

    def test_enum_boundary_first(self):
        var = SchemaVar(name="Test", var_type="ENUMERATION",
                        range_info=SchemaRange(enum_values=["A", "B", "C"]))
        val = self.strategy.generateValue(var)
        assert val == "A"


class TestRandomStrategy:
    def setup_method(self):
        self.strategy = RandomStrategy(seed=42)

    def test_boolean_random(self):
        var = SchemaVar(name="Test", var_type="BOOLEAN")
        val = self.strategy.generateValue(var)
        assert val in ("true", "false")

    def test_integer_random_in_range(self):
        var = SchemaVar(name="Test", var_type="INTEGER",
                        range_info=SchemaRange(min_value=0, max_value=100))
        val = int(self.strategy.generateValue(var))
        assert 0 <= val <= 100

    def test_integer_random_no_range(self):
        var = SchemaVar(name="Test", var_type="INTEGER")
        val = self.strategy.generateValue(var)
        assert isinstance(int(val), int)

    def test_enum_random_from_range(self):
        var = SchemaVar(name="Test", var_type="ENUMERATION",
                        range_info=SchemaRange(enum_values=["X", "Y", "Z"]))
        val = self.strategy.generateValue(var)
        assert val in ("X", "Y", "Z")

    def test_seeded_reproducible(self):
        var = SchemaVar(name="Test", var_type="INTEGER",
                        range_info=SchemaRange(min_value=0, max_value=1000))
        s1 = RandomStrategy(seed=123)
        s2 = RandomStrategy(seed=123)
        assert s1.generateValue(var) == s2.generateValue(var)

    def test_string_random(self):
        var = SchemaVar(name="Test", var_type="STRING")
        val = self.strategy.generateValue(var)
        assert isinstance(val, str)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/generator/test_strategies.py -v`
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement strategies**

Create `src/eb_model/generator/strategies.py`:

```python
"""Value generation strategies for XDM model data.

Implements: SWR_GEN_00003 (Generation Strategies)
"""

import random
import re
import string
from typing import Optional

from .schema_model import SchemaRange, SchemaRef, SchemaVar


_TYPE_DEFAULTS = {
    'BOOLEAN': 'false',
    'INTEGER': '0',
    'FLOAT': '0.0',
    'STRING': '',
    'ENUMERATION': '',
    'FUNCTION-NAME': '',
    'MULTILINE-STRING': '',
    'LINKER-SYMBOL': '',
}


class DefaultsStrategy:
    """Generate values using DEFAULT attributes from schema."""

    def generateValue(self, var: SchemaVar) -> str:
        """Generate a value for a schema variable using its default."""
        if var.default is not None:
            return var.default
        # Type-specific fallback
        if var.var_type == 'ENUMERATION' and var.range_info and var.range_info.enum_values:
            return var.range_info.enum_values[0]
        return _TYPE_DEFAULTS.get(var.var_type, '')

    def generateRefValue(self, ref: SchemaRef) -> Optional[str]:
        """Generate a mock ASPath reference value."""
        if not ref.ref_targets:
            return None
        target = ref.ref_targets[0]
        # Convert ASPathDataOfSchema:/path to ASPath:/path
        mock_path = re.sub(r'^ASPath\w*:', 'ASPath:', target)
        # Strip module prefix for simpler mock
        return mock_path


class BoundaryStrategy:
    """Generate boundary values (min, max, edge cases)."""

    def generateValue(self, var: SchemaVar) -> str:
        """Generate a boundary value for a schema variable."""
        if var.var_type == 'BOOLEAN':
            return 'true'

        if var.var_type in ('INTEGER', 'FLOAT'):
            if var.range_info and var.range_info.min_value is not None:
                return str(int(var.range_info.min_value))
            return '0'

        if var.var_type == 'ENUMERATION':
            if var.range_info and var.range_info.enum_values:
                return var.range_info.enum_values[0]
            return var.default or ''

        if var.var_type in ('STRING', 'MULTILINE-STRING'):
            return ''

        if var.var_type in ('FUNCTION-NAME', 'LINKER-SYMBOL'):
            return 'Func_%s' % var.name

        return var.default or ''

    def generateRefValue(self, ref: SchemaRef) -> Optional[str]:
        """Generate a mock ASPath reference value."""
        if not ref.ref_targets:
            return None
        target = ref.ref_targets[0]
        mock_path = re.sub(r'^ASPath\w*:', 'ASPath:', target)
        return mock_path


class RandomStrategy:
    """Generate random valid values within RANGE constraints."""

    def __init__(self, seed: Optional[int] = None) -> None:
        self.rng = random.Random(seed)

    def generateValue(self, var: SchemaVar) -> str:
        """Generate a random value for a schema variable."""
        if var.var_type == 'BOOLEAN':
            return 'true' if self.rng.random() > 0.5 else 'false'

        if var.var_type == 'INTEGER':
            min_val = int(var.range_info.min_value) if var.range_info and var.range_info.min_value is not None else 0
            max_val = int(var.range_info.max_value) if var.range_info and var.range_info.max_value is not None else 100
            if min_val > max_val:
                max_val = min_val + 100
            return str(self.rng.randint(min_val, max_val))

        if var.var_type == 'FLOAT':
            min_val = var.range_info.min_value if var.range_info and var.range_info.min_value is not None else 0.0
            max_val = var.range_info.max_value if var.range_info and var.range_info.max_value is not None else 100.0
            return str(round(self.rng.uniform(min_val, max_val), 6))

        if var.var_type == 'ENUMERATION':
            if var.range_info and var.range_info.enum_values:
                return self.rng.choice(var.range_info.enum_values)
            return var.default or ''

        if var.var_type in ('STRING', 'MULTILINE-STRING'):
            length = self.rng.randint(0, 10)
            return ''.join(self.rng.choices(string.ascii_letters + string.digits, k=length))

        if var.var_type in ('FUNCTION-NAME', 'LINKER-SYMBOL'):
            prefix = self.rng.choice(['Func', 'Cb', 'Hook', 'Notify'])
            return '%s_%s' % (prefix, var.name)

        return var.default or ''

    def generateRefValue(self, ref: SchemaRef) -> Optional[str]:
        """Generate a mock ASPath reference value."""
        if not ref.ref_targets:
            return None
        target = self.rng.choice(ref.ref_targets)
        mock_path = re.sub(r'^ASPath\w*:', 'ASPath:', target)
        return mock_path
```

- [ ] **Step 4: Run tests**

Run: `pytest tests/generator/test_strategies.py -v`
Expected: All tests PASS

- [ ] **Step 5: Commit**

```bash
git add src/eb_model/generator/strategies.py tests/generator/test_strategies.py
git commit -m "feat(generator): add value generation strategies"
```

---

### Task 4: Data Generator

**Files:**
- Create: `src/eb_model/generator/data_generator.py`
- Test: `tests/generator/test_data_generator.py`

Converts schema model into a `d:` element tree and serializes to XML.

- [ ] **Step 1: Write failing tests for data generator**

Create `tests/generator/test_data_generator.py`:

```python
"""Tests for data generator."""
import xml.etree.ElementTree as ET
from eb_model.generator.schema_model import (
    SchemaVar, SchemaCtr, SchemaLst, SchemaRef, SchemaChc, SchemaRange, SchemaRoot,
)
from eb_model.generator.data_generator import DataGenerator
from eb_model.generator.strategies import DefaultsStrategy


class TestDataGeneratorBasic:
    def _make_root(self, children=None):
        """Create a minimal SchemaRoot for testing."""
        module_def = SchemaCtr(name="TestMod", ctr_type="MODULE-DEF", children=children or [])
        return SchemaRoot(
            module_name="TestMod",
            module_def=module_def,
            version="7.0",
            namespaces={
                '': 'http://www.tresos.de/_projects/DataModel2/16/root.xsd',
                'a': 'http://www.tresos.de/_projects/DataModel2/16/attribute.xsd',
                'v': 'http://www.tresos.de/_projects/DataModel2/06/schema.xsd',
                'd': 'http://www.tresos.de/_projects/DataModel2/06/data.xsd',
            },
            ar_package_name="TestPkg",
        )

    def test_generate_simple_var(self):
        root = self._make_root([
            SchemaVar(name="TestBool", var_type="BOOLEAN", default="true"),
        ])
        gen = DataGenerator(DefaultsStrategy())
        tree = gen.generate(root)
        xml_str = gen.toString(tree)
        assert 'name="TestBool"' in xml_str
        assert 'value="true"' in xml_str
        assert '<d:var' in xml_str

    def test_generate_container_with_children(self):
        root = self._make_root([
            SchemaCtr(name="General", ctr_type="IDENTIFIABLE", children=[
                SchemaVar(name="Enabled", var_type="BOOLEAN", default="true"),
                SchemaVar(name="Count", var_type="INTEGER", default="5"),
            ]),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert '<d:ctr name="General"' in xml_str
        assert 'name="Enabled"' in xml_str
        assert 'value="true"' in xml_str
        assert 'name="Count"' in xml_str
        assert 'value="5"' in xml_str

    def test_generate_list_with_entries(self):
        root = self._make_root([
            SchemaLst(name="Items", lst_type="MAP", min_entries=2, max_entries=5,
                      child=SchemaCtr(name="Item", ctr_type="IDENTIFIABLE", children=[
                          SchemaVar(name="Val", var_type="INTEGER", default="0"),
                      ])),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        # Should have 2 entries (min_entries)
        assert xml_str.count('name="Item_') >= 2

    def test_generate_reference(self):
        root = self._make_root([
            SchemaRef(name="TargetRef", ref_type="REFERENCE",
                      ref_targets=["ASPathDataOfSchema:/TestMod/Cfg/Target"]),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert '<d:ref' in xml_str
        assert 'name="TargetRef"' in xml_str

    def test_generate_choice_first_option(self):
        root = self._make_root([
            SchemaChc(name="Action", chc_type="IDENTIFIABLE", choices=[
                SchemaCtr(name="OptionA", ctr_type="IDENTIFIABLE", children=[
                    SchemaVar(name="ValA", var_type="BOOLEAN", default="true"),
                ]),
                SchemaCtr(name="OptionB", ctr_type="IDENTIFIABLE", children=[
                    SchemaVar(name="ValB", var_type="BOOLEAN", default="false"),
                ]),
            ]),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert '<d:chc' in xml_str
        # Should contain OptionA (first choice)
        assert 'OptionA' in xml_str

    def test_output_has_wrapper_structure(self):
        root = self._make_root([])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert '<datamodel' in xml_str
        assert 'TOP-LEVEL-PACKAGES' in xml_str
        assert 'AR-PACKAGE' in xml_str
        assert 'MODULE-CONFIGURATION' in xml_str

    def test_output_valid_xml(self):
        root = self._make_root([
            SchemaVar(name="TestInt", var_type="INTEGER", default="42"),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        # Should parse without error
        parsed = ET.fromstring(xml_str)
        assert parsed is not None
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/generator/test_data_generator.py -v`
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement DataGenerator**

Create `src/eb_model/generator/data_generator.py`:

```python
"""Generate model XDM data tree from schema model.

Implements: SWR_GEN_00004 (Data Generator)
"""

import xml.etree.ElementTree as ET
from typing import Optional

from .schema_model import (
    SchemaChc, SchemaCtr, SchemaLst, SchemaRef, SchemaRoot, SchemaVar,
)
from .strategies import DefaultsStrategy


# Standard XDM namespaces
_XDM_NS = {
    '': 'http://www.tresos.de/_projects/DataModel2/16/root.xsd',
    'a': 'http://www.tresos.de/_projects/DataModel2/16/attribute.xsd',
    'v': 'http://www.tresos.de/_projects/DataModel2/06/schema.xsd',
    'd': 'http://www.tresos.de/_projects/DataModel2/06/data.xsd',
}

_D_NS = '{http://www.tresos.de/_projects/DataModel2/06/data.xsd}'
_A_NS = '{http://www.tresos.de/_projects/DataModel2/16/attribute.xsd}'

# Additional namespaces for the root ctr
_EXTRA_NS = (
    'xmlns:ad="http://www.tresos.de/_projects/DataModel2/08/admindata.xsd" '
    'xmlns:ce="http://www.tresos.de/_projects/DataModel2/18/childenable.xsd" '
    'xmlns:cd="http://www.tresos.de/_projects/DataModel2/08/customdata.xsd" '
    'xmlns:f="http://www.tresos.de/_projects/DataModel2/14/formulaexpr.xsd" '
    'xmlns:icc="http://www.tresos.de/_projects/DataModel2/08/implconfigclass.xsd" '
    'xmlns:mt="http://www.tresos.de/_projects/DataModel2/11/multitest.xsd" '
    'xmlns:variant="http://www.tresos.de/_projects/DataModel2/11/variant.xsd"'
)


class DataGenerator:
    """Generate d: element tree from schema model."""

    def __init__(self, strategy=None, list_entries: Optional[int] = None) -> None:
        self.strategy = strategy or DefaultsStrategy()
        self.list_entries = list_entries

    def generate(self, schema_root: SchemaRoot) -> ET.ElementTree:
        """Generate a complete model XDM element tree from schema root."""
        # Use namespace URIs from the schema if available
        ns = schema_root.namespaces or _XDM_NS

        d_ns = ns.get('d', '')
        d_prefix = '{%s}' % d_ns if d_ns else ''
        a_ns = ns.get('a', '')
        a_prefix = '{%s}' % a_ns if a_ns else ''

        # Build datamodel root
        datamodel = ET.Element('datamodel')
        datamodel.set('version', schema_root.version)

        # Register namespaces for proper serialization
        for prefix, uri in ns.items():
            ET.register_namespace(prefix, uri)

        # d:ctr AUTOSAR wrapper
        root_ctr = ET.SubElement(datamodel, '%sctr' % d_prefix)
        root_ctr.set('type', 'AUTOSAR')
        root_ctr.set('factory', 'autosar')

        # d:lst TOP-LEVEL-PACKAGES
        top_lst = ET.SubElement(root_ctr, '%slst' % d_prefix)
        top_lst.set('type', 'TOP-LEVEL-PACKAGES')

        # d:ctr AR-PACKAGE
        pkg_ctr = ET.SubElement(top_lst, '%sctr' % d_prefix)
        pkg_ctr.set('name', schema_root.module_name)
        pkg_ctr.set('type', 'AR-PACKAGE')

        # d:lst ELEMENTS
        elements_lst = ET.SubElement(pkg_ctr, '%slst' % d_prefix)
        elements_lst.set('type', 'ELEMENTS')

        # d:chc MODULE-CONFIGURATION
        chc = ET.SubElement(elements_lst, '%schc' % d_prefix)
        chc.set('name', schema_root.module_name)
        chc.set('type', 'AR-ELEMENT')
        chc.set('value', 'MODULE-CONFIGURATION')

        # d:ctr MODULE-CONFIGURATION
        mod_ctr = ET.SubElement(chc, '%sctr' % d_prefix)
        mod_ctr.set('type', 'MODULE-CONFIGURATION')

        # Generate content from schema
        if schema_root.module_def:
            self._generate_children(schema_root.module_def.children, mod_ctr, d_prefix, a_prefix)

        return ET.ElementTree(datamodel)

    def _generate_children(self, children, parent_elem, d_prefix: str, a_prefix: str) -> None:
        """Generate d: elements for schema children."""
        for child in children:
            if isinstance(child, SchemaVar):
                self._generate_var(child, parent_elem, d_prefix, a_prefix)
            elif isinstance(child, SchemaCtr):
                self._generate_ctr(child, parent_elem, d_prefix, a_prefix)
            elif isinstance(child, SchemaLst):
                self._generate_lst(child, parent_elem, d_prefix, a_prefix)
            elif isinstance(child, SchemaRef):
                self._generate_ref(child, parent_elem, d_prefix, a_prefix)
            elif isinstance(child, SchemaChc):
                self._generate_chc(child, parent_elem, d_prefix, a_prefix)

    def _generate_var(self, var: SchemaVar, parent: ET.Element, d_prefix: str, a_prefix: str) -> None:
        """Generate a d:var element."""
        elem = ET.SubElement(parent, '%svar' % d_prefix)
        elem.set('name', var.name)
        elem.set('type', var.var_type)
        value = self.strategy.generateValue(var)
        if value:
            elem.set('value', value)

    def _generate_ctr(self, ctr: SchemaCtr, parent: ET.Element, d_prefix: str, a_prefix: str) -> None:
        """Generate a d:ctr element."""
        elem = ET.SubElement(parent, '%sctr' % d_prefix)
        elem.set('name', ctr.name)
        elem.set('type', ctr.ctr_type)
        self._generate_children(ctr.children, elem, d_prefix, a_prefix)

    def _generate_lst(self, lst: SchemaLst, parent: ET.Element, d_prefix: str, a_prefix: str) -> None:
        """Generate a d:lst element with entries."""
        elem = ET.SubElement(parent, '%slst' % d_prefix)
        elem.set('name', lst.name)
        if lst.lst_type:
            elem.set('type', lst.lst_type)

        # Determine number of entries
        num_entries = lst.min_entries
        if self.list_entries is not None:
            num_entries = min(self.list_entries, lst.max_entries or self.list_entries)

        # Generate entries
        if lst.child and num_entries > 0:
            for i in range(num_entries):
                name = '%s_%d' % (lst.child.name, i) if lst.name_pattern is None else lst.name_pattern.replace('?', str(i))
                if isinstance(lst.child, SchemaCtr):
                    # Create a named copy of the child template
                    entry = SchemaCtr(
                        name=name,
                        ctr_type=lst.child.ctr_type,
                        children=list(lst.child.children),
                        name_pattern=lst.child.name_pattern,
                    )
                    self._generate_ctr(entry, elem, d_prefix, a_prefix)
                elif isinstance(lst.child, SchemaVar):
                    entry = SchemaVar(
                        name=name,
                        var_type=lst.child.var_type,
                        default=lst.child.default,
                        range_info=lst.child.range_info,
                    )
                    self._generate_var(entry, elem, d_prefix, a_prefix)
                elif isinstance(lst.child, SchemaRef):
                    entry = SchemaRef(
                        name=name,
                        ref_type=lst.child.ref_type,
                        ref_targets=list(lst.child.ref_targets),
                    )
                    self._generate_ref(entry, elem, d_prefix, a_prefix)

    def _generate_ref(self, ref: SchemaRef, parent: ET.Element, d_prefix: str, a_prefix: str) -> None:
        """Generate a d:ref element."""
        elem = ET.SubElement(parent, '%sref' % d_prefix)
        elem.set('name', ref.name)
        elem.set('type', ref.ref_type)
        value = self.strategy.generateRefValue(ref)
        if value:
            elem.set('value', value)

    def _generate_chc(self, chc: SchemaChc, parent: ET.Element, d_prefix: str, a_prefix: str) -> None:
        """Generate a d:chc element using first choice."""
        elem = ET.SubElement(parent, '%schc' % d_prefix)
        elem.set('name', chc.name)
        elem.set('type', chc.chc_type)

        if chc.choices:
            # Use first choice
            first = chc.choices[0]
            self._generate_ctr(first, elem, d_prefix, a_prefix)

    def toString(self, tree: ET.ElementTree) -> str:
        """Serialize element tree to XML string."""
        ET.indent(tree, space='  ')
        root = tree.getroot()

        # Build XML string manually to preserve namespace prefixes
        # ET.tostring with proper namespace registration
        xml_bytes = ET.tostring(root, encoding='unicode', xml_declaration=False)

        # Add XML declaration
        return "<?xml version='1.0'?>\n" + xml_bytes
```

- [ ] **Step 4: Run tests**

Run: `pytest tests/generator/test_data_generator.py -v`
Expected: All 7 tests PASS

- [ ] **Step 5: Commit**

```bash
git add src/eb_model/generator/data_generator.py tests/generator/test_data_generator.py
git commit -m "feat(generator): add data generator for d: nodes"
```

---

### Task 5: CLI Entry Point

**Files:**
- Create: `src/eb_model/generator/cli.py`
- Modify: `pyproject.toml` (add entry point)

- [ ] **Step 1: Write the CLI**

Create `src/eb_model/generator/cli.py`:

```python
"""CLI entry point for XDM model generator.

Implements: SWR_GEN_00005 (CLI)
"""

import argparse
import sys
import xml.etree.ElementTree as ET

from .schema_parser import SchemaParser
from .data_generator import DataGenerator
from .strategies import DefaultsStrategy, BoundaryStrategy, RandomStrategy


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        prog='model-xdm-generator',
        description='Generate model (instance) XDM files from schema XDM files for testing.',
    )
    parser.add_argument(
        'input',
        help='Path to the schema XDM file',
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output path for the generated model XDM file',
    )
    parser.add_argument(
        '--variant',
        choices=['defaults', 'boundary', 'random'],
        default='defaults',
        help='Value generation variant (default: defaults)',
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=None,
        help='Random seed for reproducible output (used with --variant random)',
    )
    parser.add_argument(
        '--list-entries',
        type=int,
        default=None,
        help='Number of entries per list (overrides MIN from schema)',
    )
    return parser


def get_strategy(variant: str, seed=None):
    """Get the appropriate strategy for the variant."""
    if variant == 'defaults':
        return DefaultsStrategy()
    elif variant == 'boundary':
        return BoundaryStrategy()
    elif variant == 'random':
        return RandomStrategy(seed=seed)
    raise ValueError("Unknown variant: %s" % variant)


def main(args=None) -> int:
    """Main entry point."""
    parser = create_parser()
    opts = parser.parse_args(args)

    # Parse schema
    schema_parser = SchemaParser()
    try:
        tree = ET.parse(opts.input)
        schema_root = schema_parser.parse(tree.getroot())
    except Exception as e:
        print("Error parsing schema XDM: %s" % str(e), file=sys.stderr)
        return 1

    # Create strategy
    strategy = get_strategy(opts.variant, opts.seed)

    # Generate model
    generator = DataGenerator(strategy=strategy, list_entries=opts.list_entries)
    result_tree = generator.generate(schema_root)

    # Write output
    xml_str = generator.toString(result_tree)
    try:
        with open(opts.output, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        print("Generated model XDM: %s" % opts.output)
    except Exception as e:
        print("Error writing output: %s" % str(e), file=sys.stderr)
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
```

- [ ] **Step 2: Add entry point to pyproject.toml**

Add to `pyproject.toml` in the `[project.scripts]` section (after the `eb-convert` line):

```toml
model-xdm-generator = "eb_model.generator.cli:main"
```

- [ ] **Step 3: Test CLI manually**

```bash
pip install -e .
model-xdm-generator doc/canif/schema/CanIf.xdm -o /tmp/CanIf_test.xdm --variant defaults
cat /tmp/CanIf_test.xdm | head -30
```

Expected: Generated XDM file with `d:var` nodes containing default values.

- [ ] **Step 4: Commit**

```bash
git add src/eb_model/generator/cli.py pyproject.toml
git commit -m "feat(generator): add CLI entry point for model-xdm-generator"
```

---

### Task 6: Integration Test with CanIf Schema

**Files:**
- Test: `tests/generator/test_integration.py`

Verify generated CanIf model XDM is parseable by existing `eb-convert` infrastructure.

- [ ] **Step 1: Write integration test**

Create `tests/generator/test_integration.py`:

```python
"""Integration tests for XDM model generator.

Tests that generated model XDM files are parseable by existing parsers.
"""
import os
import tempfile
import xml.etree.ElementTree as ET
import pytest

from eb_model.generator.schema_parser import SchemaParser
from eb_model.generator.data_generator import DataGenerator
from eb_model.generator.strategies import DefaultsStrategy, BoundaryStrategy, RandomStrategy


SCHEMA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'doc')
CANIF_SCHEMA = os.path.join(SCHEMA_DIR, 'canif', 'schema', 'CanIf.xdm')
OS_SCHEMA = os.path.join(SCHEMA_DIR, 'os', 'schema', 'Os.xdm')


def _schema_exists(path):
    """Check if schema file exists (skip test if not)."""
    return os.path.isfile(path)


class TestCanIfGeneration:
    @pytest.mark.skipif(not _schema_exists(CANIF_SCHEMA), reason="CanIf schema not available")
    def test_parse_canif_schema(self):
        """Schema parser can read the CanIf schema XDM."""
        tree = ET.parse(CANIF_SCHEMA)
        parser = SchemaParser()
        root = parser.parse(tree.getroot())
        assert root.module_name == "CanIf"
        assert root.module_def is not None
        assert len(root.module_def.children) > 0

    @pytest.mark.skipif(not _schema_exists(CANIF_SCHEMA), reason="CanIf schema not available")
    def test_generate_canif_defaults(self):
        """Generate CanIf model XDM with defaults variant."""
        tree = ET.parse(CANIF_SCHEMA)
        parser = SchemaParser()
        schema_root = parser.parse(tree.getroot())

        gen = DataGenerator(DefaultsStrategy())
        result = gen.generate(schema_root)
        xml_str = gen.toString(result)

        # Verify output is valid XML
        parsed = ET.fromstring(xml_str)
        assert parsed is not None
        assert 'CanIf' in xml_str

    @pytest.mark.skipif(not _schema_exists(CANIF_SCHEMA), reason="CanIf schema not available")
    def test_generate_canif_boundary(self):
        """Generate CanIf model XDM with boundary variant."""
        tree = ET.parse(CANIF_SCHEMA)
        parser = SchemaParser()
        schema_root = parser.parse(tree.getroot())

        gen = DataGenerator(BoundaryStrategy())
        result = gen.generate(schema_root)
        xml_str = gen.toString(result)

        parsed = ET.fromstring(xml_str)
        assert parsed is not None

    @pytest.mark.skipif(not _schema_exists(CANIF_SCHEMA), reason="CanIf schema not available")
    def test_generate_canif_random(self):
        """Generate CanIf model XDM with random variant (seeded)."""
        tree = ET.parse(CANIF_SCHEMA)
        parser = SchemaParser()
        schema_root = parser.parse(tree.getroot())

        gen = DataGenerator(RandomStrategy(seed=42))
        result = gen.generate(schema_root)
        xml_str = gen.toString(result)

        parsed = ET.fromstring(xml_str)
        assert parsed is not None

    @pytest.mark.skipif(not _schema_exists(CANIF_SCHEMA), reason="CanIf schema not available")
    def test_generate_canif_write_file(self):
        """Write generated CanIf XDM to file."""
        tree = ET.parse(CANIF_SCHEMA)
        parser = SchemaParser()
        schema_root = parser.parse(tree.getroot())

        gen = DataGenerator(DefaultsStrategy())
        result_tree = gen.generate(schema_root)
        xml_str = gen.toString(result_tree)

        with tempfile.NamedTemporaryFile(mode='w', suffix='.xdm', delete=False) as f:
            f.write(xml_str)
            tmp_path = f.name

        try:
            # Verify file is readable
            parsed = ET.parse(tmp_path)
            assert parsed.getroot() is not None
        finally:
            os.unlink(tmp_path)


class TestOsGeneration:
    @pytest.mark.skipif(not _schema_exists(OS_SCHEMA), reason="Os schema not available")
    def test_parse_os_schema(self):
        """Schema parser can read the Os schema XDM (different namespace version)."""
        tree = ET.parse(OS_SCHEMA)
        parser = SchemaParser()
        root = parser.parse(tree.getroot())
        assert root.module_name == "Os"
        assert root.module_def is not None
        assert len(root.module_def.children) > 0

    @pytest.mark.skipif(not _schema_exists(OS_SCHEMA), reason="Os schema not available")
    def test_generate_os_defaults(self):
        """Generate Os model XDM with defaults variant."""
        tree = ET.parse(OS_SCHEMA)
        parser = SchemaParser()
        schema_root = parser.parse(tree.getroot())

        gen = DataGenerator(DefaultsStrategy())
        result = gen.generate(schema_root)
        xml_str = gen.toString(result)

        parsed = ET.fromstring(xml_str)
        assert parsed is not None
        assert 'Os' in xml_str

    @pytest.mark.skipif(not _schema_exists(OS_SCHEMA), reason="Os schema not available")
    def test_generate_os_all_variants(self):
        """Generate Os model XDM with all variants."""
        tree = ET.parse(OS_SCHEMA)
        parser = SchemaParser()
        schema_root = parser.parse(tree.getroot())

        for strategy in [DefaultsStrategy(), BoundaryStrategy(), RandomStrategy(seed=42)]:
            gen = DataGenerator(strategy)
            result = gen.generate(schema_root)
            xml_str = gen.toString(result)
            parsed = ET.fromstring(xml_str)
            assert parsed is not None
```

- [ ] **Step 2: Run integration tests**

Run: `pytest tests/generator/test_integration.py -v`
Expected: All CanIf and Os tests PASS

- [ ] **Step 3: Commit**

```bash
git add tests/generator/test_integration.py
git commit -m "test(generator): add integration tests for CanIf and Os schema"
```

---

### Task 7: eb-convert Verification

**Files:**
- Test: `tests/generator/test_eb_convert_verification.py`

End-to-end test: generate → eb-convert → verify Excel output.

- [ ] **Step 1: Write eb-convert verification test**

Create `tests/generator/test_eb_convert_verification.py`:

```python
"""End-to-end verification: generate XDM → parse with eb-convert → verify output.

Implements: SWR_GEN_00006 (eb-convert Verification)
"""
import os
import subprocess
import tempfile
import xml.etree.ElementTree as ET
import pytest

from eb_model.generator.schema_parser import SchemaParser
from eb_model.generator.data_generator import DataGenerator
from eb_model.generator.strategies import DefaultsStrategy, BoundaryStrategy, RandomStrategy


SCHEMA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'doc')
CANIF_SCHEMA = os.path.join(SCHEMA_DIR, 'canif', 'schema', 'CanIf.xdm')
OS_SCHEMA = os.path.join(SCHEMA_DIR, 'os', 'schema', 'Os.xdm')


def _schema_exists(path):
    return os.path.isfile(path)


def _generate_xdm(schema_path, strategy):
    """Generate model XDM from schema and return temp file path."""
    tree = ET.parse(schema_path)
    parser = SchemaParser()
    schema_root = parser.parse(tree.getroot())
    gen = DataGenerator(strategy)
    result_tree = gen.generate(schema_root)
    xml_str = gen.toString(result_tree)

    tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.xdm', delete=False)
    tmp.write(xml_str)
    tmp.close()
    return tmp.name


class TestEbConvertVerification:
    @pytest.mark.integration
    @pytest.mark.skipif(not _schema_exists(CANIF_SCHEMA), reason="CanIf schema not available")
    def test_canif_defaults_eb_convert(self):
        """Generate CanIf defaults → eb-convert → verify exit code 0."""
        xdm_path = _generate_xdm(CANIF_SCHEMA, DefaultsStrategy())
        xlsx_path = tempfile.mktemp(suffix='.xlsx')
        try:
            result = subprocess.run(
                ['eb-convert', xdm_path, '-o', xlsx_path],
                capture_output=True, text=True, timeout=30,
            )
            assert result.returncode == 0, "eb-convert failed: %s" % result.stderr
            assert os.path.exists(xlsx_path), "Output Excel file not created"
            assert os.path.getsize(xlsx_path) > 0, "Output Excel file is empty"
        finally:
            if os.path.exists(xdm_path):
                os.unlink(xdm_path)
            if os.path.exists(xlsx_path):
                os.unlink(xlsx_path)

    @pytest.mark.integration
    @pytest.mark.skipif(not _schema_exists(OS_SCHEMA), reason="Os schema not available")
    def test_os_defaults_eb_convert(self):
        """Generate Os defaults → eb-convert → verify exit code 0."""
        xdm_path = _generate_xdm(OS_SCHEMA, DefaultsStrategy())
        xlsx_path = tempfile.mktemp(suffix='.xlsx')
        try:
            result = subprocess.run(
                ['eb-convert', xdm_path, '-o', xlsx_path],
                capture_output=True, text=True, timeout=30,
            )
            assert result.returncode == 0, "eb-convert failed: %s" % result.stderr
            assert os.path.exists(xlsx_path), "Output Excel file not created"
            assert os.path.getsize(xlsx_path) > 0, "Output Excel file is empty"
        finally:
            if os.path.exists(xdm_path):
                os.unlink(xdm_path)
            if os.path.exists(xlsx_path):
                os.unlink(xlsx_path)

    @pytest.mark.integration
    @pytest.mark.skipif(not _schema_exists(CANIF_SCHEMA), reason="CanIf schema not available")
    def test_canif_all_variants_eb_convert(self):
        """Generate CanIf with all variants → eb-convert → verify each."""
        for strategy in [DefaultsStrategy(), BoundaryStrategy(), RandomStrategy(seed=42)]:
            xdm_path = _generate_xdm(CANIF_SCHEMA, strategy)
            xlsx_path = tempfile.mktemp(suffix='.xlsx')
            try:
                result = subprocess.run(
                    ['eb-convert', xdm_path, '-o', xlsx_path],
                    capture_output=True, text=True, timeout=30,
                )
                assert result.returncode == 0, \
                    "eb-convert failed for %s: %s" % (type(strategy).__name__, result.stderr)
            finally:
                if os.path.exists(xdm_path):
                    os.unlink(xdm_path)
                if os.path.exists(xlsx_path):
                    os.unlink(xlsx_path)
```

- [ ] **Step 2: Run unit-level tests first**

Run: `pytest tests/generator/ -v -m "not integration"`
Expected: All unit tests PASS

- [ ] **Step 3: Run integration tests (may need manual eb-convert verification)**

Run: `pytest tests/generator/test_eb_convert_verification.py -v`
Expected: Tests pass if generated XDM is valid and eb-convert succeeds. May need fixes if generated XDM structure doesn't match parser expectations — fix iteratively.

- [ ] **Step 4: Commit**

```bash
git add tests/generator/test_eb_convert_verification.py
git commit -m "test(generator): add eb-convert end-to-end verification tests"
```

---

## Plan Self-Review

### Spec Coverage

| Spec Section | Task |
|---|---|
| SchemaParser | Task 2 |
| Schema Model | Task 1 |
| DataGenerator | Task 4 |
| Strategies (defaults/boundary/random) | Task 3 |
| CLI (model-xdm-generator) | Task 5 |
| Namespace handling | Task 2, Task 4 |
| RANGE parsing | Task 2, Task 3 |
| List generation | Task 4 |
| Reference generation | Task 3, Task 4 |
| Choice generation | Task 4 |
| CanIf verification | Task 6, Task 7 |
| Os verification | Task 6, Task 7 |
| eb-convert verification | Task 7 |

### Placeholder Scan

No TBD, TODO, "implement later", or vague steps found. All steps contain exact code.

### Type Consistency

- `SchemaVar`, `SchemaCtr`, `SchemaLst`, `SchemaRef`, `SchemaChc` — used consistently across all tasks
- `DefaultsStrategy`, `BoundaryStrategy`, `RandomStrategy` — all have `generateValue(var)` and `generateRefValue(ref)` methods
- `DataGenerator.__init__(strategy, list_entries)` — consistent with CLI usage
- `SchemaParser.parse(element) -> SchemaRoot` — consistent across all test and production code
