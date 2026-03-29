"""
Dem Model Module - Represents AUTOSAR Dem configuration.

Implements:
    - SWR_DEM_00001: Dem module model
    - SWR_DEM_00002: General configuration
"""
from typing import List, Optional
import logging
from .abstract import EcucParamConfContainerDef, EcucRefType, Module


class DemGeneral(EcucParamConfContainerDef):
    """
    General configuration for Dem module.

    Implements: SWR_DEM_00002 (General configuration)
    """

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.demDevErrorDetect: bool = None
        self.demEnabled: bool = None

    def getDemDevErrorDetect(self) -> bool:
        return self.demDevErrorDetect

    def setDemDevErrorDetect(self, value: bool):
        if value is not None:
            self.demDevErrorDetect = value
        return self

    def getDemEnabled(self) -> bool:
        return self.demEnabled

    def setDemEnabled(self, value: bool):
        if value is not None:
            self.demEnabled = value
        return self


class Dem(Module):
    """
    AUTOSAR Dem module.

    Provides Diagnostic Event Manager for diagnostic
    and error handling.

    Implements: SWR_DEM_00001 (Dem Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "Dem")
        self.demGeneral: DemGeneral = None
        self.logger = logging.getLogger()

    def getDemGeneral(self) -> DemGeneral:
        return self.demGeneral

    def setDemGeneral(self, value: DemGeneral):
        if value is not None:
            self.demGeneral = value
        return self