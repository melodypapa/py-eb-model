from typing import List
from eb_model.models.core.abstract import EcucParamConfContainerDef, Module, EcucRefType


class NvMTargetBlockReference(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)


class NvMEaRef(NvMTargetBlockReference):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.NvMNameOfEaBlock: EcucRefType = None

    def getNvMNameOfEaBlock(self) -> EcucRefType:
        return self.NvMNameOfEaBlock

    def setNvMNameOfEaBlock(self, value: EcucRefType):
        if value is not None:
            self.NvMNameOfEaBlock = value
        return self


class NvMFeeRef(NvMTargetBlockReference):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.NvMNameOfFeeBlock: EcucRefType = None

    def getNvMNameOfFeeBlock(self) -> EcucRefType:
        return self.NvMNameOfFeeBlock

    def setNvMNameOfFeeBlock(self, value: EcucRefType):
        if value is not None:
            self.NvMNameOfFeeBlock = value
        return self


class NvMCommon(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.NvMApiConfigClass: str = None
        self.NvMBswMMultiBlockJobStatusInformation: bool = None
        self.NvMCompiledConfigId: int = None
        self.NvMCrcNumOfBytes: int = None
        self.NvMCsmRetryCounter: int = None
        self.NvMDatasetSelectionBits: int = None
        self.NvMDevErrorDetect: bool = None
        self.NvMDynamicConfiguration: bool = None
        self.NvMJobPrioritization: bool = None
        self.NvMMainFunctionPeriod: float = None
        self.NvMMultiBlockCallback: str = None
        self.NvMMemAccUsage: bool = None
        self.NvMPollingMode: bool = None
        self.NvMRepeatMirrorOperations: int = None
        self.NvMSetRamBlockStatusApi: bool = None
        self.NvMSizeImmediateJobQueue: int = None
        self.NvMSizeStandardJobQueue: int = None
        self.NvMVersionInfoApi: bool = None
        self.NvMBufferAlignmentValue: str = None
        self.NvMEcucPartitionRefs: List[EcucRefType] = []
        self.NvMMasterEcucPartitionRef: EcucRefType = None

    def getNvMApiConfigClass(self) -> str:
        return self.NvMApiConfigClass

    def setNvMApiConfigClass(self, value: str):
        if value is not None:
            self.NvMApiConfigClass = value
        return self

    def getNvMBswMMultiBlockJobStatusInformation(self) -> bool:
        return self.NvMBswMMultiBlockJobStatusInformation

    def setNvMBswMMultiBlockJobStatusInformation(self, value: bool):
        if value is not None:
            self.NvMBswMMultiBlockJobStatusInformation = value
        return self

    def getNvMCompiledConfigId(self) -> int:
        return self.NvMCompiledConfigId

    def setNvMCompiledConfigId(self, value: int):
        if value is not None:
            self.NvMCompiledConfigId = value
        return self

    def getNvMCrcNumOfBytes(self) -> int:
        return self.NvMCrcNumOfBytes

    def setNvMCrcNumOfBytes(self, value: int):
        if value is not None:
            self.NvMCrcNumOfBytes = value
        return self

    def getNvMCsmRetryCounter(self) -> int:
        return self.NvMCsmRetryCounter

    def setNvMCsmRetryCounter(self, value: int):
        if value is not None:
            self.NvMCsmRetryCounter = value
        return self

    def getNvMDatasetSelectionBits(self) -> int:
        return self.NvMDatasetSelectionBits

    def setNvMDatasetSelectionBits(self, value: int):
        if value is not None:
            self.NvMDatasetSelectionBits = value
        return self

    def getNvMDevErrorDetect(self) -> bool:
        return self.NvMDevErrorDetect

    def setNvMDevErrorDetect(self, value: bool):
        if value is not None:
            self.NvMDevErrorDetect = value
        return self

    def getNvMDynamicConfiguration(self) -> bool:
        return self.NvMDynamicConfiguration

    def setNvMDynamicConfiguration(self, value: bool):
        if value is not None:
            self.NvMDynamicConfiguration = value
        return self

    def getNvMJobPrioritization(self) -> bool:
        return self.NvMJobPrioritization

    def setNvMJobPrioritization(self, value: bool):
        if value is not None:
            self.NvMJobPrioritization = value
        return self

    def getNvMMainFunctionPeriod(self) -> float:
        return self.NvMMainFunctionPeriod

    def setNvMMainFunctionPeriod(self, value: float):
        if value is not None:
            self.NvMMainFunctionPeriod = value
        return self

    def getNvMMultiBlockCallback(self) -> str:
        return self.NvMMultiBlockCallback

    def setNvMMultiBlockCallback(self, value: str):
        if value is not None:
            self.NvMMultiBlockCallback = value
        return self

    def getNvMMemAccUsage(self) -> bool:
        return self.NvMMemAccUsage

    def setNvMMemAccUsage(self, value: bool):
        if value is not None:
            self.NvMMemAccUsage = value
        return self

    def getNvMPollingMode(self) -> bool:
        return self.NvMPollingMode

    def setNvMPollingMode(self, value: bool):
        if value is not None:
            self.NvMPollingMode = value
        return self

    def getNvMRepeatMirrorOperations(self) -> int:
        return self.NvMRepeatMirrorOperations

    def setNvMRepeatMirrorOperations(self, value: int):
        if value is not None:
            self.NvMRepeatMirrorOperations = value
        return self

    def getNvMSetRamBlockStatusApi(self) -> bool:
        return self.NvMSetRamBlockStatusApi

    def setNvMSetRamBlockStatusApi(self, value: bool):
        if value is not None:
            self.NvMSetRamBlockStatusApi = value
        return self

    def getNvMSizeImmediateJobQueue(self) -> int:
        return self.NvMSizeImmediateJobQueue

    def setNvMSizeImmediateJobQueue(self, value: int):
        if value is not None:
            self.NvMSizeImmediateJobQueue = value
        return self

    def getNvMSizeStandardJobQueue(self) -> int:
        return self.NvMSizeStandardJobQueue

    def setNvMSizeStandardJobQueue(self, value: int):
        if value is not None:
            self.NvMSizeStandardJobQueue = value
        return self

    def getNvMVersionInfoApi(self) -> bool:
        return self.NvMVersionInfoApi

    def setNvMVersionInfoApi(self, value: bool):
        if value is not None:
            self.NvMVersionInfoApi = value
        return self

    def getNvMBufferAlignmentValue(self) -> str:
        return self.NvMBufferAlignmentValue

    def setNvMBufferAlignmentValue(self, value: str):
        if value is not None:
            self.NvMBufferAlignmentValue = value
        return self

    def getNvMEcucPartitionRefList(self) -> List[EcucRefType]:
        return self.NvMEcucPartitionRefs

    def addNvMEcucPartitionRef(self, value: EcucRefType):
        if value is not None:
            self.NvMEcucPartitionRefs.append(value)
        return self

    def getNvMMasterEcucPartitionRef(self) -> EcucRefType:
        return self.NvMMasterEcucPartitionRef

    def setNvMMasterEcucPartitionRef(self, value: EcucRefType):
        if value is not None:
            self.NvMMasterEcucPartitionRef = value
        return self


class NvMSingleBlockCallback(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.NvMSingleBlockCallbackFnc: str = None

    def getNvMSingleBlockCallbackFnc(self) -> str:
        return self.NvMSingleBlockCallbackFnc

    def setNvMSingleBlockCallbackFnc(self, value: str):
        if value is not None:
            self.NvMSingleBlockCallbackFnc = value
        return self


class NvMInitBlockCallback(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.NvMInitBlockCallbackFnc: str = None

    def getNvMInitBlockCallbackFnc(self) -> str:
        return self.NvMInitBlockCallbackFnc

    def setNvMInitBlockCallbackFnc(self, value: str):
        if value is not None:
            self.NvMInitBlockCallbackFnc = value
        return self


class CommonPublishedInformation(EcucParamConfContainerDef):
    """
    Common published information containing AUTOSAR version information.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.arMajorVersion: int = None
        self.arMinorVersion: int = None
        self.arPatchVersion: int = None
        self.swMajorVersion: int = None
        self.swMinorVersion: int = None
        self.swPatchVersion: int = None

    def getArMajorVersion(self) -> int:
        return self.arMajorVersion

    def setArMajorVersion(self, value: int):
        if value is not None:
            self.arMajorVersion = value
        return self

    def getArMinorVersion(self) -> int:
        return self.arMinorVersion

    def setArMinorVersion(self, value: int):
        if value is not None:
            self.arMinorVersion = value
        return self

    def getArPatchVersion(self) -> int:
        return self.arPatchVersion

    def setArPatchVersion(self, value: int):
        if value is not None:
            self.arPatchVersion = value
        return self

    def getSwMajorVersion(self) -> int:
        return self.swMajorVersion

    def setSwMajorVersion(self, value: int):
        if value is not None:
            self.swMajorVersion = value
        return self

    def getSwMinorVersion(self) -> int:
        return self.swMinorVersion

    def setSwMinorVersion(self, value: int):
        if value is not None:
            self.swMinorVersion = value
        return self

    def getSwPatchVersion(self) -> int:
        return self.swPatchVersion

    def setSwPatchVersion(self, value: int):
        if value is not None:
            self.swPatchVersion = value
        return self


class PublishedInformation(EcucParamConfContainerDef):
    """
    Module-specific published information.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.vendorId: str = None
        self.arReleaseMajorVersion: str = None
        self.arReleaseMinorVersion: str = None
        self.arReleasePatchVersion: str = None
        self.swMajorVersion: str = None
        self.swMinorVersion: str = None
        self.swPatchVersion: str = None

    def getVendorId(self) -> str:
        return self.vendorId

    def setVendorId(self, value: str):
        if value is not None:
            self.vendorId = value
        return self

    def getArReleaseMajorVersion(self) -> str:
        return self.arReleaseMajorVersion

    def setArReleaseMajorVersion(self, value: str):
        if value is not None:
            self.arReleaseMajorVersion = value
        return self

    def getArReleaseMinorVersion(self) -> str:
        return self.arReleaseMinorVersion

    def setArReleaseMinorVersion(self, value: str):
        if value is not None:
            self.arReleaseMinorVersion = value
        return self

    def getArReleasePatchVersion(self) -> str:
        return self.arReleasePatchVersion

    def setArReleasePatchVersion(self, value: str):
        if value is not None:
            self.arReleasePatchVersion = value
        return self

    def getSwMajorVersion(self) -> str:
        return self.swMajorVersion

    def setSwMajorVersion(self, value: str):
        if value is not None:
            self.swMajorVersion = value
        return self

    def getSwMinorVersion(self) -> str:
        return self.swMinorVersion

    def setSwMinorVersion(self, value: str):
        if value is not None:
            self.swMinorVersion = value
        return self

    def getSwPatchVersion(self) -> str:
        return self.swPatchVersion

    def setSwPatchVersion(self, value: str):
        if value is not None:
            self.swPatchVersion = value
        return self


class NvMDefensiveProgramming(EcucParamConfContainerDef):
    """
    Defensive programming configuration for NvM module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.nvMNullPointerCheck: bool = None
        self.nvMParameterCheck: bool = None

    def getNvMNullPointerCheck(self) -> bool:
        return self.nvMNullPointerCheck

    def setNvMNullPointerCheck(self, value: bool):
        if value is not None:
            self.nvMNullPointerCheck = value
        return self

    def getNvMParameterCheck(self) -> bool:
        return self.nvMParameterCheck

    def setNvMParameterCheck(self, value: bool):
        if value is not None:
            self.nvMParameterCheck = value
        return self


class NvMCommonCryptoSecurityParameters(EcucParamConfContainerDef):
    """
    Common crypto security parameters for NvM module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.nvMCryptoPrimitive: str = None
        self.nvMKeyAddress: int = None

    def getNvMCryptoPrimitive(self) -> str:
        return self.nvMCryptoPrimitive

    def setNvMCryptoPrimitive(self, value: str):
        if value is not None:
            self.nvMCryptoPrimitive = value
        return self

    def getNvMKeyAddress(self) -> int:
        return self.nvMKeyAddress

    def setNvMKeyAddress(self, value: int):
        if value is not None:
            self.nvMKeyAddress = value
        return self


class NvMServiceAPI(EcucParamConfContainerDef):
    """
    Service API configuration for NvM module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.nvMVersionInfoApi: bool = None

    def getNvMVersionInfoApi(self) -> bool:
        return self.nvMVersionInfoApi

    def setNvMVersionInfoApi(self, value: bool):
        if value is not None:
            self.nvMVersionInfoApi = value
        return self


class NvmDemEventParameterRefs(EcucParamConfContainerDef):
    """
    DEM event parameter references for NvM module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class ReportToDem(EcucParamConfContainerDef):
    """
    DEM reporting configuration for NvM module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.nvMReportStorageFailed: bool = None
        self.nvMReportVerificationFailed: bool = None

    def getNvMReportStorageFailed(self) -> bool:
        return self.nvMReportStorageFailed

    def setNvMReportStorageFailed(self, value: bool):
        if value is not None:
            self.nvMReportStorageFailed = value
        return self

    def getNvMReportVerificationFailed(self) -> bool:
        return self.nvMReportVerificationFailed

    def setNvMReportVerificationFailed(self, value: bool):
        if value is not None:
            self.nvMReportVerificationFailed = value
        return self


class MultiCoreCallout(EcucParamConfContainerDef):
    """
    Multi-core callout configuration for NvM module.
    """
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class NvMBlockDescriptor(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.nvMBlockCrcType = None                         # type: str # optional
        self.nvMBlockHeaderInclude = None                   # type: int # optional
        self.nvMBlockJobPriority: int = None
        self.nvMBlockManagementType = None                  # type: str # required
        self.nvMBlockUseAutoValidation = None               # required
        self.nvMBlockUseCompression = None                  # required
        self.nvMBlockUseCrc: bool = False
        self.nvMBlockUseCRCCompMechanism = None             # required
        self.NvMBlockUsePort = None                         # required
        self.nvMBlockUseSetRamBlockStatus = None            # required
        self.nvMBlockUseSyncMechanism = None                # required
        self.nvMBlockWriteProt = None                       # required
        self.nvMBswMBlockStatusInformation = None           # required
        self.nvMCalcRamBlockCrc = None                      # optional
        self.nvMMaxNumOfReadRetries = None                  # required
        self.nvMMaxNumOfWriteRetries = None                 # required
        self.nvMNvBlockBaseNumber = None                    # required
        self.nvMNvBlockLength = None                        # type: int # required
        self.nvMNvBlockNum = None                           # type: int # required
        self.nvMNvramBlockIdentifier = None                 # required
        self.nvMNvramDeviceId = None                        # required
        self.nvMRamBlockDataAddress = None                  # optional
        self.nvMReadRamBlockFromNvCallback = None           # optional
        self.nvMResistantToChangedSw: bool = False
        self.nvMRomBlockDataAddress = None                  # optional
        self.nvMRomBlockNum = None                          # required
        self.nvMSelectBlockForFirstInitAll = None           # optional
        self.nvMSelectBlockForReadAll = None                # required
        self.nvMSelectBlockForWriteAll = None               # required
        self.nvMStaticBlockIDCheck = None                   # required
        self.nvMWriteBlockOnce = None                       # required
        self.nvMWriteRamBlockToNvCallback = None            # optional
        self.nvMWriteVerification = None                    # required
        self.nvMWriteVerificationDataSize = None            # required
        self.nvMBlockCipheringRef = None                    # optional
        self.nvMBlockEcucPartitionRef: EcucRefType = None
        self.nvMAdvancedRecovery: bool = False
        self.aSR2011CallbackEnabled: bool = False
        self.nvMExtraBlockChecks: bool = False
        self.nvMProvideRteAdminPort: bool = False
        self.nvMProvideRteInitBlockPort: bool = False

        self.nvMInitBlockCallback: NvMInitBlockCallback = None
        self.nvMSingleBlockCallback: NvMSingleBlockCallback = None
        self.nvMTargetBlockReference: NvMTargetBlockReference = None

        # EB extended
        self.nvMProvideRteJobFinishedPort: bool = False
        self.nvMProvideRteServicePort: bool = False

    def getNvMBlockCrcType(self):
        return self.nvMBlockCrcType

    def setNvMBlockCrcType(self, value):
        if value is not None:
            self.nvMBlockCrcType = value
        return self

    def getNvMBlockHeaderInclude(self):
        return self.nvMBlockHeaderInclude

    def setNvMBlockHeaderInclude(self, value):
        if value is not None:
            self.nvMBlockHeaderInclude = value
        return self

    def getNvMBlockJobPriority(self):
        return self.nvMBlockJobPriority

    def setNvMBlockJobPriority(self, value):
        if value is not None:
            self.nvMBlockJobPriority = value
        return self

    def getNvMBlockManagementType(self):
        return self.nvMBlockManagementType

    def setNvMBlockManagementType(self, value):
        if value is not None:
            self.nvMBlockManagementType = value
        return self

    def getNvMBlockUseAutoValidation(self):
        return self.nvMBlockUseAutoValidation

    def setNvMBlockUseAutoValidation(self, value):
        if value is not None:
            self.nvMBlockUseAutoValidation = value
        return self

    def getNvMBlockUseCompression(self):
        return self.nvMBlockUseCompression

    def setNvMBlockUseCompression(self, value):
        if value is not None:
            self.nvMBlockUseCompression = value
        return self

    def getNvMBlockUseCrc(self):
        return self.nvMBlockUseCrc

    def setNvMBlockUseCrc(self, value):
        if value is not None:
            self.nvMBlockUseCrc = value
        return self

    def getNvMBlockUseCRCCompMechanism(self):
        return self.nvMBlockUseCRCCompMechanism

    def setNvMBlockUseCRCCompMechanism(self, value):
        if value is not None:
            self.nvMBlockUseCRCCompMechanism = value
        return self

    def getNvMBlockUsePort(self):
        return self.NvMBlockUsePort

    def setNvMBlockUsePort(self, value):
        if value is not None:
            self.NvMBlockUsePort = value
        return self

    def getNvMBlockUseSetRamBlockStatus(self):
        return self.nvMBlockUseSetRamBlockStatus

    def setNvMBlockUseSetRamBlockStatus(self, value):
        if value is not None:
            self.nvMBlockUseSetRamBlockStatus = value
        return self

    def getNvMBlockUseSyncMechanism(self):
        return self.nvMBlockUseSyncMechanism

    def setNvMBlockUseSyncMechanism(self, value):
        if value is not None:
            self.nvMBlockUseSyncMechanism = value
        return self

    def getNvMBlockWriteProt(self):
        return self.nvMBlockWriteProt

    def setNvMBlockWriteProt(self, value):
        if value is not None:
            self.nvMBlockWriteProt = value
        return self

    def getNvMBswMBlockStatusInformation(self):
        return self.nvMBswMBlockStatusInformation

    def setNvMBswMBlockStatusInformation(self, value):
        if value is not None:
            self.nvMBswMBlockStatusInformation = value
        return self

    def getNvMCalcRamBlockCrc(self):
        return self.nvMCalcRamBlockCrc

    def setNvMCalcRamBlockCrc(self, value):
        if value is not None:
            self.nvMCalcRamBlockCrc = value
        return self

    def getNvMMaxNumOfReadRetries(self):
        return self.nvMMaxNumOfReadRetries

    def setNvMMaxNumOfReadRetries(self, value):
        if value is not None:
            self.nvMMaxNumOfReadRetries = value
        return self

    def getNvMMaxNumOfWriteRetries(self):
        return self.nvMMaxNumOfWriteRetries

    def setNvMMaxNumOfWriteRetries(self, value):
        if value is not None:
            self.nvMMaxNumOfWriteRetries = value
        return self

    def getNvMNvBlockBaseNumber(self):
        return self.nvMNvBlockBaseNumber

    def setNvMNvBlockBaseNumber(self, value):
        if value is not None:
            self.nvMNvBlockBaseNumber = value
        return self

    def getNvMNvBlockLength(self):
        return self.nvMNvBlockLength

    def setNvMNvBlockLength(self, value):
        if value is not None:
            self.nvMNvBlockLength = value
        return self

    def getNvMNvBlockNum(self):
        return self.nvMNvBlockNum

    def setNvMNvBlockNum(self, value):
        if value is not None:
            self.nvMNvBlockNum = value
        return self

    def getNvMNvramBlockIdentifier(self):
        return self.nvMNvramBlockIdentifier

    def setNvMNvramBlockIdentifier(self, value):
        if value is not None:
            self.nvMNvramBlockIdentifier = value
        return self

    def getNvMNvramDeviceId(self):
        return self.nvMNvramDeviceId

    def setNvMNvramDeviceId(self, value):
        if value is not None:
            self.nvMNvramDeviceId = value
        return self

    def getNvMRamBlockDataAddress(self):
        return self.nvMRamBlockDataAddress

    def setNvMRamBlockDataAddress(self, value):
        if value is not None:
            self.nvMRamBlockDataAddress = value
        return self

    def getNvMReadRamBlockFromNvCallback(self):
        return self.nvMReadRamBlockFromNvCallback

    def setNvMReadRamBlockFromNvCallback(self, value):
        if value is not None:
            self.nvMReadRamBlockFromNvCallback = value
        return self

    def getNvMResistantToChangedSw(self):
        return self.nvMResistantToChangedSw

    def setNvMResistantToChangedSw(self, value):
        if value is not None:
            self.nvMResistantToChangedSw = value
        return self

    def getNvMRomBlockDataAddress(self):
        return self.nvMRomBlockDataAddress

    def setNvMRomBlockDataAddress(self, value):
        if value is not None:
            self.nvMRomBlockDataAddress = value
        return self

    def getNvMRomBlockNum(self):
        return self.nvMRomBlockNum

    def setNvMRomBlockNum(self, value):
        if value is not None:
            self.nvMRomBlockNum = value
        return self

    def getNvMSelectBlockForFirstInitAll(self):
        return self.nvMSelectBlockForFirstInitAll

    def setNvMSelectBlockForFirstInitAll(self, value):
        if value is not None:
            self.nvMSelectBlockForFirstInitAll = value
        return self

    def getNvMSelectBlockForReadAll(self):
        return self.nvMSelectBlockForReadAll

    def setNvMSelectBlockForReadAll(self, value):
        if value is not None:
            self.nvMSelectBlockForReadAll = value
        return self

    def getNvMSelectBlockForWriteAll(self):
        return self.nvMSelectBlockForWriteAll

    def setNvMSelectBlockForWriteAll(self, value):
        if value is not None:
            self.nvMSelectBlockForWriteAll = value
        return self

    def getNvMStaticBlockIDCheck(self):
        return self.nvMStaticBlockIDCheck

    def setNvMStaticBlockIDCheck(self, value):
        if value is not None:
            self.nvMStaticBlockIDCheck = value
        return self

    def getNvMWriteBlockOnce(self):
        return self.nvMWriteBlockOnce

    def setNvMWriteBlockOnce(self, value):
        if value is not None:
            self.nvMWriteBlockOnce = value
        return self

    def getNvMWriteRamBlockToNvCallback(self):
        return self.nvMWriteRamBlockToNvCallback

    def setNvMWriteRamBlockToNvCallback(self, value):
        if value is not None:
            self.nvMWriteRamBlockToNvCallback = value
        return self

    def getNvMWriteVerification(self):
        return self.nvMWriteVerification

    def setNvMWriteVerification(self, value):
        if value is not None:
            self.nvMWriteVerification = value
        return self

    def getNvMWriteVerificationDataSize(self):
        return self.nvMWriteVerificationDataSize

    def setNvMWriteVerificationDataSize(self, value):
        if value is not None:
            self.nvMWriteVerificationDataSize = value
        return self

    def getNvMBlockCipheringRef(self):
        return self.nvMBlockCipheringRef

    def setNvMBlockCipheringRef(self, value):
        if value is not None:
            self.nvMBlockCipheringRef = value
        return self

    def getNvMBlockEcucPartitionRef(self) -> EcucRefType:
        return self.nvMBlockEcucPartitionRef

    def setNvMBlockEcucPartitionRef(self, value: EcucRefType):
        if value is not None:
            self.nvMBlockEcucPartitionRef = value
        return self

    def getNvMAdvancedRecovery(self) -> bool:
        return self.nvMAdvancedRecovery

    def setNvMAdvancedRecovery(self, value: bool):
        if value is not None:
            self.nvMAdvancedRecovery = value
        return self

    def getASR2011CallbackEnabled(self) -> bool:
        return self.aSR2011CallbackEnabled

    def setASR2011CallbackEnabled(self, value: bool):
        if value is not None:
            self.aSR2011CallbackEnabled = value
        return self

    def getNvMExtraBlockChecks(self) -> bool:
        return self.nvMExtraBlockChecks

    def setNvMExtraBlockChecks(self, value: bool):
        if value is not None:
            self.nvMExtraBlockChecks = value
        return self

    def getNvMProvideRteAdminPort(self) -> bool:
        return self.nvMProvideRteAdminPort

    def setNvMProvideRteAdminPort(self, value: bool):
        if value is not None:
            self.nvMProvideRteAdminPort = value
        return self

    def getNvMProvideRteInitBlockPort(self) -> bool:
        return self.nvMProvideRteInitBlockPort

    def setNvMProvideRteInitBlockPort(self, value: bool):
        if value is not None:
            self.nvMProvideRteInitBlockPort = value
        return self

    def getNvMInitBlockCallback(self) -> NvMInitBlockCallback:
        return self.nvMInitBlockCallback

    def setNvMInitBlockCallback(self, value: NvMInitBlockCallback):
        if value is not None:
            self.nvMInitBlockCallback = value
        return self

    def getNvMSingleBlockCallback(self) -> NvMSingleBlockCallback:
        return self.nvMSingleBlockCallback

    def setNvMSingleBlockCallback(self, value: NvMSingleBlockCallback):
        if value is not None:
            self.nvMSingleBlockCallback = value
        return self

    def getNvMTargetBlockReference(self) -> NvMTargetBlockReference:
        return self.nvMTargetBlockReference

    def setNvMTargetBlockReference(self, value: NvMTargetBlockReference):
        if value is not None:
            self.nvMTargetBlockReference = value
        return self

    def getNvMProvideRteJobFinishedPort(self) -> bool:
        return self.nvMProvideRteJobFinishedPort

    def setNvMProvideRteJobFinishedPort(self, value: bool):
        if value is not None:
            self.nvMProvideRteJobFinishedPort = value
        return self

    def getNvMProvideRteServicePort(self) -> bool:
        return self.nvMProvideRteServicePort

    def setNvMProvideRteServicePort(self, value: bool):
        if value is not None:
            self.nvMProvideRteServicePort = value
        return self


class NvM(Module):
    def __init__(self, parent):
        super().__init__(parent, "NvM")

        self.NvMBlockDescriptors: List[NvMBlockDescriptor] = []
        self.NvMCommon: NvMCommon = None
        self.commonPublishedInformation: CommonPublishedInformation = None
        self.publishedInformation: PublishedInformation = None
        self.nvMDefensiveProgramming: NvMDefensiveProgramming = None
        self.nvMCommonCryptoSecurityParameters: NvMCommonCryptoSecurityParameters = None
        self.nvMServiceAPI: NvMServiceAPI = None
        self.nvmDemEventParameterRefs: NvmDemEventParameterRefs = None
        self.reportToDem: ReportToDem = None
        self.multiCoreCallout: MultiCoreCallout = None

    def getNvMCommon(self) -> NvMCommon:
        return self.NvMCommon

    def setNvMCommon(self, value: NvMCommon):
        if value is not None:
            self.NvMCommon = value
        return self

    def getCommonPublishedInformation(self) -> CommonPublishedInformation:
        return self.commonPublishedInformation

    def setCommonPublishedInformation(self, value: CommonPublishedInformation):
        if value is not None:
            self.commonPublishedInformation = value
        return self

    def getPublishedInformation(self) -> PublishedInformation:
        return self.publishedInformation

    def setPublishedInformation(self, value: PublishedInformation):
        if value is not None:
            self.publishedInformation = value
        return self

    def getNvMDefensiveProgramming(self) -> NvMDefensiveProgramming:
        return self.nvMDefensiveProgramming

    def setNvMDefensiveProgramming(self, value: NvMDefensiveProgramming):
        if value is not None:
            self.nvMDefensiveProgramming = value
        return self

    def getNvMCommonCryptoSecurityParameters(self) -> NvMCommonCryptoSecurityParameters:
        return self.nvMCommonCryptoSecurityParameters

    def setNvMCommonCryptoSecurityParameters(self, value: NvMCommonCryptoSecurityParameters):
        if value is not None:
            self.nvMCommonCryptoSecurityParameters = value
        return self

    def getNvMServiceAPI(self) -> NvMServiceAPI:
        return self.nvMServiceAPI

    def setNvMServiceAPI(self, value: NvMServiceAPI):
        if value is not None:
            self.nvMServiceAPI = value
        return self

    def getNvmDemEventParameterRefs(self) -> NvmDemEventParameterRefs:
        return self.nvmDemEventParameterRefs

    def setNvmDemEventParameterRefs(self, value: NvmDemEventParameterRefs):
        if value is not None:
            self.nvmDemEventParameterRefs = value
        return self

    def getReportToDem(self) -> ReportToDem:
        return self.reportToDem

    def setReportToDem(self, value: ReportToDem):
        if value is not None:
            self.reportToDem = value
        return self

    def getMultiCoreCallout(self) -> MultiCoreCallout:
        return self.multiCoreCallout

    def setMultiCoreCallout(self, value: MultiCoreCallout):
        if value is not None:
            self.multiCoreCallout = value
        return self

    def getNvMBlockDescriptorList(self) -> List[NvMBlockDescriptor]:
        return self.NvMBlockDescriptors

    def addNvMBlockDescriptor(self, value: NvMBlockDescriptor):
        if value is not None:
            self.NvMBlockDescriptors.append(value)
        return self
