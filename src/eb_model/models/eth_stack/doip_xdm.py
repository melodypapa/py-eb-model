from typing import List, Optional
import logging
from eb_model.models.core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class DoIPGeneral(EcucParamConfContainerDef):
    """DoIP general configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.doIPDevErrorDetect: bool = None
        self.doIPVersionInfoApi: bool = None
        self.doIPMainFunctionPeriod: float = None

    def getDoIPDevErrorDetect(self) -> bool:
        return self.doIPDevErrorDetect

    def setDoIPDevErrorDetect(self, value: bool):
        if value is not None:
            self.doIPDevErrorDetect = value
        return self

    def getDoIPVersionInfoApi(self) -> bool:
        return self.doIPVersionInfoApi

    def setDoIPVersionInfoApi(self, value: bool):
        if value is not None:
            self.doIPVersionInfoApi = value
        return self

    def getDoIPMainFunctionPeriod(self) -> float:
        return self.doIPMainFunctionPeriod

    def setDoIPMainFunctionPeriod(self, value: float):
        if value is not None:
            self.doIPMainFunctionPeriod = value
        return self


class DoIPPduRRxPdu(EcucParamConfContainerDef):
    """DoIP PduRRxPDU configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class DoIPPduRTxPdu(EcucParamConfContainerDef):
    """DoIP PduRTxPdu configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class DoIPChannel(EcucParamConfContainerDef):
    """DoIP channel configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.doIPPduRRxPdu: DoIPPduRRxPdu = None
        self.doIPPduRTxPdu: DoIPPduRTxPdu = None

    def getDoIPPduRRxPdu(self) -> DoIPPduRRxPdu:
        return self.doIPPduRRxPdu

    def setDoIPPduRRxPdu(self, value: DoIPPduRRxPdu):
        if value is not None:
            self.doIPPduRRxPdu = value
        return self

    def getDoIPPduRTxPdu(self) -> DoIPPduRTxPdu:
        return self.doIPPduRTxPdu

    def setDoIPPduRTxPdu(self, value: DoIPPduRTxPdu):
        if value is not None:
            self.doIPPduRTxPdu = value
        return self


class DoIPSoAdRxPdu(EcucParamConfContainerDef):
    """DoIP SoAdRxPDU configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class DoIPSoAdTxPdu(EcucParamConfContainerDef):
    """DoIP SoAdTxPdu configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class DoIPTcpConnection(EcucParamConfContainerDef):
    """DoIP TCP connection configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.doIPSoAdRxPdu: DoIPSoAdRxPdu = None
        self.doIPSoAdTxPdu: DoIPSoAdTxPdu = None

    def getDoIPSoAdRxPdu(self) -> DoIPSoAdRxPdu:
        return self.doIPSoAdRxPdu

    def setDoIPSoAdRxPdu(self, value: DoIPSoAdRxPdu):
        if value is not None:
            self.doIPSoAdRxPdu = value
        return self

    def getDoIPSoAdTxPdu(self) -> DoIPSoAdTxPdu:
        return self.doIPSoAdTxPdu

    def setDoIPSoAdTxPdu(self, value: DoIPSoAdTxPdu):
        if value is not None:
            self.doIPSoAdTxPdu = value
        return self


class DoIPUdpConnection(EcucParamConfContainerDef):
    """DoIP UDP connection configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.doIPSoAdRxPdu: DoIPSoAdRxPdu = None
        self.doIPSoAdTxPdu: DoIPSoAdTxPdu = None

    def getDoIPSoAdRxPdu(self) -> DoIPSoAdRxPdu:
        return self.doIPSoAdRxPdu

    def setDoIPSoAdRxPdu(self, value: DoIPSoAdRxPdu):
        if value is not None:
            self.doIPSoAdRxPdu = value
        return self

    def getDoIPSoAdTxPdu(self) -> DoIPSoAdTxPdu:
        return self.doIPSoAdTxPdu

    def setDoIPSoAdTxPdu(self, value: DoIPSoAdTxPdu):
        if value is not None:
            self.doIPSoAdTxPdu = value
        return self


class DoIPUdpVehicleAnnouncement(EcucParamConfContainerDef):
    """DoIP UDP vehicle announcement configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.doIPSoAdTxPdu: DoIPSoAdTxPdu = None

    def getDoIPSoAdTxPdu(self) -> DoIPSoAdTxPdu:
        return self.doIPSoAdTxPdu

    def setDoIPSoAdTxPdu(self, value: DoIPSoAdTxPdu):
        if value is not None:
            self.doIPSoAdTxPdu = value
        return self


class DoIPConnections(EcucParamConfContainerDef):
    """DoIP connections configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.doIPTcpConnections: List[DoIPTcpConnection] = []
        self.doIPUdpConnections: List[DoIPUdpConnection] = []
        self.doIPUdpVehicleAnnouncement: DoIPUdpVehicleAnnouncement = None

    def getDoIPTcpConnectionList(self) -> List[DoIPTcpConnection]:
        return list(sorted(filter(lambda a: isinstance(a, DoIPTcpConnection), self.elements.values()), key=lambda o: o.getName()))

    def addDoIPTcpConnection(self, value: DoIPTcpConnection):
        self.addElement(value)
        self.doIPTcpConnections.append(value)
        return self

    def getDoIPUdpConnectionList(self) -> List[DoIPUdpConnection]:
        return list(sorted(filter(lambda a: isinstance(a, DoIPUdpConnection), self.elements.values()), key=lambda o: o.getName()))

    def addDoIPUdpConnection(self, value: DoIPUdpConnection):
        self.addElement(value)
        self.doIPUdpConnections.append(value)
        return self

    def getDoIPUdpVehicleAnnouncement(self) -> DoIPUdpVehicleAnnouncement:
        return self.doIPUdpVehicleAnnouncement

    def setDoIPUdpVehicleAnnouncement(self, value: DoIPUdpVehicleAnnouncement):
        if value is not None:
            self.doIPUdpVehicleAnnouncement = value
        return self


class DoIP(Module):
    """DoIP module model."""
    def __init__(self, parent) -> None:
        super().__init__(parent, "DoIP")

        self.doIPGeneral: DoIPGeneral = None
        self.doIPChannels: List[DoIPChannel] = []
        self.doIPCustomChannels: List[DoIPChannel] = []
        self.doIPConnections: DoIPConnections = None

        self.logger = logging.getLogger()

    def getDoIPGeneral(self) -> DoIPGeneral:
        return self.doIPGeneral

    def setDoIPGeneral(self, value: DoIPGeneral):
        if value is not None:
            self.doIPGeneral = value
        return self

    def getDoIPChannelList(self) -> List[DoIPChannel]:
        return list(sorted(
            filter(
                lambda a: isinstance(a, DoIPChannel) and a not in self.doIPCustomChannels,
                self.elements.values()
            ),
            key=lambda o: o.getName()
        ))

    def addDoIPChannel(self, value: DoIPChannel):
        self.addElement(value)
        self.doIPChannels.append(value)
        return self

    def getDoIPCustomChannelList(self) -> List[DoIPChannel]:
        return list(sorted(
            filter(
                lambda a: isinstance(a, DoIPChannel) and a in self.doIPCustomChannels,
                self.elements.values()
            ),
            key=lambda o: o.getName()
        ))

    def addDoIPCustomChannel(self, value: DoIPChannel):
        self.addElement(value)
        self.doIPCustomChannels.append(value)
        return self

    def getDoIPConnections(self) -> DoIPConnections:
        return self.doIPConnections

    def setDoIPConnections(self, value: DoIPConnections):
        if value is not None:
            self.doIPConnections = value
        return self
