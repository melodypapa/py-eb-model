from typing import List
from ..models.abstract import EcucParamConfContainerDef, Module, EcucRefType


class NvM(Module):
    def __init__(self, parent):
        super().__init__(parent, "NvM")

        self.NvMBlockDescriptors = []                       # type: List[NvMBlockDescriptor]

    def getNvMBlockDescriptorList(self):
        return self.NvMBlockDescriptors

    def addNvMBlockDescriptor(self, value):
        if value is not None:
            self.NvMBlockDescriptors.append(value)
        return self


class NvMBlockDescriptor(EcucParamConfContainerDef):
    def __init__(self, parent, name):
        super().__init__(parent, name)

        self.nvMBlockCrcType = None                         # type: str # optional
        self.nvMBlockHeaderInclude = None                   # type: int # optional
        self.nvMBlockJobPriority = None                     # type: str # required
        self.nvMBlockManagementType = None                  # type: str # required
        self.nvMBlockUseAutoValidation = None               # required
        self.nvMBlockUseCompression = None                  # required
        self.nvMBlockUseCrc = None                          # required
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
        self.nvMResistantToChangedSw = None                 # required
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
        self.nvMBlockEcucPartitionRef = None                # type: EcucRefType # required

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
