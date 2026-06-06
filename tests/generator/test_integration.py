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
