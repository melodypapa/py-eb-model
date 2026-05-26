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
                <d:var name="PbcfgMSupport" type="BOOLEAN" value="false"/>
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
        assert pub_info.getPbcfgMSupport() is False


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
                    <d:var name="OsSpinlockLockMethod" type="ENUMERATION" value="STANDARD"/>
                    <d:ref name="OsSpinlockSuccessor" type="REFERENCE" value="ASPath:/Os/Spinlock2"/>
                    <d:lst name="OsSpinlockAccessingApplication">
                        <d:ref type="REFERENCE" value="ASPath:/Os/OsApplication_C0"/>
                    </d:lst>
                </d:ctr>
                <d:ctr name="Spinlock2">
                    <d:var name="OsSpinlockLockMethod" type="ENUMERATION" value="SCHEDULER"/>
                    <d:lst name="OsSpinlockAccessingApplication"/>
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
        assert spinlocks[0].getOsSpinlockLockMethod() == "STANDARD"
        assert spinlocks[0].getOsSpinlockSuccessor().getValue() == "/Os/Spinlock2"
        assert len(spinlocks[0].getOsSpinlockAccessingApplications()) == 1
        assert spinlocks[1].getName() == "Spinlock2"
        assert spinlocks[1].getOsSpinlockLockMethod() == "SCHEDULER"
        assert spinlocks[1].getOsSpinlockSuccessor() is None
        assert len(spinlocks[1].getOsSpinlockAccessingApplications()) == 0


class TestOsOS:

    def test_read_os_os(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="OsOS">
                <d:var name="OsScalabilityClass" type="ENUMERATION" value="SC1"/>
                <d:var name="OsNumberOfCores" type="INTEGER" value="2"/>
                <d:var name="OsStackMonitoring" type="BOOLEAN" value="true"/>
                <d:var name="OsUseGetServiceId" type="BOOLEAN" value="false"/>
                <d:var name="OsUseParameterAccess" type="BOOLEAN" value="true"/>
                <d:var name="OsUseResScheduler" type="BOOLEAN" value="true"/>
                <d:var name="OsStatus" type="ENUMERATION" value="STANDARD"/>
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
        assert os_os.getOsScalabilityClass() == "SC1"
        assert os_os.getOsNumberOfCores() == 2
        assert os_os.getOsStackMonitoring() is True
        assert os_os.getOsUseGetServiceId() is False
        assert os_os.getOsUseParameterAccess() is True
        assert os_os.getOsUseResScheduler() is True
        assert os_os.getOsStatus() == "STANDARD"


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


class TestOsPeripheralArea:

    def test_read_os_peripheral_areas(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="OsPeripheralArea" type="MAP">
                <d:ctr name="Peripheral1">
                    <d:var name="OsPeripheralAreaStartAddress" type="INTEGER" value="1073741824"/>
                    <d:var name="OsPeripheralAreaEndAddress" type="INTEGER" value="1073750015"/>
                    <d:var name="OsPeripheralAreaAccessPermission" type="ENUMERATION" value="READ_WRITE"/>
                </d:ctr>
                <d:ctr name="Peripheral2">
                    <d:var name="OsPeripheralAreaStartAddress" type="INTEGER" value="1073750016"/>
                    <d:var name="OsPeripheralAreaEndAddress" type="INTEGER" value="1073766399"/>
                    <d:var name="OsPeripheralAreaAccessPermission" type="ENUMERATION" value="READ_ONLY"/>
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

        parser.read_os_peripheral_areas(element, os)

        areas = os.getOsPeripheralAreaList()
        assert len(areas) == 2
        assert areas[0].getName() == "Peripheral1"
        assert areas[0].getOsPeripheralAreaStartAddress() == 1073741824
        assert areas[0].getOsPeripheralAreaEndAddress() == 1073750015
        assert areas[0].getOsPeripheralAreaAccessPermission() == "READ_WRITE"
        assert areas[1].getName() == "Peripheral2"
        assert areas[1].getOsPeripheralAreaStartAddress() == 1073750016
        assert areas[1].getOsPeripheralAreaEndAddress() == 1073766399
        assert areas[1].getOsPeripheralAreaAccessPermission() == "READ_ONLY"


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
