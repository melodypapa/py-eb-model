from typing import List
from ..models.abstract import EcucParamConfContainerDef, Module, EcucRefType


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

        # type: List[NvMBlockDescriptor]
        self.NvMBlockDescriptors = []
        self.NvMCommon: NvMCommon = None

    def getNvMCommon(self) -> NvMCommon:
        return self.NvMCommon

    def setNvMCommon(self, value: NvMCommon):
        if value is not None:
            self.NvMCommon = value
        return self

    def getNvMBlockDescriptorList(self) -> List[NvMBlockDescriptor]:
        return self.NvMBlockDescriptors

    def addNvMBlockDescriptor(self, value: NvMBlockDescriptor):
        if value is not None:
            self.NvMBlockDescriptors.append(value)
        return self
