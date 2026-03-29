"""
EcuC XDM Parser Tests - Tests for EcuC parser functionality.
"""
import pytest
import xml.etree.ElementTree as ET

from ...parser.ecuc_xdm_parser import EcucXdmParser
from ...models.ecuc_xdm import EcuC
from ...models.eb_doc import EBModel


class TestEcucXdmParser:

    def setup_method(self):
        self.parser = EcucXdmParser()
        self.parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

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
        ecuc = model.getEcuC()

        self.parser.read_common_published_information(element, ecuc)

        pub_info = ecuc.getCommonPublishedInformation()
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
        ecuc = model.getEcuC()

        self.parser.read_published_information(element, ecuc)

        pub_info = ecuc.getPublishedInformation()
        assert pub_info is not None
        assert pub_info.getVendorId() == "Vector"
        assert pub_info.getArReleaseMajorVersion() == "4"
        assert pub_info.getArReleaseMinorVersion() == "3"
        assert pub_info.getArReleasePatchVersion() == "0"

    def test_read_ecuc_general(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="EcucGeneral" type="IDENTIFIABLE">
                <d:var name="DevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="LoadTolerant" type="BOOLEAN" value="false"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        ecuc = model.getEcuC()

        self.parser.read_ecuc_general(element, ecuc)

        general = ecuc.getEcucGeneral()
        assert general is not None
        assert general.getDevErrorDetect() is True
        assert general.getLoadTolerant() is False

    def test_read_ecuc_hardware(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="EcucHardware" type="IDENTIFIABLE"/>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        ecuc = model.getEcuC()

        self.parser.read_ecuc_hardware(element, ecuc)

        hardware = ecuc.getEcucHardware()
        assert hardware is not None
        assert hardware.getName() == "EcucHardware"

    def test_read_ecuc_partition_collection(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="EcucPartitionCollection" type="IDENTIFIABLE">
                <d:lst name="EcucPartition">
                    <d:ctr name="EcucPartition1" type="IDENTIFIABLE">
                        <d:var name="EcucDefaultBswPartition" type="BOOLEAN" value="true"/>
                        <d:var name="PartitionCanBeRestarted" type="BOOLEAN" value="false"/>
                        <d:var name="EcucPartitionBswModuleExecution" type="BOOLEAN" value="true"/>
                        <d:var name="EcucPartitionQmBswModuleExecution" type="BOOLEAN" value="false"/>
                    </d:ctr>
                    <d:ctr name="EcucPartition2" type="IDENTIFIABLE">
                        <d:var name="EcucDefaultBswPartition" type="BOOLEAN" value="false"/>
                        <d:var name="PartitionCanBeRestarted" type="BOOLEAN" value="true"/>
                        <d:var name="EcucPartitionBswModuleExecution" type="BOOLEAN" value="false"/>
                        <d:var name="EcucPartitionQmBswModuleExecution" type="BOOLEAN" value="true"/>
                    </d:ctr>
                </d:lst>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        ecuc = model.getEcuC()

        self.parser.read_ecuc_partition_collection(element, ecuc)

        collection = ecuc.getEcucPartitionCollection()
        assert collection is not None
        partitions = collection.getEcucPartitions()
        assert len(partitions) == 2

        partition1 = partitions[0]
        assert partition1.getName() == "EcucPartition1"
        assert partition1.getEcucDefaultBswPartition() is True
        assert partition1.getEcucPartitionBswModuleExecution() is True
        assert partition1.getEcucPartitionQmBswModuleExecution() is False

        partition2 = partitions[1]
        assert partition2.getName() == "EcucPartition2"
        assert partition2.getEcucDefaultBswPartition() is False
        assert partition2.getEcucPartitionBswModuleExecution() is False
        assert partition2.getEcucPartitionQmBswModuleExecution() is True
