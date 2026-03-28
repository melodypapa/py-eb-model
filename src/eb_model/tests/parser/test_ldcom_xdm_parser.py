"""
Test module for LdCom XDM parser.

Implements:
    - SWR_LDCOM_00001: LdCom module parser tests
"""
import xml.etree.ElementTree as ET
from ...parser.ldcom_xdm_parser import LdComXdmParser
from ...models.ldcom_xdm import LdCom
from ...models.eb_doc import EBModel


class TestLdComXdmParser:
    def test_parse_ldcom(self):
        """
        Test basic LdCom module parsing.

        Implements: SWR_LDCOM_00001
        """
        model = EBModel.getInstance()
        ldcom = model.getLdCom()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:chc type="AR-ELEMENT" value="MODULE-CONFIGURATION" name="LdCom"/>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = LdComXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.parse(element, model)

        assert parser.get_component_name(element) == "LdCom"
        assert ldcom is not None