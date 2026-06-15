"""Tests for XDM schema parser."""
import xml.etree.ElementTree as ET
from eb_model.generator.schema_parser import SchemaParser
from eb_model.generator.schema_model import (
    SchemaVar, SchemaCtr, SchemaLst, SchemaRef, SchemaChc,
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

    def test_parse_var_with_derived(self):
        """Parse v:var with DERIVED a:a attribute."""
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
                      <v:var name="Computed" type="INTEGER">
                        <a:a name="DERIVED" value="true"/>
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
        assert isinstance(var, SchemaVar)
        assert var.derived == "true"

    def test_parse_var_with_optional(self):
        """Parse v:var with OPTIONAL a:a attribute."""
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
                      <v:var name="OptParam" type="BOOLEAN">
                        <a:a name="OPTIONAL" value="true"/>
                        <a:da name="ENABLE" value="false"/>
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
        assert isinstance(var, SchemaVar)
        assert var.optional == "true"
        assert var.enabled == "false"

    def test_parse_var_with_multiplicity(self):
        """Parse v:var with LOWER-MULTIPLICITY/UPPER-MULTIPLICITY."""
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
                      <v:var name="Multi" type="INTEGER">
                        <a:da name="LOWER-MULTIPLICITY" value="2"/>
                        <a:da name="UPPER-MULTIPLICITY" value="5"/>
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
        assert isinstance(var, SchemaVar)
        assert var.lower_multiplicity == 2
        assert var.upper_multiplicity == 5

    def test_parse_instance_ctr_with_target_context(self):
        """Parse v:ctr type=INSTANCE with TARGET and CONTEXT a:da attributes."""
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
                      <v:ctr name="OsTask" type="INSTANCE">
                        <a:da name="TARGET" value="ASPathDataOfSchema:/TestMod/OsTask"/>
                        <a:da name="CONTEXT" value="ASPath:/TestMod/OsConfig"/>
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
        assert ctr.ctr_type == "INSTANCE"
        assert ctr.target == "ASPathDataOfSchema:/TestMod/OsTask"
        assert ctr.context == "ASPath:/TestMod/OsConfig"
