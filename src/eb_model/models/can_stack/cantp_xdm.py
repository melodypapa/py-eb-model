from typing import List, Optional
import logging
from eb_model.models.core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class CanTpGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.canTpDevErrorDetect: bool = None
        self.canTpMainFunctionPeriod: float = None
        self.canTpMaxTxChannels: int = None
        self.canTpMaxRxChannels: int = None

    def getCanTpDevErrorDetect(self) -> bool:
        return self.canTpDevErrorDetect

    def setCanTpDevErrorDetect(self, value: bool):
        if value is not None:
            self.canTpDevErrorDetect = value
        return self

    def getCanTpMainFunctionPeriod(self) -> float:
        return self.canTpMainFunctionPeriod

    def setCanTpMainFunctionPeriod(self, value: float):
        if value is not None:
            self.canTpMainFunctionPeriod = value
        return self

    def getCanTpMaxTxChannels(self) -> int:
        return self.canTpMaxTxChannels

    def setCanTpMaxTxChannels(self, value: int):
        if value is not None:
            self.canTpMaxTxChannels = value
        return self

    def getCanTpMaxRxChannels(self) -> int:
        return self.canTpMaxRxChannels

    def setCanTpMaxRxChannels(self, value: int):
        if value is not None:
            self.canTpMaxRxChannels = value
        return self


class CanTpChannel(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.canTpChannelMode: str = None
        self.canTpSTmin: float = None

    def getCanTpChannelMode(self) -> str:
        return self.canTpChannelMode

    def setCanTpChannelMode(self, value: str):
        if value is not None:
            self.canTpChannelMode = value
        return self

    def getCanTpSTmin(self) -> float:
        return self.canTpSTmin

    def setCanTpSTmin(self, value: float):
        if value is not None:
            self.canTpSTmin = value
        return self


class CanTpRxNSdu(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.canTpRxNSduId: int = None
        self.canTpRxNSduRef: EcucRefType = None
        self.canTpBs: int = None
        self.canTpSTmin: float = None

    def getCanTpRxNSduId(self) -> int:
        return self.canTpRxNSduId

    def setCanTpRxNSduId(self, value: int):
        if value is not None:
            self.canTpRxNSduId = value
        return self

    def getCanTpRxNSduRef(self) -> EcucRefType:
        return self.canTpRxNSduRef

    def setCanTpRxNSduRef(self, value: EcucRefType):
        if value is not None:
            self.canTpRxNSduRef = value
        return self

    def getCanTpBs(self) -> int:
        return self.canTpBs

    def setCanTpBs(self, value: int):
        if value is not None:
            self.canTpBs = value
        return self

    def getCanTpSTmin(self) -> float:
        return self.canTpSTmin

    def setCanTpSTmin(self, value: float):
        if value is not None:
            self.canTpSTmin = value
        return self


class CanTpTxNSdu(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.canTpTxNSduId: int = None
        self.canTpTxNSduRef: EcucRefType = None
        self.canTpTc: bool = None
        self.canTpSTmin: float = None

    def getCanTpTxNSduId(self) -> int:
        return self.canTpTxNSduId

    def setCanTpTxNSduId(self, value: int):
        if value is not None:
            self.canTpTxNSduId = value
        return self

    def getCanTpTxNSduRef(self) -> EcucRefType:
        return self.canTpTxNSduRef

    def setCanTpTxNSduRef(self, value: EcucRefType):
        if value is not None:
            self.canTpTxNSduRef = value
        return self

    def getCanTpTc(self) -> bool:
        return self.canTpTc

    def setCanTpTc(self, value: bool):
        if value is not None:
            self.canTpTc = value
        return self

    def getCanTpSTmin(self) -> float:
        return self.canTpSTmin

    def setCanTpSTmin(self, value: float):
        if value is not None:
            self.canTpSTmin = value
        return self


class CanTp(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "CanTp")
        self.canTpGeneral: CanTpGeneral = None
        self.canTpChannels: List[CanTpChannel] = []
        self.canTpRxNSdus: List[CanTpRxNSdu] = []
        self.canTpTxNSdus: List[CanTpTxNSdu] = []
        self.logger = logging.getLogger()

    def getCanTpGeneral(self) -> CanTpGeneral:
        return self.canTpGeneral

    def setCanTpGeneral(self, value: CanTpGeneral):
        if value is not None:
            self.canTpGeneral = value
        return self

    def getCanTpChannelList(self) -> List[CanTpChannel]:
        return list(sorted(filter(lambda a: isinstance(a, CanTpChannel), self.elements.values()), key=lambda o: o.getName()))

    def addCanTpChannel(self, value: CanTpChannel):
        self.addElement(value)
        self.canTpChannels.append(value)
        return self

    def getCanTpRxNSduList(self) -> List[CanTpRxNSdu]:
        return list(sorted(filter(lambda a: isinstance(a, CanTpRxNSdu), self.elements.values()), key=lambda o: o.getName()))

    def addCanTpRxNSdu(self, value: CanTpRxNSdu):
        self.addElement(value)
        self.canTpRxNSdus.append(value)
        return self

    def getCanTpTxNSduList(self) -> List[CanTpTxNSdu]:
        return list(sorted(filter(lambda a: isinstance(a, CanTpTxNSdu), self.elements.values()), key=lambda o: o.getName()))

    def addCanTpTxNSdu(self, value: CanTpTxNSdu):
        self.addElement(value)
        self.canTpTxNSdus.append(value)
        return self
