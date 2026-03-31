"""
Os Parser Tests for New Containers and Attributes - Tests for OS module parser.
"""
import pytest
from eb_model.parser.core.os_xdm_parser import OsXdmParser
from eb_model.models.core.eb_doc import EBModel
from eb_model.models.core.os_xdm import (
    CommonPublishedInformation, PublishedInformation, OsHwIncrementer,
    OsEvent, OsSpinlock, OsPeripheralArea, OsOS, OsHooks, OsCoreConfig,
    OsAutosarCustomization
)
import xml.etree.ElementTree as ET


class TestOsCommonPublishedInformation:

    def test_read_common_published_information(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="CommonPublishedInformation">
                <d:var name="ArMajorVersion" type="INTEGER" value="4"/>
                <d:var name="ArMinorVersion" type="INTEGER" value="0"/>
                <d:var name="ArPatchVersion" type="INTEGER" value="3"/>
                <d:var name="SwMajorVersion" type="INTEGER" value="1"/>
                <d:var name="SwMinorVersion" type="INTEGER" value="0"/>
                <d:var name="SwPatchVersion" type="INTEGER" value="0"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_common_published_information(element, os)

        pub_info = os.getCommonPublishedInformation()
        assert pub_info is not None
        assert pub_info.getArMajorVersion() == 4
        assert pub_info.getArMinorVersion() == 0
        assert pub_info.getArPatchVersion() == 3
        assert pub_info.getSwMajorVersion() == 1
        assert pub_info.getSwMinorVersion() == 0
        assert pub_info.getSwPatchVersion() == 0


class TestOsPublishedInformation:

    def test_read_published_information(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="PublishedInformation">
                <d:var name="VendorId" type="STRING" value="EB"/>
                <d:var name="ArReleaseMajorVersion" type="STRING" value="4"/>
                <d:var name="ArReleaseMinorVersion" type="STRING" value="2"/>
                <d:var name="ArReleasePatchVersion" type="STRING" value="0"/>
                <d:var name="SwMajorVersion" type="STRING" value="1"/>
                <d:var name="SwMinorVersion" type="STRING" value="2"/>
                <d:var name="SwPatchVersion" type="STRING" value="3"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_published_information(element, os)

        pub_info = os.getPublishedInformation()
        assert pub_info is not None
        assert pub_info.getVendorId() == "EB"
        assert pub_info.getArReleaseMajorVersion() == "4"
        assert pub_info.getArReleaseMinorVersion() == "2"
        assert pub_info.getArReleasePatchVersion() == "0"
        assert pub_info.getSwMajorVersion() == "1"
        assert pub_info.getSwMinorVersion() == "2"
        assert pub_info.getSwPatchVersion() == "3"


class TestOsHwIncrementer:

    def test_read_os_hw_incrementer(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="OsHwIncrementer">
                <d:var name="OsHwIncrementerBase" type="INTEGER" value="0"/>
                <d:var name="OsHwIncrementerMax" type="INTEGER" value="65535"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_hw_incrementer(element, os)

        hw_inc = os.getOsHwIncrementer()
        assert hw_inc is not None
        assert hw_inc.getOsHwIncrementerBase() == 0
        assert hw_inc.getOsHwIncrementerMax() == 65535


class TestOsEvent:

    def test_read_os_events(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsEvent" type="MAP">
                <d:ctr name="Event1">
                    <d:var name="OsEventMask" type="INTEGER" value="1"/>
                </d:ctr>
                <d:ctr name="Event2">
                    <d:var name="OsEventMask" type="INTEGER" value="2"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_events(element, os)

        events = os.getOsEventList()
        assert len(events) == 2
        assert events[0].getName() == "Event1"
        assert events[0].getOsEventMask() == 1
        assert events[1].getName() == "Event2"
        assert events[1].getOsEventMask() == 2


class TestOsSpinlock:

    def test_read_os_spinlocks(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsSpinlock" type="MAP">
                <d:ctr name="Spinlock1">
                    <d:var name="OsSpinlockType" type="ENUMERATION" value="STANDARD"/>
                    <d:var name="OsSpinlockSpinCount" type="INTEGER" value="100"/>
                </d:ctr>
                <d:ctr name="Spinlock2">
                    <d:var name="OsSpinlockType" type="ENUMERATION" value="SCHEDULER"/>
                    <d:var name="OsSpinlockSpinCount" type="INTEGER" value="50"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_spinlocks(element, os)

        spinlocks = os.getOsSpinlockList()
        assert len(spinlocks) == 2
        assert spinlocks[0].getName() == "Spinlock1"
        assert spinlocks[0].getOsSpinlockType() == "STANDARD"
        assert spinlocks[0].getOsSpinlockSpinCount() == 100
        assert spinlocks[1].getName() == "Spinlock2"
        assert spinlocks[1].getOsSpinlockType() == "SCHEDULER"
        assert spinlocks[1].getOsSpinlockSpinCount() == 50


class TestOsOS:

    def test_read_os_os(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="OsOS">
                <d:var name="OsOSCoreAssignment" type="INTEGER" value="0"/>
                <d:var name="OsOsStackMonitoring" type="BOOLEAN" value="true"/>
                <d:var name="OsOsUseGetServiceId" type="BOOLEAN" value="false"/>
                <d:var name="OsOsUseParameterAccess" type="BOOLEAN" value="true"/>
                <d:var name="OsOsUseServiceId" type="BOOLEAN" value="false"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_os(element, os)

        os_os = os.getOsOS()
        assert os_os is not None
        assert os_os.getOsOSCoreAssignment() == 0
        assert os_os.getOsOsStackMonitoring() is True
        assert os_os.getOsOsUseGetServiceId() is False
        assert os_os.getOsOsUseParameterAccess() is True
        assert os_os.getOsOsUseServiceId() is False


class TestOsHooks:

    def test_read_os_hooks(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="OsHooks">
                <d:var name="OsErrorHook" type="BOOLEAN" value="true"/>
                <d:var name="OsShutdownHook" type="BOOLEAN" value="false"/>
                <d:var name="OsStartupHook" type="BOOLEAN" value="true"/>
                <d:var name="OsPreTaskHook" type="BOOLEAN" value="false"/>
                <d:var name="OsPostTaskHook" type="BOOLEAN" value="false"/>
                <d:var name="OsProtectionHook" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_hooks(element, os)

        hooks = os.getOsHooks()
        assert hooks is not None
        assert hooks.getOsErrorHook() is True
        assert hooks.getOsShutdownHook() is False
        assert hooks.getOsStartupHook() is True
        assert hooks.getOsPreTaskHook() is False
        assert hooks.getOsPostTaskHook() is False
        assert hooks.getOsProtectionHook() is True


class TestOsCoreConfig:

    def test_read_os_core_configs(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsCoreConfig" type="MAP">
                <d:ctr name="Core0">
                    <d:var name="OsCoreId" type="INTEGER" value="0"/>
                    <d:var name="OsCoreMainFunction" type="STRING" value="Main_Core0"/>
                    <d:var name="OsCoreStackStartAddress" type="INTEGER" value="536870912"/>
                    <d:var name="OsCoreStackSize" type="INTEGER" value="4096"/>
                </d:ctr>
                <d:ctr name="Core1">
                    <d:var name="OsCoreId" type="INTEGER" value="1"/>
                    <d:var name="OsCoreMainFunction" type="STRING" value="Main_Core1"/>
                    <d:var name="OsCoreStackStartAddress" type="INTEGER" value="536875008"/>
                    <d:var name="OsCoreStackSize" type="INTEGER" value="4096"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_core_configs(element, os)

        core_configs = os.getOsCoreConfigList()
        assert len(core_configs) == 2
        assert core_configs[0].getName() == "Core0"
        assert core_configs[0].getOsCoreId() == 0
        assert core_configs[0].getOsCoreMainFunction() == "Main_Core0"
        assert core_configs[0].getOsCoreStackStartAddress() == 536870912
        assert core_configs[0].getOsCoreStackSize() == 4096
        assert core_configs[1].getName() == "Core1"
        assert core_configs[1].getOsCoreId() == 1
        assert core_configs[1].getOsCoreMainFunction() == "Main_Core1"
        assert core_configs[1].getOsCoreStackStartAddress() == 536875008
        assert core_configs[1].getOsCoreStackSize() == 4096
        assert core_configs[1].getOsCoreStackStartAddress() == 536875008
        assert core_configs[1].getOsCoreStackSize() == 4096


class TestOsAutosarCustomization:

    def test_read_os_autosar_customization(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="OsAutosarCustomization">
                <d:var name="OsScalableClass" type="ENUMERATION" value="BCC"/>
                <d:var name="OsApplicationType" type="ENUMERATION" value="SYSTEM"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        os = model.getOs()
        parser = OsXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        parser.read_os_autosar_customization(element, os)

        customization = os.getOsAutosarCustomization()
        assert customization is not None
        assert customization.getOsScalableClass() == "BCC"
        assert customization.getOsApplicationType() == "SYSTEM"
