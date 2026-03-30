from eb_model.parser.core.bswm_xdm_parser import BswMXdmParser
from eb_model.models.core.bswm_xdm import BswM, BswMGeneral, BswMModeDeclaration, BswMModeCondition
from eb_model.models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET
import pytest


class TestBswMXdmParser:
    def test_read_bswm_general(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="BswMGeneral" type="IDENTIFIABLE">
                <d:var name="BswMDevErrorDetect" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock BswM object
        model = EBModel.getInstance()
        bswm = model.getBswM()

        # Create parser instance
        parser = BswMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_bswm_general(element, bswm)

        # Assertions
        general = bswm.getBswMGeneral()
        assert general is not None
        assert general.getBswMDevErrorDetect() is True

    def test_read_bswm_mode_declarations(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="BswMModeDeclaration" type="MAP">
                <d:ctr name="Mode1">
                    <d:var name="BswMAvailableForScheduler" type="BOOLEAN" value="true"/>
                    <d:var name="BswMModeType" type="ENUMERATION" value="PORT"/>
                </d:ctr>
                <d:ctr name="Mode2">
                    <d:var name="BswMAvailableForScheduler" type="BOOLEAN" value="false"/>
                    <d:var name="BswMModeType" type="ENUMERATION" value="VALUE"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock BswM object
        model = EBModel.getInstance()
        bswm = model.getBswM()

        # Create parser instance
        parser = BswMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_bswm_mode_declarations(element, bswm)

        # Assertions
        mode_declarations = bswm.getBswMModeDeclarationList()
        assert len(mode_declarations) == 2

        mode1 = mode_declarations[0]
        assert mode1.getName() == "Mode1"
        assert mode1.getBswMAvailableForScheduler() is True
        assert mode1.getBswMModeType() == "PORT"

        mode2 = mode_declarations[1]
        assert mode2.getName() == "Mode2"
        assert mode2.getBswMAvailableForScheduler() is False
        assert mode2.getBswMModeType() == "VALUE"

    def test_read_bswm_mode_conditions(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="Mode1" type="IDENTIFIABLE">
                <d:var name="BswMAvailableForScheduler" type="BOOLEAN" value="true"/>
                <d:var name="BswMModeType" type="ENUMERATION" value="PORT"/>
                <d:lst name="BswMModeCondition" type="MAP">
                    <d:ctr name="Condition1">
                        <d:ref name="BswMModeConditionSourceRef" type="REFERENCE" value="ASPath:/Os/Os/AppMode1"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock BswM object
        model = EBModel.getInstance()
        bswm = model.getBswM()

        # Create parser instance
        parser = BswMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Create mode declaration
        mode_declaration = BswMModeDeclaration(bswm, "Mode1")

        # Call the method
        parser.read_bswm_mode_conditions(element, mode_declaration)

        # Assertions
        mode_conditions = mode_declaration.getBswMModeConditionList()
        assert len(mode_conditions) == 1

        condition1 = mode_conditions[0]
        assert condition1.getName() == "Condition1"
        assert condition1.getBswMModeConditionSourceRef().getValue() == "/Os/Os/AppMode1"
