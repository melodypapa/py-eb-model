from typing import List, Optional
import logging
from ..core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class FrNmGeneral(EcucParamConfContainerDef):
    """FrNm general configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frNmDevErrorDetect: bool = None
        self.frNmVersionInfoApi: bool = None
        self.frNmMainFunctionPeriod: float = None

    def getFrNmDevErrorDetect(self) -> bool:
        return self.frNmDevErrorDetect

    def setFrNmDevErrorDetect(self, value: bool):
        if value is not None:
            self.frNmDevErrorDetect = value
        return self

    def getFrNmVersionInfoApi(self) -> bool:
        return self.frNmVersionInfoApi

    def setFrNmVersionInfoApi(self, value: bool):
        if value is not None:
            self.frNmVersionInfoApi = value
        return self

    def getFrNmMainFunctionPeriod(self) -> float:
        return self.frNmMainFunctionPeriod

    def setFrNmMainFunctionPeriod(self, value: float):
        if value is not None:
            self.frNmMainFunctionPeriod = value
        return self


class FrNmChannelIdentifiers(EcucParamConfContainerDef):
    """FrNm channel identifiers configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frNmChannelId: int = None

    def getFrNmChannelId(self) -> int:
        return self.frNmChannelId

    def setFrNmChannelId(self, value: int):
        if value is not None:
            self.frNmChannelId = value
        return self


class FrNmRxPdu(EcucParamConfContainerDef):
    """FrNm RxPDU configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frNmRxPduId: int = None
        self.frNmRxPduRef: EcucRefType = None

    def getFrNmRxPduId(self) -> int:
        return self.frNmRxPduId

    def setFrNmRxPduId(self, value: int):
        if value is not None:
            self.frNmRxPduId = value
        return self

    def getFrNmRxPduRef(self) -> EcucRefType:
        return self.frNmRxPduRef

    def setFrNmRxPduRef(self, value: EcucRefType):
        if value is not None:
            self.frNmRxPduRef = value
        return self


class FrNmTxPdu(EcucParamConfContainerDef):
    """FrNm TxPDU configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frNmTxPduId: int = None
        self.frNmTxPduRef: EcucRefType = None

    def getFrNmTxPduId(self) -> int:
        return self.frNmTxPduId

    def setFrNmTxPduId(self, value: int):
        if value is not None:
            self.frNmTxPduId = value
        return self

    def getFrNmTxPduRef(self) -> EcucRefType:
        return self.frNmTxPduRef

    def setFrNmTxPduRef(self, value: EcucRefType):
        if value is not None:
            self.frNmTxPduRef = value
        return self


class FrNmChannel(EcucParamConfContainerDef):
    """FrNm channel configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.frNmChannelIdentifiers: FrNmChannelIdentifiers = None
        self.frNmRxPdu: FrNmRxPdu = None
        self.frNmTxPdu: FrNmTxPdu = None

    def getFrNmChannelIdentifiers(self) -> FrNmChannelIdentifiers:
        return self.frNmChannelIdentifiers

    def setFrNmChannelIdentifiers(self, value: FrNmChannelIdentifiers):
        if value is not None:
            self.frNmChannelIdentifiers = value
        return self

    def getFrNmRxPdu(self) -> FrNmRxPdu:
        return self.frNmRxPdu

    def setFrNmRxPdu(self, value: FrNmRxPdu):
        if value is not None:
            self.frNmRxPdu = value
        return self

    def getFrNmTxPdu(self) -> FrNmTxPdu:
        return self.frNmTxPdu

    def setFrNmTxPdu(self, value: FrNmTxPdu):
        if value is not None:
            self.frNmTxPdu = value
        return self


class FrNm(Module):
    """FrNm module model."""
    def __init__(self, parent) -> None:
        super().__init__(parent, "FrNm")

        self.frNmGeneral: FrNmGeneral = None
        self.frNmChannels: List[FrNmChannel] = []

        self.logger = logging.getLogger()

    def getFrNmGeneral(self) -> FrNmGeneral:
        return self.frNmGeneral

    def setFrNmGeneral(self, value: FrNmGeneral):
        if value is not None:
            self.frNmGeneral = value
        return self

    def getFrNmChannelList(self) -> List[FrNmChannel]:
        return list(sorted(filter(lambda a: isinstance(a, FrNmChannel), self.elements.values()), key=lambda o: o.getName()))

    def addFrNmChannel(self, value: FrNmChannel):
        self.addElement(value)
        self.frNmChannels.append(value)
        return self
