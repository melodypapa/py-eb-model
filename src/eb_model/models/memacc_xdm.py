from typing import List, Optional
import logging

from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class MemAccCommon(EcucParamConfContainerDef):
    """Common configuration for MemAcc module."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.memAccDevErrorDetect: bool = None
        self.memAccProtectionApi: str = None
        self.memAccVirtualProtection: bool = None

    def getMemAccDevErrorDetect(self) -> bool:
        return self.memAccDevErrorDetect

    def setMemAccDevErrorDetect(self, value: bool):
        if value is not None:
            self.memAccDevErrorDetect = value
        return self

    def getMemAccProtectionApi(self) -> str:
        return self.memAccProtectionApi

    def setMemAccProtectionApi(self, value: str):
        if value is not None:
            self.memAccProtectionApi = value
        return self

    def getMemAccVirtualProtection(self) -> bool:
        return self.memAccVirtualProtection

    def setMemAccVirtualProtection(self, value: bool):
        if value is not None:
            self.memAccVirtualProtection = value
        return self


class MemAcc(Module):
    """
    AUTOSAR Memory Access (MemAcc) module.

    Provides memory access protection and runtime address validation
    for application and BSW modules.

    Implements: SWR_MEMACC_00001 (MemAcc Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "MemAcc")
        self.memAccCommon: MemAccCommon = None
        self.logger = logging.getLogger()

    def getMemAccCommon(self) -> MemAccCommon:
        return self.memAccCommon

    def setMemAccCommon(self, value: MemAccCommon):
        if value is not None:
            self.memAccCommon = value
        return self