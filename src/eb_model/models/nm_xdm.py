"""
Nm Model Classes - AUTOSAR Nm (Network Management) configuration objects.

Implements:
    - SWR_NM_00001: Nm module model
    - SWR_NM_00002: Nm channel configuration model
"""
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class NmChannel(EcucParamConfContainerDef):
    """
    Nm channel configuration.

    Represents a single Nm channel for network management communication.

    Implements: SWR_NM_00002 (Nm channel configuration model)
    """

    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        """Initialize Nm channel."""
        super().__init__(parent, name)

        self.nmChannelId: int = None
        self.nmBusType: str = None
        self.nmMsgCycleTime: float = None
        self.nmTimeoutTime: float = None
        self.nmNetworkHandle: int = None
        self.nmComMNetworkHandleRef: EcucRefType = None
        self.nmNodeEnabled: bool = None

    def getNmChannelId(self) -> int:
        return self.nmChannelId

    def setNmChannelId(self, value: int):
        if value is not None:
            self.nmChannelId = value
        return self

    def getNmBusType(self) -> str:
        return self.nmBusType

    def setNmBusType(self, value: str):
        if value is not None:
            self.nmBusType = value
        return self

    def getNmMsgCycleTime(self) -> float:
        return self.nmMsgCycleTime

    def setNmMsgCycleTime(self, value: float):
        if value is not None:
            self.nmMsgCycleTime = value
        return self

    def getNmTimeoutTime(self) -> float:
        return self.nmTimeoutTime

    def setNmTimeoutTime(self, value: float):
        if value is not None:
            self.nmTimeoutTime = value
        return self

    def getNmNetworkHandle(self) -> int:
        return self.nmNetworkHandle

    def setNmNetworkHandle(self, value: int):
        if value is not None:
            self.nmNetworkHandle = value
        return self

    def getNmComMNetworkHandleRef(self) -> EcucRefType:
        return self.nmComMNetworkHandleRef

    def setNmComMNetworkHandleRef(self, value: EcucRefType):
        if value is not None:
            self.nmComMNetworkHandleRef = value
        return self

    def getNmNodeEnabled(self) -> bool:
        return self.nmNodeEnabled

    def setNmNodeEnabled(self, value: bool):
        if value is not None:
            self.nmNodeEnabled = value
        return self


class Nm(Module):
    """
    AUTOSAR Nm (Network Management) module configuration.

    Manages network management communication across different bus systems.

    Implements: SWR_NM_00001 (Nm module model)
    """

    def __init__(self, parent: Optional['EcucObject']) -> None:
        """Initialize Nm module."""
        super().__init__(parent, "Nm")

        self.nmChannelList: List[NmChannel] = []

        self.logger = logging.getLogger()

    def getNmChannelList(self) -> List[NmChannel]:
        return list(sorted(filter(lambda a: isinstance(a, NmChannel), self.elements.values()), key=lambda o: o.getName()))

    def addNmChannel(self, value: NmChannel):
        self.addElement(value)
        self.nmChannelList.append(value)
        return self