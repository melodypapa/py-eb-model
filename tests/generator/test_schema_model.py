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
