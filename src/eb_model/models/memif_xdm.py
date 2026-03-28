from typing import List, Optional
import logging

from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class MemIfInit(EcucParamConfContainerDef):
    """Initialization configuration for MemIf module."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.memIfDevErrorDetect: bool = None
        self.memIfIndex: int = None
        self.memIfJobPriority: str = None
        self.memIfMaxNumberJobs: int = None

    def getMemIfDevErrorDetect(self) -> bool:
        return self.memIfDevErrorDetect

    def setMemIfDevErrorDetect(self, value: bool):
        if value is not None:
            self.memIfDevErrorDetect = value
        return self

    def getMemIfIndex(self) -> int:
        return self.memIfIndex

    def setMemIfIndex(self, value: int):
        if value is not None:
            self.memIfIndex = value
        return self

    def getMemIfJobPriority(self) -> str:
        return self.memIfJobPriority

    def setMemIfJobPriority(self, value: str):
        if value is not None:
            self.memIfJobPriority = value
        return self

    def getMemIfMaxNumberJobs(self) -> int:
        return self.memIfMaxNumberJobs

    def setMemIfMaxNumberJobs(self, value: int):
        if value is not None:
            self.memIfMaxNumberJobs = value
        return self


class MemIf(Module):
    """
    AUTOSAR Memory Abstraction Interface (MemIf) module.

    Provides a standardized interface between upper layer modules
    and hardware-specific memory drivers (Fee, Ea).

    Implements: SWR_MEMIF_00001 (MemIf Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "MemIf")
        self.memIfInit: MemIfInit = None
        self.logger = logging.getLogger()

    def getMemIfInit(self) -> MemIfInit:
        return self.memIfInit

    def setMemIfInit(self, value: MemIfInit):
        if value is not None:
            self.memIfInit = value
        return self