"""
Dlt Parser Tests - Tests for Dlt XDM parser.
"""
import pytest
from eb_model.parser.diag_stack.dlt_xdm_parser import DltXdmParser
from eb_model.models.diag_stack.dlt_xdm import DltGeneral
from eb_model.models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestDltXdmParser:
    def test_read_dlt_general(self):
        model = EBModel.getInstance()
        dlt = model.getDlt()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="DltGeneral" type="IDENTIFIABLE">
                <d:var name="DltDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="DltEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = DltXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_dlt_general(element, dlt)

        general = dlt.getDltGeneral()
        assert general is not None
        assert general.getDltDevErrorDetect() is True
