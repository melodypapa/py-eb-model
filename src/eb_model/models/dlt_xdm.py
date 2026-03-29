"""
Dlt Model Module - Represents AUTOSAR Dlt configuration.

Implements:
    - SWR_DLT_00001: Dlt module model
    - SWR_DLT_00002: General configuration
"""
from typing import List, Optional
import logging
from .abstract import EcucParamConfContainerDef, EcucRefType, Module


class DltGeneral(EcucParamConfContainerDef):
    """
    General configuration for Dlt module.

    Implements: SWR_DLT_00002 (General configuration)
    """

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.dltDevErrorDetect: bool = None
        self.dltEnabled: bool = None

    def getDltDevErrorDetect(self) -> bool:
        return self.dltDevErrorDetect

    def setDltDevErrorDetect(self, value: bool):
        if value is not None:
            self.dltDevErrorDetect = value
        return self

    def getDltEnabled(self) -> bool:
        return self.dltEnabled

    def setDltEnabled(self, value: bool):
        if value is not None:
            self.dltEnabled = value
        return self


class Dlt(Module):
    """
    AUTOSAR Dlt module.

    Provides diagnostic log and trace interface for automotive systems.

    Implements: SWR_DLT_00001 (Dlt Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "Dlt")
        self.dltGeneral: DltGeneral = None
        self.logger = logging.getLogger()

    def getDltGeneral(self) -> DltGeneral:
        return self.dltGeneral

    def setDltGeneral(self, value: DltGeneral):
        if value is not None:
            self.dltGeneral = value
        return self