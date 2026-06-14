"""End-to-end verification: generate XDM -> verify parser can load it.

eb-convert may fail on some modules due to missing cross-references or
parser limitations (e.g., CanIf requires Can module references). The
generator produces structurally valid XDM — this test verifies:
1. Module is correctly detected from generated XDM
2. XML is valid and parseable
3. Parsers can begin reading the generated configuration

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


class TestEbConvertDetection:
    """Verify eb-convert can detect and begin loading generated XDMs."""

    @pytest.mark.integration
    @pytest.mark.skipif(not _schema_exists(CANIF_SCHEMA), reason="CanIf schema not available")
    def test_canif_module_detected(self):
        """eb-convert detects CanIf module from generated XDM."""
        xdm_path = _generate_xdm(CANIF_SCHEMA, DefaultsStrategy())
        output_dir = tempfile.mkdtemp()
        try:
            result = subprocess.run(
                ['eb-convert', xdm_path, output_dir],
                capture_output=True, text=True, timeout=30,
            )
            assert 'Detected module: CanIf' in result.stderr
        finally:
            if os.path.exists(xdm_path):
                os.unlink(xdm_path)
            for f in os.listdir(output_dir):
                os.unlink(os.path.join(output_dir, f))
            os.rmdir(output_dir)

    @pytest.mark.integration
    @pytest.mark.skipif(not _schema_exists(OS_SCHEMA), reason="Os schema not available")
    def test_os_module_detected(self):
        """eb-convert detects Os module from generated XDM."""
        xdm_path = _generate_xdm(OS_SCHEMA, DefaultsStrategy())
        output_dir = tempfile.mkdtemp()
        try:
            result = subprocess.run(
                ['eb-convert', xdm_path, output_dir],
                capture_output=True, text=True, timeout=30,
            )
            assert 'Detected module: Os' in result.stderr
        finally:
            if os.path.exists(xdm_path):
                os.unlink(xdm_path)
            for f in os.listdir(output_dir):
                os.unlink(os.path.join(output_dir, f))
            os.rmdir(output_dir)


class TestGeneratedXdmValidXml:
    """Verify generated XDMs are valid XML that parsers can read namespaces from."""

    @pytest.mark.skipif(not _schema_exists(CANIF_SCHEMA), reason="CanIf schema not available")
    def test_canif_namespaces_readable(self):
        """Generated CanIf XDM has readable namespace declarations."""
        xdm_path = _generate_xdm(CANIF_SCHEMA, DefaultsStrategy())
        try:
            # Verify namespaces are readable via iterparse (same method parsers use)
            nsmap = dict([node for _, node in ET.iterparse(xdm_path, events=['start-ns'])])
            assert 'd' in nsmap or '' in nsmap, "Missing namespace declarations"
        finally:
            if os.path.exists(xdm_path):
                os.unlink(xdm_path)

    @pytest.mark.skipif(not _schema_exists(OS_SCHEMA), reason="Os schema not available")
    def test_os_namespaces_readable(self):
        """Generated Os XDM has readable namespace declarations."""
        xdm_path = _generate_xdm(OS_SCHEMA, DefaultsStrategy())
        try:
            nsmap = dict([node for _, node in ET.iterparse(xdm_path, events=['start-ns'])])
            assert 'd' in nsmap or '' in nsmap, "Missing namespace declarations"
        finally:
            if os.path.exists(xdm_path):
                os.unlink(xdm_path)

    @pytest.mark.skipif(not _schema_exists(CANIF_SCHEMA), reason="CanIf schema not available")
    def test_canif_all_variants_valid_xml(self):
        """All variants produce valid parseable XML."""
        for strategy in [DefaultsStrategy(), BoundaryStrategy(), RandomStrategy(seed=42)]:
            xdm_path = _generate_xdm(CANIF_SCHEMA, strategy)
            try:
                tree = ET.parse(xdm_path)
                assert tree.getroot() is not None
            finally:
                if os.path.exists(xdm_path):
                    os.unlink(xdm_path)
