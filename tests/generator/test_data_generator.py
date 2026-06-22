"""Tests for data generator."""
import xml.etree.ElementTree as ET
from eb_model.generator.schema_model import (
    SchemaVar, SchemaCtr, SchemaLst, SchemaRef, SchemaChc, SchemaRange, SchemaRoot,
)
from eb_model.generator.data_generator import DataGenerator
from eb_model.generator.strategies import DefaultsStrategy, CombinedStrategy


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

    def test_multiple_configuration_container_wrapped_in_lst(self):
        """Standalone v:ctr type=MULTIPLE-CONFIGURATION-CONTAINER emitted as d:lst > d:ctr."""
        root = self._make_root([
            SchemaCtr(name="MultiCfg", ctr_type="MULTIPLE-CONFIGURATION-CONTAINER", children=[
                SchemaVar(name="Val", var_type="BOOLEAN", default="true"),
            ]),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        parsed = ET.fromstring(xml_str)
        # Find the d:ctr type=MULTIPLE-CONFIGURATION-CONTAINER
        ns = {'d': 'http://www.tresos.de/_projects/DataModel2/06/data.xsd'}
        ctrs = parsed.findall('.//d:ctr[@type="MULTIPLE-CONFIGURATION-CONTAINER"]', ns)
        assert len(ctrs) == 1, "MULTIPLE-CONFIGURATION-CONTAINER ctr must be emitted"
        # Its parent must be a d:lst (the auto-wrap), not the MODULE-CONFIGURATION ctr
        parent = self._find_parent(parsed, ctrs[0])
        assert parent is not None
        assert parent.tag.endswith('}lst'), \
            "MULTIPLE-CONFIGURATION-CONTAINER ctr must be wrapped in d:lst, got parent: %s" % parent.tag

    @staticmethod
    def _find_parent(root, target):
        """Walk tree to find parent of target element."""
        for elem in root.iter():
            for child in elem:
                if child is target:
                    return elem
        return None

    def test_var_with_derived_emits_derived_attribute(self):
        """v:var with DERIVED=true produces d:var with a:a DERIVED=true child."""
        root = self._make_root([
            SchemaVar(name="Computed", var_type="INTEGER", derived="true"),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert 'name="DERIVED"' in xml_str
        assert 'value="true"' in xml_str

    def test_var_without_derived_omits_derived_attribute(self):
        """v:var without derived does not emit DERIVED attribute."""
        root = self._make_root([
            SchemaVar(name="Plain", var_type="INTEGER", default="5"),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert 'name="DERIVED"' not in xml_str

    def test_var_with_non_one_multiplicity_wrapped_in_lst(self):
        """v:var with LOWER-MULTIPLICITY != 1 emitted wrapped in d:lst (XDM Spec 5.2.5)."""
        root = self._make_root([
            SchemaVar(name="Multi", var_type="INTEGER", default="0",
                      lower_multiplicity=2, upper_multiplicity=5),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        parsed = ET.fromstring(xml_str)
        ns = {'d': 'http://www.tresos.de/_projects/DataModel2/06/data.xsd'}
        lst = parsed.find('.//d:lst[@name="Multi"]', ns)
        assert lst is not None, "var with non-1 multiplicity must be wrapped in d:lst"
        # Verify multiplicity was honored: at least min (2) entries
        vars_in_lst = lst.findall('d:var', ns)
        assert len(vars_in_lst) >= 2

    def test_var_with_unit_multiplicity_not_wrapped(self):
        """v:var with no multiplicity (default 1) is NOT wrapped in d:lst."""
        root = self._make_root([
            SchemaVar(name="Single", var_type="INTEGER", default="0"),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert '<d:lst name="Single"' not in xml_str

    def test_instance_ctr_emits_target_context(self):
        """v:ctr type=INSTANCE with target/context emits a:da TARGET/CONTEXT."""
        root = self._make_root([
            SchemaCtr(name="OsTask", ctr_type="INSTANCE",
                      target="ASPathDataOfSchema:/TestMod/OsTask",
                      context="ASPath:/TestMod/OsConfig"),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert 'name="TARGET"' in xml_str
        assert 'ASPathDataOfSchema:/TestMod/OsTask' in xml_str
        assert 'name="CONTEXT"' in xml_str
        assert 'ASPath:/TestMod/OsConfig' in xml_str

    def test_chc_empty_type_defaults_to_identifiable_for_modern_schema(self):
        """v:chc with empty type under DataModel2/16 defaults to IDENTIFIABLE (AUTOSAR 3.x+)."""
        root = self._make_root([
            SchemaChc(name="Action", chc_type="", choices=[
                SchemaCtr(name="OptionA", ctr_type="IDENTIFIABLE"),
            ]),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert 'type="IDENTIFIABLE"' in xml_str

    def test_chc_empty_type_defaults_to_choice_for_legacy_schema(self):
        """v:chc with empty type under DataModel2/08 defaults to CHOICE (AUTOSAR 2.x)."""
        module_def = SchemaCtr(name="TestMod", ctr_type="MODULE-DEF", children=[
            SchemaChc(name="Action", chc_type="", choices=[
                SchemaCtr(name="OptionA", ctr_type="IDENTIFIABLE"),
            ]),
        ])
        root = SchemaRoot(
            module_name="TestMod",
            module_def=module_def,
            version="7.0",
            namespaces={
                '': 'http://www.tresos.de/_projects/DataModel2/08/root.xsd',
                'a': 'http://www.tresos.de/_projects/DataModel2/08/attribute.xsd',
                'v': 'http://www.tresos.de/_projects/DataModel2/08/schema.xsd',
                'd': 'http://www.tresos.de/_projects/DataModel2/08/data.xsd',
            },
            ar_package_name="TestPkg",
        )
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert 'type="CHOICE"' in xml_str


class TestDataGeneratorCombined:
    """Tests for combined variant data generation."""

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

    def test_list_min_zero_generates_two(self):
        """List with min=0 generates 2 entries for combined variant."""
        root = self._make_root([
            SchemaLst(name="Items", lst_type="MAP", min_entries=0, max_entries=10,
                      child=SchemaCtr(name="Item", ctr_type="IDENTIFIABLE", children=[
                          SchemaVar(name="Val", var_type="INTEGER", default="0"),
                      ])),
        ])
        gen = DataGenerator(CombinedStrategy(seed=42))
        xml_str = gen.toString(gen.generate(root))
        assert xml_str.count('name="Item_') == 2

    def test_list_with_min_generates_extra(self):
        """List with min=1 generates min+2=3 entries for combined variant."""
        root = self._make_root([
            SchemaLst(name="Items", lst_type="MAP", min_entries=1, max_entries=10,
                      child=SchemaCtr(name="Item", ctr_type="IDENTIFIABLE", children=[
                          SchemaVar(name="Val", var_type="INTEGER", default="0"),
                      ])),
        ])
        gen = DataGenerator(CombinedStrategy(seed=42))
        xml_str = gen.toString(gen.generate(root))
        assert xml_str.count('name="Item_') == 3

    def test_optional_list_min_zero_max_one_combined_emits_single_entry_with_enable(self):
        """Optional list (MIN=0, MAX=1) under Combined: 1 entry with ENABLE=true (XDM Spec 5.2.5.1)."""
        root = self._make_root([
            SchemaLst(name="OptItem", lst_type="MAP", min_entries=0, max_entries=1,
                      child=SchemaCtr(name="Item", ctr_type="IDENTIFIABLE", children=[
                          SchemaVar(name="Val", var_type="INTEGER", default="0"),
                      ])),
        ])
        gen = DataGenerator(CombinedStrategy(seed=42))
        xml_str = gen.toString(gen.generate(root))
        assert xml_str.count('name="Item_') == 1
        assert 'name="ENABLE"' in xml_str

    def test_optional_list_min_zero_max_one_defaults_emits_zero_entries(self):
        """Optional list (MIN=0, MAX=1) under Defaults: 0 entries (stays inactive)."""
        root = self._make_root([
            SchemaLst(name="OptItem", lst_type="MAP", min_entries=0, max_entries=1,
                      child=SchemaCtr(name="Item", ctr_type="IDENTIFIABLE", children=[
                          SchemaVar(name="Val", var_type="INTEGER", default="0"),
                      ])),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert xml_str.count('name="Item_') == 0

    def test_choice_generates_all_options(self):
        """Choice generates all options for combined variant."""
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
        gen = DataGenerator(CombinedStrategy(seed=42))
        xml_str = gen.toString(gen.generate(root))
        # Count chc elements with name="Action" (there are 2 for the 2 options)
        assert xml_str.count('name="Action"') == 2
        assert 'OptionA' in xml_str
        assert 'OptionB' in xml_str

    def test_optional_items_have_enable(self):
        """Combined variant adds ENABLE=true to optional var items."""
        root = self._make_root([
            SchemaVar(name="TestBool", var_type="BOOLEAN", default="true", optional="true"),
        ])
        gen = DataGenerator(CombinedStrategy(seed=42))
        xml_str = gen.toString(gen.generate(root))
        assert 'name="ENABLE"' in xml_str
        assert 'value="true"' in xml_str

    def test_non_optional_var_omits_enable(self):
        """Combined variant does not add ENABLE to non-optional vars."""
        root = self._make_root([
            SchemaVar(name="Plain", var_type="BOOLEAN", default="true"),
        ])
        gen = DataGenerator(CombinedStrategy(seed=42))
        xml_str = gen.toString(gen.generate(root))
        assert 'name="ENABLE"' not in xml_str

    def test_container_has_enable(self):
        """Combined variant adds ENABLE=true to optional containers."""
        root = self._make_root([
            SchemaCtr(name="General", ctr_type="IDENTIFIABLE", optional="true", children=[
                SchemaVar(name="Enabled", var_type="BOOLEAN", default="true"),
            ]),
        ])
        gen = DataGenerator(CombinedStrategy(seed=42))
        xml_str = gen.toString(gen.generate(root))
        assert 'name="ENABLE"' in xml_str
        assert 'value="true"' in xml_str

    def test_non_optional_container_omits_enable(self):
        """Combined variant does not add ENABLE to non-optional containers."""
        root = self._make_root([
            SchemaCtr(name="General", ctr_type="IDENTIFIABLE", children=[
                SchemaVar(name="Enabled", var_type="BOOLEAN", default="true"),
            ]),
        ])
        gen = DataGenerator(CombinedStrategy(seed=42))
        xml_str = gen.toString(gen.generate(root))
        assert 'name="ENABLE"' not in xml_str

    def test_reference_has_enable(self):
        """Combined variant adds ENABLE=true to optional references."""
        root = self._make_root([
            SchemaRef(name="TargetRef", ref_type="REFERENCE", optional="true",
                      ref_targets=["ASPathDataOfSchema:/TestMod/Cfg/Target"]),
        ])
        gen = DataGenerator(CombinedStrategy(seed=42))
        xml_str = gen.toString(gen.generate(root))
        assert 'name="ENABLE"' in xml_str
        assert 'value="true"' in xml_str

    def test_non_optional_reference_omits_enable(self):
        """Combined variant does not add ENABLE to non-optional references."""
        root = self._make_root([
            SchemaRef(name="TargetRef", ref_type="REFERENCE",
                      ref_targets=["ASPathDataOfSchema:/TestMod/Cfg/Target"]),
        ])
        gen = DataGenerator(CombinedStrategy(seed=42))
        xml_str = gen.toString(gen.generate(root))
        assert 'name="ENABLE"' not in xml_str


class TestDataGeneratorConfigAlignment:
    """Tests asserting generator output aligns with doc/config authentic format.

    See docs/usage/model-xdm-generator.md "Output Format Principles" section.
    Alignment covers schema version, namespaces, IMPORTER_INFO, ENABLE format,
    and ref value handling. Concrete data values may legitimately differ.
    """

    @staticmethod
    def _make_legacy_root(children=None):
        """Create SchemaRoot declaring legacy DataModel2/08 / version 3.0."""
        module_def = SchemaCtr(name="TestMod", ctr_type="MODULE-DEF", children=children or [])
        return SchemaRoot(
            module_name="TestMod",
            module_def=module_def,
            version="3.0",
            namespaces={
                '': 'http://www.tresos.de/_projects/DataModel2/08/root.xsd',
                'a': 'http://www.tresos.de/_projects/DataModel2/08/attribute.xsd',
                'v': 'http://www.tresos.de/_projects/DataModel2/08/schema.xsd',
                'd': 'http://www.tresos.de/_projects/DataModel2/08/data.xsd',
            },
            ar_package_name="TestPkg",
        )

    def test_output_version_always_7_regardless_of_schema_source(self):
        """datamodel version forced to 7.0 even when schema source is 3.0."""
        root = self._make_legacy_root([])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert 'version="7.0"' in xml_str
        assert 'version="3.0"' not in xml_str

    def test_output_namespaces_always_data_model_16(self):
        """Output uses DataModel2/16 URIs even when schema source is DataModel2/08."""
        root = self._make_legacy_root([])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        # Main datamodel element should use DataModel2/16
        assert 'DataModel2/16/root.xsd' in xml_str
        assert 'DataModel2/16/attribute.xsd' in xml_str
        # AUTOSAR container may have additional namespaces with older versions
        # (admindata, childenable, customdata, formulaexpr, implconfigclass, multitest, variant)
        # These are legitimate EB Tresos namespaces and should be allowed
        # We only check that the main namespaces (root, attribute) are DataModel2/16
        assert 'xmlns="http://www.tresos.de/_projects/DataModel2/16/root.xsd"' in xml_str
        assert 'xmlns:a="http://www.tresos.de/_projects/DataModel2/16/attribute.xsd"' in xml_str

    def test_importer_info_def_emitted_on_defaulted_var(self):
        """Var whose value came from schema DEFAULT emits IMPORTER_INFO=@DEF."""
        root = self._make_legacy_root([
            SchemaVar(name="Enabled", var_type="BOOLEAN", default="true"),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert 'name="IMPORTER_INFO"' in xml_str
        assert 'value="@DEF"' in xml_str

    def test_importer_info_def_not_emitted_when_no_default(self):
        """Var without schema DEFAULT (strategy falls back to type default) does not emit @DEF.

        Rationale: @DEF marks values pulled from schema DEFAULT. Type-based fallback
        values are not schema-declared defaults, so generator cannot soundly claim @DEF.
        """
        root = self._make_legacy_root([
            SchemaVar(name="Plain", var_type="INTEGER"),  # no default
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert 'name="IMPORTER_INFO"' not in xml_str

    def test_importer_info_emitted_after_enable_attribute(self):
        """IMPORTER_INFO comes after ENABLE in <a:a> child order (matches config)."""
        root = self._make_legacy_root([
            SchemaVar(name="Opt", var_type="BOOLEAN", default="true", optional="true"),
        ])
        gen = DataGenerator(CombinedStrategy(seed=42))
        xml_str = gen.toString(gen.generate(root))
        enable_idx = xml_str.find('name="ENABLE"')
        importer_idx = xml_str.find('name="IMPORTER_INFO"')
        assert enable_idx != -1
        assert importer_idx != -1
        assert enable_idx < importer_idx

    def test_enable_false_emitted_on_skipped_optional_var_defaults(self):
        """Optional var skipped by DefaultsStrategy emits ENABLE=false."""
        root = self._make_legacy_root([
            SchemaVar(name="Opt", var_type="BOOLEAN", default="true", optional="true"),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        parsed = ET.fromstring(xml_str)
        ns = {'a': 'http://www.tresos.de/_projects/DataModel2/16/attribute.xsd',
              'd': 'http://www.tresos.de/_projects/DataModel2/06/data.xsd'}
        opt_var = parsed.find('.//d:var[@name="Opt"]', ns)
        assert opt_var is not None, "Optional var must still be emitted with ENABLE=false"
        enable_attr = opt_var.find('a:a[@name="ENABLE"]', ns)
        assert enable_attr is not None, "ENABLE attribute must be present on skipped optional"
        assert enable_attr.get('value') == 'false'

    def test_enable_uses_a_tag_not_da_tag_in_output(self):
        """ENABLE attribute always on <a:a> tag, never <a:da>."""
        root = self._make_legacy_root([
            SchemaVar(name="Opt", var_type="BOOLEAN", default="true", optional="true"),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        assert '<a:a name="ENABLE"' in xml_str
        assert '<a:da name="ENABLE"' not in xml_str

    def test_ref_to_autosar_ecuc_defs_emitted_without_value(self):
        """Ref whose schema REF target contains AUTOSAR/EcucDefs emitted with no value."""
        root = self._make_legacy_root([
            SchemaRef(name="OsAlarmCounterRef", ref_type="REFERENCE",
                      ref_targets=["ASPathDataOfSchema:/AUTOSAR/EcucDefs/Os/OsCounter"]),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        parsed = ET.fromstring(xml_str)
        ns = {'d': 'http://www.tresos.de/_projects/DataModel2/06/data.xsd'}
        ref = parsed.find('.//d:ref[@name="OsAlarmCounterRef"]', ns)
        assert ref is not None
        assert ref.get('value') is None, \
            "Ref to AUTOSAR/EcucDefs must not have value attribute, got: %s" % ref.get('value')

    def test_ref_to_concrete_path_still_emits_value(self):
        """Ref whose schema REF target is a concrete config path emits transformed value."""
        root = self._make_legacy_root([
            SchemaRef(name="CanIfInitRefCfgSet", ref_type="REFERENCE",
                      ref_targets=["ASPathDataOfSchema:/Can/Can/CanConfigSet"]),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        parsed = ET.fromstring(xml_str)
        ns = {'d': 'http://www.tresos.de/_projects/DataModel2/06/data.xsd'}
        ref = parsed.find('.//d:ref[@name="CanIfInitRefCfgSet"]', ns)
        assert ref is not None
        assert ref.get('value') == 'ASPath:/Can/Can/CanConfigSet'

    def test_no_autosar_ecuc_defs_in_emitted_ref_values(self):
        """Whole output must contain no AUTOSAR/EcucDefs in any emitted ref value.

        Authentic config never carries schema-definition paths in ref values.
        """
        root = self._make_legacy_root([
            SchemaRef(name="Ref1", ref_type="REFERENCE",
                      ref_targets=["ASPathDataOfSchema:/AUTOSAR/EcucDefs/Os/OsTask"]),
            SchemaRef(name="Ref2", ref_type="REFERENCE",
                      ref_targets=["ASPathDataOfSchema:/AUTOSAR/EcucDefs/Os/OsAlarm"]),
        ])
        gen = DataGenerator(DefaultsStrategy())
        xml_str = gen.toString(gen.generate(root))
        # No value="ASPath:/AUTOSAR/EcucDefs/..." substring allowed anywhere
        assert 'ASPath:/AUTOSAR/EcucDefs' not in xml_str
