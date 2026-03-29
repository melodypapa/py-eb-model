from ...parser.j1939rm_xdm_parser import J1939RmXdmParser
from ...models.j1939rm_xdm import J1939RmGeneral
from ...models.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestJ1939RmXdmParser:
    def test_read_j1939rm_general(self):
        model = EBModel.getInstance()
        j1939rm = model.getJ1939Rm()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="J1939RmGeneral" type="IDENTIFIABLE">
                <d:var name="J1939RmDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="J1939RmEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = J1939RmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_j1939rm_general(element, j1939rm)

        general = j1939rm.getJ1939RmGeneral()
        assert general is not None
        assert general.getJ1939RmDevErrorDetect() is True