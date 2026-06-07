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
        parsed = ET.fromstring(xml_str)
        assert parsed is not None
