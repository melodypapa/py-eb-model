"""
NvM XDM Parser Module - Extracts AUTOSAR NvM configuration from EB Tresos XDM files.

Implements:
    - SWR_NVM_00001: NvM module parsing
    - SWR_NVM_00002: NvM common configuration parsing
    - SWR_NVM_00003: NvM block descriptor parsing
"""
import xml.etree.ElementTree as ET

from eb_model.models.mem_stack.nvm_xdm import NvM, NvMBlockDescriptor, NvMCommon
from eb_model.models.mem_stack.nvm_xdm import NvMEaRef, NvMFeeRef
from eb_model.models.mem_stack.nvm_xdm import NvMInitBlockCallback, NvMSingleBlockCallback
from eb_model.models.mem_stack.nvm_xdm import CommonPublishedInformation, PublishedInformation
from eb_model.models.mem_stack.nvm_xdm import NvMDefensiveProgramming
from eb_model.models.mem_stack.nvm_xdm import NvMCommonCryptoSecurityParameters, NvMServiceAPI
from eb_model.models.mem_stack.nvm_xdm import NvmDemEventParameterRefs, ReportToDem, MultiCoreCallout
from eb_model.models.core.eb_doc import EBModel
from eb_model.parser.core.eb_parser import AbstractEbModelParser


