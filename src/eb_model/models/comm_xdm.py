"""
ComM Model Classes - AUTOSAR ComM (Communication Manager) configuration objects.

Implements:
    - SWR_COMM_00001: ComM module model
    - SWR_COMM_00002: ComM channel configuration model
"""
from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, Module


class ComMChannel(EcucParamConfContainerDef):
    """
    ComM channel configuration.

    Represents a single communication channel in the ComM module.

    Implements: SWR_COMM_00002 (ComM channel configuration model)
    """

    def __init__(self, parent: Optional['EcucObject'], name: str) -> None:
        """Initialize ComM channel."""
        super().__init__(parent, name)

        self.comMChannelName: str = None
        self.comMChannelId: int = None

    def getComMChannelName(self) -> str:
        return self.comMChannelName

    def setComMChannelName(self, value: str):
        if value is not None:
            self.comMChannelName = value
        return self

    def getComMChannelId(self) -> int:
        return self.comMChannelId

    def setComMChannelId(self, value: int):
        if value is not None:
            self.comMChannelId = value
        return self


class ComM(Module):
    """
    AUTOSAR ComM (Communication Manager) module configuration.

    Manages communication channels and communication modes for the vehicle.

    Implements: SWR_COMM_00001 (ComM module model)
    """

    def __init__(self, parent: Optional['EcucObject']) -> None:
        """Initialize ComM module."""
        super().__init__(parent, "ComM")

        self.comMChannelList: List[ComMChannel] = []

        self.logger = logging.getLogger()

    def getComMChannelList(self) -> List[ComMChannel]:
        return list(sorted(filter(lambda a: isinstance(a, ComMChannel), self.elements.values()), key=lambda o: o.getName()))

    def addComMChannel(self, value: ComMChannel):
        self.addElement(value)
        self.comMChannelList.append(value)
        return self