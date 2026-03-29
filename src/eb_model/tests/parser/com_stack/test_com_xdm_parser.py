import xml.etree.ElementTree as ET
from ....parser.com_xdm_parser import ComXdmParser
from ....models.com_stack.com_xdm import Com, ComGeneral
from ....models.core.eb_doc import EBModel


class TestComXdmParser:
    def test_read_com_general(self):
        model = EBModel.getInstance()
        com = model.getCom()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="ComConfig" type="IDENTIFIABLE">
                <d:var name="ComEnableUserSupport" type="BOOLEAN" value="true"/>
                <d:var name="ComUserInitSignal" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = ComXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_com_general(element, com)

        general = com.getComGeneral()
        assert general is not None
        assert general.getComEnableUserSupport() is True
        assert general.getComUserInitSignal() is True
