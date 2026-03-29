from ....parser.cryif_xdm_parser import CryIfXdmParser
from ....models.crypto_stack.cryif_xdm import CryIfGeneral
from ....models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestCryIfXdmParser:
    def test_read_cryif_general(self):
        model = EBModel.getInstance()
        cryif = model.getCryIf()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CryIfGeneral" type="IDENTIFIABLE">
                <d:var name="CryIfDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="CryIfEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = CryIfXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_cryif_general(element, cryif)

        general = cryif.getCryIfGeneral()
        assert general is not None
        assert general.getCryIfDevErrorDetect() is True