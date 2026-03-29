from typing import List, Optional
import logging

from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class MemMapCommon(EcucParamConfContainerDef):
    """Common configuration for MemMap module."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.memMapDevErrorDetect: bool = None
        self.memMapApi: str = None
        self.memMapInitStatus: str = None

    def getMemMapDevErrorDetect(self) -> bool:
        return self.memMapDevErrorDetect

    def setMemMapDevErrorDetect(self, value: bool):
        if value is not None:
            self.memMapDevErrorDetect = value
        return self

    def getMemMapApi(self) -> str:
        return self.memMapApi

    def setMemMapApi(self, value: str):
        if value is not None:
            self.memMapApi = value
        return self

    def getMemMapInitStatus(self) -> str:
        return self.memMapInitStatus

    def setMemMapInitStatus(self, value: str):
        if value is not None:
            self.memMapInitStatus = value
        return self


class MemMap(Module):
    """
    AUTOSAR Memory Mapping (MemMap) module.

    Defines memory layout and section assignments for AUTOSAR
    applications and BSW modules.

    Implements: SWR_MEMMAP_00001 (MemMap Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "MemMap")
        self.memMapCommon: MemMapCommon = None
        self.logger = logging.getLogger()

    def getMemMapCommon(self) -> MemMapCommon:
        return self.memMapCommon

    def setMemMapCommon(self, value: MemMapCommon):
        if value is not None:
            self.memMapCommon = value
        return self