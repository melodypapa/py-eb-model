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
            nvm_common.setNvMSoftwareChangeCallout(self.read_optional_value(ctr_tag, "NvMSoftwareChangeCallout"))
            nvm_common.setNvMDrvModeSwitch(self.read_optional_value(ctr_tag, "NvMDrvModeSwitch"))
            nvm_common.setNvMCancelInternalOperations(self.read_optional_value(ctr_tag, "NvMCancelInternalOperations"))
            nvm_common.setNvMReadBlockHook(self.read_optional_value(ctr_tag, "NvMReadBlockHook"))
            nvm_common.setNvMRteUsage(self.read_optional_value(ctr_tag, "NvMRteUsage"))
            header_lst = self.find_lst_tag(ctr_tag, "NvMUserHeader")
            if header_lst is not None:
                for var in header_lst.findall("d:var", self.nsmap):
                    value = var.get("value")
                    if value:
                        nvm_common.addNvMUserHeader(value)
            nvm_common.setNvMWriteBlockHook(self.read_optional_value(ctr_tag, "NvMWriteBlockHook"))
            nvm_common.setNvMRedundantRecovery(self.read_optional_value(ctr_tag, "NvMRedundantRecovery"))
            nvm_common.setNvMExportBlockLengths(self.read_optional_value(ctr_tag, "NvMExportBlockLengths"))
            nvm_common.setNvMResultErasedBlocks(self.read_optional_value(ctr_tag, "NvMResultErasedBlocks"))
            nvm_common.setNvMEnableLegacySymbolicNames(self.read_optional_value(ctr_tag, "NvMEnableLegacySymbolicNames"))
            nvm_common.setNvMResetRamBlockAfterReset(self.read_optional_value(ctr_tag, "NvMResetRamBlockAfterReset"))

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
        """Parse NvMDefensiveProgramming container from XDM.

        Implements: SWR_NVM_00005
        """
        ctr_tag = self.find_ctr_tag(element, "NvMDefensiveProgramming")
        if ctr_tag is not None:
            defensive = NvMDefensiveProgramming(nvm, ctr_tag.attrib["name"])
            defensive.setNvMDefProgEnabled(self.read_optional_value(ctr_tag, "NvMDefProgEnabled"))
            defensive.setNvMPrecondAssertEnabled(self.read_optional_value(ctr_tag, "NvMPrecondAssertEnabled"))
            defensive.setNvMPostcondAssertEnabled(self.read_optional_value(ctr_tag, "NvMPostcondAssertEnabled"))
            defensive.setNvMStaticAssertEnabled(self.read_optional_value(ctr_tag, "NvMStaticAssertEnabled"))
            defensive.setNvMUnreachAssertEnabled(self.read_optional_value(ctr_tag, "NvMUnreachAssertEnabled"))
            defensive.setNvMInvariantAssertEnabled(self.read_optional_value(ctr_tag, "NvMInvariantAssertEnabled"))
            nvm.setNvMDefensiveProgramming(defensive)
            self.logger.debug("Read NvMDefensiveProgramming")

    def read_nvm_common_crypto_security_parameters(self, element: ET.Element, nvm: NvM):
        """Parse NvMCommonCryptoSecurityParameters container from XDM.

        Implements: SWR_NVM_00006
        """
        ctr_tag = self.find_ctr_tag(element, "NvMCommonCryptoSecurityParameters")
        if ctr_tag is not None:
            crypto = NvMCommonCryptoSecurityParameters(nvm, ctr_tag.attrib["name"])
            crypto.setNvMEnableCryptoSecurityHooks(self.read_optional_value(ctr_tag, "NvMEnableCryptoSecurityHooks"))
            crypto.setNvMCryptoReadHook(self.read_optional_value(ctr_tag, "NvMCryptoReadHook"))
            crypto.setNvMCryptoWriteHook(self.read_optional_value(ctr_tag, "NvMCryptoWriteHook"))
            nvm.setNvMCommonCryptoSecurityParameters(crypto)
            self.logger.debug("Read NvMCommonCryptoSecurityParameters")

    def read_nvm_service_api(self, element: ET.Element, nvm: NvM):
        """Parse NvMServiceAPI container from XDM.

        Implements: SWR_NVM_00007
        """
        ctr_tag = self.find_ctr_tag(element, "NvMServiceAPI")
        if ctr_tag is not None:
            service_api = NvMServiceAPI(nvm, ctr_tag.attrib["name"])
            service_api.setNvMEnableASR32ServiceAPI(self.read_optional_value(ctr_tag, "NvMEnableASR32ServiceAPI"))
            service_api.setNvMEnableASR40ServiceAPI(self.read_optional_value(ctr_tag, "NvMEnableASR40ServiceAPI"))
            service_api.setNvMEnableASR42ServiceAPI(self.read_optional_value(ctr_tag, "NvMEnableASR42ServiceAPI"))
            service_api.setNvMDefaultASRServiceAPI(self.read_optional_value(ctr_tag, "NvMDefaultASRServiceAPI"))
            nvm.setNvMServiceAPI(service_api)
            self.logger.debug("Read NvMServiceAPI")

    def read_nvm_dem_event_parameter_refs(self, element: ET.Element, nvm: NvM):
        """Parse NvmDemEventParameterRefs container from XDM.

        Implements: SWR_NVM_00008
        """
        ctr_tag = self.find_ctr_tag(element, "NvmDemEventParameterRefs")
        if ctr_tag is not None:
            dem_params = NvmDemEventParameterRefs(nvm, ctr_tag.attrib["name"])
            ref = self.read_optional_ref_value(ctr_tag, "NVM_E_INTEGRITY_FAILED")
            if ref:
                dem_params.addDemEventRef(ref)
            ref = self.read_optional_ref_value(ctr_tag, "NVM_E_LOSS_OF_REDUNDANCY")
            if ref:
                dem_params.addDemEventRef(ref)
            ref = self.read_optional_ref_value(ctr_tag, "NVM_E_QUEUE_OVERFLOW")
            if ref:
                dem_params.addDemEventRef(ref)
            ref = self.read_optional_ref_value(ctr_tag, "NVM_E_REQ_FAILED")
            if ref:
                dem_params.addDemEventRef(ref)
            ref = self.read_optional_ref_value(ctr_tag, "NVM_E_VERIFY_FAILED")
            if ref:
                dem_params.addDemEventRef(ref)
            ref = self.read_optional_ref_value(ctr_tag, "NVM_E_WRITE_PROTECTED")
            if ref:
                dem_params.addDemEventRef(ref)
            ref = self.read_optional_ref_value(ctr_tag, "NVM_E_WRONG_BLOCK_ID")
            if ref:
                dem_params.addDemEventRef(ref)
            ref = self.read_optional_ref_value(ctr_tag, "NVM_E_BLOCK_CHECK")
            if ref:
                dem_params.addDemEventRef(ref)
            ref = self.read_optional_ref_value(ctr_tag, "NVM_E_HARDWARE")
            if ref:
                dem_params.addDemEventRef(ref)
            nvm.setNvmDemEventParameterRefs(dem_params)
            self.logger.debug("Read NvmDemEventParameterRefs")

    def read_report_to_dem(self, element: ET.Element, nvm: NvM):
        """Parse ReportToDem container from XDM.

        Implements: SWR_NVM_00009
        """
        ctr_tag = self.find_ctr_tag(element, "ReportToDem")
        if ctr_tag is not None:
            report = ReportToDem(nvm, ctr_tag.attrib["name"])
            report.setNvMUserCalloutFunctionProductionErrors(
                self.read_optional_value(ctr_tag, "NvMUserCalloutFunctionProductionErrors"))
            report.setNvMUserCalloutFunctionPassedProductionErrors(
                self.read_optional_value(ctr_tag, "NvMUserCalloutFunctionPassedProductionErrors"))
            report.setNvMIntegrityFailedReportToDem(
                self.read_optional_value(ctr_tag, "NvMIntegrityFailedReportToDem"))
            report.setNvMIntegrityFailedReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMIntegrityFailedReportToDemDetErrorId"))
            report.setNvMRequestFailedReportToDem(
                self.read_optional_value(ctr_tag, "NvMRequestFailedReportToDem"))
            report.setNvMRequestFailedReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMRequestFailedReportToDemDetErrorId"))
            report.setNvMWrongBlockIdReportToDem(
                self.read_optional_value(ctr_tag, "NvMWrongBlockIdReportToDem"))
            report.setNvMWrongBlockIdReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMWrongBlockIdReportToDemDetErrorId"))
            report.setNvMLossOfRedundancyReportToDem(
                self.read_optional_value(ctr_tag, "NvMLossOfRedundancyReportToDem"))
            report.setNvMLossOfRedundancyReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMLossOfRedundancyReportToDemDetErrorId"))
            report.setNvMQueueOverflowReportToDem(
                self.read_optional_value(ctr_tag, "NvMQueueOverflowReportToDem"))
            report.setNvMQueueOverflowReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMQueueOverflowReportToDemDetErrorId"))
            report.setNvMVerifyFailedReportToDem(
                self.read_optional_value(ctr_tag, "NvMVerifyFailedReportToDem"))
            report.setNvMVerifyFailedReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMVerifyFailedReportToDemDetErrorId"))
            report.setNvMWriteProtectedReportToDem(
                self.read_optional_value(ctr_tag, "NvMWriteProtectedReportToDem"))
            report.setNvMWriteProtectedReportToDemDetErrorId(
                self.read_optional_value(ctr_tag, "NvMWriteProtectedReportToDemDetErrorId"))
            report.setNvMBlockCheckReportProdError(
                self.read_optional_value(ctr_tag, "NvMBlockCheckReportProdError"))
            report.setNvMBlockCheckReportProdErrorId(
                self.read_optional_value(ctr_tag, "NvMBlockCheckReportProdErrorId"))
            nvm.setReportToDem(report)
            self.logger.debug("Read ReportToDem")

    def read_multi_core_callout(self, element: ET.Element, nvm: NvM):
        """Parse MultiCoreCallout container from XDM.

        Implements: SWR_NVM_00010
        """
        ctr_tag = self.find_ctr_tag(element, "MultiCoreCallout")
        if ctr_tag is not None:
            callout = MultiCoreCallout(nvm, ctr_tag.attrib["name"])
            callout.setNvMReadBlockCallout(self.read_optional_value(ctr_tag, "NvMReadBlockCallout"))
            callout.setNvMWriteBlockCallout(self.read_optional_value(ctr_tag, "NvMWriteBlockCallout"))
            callout.setNvMRestoreBlockDefaultsCallout(self.read_optional_value(ctr_tag, "NvMRestoreBlockDefaultsCallout"))
            callout.setNvMReadPRAMBlockCallout(self.read_optional_value(ctr_tag, "NvMReadPRAMBlockCallout"))
            callout.setNvMWritePRAMBlockCallout(self.read_optional_value(ctr_tag, "NvMWritePRAMBlockCallout"))
            callout.setNvMRestorePRAMBlockDefaultsCallout(self.read_optional_value(ctr_tag, "NvMRestorePRAMBlockDefaultsCallout"))
            callout.setNvMEraseNvBlockCallout(self.read_optional_value(ctr_tag, "NvMEraseNvBlockCallout"))
            callout.setNvMInvalidateNvBlockCallout(self.read_optional_value(ctr_tag, "NvMInvalidateNvBlockCallout"))
            callout.setNvMCancelJobsCallout(self.read_optional_value(ctr_tag, "NvMCancelJobsCallout"))
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

            nvm_block.setNvMEnBlockCheck(self.read_optional_value(ctr_tag, "NvMEnBlockCheck"))
            nvm_block.setNvMEnableBlockCryptoSecurityHandling(self.read_optional_value(ctr_tag, "NvMEnableBlockCryptoSecurityHandling"))
            nvm_block.setNvMCryptoExtraInfoSize(self.read_optional_value(ctr_tag, "NvMCryptoExtraInfoSize"))
            nvm_block.setNvMBcEnSetAPI(self.read_optional_value(ctr_tag, "NvMBcEnSetAPI"))
            nvm_block.setNvMBcEnAutoStart(self.read_optional_value(ctr_tag, "NvMBcEnAutoStart"))
            nvm_block.setNvMBcEnCrcComp(self.read_optional_value(ctr_tag, "NvMBcEnCrcComp"))
            nvm_block.setNvMBcEnRamComp(self.read_optional_value(ctr_tag, "NvMBcEnRamComp"))
            nvm_block.setNvMBcEnReddCopiesComp(self.read_optional_value(ctr_tag, "NvMBcEnReddCopiesComp"))
            nvm_block.setNvMBcEnAutoRepair(self.read_optional_value(ctr_tag, "NvMBcEnAutoRepair"))
            nvm_block.setNvMBcDelayCounter(self.read_optional_value(ctr_tag, "NvMBcDelayCounter"))
            nvm_block.setNvMWriteBlockOnce(self.read_optional_value(ctr_tag, "NvMWriteBlockOnce"))
            nvm_block.setNvMWriteVerification(self.read_optional_value(ctr_tag, "NvMWriteVerification"))
            nvm_block.setNvMWriteVerificationDataSize(self.read_optional_value(ctr_tag, "NvMWriteVerificationDataSize"))
            nvm_block.setNvMPreWriteDataComp(self.read_optional_value(ctr_tag, "NvMPreWriteDataComp"))
            nvm_block.setNvMPreWriteDataCompDataSize(self.read_optional_value(ctr_tag, "NvMPreWriteDataCompDataSize"))

            self.read_nvm_init_block_callback(ctr_tag, nvm_block)
            self.read_nvm_single_block_callback(ctr_tag, nvm_block)

            nvm_block.setNvMNvBlockBaseNumber(self.read_value(ctr_tag, "NvMNvBlockBaseNumber"))
            self.read_nvm_block_target_block_reference(ctr_tag, nvm_block)

            nvm_block.setNvMBlockWriteProt(self.read_optional_value(ctr_tag, "NvMBlockWriteProt"))
            nvm_block.setNvMBswMBlockStatusInformation(self.read_optional_value(ctr_tag, "NvMBswMBlockStatusInformation"))
            nvm_block.setNvMBlockUseAutoValidation(self.read_optional_value(ctr_tag, "NvMBlockUseAutoValidation"))
            nvm_block.setNvMBlockUseCompression(self.read_optional_value(ctr_tag, "NvMBlockUseCompression"))
            nvm_block.setNvMBlockUsePort(self.read_optional_value(ctr_tag, "NvMBlockUsePort"))
            nvm_block.setNvMBlockUseSetRamBlockStatus(self.read_optional_value(ctr_tag, "NvMBlockUseSetRamBlockStatus"))
            nvm_block.setNvMCalcRamBlockCrc(self.read_optional_value(ctr_tag, "NvMCalcRamBlockCrc"))
            nvm_block.setNvMMaxNumOfReadRetries(self.read_optional_value(ctr_tag, "NvMMaxNumOfReadRetries"))
            nvm_block.setNvMMaxNumOfWriteRetries(self.read_optional_value(ctr_tag, "NvMMaxNumOfWriteRetries"))
            nvm_block.setNvMSelectBlockForFirstInitAll(self.read_optional_value(ctr_tag, "NvMSelectBlockForFirstInitAll"))
            nvm_block.setNvMStaticBlockIDCheck(self.read_optional_value(ctr_tag, "NvMStaticBlockIDCheck"))
            nvm_block.setNvMNvramDeviceId(self.read_optional_value(ctr_tag, "NvMNvramDeviceId"))
            nvm_block.setNvMBlockHeaderInclude(self.read_optional_value(ctr_tag, "NvMBlockHeaderInclude"))
            nvm_block.setNvMBlockCipheringRef(self.read_optional_ref_value(ctr_tag, "NvMBlockCipheringRef"))

            nvm.addNvMBlockDescriptor(nvm_block)

