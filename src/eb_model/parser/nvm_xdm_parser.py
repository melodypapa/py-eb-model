import xml.etree.ElementTree as ET

from ..models.nvm_xdm import NvM, NvMBlockDescriptor, NvMCommon, NvMEaRef, NvMFeeRef, NvMInitBlockCallback, NvMSingleBlockCallback
from ..models.eb_doc import EBModel
from ..parser.eb_parser import AbstractEbModelParser


class NvMXdmParser(AbstractEbModelParser):
    def __init__(self, ) -> None:
        super().__init__()

        self.nvm = None

    def parse(self, element: ET.Element, doc: EBModel):
        if self.get_component_name(element) != "NvM":
            raise ValueError("Invalid <%s> xdm file" % "NvM")

        nvm = doc.getNvM()

        self.read_version(element, nvm)

        self.logger.info("Parse NvM ARVersion:<%s> SwVersion:<%s>" % (nvm.getArVersion().getVersion(), nvm.getSwVersion().getVersion()))

        self.nvm = nvm

        self.read_nvm_common(element, nvm)
        self.read_nvm_block_descriptors(element, nvm)

    def read_nvm_common(self, element: ET.Element, nvm: NvM):
        ctr_tag = self.find_ctr_tag(element, "NvMCommon")
        if ctr_tag is not None:
            nvm_common = NvMCommon(nvm, "NvMCommon")
            nvm_common.setNvMApiConfigClass(self.read_value(ctr_tag, "NvMApiConfigClass"))
            nvm_common.setNvMBswMMultiBlockJobStatusInformation(self.read_value(ctr_tag, "NvMBswMMultiBlockJobStatusInformation"))
            nvm_common.setNvMCompiledConfigId(self.read_value(ctr_tag, "NvMCompiledConfigId"))
            nvm_common.setNvMCrcNumOfBytes(self.read_value(ctr_tag, "NvMCrcNumOfBytes"))
            nvm_common.setNvMCsmRetryCounter(self.read_optional_value(ctr_tag, "NvMCsmRetryCounter"))
            nvm_common.setNvMDatasetSelectionBits(self.read_value(ctr_tag, "NvMDatasetSelectionBits"))
            nvm_common.setNvMDevErrorDetect(self.read_value(ctr_tag, "NvMDevErrorDetect"))
            nvm_common.setNvMDynamicConfiguration(self.read_value(ctr_tag, "NvMDynamicConfiguration"))
            nvm_common.setNvMJobPrioritization(self.read_value(ctr_tag, "NvMJobPrioritization"))
            nvm_common.setNvMMainFunctionPeriod(self.read_value(ctr_tag, "NvMMainFunctionPeriod"))
            nvm_common.setNvMMultiBlockCallback(self.read_optional_value(ctr_tag, "NvMMultiBlockCallback"))
            nvm_common.setNvMPollingMode(self.read_value(ctr_tag, "NvMPollingMode"))
            nvm_common.setNvMRepeatMirrorOperations(self.read_value(ctr_tag, "NvMRepeatMirrorOperations"))
            nvm_common.setNvMSetRamBlockStatusApi(self.read_value(ctr_tag, "NvMSetRamBlockStatusApi"))
            nvm_common.setNvMSizeImmediateJobQueue(self.read_optional_value(ctr_tag, "NvMSizeImmediateJobQueue"))
            nvm_common.setNvMSizeStandardJobQueue(self.read_value(ctr_tag, "NvMSizeStandardJobQueue"))
            nvm_common.setNvMVersionInfoApi(self.read_value(ctr_tag, "NvMVersionInfoApi"))
            nvm_common.setNvMBufferAlignmentValue(self.read_value(ctr_tag, "NvMBufferAlignmentValue"))
            for ref in self.read_ref_value_list(ctr_tag, "NvMEcucPartitionRef"):
                nvm_common.addNvMEcucPartitionRef(ref)
            nvm_common.setNvMMasterEcucPartitionRef(self.read_ref_value(ctr_tag, "NvMMasterEcucPartitionRef"))

            nvm.setNvMCommon(nvm_common)

    def read_nvm_init_block_callback(self, element: ET.Element, nvm_block: NvMBlockDescriptor):
        ctr_tag = self.find_ctr_tag(element, "NvMInitBlockCallback")
        if ctr_tag is not None:
            init_block_callback = NvMInitBlockCallback(nvm_block, "NvMInitBlockCallback")
            init_block_callback.setNvMInitBlockCallbackFnc(self.read_value(ctr_tag, "NvMInitBlockCallbackFnc"))
            nvm_block.setNvMInitBlockCallback(init_block_callback)

    def read_nvm_single_block_callback(self, element: ET.Element, nvm_block: NvMBlockDescriptor):
        ctr_tag = self.find_ctr_tag(element, "NvMSingleBlockCallback")
        if ctr_tag is not None:
            single_block_callback = NvMSingleBlockCallback(nvm_block, "NvMSingleBlockCallback")
            single_block_callback.setNvMSingleBlockCallbackFnc(self.read_value(ctr_tag, "NvMSingleBlockCallbackFnc"))
            nvm_block.setNvMSingleBlockCallback(single_block_callback)

    def read_nvm_block_target_block_reference(self, element: ET.Element, nvm_block: NvMBlockDescriptor):
        block_ref = self.read_choice_value(element, "NvMTargetBlockReference")
        if block_ref == "NvMEaRef":
            ctr_tag = self.find_ctr_tag(element, "NvMEaRef")
            if ctr_tag is not None:
                ref = NvMEaRef(nvm_block, block_ref)
                ref.setNvMNameOfEaBlock(self.read_ref_value(element, "NvMNameOfEaBlock"))
                nvm_block.setNvMTargetBlockReference(ref)
        elif block_ref == "NvMFeeRef":
            ctr_tag = self.find_ctr_tag(element, "NvMFeeRef")
            if ctr_tag is not None:
                ref = NvMFeeRef(nvm_block, block_ref)
                ref.setNvMNameOfFeeBlock(self.read_ref_value(element, "NvMNameOfFeeBlock"))
                nvm_block.setNvMTargetBlockReference(ref)
        else:
            raise ValueError("Invalid block reference type <%s>" % block_ref)

    def read_nvm_block_descriptors(self, element: ET.Element, nvm: NvM):
        for ctr_tag in self.find_ctr_tag_list(element, "NvMBlockDescriptor"):
            nvm_block = NvMBlockDescriptor(nvm, ctr_tag.attrib["name"])
            nvm_block.setNvMBlockCrcType(self.read_optional_value(ctr_tag, "NvMBlockCrcType"))
            nvm_block.setNvMBlockEcucPartitionRef(self.read_ref_value(ctr_tag, "NvMBlockEcucPartitionRef"))
            nvm_block.setNvMNvramBlockIdentifier(self.read_value(ctr_tag, "NvMNvramBlockIdentifier"))
            nvm_block.setNvMRamBlockDataAddress(self.read_optional_value(ctr_tag, "NvMRamBlockDataAddress"))
            nvm_block.setNvMRomBlockDataAddress(self.read_optional_value(ctr_tag, "NvMRomBlockDataAddress"))
            nvm_block.setNvMBlockJobPriority(self.read_value(ctr_tag, "NvMBlockJobPriority"))
            nvm_block.setNvMResistantToChangedSw(self.read_value(ctr_tag, "NvMResistantToChangedSw"))
            nvm_block.setNvMBlockCrcType(self.read_value(ctr_tag, "NvMBlockCrcType"))
            nvm_block.setNvMBlockUseCrc(self.read_value(ctr_tag, "NvMBlockUseCrc"))
            nvm_block.setNvMRomBlockNum(self.read_value(ctr_tag, "NvMRomBlockNum"))
            nvm_block.setNvMBlockManagementType(self.read_value(ctr_tag, "NvMBlockManagementType"))
            nvm_block.setNvMNvBlockLength(self.read_value(ctr_tag, "NvMNvBlockLength"))
            nvm_block.setNvMNvBlockNum(self.read_value(ctr_tag, "NvMNvBlockNum"))
            nvm_block.setNvMSelectBlockForReadAll(self.read_value(ctr_tag, "NvMSelectBlockForReadAll"))
            nvm_block.setNvMSelectBlockForWriteAll(self.read_value(ctr_tag, "NvMSelectBlockForWriteAll"))

            nvm_block.setNvMProvideRteJobFinishedPort(self.read_value(ctr_tag, "NvMProvideRteJobFinishedPort"))
            nvm_block.setNvMProvideRteServicePort(self.read_value(ctr_tag, "NvMProvideRteServicePort"))

            nvm_block.setNvMReadRamBlockFromNvCallback(self.read_optional_value(ctr_tag, "NvMReadRamBlockFromNvCallback"))
            nvm_block.setNvMWriteRamBlockToNvCallback(self.read_optional_value(ctr_tag, "NvMWriteRamBlockToNvCallback"))
            nvm_block.setNvMBlockUseSyncMechanism(self.read_value(ctr_tag, "NvMBlockUseSyncMechanism"))

            self.read_nvm_init_block_callback(ctr_tag, nvm_block)
            self.read_nvm_single_block_callback(ctr_tag, nvm_block)
            
            nvm_block.setNvMNvBlockBaseNumber(self.read_value(ctr_tag, "NvMNvBlockBaseNumber"))
            self.read_nvm_block_target_block_reference(ctr_tag, nvm_block)

            nvm.addNvMBlockDescriptor(nvm_block)
                     
