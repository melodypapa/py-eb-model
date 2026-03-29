from typing import List, Optional
import logging
from eb_model.models.core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class UdpNmGeneral(EcucParamConfContainerDef):
    """UdpNm general configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.udpNmDevErrorDetect: bool = None
        self.udpNmVersionInfoApi: bool = None
        self.udpNmMainFunctionPeriod: float = None

    def getUdpNmDevErrorDetect(self) -> bool:
        return self.udpNmDevErrorDetect

    def setUdpNmDevErrorDetect(self, value: bool):
        if value is not None:
            self.udpNmDevErrorDetect = value
        return self

    def getUdpNmVersionInfoApi(self) -> bool:
        return self.udpNmVersionInfoApi

    def setUdpNmVersionInfoApi(self, value: bool):
        if value is not None:
            self.udpNmVersionInfoApi = value
        return self

    def getUdpNmMainFunctionPeriod(self) -> float:
        return self.udpNmMainFunctionPeriod

    def setUdpNmMainFunctionPeriod(self, value: float):
        if value is not None:
            self.udpNmMainFunctionPeriod = value
        return self


class UdpNmChannelIdentifiers(EcucParamConfContainerDef):
    """UdpNm channel identifiers configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.udpNmChannelId: int = None

    def getUdpNmChannelId(self) -> int:
        return self.udpNmChannelId

    def setUdpNmChannelId(self, value: int):
        if value is not None:
            self.udpNmChannelId = value
        return self


class UdpNmRxPdu(EcucParamConfContainerDef):
    """UdpNm RxPDU configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.udpNmRxPduId: int = None
        self.udpNmRxPduRef: EcucRefType = None

    def getUdpNmRxPduId(self) -> int:
        return self.udpNmRxPduId

    def setUdpNmRxPduId(self, value: int):
        if value is not None:
            self.udpNmRxPduId = value
        return self

    def getUdpNmRxPduRef(self) -> EcucRefType:
        return self.udpNmRxPduRef

    def setUdpNmRxPduRef(self, value: EcucRefType):
        if value is not None:
            self.udpNmRxPduRef = value
        return self


class UdpNmTxPdu(EcucParamConfContainerDef):
    """UdpNm TxPDU configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.udpNmTxPduId: int = None
        self.udpNmTxPduRef: EcucRefType = None

    def getUdpNmTxPduId(self) -> int:
        return self.udpNmTxPduId

    def setUdpNmTxPduId(self, value: int):
        if value is not None:
            self.udpNmTxPduId = value
        return self

    def getUdpNmTxPduRef(self) -> EcucRefType:
        return self.udpNmTxPduRef

    def setUdpNmTxPduRef(self, value: EcucRefType):
        if value is not None:
            self.udpNmTxPduRef = value
        return self


class UdpNmUserDataTxPdu(EcucParamConfContainerDef):
    """UdpNm UserDataTxPDU configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class UdpNmUserDataRxPdu(EcucParamConfContainerDef):
    """UdpNm UserDataRxPdu configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class UdpNmChannel(EcucParamConfContainerDef):
    """UdpNm channel configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.udpNmChannelIdentifiers: UdpNmChannelIdentifiers = None
        self.udpNmRxPdu: UdpNmRxPdu = None
        self.udpNmTxPdu: UdpNmTxPdu = None

    def getUdpNmChannelIdentifiers(self) -> UdpNmChannelIdentifiers:
        return self.udpNmChannelIdentifiers

    def setUdpNmChannelIdentifiers(self, value: UdpNmChannelIdentifiers):
        if value is not None:
            self.udpNmChannelIdentifiers = value
        return self

    def getUdpNmRxPdu(self) -> UdpNmRxPdu:
        return self.udpNmRxPdu

    def setUdpNmRxPdu(self, value: UdpNmRxPdu):
        if value is not None:
            self.udpNmRxPdu = value
        return self

    def getUdpNmTxPdu(self) -> UdpNmTxPdu:
        return self.udpNmTxPdu

    def setUdpNmTxPdu(self, value: UdpNmTxPdu):
        if value is not None:
            self.udpNmTxPdu = value
        return self


class UdpNm(Module):
    """UdpNm module model."""
    def __init__(self, parent) -> None:
        super().__init__(parent, "UdpNm")

        self.udpNmGeneral: UdpNmGeneral = None
        self.udpNmChannels: List[UdpNmChannel] = []

        self.logger = logging.getLogger()

    def getUdpNmGeneral(self) -> UdpNmGeneral:
        return self.udpNmGeneral

    def setUdpNmGeneral(self, value: UdpNmGeneral):
        if value is not None:
            self.udpNmGeneral = value
        return self

    def getUdpNmChannelList(self) -> List[UdpNmChannel]:
        return list(sorted(filter(lambda a: isinstance(a, UdpNmChannel), self.elements.values()), key=lambda o: o.getName()))

    def addUdpNmChannel(self, value: UdpNmChannel):
        self.addElement(value)
        self.udpNmChannels.append(value)
        return self