class NvMXdmParser(AbstractEbModelParser):
    """
    Parser for AUTOSAR NvM (Non-volatile Memory) module configuration.

    Extracts NvM configuration including common settings and block descriptors.

    Implements: SWR_NVM_00001 (NvM Module Parser)
    """

    def __init__(self, ) -> None:
        """Initialize the NvM XDM parser."""
        super().__init__()

        self.nvm = None

    def parse(self, element: ET.Element, doc: EBModel):
        """
        Parse NvM module configuration from XDM element.

        Implements: SWR_NVM_00001
        """
        if self.get_component_name(element) != "NvM":
            raise ValueError("Invalid <%s> xdm file" % "NvM")

        nvm = doc.getNvM()

        self.read_version(element, nvm)

        self.logger.info("Parse NvM ARVersion:<%s> SwVersion:<%s>" % (nvm.getArVersion().getVersion(), nvm.getSwVersion().getVersion()))

        self.nvm = nvm

        self.read_common_published_information(element, nvm)
        self.read_published_information(element, nvm)
        self.read_nvm_defensive_programming(element, nvm)
        self.read_nvm_common_crypto_security_parameters(element, nvm)
        self.read_nvm_service_api(element, nvm)
        self.read_nvm_dem_event_parameter_refs(element, nvm)
        self.read_report_to_dem(element, nvm)
        self.read_multi_core_callout(element, nvm)

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
            nvm_common.setNvMMemAccUsage(self.read_optional_value(ctr_tag, "NvMMemAccUsage"))
            nvm_common.setNvMPollingMode(self.read_value(ctr_tag, "NvMPollingMode"))
            nvm_common.setNvMRepeatMirrorOperations(self.read_value(ctr_tag, "NvMRepeatMirrorOperations"))
            nvm_common.setNvMSetRamBlockStatusApi(self.read_value(ctr_tag, "NvMSetRamBlockStatusApi"))
            nvm_common.setNvMSizeImmediateJobQueue(self.read_optional_value(ctr_tag, "NvMSizeImmediateJobQueue"))
            nvm_common.setNvMSizeStandardJobQueue(self.read_value(ctr_tag, "NvMSizeStandardJobQueue"))
            nvm_common.setNvMVersionInfoApi(self.read_value(ctr_tag, "NvMVersionInfoApi"))
            nvm_common.setNvMBufferAlignmentValue(self.read_value(ctr_tag, "NvMBufferAlignmentValue"))
            for ref in self.read_ref_value_list(ctr_tag, "NvMEcucPartitionRef"):
                nvm_common.addNvMEcucPartitionRef(ref)
            nvm_common.setNvMMasterEcucPartitionRef(self.read_optional_ref_value(ctr_tag, "NvMMasterEcucPartitionRef"))

            nvm.setNvMCommon(nvm_common)

    def read_common_published_information(self, element: ET.Element, nvm: NvM):
        """
        Parse CommonPublishedInformation container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "CommonPublishedInformation")
        if ctr_tag is not None:
            pub_info = CommonPublishedInformation(nvm, ctr_tag.attrib["name"])
            pub_info.setArMajorVersion(self.read_value(ctr_tag, "ArMajorVersion"))
            pub_info.setArMinorVersion(self.read_value(ctr_tag, "ArMinorVersion"))
            pub_info.setArPatchVersion(self.read_value(ctr_tag, "ArPatchVersion"))
            pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
            pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
            pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
            nvm.setCommonPublishedInformation(pub_info)
            self.logger.debug("Read CommonPublishedInformation")

    def read_published_information(self, element: ET.Element, nvm: NvM):
        """
        Parse PublishedInformation container from XDM.
        """
        ctr_tag = self.find_ctr_tag(element, "PublishedInformation")
        if ctr_tag is not None:
            pub_info = PublishedInformation(nvm, ctr_tag.attrib["name"])
            pub_info.setVendorId(self.read_value(ctr_tag, "VendorId"))
            pub_info.setArReleaseMajorVersion(self.read_value(ctr_tag, "ArReleaseMajorVersion"))
            pub_info.setArReleaseMinorVersion(self.read_value(ctr_tag, "ArReleaseMinorVersion"))
            pub_info.setArReleasePatchVersion(self.read_value(ctr_tag, "ArReleasePatchVersion"))
            pub_info.setSwMajorVersion(self.read_value(ctr_tag, "SwMajorVersion"))
            pub_info.setSwMinorVersion(self.read_value(ctr_tag, "SwMinorVersion"))
            pub_info.setSwPatchVersion(self.read_value(ctr_tag, "SwPatchVersion"))
            nvm.setPublishedInformation(pub_info)
            self.logger.debug("Read PublishedInformation")

    def read_nvm_defensive_programming(self, element: ET.Element, nvm: NvM):
        """Parse NvMDefensiveProgramming container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "NvMDefensiveProgramming")
        if ctr_tag is not None:
            defensive = NvMDefensiveProgramming(nvm, ctr_tag.attrib["name"])
            defensive.setNvMNullPointerCheck(self.read_optional_value(ctr_tag, "NvMNullPointerCheck"))
            defensive.setNvMParameterCheck(self.read_optional_value(ctr_tag, "NvMParameterCheck"))
            nvm.setNvMDefensiveProgramming(defensive)
            self.logger.debug("Read NvMDefensiveProgramming")

    def read_nvm_common_crypto_security_parameters(self, element: ET.Element, nvm: NvM):
        """Parse NvMCommonCryptoSecurityParameters container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "NvMCommonCryptoSecurityParameters")
        if ctr_tag is not None:
            crypto = NvMCommonCryptoSecurityParameters(nvm, ctr_tag.attrib["name"])
            crypto.setNvMCryptoPrimitive(self.read_optional_value(ctr_tag, "NvMCryptoPrimitive"))
            crypto.setNvMKeyAddress(self.read_optional_value(ctr_tag, "NvMKeyAddress"))
            nvm.setNvMCommonCryptoSecurityParameters(crypto)
            self.logger.debug("Read NvMCommonCryptoSecurityParameters")

    def read_nvm_service_api(self, element: ET.Element, nvm: NvM):
        """Parse NvMServiceAPI container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "NvMServiceAPI")
        if ctr_tag is not None:
            service_api = NvMServiceAPI(nvm, ctr_tag.attrib["name"])
            service_api.setNvMVersionInfoApi(self.read_optional_value(ctr_tag, "NvMVersionInfoApi"))
            nvm.setNvMServiceAPI(service_api)
            self.logger.debug("Read NvMServiceAPI")

    def read_nvm_dem_event_parameter_refs(self, element: ET.Element, nvm: NvM):
        """Parse NvmDemEventParameterRefs container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "NvmDemEventParameterRefs")
        if ctr_tag is not None:
            dem_params = NvmDemEventParameterRefs(nvm, ctr_tag.attrib["name"])
            nvm.setNvmDemEventParameterRefs(dem_params)
            self.logger.debug("Read NvmDemEventParameterRefs")

    def read_report_to_dem(self, element: ET.Element, nvm: NvM):
        """Parse ReportToDem container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "ReportToDem")
        if ctr_tag is not None:
            report = ReportToDem(nvm, ctr_tag.attrib["name"])
            report.setNvMReportStorageFailed(self.read_optional_value(ctr_tag, "NvMReportStorageFailed"))
            report.setNvMReportVerificationFailed(self.read_optional_value(ctr_tag, "NvMReportVerificationFailed"))
            nvm.setReportToDem(report)
            self.logger.debug("Read ReportToDem")

    def read_multi_core_callout(self, element: ET.Element, nvm: NvM):
        """Parse MultiCoreCallout container from XDM."""
        ctr_tag = self.find_ctr_tag(element, "MultiCoreCallout")
        if ctr_tag is not None:
            callout = MultiCoreCallout(nvm, ctr_tag.attrib["name"])
            nvm.setMultiCoreCallout(callout)
            self.logger.debug("Read MultiCoreCallout")

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
        block_ref = self.read_optional_choice_value(element, "NvMTargetBlockReference")
        if block_ref is None:
            return
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
            self.logger.warning("Unknown block reference type <%s> in NvMBlockDescriptor <%s>",
                               block_ref, nvm_block.getName())

    def read_nvm_block_descriptors(self, element: ET.Element, nvm: NvM):
        for ctr_tag in self.find_ctr_tag_list(element, "NvMBlockDescriptor"):
            nvm_block = NvMBlockDescriptor(nvm, ctr_tag.attrib["name"])
            nvm_block.setNvMBlockCrcType(self.read_value(ctr_tag, "NvMBlockCrcType"))
            nvm_block.setNvMBlockEcucPartitionRef(self.read_optional_ref_value(ctr_tag, "NvMBlockEcucPartitionRef"))
            nvm_block.setNvMNvramBlockIdentifier(self.read_value(ctr_tag, "NvMNvramBlockIdentifier"))
            nvm_block.setNvMRamBlockDataAddress(self.read_optional_value(ctr_tag, "NvMRamBlockDataAddress"))
            nvm_block.setNvMRomBlockDataAddress(self.read_optional_value(ctr_tag, "NvMRomBlockDataAddress"))
            nvm_block.setNvMBlockJobPriority(self.read_value(ctr_tag, "NvMBlockJobPriority"))
            nvm_block.setNvMResistantToChangedSw(self.read_value(ctr_tag, "NvMResistantToChangedSw"))
            nvm_block.setNvMBlockUseCrc(self.read_value(ctr_tag, "NvMBlockUseCrc"))
            nvm_block.setNvMRomBlockNum(self.read_value(ctr_tag, "NvMRomBlockNum"))
            nvm_block.setNvMBlockManagementType(self.read_value(ctr_tag, "NvMBlockManagementType"))
            nvm_block.setNvMNvBlockLength(self.read_value(ctr_tag, "NvMNvBlockLength"))
            nvm_block.setNvMNvBlockNum(self.read_value(ctr_tag, "NvMNvBlockNum"))
            nvm_block.setNvMSelectBlockForReadAll(self.read_value(ctr_tag, "NvMSelectBlockForReadAll"))
            nvm_block.setNvMSelectBlockForWriteAll(self.read_value(ctr_tag, "NvMSelectBlockForWriteAll"))

            nvm_block.setNvMProvideRteJobFinishedPort(self.read_value(ctr_tag, "NvMProvideRteJobFinishedPort"))
            nvm_block.setNvMProvideRteServicePort(self.read_value(ctr_tag, "NvMProvideRteServicePort"))
            nvm_block.setNvMAdvancedRecovery(self.read_optional_value(ctr_tag, "NvMAdvancedRecovery"))
            nvm_block.setASR2011CallbackEnabled(self.read_optional_value(ctr_tag, "ASR2011CallbackEnabled"))
            nvm_block.setNvMExtraBlockChecks(self.read_optional_value(ctr_tag, "NvMExtraBlockChecks"))
            nvm_block.setNvMProvideRteAdminPort(self.read_optional_value(ctr_tag, "NvMProvideRteAdminPort"))
            nvm_block.setNvMProvideRteInitBlockPort(self.read_optional_value(ctr_tag, "NvMProvideRteInitBlockPort"))

            nvm_block.setNvMReadRamBlockFromNvCallback(self.read_optional_value(ctr_tag, "NvMReadRamBlockFromNvCallback"))
            nvm_block.setNvMWriteRamBlockToNvCallback(self.read_optional_value(ctr_tag, "NvMWriteRamBlockToNvCallback"))
            nvm_block.setNvMBlockUseSyncMechanism(self.read_value(ctr_tag, "NvMBlockUseSyncMechanism"))

            self.read_nvm_init_block_callback(ctr_tag, nvm_block)
            self.read_nvm_single_block_callback(ctr_tag, nvm_block)

            nvm_block.setNvMNvBlockBaseNumber(self.read_value(ctr_tag, "NvMNvBlockBaseNumber"))
            self.read_nvm_block_target_block_reference(ctr_tag, nvm_block)

            nvm.addNvMBlockDescriptor(nvm_block)

