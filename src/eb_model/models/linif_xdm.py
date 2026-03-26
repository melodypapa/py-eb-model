from typing import List, Optional
import logging
from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class LinIfGeneral(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.linIfDevErrorDetect: bool = None
        self.linIfMaxChannels: int = None
        self.linIfTpSupported: bool = None

    def getLinIfDevErrorDetect(self) -> bool:
        return self.linIfDevErrorDetect

    def setLinIfDevErrorDetect(self, value: bool):
        if value is not None:
            self.linIfDevErrorDetect = value
        return self

    def getLinIfMaxChannels(self) -> int:
        return self.linIfMaxChannels

    def setLinIfMaxChannels(self, value: int):
        if value is not None:
            self.linIfMaxChannels = value
        return self

    def getLinIfTpSupported(self) -> bool:
        return self.linIfTpSupported

    def setLinIfTpSupported(self, value: bool):
        if value is not None:
            self.linIfTpSupported = value
        return self


class LinIfChannel(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.linIfChannelId: int = None
        self.linIfChannelRef: EcucRefType = None
        self.linIfComMNetworkHandleRef: EcucRefType = None

    def getLinIfChannelId(self) -> int:
        return self.linIfChannelId

    def setLinIfChannelId(self, value: int):
        if value is not None:
            self.linIfChannelId = value
        return self

    def getLinIfChannelRef(self) -> EcucRefType:
        return self.linIfChannelRef

    def setLinIfChannelRef(self, value: EcucRefType):
        if value is not None:
            self.linIfChannelRef = value
        return self

    def getLinIfComMNetworkHandleRef(self) -> EcucRefType:
        return self.linIfComMNetworkHandleRef

    def setLinIfComMNetworkHandleRef(self, value: EcucRefType):
        if value is not None:
            self.linIfComMNetworkHandleRef = value
        return self


class LinIfFrame(EcucParamConfContainerDef):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.linIfFrameId: int = None
        self.linIfFrameType: str = None
        self.linIfChecksumType: str = None
        self.linIfLength: int = None

    def getLinIfFrameId(self) -> int:
        return self.linIfFrameId

    def setLinIfFrameId(self, value: int):
        if value is not None:
            self.linIfFrameId = value
        return self

    def getLinIfFrameType(self) -> str:
        return self.linIfFrameType

    def setLinIfFrameType(self, value: str):
        if value is not None:
            self.linIfFrameType = value
        return self

    def getLinIfChecksumType(self) -> str:
        return self.linIfChecksumType

    def setLinIfChecksumType(self, value: str):
        if value is not None:
            self.linIfChecksumType = value
        return self

    def getLinIfLength(self) -> int:
        return self.linIfLength

    def setLinIfLength(self, value: int):
        if value is not None:
            self.linIfLength = value
        return self


class LinIf(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "LinIf")
        self.linIfGeneral: LinIfGeneral = None
        self.linIfChannels: List[LinIfChannel] = []
        self.linIfFrames: List[LinIfFrame] = []
        self.logger = logging.getLogger()

    def getLinIfGeneral(self) -> LinIfGeneral:
        return self.linIfGeneral

    def setLinIfGeneral(self, value: LinIfGeneral):
        if value is not None:
            self.linIfGeneral = value
        return self

    def getLinIfChannelList(self) -> List[LinIfChannel]:
        return list(sorted(filter(lambda a: isinstance(a, LinIfChannel), self.elements.values()), key=lambda o: o.getName()))

    def addLinIfChannel(self, value: LinIfChannel):
        self.addElement(value)
        self.linIfChannels.append(value)
        return self

    def getLinIfFrameList(self) -> List[LinIfFrame]:
        return list(sorted(filter(lambda a: isinstance(a, LinIfFrame), self.elements.values()), key=lambda o: o.getName()))

    def addLinIfFrame(self, value: LinIfFrame):
        self.addElement(value)
        self.linIfFrames.append(value)
        return self