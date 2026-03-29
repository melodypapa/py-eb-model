from typing import List, Optional
import logging

from ..models.abstract import EcucParamConfContainerDef, EcucRefType, Module


class FeeGeneral(EcucParamConfContainerDef):
    """General configuration for Fee module."""

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.feeDevErrorDetect: bool = None
        self.feePageSize: int = None
        self.feeVirtualPageSize: int = None
        self.feeNumberOfSectors: int = None

    def getFeeDevErrorDetect(self) -> bool:
        return self.feeDevErrorDetect

    def setFeeDevErrorDetect(self, value: bool):
        if value is not None:
            self.feeDevErrorDetect = value
        return self

    def getFeePageSize(self) -> int:
        return self.feePageSize

    def setFeePageSize(self, value: int):
        if value is not None:
            self.feePageSize = value
        return self

    def getFeeVirtualPageSize(self) -> int:
        return self.feeVirtualPageSize

    def setFeeVirtualPageSize(self, value: int):
        if value is not None:
            self.feeVirtualPageSize = value
        return self

    def getFeeNumberOfSectors(self) -> int:
        return self.feeNumberOfSectors

    def setFeeNumberOfSectors(self, value: int):
        if value is not None:
            self.feeNumberOfSectors = value
        return self


class Fee(Module):
    """
    AUTOSAR Flash EEPROM Emulation (Fee) module.

    Simulates EEPROM behavior on Flash memory by implementing
    wear-leveling and data consistency mechanisms.

    Implements: SWR_FEE_00001 (Fee Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "Fee")
        self.feeGeneral: FeeGeneral = None
        self.logger = logging.getLogger()

    def getFeeGeneral(self) -> FeeGeneral:
        return self.feeGeneral

    def setFeeGeneral(self, value: FeeGeneral):
        if value is not None:
            self.feeGeneral = value
        return self