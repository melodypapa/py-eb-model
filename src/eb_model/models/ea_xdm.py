from typing import List, Optional
import logging

from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class EaGeneral(EcucParamConfContainerDef):
    """General configuration for Ea module."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.eaDevErrorDetect: bool = None
        self.eaPageSize: int = None
        self.eaAddressAlignment: int = None
        self.eaReadMode: str = None

    def getEaDevErrorDetect(self) -> bool:
        return self.eaDevErrorDetect

    def setEaDevErrorDetect(self, value: bool):
        if value is not None:
            self.eaDevErrorDetect = value
        return self

    def getEaPageSize(self) -> int:
        return self.eaPageSize

    def setEaPageSize(self, value: int):
        if value is not None:
            self.eaPageSize = value
        return self

    def getEaAddressAlignment(self) -> int:
        return self.eaAddressAlignment

    def setEaAddressAlignment(self, value: int):
        if value is not None:
            self.eaAddressAlignment = value
        return self

    def getEaReadMode(self) -> str:
        return self.eaReadMode

    def setEaReadMode(self, value: str):
        if value is not None:
            self.eaReadMode = value
        return self


class Ea(Module):
    """
    AUTOSAR EEPROM Abstraction (Ea) module.

    Provides hardware-independent access to EEPROM memory,
    abstracting the specific EEPROM device characteristics.

    Implements: SWR_EA_00001 (Ea Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "Ea")
        self.eaGeneral: EaGeneral = None
        self.logger = logging.getLogger()

    def getEaGeneral(self) -> EaGeneral:
        return self.eaGeneral

    def setEaGeneral(self, value: EaGeneral):
        if value is not None:
            self.eaGeneral = value
        return self