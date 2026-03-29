from eb_model.parser.diag_stack.fim_xdm_parser import FiMXdmParser
from eb_model.models.diag_stack.fim_xdm import FiMGeneral
from eb_model.models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestFiMXdmParser:
    def test_read_fim_general(self):
        model = EBModel.getInstance()
        fim = model.getFiM()

        xml = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="FiMGeneral" type="IDENTIFIABLE">
                <d:var name="FimDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="FimEnabled" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """

        element = ET.fromstring(xml)
        parser = FiMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_fim_general(element, fim)

        general = fim.getFimGeneral()
        assert general is not None
        assert general.getFimDevErrorDetect() is True
