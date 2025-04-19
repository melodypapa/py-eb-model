from eb_model.parser.nvm_xdm_parser import NvMXdmParser
from eb_model.models.eb_doc import EBModel

import xml.etree.ElementTree as ET
import pytest


class TestNvmXdmParser:
    def test_read_nvm_block_descriptors(self):

        # Create a mock XML element for testing
        xml_content = """
            <datamodel version="8.0"
                xmlns="http://www.tresos.de/_projects/DataModel2/18/root.xsd"
                xmlns:a="http://www.tresos.de/_projects/DataModel2/18/attribute.xsd"
                xmlns:v="http://www.tresos.de/_projects/DataModel2/06/schema.xsd"
                xmlns:d="http://www.tresos.de/_projects/DataModel2/06/data.xsd">
                <d:lst name="NvMBlockDescriptor" type="MAP">
                    <d:ctr name="NvmBlock_TestData" type="IDENTIFIABLE">
                        <d:ref name="NvMBlockEcucPartitionRef" type="REFERENCE" value="ASPath:/EcuC/EcuC/EcucPartitionCollection/OsApplication_C0">
                        </d:ref>
                        <d:var name="NvMAdvancedRecovery" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBlockUsePort" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBlockUseCompression" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:ref name="NvMBlockCipheringRef" type="REFERENCE">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:ref>
                        <d:var name="NvMBlockHeaderInclude" type="STRING">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBlockCrcType" type="ENUMERATION" value="NVM_CRC16">
                            <a:a name="ENABLE" value="true"/>
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBlockJobPriority" type="INTEGER" value="64">
                        </d:var>
                        <d:var name="NvMBlockManagementType" type="ENUMERATION" value="NVM_BLOCK_NATIVE">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBlockUseCrc" type="BOOLEAN" value="true">
                        </d:var>
                        <d:var name="NvMBlockUseSyncMechanism" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="ASR2011CallbackEnabled" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBlockWriteProt" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBswMBlockStatusInformation" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMCalcRamBlockCrc" type="BOOLEAN" value="false">
                            <a:a name="ENABLE" value="false"/>
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBlockUseCRCCompMechanism" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBlockUseSetRamBlockStatus" type="BOOLEAN" value="true">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMExtraBlockChecks" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:ctr name="NvMInitBlockCallback" type="IDENTIFIABLE">
                            <a:a name="ENABLE" value="false"/>
                            <d:var name="NvMInitBlockCallbackFnc" type="FUNCTION-NAME" >
                            <a:a name="ENABLE" value="false"/>
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                            </d:var>
                        </d:ctr>
                        <d:var name="NvMMaxNumOfReadRetries" type="INTEGER" value="0">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMMaxNumOfWriteRetries" type="INTEGER" value="3">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMNvBlockBaseNumber" type="INTEGER" value="6">
                            <a:a name="IMPORTER_INFO">
                            <a:v>@DEF</a:v>
                            <a:v>@CALC</a:v>
                            </a:a>
                        </d:var>
                        <d:var name="NvMNvBlockLength" type="INTEGER" value="64">
                            </d:var>
                        <d:var name="NvMNvBlockNum" type="INTEGER" value="1">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMNvramBlockIdentifier" type="INTEGER" value="9">
                            <a:a name="IMPORTER_INFO">
                            <a:v>@DEF</a:v>
                            <a:v>@CALC</a:v>
                            </a:a>
                        </d:var>
                        <d:var name="NvMNvramDeviceId" type="INTEGER" value="0">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMProvideRteAdminPort" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMProvideRteInitBlockPort" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMProvideRteJobFinishedPort" type="BOOLEAN" value="true">
                        </d:var>
                        <d:var name="NvMProvideRteMirrorPort" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMProvideRteServicePort" type="BOOLEAN" value="true">
                            </d:var>
                        <d:var name="NvMRPortInterfacesASRVersion" type="ENUMERATION" value="DEFAULT">
                            </d:var>
                        <d:var name="NvMRamBlockDataAddress" type="STRING" value="&amp;Ram_TestData">
                            <a:a name="ENABLE" value="TRUE"/>
                        </d:var>
                        <d:var name="NvMReadRamBlockFromNvCallback" type="FUNCTION-NAME" value="">
                            <a:a name="ENABLE" value="FALSE"/>
                        </d:var>
                        <d:var name="NvMResistantToChangedSw" type="BOOLEAN" value="true">
                        </d:var>
                        <d:var name="NvMRomBlockDataAddress" type="STRING" value="&amp;Rom_TestData">
                            <a:a name="ENABLE" value="TRUE"/>
                        </d:var>
                        <d:var name="NvMRomBlockNum" type="INTEGER" value="1">
                        </d:var>
                        <d:var name="NvMSelectBlockForReadAll" type="BOOLEAN" value="true">
                            <a:a name="ENABLE" value="TRUE"/>
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMSelectBlockForWriteAll" type="BOOLEAN" value="true">
                            <a:a name="ENABLE" value="TRUE"/>
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMSelectBlockForFirstInitAll" type="BOOLEAN" value="false">
                            <a:a name="ENABLE" value="TRUE"/>
                        </d:var>
                        <d:ctr name="NvMSingleBlockCallback" type="IDENTIFIABLE">
                            <a:a name="ENABLE" value="false"/>
                            <d:var name="NvMSingleBlockCallbackFnc" type="FUNCTION-NAME" >
                            <a:a name="ENABLE" value="false"/>
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                            </d:var>
                        </d:ctr>
                        <d:var name="NvMStaticBlockIDCheck" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBlockUseAutoValidation" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:chc name="NvMTargetBlockReference" type="IDENTIFIABLE" value="NvMFeeRef">
                            <d:ctr name="NvMEaRef" type="IDENTIFIABLE">
                            <d:ref name="NvMNameOfEaBlock" type="REFERENCE" ><a:a name="IMPORTER_INFO" value="@DEF"/>
                            </d:ref>
                            </d:ctr>
                            <d:ctr name="NvMFeeRef" type="IDENTIFIABLE">
                            <d:ref name="NvMNameOfFeeBlock" type="REFERENCE" value="ASPath:/Fee/Fee/Fee_NvmBlock_TestData"/>
                            </d:ctr>
                        </d:chc>
                        <d:var name="NvMUserProvidesSpaceForBlockAndCrc" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMEnBlockCheck" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMEnableBlockCryptoSecurityHandling" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMCryptoExtraInfoSize" type="INTEGER" value="0">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBcEnSetAPI" type="BOOLEAN" value="true">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBcEnAutoStart" type="BOOLEAN" value="true">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBcEnCrcComp" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBcEnRamComp" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBcEnReddCopiesComp" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBcEnAutoRepair" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMBcDelayCounter" type="INTEGER" value="0">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMWriteBlockOnce" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMWriteRamBlockToNvCallback" type="FUNCTION-NAME" value="">
                            <a:a name="ENABLE" value="FALSE"/>
                            </d:var>
                        <d:var name="NvMWriteVerification" type="BOOLEAN" value="false">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMWriteVerificationDataSize" type="INTEGER" value="1">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMPreWriteDataComp" type="BOOLEAN" value="false">
                            <a:a name="ENABLE" value="false"/>
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                        <d:var name="NvMPreWriteDataCompDataSize" type="INTEGER" value="1">
                            <a:a name="IMPORTER_INFO" value="@DEF"/>
                        </d:var>
                    </d:ctr>
                </d:lst>
            </datamodel>
            """
        element = ET.fromstring(xml_content)

        model = EBModel.getInstance()
        nvm = model.getNvM()

        # Create parser instance
        parser = NvMXdmParser()
        parser.nsmap = {
            '': "http://www.tresos.de/_projects/DataModel2/18/root.xsd",
            'a': "http://www.tresos.de/_projects/DataModel2/18/attribute.xsd",
            'v': "http://www.tresos.de/_projects/DataModel2/06/schema.xsd",
            'd': "http://www.tresos.de/_projects/DataModel2/06/data.xsd"
        }

        # Call the method
        parser.read_nvm_block_descriptors(element, nvm)

        # Assertions
        blocks = nvm.getNvMBlockDescriptorList()
        assert len(blocks) == 1

        # Validate first block
        block1 = blocks[0]
        assert block1.getName() == "NvmBlock_TestData"
        assert block1.getNvMBlockCrcType() == "NVM_CRC16"
        assert block1.getNvMBlockEcucPartitionRef().getShortName() == "OsApplication_C0"
        assert block1.getNvMNvramBlockIdentifier() == 9
        assert block1.getNvMRamBlockDataAddress() == "&Ram_TestData"
        assert block1.getNvMRomBlockDataAddress() == "&Rom_TestData"
        assert block1.getNvMRomBlockNum() == 1
        assert block1.getNvMBlockManagementType() == "NVM_BLOCK_NATIVE"
        assert block1.getNvMNvBlockLength() == 64
        assert block1.getNvMNvBlockNum() == 1
        assert block1.getNvMSelectBlockForReadAll() is True
        assert block1.getNvMSelectBlockForWriteAll() is True

        