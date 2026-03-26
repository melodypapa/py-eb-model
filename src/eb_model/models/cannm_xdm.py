from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class CanNmGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canNmMultiCoreSupport: bool = None
        self.canNmPnSupported: bool = None
        self.canNmMaxPn: int = None
        self.canNmDetRuntimeChecks: bool = None

    def getCanNmMultiCoreSupport(self) -> bool:
        return self.canNmMultiCoreSupport

    def setCanNmMultiCoreSupport(self, value: bool):
        if value is not None:
            self.canNmMultiCoreSupport = value
        return self

    def getCanNmPnSupported(self) -> bool:
        return self.canNmPnSupported

    def setCanNmPnSupported(self, value: bool):
        if value is not None:
            self.canNmPnSupported = value
        return self

    def getCanNmMaxPn(self) -> int:
        return self.canNmMaxPn

    def setCanNmMaxPn(self, value: int):
        if value is not None:
            self.canNmMaxPn = value
        return self

    def getCanNmDetRuntimeChecks(self) -> bool:
        return self.canNmDetRuntimeChecks

    def setCanNmDetRuntimeChecks(self, value: bool):
        if value is not None:
            self.canNmDetRuntimeChecks = value
        return self


class CanNmGlobalConfig(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canNmDevErrorDetect: bool = None
        self.canNmPassiveModeEnabled: bool = None
        self.canNmBusLoadReductionEnabled: bool = None
        self.canNmRemoteSleepIndEnabled: bool = None
        self.canNmStateChangeIndEnabled: bool = None
        self.canNmComUserDataSupport: bool = None
        self.canNmMainFunctionPeriod: float = None
        self.canNmNumberOfChannels: int = None
        self.canNmNodeIdCallback: str = None

    def getCanNmDevErrorDetect(self) -> bool:
        return self.canNmDevErrorDetect

    def setCanNmDevErrorDetect(self, value: bool):
        if value is not None:
            self.canNmDevErrorDetect = value
        return self

    def getCanNmPassiveModeEnabled(self) -> bool:
        return self.canNmPassiveModeEnabled

    def setCanNmPassiveModeEnabled(self, value: bool):
        if value is not None:
            self.canNmPassiveModeEnabled = value
        return self

    def getCanNmBusLoadReductionEnabled(self) -> bool:
        return self.canNmBusLoadReductionEnabled

    def setCanNmBusLoadReductionEnabled(self, value: bool):
        if value is not None:
            self.canNmBusLoadReductionEnabled = value
        return self

    def getCanNmRemoteSleepIndEnabled(self) -> bool:
        return self.canNmRemoteSleepIndEnabled

    def setCanNmRemoteSleepIndEnabled(self, value: bool):
        if value is not None:
            self.canNmRemoteSleepIndEnabled = value
        return self

    def getCanNmStateChangeIndEnabled(self) -> bool:
        return self.canNmStateChangeIndEnabled

    def setCanNmStateChangeIndEnabled(self, value: bool):
        if value is not None:
            self.canNmStateChangeIndEnabled = value
        return self

    def getCanNmComUserDataSupport(self) -> bool:
        return self.canNmComUserDataSupport

    def setCanNmComUserDataSupport(self, value: bool):
        if value is not None:
            self.canNmComUserDataSupport = value
        return self

    def getCanNmMainFunctionPeriod(self) -> float:
        return self.canNmMainFunctionPeriod

    def setCanNmMainFunctionPeriod(self, value: float):
        if value is not None:
            self.canNmMainFunctionPeriod = value
        return self

    def getCanNmNumberOfChannels(self) -> int:
        return self.canNmNumberOfChannels

    def setCanNmNumberOfChannels(self, value: int):
        if value is not None:
            self.canNmNumberOfChannels = value
        return self

    def getCanNmNodeIdCallback(self) -> str:
        return self.canNmNodeIdCallback

    def setCanNmNodeIdCallback(self, value: str):
        if value is not None:
            self.canNmNodeIdCallback = value
        return self


class CanNmChannel(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canNmNodeIdEnabled: bool = None
        self.canNmPnEnabled: bool = None
        self.canNmMsgCycleTime: float = None
        self.canNmTimeoutTime: float = None
        self.canNmNetworkHandle: int = None
        self.canNmComMNetworkHandleRef: EcucRefType = None
        self.canNmCanNmChannelRef: EcucRefType = None

    def getCanNmNodeIdEnabled(self) -> bool:
        return self.canNmNodeIdEnabled

    def setCanNmNodeIdEnabled(self, value: bool):
        if value is not None:
            self.canNmNodeIdEnabled = value
        return self

    def getCanNmPnEnabled(self) -> bool:
        return self.canNmPnEnabled

    def setCanNmPnEnabled(self, value: bool):
        if value is not None:
            self.canNmPnEnabled = value
        return self

    def getCanNmMsgCycleTime(self) -> float:
        return self.canNmMsgCycleTime

    def setCanNmMsgCycleTime(self, value: float):
        if value is not None:
            self.canNmMsgCycleTime = value
        return self

    def getCanNmTimeoutTime(self) -> float:
        return self.canNmTimeoutTime

    def setCanNmTimeoutTime(self, value: float):
        if value is not None:
            self.canNmTimeoutTime = value
        return self

    def getCanNmNetworkHandle(self) -> int:
        return self.canNmNetworkHandle

    def setCanNmNetworkHandle(self, value: int):
        if value is not None:
            self.canNmNetworkHandle = value
        return self

    def getCanNmComMNetworkHandleRef(self) -> EcucRefType:
        return self.canNmComMNetworkHandleRef

    def setCanNmComMNetworkHandleRef(self, value: EcucRefType):
        if value is not None:
            self.canNmComMNetworkHandleRef = value
        return self

    def getCanNmCanNmChannelRef(self) -> EcucRefType:
        return self.canNmCanNmChannelRef

    def setCanNmCanNmChannelRef(self, value: EcucRefType):
        if value is not None:
            self.canNmCanNmChannelRef = value
        return self


class CanNmRxPdu(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canNmRxPduId: int = None
        self.canNmRxPduRef: EcucRefType = None

    def getCanNmRxPduId(self) -> int:
        return self.canNmRxPduId

    def setCanNmRxPduId(self, value: int):
        if value is not None:
            self.canNmRxPduId = value
        return self

    def getCanNmRxPduRef(self) -> EcucRefType:
        return self.canNmRxPduRef

    def setCanNmRxPduRef(self, value: EcucRefType):
        if value is not None:
            self.canNmRxPduRef = value
        return self


class CanNmTxPdu(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canNmTxConfirmationPduId: int = None
        self.canNmTxPduRef: EcucRefType = None

    def getCanNmTxConfirmationPduId(self) -> int:
        return self.canNmTxConfirmationPduId

    def setCanNmTxConfirmationPduId(self, value: int):
        if value is not None:
            self.canNmTxConfirmationPduId = value
        return self

    def getCanNmTxPduRef(self) -> EcucRefType:
        return self.canNmTxPduRef

    def setCanNmTxPduRef(self, value: EcucRefType):
        if value is not None:
            self.canNmTxPduRef = value
        return self


class CanNmPnFilterMaskByte(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canNmPnFilterMaskByteIndex: int = None
        self.canNmPnFilterMaskByteValue: int = None

    def getCanNmPnFilterMaskByteIndex(self) -> int:
        return self.canNmPnFilterMaskByteIndex

    def setCanNmPnFilterMaskByteIndex(self, value: int):
        if value is not None:
            self.canNmPnFilterMaskByteIndex = value
        return self

    def getCanNmPnFilterMaskByteValue(self) -> int:
        return self.canNmPnFilterMaskByteValue

    def setCanNmPnFilterMaskByteValue(self, value: int):
        if value is not None:
            self.canNmPnFilterMaskByteValue = value
        return self


class CanNmPnInfo(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.canNmPnInfoLength: int = None
        self.canNmPnInfoOffset: int = None
        self.canNmPnFilterMaskBytes: List[CanNmPnFilterMaskByte] = []

    def getCanNmPnInfoLength(self) -> int:
        return self.canNmPnInfoLength

    def setCanNmPnInfoLength(self, value: int):
        if value is not None:
            self.canNmPnInfoLength = value
        return self

    def getCanNmPnInfoOffset(self) -> int:
        return self.canNmPnInfoOffset

    def setCanNmPnInfoOffset(self, value: int):
        if value is not None:
            self.canNmPnInfoOffset = value
        return self

    def getCanNmPnFilterMaskByteList(self) -> List[CanNmPnFilterMaskByte]:
        return list(sorted(filter(lambda a: isinstance(a, CanNmPnFilterMaskByte), self.elements.values()), key=lambda o: o.getName()))

    def addCanNmPnFilterMaskByte(self, value: CanNmPnFilterMaskByte):
        self.addElement(value)
        self.canNmPnFilterMaskBytes.append(value)
        return self


class CanNm(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "CanNm")

        self.canNmGeneral: CanNmGeneral = None
        self.canNmGlobalConfig: CanNmGlobalConfig = None
        self.canNmChannels: List[CanNmChannel] = []
        self.canNmRxPdus: List[CanNmRxPdu] = []
        self.canNmTxPdus: List[CanNmTxPdu] = []
        self.canNmPnInfo: CanNmPnInfo = None

        self.logger = logging.getLogger()

    def getCanNmGeneral(self) -> CanNmGeneral:
        return self.canNmGeneral

    def setCanNmGeneral(self, value: CanNmGeneral):
        if value is not None:
            self.canNmGeneral = value
        return self

    def getCanNmGlobalConfig(self) -> CanNmGlobalConfig:
        return self.canNmGlobalConfig

    def setCanNmGlobalConfig(self, value: CanNmGlobalConfig):
        if value is not None:
            self.canNmGlobalConfig = value
        return self

    def getCanNmChannelList(self) -> List[CanNmChannel]:
        return list(sorted(filter(lambda a: isinstance(a, CanNmChannel), self.elements.values()), key=lambda o: o.getName()))

    def addCanNmChannel(self, value: CanNmChannel):
        self.addElement(value)
        self.canNmChannels.append(value)
        return self

    def getCanNmRxPduList(self) -> List[CanNmRxPdu]:
        return list(sorted(filter(lambda a: isinstance(a, CanNmRxPdu), self.elements.values()), key=lambda o: o.getName()))

    def addCanNmRxPdu(self, value: CanNmRxPdu):
        self.addElement(value)
        self.canNmRxPdus.append(value)
        return self

    def getCanNmTxPduList(self) -> List[CanNmTxPdu]:
        return list(sorted(filter(lambda a: isinstance(a, CanNmTxPdu), self.elements.values()), key=lambda o: o.getName()))

    def addCanNmTxPdu(self, value: CanNmTxPdu):
        self.addElement(value)
        self.canNmTxPdus.append(value)
        return self

    def getCanNmPnInfo(self) -> CanNmPnInfo:
        return self.canNmPnInfo

    def setCanNmPnInfo(self, value: CanNmPnInfo):
        if value is not None:
            self.canNmPnInfo = value
        return self
