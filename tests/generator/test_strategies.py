"""Tests for value generation strategies."""
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
        assert self.strategy.generateValue(var) == "true"

    def test_integer_with_range(self):
        var = SchemaVar(name="Test", var_type="INTEGER",
                        range_info=SchemaRange(min_value=0, max_value=255))
        val = self.strategy.generateValue(var)
        assert int(val) == 0

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
