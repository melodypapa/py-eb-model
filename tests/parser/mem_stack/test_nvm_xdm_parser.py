"""
NvM XDM Parser Tests - Tests for NvM parser functionality.
"""
import pytest
import xml.etree.ElementTree as ET

from eb_model.parser.mem_stack.nvm_xdm_parser import NvMXdmParser
from eb_model.models.mem_stack.nvm_xdm import NvM
from eb_model.models.core.eb_doc import EBModel


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
                <d:var name="NvMDefProgEnabled" type="BOOLEAN" value="true"/>
                <d:var name="NvMPrecondAssertEnabled" type="BOOLEAN" value="false"/>
                <d:var name="NvMPostcondAssertEnabled" type="BOOLEAN" value="false"/>
                <d:var name="NvMStaticAssertEnabled" type="BOOLEAN" value="true"/>
                <d:var name="NvMUnreachAssertEnabled" type="BOOLEAN" value="false"/>
                <d:var name="NvMInvariantAssertEnabled" type="BOOLEAN" value="false"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        nvm = model.getNvM()

        self.parser.read_nvm_defensive_programming(element, nvm)

        defensive = nvm.getNvMDefensiveProgramming()
        assert defensive is not None
        assert defensive.getNvMDefProgEnabled() is True
        assert defensive.getNvMPrecondAssertEnabled() is False
        assert defensive.getNvMStaticAssertEnabled() is True
        assert defensive.getNvMInvariantAssertEnabled() is False

    def test_read_report_to_dem(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="ReportToDem" type="IDENTIFIABLE">
                <d:var name="NvMIntegrityFailedReportToDem" type="ENUMERATION" value="DISABLE"/>
                <d:var name="NvMIntegrityFailedReportToDemDetErrorId" type="INTEGER" value="25"/>
                <d:var name="NvMRequestFailedReportToDem" type="ENUMERATION" value="ENABLE"/>
                <d:var name="NvMRequestFailedReportToDemDetErrorId" type="INTEGER" value="26"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        nvm = model.getNvM()

        self.parser.read_report_to_dem(element, nvm)

        report = nvm.getReportToDem()
        assert report is not None
        assert report.getNvMIntegrityFailedReportToDem() == "DISABLE"
        assert report.getNvMIntegrityFailedReportToDemDetErrorId() == 25
        assert report.getNvMRequestFailedReportToDem() == "ENABLE"
        assert report.getNvMRequestFailedReportToDemDetErrorId() == 26

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
                <d:var name="NvMSoftwareChangeCallout" type="FUNCTION-NAME" value=""/>
                <d:var name="NvMDrvModeSwitch" type="BOOLEAN" value="false"/>
                <d:var name="NvMCancelInternalOperations" type="BOOLEAN" value="false"/>
                <d:var name="NvMReadBlockHook" type="BOOLEAN" value="false"/>
                <d:var name="NvMRteUsage" type="BOOLEAN" value="true"/>
                <d:var name="NvMWriteBlockHook" type="BOOLEAN" value="false"/>
                <d:var name="NvMRedundantRecovery" type="ENUMERATION" value="NVM_RECOVERY_ON_REQUEST"/>
                <d:var name="NvMExportBlockLengths" type="BOOLEAN" value="false"/>
                <d:var name="NvMResultErasedBlocks" type="ENUMERATION" value="MEMIF_BLOCK_INCONSISTENT"/>
                <d:var name="NvMEnableLegacySymbolicNames" type="BOOLEAN" value="true"/>
                <d:var name="NvMResetRamBlockAfterReset" type="BOOLEAN" value="false"/>
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
        assert common.getNvMCompiledConfigId() == 0
        assert common.getNvMDrvModeSwitch() is False
        assert common.getNvMCancelInternalOperations() is False
        assert common.getNvMReadBlockHook() is False
        assert common.getNvMRteUsage() is True
        assert common.getNvMWriteBlockHook() is False
        assert common.getNvMRedundantRecovery() == "NVM_RECOVERY_ON_REQUEST"
        assert common.getNvMExportBlockLengths() is False
        assert common.getNvMResultErasedBlocks() == "MEMIF_BLOCK_INCONSISTENT"
        assert common.getNvMEnableLegacySymbolicNames() is True
        assert common.getNvMResetRamBlockAfterReset() is False

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

    def test_read_nvm_common_crypto_security_parameters(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="NvMCommonCryptoSecurityParameters" type="IDENTIFIABLE">
                <d:var name="NvMEnableCryptoSecurityHooks" type="BOOLEAN" value="true"/>
                <d:var name="NvMCryptoReadHook" type="FUNCTION-NAME" value="NvM_CryptoRead"/>
                <d:var name="NvMCryptoWriteHook" type="FUNCTION-NAME" value="NvM_CryptoWrite"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        nvm = model.getNvM()
        self.parser.read_nvm_common_crypto_security_parameters(element, nvm)
        crypto = nvm.getNvMCommonCryptoSecurityParameters()
        assert crypto is not None
        assert crypto.getNvMEnableCryptoSecurityHooks() is True
        assert crypto.getNvMCryptoReadHook() == "NvM_CryptoRead"
        assert crypto.getNvMCryptoWriteHook() == "NvM_CryptoWrite"

    def test_read_nvm_service_api(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="NvMServiceAPI" type="IDENTIFIABLE">
                <d:var name="NvMEnableASR32ServiceAPI" type="BOOLEAN" value="false"/>
                <d:var name="NvMEnableASR40ServiceAPI" type="BOOLEAN" value="false"/>
                <d:var name="NvMEnableASR42ServiceAPI" type="BOOLEAN" value="true"/>
                <d:var name="NvMDefaultASRServiceAPI" type="ENUMERATION" value="AUTOSAR_42"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        nvm = model.getNvM()
        self.parser.read_nvm_service_api(element, nvm)
        api = nvm.getNvMServiceAPI()
        assert api is not None
        assert api.getNvMEnableASR32ServiceAPI() is False
        assert api.getNvMEnableASR42ServiceAPI() is True
        assert api.getNvMDefaultASRServiceAPI() == "AUTOSAR_42"

    def test_read_nvm_dem_event_parameter_refs(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="NvmDemEventParameterRefs" type="IDENTIFIABLE">
                <d:ref name="NVM_E_INTEGRITY_FAILED" type="REFERENCE" value="ASPath:/Dem/Dem/DemEvent"/>
                <d:ref name="NVM_E_REQ_FAILED" type="REFERENCE" value="ASPath:/Dem/Dem/DemEvent2"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        nvm = model.getNvM()
        self.parser.read_nvm_dem_event_parameter_refs(element, nvm)
        dem_params = nvm.getNvmDemEventParameterRefs()
        assert dem_params is not None
        assert len(dem_params.getDemEventRefList()) == 2

    def test_read_multi_core_callout(self):
        xml_content = """
        <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
            <d:ctr name="MultiCoreCallout" type="IDENTIFIABLE">
                <d:var name="NvMReadBlockCallout" type="FUNCTION-NAME" value="NvM_ReadBlock_Callout"/>
                <d:var name="NvMWriteBlockCallout" type="FUNCTION-NAME" value="NvM_WriteBlock_Callout"/>
            </d:ctr>
        </datamodel>
        """
        element = ET.fromstring(xml_content)
        model = EBModel.getInstance()
        nvm = model.getNvM()
        self.parser.read_multi_core_callout(element, nvm)
        callout = nvm.getMultiCoreCallout()
        assert callout is not None
        assert callout.getNvMReadBlockCallout() == "NvM_ReadBlock_Callout"
        assert callout.getNvMWriteBlockCallout() == "NvM_WriteBlock_Callout"
