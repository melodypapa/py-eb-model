from eb_model.parser.diag_stack.dem_xdm_parser import DemXdmParser
from eb_model.models.diag_stack.dem_xdm import DemGeneral
from eb_model.models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestDemXdmParser:
    def test_read_dem_general(self):
        model = EBModel.getInstance()
        dem = model.getDem()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="DemGeneral" type="IDENTIFIABLE">
                <d:var name="DemDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="DemEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = DemXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_dem_general(element, dem)

        general = dem.getDemGeneral()
        assert general is not None
        assert general.getDemDevErrorDetect() is True