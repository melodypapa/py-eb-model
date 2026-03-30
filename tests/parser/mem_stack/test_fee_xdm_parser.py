from eb_model.parser.mem_stack.fee_xdm_parser import FeeXdmParser
from eb_model.models.mem_stack.fee_xdm import Fee, FeeGeneral
from eb_model.models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestFeeXdmParser:
    def test_read_fee_general(self):

        model = EBModel.getInstance()
        fee = model.getFee()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="FeeGeneral" type="IDENTIFIABLE">
                <d:var name="FeeDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="FeePageSize" type="INTEGER" value="256"/>
                <d:var name="FeeVirtualPageSize" type="INTEGER" value="8"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = FeeXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_fee_general(element, fee)

        general = fee.getFeeGeneral()
        assert general is not None
        assert general.getFeeDevErrorDetect() is True
        assert general.getFeePageSize() == 256
        assert general.getFeeVirtualPageSize() == 8
