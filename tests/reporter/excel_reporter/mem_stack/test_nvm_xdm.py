"""
NvM Excel Reporter Tests.

Implements:
    - TC_UNIT_REPORTER_00017: NvM Excel Reporter - File Creation
"""
import os
import tempfile
from openpyxl import load_workbook
from eb_model.reporter.excel_reporter.mem_stack.nvm_xdm import NvMXdmXlsWriter
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.mem_stack.nvm_xdm import NvMCommon
from tests.mock_data import MOCK_NVM_XDM
import xml.etree.ElementTree as ET
from eb_model.parser.mem_stack.nvm_xdm_parser import NvMXdmParser


class TestNvMXdmXlsWriter:

    def _create_populated_doc(self):
        """Parse MOCK_NVM_XDM to create a fully populated EBModel."""
        EBModel._EBModel__instance = None
        doc = EBModel.getInstance()
        parser = NvMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }
        element = ET.fromstring(MOCK_NVM_XDM)
        parser.parse(element, doc)
        return doc

    def test_write_creates_excel_file(self):
        """Test that write() creates a valid Excel file."""
        writer = NvMXdmXlsWriter()
        doc = self._create_populated_doc()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            writer.write(filename, doc, options={})
            assert os.path.exists(filename)
            assert os.path.getsize(filename) > 0
            wb = load_workbook(filename)
            assert len(wb.sheetnames) > 0
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_general_sheet_populated(self):
        """Test General sheet contains expected data."""
        writer = NvMXdmXlsWriter()
        doc = self._create_populated_doc()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            writer.write(filename, doc, options={})
            wb = load_workbook(filename)
            ws = wb["General"]
            values = {}
            for row in ws.iter_rows(min_row=2, max_col=2, values_only=True):
                if row[0]:
                    values[row[0]] = row[1]
            assert values.get("NvMCompiledConfigId") == 1
            assert values.get("NvMDevErrorDetect") is True
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_block_list_sheet_populated(self):
        """Test Block List sheet contains block data."""
        writer = NvMXdmXlsWriter()
        doc = self._create_populated_doc()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            writer.write(filename, doc, options={})
            wb = load_workbook(filename)
            ws = wb["Block List"]
            assert ws.max_row >= 2
            block_id = ws.cell(row=2, column=1).value
            assert block_id == 1
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_bsw_distribution_sheet(self):
        """Test BSW Distribution sheet is created."""
        writer = NvMXdmXlsWriter()
        doc = self._create_populated_doc()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            writer.write(filename, doc, options={})
            wb = load_workbook(filename)
            assert "BSW Distribution" in wb.sheetnames
            ws = wb["BSW Distribution"]
            assert ws.max_row >= 1
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_write_nvm_common_none_skips_general(self):
        """Test that None NvMCommon skips General sheet safely."""
        writer = NvMXdmXlsWriter()
        EBModel._EBModel__instance = None
        doc = EBModel.getInstance()

        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
            filename = f.name

        try:
            writer.write(filename, doc, options={})
            wb = load_workbook(filename)
            assert "General" not in wb.sheetnames
            wb.close()
        finally:
            if os.path.exists(filename):
                os.remove(filename)
