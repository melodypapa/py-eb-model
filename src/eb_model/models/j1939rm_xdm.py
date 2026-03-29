"""
J1939Rm Model Module - Represents AUTOSAR J1939Rm configuration.

Implements:
    - SWR_J1939RM_00001: J1939Rm module model
    - SWR_J1939RM_00002: General configuration
"""
from typing import List, Optional
import logging
from .abstract import EcucParamConfContainerDef, EcucRefType, Module


class J1939RmGeneral(EcucParamConfContainerDef):
    """
    General configuration for J1939Rm module.

    Implements: SWR_J1939RM_00002 (General configuration)
    """

    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.j1939RmDevErrorDetect: bool = None
        self.j1939RmEnabled: bool = None

    def getJ1939RmDevErrorDetect(self) -> bool:
        return self.j1939RmDevErrorDetect

    def setJ1939RmDevErrorDetect(self, value: bool):
        if value is not None:
            self.j1939RmDevErrorDetect = value
        return self

    def getJ1939RmEnabled(self) -> bool:
        return self.j1939RmEnabled

    def setJ1939RmEnabled(self, value: bool):
        if value is not None:
            self.j1939RmEnabled = value
        return self


class J1939Rm(Module):
    """
    AUTOSAR J1939Rm module.

    Provides J1939 request manager for SAE J1939 protocol.

    Implements: SWR_J1939RM_00001 (J1939Rm Module)
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, "J1939Rm")
        self.j1939RmGeneral: J1939RmGeneral = None

    def getJ1939RmGeneral(self) -> J1939RmGeneral:
        return self.j1939RmGeneral

    def setJ1939RmGeneral(self, value: J1939RmGeneral):
        if value is not None:
            self.j1939RmGeneral = value
        return self