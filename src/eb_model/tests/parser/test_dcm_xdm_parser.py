from ...parser.dcm_xdm_parser import DcmXdmParser
from ...models.dcm_xdm import DcmGeneral
from ...models.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestDcmXdmParser:
    def test_read_dcm_general(self):
        model = EBModel.getInstance()
        dcm = model.getDcm()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="DcmGeneral" type="IDENTIFIABLE">
                <d:var name="DcmDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="DcmEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = DcmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_dcm_general(element, dcm)

        general = dcm.getDcmGeneral()
        assert general is not None
        assert general.getDcmDevErrorDetect() is True