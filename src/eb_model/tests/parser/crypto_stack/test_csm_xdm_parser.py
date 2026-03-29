from ....parser.csm_xdm_parser import CsmXdmParser
from ....models.crypto_stack.csm_xdm import CsmGeneral
from ....models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestCsmXdmParser:
    def test_read_csm_general(self):
        model = EBModel.getInstance()
        csm = model.getCsm()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CsmGeneral" type="IDENTIFIABLE">
                <d:var name="CsmDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="CsmEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = CsmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_csm_general(element, csm)

        general = csm.getCsmGeneral()
        assert general is not None
        assert general.getCsmDevErrorDetect() is True