from eb_model.parser.core.tm_xdm_parser import TmXdmParser
from eb_model.models.core.tm_xdm import Tm, TmGeneral, TmInterruptSynchronization, TmTickTime, TmTrigger
from eb_model.models.core.eb_doc import EBModel

import xml.etree.ElementTree as ET
import pytest


class TestTmXdmParser:
    def test_read_tm_general(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="TmGeneral" type="IDENTIFIABLE">
                <d:var name="TmDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="TmMainWindowProtect" type="BOOLEAN" value="false"/>
                <d:var name="TmVersionInfoApi" type="BOOLEAN" value="true"/>
                <d:var name="TmEnablePredefTimer1us16bit" type="BOOLEAN" value="true"/>
                <d:var name="TmEnablePredefTimer1us24bit" type="BOOLEAN" value="false"/>
                <d:var name="TmEnablePredefTimer1us32bit" type="BOOLEAN" value="false"/>
                <d:var name="TmEnablePredefTimer100us32bit" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock Tm object
        model = EBModel.getInstance()
        tm = model.getTm()

        # Create parser instance
        parser = TmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_tm_general(element, tm)

        # Assertions
        general = tm.getTmGeneral()
        assert general is not None
        assert general.getTmDevErrorDetect() is True
        assert general.getTmMainWindowProtect() is False
        assert general.getTmVersionInfoApi() is True
        assert general.getTmEnablePredefTimer1us16bit() is True
        assert general.getTmEnablePredefTimer1us24bit() is False
        assert general.getTmEnablePredefTimer1us32bit() is False
        assert general.getTmEnablePredefTimer100us32bit() is True

    def test_read_tm_interrupt_synchronization(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="TmInterruptSynchronization" type="IDENTIFIABLE">
                <d:var name="TmSyncMode" type="ENUMERATION" value="SYNCHRONOUS"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock Tm object
        model = EBModel.getInstance()
        tm = model.getTm()

        # Create parser instance
        parser = TmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_tm_interrupt_synchronization(element, tm)

        # Assertions
        sync = tm.getTmInterruptSynchronization()
        assert sync is not None
        assert sync.getTmSyncMode() == "SYNCHRONOUS"

    def test_read_tm_tick_time(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="TmTickTime" type="IDENTIFIABLE">
                <d:var name="TmTickTimeBase" type="INTEGER" value="1000"/>
                <d:var name="TmTickPriority" type="INTEGER" value="10"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock Tm object
        model = EBModel.getInstance()
        tm = model.getTm()

        # Create parser instance
        parser = TmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_tm_tick_time(element, tm)

        # Assertions
        tick_time = tm.getTmTickTime()
        assert tick_time is not None
        assert tick_time.getTmTickTimeBase() == 1000
        assert tick_time.getTmTickPriority() == 10

    def test_read_tm_triggers(self):

        # Create a mock XML element for testing
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="TmTrigger" type="MAP">
                <d:ctr name="Trigger1">
                    <d:ref name="TmTriggerChannelRef" type="REFERENCE" value="ASPath:/Gpt/Gpt/Channel1"/>
                </d:ctr>
                <d:ctr name="Trigger2">
                    <d:ref name="TmTriggerChannelRef" type="REFERENCE" value="ASPath:/Gpt/Gpt/Channel2"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        # Mock Tm object
        model = EBModel.getInstance()
        tm = model.getTm()

        # Create parser instance
        parser = TmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_tm_triggers(element, tm)

        # Assertions
        triggers = tm.getTmTriggerList()
        assert len(triggers) == 2

        trigger1 = triggers[0]
        assert trigger1.getName() == "Trigger1"
        assert trigger1.getTmTriggerChannelRef().getValue() == "/Gpt/Gpt/Channel1"

        trigger2 = triggers[1]
        assert trigger2.getName() == "Trigger2"
        assert trigger2.getTmTriggerChannelRef().getValue() == "/Gpt/Gpt/Channel2"

    def test_read_common_published_information(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CommonPublishedInformation" type="IDENTIFIABLE">
                <d:var name="ArMajorVersion" type="INTEGER" value="4"/>
                <d:var name="ArMinorVersion" type="INTEGER" value="3"/>
                <d:var name="ArPatchVersion" type="INTEGER" value="0"/>
                <d:var name="SwMajorVersion" type="INTEGER" value="1"/>
                <d:var name="SwMinorVersion" type="INTEGER" value="0"/>
                <d:var name="SwPatchVersion" type="INTEGER" value="0"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        tm = model.getTm()

        parser = TmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_common_published_information(element, tm)

        pub_info = tm.getCommonPublishedInformation()
        assert pub_info is not None
        assert pub_info.getArMajorVersion() == 4
        assert pub_info.getArMinorVersion() == 3
        assert pub_info.getArPatchVersion() == 0
        assert pub_info.getSwMajorVersion() == 1
        assert pub_info.getSwMinorVersion() == 0
        assert pub_info.getSwPatchVersion() == 0

    def test_read_published_information(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="PublishedInformation" type="IDENTIFIABLE">
                <d:var name="VendorId" type="STRING" value="Vector"/>
                <d:var name="ArReleaseMajorVersion" type="STRING" value="4"/>
                <d:var name="ArReleaseMinorVersion" type="STRING" value="3"/>
                <d:var name="ArReleasePatchVersion" type="STRING" value="0"/>
                <d:var name="SwMajorVersion" type="STRING" value="1"/>
                <d:var name="SwMinorVersion" type="STRING" value="0"/>
                <d:var name="SwPatchVersion" type="STRING" value="0"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        tm = model.getTm()

        parser = TmXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_published_information(element, tm)

        pub_info = tm.getPublishedInformation()
        assert pub_info is not None
        assert pub_info.getVendorId() == "Vector"
        assert pub_info.getArReleaseMajorVersion() == "4"
        assert pub_info.getArReleaseMinorVersion() == "3"
        assert pub_info.getArReleasePatchVersion() == "0"
        assert pub_info.getSwMajorVersion() == "1"
        assert pub_info.getSwMinorVersion() == "0"
        assert pub_info.getSwPatchVersion() == "0"
