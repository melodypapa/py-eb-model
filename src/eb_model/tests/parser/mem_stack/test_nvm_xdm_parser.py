"""
NvM XDM Parser Tests - Tests for NvM parser functionality.
"""
import pytest
import xml.etree.ElementTree as ET

from ....parser.nvm_xdm_parser import NvMXdmParser
from ....models.mem_stack.nvm_xdm import NvM
from ....models.core.eb_doc import EBModel


class TestNvMXdmParser:

    def setup_method(self):
        self.parser = NvMXdmParser()
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
        nvm = model.getNvM()

        self.parser.read_common_published_information(element, nvm)

        pub_info = nvm.getCommonPublishedInformation()
        assert pub_info is not None
        assert pub_info.getArMajorVersion() == 4
        assert pub_info.getArMinorVersion() == 3
        assert pub_info.getArPatchVersion() == 0
        assert pub_info.getSwMajorVersion() == 1
        assert pub_info.getSwMinorVersion() == 0
        assert pub_info.getSwPatchVersion() == 0

    def test_read_nvm_defensive_programming(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="NvMDefensiveProgramming" type="IDENTIFIABLE">
                <d:var name="NvMNullPointerCheck" type="BOOLEAN" value="true"/>
                <d:var name="NvMParameterCheck" type="BOOLEAN" value="true"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        nvm = model.getNvM()

        self.parser.read_nvm_defensive_programming(element, nvm)

        defensive = nvm.getNvMDefensiveProgramming()
        assert defensive is not None
        assert defensive.getNvMNullPointerCheck() is True
        assert defensive.getNvMParameterCheck() is True

    def test_read_report_to_dem(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="ReportToDem" type="IDENTIFIABLE">
                <d:var name="NvMReportStorageFailed" type="BOOLEAN" value="true"/>
                <d:var name="NvMReportVerificationFailed" type="BOOLEAN" value="false"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        nvm = model.getNvM()

        self.parser.read_report_to_dem(element, nvm)

        report = nvm.getReportToDem()
        assert report is not None
        assert report.getNvMReportStorageFailed() is True
        assert report.getNvMReportVerificationFailed() is False

    def test_read_nvm_common(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="NvMCommon" type="IDENTIFIABLE">
                <d:var name="NvMApiConfigClass" type="STRING" value="NVM_CCP"/>
                <d:var name="NvMBswMMultiBlockJobStatusInformation" type="BOOLEAN" value="false"/>
                <d:var name="NvMCompiledConfigId" type="INTEGER" value="0"/>
                <d:var name="NvMCrcNumOfBytes" type="INTEGER" value="2"/>
                <d:var name="NvMDatasetSelectionBits" type="INTEGER" value="0"/>
                <d:var name="NvMDevErrorDetect" type="BOOLEAN" value="true"/>
                <d:var name="NvMDynamicConfiguration" type="BOOLEAN" value="false"/>
                <d:var name="NvMJobPrioritization" type="BOOLEAN" value="false"/>
                <d:var name="NvMMainFunctionPeriod" type="FLOAT" value="0.0"/>
                <d:var name="NvMMemAccUsage" type="BOOLEAN" value="true"/>
                <d:var name="NvMPollingMode" type="BOOLEAN" value="false"/>
                <d:var name="NvMRepeatMirrorOperations" type="INTEGER" value="0"/>
                <d:var name="NvMSetRamBlockStatusApi" type="BOOLEAN" value="false"/>
                <d:var name="NvMSizeStandardJobQueue" type="INTEGER" value="10"/>
                <d:var name="NvMVersionInfoApi" type="BOOLEAN" value="false"/>
                <d:var name="NvMBufferAlignmentValue" type="STRING" value=""/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        nvm = model.getNvM()

        self.parser.read_nvm_common(element, nvm)

        common = nvm.getNvMCommon()
        assert common is not None
        assert common.getNvMApiConfigClass() == "NVM_CCP"
        assert common.getNvMDevErrorDetect() is True
        assert common.getNvMMemAccUsage() is True

    def test_read_nvm_block_descriptors(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:lst name="NvMBlockDescriptor">
                <d:ctr name="NvMBlock1" type="IDENTIFIABLE">
                    <d:var name="NvMBlockCrcType" type="STRING" value="NVM_CRC32"/>
                    <d:var name="NvMBlockManagementType" type="STRING" value="NVM_BLOCK_NATIVE"/>
                    <d:var name="NvMBlockUseAutoValidation" type="BOOLEAN" value="false"/>
                    <d:var name="NvMBlockUseCompression" type="BOOLEAN" value="false"/>
                    <d:var name="NvMBlockUseCrc" type="BOOLEAN" value="true"/>
                    <d:var name="NvMBlockUseCRCCompMechanism" type="BOOLEAN" value="false"/>
                    <d:var name="NvMBlockUsePort" type="BOOLEAN" value="false"/>
                    <d:var name="NvMBlockUseSetRamBlockStatus" type="BOOLEAN" value="false"/>
                    <d:var name="NvMBlockUseSyncMechanism" type="BOOLEAN" value="false"/>
                    <d:var name="NvMBlockWriteProt" type="BOOLEAN" value="false"/>
                    <d:var name="NvMBswMBlockStatusInformation" type="BOOLEAN" value="false"/>
                    <d:var name="NvMCalcRamBlockCrc" type="BOOLEAN" value="false"/>
                    <d:var name="NvMMaxNumOfReadRetries" type="INTEGER" value="0"/>
                    <d:var name="NvMMaxNumOfWriteRetries" type="INTEGER" value="0"/>
                    <d:var name="NvMSelectBlockForFirstInitAll" type="BOOLEAN" value="false"/>
                    <d:var name="NvMSelectBlockForReadAll" type="BOOLEAN" value="false"/>
                    <d:var name="NvMSelectBlockForWriteAll" type="BOOLEAN" value="false"/>
                    <d:var name="NvMStaticBlockIDCheck" type="BOOLEAN" value="true"/>
                    <d:var name="NvMWriteBlockOnce" type="BOOLEAN" value="false"/>
                    <d:var name="NvMWriteVerification" type="BOOLEAN" value="false"/>
                    <d:var name="NvMWriteVerificationDataSize" type="INTEGER" value="0"/>
                    <d:var name="NvMNvBlockNum" type="INTEGER" value="1"/>
                    <d:var name="NvMNvBlockLength" type="INTEGER" value="1024"/>
                    <d:var name="NvMNvBlockBaseNumber" type="INTEGER" value="1"/>
                    <d:var name="NvMNvramBlockIdentifier" type="STRING" value="NVRAM_BLOCK_1"/>
                    <d:var name="NvMNvramDeviceId" type="INTEGER" value="0"/>
                    <d:var name="NvMRomBlockNum" type="INTEGER" value="0"/>
                    <d:var name="NvMBlockJobPriority" type="INTEGER" value="0"/>
                    <d:var name="NvMResistantToChangedSw" type="BOOLEAN" value="false"/>
                    <d:var name="NvMProvideRteJobFinishedPort" type="BOOLEAN" value="false"/>
                    <d:var name="NvMProvideRteServicePort" type="BOOLEAN" value="false"/>
                    <d:var name="NvMAdvancedRecovery" type="BOOLEAN" value="false"/>
                    <d:var name="ASR2011CallbackEnabled" type="BOOLEAN" value="true"/>
                    <d:var name="NvMExtraBlockChecks" type="BOOLEAN" value="false"/>
                    <d:var name="NvMProvideRteAdminPort" type="BOOLEAN" value="true"/>
                    <d:var name="NvMProvideRteInitBlockPort" type="BOOLEAN" value="false"/>
                </d:ctr>
            </d:lst>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        nvm = model.getNvM()

        self.parser.read_nvm_block_descriptors(element, nvm)

        blocks = nvm.getNvMBlockDescriptorList()
        assert len(blocks) == 1

        block = blocks[0]
        assert block.getName() == "NvMBlock1"
        assert block.getNvMNvBlockNum() == 1
        assert block.getNvMNvBlockLength() == 1024
        assert block.getNvMNvramBlockIdentifier() == "NVRAM_BLOCK_1"
        assert block.getNvMAdvancedRecovery() is False
        assert block.getASR2011CallbackEnabled() is True
        assert block.getNvMExtraBlockChecks() is False
        assert block.getNvMProvideRteAdminPort() is True
        assert block.getNvMProvideRteInitBlockPort() is False
