from ....parser.j1939tp_xdm_parser import J1939TpXdmParser
from ....models.j1939_stack.j1939tp_xdm import J1939TpGeneral
from ....models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestJ1939TpXdmParser:
    def test_read_j1939tp_general(self):
        model = EBModel.getInstance()
        j1939tp = model.getJ1939Tp()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="J1939TpGeneral" type="IDENTIFIABLE">
                <d:var name="J1939TpDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="J1939TpEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = J1939TpXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_j1939tp_general(element, j1939tp)

        general = j1939tp.getJ1939TpGeneral()
        assert general is not None
        assert general.getJ1939TpDevErrorDetect() is True