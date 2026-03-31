from eb_model.parser.j1939_stack.j1939dcm_xdm_parser import J1939DcmXdmParser
from eb_model.models.j1939_stack.j1939dcm_xdm import J1939DcmGeneral
from eb_model.models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestJ1939DcmXdmParser:
    def test_read_j1939dcm_general(self):
        model = EBModel.getInstance()
        j1939dcm = model.getJ1939Dcm()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="J1939DcmGeneral" type="IDENTIFIABLE">
                <d:var name="J1939DcmDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="J1939DcmEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = J1939DcmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_j1939dcm_general(element, j1939dcm)

        general = j1939dcm.getJ1939DcmGeneral()
        assert general is not None
        assert general.getJ1939DcmDevErrorDetect() is True
