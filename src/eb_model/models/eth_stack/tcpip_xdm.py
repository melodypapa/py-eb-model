from typing import List, Optional
import logging
from eb_model.models.core.abstract import EcucParamConfContainerDef, EcucRefType, Module


class TcpIpGeneral(EcucParamConfContainerDef):
    """TcpIp general configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tcpIpDevErrorDetect: bool = None
        self.tcpIpMainFunctionPeriod: float = None
        self.tcpIpBufferSizeMax: int = None
        self.tcpIpMaxNumOfSockets: int = None

    def getTcpIpDevErrorDetect(self) -> bool:
        return self.tcpIpDevErrorDetect

    def setTcpIpDevErrorDetect(self, value: bool):
        if value is not None:
            self.tcpIpDevErrorDetect = value
        return self

    def getTcpIpMainFunctionPeriod(self) -> float:
        return self.tcpIpMainFunctionPeriod

    def setTcpIpMainFunctionPeriod(self, value: float):
        if value is not None:
            self.tcpIpMainFunctionPeriod = value
        return self

    def getTcpIpBufferSizeMax(self) -> int:
        return self.tcpIpBufferSizeMax

    def setTcpIpBufferSizeMax(self, value: int):
        if value is not None:
            self.tcpIpBufferSizeMax = value
        return self

    def getTcpIpMaxNumOfSockets(self) -> int:
        return self.tcpIpMaxNumOfSockets

    def setTcpIpMaxNumOfSockets(self, value: int):
        if value is not None:
            self.tcpIpMaxNumOfSockets = value
        return self


class TcpIpOffloadChecksum(EcucParamConfContainerDef):
    """TcpIp offload checksum configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)


class TcpIpIpV4Ctrl(EcucParamConfContainerDef):
    """TcpIp IPv4 controller configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tcpIpIpV4PathMtuEnabled: bool = None
        self.tcpIpIpV4PathMtuTimeout: float = None

    def getTcpIpIpV4PathMtuEnabled(self) -> bool:
        return self.tcpIpIpV4PathMtuEnabled

    def setTcpIpIpV4PathMtuEnabled(self, value: bool):
        if value is not None:
            self.tcpIpIpV4PathMtuEnabled = value
        return self

    def getTcpIpIpV4PathMtuTimeout(self) -> float:
        return self.tcpIpIpV4PathMtuTimeout

    def setTcpIpIpV4PathMtuTimeout(self, value: float):
        if value is not None:
            self.tcpIpIpV4PathMtuTimeout = value
        return self


class TcpIpIpV6Ctrl(EcucParamConfContainerDef):
    """TcpIp IPv6 controller configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tcpIpIpV6PathMtuEnabled: bool = None
        self.tcpIpIpV6PathMtuTimeout: float = None

    def getTcpIpIpV6PathMtuEnabled(self) -> bool:
        return self.tcpIpIpV6PathMtuEnabled

    def setTcpIpIpV6PathMtuEnabled(self, value: bool):
        if value is not None:
            self.tcpIpIpV6PathMtuEnabled = value
        return self

    def getTcpIpIpV6PathMtuTimeout(self) -> float:
        return self.tcpIpIpV6PathMtuTimeout

    def setTcpIpIpV6PathMtuTimeout(self, value: float):
        if value is not None:
            self.tcpIpIpV6PathMtuTimeout = value
        return self


class TcpIpCtrl(EcucParamConfContainerDef):
    """TcpIp controller configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tcpIpEthIfCtrlRef: EcucRefType = None
        self.tcpIpDhcpServerConfigRef: EcucRefType = None
        self.tcpIpOffloadChecksum: TcpIpOffloadChecksum = None
        self.tcpIpIpV4Ctrl: TcpIpIpV4Ctrl = None
        self.tcpIpIpV6Ctrl: TcpIpIpV6Ctrl = None

    def getTcpIpEthIfCtrlRef(self) -> EcucRefType:
        return self.tcpIpEthIfCtrlRef

    def setTcpIpEthIfCtrlRef(self, value: EcucRefType):
        if value is not None:
            self.tcpIpEthIfCtrlRef = value
        return self

    def getTcpIpDhcpServerConfigRef(self) -> EcucRefType:
        return self.tcpIpDhcpServerConfigRef

    def setTcpIpDhcpServerConfigRef(self, value: EcucRefType):
        if value is not None:
            self.tcpIpDhcpServerConfigRef = value
        return self

    def getTcpIpOffloadChecksum(self) -> TcpIpOffloadChecksum:
        return self.tcpIpOffloadChecksum

    def setTcpIpOffloadChecksum(self, value: TcpIpOffloadChecksum):
        if value is not None:
            self.tcpIpOffloadChecksum = value
        return self

    def getTcpIpIpV4Ctrl(self) -> TcpIpIpV4Ctrl:
        return self.tcpIpIpV4Ctrl

    def setTcpIpIpV4Ctrl(self, value: TcpIpIpV4Ctrl):
        if value is not None:
            self.tcpIpIpV4Ctrl = value
        return self

    def getTcpIpIpV6Ctrl(self) -> TcpIpIpV6Ctrl:
        return self.tcpIpIpV6Ctrl

    def setTcpIpIpV6Ctrl(self, value: TcpIpIpV6Ctrl):
        if value is not None:
            self.tcpIpIpV6Ctrl = value
        return self


class TcpIpLocalAddr(EcucParamConfContainerDef):
    """TcpIp local address configuration container."""
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)

        self.tcpIpAddrId: int = None
        self.tcpIpAddressType: str = None
        self.tcpIpDomainType: str = None

    def getTcpIpAddrId(self) -> int:
        return self.tcpIpAddrId

    def setTcpIpAddrId(self, value: int):
        if value is not None:
            self.tcpIpAddrId = value
        return self

    def getTcpIpAddressType(self) -> str:
        return self.tcpIpAddressType

    def setTcpIpAddressType(self, value: str):
        if value is not None:
            self.tcpIpAddressType = value
        return self

    def getTcpIpDomainType(self) -> str:
        return self.tcpIpDomainType

    def setTcpIpDomainType(self, value: str):
        if value is not None:
            self.tcpIpDomainType = value
        return self


class TcpIp(Module):
    """TcpIp module model."""
    def __init__(self, parent) -> None:
        super().__init__(parent, "TcpIp")

        self.tcpIpGeneral: TcpIpGeneral = None
        self.tcpIpCtrls: List[TcpIpCtrl] = []
        self.tcpIpLocalAddrs: List[TcpIpLocalAddr] = []

        self.logger = logging.getLogger()

    def getTcpIpGeneral(self) -> TcpIpGeneral:
        return self.tcpIpGeneral

    def setTcpIpGeneral(self, value: TcpIpGeneral):
        if value is not None:
            self.tcpIpGeneral = value
        return self

    def getTcpIpCtrlList(self) -> List[TcpIpCtrl]:
        return list(sorted(filter(lambda a: isinstance(a, TcpIpCtrl), self.elements.values()), key=lambda o: o.getName()))

    def addTcpIpCtrl(self, value: TcpIpCtrl):
        self.addElement(value)
        self.tcpIpCtrls.append(value)
        return self

    def getTcpIpLocalAddrList(self) -> List[TcpIpLocalAddr]:
        return list(sorted(filter(lambda a: isinstance(a, TcpIpLocalAddr), self.elements.values()), key=lambda o: o.getName()))

    def addTcpIpLocalAddr(self, value: TcpIpLocalAddr):
        self.addElement(value)
        self.tcpIpLocalAddrs.append(value)
        return self
