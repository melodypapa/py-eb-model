"""
SecOC Parser Tests - Tests for SecOC XDM parser.
"""
from eb_model.parser.crypto_stack.secoc_xdm_parser import SecOCXdmParser
from eb_model.models.crypto_stack.secoc_xdm import SecOCGeneral
from eb_model.models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestSecOCXdmParser:
    def test_read_secoc_general(self):
        model = EBModel.getInstance()
        secoc = model.getSecOC()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="SecOCGeneral" type="IDENTIFIABLE">
                <d:var name="SecOCDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="SecOCEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = SecOCXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_secoc_general(element, secoc)

        general = secoc.getSecocGeneral()
        assert general is not None
        assert general.getSecocDevErrorDetect() is True
