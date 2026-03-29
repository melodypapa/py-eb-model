from ...parser.j1939nm_xdm_parser import J1939NmXdmParser
from ...models.j1939nm_xdm import J1939NmGeneral
from ...models.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestJ1939NmXdmParser:
    def test_read_j1939nm_general(self):
        model = EBModel.getInstance()
        j1939nm = model.getJ1939Nm()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="J1939NmGeneral" type="IDENTIFIABLE">
                <d:var name="J1939NmDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="J1939NmEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = J1939NmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_j1939nm_general(element, j1939nm)

        general = j1939nm.getJ1939NmGeneral()
        assert general is not None
        assert general.getJ1939NmDevErrorDetect() is True