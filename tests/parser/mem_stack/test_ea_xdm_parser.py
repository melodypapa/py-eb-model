from eb_model.parser.mem_stack.ea_xdm_parser import EaXdmParser
from eb_model.models.mem_stack.ea_xdm import Ea, EaGeneral
from eb_model.models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestEaXdmParser:
    def test_read_ea_general(self):

        model = EBModel.getInstance()
        ea = model.getEa()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="EaGeneral" type="IDENTIFIABLE">
                <d:var name="EaDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="EaPageSize" type="INTEGER" value="8"/>
                <d:var name="EaAddressAlignment" type="INTEGER" value="8"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = EaXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_ea_general(element, ea)

        general = ea.getEaGeneral()
        assert general is not None
        assert general.getEaDevErrorDetect() is True
        assert general.getEaPageSize() == 8
        assert general.getEaAddressAlignment() == 8
