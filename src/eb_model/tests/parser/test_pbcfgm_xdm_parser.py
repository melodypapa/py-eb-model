from ...parser.pbcfgm_xdm_parser import PbcfgMXdmParser
from ...models.eb_doc import EBModel

import xml.etree.ElementTree as ET


class TestPbcfgMXdmParser:
    def test_read_pbcfgm_general(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="PbcfgMGeneral" type="IDENTIFIABLE">
                <d:var name="PbcfgMDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="PbcfgMInitConfiguration" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock PbcfgM object
        model = EBModel.getInstance()
        pbcfgm = model.getPbcfgM()

        # Create parser instance
        parser = PbcfgMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_pbcfgm_general(element, pbcfgm)

        # Assertions
        general = pbcfgm.getPbcfgMGeneral()
        assert general is not None
        assert general.getPbcfgMDevErrorDetect() is True
        assert general.getPbcfgMInitConfiguration() is True

    def test_read_pbcfgm_protection_sets(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="PbcfgMProtectionSet" type="MAP">
                <d:ctr name="ProtectionSet1">
                    <d:var name="PbcfgMProtectionSetName" type="STRING" value="Core0Protected"/>
                </d:ctr>
                <d:ctr name="ProtectionSet2">
                    <d:var name="PbcfgMProtectionSetName" type="STRING" value="Core1Protected"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock PbcfgM object
        model = EBModel.getInstance()
        pbcfgm = model.getPbcfgM()

        # Create parser instance
        parser = PbcfgMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_pbcfgm_protection_sets(element, pbcfgm)

        # Assertions
        protection_sets = pbcfgm.getPbcfgMProtectionSetList()
        assert len(protection_sets) == 2

        ps1 = protection_sets[0]
        assert ps1.getName() == "ProtectionSet1"
        assert ps1.getPbcfgMProtectionSetName() == "Core0Protected"

        ps2 = protection_sets[1]
        assert ps2.getName() == "ProtectionSet2"
        assert ps2.getPbcfgMProtectionSetName() == "Core1Protected"
