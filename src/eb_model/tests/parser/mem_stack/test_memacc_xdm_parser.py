from eb_model.parser.mem_stack.memacc_xdm_parser import MemAccXdmParser
from eb_model.models.mem_stack.memacc_xdm import MemAcc, MemAccCommon
from eb_model.models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestMemAccXdmParser:
    def test_read_memacc_common(self):

        model = EBModel.getInstance()
        memacc = model.getMemAcc()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="MemAccCommon" type="IDENTIFIABLE">
                <d:var name="MemAccDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="MemAccProtectionApi" type="ENUMERATION" value="MEMACC_PROTECTION_FALSE"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = MemAccXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_memacc_common(element, memacc)

        common = memacc.getMemAccCommon()
        assert common is not None
        assert common.getMemAccDevErrorDetect() is True
        assert common.getMemAccProtectionApi() == "MEMACC_PROTECTION_FALSE"